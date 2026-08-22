import { useState, useEffect, useCallback, useRef } from "react";
import { AlertCircle, CheckCircle2, Lock, LogOut, ArrowRight, ArrowLeft, Headphones, ShieldCheck, RotateCcw, Tag, X } from "lucide-react";
import { ChromeControls } from "../lib/i18n.jsx";
import { useLang } from "../lib/contexts.js";
import { DiyaLogo } from "../ui/Brand.jsx";
import { LOGIN_CSS, ContactModal } from "./authChrome.jsx";
import { getSupabase } from "../lib/supabase.js";
import { currentUser, getProfile, getPlan, myPlanCodes, checkCoupon } from "../lib/db.js";
import { Skeleton } from "../ui/Feedback.jsx";

/* ============================================================
   ENROLLMENT + PAYMENT — the paywall before the dashboard.

   Nothing about the price or the outcome is decided in this file.
   The edge function reads the amount from the `plans` table, and an
   enrollment is only ever granted after a signature the server
   verified. The browser's job is to open the checkout and wait.
   ============================================================ */

/** Load the Razorpay checkout script once, with a timeout so a blocked
    network doesn't hang the button forever. */
function loadRazorpayScript() {
  if (typeof window !== "undefined" && window.Razorpay) return Promise.resolve(true);
  return new Promise((resolve) => {
    const s = document.createElement("script");
    s.src = "https://checkout.razorpay.com/v1/checkout.js";
    const done = (ok) => { clearTimeout(timer); resolve(ok); };
    const timer = setTimeout(() => done(false), 12000);
    s.onload = () => done(true);
    s.onerror = () => done(false);
    document.body.appendChild(s);
  });
}

const DEFAULT_PLAN = "prelims-2026";

