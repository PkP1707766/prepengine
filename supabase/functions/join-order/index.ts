// POST /functions/v1/join-order   { plan?: string }
//
// Creates a Razorpay order for the signed-in student. The amount is read from
// the `plans` table server-side, so a tampered client cannot buy access for ₹1.
import { adminClient, callerFromRequest, couponQuote } from "../_shared/supabase.ts";
import { json, preflight } from "../_shared/cors.ts";

const RZP_KEY_ID = Deno.env.get("RAZORPAY_KEY_ID") ?? "";
const RZP_KEY_SECRET = Deno.env.get("RAZORPAY_KEY_SECRET") ?? "";

Deno.serve(async (req) => {
  const pre = preflight(req);
  if (pre) return pre;
  if (req.method !== "POST") return json(req, { error: "method_not_allowed" }, 405);

  if (!RZP_KEY_ID || !RZP_KEY_SECRET) {
    console.error("Razorpay credentials are not configured");
    return json(req, { error: "payments_unconfigured" }, 503);
  }

  const user = await callerFromRequest(req);
  if (!user) return json(req, { error: "unauthorized" }, 401);

  let planCode = "prelims-2026";
  let couponCode = "";
  try {
    const body = await req.json();
    if (body && typeof body.plan === "string") planCode = body.plan;
    if (body && typeof body.coupon === "string") couponCode = body.coupon.trim();
  } catch { /* empty body is fine — use the default plan */ }

  const sb = adminClient();

  const { data: plan, error: planErr } = await sb
    .from("plans")
    .select("code, name, price_paise, currency, is_active")
    .eq("code", planCode)
    .single();

  if (planErr || !plan || !plan.is_active) {
    return json(req, { error: "plan_not_found" }, 404);
  }

  // Already own THIS bundle? Don't let them buy it twice. Checking for "any
  // active enrollment" would wrongly block a UPSC subscriber from buying BPSC.
  const { data: existing } = await sb
    .from("enrollments")
    .select("id, expires_at, status, plan_code")
    .eq("student_id", user.id)
    .eq("plan_code", plan.code)
    .eq("status", "active");
  const alreadyOwns = (existing ?? []).some(
    (e) => !e.expires_at || new Date(e.expires_at).getTime() > Date.now(),
  );
  if (alreadyOwns) return json(req, { alreadyEnrolled: true });

  // ---- Pricing. The browser sent a plan code and maybe a coupon code, and
  // nothing else. Both the list price and the discount are read here.
  let grossPaise = plan.price_paise as number;
  let discountPaise = 0;
  let couponId: string | null = null;

  if (couponCode) {
    const q = await couponQuote(sb, couponCode, plan.code, user.id);
    if (!q || !q.valid) {
      // Fail the order rather than silently charging full price — a student
      // who typed a code expects either the discount or an explanation.
      return json(req, { error: "coupon_invalid", reason: q?.reason ?? "not_found" }, 400);
    }
    grossPaise = q.gross_paise;
    discountPaise = q.discount_paise;
    couponId = q.coupon_id;
  }

  const chargePaise = grossPaise - discountPaise;

  const receipt = `jn_${user.id.slice(0, 8)}_${Date.now().toString(36)}`;
  const auth = btoa(`${RZP_KEY_ID}:${RZP_KEY_SECRET}`);

  const rzpRes = await fetch("https://api.razorpay.com/v1/orders", {
    method: "POST",
    headers: { Authorization: `Basic ${auth}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      amount: chargePaise,
      currency: plan.currency || "INR",
      receipt,
      notes: {
        user_id: user.id, plan: plan.code, email: user.email ?? "",
        coupon: couponId ? couponCode.toUpperCase() : "",
      },
    }),
  });

  if (!rzpRes.ok) {
    console.error("Razorpay order creation failed", rzpRes.status, await rzpRes.text());
    return json(req, { error: "order_failed" }, 502);
  }

  const order = await rzpRes.json();

  // Record the intent so a webhook that arrives before the browser does still
  // has a row to update.
  await sb.from("payments").upsert(
    {
      user_id: user.id,
      plan_code: plan.code,
      amount: chargePaise / 100,
      gross_paise: grossPaise,
      discount_paise: discountPaise,
      coupon_id: couponId,
      currency: plan.currency || "INR",
      status: "created",
      razorpay_order_id: order.id,
      notes: { receipt, plan: plan.code, coupon: couponId ? couponCode.toUpperCase() : null },
    },
    { onConflict: "razorpay_order_id" },
  );

  return json(req, {
    orderId: order.id,
    amount: order.amount,
    currency: order.currency,
    keyId: RZP_KEY_ID,
    planName: plan.name,
    grossPaise,
    discountPaise,
    finalPaise: chargePaise,
  });
});
