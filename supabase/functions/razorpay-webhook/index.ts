// POST /functions/v1/razorpay-webhook
//
// The authoritative source of truth for payment state. Razorpay signs the raw
// body with the webhook secret; anything that does not verify is dropped.
// Deploy with `--no-verify-jwt` (Razorpay does not send a Supabase JWT):
//   supabase functions deploy razorpay-webhook --no-verify-jwt
import {
  adminClient, grantEnrollment, redeemCoupon, creditReferralBonus, reverseReferralBonus,
} from "../_shared/supabase.ts";

const WEBHOOK_SECRET = Deno.env.get("RAZORPAY_WEBHOOK_SECRET") ?? "";

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

function safeEqual(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

Deno.serve(async (req) => {
  if (req.method !== "POST") return new Response("method not allowed", { status: 405 });
  if (!WEBHOOK_SECRET) {
    console.error("RAZORPAY_WEBHOOK_SECRET is not set");
    return new Response("unconfigured", { status: 503 });
  }

  // Read the body as raw text — re-serialising JSON would change the bytes and
  // break the signature.
  const raw = await req.text();
  const signature = req.headers.get("x-razorpay-signature") ?? "";
  const expected = await hmacSha256Hex(WEBHOOK_SECRET, raw);
  if (!safeEqual(expected, signature)) {
    console.warn("Rejected webhook with bad signature");
    return new Response("invalid signature", { status: 400 });
  }

  let event: any;
  try {
    event = JSON.parse(raw);
  } catch {
    return new Response("bad json", { status: 400 });
  }

  const sb = adminClient();
  const entity = event?.payload?.payment?.entity ?? {};
  const orderId: string | undefined = entity.order_id;
  const paymentId: string | undefined = entity.id;

  if (!orderId) return new Response("ignored", { status: 200 });

  const { data: payment } = await sb
    .from("payments")
    .select("id, user_id, plan_code, status, coupon_id, discount_paise")
    .eq("razorpay_order_id", orderId)
    .single();

  // A payment we have no record of (e.g. created outside the app) is logged and
  // acknowledged — returning non-200 would make Razorpay retry forever.
  if (!payment) {
    console.warn("Webhook for unknown order", orderId, event.event);
    return new Response("ok", { status: 200 });
  }

  switch (event.event) {
    case "payment.captured":
    case "order.paid": {
      if (payment.status !== "paid") {
        await sb
          .from("payments")
          .update({
            status: "paid",
            razorpay_payment_id: paymentId ?? null,
            method: entity.method ?? null,
            verified_at: new Date().toISOString(),
          })
          .eq("id", payment.id);
      }
      if (payment.user_id) {
        await grantEnrollment(sb, payment.user_id, payment.plan_code ?? "prelims-2026");
        // Idempotent — the browser's own confirmation may already have done
        // this for the same payment.
        await redeemCoupon(sb, payment.coupon_id, payment.user_id, payment.id, payment.discount_paise ?? 0);
        // Idempotent too — whichever of the webhook and the browser arrives
        // second gets 'already_credited' and changes nothing.
        await creditReferralBonus(sb, payment.id);
        await sb.from("notifications").insert({
          user_id: payment.user_id,
          kind: "success",
          title: "Payment received — you're in! 🪔",
          body: "Your full access is active. Every mock test and analytics report is unlocked.",
          link: "/tests",
        });
      }
      break;
    }
    case "payment.failed": {
      await sb
        .from("payments")
        .update({
          status: "failed",
          razorpay_payment_id: paymentId ?? null,
          failure_reason: entity.error_description ?? entity.error_reason ?? null,
        })
        .eq("id", payment.id);
      break;
    }
    case "refund.created":
    case "refund.processed": {
      await sb.from("payments").update({ status: "refunded" }).eq("id", payment.id);
      if (payment.user_id) {
        await sb
          .from("enrollments")
          .update({ status: "refunded" })
          .eq("student_id", payment.user_id)
          .eq("plan_code", payment.plan_code ?? "prelims-2026");
        // Take the referrer's bonus back with it.
        await reverseReferralBonus(sb, payment.id);
      }
      break;
    }
    default:
      // Acknowledge everything else so Razorpay stops retrying.
      break;
  }

  return new Response("ok", { status: 200 });
});
