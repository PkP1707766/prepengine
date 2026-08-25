import { useState } from "react";
import { AlertCircle, CheckCircle2, Eye, EyeOff, ArrowLeft, User, Mail, Phone, ArrowRight, Headphones } from "lucide-react";
import { ChromeControls } from "../lib/i18n.jsx";
import { useLang } from "../lib/contexts.js";
import { DiyaLogo } from "../ui/Brand.jsx";
import { LOGIN_CSS, Mandala, ContactModal } from "./authChrome.jsx";
import { getSupabase } from "../lib/supabase.js";
import { ensureProfile } from "../lib/db.js";

/* Supabase returns developer-facing strings. Students should see plain
   language, and we should never leak whether an email exists. */
function friendlyAuthError(error, t) {
  const msg = String(error?.message || "").toLowerCase();
  const status = error?.status;
  if (status === 429 || msg.includes("rate limit") || msg.includes("too many")) return t("err_rate");
  if (msg.includes("invalid login") || msg.includes("invalid credentials")) return t("err_bad_login");
  if (msg.includes("email not confirmed")) return t("ok_check_email");
  if (msg.includes("already registered") || msg.includes("already been registered")) {
    return "An account with this email already exists. Try signing in instead.";
  }
  if (msg.includes("password should be") || msg.includes("weak")) return t("err_pwd_short");
  if (msg.includes("failed to fetch") || msg.includes("network")) return t("err_network");
  if (msg.includes("token has expired") || msg.includes("invalid otp") || msg.includes("expired")) return t("err_bad_otp");
  return error?.message || t("err_network");
}

/* A password that survives a dictionary attack, explained honestly. */
function passwordIssue(pwd) {
  if (pwd.length < 8) return "short";
  if (!/[0-9]/.test(pwd) && !/[^A-Za-z0-9]/.test(pwd)) return "weak";
  return null;
}

