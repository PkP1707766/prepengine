
import { Mail, MapPin } from "lucide-react";
import { useLang } from "../lib/contexts.js";

/* ============================================================
   AUTH SCREEN  —  JUNOONIAS  (bilingual · light/dark · responsive)
   ============================================================ */
const LOGIN_CSS = `
.jn-root{ --bg1:#6b1a1a; --bg2:#3a0e0e; --panel:linear-gradient(155deg,#7a1f1f 0%,#3a0e0e 100%);
  --surface:#fffdf7; --ink:#2a1810; --sub:#7a6450; --line:#ecdfc4; --inbg:#fbf6ea; --inbd:#e6d6b2;
  --gold:#b8923a; --gold2:#d4a64a; --garnet:#6b1a1a; --cream:#fdf6e3;
  font-family:var(--font-body,system-ui);
  min-height:100vh; min-height:100dvh; display:grid; place-items:center; padding:20px; color:var(--ink);
  background:
    radial-gradient(120% 90% at 50% -10%, rgba(212,166,74,.18), transparent 60%),
    radial-gradient(90% 70% at 50% 120%, rgba(107,26,26,.20), transparent 60%),
    linear-gradient(160deg,#f6ead0 0%, #efddbb 45%, #e7cfa6 100%);
}
[data-theme="dark"] .jn-root{
  --surface:#241318; --ink:#f3e6cf; --sub:#bcaa8c; --line:#3a2630; --inbg:#1c0f13; --inbd:#43232c;
  background:
    radial-gradient(120% 90% at 50% -10%, rgba(184,146,58,.16), transparent 60%),
    radial-gradient(90% 80% at 50% 120%, rgba(58,14,14,.55), transparent 60%),
    linear-gradient(160deg,#1a0e0e 0%, #25110f 50%, #160a0c 100%);
}
.jn-root *{box-sizing:border-box}
.jn-root :where(button){font-family:inherit;cursor:pointer;border:none;background:none}
.jn-topbar{display:none}

.jn-card{display:grid;grid-template-columns:1.05fr 1fr;width:100%;max-width:940px;
  background:var(--surface);border-radius:22px;overflow:hidden;
  box-shadow:0 30px 90px rgba(58,14,14,.34), 0 2px 0 rgba(255,235,190,.5) inset;
  animation:jnCardIn .55s cubic-bezier(.16,1,.3,1);}
@keyframes jnCardIn{from{opacity:0;transform:translateY(18px) scale(.98)}to{opacity:1;transform:translateY(0) scale(1)}}

/* ---- brand panel ---- */
.jn-brand{position:relative;background:var(--panel);color:#fdeecb;padding:42px 36px;display:flex;flex-direction:column;overflow:hidden}
.jn-scene{position:absolute;inset:0;width:100%;height:100%;opacity:.9;pointer-events:none}
.jn-mandala{position:absolute;inset:0;opacity:.14;pointer-events:none}
.jn-brand-header{display:flex;align-items:center;justify-content:space-between;gap:12px;position:relative;z-index:2}
.jn-brand-top{display:flex;align-items:center;gap:14px;flex:1;min-width:0}
.jn-controls{display:flex;gap:7px;flex-shrink:0}
.jn-word{font-family:var(--font-display,serif);font-weight:700;font-size:22px;letter-spacing:.04em;line-height:1;white-space:nowrap}
.jn-word b{color:var(--gold2)}
.jn-tag{font-family:var(--font-quote,serif);font-style:italic;font-size:13px;color:#e7c98e;margin-top:3px;letter-spacing:.02em}
.jn-intro{position:relative;z-index:1;margin-top:22px;font-size:14px;line-height:1.6;color:#f2ddb6;max-width:34ch}
.jn-points{list-style:none;padding:0;margin:22px 0 0;display:flex;flex-direction:column;gap:13px;position:relative;z-index:1}
.jn-points li{display:flex;align-items:center;gap:11px;font-size:13.5px;color:#f3e2bd;font-weight:500}
.jn-points li svg{color:var(--gold2);flex:0 0 auto}
.jn-shloka{position:relative;z-index:1;margin-top:26px;padding:16px 18px;border-radius:14px;
  background:rgba(0,0,0,.22);border:1px solid rgba(212,166,74,.28)}
.jn-shloka .dev{font-family:var(--font-deva,serif);font-size:19px;line-height:1.5;color:#ffe6b0}
.jn-shloka .tr{font-family:var(--font-quote,serif);font-style:italic;font-size:13.5px;color:#dcc093;margin-top:7px}
.jn-shloka .src{font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:#b58c54;margin-top:8px;font-weight:700}
.jn-foot{margin-top:auto;padding-top:26px;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:#c79a5c;font-weight:700;position:relative;z-index:1}
.jn-trust{display:flex;align-items:center;gap:10px;margin-top:20px;padding:12px 14px;border-radius:13px;
  background:rgba(212,166,74,.12);border:1px solid rgba(212,166,74,.25);position:relative;z-index:1}
.jn-trust-avatars{display:flex;flex-shrink:0}
.jn-trust-avatars span{width:26px;height:26px;border-radius:50%;background:linear-gradient(140deg,var(--gold2),var(--gold));
  border:2px solid #5b1414;margin-left:-9px;display:grid;place-items:center;font-size:10px;font-weight:800;color:#4a1010}
.jn-trust-avatars span:first-child{margin-left:0}
.jn-trust-text{font-size:12px;color:#f3e2bd;line-height:1.35}
.jn-trust-text b{color:var(--gold2);font-weight:800}

/* ---- form panel ---- */
.jn-form{padding:40px 36px;display:flex;flex-direction:column;min-width:0}
.jn-h{margin:0;font-family:var(--font-display,serif);font-weight:600;font-size:23px;letter-spacing:.01em;color:var(--ink)}
.jn-hsub{margin:7px 0 22px;font-size:13.5px;color:var(--sub)}
.jn-tabs{display:flex;gap:8px;margin-bottom:20px;background:var(--inbg);padding:5px;border-radius:12px;border:1px solid var(--line)}
.jn-tabs button{flex:1;display:flex;align-items:center;justify-content:center;gap:7px;padding:10px;border-radius:9px;
  font-size:13.5px;font-weight:700;color:var(--sub);transition:all .2s cubic-bezier(.4,0,.2,1)}
.jn-tabs button.on{background:var(--surface);color:var(--garnet);box-shadow:0 2px 8px rgba(58,14,14,.12)}
.jn-tabs button:not(.on):hover{color:var(--garnet)}
.jn-field{margin-bottom:14px}
.jn-field label{display:block;font-size:12.5px;font-weight:700;color:var(--ink);margin-bottom:6px}
.jn-field label span{color:#c0392b}
.jn-input{width:100%;padding:12px 13px;border:1.5px solid var(--inbd);border-radius:10px;font-size:14.5px;outline:none;
  color:var(--ink);background:var(--inbg);transition:.14s;font-family:inherit}
.jn-input::placeholder{color:#b6a888}
.jn-input:focus{border-color:var(--gold);box-shadow:0 0 0 3px rgba(184,146,58,.16);background:var(--surface)}
.jn-hint{font-size:11.5px;color:#a8997c;margin-top:5px}
.jn-eye{position:absolute;right:10px;top:50%;transform:translateY(-50%);color:#b0a07e;padding:5px}
.jn-cta{display:flex;align-items:center;justify-content:center;gap:9px;width:100%;
  color:#fff !important;font-weight:700;font-size:15px;
  padding:13px;border-radius:11px;margin-top:6px;transition:.16s;border:none;
  background:linear-gradient(135deg,#8a2222 0%,#5b1414 100%) !important;
  box-shadow:0 8px 24px rgba(91,20,20,.38) !important;cursor:pointer}
.jn-cta:hover:not(:disabled){filter:brightness(1.08);transform:translateY(-2px);box-shadow:0 12px 30px rgba(91,20,20,.46) !important}
.jn-cta:active:not(:disabled){transform:translateY(0)}
.jn-cta:disabled{opacity:.6;cursor:default}
.jn-div{display:flex;align-items:center;gap:12px;margin:18px 0;color:#b6a888;font-size:12px;font-weight:600}
.jn-div::before,.jn-div::after{content:"";flex:1;height:1px;background:var(--line)}
.jn-alt{display:flex;align-items:center;justify-content:center;gap:10px;width:100%;background:var(--surface);
  border:1.5px solid var(--inbd);font-weight:700;font-size:14px;padding:12px;border-radius:11px;color:var(--ink);transition:.14s}
.jn-alt:hover{background:var(--inbg);border-color:var(--gold)}
.jn-gicon{flex-shrink:0}
.jn-google{position:relative;overflow:hidden}
.jn-google:hover{border-color:#4285F4;box-shadow:0 4px 14px rgba(66,133,244,.15)}
.jn-link{font-size:13px;color:var(--sub);display:inline-flex;align-items:center;gap:6px;margin-top:14px;font-weight:600}
.jn-link:hover{color:var(--garnet)}
.jn-foothelp{margin-top:20px;text-align:center}
.jn-foothelp button{font-size:12.5px;color:var(--gold);font-weight:700;display:inline-flex;align-items:center;gap:6px}
.jn-staff{margin-top:10px;text-align:center;font-size:11.5px;color:#a8997c}
.jn-banner{display:flex;align-items:center;gap:9px;border-radius:10px;padding:11px 13px;margin-bottom:14px;font-size:13px;font-weight:600;
  animation:jnBannerIn .3s ease}
@keyframes jnBannerIn{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:translateY(0)}}
.jn-banner.ok{background:#e8f6ee;color:#1a6b3c;border:1px solid #c9e8d5}
.jn-banner.err{background:#fbeaea;color:#a32f24;border:1px solid #f1cccc}
[data-theme="dark"] .jn-banner.ok{background:#13301f;color:#7fe0a3;border-color:#1f5236}
[data-theme="dark"] .jn-banner.err{background:#3a1614;color:#f0a79b;border-color:#5a2420}

/* ---- responsive ---- */
@media (max-width:880px){
  .jn-card{grid-template-columns:1fr;max-width:480px}
  .jn-brand{padding:20px 22px 18px}
  .jn-intro,.jn-points{display:none}
  .jn-shloka{display:none}
  .jn-foot{display:none}
  .jn-word{font-size:20px}
  .jn-tag{font-size:12px}
}
@media (max-width:520px){
  .jn-root{padding:0}
  .jn-card{border-radius:0;min-height:100vh;min-height:100dvh;max-width:100%}
  .jn-form{padding:24px 20px 40px}
  .jn-brand{padding:16px 18px 14px}
  .jn-word{font-size:18px}
  .jn-controls button{font-size:11px;padding:5px 9px}
}

/* ---- contact modal ---- */
.jn-scrim{position:fixed;inset:0;background:rgba(30,8,8,.55);backdrop-filter:blur(3px);display:grid;place-items:center;z-index:50;padding:18px}
.jn-modal{background:var(--surface);color:var(--ink);width:100%;max-width:400px;border-radius:18px;padding:26px 24px;
  box-shadow:0 30px 80px rgba(0,0,0,.4);border:1px solid var(--line)}
.jn-modal h3{margin:0 0 4px;font-family:var(--font-display,serif);font-weight:600;font-size:19px}
.jn-modal p{margin:0 0 16px;font-size:13px;color:var(--sub)}
.jn-crow{display:flex;align-items:center;gap:12px;padding:12px;border:1px solid var(--line);border-radius:12px;margin-bottom:10px;
  background:var(--inbg);transition:.14s;text-decoration:none;color:var(--ink)}
.jn-crow:hover{border-color:var(--gold)}
.jn-cic{width:38px;height:38px;border-radius:10px;display:grid;place-items:center;flex:0 0 auto;background:linear-gradient(150deg,#7a1f1f,#3a0e0e);color:#f4cf86}
.jn-cmeta b{display:block;font-size:13.5px;font-weight:700}
.jn-cmeta span{font-size:12px;color:var(--sub)}
.jn-social{display:flex;gap:10px;justify-content:center;margin-top:14px}
.jn-social a{width:40px;height:40px;border-radius:11px;display:grid;place-items:center;background:var(--inbg);border:1px solid var(--line);color:var(--garnet)}
.jn-social a:hover{border-color:var(--gold);color:var(--gold)}

/* ---- coupon field (checkout) ---- */
.jn-coupon{margin-top:18px;border:1px dashed var(--gold,#d4a64a);border-radius:14px;padding:12px}
.jn-coupon-row{display:flex;align-items:center;gap:8px}
.jn-coupon-ic{width:32px;height:32px;flex:0 0 auto;border-radius:9px;display:grid;place-items:center;
  background:rgba(212,166,74,.16);color:var(--gold,#d4a64a)}
.jn-coupon-ic.ok{background:rgba(31,138,76,.14);color:#1f8a4c}
.jn-coupon-input{flex:1;min-width:0;margin:0;letter-spacing:.08em;font-weight:700;text-transform:uppercase}
.jn-coupon-apply{flex:0 0 auto;background:var(--garnet,#6b1a1a);color:#fff;border:0;font:inherit;
  font-size:13.5px;font-weight:700;padding:11px 16px;border-radius:10px;cursor:pointer;min-height:44px}
.jn-coupon-apply:disabled{opacity:.5;cursor:not-allowed}
.jn-coupon-msg{display:flex;align-items:flex-start;gap:7px;font-size:12.5px;line-height:1.5;margin-top:9px}
.jn-coupon-msg.err{color:#c0392b}
.jn-coupon-msg svg{flex:0 0 auto;margin-top:1px}
.jn-coupon-applied{display:flex;align-items:center;gap:10px}
.jn-coupon-applied b{display:block;font-size:14px;letter-spacing:.06em;color:var(--ink,#2e1c12)}
.jn-coupon-applied span{display:block;font-size:12.5px;color:#1f8a4c;font-weight:600;margin-top:1px}
.jn-coupon-x{flex:0 0 auto;width:32px;height:32px;border-radius:9px;border:1px solid var(--line,#e8dcc0);
  background:none;color:var(--sub,#7a6450);cursor:pointer;display:grid;place-items:center}
.jn-coupon-x:hover{border-color:#c0392b;color:#c0392b}
.jn-coupon-lines{margin-top:12px;padding-top:11px;border-top:1px solid var(--line,#e8dcc0);
  display:flex;flex-direction:column;gap:7px;font-size:13.5px;color:var(--sub,#7a6450)}
.jn-coupon-lines>div{display:flex;justify-content:space-between;gap:12px}
.jn-coupon-lines .off{color:#1f8a4c;font-weight:600}
.jn-coupon-lines .total{padding-top:8px;border-top:1px solid var(--line,#e8dcc0);
  color:var(--ink,#2e1c12);font-weight:800;font-size:15px}
@media (pointer: coarse){ .jn-coupon-x{min-height:44px;min-width:44px} }
`;

