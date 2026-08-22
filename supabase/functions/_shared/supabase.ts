import { createClient, type SupabaseClient } from "https://esm.sh/@supabase/supabase-js@2";

/** Service-role client — bypasses RLS. Never expose this to the browser. */
export function adminClient(): SupabaseClient {
  return createClient(
    Deno.env.get("SUPABASE_URL")!,
    Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
    { auth: { persistSession: false } },
  );
}

/** Resolve the calling user from the Authorization header, or null. */
export async function callerFromRequest(req: Request) {
  const auth = req.headers.get("Authorization") ?? "";
  const token = auth.startsWith("Bearer ") ? auth.slice(7) : "";
  if (!token) return null;
  const sb = adminClient();
  const { data, error } = await sb.auth.getUser(token);
  if (error || !data?.user) return null;
  return data.user;
}

/** Grant (or extend) access for a student after a verified payment. */
export async function grantEnrollment(
  sb: SupabaseClient,
  userId: string,
  planCode: string,
) {
  const { data: plan } = await sb
    .from("plans")
    .select("code, duration_days")
    .eq("code", planCode)
    .single();

  const expiresAt = plan?.duration_days
    ? new Date(Date.now() + plan.duration_days * 86_400_000).toISOString()
    : null;

  await sb.from("enrollments").upsert(
    {
      student_id: userId,
      plan_code: planCode,
      batch_id: null,
      source: "purchase",
      status: "active",
      expires_at: expiresAt,
      enrolled_at: new Date().toISOString(),
    },
    { onConflict: "student_id,plan_code,batch_id" },
  );
}

/** Ask Postgres what a coupon is worth. The browser never computes this. */
export async function couponQuote(
  sb: SupabaseClient,
  code: string,
  planCode: string,
  userId: string | null,
) {
  const { data, error } = await sb.rpc("coupon_quote", {
    p_code: code,
    p_plan: planCode,
    p_user: userId,
  });
  if (error) throw error;
  const row = Array.isArray(data) ? data[0] : data;
  return row ?? null;
}

/** Record a redemption. Idempotent: safe to call from both the browser's
    confirmation and the webhook, for the same payment. */
export async function redeemCoupon(
  sb: SupabaseClient,
  couponId: string | null,
  userId: string,
  paymentId: string,
  discountPaise: number,
) {
  if (!couponId) return;
  const { error } = await sb.rpc("redeem_coupon", {
    p_coupon: couponId,
    p_user: userId,
    p_payment: paymentId,
    p_discount: discountPaise ?? 0,
  });
  if (error) console.error("redeem_coupon failed", error);
}

/** Credit the referrer's wallet for a verified paid enrollment.
 *
 *  Idempotent by construction — a partial unique index on the ledger means one
 *  referral can only ever produce one bonus line, so the browser's confirmation
 *  and the webhook can both call this for the same payment and only one wins.
 *  Never called from signup, and never reachable by a client (fraud rule 1). */
export async function creditReferralBonus(sb: SupabaseClient, paymentId: string) {
  const { data, error } = await sb.rpc("credit_referral_bonus", { p_payment: paymentId });
  if (error) {
    console.error("credit_referral_bonus failed", error);
    return null;
  }
  // Most payments have no referrer behind them; that is not worth logging.
  if (data && data !== "no_referral" && data !== "already_credited") {
    console.log("referral bonus:", data, "payment:", paymentId);
  }
  return data as string | null;
}

/** Claw the bonus back when the referred student's payment is refunded, so
 *  refund-then-keep-the-bonus does not work (fraud rule 4). Bounded by a
 *  configurable window — past it the money may already be withdrawn. */
export async function reverseReferralBonus(sb: SupabaseClient, paymentId: string) {
  const { data, error } = await sb.rpc("reverse_referral_bonus", { p_payment: paymentId });
  if (error) {
    console.error("reverse_referral_bonus failed", error);
    return null;
  }
  if (data && data !== "no_referral" && data !== "no_bonus") {
    console.log("referral reversal:", data, "payment:", paymentId);
  }
  return data as string | null;
}
