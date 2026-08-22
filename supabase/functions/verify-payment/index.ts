// POST /functions/v1/verify-payment
//   { razorpay_order_id, razorpay_payment_id, razorpay_signature }
//
// The browser calls this the instant Razorpay's checkout succeeds so the
// student is not left staring at a spinner while the webhook makes its way
// over. The signature is verified here exactly the way the webhook verifies
// its own — a forged callback grants nothing.
import {
  adminClient, callerFromRequest, grantEnrollment, redeemCoupon, creditReferralBonus,
} from "../_shared/supabase.ts";
import { json, preflight } from "../_shared/cors.ts";

const RZP_KEY_SECRET = Deno.env.get("RAZORPAY_KEY_SECRET") ?? "";

async function hmacSha256Hex(secret: string, message: string): Promise<string> {
  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  );
  const sig = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(message));
  return [...new Uint8Array(sig)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

/** Length-safe, timing-safe comparison. */
function safeEqual(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

Deno.serve(async (req) => {
  const pre = preflight(req);
  if (pre) return pre;
  if (req.method !== "POST") return json(req, { error: "method_not_allowed" }, 405);
  if (!RZP_KEY_SECRET) return json(req, { error: "payments_unconfigured" }, 503);

  const user = await callerFromRequest(req);
  if (!user) return json(req, { error: "unauthorized" }, 401);

  let payload: Record<string, string>;
  try {
    payload = await req.json();
  } catch {
    return json(req, { error: "bad_request" }, 400);
  }

  const orderId = payload.razorpay_order_id ?? "";
  const paymentId = payload.razorpay_payment_id ?? "";
  const signature = payload.razorpay_signature ?? "";
  if (!orderId || !paymentId || !signature) return json(req, { error: "bad_request" }, 400);

  const expected = await hmacSha256Hex(RZP_KEY_SECRET, `${orderId}|${paymentId}`);
  if (!safeEqual(expected, signature)) {
    console.warn("Signature mismatch for order", orderId);
    return json(req, { error: "invalid_signature" }, 400);
  }

  const sb = adminClient();

  // The order must belong to this user — the signature alone proves the payment
  // is genuine, not that it is *theirs*.
  const { data: payment } = await sb
    .from("payments")
    .select("id, user_id, plan_code, status, coupon_id, discount_paise")
    .eq("razorpay_order_id", orderId)
    .single();

  if (!payment) return json(req, { error: "order_not_found" }, 404);
  if (payment.user_id !== user.id) return json(req, { error: "forbidden" }, 403);

  await sb
    .from("payments")
    .update({
      status: "paid",
      razorpay_payment_id: paymentId,
      razorpay_signature: signature,
      verified_at: new Date().toISOString(),
    })
    .eq("id", payment.id);

  await grantEnrollment(sb, user.id, payment.plan_code ?? "prelims-2026");

  // A coupon is only spent once real money has moved and the signature has
  // verified — an abandoned checkout must never burn a use.
  await redeemCoupon(sb, payment.coupon_id, user.id, payment.id, payment.discount_paise ?? 0);

  // Whoever introduced this student gets paid — but only now, once real money
  // has actually moved and the signature has verified.
  await creditReferralBonus(sb, payment.id);

  return json(req, { ok: true });
});
