// POST /functions/v1/coupon-check   { code, plan }
//
// Tells the checkout what a code is worth, so the student sees the discounted
// price before paying. It returns the *same numbers* join-order will use,
// because both call the same coupon_quote() function in Postgres — the price
// shown and the price charged cannot drift apart.
//
// The coupons table itself is admin-only readable. A student learns a code's
// value by submitting it here, never by listing them.
import { adminClient, callerFromRequest, couponQuote } from "../_shared/supabase.ts";
import { json, preflight } from "../_shared/cors.ts";

/** Why a code was rejected, in language a student can act on. */
const REASONS: Record<string, string> = {
  not_found:     "That code isn't recognised. Check the spelling and try again.",
  inactive:      "That code is no longer active.",
  not_started:   "That code isn't live yet.",
  expired:       "That code has expired.",
  exhausted:     "That code has been fully claimed.",
  wrong_plan:    "That code doesn't apply to this test series.",
  below_minimum: "That code needs a higher order value.",
  already_used:  "You've already used this code.",
  plan_not_found:"This test series is not available right now.",
};

Deno.serve(async (req) => {
  const pre = preflight(req);
  if (pre) return pre;
  if (req.method !== "POST") return json(req, { error: "method_not_allowed" }, 405);

  const user = await callerFromRequest(req);
  if (!user) return json(req, { error: "unauthorized" }, 401);

  let body: { code?: string; plan?: string };
  try { body = await req.json(); } catch { return json(req, { error: "bad_request" }, 400); }

  const code = String(body.code ?? "").trim();
  const plan = String(body.plan ?? "").trim();
  if (!code || !plan) return json(req, { error: "bad_request" }, 400);
  if (code.length > 64) return json(req, { valid: false, message: REASONS.not_found });

  try {
    const q = await couponQuote(adminClient(), code, plan, user.id);
    if (!q) return json(req, { valid: false, message: REASONS.not_found });

    if (!q.valid) {
      return json(req, { valid: false, reason: q.reason, message: REASONS[q.reason] ?? REASONS.not_found });
    }
    return json(req, {
      valid: true,
      code: q.code,
      label: q.label,
      grossPaise: q.gross_paise,
      discountPaise: q.discount_paise,
      finalPaise: q.final_paise,
    });
  } catch (e) {
    console.error("coupon-check failed", e);
    return json(req, { error: "server_error" }, 500);
  }
});