/* night-study watermark for the brand panel — inspired by the late-night aspirant's desk */
function AspirationScene() {
  const stars = [];
  for (let i = 0; i < 18; i++) {
    stars.push(
      <circle key={i}
        cx={20 + ((i * 41) % 360)}
        cy={8 + ((i * 23) % 70)}
        r={i % 4 === 0 ? 1.5 : 0.8}
        fill="#ffe6b0"
        opacity={0.18 + (i % 5) * 0.08} />
    );
  }
  return (
    <svg className="jn-scene" viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
      <defs>
        <radialGradient id="lampGlow" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stopColor="#ffdb8a" stopOpacity="0.5" />
          <stop offset="100%" stopColor="#ffdb8a" stopOpacity="0" />
        </radialGradient>
        <linearGradient id="duskSky" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stopColor="#f0c987" stopOpacity="0.35" />
          <stop offset="100%" stopColor="#c97a3a" stopOpacity="0.12" />
        </linearGradient>
      </defs>

      {stars}

      {/* window with a domed dream-building silhouette, upper-right */}
      <g transform="translate(238 300)" opacity="0.85">
        <rect x="0" y="0" width="150" height="185" rx="4" fill="url(#duskSky)" stroke="#f4cf86" strokeWidth="1.4" strokeOpacity="0.35" />
        <line x1="75" y1="0" x2="75" y2="185" stroke="#f4cf86" strokeWidth="1" strokeOpacity="0.25" />
        <line x1="0" y1="92" x2="150" y2="92" stroke="#f4cf86" strokeWidth="1" strokeOpacity="0.25" />
        {/* dome building */}
        <g opacity="0.7" fill="#f4cf86">
          <rect x="30" y="120" width="90" height="55" opacity="0.5" />
          <circle cx="75" cy="105" r="26" opacity="0.55" />
          <rect x="60" y="60" width="30" height="45" opacity="0.55" />
          <path d="M75 30 a15 15 0 0 1 15 15 h-30 a15 15 0 0 1 15 -15 Z" opacity="0.6" />
          <line x1="75" y1="30" x2="75" y2="16" stroke="#f4cf86" strokeWidth="1.6" opacity="0.7" />
        </g>
        {/* small flag */}
        <line x1="112" y1="150" x2="112" y2="128" stroke="#f4cf86" strokeWidth="1.3" opacity="0.6" />
        <path d="M112 128 L126 133 L112 138 Z" fill="#d4a64a" opacity="0.65" />
      </g>

      {/* desk lamp glow, lower-left where the aspirant studies */}
      <circle cx="95" cy="470" r="130" fill="url(#lampGlow)" />
      <g opacity="0.55" stroke="#f4cf86" strokeWidth="1.6" fill="none" strokeLinecap="round">
        <line x1="95" y1="470" x2="70" y2="430" />
        <line x1="70" y1="430" x2="55" y2="390" />
        <path d="M40 385 l30 10 l-8 22 Z" fill="#f4cf86" opacity="0.7" stroke="none" />
      </g>

      {/* stack of books, foreground-left */}
      <g opacity="0.55" fill="#f4cf86">
        <rect x="20" y="530" width="70" height="12" rx="1.5" />
        <rect x="14" y="544" width="82" height="12" rx="1.5" />
        <rect x="24" y="558" width="62" height="12" rx="1.5" />
      </g>
    </svg>
  );
}