function JoinScreen({ planCode, onJoined, onLogout, onBrowse }) {
  // Which bundle the visitor picked on the storefront. Falls back to the
  // original single plan for anyone who lands here without choosing.
  const PLAN_CODE = planCode || DEFAULT_PLAN;
  const { t } = useLang();
  const [first, setFirst] = useState("");
  const [plan, setPlan] = useState(null);
  const [planErr, setPlanErr] = useState("");
  const [busy, setBusy] = useState(false);
  const [phase, setPhase] = useState("idle"); // idle | confirming | done
  const [err, setErr] = useState("");
  const [contact, setContact] = useState(false);

  /* Coupon state. `applied` holds the SERVER's quote — the browser never
     computes a discount, it only displays the one Postgres returned. */
  const [couponInput, setCouponInput] = useState("");
  const [applied, setApplied] = useState(null);
  const [couponMsg, setCouponMsg] = useState("");
  const [checking, setChecking] = useState(false);

  const joined = useRef(false);
  const finish = useCallback(() => {
    if (joined.current) return;
    joined.current = true;
    onJoined();
  }, [onJoined]);

  /* Greet the student by name, and skip the paywall entirely if they already
     have access (a refresh mid-payment must not charge them twice). */
  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const user = await currentUser();
        if (!user) return;
        const prof = await getProfile(user.id).catch(() => null);
        const nm = (prof?.full_name || "").trim() || (user.email ? user.email.split("@")[0] : "");
        if (alive) setFirst(nm.split(" ")[0]);
        // Only skip the paywall if they already own THIS bundle. Checking for
        // "any active enrollment" would stop a UPSC subscriber from ever
        // buying BPSC.
        const owned = await myPlanCodes(user.id);
        if (owned.has(PLAN_CODE)) { if (alive) finish(); return; }
      } catch (e) {
        console.error("join screen bootstrap failed", e);
      }
      try {
        const p = await getPlan(PLAN_CODE);
        if (alive) {
          if (p) setPlan(p);
          else setPlanErr("This plan is not available right now. Please contact us.");
        }
      } catch (e) {
        console.error(e);
        if (alive) setPlanErr("Couldn't load pricing. Check your connection and try again.");
      }
    })();
    return () => { alive = false; };
  }, [finish, PLAN_CODE]);

  const applyCoupon = async () => {
    const code = couponInput.trim();
    if (!code) return;
    setChecking(true); setCouponMsg("");
    try {
      const r = await checkCoupon(code, PLAN_CODE);
      if (r?.valid) {
        setApplied(r);
        setCouponMsg("");
      } else {
        setApplied(null);
        setCouponMsg(r?.message || "That code isn't recognised.");
      }
    } catch (e) {
      console.error(e);
      setApplied(null);
      setCouponMsg("Couldn't check that code just now. Try again in a moment.");
    }
    setChecking(false);
  };

  const removeCoupon = () => { setApplied(null); setCouponInput(""); setCouponMsg(""); };

  const pay = async () => {
    setErr("");
    setBusy(true);
    try {
      const sb = await getSupabase();
      const { data: { user } } = await sb.auth.getUser();
      if (!user) { setBusy(false); return setErr("Your session expired. Please sign in again."); }

      // The server decides the amount. A tampered client can only ask for a
      // plan code; it cannot name its own price.
      const { data: order, error } = await sb.functions.invoke("join-order", {
        body: { plan: PLAN_CODE, coupon: applied ? applied.code : undefined },
      });
      if (error || !order || order.error) {
        console.error("order failed", error || order);
        setBusy(false);
        if (order?.error === "coupon_invalid") {
          // The code went stale between applying and paying — someone else took
          // the last use, or it expired in the meantime.
          setApplied(null);
          setCouponMsg("That code is no longer valid. Remove it or try another.");
          return;
        }
        return setErr(order?.error === "payments_unconfigured"
          ? "Payments aren't switched on yet. Please contact us and we'll enrol you directly."
          : t("pay_failed"));
      }
      if (order.alreadyEnrolled) { setBusy(false); return finish(); }

      const ready = await loadRazorpayScript();
      if (!ready) {
        setBusy(false);
        return setErr("The payment window couldn't load. Disable any ad blocker and try again.");
      }

      const rzp = new window.Razorpay({
        key: order.keyId,
        order_id: order.orderId,
        amount: order.amount,
        currency: order.currency || "INR",
        name: "JUNOONIAS",
        description: order.planName || t("plan_name"),
        prefill: { name: first, email: user.email || "" },
        theme: { color: "#6b1a1a" },
        handler: async (resp) => {
          setPhase("confirming");
          // Confirm immediately so the student isn't stuck waiting on a
          // webhook. The webhook is still the authority; this just makes the
          // happy path instant. Both verify the same signature server-side.
          try {
            const { data: v } = await sb.functions.invoke("verify-payment", {
              body: {
                razorpay_order_id: resp.razorpay_order_id,
                razorpay_payment_id: resp.razorpay_payment_id,
                razorpay_signature: resp.razorpay_signature,
              },
            });
            if (v?.ok) { setPhase("done"); return finish(); }
          } catch (e) {
            console.error("verify-payment failed", e);
          }
          // Fall back to polling for the webhook.
          for (let i = 0; i < 12; i++) {
            await new Promise((r) => setTimeout(r, 1500));
            const owned = await myPlanCodes(user.id);
            if (owned.has(PLAN_CODE)) { setPhase("done"); return finish(); }
          }
          setBusy(false);
          setPhase("idle");
          setErr("Your payment went through but access is still activating. Refresh in a minute, or contact us and we'll sort it out immediately.");
        },
        modal: { ondismiss: () => { setBusy(false); setPhase("idle"); } },
      });

      rzp.on("payment.failed", (resp) => {
        setBusy(false);
        setPhase("idle");
        setErr(resp?.error?.description || "The payment didn't go through. No money was deducted — please try again.");
      });

      rzp.open();
    } catch (e) {
      console.error(e);
      setBusy(false);
      setErr(t("pay_failed"));
    }
  };

  const price = plan ? plan.price_paise / 100 : null;
  const mrp = plan?.mrp_paise ? plan.mrp_paise / 100 : null;
  const off = price != null && mrp && mrp > price ? Math.round((1 - price / mrp) * 100) : 0;
  const features = Array.isArray(plan?.features) && plan.features.length
    ? plan.features
    : [t("plan_tests"), t("plan_solutions"), t("plan_analytics"), t("plan_rank"), t("plan_validity")];

  return (
    <div className="jn-root">
      <style>{LOGIN_CSS}</style>
      <div className="jn-card" style={{ maxWidth: 560, gridTemplateColumns: "1fr" }}>
        <div className="jn-form" style={{ padding: "34px 32px 30px" }}>
          <div className="jn-brand-header" style={{ marginBottom: 18 }}>
            <div className="jn-brand-top">
              <DiyaLogo size={40} boxed radius={11} />
              <div>
                <div className="jn-word" style={{ color: "var(--garnet)" }}>JUNOON<b style={{ color: "var(--gold)" }}>IAS</b></div>
                <div className="jn-tag" style={{ color: "var(--sub)" }}>{t("tagline")}</div>
              </div>
            </div>
            <div className="jn-controls"><ChromeControls /></div>
          </div>

          <h2 className="jn-h">{t("join_hi")}{first ? ", " + first : ""} 🪔</h2>
          <div className="jn-hsub">{t("join_title")} — {t("join_sub")}</div>

          {phase === "confirming" && <div className="jn-banner ok"><CheckCircle2 size={17} />{t("pay_processing")}</div>}
          {phase === "done" && <div className="jn-banner ok"><CheckCircle2 size={17} />{t("pay_success")}</div>}
          {err && <div className="jn-banner err"><AlertCircle size={17} />{err}</div>}
          {planErr && <div className="jn-banner err"><AlertCircle size={17} />{planErr}</div>}

          {/* PLAN CARD */}
          <div style={{
            border: "1.5px solid var(--gold)", borderRadius: 16, padding: "20px 20px 22px", marginTop: 6,
            background: "linear-gradient(180deg, rgba(212,166,74,.10), rgba(212,166,74,.02))", position: "relative",
          }}>
            {off > 0 && (
              <div style={{ position: "absolute", top: -11, right: 16, background: "linear-gradient(135deg,#8a2222,#5b1414)",
                color: "#fff", fontSize: 11, fontWeight: 800, letterSpacing: ".06em", padding: "4px 10px", borderRadius: 999 }}>
                {off}% OFF · {t("plan_best")}
              </div>
            )}

            {!plan ? (
              <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
                <Skeleton h={18} w="60%" />
                <Skeleton h={34} w="45%" />
                {[0, 1, 2, 3, 4].map((i) => <Skeleton key={i} h={14} w="85%" />)}
              </div>
            ) : (
              <>
                <div style={{ fontFamily: "var(--font-display,serif)", fontWeight: 600, fontSize: 18, color: "var(--ink)" }}>{plan.name}</div>
                <div style={{ display: "flex", alignItems: "baseline", gap: 9, margin: "10px 0 4px" }}>
                  <span style={{ fontFamily: "var(--font-display,serif)", fontWeight: 700, fontSize: 34, color: "var(--garnet)" }}>₹{price}</span>
                  {off > 0 && <span style={{ fontSize: 16, color: "var(--sub)", textDecoration: "line-through" }}>₹{mrp}</span>}
                  <span style={{ fontSize: 12.5, color: "var(--sub)", fontWeight: 600 }}>
                    {plan.duration_days ? `for ${Math.round(plan.duration_days / 30)} months` : t("one_time")}
                  </span>
                </div>
                {plan.description && (
                  <div style={{ fontSize: 13, color: "var(--sub)", lineHeight: 1.6, marginTop: 6 }}>{plan.description}</div>
                )}
                <ul style={{ listStyle: "none", padding: 0, margin: "14px 0 0", display: "flex", flexDirection: "column", gap: 10 }}>
                  {features.map((f, i) => (
                    <li key={i} style={{ display: "flex", alignItems: "flex-start", gap: 10, fontSize: 13.5, color: "var(--ink)", fontWeight: 500 }}>
                      <CheckCircle2 size={17} style={{ color: "#1f8a4c", flex: "0 0 auto", marginTop: 2 }} /> {f}
                    </li>
                  ))}
                </ul>
              </>
            )}
          </div>

          {/* ---- COUPON ----------------------------------------------------
              The field only ever sends a code. Every number shown below comes
              back from the server, and join-order recomputes it independently
              at order time — a tampered client cannot discount itself. */}
          {plan && (
            <div className="jn-coupon">
              {!applied ? (
                <>
                  <div className="jn-coupon-row">
                    <span className="jn-coupon-ic"><Tag size={15} /></span>
                    <input
                      className="jn-input jn-coupon-input"
                      value={couponInput}
                      onChange={(e) => { setCouponInput(e.target.value.toUpperCase()); setCouponMsg(""); }}
                      onKeyDown={(e) => { if (e.key === "Enter") { e.preventDefault(); applyCoupon(); } }}
                      placeholder="Coupon code"
                      autoCapitalize="characters"
                      autoComplete="off"
                      spellCheck={false}
                      aria-label="Coupon code"
                    />
                    <button type="button" className="jn-coupon-apply"
                            onClick={applyCoupon} disabled={checking || !couponInput.trim()}>
                      {checking ? "Checking…" : "Apply"}
                    </button>
                  </div>
                  {couponMsg && (
                    <div className="jn-coupon-msg err"><AlertCircle size={14} />{couponMsg}</div>
                  )}
                </>
              ) : (
                <>
                  <div className="jn-coupon-applied">
                    <span className="jn-coupon-ic ok"><Tag size={15} /></span>
                    <div style={{ flex: 1, minWidth: 0 }}>
                      <b>{applied.code}</b>
                      <span>{applied.label} applied</span>
                    </div>
                    <button type="button" className="jn-coupon-x" onClick={removeCoupon} aria-label="Remove coupon">
                      <X size={15} />
                    </button>
                  </div>
                  <div className="jn-coupon-lines">
                    <div><span>Test series</span><span>₹{(applied.grossPaise / 100).toLocaleString("en-IN")}</span></div>
                    <div className="off"><span>Coupon {applied.code}</span><span>−₹{(applied.discountPaise / 100).toLocaleString("en-IN")}</span></div>
                    <div className="total"><span>You pay</span><span>₹{(applied.finalPaise / 100).toLocaleString("en-IN")}</span></div>
                  </div>
                </>
              )}
              {couponMsg && applied && (
                <div className="jn-coupon-msg err"><AlertCircle size={14} />{couponMsg}</div>
              )}
            </div>
          )}

          <button className="jn-cta" style={{ marginTop: 16 }} onClick={pay} disabled={busy || !plan}>
            {busy
              ? <><RotateCcw size={16} className="jn-spin" />{phase === "confirming" ? t("pay_processing") : t("please_wait")}</>
              : (<>
                  <span>
                    {t("pay_join")}
                    {applied ? " · ₹" + (applied.finalPaise / 100).toLocaleString("en-IN")
                             : price != null ? " · ₹" + price : ""}
                  </span>
                  <ArrowRight size={17} />
                </>)}
          </button>

          <div style={{ display: "flex", flexDirection: "column", gap: 6, alignItems: "center", marginTop: 12 }}>
            <div style={{ fontSize: 11.5, color: "var(--sub)", display: "flex", alignItems: "center", gap: 6 }}>
              <Lock size={12} /> {t("secure_pay")}
            </div>
            <div style={{ fontSize: 11.5, color: "var(--sub)", display: "flex", alignItems: "center", gap: 6 }}>
              <ShieldCheck size={12} /> {t("refund_note")}
            </div>
          </div>

          {onBrowse && (
            <button className="jn-link" style={{ marginTop: 14 }} onClick={onBrowse}>
              <ArrowLeft size={14} /> Compare all test series
            </button>
          )}

          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginTop: 18 }}>
            <button className="jn-link" onClick={() => setContact(true)} style={{ marginTop: 0 }}><Headphones size={14} /> {t("need_help")}</button>
            <button className="jn-link" onClick={onLogout} style={{ marginTop: 0 }}><LogOut size={14} /> {t("logout")}</button>
          </div>
        </div>
      </div>
      {contact && <ContactModal onClose={() => setContact(false)} />}
    </div>
  );
}

export default JoinScreen;