function LoginScreen({ onStudent, onAdmin, onBack }) {
  const { t } = useLang();
  /* mode: "login" | "signup" | "phone" | "otp" | "forgot" */
  const [mode, setMode] = useState("login");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [fullName, setFullName] = useState("");
  const [phone, setPhone] = useState("");
  const [otp, setOtp] = useState("");
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState("");
  const [ok, setOk] = useState("");
  const [showPwd, setShowPwd] = useState(false);
  const [contact, setContact] = useState(false);

  const reset = (m) => { setMode(m); setErr(""); setOk(""); };

  const routeByRole = async (sb) => {
    const { data: { user } } = await sb.auth.getUser();
    if (!user) return;
    // ensureProfile also backfills a profile row for accounts created before
    // the signup trigger existed, so nobody lands in a roleless limbo.
    const profile = await ensureProfile(user).catch(() => null);
    if (profile?.role === "admin") onAdmin(); else onStudent();
  };

  const doLogin = async () => {
    setErr(""); setOk("");
    if (!email.trim()) return setErr(t("err_email_req"));
    if (!password) return setErr(t("err_pwd_req"));
    setLoading(true);
    try {
      const sb = await getSupabase();
      const { error } = await sb.auth.signInWithPassword({ email: email.trim().toLowerCase(), password });
      if (error) { setLoading(false); return setErr(friendlyAuthError(error, t)); }
      await routeByRole(sb);
    } catch (e) { setErr(friendlyAuthError(e, t)); }
    setLoading(false);
  };

  const doSignup = async () => {
    setErr(""); setOk("");
    if (!fullName.trim()) return setErr(t("err_name_req"));
    if (!email.trim()) return setErr(t("err_email_req"));
    if (!/^\S+@\S+\.\S+$/.test(email.trim())) return setErr("That doesn't look like a valid email address.");
    const issue = passwordIssue(password);
    if (issue === "short") return setErr(t("err_pwd_short"));
    if (issue === "weak") return setErr(t("err_pwd_weak"));
    setLoading(true);
    try {
      const sb = await getSupabase();
      const { data, error } = await sb.auth.signUp({
        email: email.trim().toLowerCase(), password,
        options: { data: { full_name: fullName.trim() }, emailRedirectTo: window.location.origin },
      });
      if (error) { setLoading(false); return setErr(friendlyAuthError(error, t)); }
      // With email confirmation on, Supabase returns a user but no session.
      if (data?.session) { await routeByRole(sb); }
      else { setOk(t("ok_check_email")); setPassword(""); reset("login"); setOk(t("ok_check_email")); }
    } catch (e) { setErr(friendlyAuthError(e, t)); }
    setLoading(false);
  };

  const sendReset = async () => {
    setErr(""); setOk("");
    if (!email.trim()) return setErr(t("err_email_req"));
    setLoading(true);
    try {
      const sb = await getSupabase();
      await sb.auth.resetPasswordForEmail(email.trim().toLowerCase(), { redirectTo: window.location.origin });
      // Always the same message, whether or not the address is registered —
      // otherwise this page becomes an account-enumeration oracle.
      setOk(t("ok_reset_sent"));
    } catch (e) { setErr(friendlyAuthError(e, t)); }
    setLoading(false);
  };

  const sendOtp = async () => {
    setErr(""); setOk("");
    let p = phone.trim().replace(/\s/g, "");
    if (!p.startsWith("+")) p = "+91" + p.replace(/^0/, "");
    if (p.replace(/\D/g, "").length < 10) return setErr(t("err_phone"));
    setLoading(true);
    try {
      const sb = await getSupabase();
      const { error } = await sb.auth.signInWithOtp({ phone: p });
      if (error) { setLoading(false); return setErr(friendlyAuthError(error, t)); }
      setPhone(p); setOk(t("ok_otp_sent") + " " + p); setMode("otp");
    } catch (e) { setErr(String(e.message || e)); }
    setLoading(false);
  };

  const verifyOtp = async () => {
    setErr(""); setOk("");
    if (otp.replace(/\D/g, "").length < 4) return setErr(t("err_otp"));
    setLoading(true);
    try {
      const sb = await getSupabase();
      const { error } = await sb.auth.verifyOtp({ phone, token: otp, type: "sms" });
      if (error) { setLoading(false); return setErr(friendlyAuthError(error, t)); }
      await routeByRole(sb);
    } catch (e) { setErr(friendlyAuthError(e, t)); }
    setLoading(false);
  };

  const google = async () => {
    setErr("");
    try {
      const sb = await getSupabase();
      const { error } = await sb.auth.signInWithOAuth({
        provider: "google",
        options: { redirectTo: window.location.origin },
      });
      if (error) setErr(friendlyAuthError(error, t));
    } catch (e) { setErr(friendlyAuthError(e, t)); }
  };

  const onEnter = (fn) => (e) => { if (e.key === "Enter") fn(); };
  const isEmail = mode === "login" || mode === "signup";

  return (
    <div className="jn-root">
      <style>{LOGIN_CSS}</style>

      <div className="jn-card">
        {/* BRAND */}
        <div className="jn-brand">
          <Mandala />
          <div className="jn-brand-header">
            <div className="jn-brand-top">
              <DiyaLogo size={44} boxed radius={12} />
              <div>
                <div className="jn-word">JUNOON<b>IAS</b></div>
                <div className="jn-tag">{t("tagline")}</div>
              </div>
            </div>
            <div className="jn-controls"><ChromeControls light /></div>
          </div>
          <div className="jn-intro">{t("intro_sub")}</div>
          <ul className="jn-points">
            <li><CheckCircle2 size={17} /> {t("feat_tests")}</li>
            <li><CheckCircle2 size={17} /> {t("feat_analytics")}</li>
            <li><CheckCircle2 size={17} /> {t("feat_rank")}</li>
            <li><CheckCircle2 size={17} /> {t("feat_material")}</li>
          </ul>
          <div className="jn-trust">
            <div className="jn-trust-avatars">
              <span>अ</span><span>र</span><span>प</span>
            </div>
            {/* This said "1000+ aspirants" against 12 registered accounts —
                a false claim on a site that takes payments. Replaced with
                something checkable. */}
            <div className="jn-trust-text"><b>UPSC · BPSC · UPPCS</b> — three exams, one platform</div>
          </div>

          <div className="jn-shloka">
            <div className="dev">तमसो मा ज्योतिर्गमय</div>
            <div className="tr">"{t("shloka_en")}"</div>
            <div className="src">Bṛhadāraṇyaka Upaniṣad · I.3.28</div>
          </div>
          <div className="jn-foot">{t("lg_statepsc")}</div>
        </div>

        {/* FORM */}
        <div className="jn-form">
          {mode === "login" && (<><h2 className="jn-h">{t("welcome_back")}</h2><div className="jn-hsub">{t("signin_sub")}</div></>)}
          {mode === "signup" && (<><h2 className="jn-h">{t("create_acc")}</h2><div className="jn-hsub">{t("create_sub")}</div></>)}
          {mode === "phone" && (<><h2 className="jn-h">{t("phone_login")}</h2><div className="jn-hsub">{t("phone_sub")}</div></>)}
          {mode === "otp" && (<><h2 className="jn-h">{t("verify_otp")}</h2><div className="jn-hsub">{ok || t("phone_sub")}</div></>)}
          {mode === "forgot" && (<><h2 className="jn-h">{t("reset_title")}</h2><div className="jn-hsub">{t("reset_sub")}</div></>)}

          {isEmail && (
            <div className="jn-tabs">
              <button className={mode === "login" ? "on" : ""} onClick={() => reset("login")}><Mail size={15} /> {t("tab_signin")}</button>
              <button className={mode === "signup" ? "on" : ""} onClick={() => reset("signup")}><User size={15} /> {t("tab_signup")}</button>
            </div>
          )}

          {ok && mode !== "otp" && <div className="jn-banner ok"><CheckCircle2 size={17} />{ok}</div>}
          {err && <div className="jn-banner err"><AlertCircle size={17} />{err}</div>}

          {mode === "signup" && (
            <div className="jn-field">
              <label>{t("full_name")} <span>*</span></label>
              <input className="jn-input" value={fullName} onChange={(e) => setFullName(e.target.value)}
                placeholder={t("full_name")} onKeyDown={onEnter(doSignup)} />
            </div>
          )}

          {isEmail && (
            <>
              <div className="jn-field">
                <label>{t("email_addr")} <span>*</span></label>
                <input className="jn-input" type="email" value={email} onChange={(e) => setEmail(e.target.value)}
                  placeholder="you@gmail.com" onKeyDown={onEnter(mode === "login" ? doLogin : doSignup)} />
              </div>
              <div className="jn-field">
                <label>{t("password")} <span>*</span></label>
                <div style={{ position: "relative" }}>
                  <input className="jn-input" type={showPwd ? "text" : "password"} value={password}
                    onChange={(e) => setPassword(e.target.value)} style={{ paddingRight: 44 }}
                    placeholder={mode === "signup" ? t("min8") : "••••••••"}
                    onKeyDown={onEnter(mode === "login" ? doLogin : doSignup)} />
                  <button className="jn-eye" onClick={() => setShowPwd(!showPwd)} aria-label={t("lg_showpwd")} type="button">
                    {showPwd ? <EyeOff size={18} /> : <Eye size={18} />}
                  </button>
                </div>
                {mode === "signup"
                  ? <div className="jn-hint">{t("pwd_hint")}</div>
                  : <button type="button" className="jn-link" style={{ marginTop: 6, fontSize: 12.5 }}
                            onClick={() => reset("forgot")}>{t("forgot_pwd")}</button>}
              </div>
              <button className="jn-cta" onClick={mode === "login" ? doLogin : doSignup} disabled={loading}>
                {loading ? t("please_wait") : (<><span>{mode === "login" ? t("btn_signin") : t("btn_create")}</span><ArrowRight size={17} /></>)}
              </button>
              <div className="jn-div">{t("or")}</div>
              <button className="jn-alt jn-google" onClick={google}>
                <svg className="jn-gicon" width="18" height="18" viewBox="0 0 48 48">
                  <path fill="#FFC107" d="M43.6 20.5H42V20H24v8h11.3C33.7 32.4 29.3 35 24 35c-6.1 0-11-4.9-11-11s4.9-11 11-11c2.8 0 5.3 1 7.3 2.8l5.7-5.7C33.6 6.5 29 4.5 24 4.5 13.2 4.5 4.5 13.2 4.5 24S13.2 43.5 24 43.5 43.5 34.8 43.5 24c0-1.2-.1-2.4-.3-3.5z" />
                  <path fill="#FF3D00" d="M6.3 14.7l6.6 4.8C14.6 15.9 18.9 13 24 13c2.8 0 5.3 1 7.3 2.8l5.7-5.7C33.6 6.5 29 4.5 24 4.5c-7.7 0-14.4 4.4-17.7 10.2z" />
                  <path fill="#4CAF50" d="M24 43.5c5 0 9.6-1.9 13-5.1l-6-5.1C29.1 34.7 26.7 35.5 24 35.5c-5.3 0-9.7-3.4-11.3-8l-6.6 5.1C9.5 39 16.2 43.5 24 43.5z" />
                  <path fill="#1976D2" d="M43.6 20.5H42V20H24v8h11.3c-.8 2.3-2.3 4.2-4.2 5.5l6 5.1C40.3 36 43.5 30.6 43.5 24c0-1.2-.1-2.4-.3-3.5z" />
                </svg>
                {t("google")}
              </button>
              <button className="jn-alt" style={{ marginTop: 10 }} onClick={() => reset("phone")}>
                <Phone size={16} /> {t("use_phone")}
              </button>
              {mode === "signup" && (
                <div style={{ fontSize: 11.5, color: "var(--sub)", textAlign: "center", marginTop: 14, lineHeight: 1.6 }}>
                  {t("agree_terms")}
                </div>
              )}
            </>
          )}

          {mode === "forgot" && (
            <>
              <div className="jn-field">
                <label htmlFor="jn-reset-email">{t("email_addr")} <span>*</span></label>
                <input id="jn-reset-email" className="jn-input" type="email" autoComplete="email" value={email}
                  onChange={(e) => setEmail(e.target.value)} placeholder="you@gmail.com" onKeyDown={onEnter(sendReset)} />
              </div>
              <button className="jn-cta" onClick={sendReset} disabled={loading}>
                {loading ? t("please_wait") : (<><span>{t("btn_send_reset")}</span><ArrowRight size={17} /></>)}
              </button>
              <button className="jn-link" onClick={() => reset("login")}><ArrowLeft size={15} /> {t("use_email")}</button>
            </>
          )}

          {mode === "phone" && (
            <>
              <div className="jn-field">
                <label>{t("phone_no")} <span>*</span></label>
                <input className="jn-input" type="tel" value={phone} onChange={(e) => setPhone(e.target.value)}
                  placeholder="+91 98765 43210" onKeyDown={onEnter(sendOtp)} />
                <div className="jn-hint">{t("phone_hint")}</div>
              </div>
              <button className="jn-cta" onClick={sendOtp} disabled={loading}>
                {loading ? t("please_wait") : (<><span>{t("btn_send_otp")}</span><ArrowRight size={17} /></>)}
              </button>
              <button className="jn-link" onClick={() => reset("login")}><ArrowLeft size={15} /> {t("use_email")}</button>
            </>
          )}

          {mode === "otp" && (
            <>
              <div className="jn-field">
                <label>{t("otp_code")} <span>*</span></label>
                <input className="jn-input" type="number" inputMode="numeric" value={otp}
                  onChange={(e) => setOtp(e.target.value)} placeholder="123456" maxLength={6}
                  style={{ letterSpacing: ".3em", fontSize: 20, fontWeight: 700, textAlign: "center" }}
                  onKeyDown={onEnter(verifyOtp)} />
              </div>
              <button className="jn-cta" onClick={verifyOtp} disabled={loading}>
                {loading ? t("please_wait") : (<><span>{t("btn_verify")}</span><ArrowRight size={17} /></>)}
              </button>
              <button className="jn-link" onClick={() => reset("phone")}><ArrowLeft size={15} /> {t("resend")}</button>
            </>
          )}

          <div className="jn-foothelp">
            {onBack && (
              <button onClick={onBack} style={{ marginBottom: 8 }}>
                <ArrowLeft size={14} /> {t("lg_back_tests")}
              </button>
            )}
            <button onClick={() => setContact(true)}><Headphones size={14} /> {t("need_help")} {t("contact_us")}</button>
          </div>
        </div>
      </div>

      {contact && <ContactModal onClose={() => setContact(false)} />}
    </div>
  );
}

export default LoginScreen;