function Mandala() {
  const petals = [];
  for (let i = 0; i < 24; i++) {
    const a = (i * 360) / 24;
    petals.push(<ellipse key={i} cx="100" cy="38" rx="6" ry="20" fill="none" stroke="#f4cf86" strokeWidth="1.1"
      transform={`rotate(${a} 100 100)`} />);
  }
  return (
    <svg className="jn-mandala" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <circle cx="100" cy="100" r="78" fill="none" stroke="#f4cf86" strokeWidth="1" />
      <circle cx="100" cy="100" r="64" fill="none" stroke="#f4cf86" strokeWidth="0.8" strokeDasharray="2 4" />
      <circle cx="100" cy="100" r="40" fill="none" stroke="#f4cf86" strokeWidth="1" />
      {petals}
    </svg>
  );
}

function ContactModal({ onClose }) {
  const { t } = useLang();
  return (
    <div className="jn-scrim" onClick={onClose}>
      <div className="jn-modal" onClick={(e) => e.stopPropagation()}>
        <h3>{t("need_help")}</h3>
        <p>{t("help_sub")}</p>
        <a className="jn-crow" href="mailto:junoonias123@gmail.com">
          <span className="jn-cic"><Mail size={18} /></span>
          <span className="jn-cmeta"><b>junoonias123@gmail.com</b><span>Email support</span></span>
        </a>
        <div className="jn-crow" style={{ cursor: "default" }}>
          <span className="jn-cic"><MapPin size={18} /></span>
          <span className="jn-cmeta"><b>New Delhi, India</b><span>Mon–Sat, 10am–7pm</span></span>
        </div>
        <button className="jn-cta" style={{ marginTop: 16 }} onClick={onClose}>{t("close")}</button>
      </div>
    </div>
  );
}

export { LOGIN_CSS, AspirationScene, Mandala, ContactModal };
