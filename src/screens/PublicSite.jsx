import { useState, useEffect, useRef } from "react";
import {
  CheckCircle2, ArrowRight, ArrowLeft, Lock, Headphones, Menu, X,
  ShieldCheck, Layers, Target, Timer,
} from "lucide-react";
import { ChromeControls } from "../lib/i18n.jsx";
import { useLang } from "../lib/contexts.js";
import { ContactModal } from "./authChrome.jsx";
import { ErrorState, Skeleton } from "../ui/Feedback.jsx";
import { Diya, Mandala, StepArt, ReportArt, TicketIcon, Divider } from "../ui/Illustrations.jsx";
import ContentPage from "./ContentPages.jsx";
import { RESOURCES, RESOURCE_TITLES } from "../lib/resources.js";
import { COMPANY, SOCIAL_LINKS } from "../lib/legal.js";
import { Instagram, YouTube, Telegram, WhatsApp, LinkedIn, XMark } from "../ui/SocialIcons.jsx";
import * as DB from "../lib/db.js";

/* ============================================================
   PUBLIC SITE — the storefront.

   Built on the brand that already existed in the login screen —
   maroon, gold, the diya, the Upaniṣad line — rather than a new
   theme invented from scratch. Fraunces for display, Inter for
   body, one animated signature element (the flame), and scroll
   reveal on section headers and cards only, never everywhere.
   ============================================================ */

const CSS = `
.pb-root{
  background:var(--cream-50); color:var(--ink-900); min-height:100vh;
  font-family:var(--font-body); -webkit-font-smoothing:antialiased;
}
.pb-root *{box-sizing:border-box}
.pb-root a{color:inherit;text-decoration:none}
.pb-sec-narrow{max-width:1180px;margin:0 auto;padding-inline:24px}
.pb-eyebrow{font-family:var(--font-roman);font-size:13px;letter-spacing:.26em;text-transform:uppercase;
  color:var(--gold-600);font-weight:400}
.pb-eyebrow::after{content:"";display:block;width:34px;height:1px;margin:9px auto 0;
  background:linear-gradient(90deg,transparent,var(--gold-500),transparent)}

/* ---------- HEADER ---------- */
.pb-head{position:sticky;top:0;z-index:50;backdrop-filter:blur(12px);
  background:color-mix(in srgb,var(--cream-50) 86%,transparent);border-bottom:1px solid var(--line)}
.pb-head-in{max-width:1180px;margin:0 auto;padding:12px 24px;display:flex;align-items:center;gap:16px}
.pb-brand{display:flex;align-items:center;gap:11px;background:none;border:0;padding:0;cursor:pointer;font-family:inherit}
.pb-mark{border-radius:11px;flex:0 0 auto;display:grid;place-items:center;
  background:linear-gradient(155deg,var(--brand-700),var(--brand-900));box-shadow:var(--shadow-card)}
.pb-name{display:block;font-family:var(--font-display);font-weight:700;font-size:19px;letter-spacing:.01em;
  color:var(--ink-900);line-height:1.1;text-align:left;white-space:nowrap}
.pb-name span{color:var(--gold-600)}
.pb-tagline{display:block;font-size:10.5px;color:var(--ink-400);letter-spacing:.05em;text-align:left;
  margin-top:1px;white-space:nowrap}
.pb-nav{display:flex;align-items:center;gap:6px;margin-left:auto}
.pb-nav .link{background:none;border:0;font:inherit;font-size:14.5px;font-weight:600;color:var(--ink-600);
  padding:9px 12px;border-radius:9px;cursor:pointer;transition:color .16s,background .16s;white-space:nowrap}
.pb-nav .link{position:relative}
.pb-nav .link::after{content:"";position:absolute;left:50%;right:50%;bottom:4px;height:1.5px;
  background:var(--gold-500);transition:left .22s ease,right .22s ease;border-radius:2px}
.pb-nav .link:hover{color:var(--brand-700);background:color-mix(in srgb,var(--gold-300) 20%,transparent)}
.pb-nav .link:hover::after{left:12px;right:12px}
.pb-burger{display:none;width:40px;height:40px;border-radius:10px;border:1px solid var(--line);
  background:var(--cream-50);align-items:center;justify-content:center;cursor:pointer;color:var(--ink-600)}

/* ---------- BUTTONS ---------- */
.pb-btn{position:relative;overflow:hidden;isolation:isolate;
  display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:11px 22px;
  border-radius:100px;font:inherit;font-weight:700;font-size:14.5px;border:1.5px solid transparent;
  cursor:pointer;transition:transform .18s cubic-bezier(.2,.8,.3,1),box-shadow .18s ease,background .16s}
.pb-btn:hover{transform:translateY(-2px)}
.pb-btn:active{transform:translateY(0) scale(.98);transition-duration:.06s}
.pb-btn:focus-visible{outline:2.5px solid var(--gold-500);outline-offset:3px}

/* A slow sheen crossing the face on hover — the one flourish the primary
   actions get, and only on a real pointer. */
.pb-btn::after{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;
  background:linear-gradient(105deg,transparent 38%,rgba(255,255,255,.42) 50%,transparent 62%);
  transform:translateX(-130%);transition:transform .62s cubic-bezier(.3,.7,.3,1)}
@media (hover:hover){ .pb-btn:hover::after{transform:translateX(130%)} }

/* The arrow leans into the direction it points. */
.pb-btn svg{transition:transform .2s cubic-bezier(.2,.8,.3,1)}
.pb-btn:hover svg:last-child{transform:translateX(3px)}
.pb-btn[disabled]{cursor:not-allowed;transform:none}
.pb-btn[disabled]::after{display:none}
.pb-btn-gold{background:linear-gradient(155deg,var(--gold-500),var(--gold-600));color:#2a1e05;
  box-shadow:0 10px 24px -10px rgba(197,150,30,.65)}
.pb-btn-maroon{background:var(--brand-700);color:#fff;box-shadow:0 10px 24px -12px rgba(99,19,34,.7)}
.pb-btn-ghost{border-color:var(--brand-700);color:var(--brand-700);background:transparent}
.pb-btn-onDark{border:1.5px solid rgba(255,255,255,.34);color:var(--on-dark);background:rgba(255,255,255,.06)}
.pb-btn-onDark:hover{background:rgba(255,255,255,.13)}
.pb-btn-sm{padding:9px 16px;font-size:13.5px}
.pb-btn-block{width:100%}

/* ---------- HERO ---------- */
.pb-hero{position:relative;overflow:hidden;color:var(--on-dark);
  background:linear-gradient(175deg,var(--brand-800) 0%,var(--brand-900) 100%)}
[data-theme="dark"] .pb-hero{background:linear-gradient(175deg,#2a0d13 0%,#150609 100%)}
.pb-hero::before{content:"";position:absolute;inset:0;pointer-events:none;
  background:radial-gradient(620px 320px at 82% -8%, rgba(201,162,39,.20), transparent 62%),
             repeating-linear-gradient(115deg, rgba(255,255,255,.02) 0 2px, transparent 2px 26px)}
.pb-hero-grid{position:relative;z-index:2;display:grid;grid-template-columns:1.08fr .92fr;gap:44px;
  align-items:center;max-width:1180px;margin:0 auto;padding:74px 24px 66px}
.pb-hero-deva{font-family:var(--font-shloka);font-size:19px;letter-spacing:.03em;color:var(--gold-300);
  opacity:.95;margin-bottom:12px;line-height:1.5}
.pb-h1{font-family:var(--font-display);font-optical-sizing:auto;font-size:clamp(33px,4.6vw,53px);
  line-height:1.07;font-weight:600;letter-spacing:-.012em;margin:0 0 18px;text-wrap:balance}
.pb-h1 em{font-family:var(--font-quote);font-style:italic;font-weight:500;color:var(--gold-300);
  font-size:1.1em;letter-spacing:-.005em}
.pb-lede{font-size:17px;line-height:1.62;color:#e9ddc9;max-width:50ch;margin:0 0 28px}
.pb-hero-ctas{display:flex;gap:13px;flex-wrap:wrap;margin-bottom:32px}
.pb-ticks{display:flex;flex-wrap:wrap;gap:20px;padding:0;margin:0;list-style:none;font-size:13.5px;color:#d8c9ae}
.pb-ticks li{display:flex;align-items:center;gap:8px}
.pb-ticks svg{color:var(--gold-300);flex:none}
.pb-stage{display:flex;align-items:center;justify-content:center;min-height:340px;position:relative}

/* ---------- FEATURE STRIP ---------- */
.pb-strip{background:var(--cream-100);border-bottom:1px solid var(--line)}
.pb-strip-in{max-width:1180px;margin:0 auto;padding:26px 24px;display:grid;grid-template-columns:repeat(4,1fr)}
.pb-strip-item{padding:0 22px;border-left:1px solid var(--line);font-size:13.5px;color:var(--ink-600);line-height:1.5}
.pb-strip-item:first-child{border-left:0;padding-left:0}
.pb-strip-item b{display:block;font-family:var(--font-display);font-size:16px;color:var(--brand-700);
  margin-bottom:4px;font-weight:600}

/* ---------- SECTIONS ---------- */
.pb-sec{padding-block:76px;position:relative}
.pb-sec-head{max-width:660px;margin:0 auto 42px;text-align:center;position:relative;z-index:2}
.pb-h2{font-family:var(--font-display);font-optical-sizing:auto;font-size:clamp(27px,3.1vw,37px);
  margin:9px 0 12px;font-weight:600;line-height:1.16;color:var(--ink-900)}
.pb-sub{color:var(--ink-600);font-size:15.5px;line-height:1.65;margin:0}
.pb-h2 em{font-family:var(--font-quote);font-style:italic;font-weight:500;font-size:1.08em;color:var(--brand-600)}
.pb-sec-mandala{position:absolute;top:-74px;left:50%;transform:translateX(-50%);
  width:460px;height:460px;opacity:.15;pointer-events:none;z-index:0}

/* ---------- TABS + CARDS ---------- */
.pb-tabs{display:flex;justify-content:center;gap:10px;margin-bottom:34px;flex-wrap:wrap;
  scroll-margin-top:88px}
.pb-tab{padding:10px 22px;border-radius:100px;border:1.5px solid var(--line);background:var(--cream-50);
  font:inherit;font-weight:700;font-size:14px;color:var(--ink-600);cursor:pointer;transition:.16s}
.pb-tab:hover{border-color:var(--gold-500)}
.pb-tab.on{background:var(--brand-700);border-color:var(--brand-700);color:#fff}
.pb-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:22px}
.pb-card{background:var(--cream-50);border:1px solid var(--line);border-radius:var(--radius-lg);
  padding:28px 26px 26px;box-shadow:var(--shadow-card);position:relative;overflow:hidden;
  display:flex;flex-direction:column;
  transition:transform .26s cubic-bezier(.2,.8,.3,1),box-shadow .26s ease,border-color .26s ease}
.pb-card::before{content:"";position:absolute;top:0;left:0;right:0;height:5px;
  background:linear-gradient(90deg,var(--gold-500),var(--brand-600))}
.pb-card:hover{transform:translateY(-5px);box-shadow:var(--shadow-lift);border-color:var(--gold-300)}
.pb-card-soon{opacity:.82}
.pb-card-soon::before{background:linear-gradient(90deg,var(--ink-400),var(--clay-400,#b9a184))}
.pb-soon{background:var(--cream-100);color:var(--ink-400);border:1.5px dashed var(--line);cursor:not-allowed}
.pb-soon:hover{transform:none}
.pb-card-exam{display:inline-flex;align-self:flex-start;font-size:10.5px;font-weight:800;letter-spacing:.1em;
  text-transform:uppercase;padding:5px 11px;border-radius:100px;margin-bottom:12px;
  background:color-mix(in srgb,var(--gold-300) 34%,transparent);color:var(--brand-700)}
.pb-card-title{font-family:var(--font-display);font-size:20px;font-weight:600;line-height:1.25;
  color:var(--ink-900);margin:0 0 8px}
.pb-card-meta{font-size:13px;color:var(--ink-400);margin-bottom:12px}
.pb-card-desc{font-size:14px;color:var(--ink-600);line-height:1.55;margin:0 0 18px;min-height:44px}
.pb-price-row{display:flex;align-items:baseline;gap:10px;margin-bottom:18px;flex-wrap:wrap}
.pb-price{font-family:var(--font-display);font-size:26px;font-weight:700;color:var(--brand-700);line-height:1}
.pb-price-mrp{font-size:14.5px;color:var(--ink-400);text-decoration:line-through}
.pb-off{font-size:11px;font-weight:800;color:var(--ok-600);
  background:color-mix(in srgb,var(--ok-600) 14%,transparent);padding:3px 9px;border-radius:100px}
.pb-card-btns{margin-top:auto;display:flex;gap:9px}
.pb-owned{background:color-mix(in srgb,var(--ok-600) 12%,transparent) !important;color:var(--ok-600) !important;
  border:1.5px solid color-mix(in srgb,var(--ok-600) 34%,transparent) !important;box-shadow:none !important}

/* ---------- JOURNEY ---------- */
.pb-steps{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.pb-step{background:var(--cream-50);border:1px solid var(--line);border-radius:var(--radius-lg);
  padding:30px 24px 26px;text-align:center;position:relative;box-shadow:var(--shadow-card)}
.pb-step-n{position:absolute;top:-15px;left:50%;transform:translateX(-50%);width:30px;height:30px;
  border-radius:50%;background:var(--brand-700);color:#fff;display:grid;place-items:center;
  font-size:13px;font-weight:800;box-shadow:var(--shadow-card)}
.pb-step .ill-step{margin:8px auto 14px;color:var(--brand-600)}
.pb-step h3{font-family:var(--font-display);font-size:18px;font-weight:600;margin:0 0 8px;color:var(--ink-900)}
.pb-step p{font-size:14px;color:var(--ink-600);line-height:1.6;margin:0}

/* ---------- REPORT SHOWCASE ---------- */
.pb-show{background:var(--cream-100);border-block:1px solid var(--line)}
.pb-show-grid{display:grid;grid-template-columns:1fr 1.05fr;gap:52px;align-items:center;
  max-width:1180px;margin:0 auto;padding:76px 24px}
.pb-show-list{list-style:none;padding:0;margin:24px 0 0;display:flex;flex-direction:column;gap:16px}
.pb-show-list li{display:flex;gap:13px;align-items:flex-start}
.pb-show-ic{width:34px;height:34px;border-radius:10px;flex:none;display:grid;place-items:center;
  background:color-mix(in srgb,var(--gold-300) 34%,transparent);color:var(--brand-700)}
.pb-show-list b{display:block;font-size:14.5px;color:var(--ink-900);margin-bottom:3px}
.pb-show-list em{display:block;font-style:normal;font-size:13.5px;color:var(--ink-600);line-height:1.55}
.ill-report{width:100%;max-width:440px;height:auto;display:block;margin-inline:auto;
  filter:drop-shadow(var(--shadow-soft))}

/* ---------- FREE RESOURCES ---------- */
.pb-res{background:var(--brand-900);color:var(--on-dark);position:relative;overflow:hidden}
[data-theme="dark"] .pb-res{background:#150609}
.pb-res .pb-h2{color:var(--on-dark)}
.pb-res .pb-sub{color:#d8c9ae}
.pb-res .pb-eyebrow{color:var(--gold-300)}
.pb-res-mandala{position:absolute;right:-170px;bottom:-190px;width:520px;height:520px;opacity:.10;color:var(--gold-300)}
.pb-resgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(196px,1fr));gap:16px}
.pb-rescard{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10);border-radius:16px;
  padding:22px 20px;text-align:left;cursor:pointer;font:inherit;color:inherit;display:flex;flex-direction:column;
  transition:background .2s ease,transform .2s ease,border-color .2s ease}
.pb-rescard:hover{background:rgba(255,255,255,.1);transform:translateY(-3px);border-color:rgba(227,200,119,.42)}
.pb-rescard svg{color:var(--gold-300);margin-bottom:14px}
.pb-rescard h4{font-size:15px;margin:0 0 6px;font-weight:700;color:var(--on-dark)}
.pb-rescard p{font-size:12.5px;color:#c9b998;margin:0;line-height:1.5}

/* ---------- COUPON TICKET ---------- */
.pb-ticket-wrap{overflow-x:clip;padding-inline:14px}
.pb-ticket{max-width:900px;margin:0 auto;display:flex;align-items:center;gap:24px;flex-wrap:wrap;
  background:var(--cream-50);border:1.5px dashed var(--gold-600);border-radius:18px;
  padding:26px 30px;box-shadow:var(--shadow-card);position:relative}
.pb-notch{position:absolute;width:26px;height:26px;background:var(--cream-50);border-radius:50%;
  border:1.5px dashed var(--gold-600);top:50%;transform:translateY(-50%)}
.pb-notch-l{left:-14px} .pb-notch-r{right:-14px}
.pb-ticket-ic{width:52px;height:52px;flex:none;border-radius:14px;display:grid;place-items:center;
  background:var(--cream-100);color:var(--brand-700)}
.pb-ticket h4{margin:0 0 4px;font-family:var(--font-display);font-size:18px;font-weight:600;color:var(--ink-900)}
.pb-ticket p{margin:0;font-size:13.5px;color:var(--ink-600);line-height:1.55}

/* ---------- QUOTE ---------- */
.pb-sec-coupon{padding-block:62px}
.pb-quote{text-align:center;padding:74px 24px}
.pb-quote .deva{font-family:var(--font-deva);font-size:27px;color:var(--brand-700);margin-bottom:12px}
.pb-quote p{font-family:var(--font-display);font-style:italic;color:var(--ink-600);font-size:17px;
  max-width:480px;margin:0 auto}
.pb-quote .src{margin-top:10px;font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-400)}

/* ---------- FOOTER ----------
   Built as one inset card on a darker ground rather than a full-bleed band, so
   the page ends deliberately instead of just running out. Two halves split by
   a rule: the brand and the newsletter on the left, the link columns on the
   right; then a separated bottom bar for the legal line. */
.pb-foot{background:var(--cream-100);border-top:1px solid var(--line);padding:56px 24px 26px}
.pb-foot-card{max-width:1180px;margin:0 auto;background:var(--cream-50);border:1px solid var(--line);
  border-radius:26px;overflow:hidden;box-shadow:var(--shadow-card)}
.pb-foot-in{display:grid;grid-template-columns:1.05fr 1.35fr;gap:0}

/* -- left: identity + newsletter -- */
.pb-foot-brand{padding:42px 40px;border-right:1px solid var(--line);min-width:0}
.pb-foot-logo{display:flex;align-items:center;gap:12px;margin-bottom:16px}
.pb-foot-blurb{font-size:14px;line-height:1.7;color:var(--ink-600);margin:0 0 30px;max-width:40ch}
.pb-news h5{font-family:var(--font-display);font-size:20px;font-weight:600;text-transform:none;
  letter-spacing:-.01em;color:var(--ink-900);margin:0 0 6px}
.pb-news p{font-size:13px;color:var(--ink-400);margin:0 0 14px;line-height:1.6}
.pb-news-row{display:flex;align-items:stretch;background:var(--cream-50);border:1.5px solid var(--line);
  border-radius:100px;padding:5px 5px 5px 6px;transition:border-color .18s,box-shadow .18s;max-width:420px}
.pb-news-row:focus-within{border-color:var(--gold-500);box-shadow:0 0 0 4px color-mix(in srgb,var(--gold-500) 16%,transparent)}
.pb-news-row input{flex:1;min-width:0;border:0;background:none;outline:none;font:inherit;font-size:14.5px;
  color:var(--ink-900);padding:10px 12px}
.pb-news-row input::placeholder{color:var(--ink-400)}
.pb-news-btn{flex:0 0 auto;border:0;border-radius:100px;font:inherit;font-weight:700;font-size:14px;
  padding:10px 22px;cursor:pointer;color:#2a1e05;background:linear-gradient(155deg,var(--gold-500),var(--gold-600));
  transition:filter .16s,transform .16s}
.pb-news-btn:hover:not(:disabled){filter:brightness(1.06);transform:translateY(-1px)}
.pb-news-btn:disabled{opacity:.55;cursor:default}
.pb-news-msg{margin:11px 2px 0;font-size:12.5px;line-height:1.5;display:flex;align-items:flex-start;gap:6px}
.pb-news-msg.ok{color:var(--ok-600)}
.pb-news-msg.bad{color:var(--bad-600)}
.pb-socials{display:flex;gap:10px;margin-top:26px}
/* Scoped under .pb-foot so it outranks the .pb-foot a rule (display:block,
   width:100%), which was turning the linked icon into a 240px-wide block and
   squeezing the rest of the row down to 25px. flex:0 0 auto stops them shrinking at all. */
.pb-foot .pb-social{flex:0 0 auto;width:42px;height:42px;margin:0;border-radius:50%;
  border:1.5px solid var(--line);background:var(--cream-50);
  display:grid;place-items:center;color:var(--ink-600);cursor:pointer;text-align:center;
  transition:border-color .18s,color .18s,transform .18s,background .18s}
.pb-foot .pb-social:hover{border-color:var(--brand-700);color:var(--brand-700);transform:translateY(-2px);
  background:color-mix(in srgb,var(--gold-300) 18%,transparent)}
/* Placed but not yet linked. Muted and inert — the row reads as designed
   rather than broken, and nothing here opens a dead tab. */
.pb-foot .pb-social-soon{opacity:.34;cursor:default;border-style:dashed}
.pb-foot .pb-social-soon:hover{border-color:var(--line);color:var(--ink-600);transform:none;background:var(--cream-50)}

/* -- right: link columns -- */
.pb-foot-links{padding:42px 40px;display:grid;grid-template-columns:1fr 1fr 1.35fr;gap:28px;min-width:0}
.pb-foot h5{font-size:12px;text-transform:uppercase;letter-spacing:.13em;color:var(--gold-600);
  margin:0 0 16px;font-weight:800;font-family:var(--font-roman)}
.pb-foot a,.pb-foot .flink{display:block;width:100%;font-size:14px;color:var(--ink-600);margin-bottom:11px;
  background:none;border:0;font-family:inherit;padding:0;cursor:pointer;text-align:left;
  transition:color .16s,transform .16s;min-width:0;overflow-wrap:break-word}
.pb-foot a:hover,.pb-foot .flink:hover{color:var(--brand-700);transform:translateX(2px)}
.pb-foot-contact{font-size:13.5px;line-height:1.7;color:var(--ink-600);margin:0}
.pb-foot-contact a{display:inline;margin:0;color:var(--brand-700);text-decoration:underline;
  text-underline-offset:2px;overflow-wrap:break-word;word-break:normal}

/* -- bottom bar -- */
.pb-foot-bottom{max-width:1180px;margin:22px auto 0;padding:0 8px;
  display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;
  font-size:12.5px;color:var(--ink-400)}
.pb-foot-legal{display:flex;gap:16px;flex-wrap:wrap}
.pb-foot-legal button{background:none;border:0;font:inherit;font-size:12.5px;color:var(--ink-400);
  cursor:pointer;padding:0;transition:color .16s}
.pb-foot-legal button:hover{color:var(--brand-700)}

/* ---------- CONTENT HUB ---------- */
.pb-panel{background:var(--cream-50);border:1px solid var(--line);border-radius:var(--radius-lg);
  padding:26px;box-shadow:var(--shadow-card)}
.pb-h3{font-family:var(--font-display);font-size:19px;font-weight:600;color:var(--ink-900);margin:6px 0 14px}
.pb-kicker{font-size:11.5px;font-weight:800;letter-spacing:.13em;text-transform:uppercase;color:var(--gold-600)}
.pb-note{background:color-mix(in srgb,var(--gold-300) 22%,transparent);
  border:1px solid color-mix(in srgb,var(--gold-500) 42%,transparent);border-radius:12px;
  padding:14px 17px;font-size:13.5px;color:var(--ink-600);line-height:1.65;margin-bottom:20px}
.pb-note a{color:var(--brand-700);font-weight:700;text-decoration:underline}
.pb-syl{list-style:none;counter-reset:syl;padding:0;margin:0;display:flex;flex-direction:column;gap:15px}
.pb-syl li{counter-increment:syl;display:flex;flex-direction:column;gap:3px;padding-left:36px;position:relative}
.pb-syl li::before{content:counter(syl);position:absolute;left:0;top:0;width:25px;height:25px;border-radius:8px;
  background:color-mix(in srgb,var(--gold-300) 34%,transparent);color:var(--brand-700);
  display:grid;place-items:center;font-size:11.5px;font-weight:800}
.pb-syl-sec{font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--gold-600)}
.pb-syl-topic{font-size:14.5px;color:var(--ink-900);line-height:1.6;font-weight:500}
.pb-syl-detail{font-size:13px;color:var(--ink-600);line-height:1.6}
.pb-listrow{display:flex;align-items:center;gap:14px;padding:15px 0;border-bottom:1px solid var(--line);flex-wrap:wrap}
.pb-listrow:last-child{border-bottom:0}
.pb-listrow-t{display:block;font-size:14.5px;font-weight:700;color:var(--ink-900);line-height:1.45}
.pb-listrow-s{display:block;font-size:12.5px;color:var(--ink-400);margin-top:3px}
.pb-b-tight{padding:9px 15px;font-size:13px;display:inline-flex;align-items:center;gap:6px;border-radius:100px;
  font-weight:700;border:1.5px solid var(--line);color:var(--ink-600);background:var(--cream-50)}
.pb-b-tight:hover{border-color:var(--gold-500);color:var(--brand-700)}
.pb-b-primary{padding:9px 15px;font-size:13px;display:inline-flex;align-items:center;gap:6px;border-radius:100px;
  font-weight:700;background:var(--brand-700);color:#fff;border:1.5px solid transparent}
.pb-b-ghost{padding:9px 15px;font-size:13px;display:inline-flex;align-items:center;gap:6px;border-radius:100px;
  font-weight:700;border:1.5px solid var(--line);color:var(--ink-600);background:var(--cream-50);cursor:pointer;font-family:inherit}
.pb-card-link{cursor:pointer}
.pb-res-ic{width:46px;height:46px;border-radius:13px;display:grid;place-items:center;margin-bottom:14px;
  background:linear-gradient(150deg,var(--brand-700),var(--brand-900));color:var(--gold-300)}
.pb-openlink{display:inline-flex;align-items:center;gap:6px;margin-top:auto;padding-top:14px;
  font-size:13.5px;font-weight:700;color:var(--brand-700)}
.pb-search-wrap{display:flex;justify-content:center;margin-bottom:26px}
.pb-search{display:flex;align-items:center;gap:10px;background:var(--cream-50);border:1.5px solid var(--line);
  border-radius:100px;padding:11px 20px;min-width:min(430px,100%);color:var(--ink-400)}
.pb-search input{border:0;background:none;outline:none;font:inherit;font-size:14.5px;color:var(--ink-900);width:100%}
.pb-chipwrap{display:flex;flex-wrap:wrap;gap:9px}
.pb-chip-link{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--line);border-radius:100px;
  padding:10px 16px;font-size:13.5px;font-weight:600;color:var(--ink-900);
  background:color-mix(in srgb,var(--gold-300) 14%,transparent);transition:.16s}
.pb-chip-link:hover{border-color:var(--gold-500);background:color-mix(in srgb,var(--gold-300) 28%,transparent)}
.pb-lang{font-size:10.5px;font-weight:800;color:var(--gold-600)}
.pb-news{border-bottom:1px solid var(--line)}
.pb-news:last-child{border-bottom:0}
.pb-news-head{display:flex;align-items:flex-start;gap:12px;width:100%;text-align:left;background:none;
  border:0;font:inherit;cursor:pointer;padding:16px 0;color:var(--ink-900)}
.pb-news-body{padding:0 0 18px;font-size:14.5px;color:var(--ink-600);line-height:1.75}
.pb-news-body p{margin:0 0 12px;white-space:pre-wrap}
.pb-tagrow{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:10px}
.pb-tag{font-size:10.5px;font-weight:800;letter-spacing:.08em;padding:4px 10px;border-radius:100px;
  background:color-mix(in srgb,var(--brand-600) 13%,transparent);color:var(--brand-700)}
.pb-tag-soft{background:color-mix(in srgb,var(--gold-300) 30%,transparent);color:var(--gold-600);
  letter-spacing:.02em;text-transform:none}

/* ---------- BUNDLE DETAIL ---------- */
.pb-detail{display:grid;grid-template-columns:1.5fr 1fr;gap:32px;align-items:start}
.pb-buy{position:sticky;top:84px}
.pb-list{list-style:none;padding:0;margin:16px 0 0;display:flex;flex-direction:column;gap:13px}
.pb-list li{display:flex;gap:11px;align-items:flex-start;font-size:14.5px;line-height:1.6;color:var(--ink-900)}
.pb-list svg{color:var(--ok-600);flex:0 0 auto;margin-top:2px}
.pb-trow{display:flex;align-items:center;gap:12px;padding:14px 0;border-bottom:1px solid var(--line)}
.pb-trow:last-child{border-bottom:0}
.pb-tnum{width:30px;height:30px;border-radius:9px;flex:0 0 auto;display:grid;place-items:center;
  font-size:12px;font-weight:800;background:color-mix(in srgb,var(--gold-300) 34%,transparent);color:var(--brand-700)}
.pb-tname{flex:1;min-width:0;font-size:14.5px;font-weight:600;color:var(--ink-900)}
.pb-tmeta{font-size:12.5px;color:var(--ink-400);margin-top:2px;font-weight:500}

/* ---------- RESPONSIVE ---------- */
/* ---------- MOBILE POLISH -----------------------------------------------
   Measured on a 375px phone, not guessed. The hero used to eat the whole
   first screen before a single word appeared, the headline broke onto a
   third line with one orphaned word, and every section carried desktop
   padding. Type, rhythm and density are all tightened here. */
@media (max-width:640px){
  .pb-hero-grid{padding:26px 20px 38px;gap:18px}
  .pb-stage{min-height:0}
  .ill-diya{width:186px;height:186px}
  .pb-hero-deva{font-size:14px;margin-bottom:6px}
  .pb-h1{font-size:30px;line-height:1.14;letter-spacing:-.015em;margin-bottom:14px}
  .pb-h1 br{display:inline}
  .pb-lede{font-size:15.5px;line-height:1.6;margin-bottom:22px}
  .pb-hero-ctas{gap:10px;margin-bottom:24px}
  .pb-hero-ctas .pb-btn{flex:1 1 100%;padding:14px 20px;font-size:15px}
  .pb-ticks{gap:10px 18px;font-size:12.5px}

  .pb-head-in{padding:10px 16px;gap:10px}
  .pb-name{font-size:17px}
  .pb-tagline{font-size:9.5px}

  .pb-sec{padding-block:48px}
  /* The tab rows bleed to the screen edge with a negative margin so they can
     scroll edge-to-edge. Clipping here keeps that bleed from becoming a
     page-level scrollbar. (clip, not hidden — hidden would break any sticky
     descendant.) */
  .pb-sec-narrow{padding-inline:18px;overflow-x:clip}
  .pb-sec-head{margin-bottom:28px}
  .pb-h2{font-size:25px;line-height:1.2;text-wrap:balance}
  .pb-sub{font-size:14.5px;line-height:1.6}
  .pb-eyebrow{font-size:11px;letter-spacing:.12em}

  .pb-grid{gap:16px;grid-template-columns:1fr}
  .pb-card{padding:22px 20px 20px;border-radius:18px}
  .pb-card-title{font-size:18px}
  .pb-card-desc{min-height:0;margin-bottom:14px}
  .pb-price{font-size:24px}
  .pb-card-btns{flex-direction:column}
  .pb-card-btns .pb-btn{width:100%}

  .pb-tabs{gap:7px;margin-bottom:24px;justify-content:flex-start;
    flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;
    margin-inline:-18px;padding:2px 18px 6px}
  .pb-tabs::-webkit-scrollbar{display:none}
  .pb-tab{flex:0 0 auto;padding:9px 17px;font-size:13.5px}

  .pb-steps{gap:22px}
  .pb-step{padding:26px 20px 22px}
  .pb-step h3{font-size:17px}
  .pb-step p{font-size:13.5px}

  .pb-show-grid{padding:48px 18px;gap:26px}
  .pb-show-list{gap:14px;margin-top:18px}
  .pb-show-list b{font-size:14px}
  .pb-show-list em{font-size:13px}
  .ill-report{max-width:100%}

  .pb-resgrid{grid-template-columns:1fr 1fr;gap:11px}
  .pb-rescard{padding:16px 14px;border-radius:14px}
  .pb-rescard svg{width:22px;height:22px;margin-bottom:10px}
  .pb-rescard h4{font-size:13.5px}
  .pb-rescard p{font-size:11.5px;line-height:1.45}

  .pb-ticket{padding:20px;gap:16px}
  .pb-ticket-ic{width:44px;height:44px}
  .pb-ticket h4{font-size:16.5px}
  .pb-ticket p{font-size:13px}
  .pb-ticket .pb-btn{width:100%}
  .pb-notch{display:none}

  .pb-quote{padding:48px 20px}
  .pb-quote .deva{font-size:23px}
  .pb-quote p{font-size:15.5px}

  .pb-foot{padding:34px 14px 20px}
  .pb-foot-card{border-radius:20px}
  .pb-foot-brand,.pb-foot-links{padding:28px 22px}
  .pb-foot-bottom{flex-direction:column;align-items:flex-start;gap:10px;padding:0 6px}

  .pb-panel{padding:20px;border-radius:18px}
  .pb-h3{font-size:17px}
  .pb-syl li{padding-left:31px}
  .pb-listrow{padding:13px 0}
  .pb-detail{gap:22px}
}

/* Very narrow phones — 360px and below. */
@media (max-width:380px){
  .pb-h1{font-size:28px}
  .ill-diya{width:164px;height:164px}
  .pb-resgrid{grid-template-columns:1fr}
}

@media (max-width:980px){
  .pb-hero-grid{grid-template-columns:1fr;padding:52px 20px 46px;gap:28px}
  .pb-stage{min-height:240px;order:-1}
  .pb-lede{max-width:none}
  .pb-show-grid{grid-template-columns:1fr;gap:34px;padding:58px 24px}
  /* Three across on a tablet, one on a phone. Written as a range so it
     does not depend on where this block sits in the sheet. */
  .pb-steps{grid-template-columns:1fr;gap:26px}
  .pb-detail{grid-template-columns:1fr}
  .pb-buy{position:static}
}
@media (max-width:1000px){
  .pb-nav{display:none}
  .pb-nav.open{display:flex;position:absolute;top:100%;left:0;right:0;flex-direction:column;
    align-items:stretch;background:var(--cream-50);border-bottom:1px solid var(--line);padding:12px;gap:5px;
    box-shadow:var(--shadow-card)}
  .pb-nav.open .link{text-align:left;width:100%}
  .pb-burger{display:flex}
  .pb-head-in{position:relative}
  .pb-strip-in{grid-template-columns:1fr 1fr;row-gap:20px}
  .pb-strip-item:nth-child(3){border-left:0;padding-left:0}
  .pb-foot-links{grid-template-columns:1fr 1fr;gap:22px}
}
@media (max-width:560px){
  .pb-sec{padding-block:56px}
  .pb-strip-in{grid-template-columns:1fr}
  .pb-strip-item{border-left:0;padding-left:0}
  .pb-foot-links{grid-template-columns:1fr;gap:4px}
  .pb-ticket{padding:22px}
  .pb-quote{padding:56px 20px}
  .pb-sec-mandala{width:340px;height:340px}
}

/* Tablets keep the three steps side by side; phones stack them. Placed last
   on purpose — an earlier max-width:980px rule also targets .pb-steps, and
   with equal specificity the later block wins. That ordering is exactly how
   this collapsed to a single column across the whole tablet range. */
@media (min-width:641px) and (max-width:980px){
  .pb-steps{grid-template-columns:repeat(3,1fr);gap:18px}
}

/* ---------- LEGAL PAGES ---------- */
.lg-doc{max-width:760px}
.lg-head{padding-bottom:24px;margin-bottom:8px;border-bottom:1px solid var(--line)}
.lg-head h1{font-family:var(--font-display);font-size:clamp(27px,4vw,38px);font-weight:600;
  line-height:1.15;margin:0 0 12px;color:var(--ink-900)}
.lg-head p{margin:0;font-size:16px;line-height:1.65;color:var(--ink-600);max-width:62ch}
.lg-block{padding:26px 0;border-bottom:1px solid var(--line)}
.lg-block:last-of-type{border-bottom:0}
.lg-block h2{font-family:var(--font-display);font-size:19px;font-weight:600;margin:0 0 14px;
  color:var(--brand-700);letter-spacing:-.005em}
.lg-block ul{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:12px}
.lg-block li{position:relative;padding-left:20px;font-size:15px;line-height:1.7;color:var(--ink-600)}
.lg-block li::before{content:"";position:absolute;left:2px;top:10px;width:6px;height:6px;border-radius:50%;
  background:var(--gold-500)}
.lg-who{background:var(--cream-100);border:1px solid var(--line);border-radius:var(--radius-lg);
  padding:24px 26px;margin-top:26px}
.lg-dl{margin:0;display:grid;gap:11px}
.lg-dl > div{display:grid;grid-template-columns:170px 1fr;gap:14px;align-items:baseline}
.lg-dl dt{font-size:12.5px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;
  color:var(--ink-400);margin:0}
.lg-dl dd{margin:0;font-size:14.5px;color:var(--ink-900);line-height:1.55;min-width:0;overflow-wrap:anywhere}
.lg-dl a{color:var(--brand-700);text-decoration:underline;text-underline-offset:2px}
.lg-updated{margin:18px 0 0;font-size:12.5px;color:var(--ink-400)}

/* A 170px label column leaves nothing for a long registered address. */
@media (max-width:640px){
  .lg-block{padding:22px 0}
  .lg-who{padding:20px 18px}
  .lg-dl > div{grid-template-columns:1fr;gap:3px}
  .lg-dl dt{font-size:11.5px}
}


/* The footer's two halves stack below 900px; the divider becomes a rule
   between them rather than beside them. */
@media (max-width:900px){
  .pb-foot-in{grid-template-columns:1fr}
  .pb-foot-brand{border-right:0;border-bottom:1px solid var(--line)}
}

/* Newsletter on a phone. Two fixes, both learned the hard way:
   - 16px on the input. The baseline rule .pb-root input{font-size:16px} and
     .pb-news-row input{font-size:14.5px} have identical specificity, so the
     later one won and iOS would have zoomed the whole page on focus — exactly
     the bug the baseline rule exists to prevent.
   - Stacked, because side by side the button took 114px of 257px and left the
     address field 130px to type an email into. */
@media (max-width:560px){
  .pb-news-row{flex-direction:column;border-radius:16px;padding:6px;gap:6px;max-width:none}
  .pb-news-row input{font-size:16px;padding:11px 12px;width:100%}
  .pb-news-btn{width:100%;padding:13px 22px;border-radius:12px}
}

/* Footer links on a phone. The coarse-pointer baseline already gives every
   button a 44px touch target, so the 11px margin on top of it pushed each
   link 55px apart and made the footer enormous. Drop the margin and let the
   touch target do the spacing; separate the groups instead. */
@media (max-width:640px){
  .pb-foot a,.pb-foot .flink{margin-bottom:0;display:flex;align-items:center}
  .pb-foot-links > div + div{margin-top:18px;padding-top:18px;border-top:1px solid var(--line)}
  .pb-foot h5{margin-bottom:6px}
  .pb-foot-contact{padding:6px 0}
}

/* Note on a page pinned to English, shown only to a Hindi reader. */
.lg-enonly{margin:14px 0 0;font-size:13px;line-height:1.6;color:var(--ink-600);
  background:var(--cream-100);border-left:3px solid var(--gold-500);border-radius:0 8px 8px 0;
  padding:10px 14px;max-width:62ch}

/* ---------- MOBILE VERTICAL RHYTHM ----------
   Desktop spacing on a phone is what made this feel empty. Each section
   carried 56px of padding top AND bottom, the section heading added another
   42px beneath itself, and the dark bands nested a padded section inside a
   padded band — so the measured gap between the catalogue cards and the next
   heading was 229px, and between the report and the resources grid 230px. On
   an 812px screen that is a third of the view showing nothing at all.

   Measured targets here: section-to-section gaps of roughly 64-76px, and a
   page that scrolls in about seven screens rather than nine and a half. */
@media (max-width:640px){
  /* padding-block, not the padding shorthand: .pb-sec-narrow carries the
     side padding, shares the .pb-sec class, and is declared earlier in the
     sheet — a shorthand here wiped its padding-inline and ran the legal pages
     edge to edge on a phone. */
  .pb-sec{padding-block:38px}
  .pb-sec-head{margin-bottom:24px}
  .pb-sec-coupon{padding-block:34px}
  .pb-quote{padding:40px 20px}
  .pb-show-grid{padding:38px 20px;gap:26px}
  .pb-strip-in{padding:20px 20px}
  .pb-hero-grid{padding:30px 20px 36px;gap:20px}
  .pb-stage{min-height:190px}
  .pb-steps{gap:18px}
  .pb-step{padding:20px 18px}
  .pb-sec-mandala{width:280px;height:280px;top:-40px}
}
`;

const money = (n) => "₹" + Number(n || 0).toLocaleString("en-IN", { maximumFractionDigits: 0 });

/* Scroll reveal — observes once, then forgets the element. */
function useReveal(deps = []) {
  const root = useRef(null);
  useEffect(() => {
    const el = root.current;
    if (!el) return;
    const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const showAll = () => el.querySelectorAll(".reveal:not(.in)").forEach((n) => n.classList.add("in"));

    if (reduced || !("IntersectionObserver" in window)) { showAll(); return; }

    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });

    const observeAll = () => el.querySelectorAll(".reveal:not(.in)").forEach((n) => io.observe(n));
    observeAll();

    // Filtering the catalogue replaces every card with a brand-new node.
    // Those nodes were never observed, so they stayed at opacity 0 and the
    // whole section appeared to vanish the moment anyone tapped an exam tab.
    // Watching the tree means no future filter has to remember to add itself
    // to this hook's dependency list — the class of bug is gone, not just the
    // one instance of it.
    const mo = new MutationObserver(observeAll);
    mo.observe(el, { childList: true, subtree: true });

    // Failsafe. An animation that fails should cost a fade, never the content:
    // anything still hidden after a moment is shown regardless.
    const failsafe = setTimeout(showAll, 1600);

    return () => { io.disconnect(); mo.disconnect(); clearTimeout(failsafe); };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps);
  return root;
}

function BrandMark({ size = 40 }) {
  return (
    <span className="pb-mark" style={{ width: size, height: size }}>
      <svg width={size * 0.46} height={size * 0.46} viewBox="0 0 24 24" fill="none" aria-hidden="true">
        <path d="M12 2c2 3-1 4-1 7a3 3 0 1 0 6 0c0-2-1-3-1-4 3 2 5 6 5 9a8 8 0 1 1-16 0c0-5 4-8 7-12z" fill="#e3c877" />
      </svg>
    </span>
  );
}

/* ------------------------------------------------------------------ card -- */
function BundleCard({ b, owned, onView, onEnroll, delay = 1 }) {
  const { t } = useLang();
  const off = b.mrp && b.mrp > b.price ? Math.round((1 - b.price / b.mrp) * 100) : 0;
  // A bundle with no published test is not something anyone should be able to
  // pay for. It is shown, so the exam still appears in the catalogue and the
  // interest is visible, but it cannot be bought until a paper exists in it.
  const empty = !b.testCount;
  return (
    <div className={`pb-card reveal reveal-d${delay}${empty ? " pb-card-soon" : ""}`}>
      <span className="pb-card-exam" title={b.examFullName || undefined}>{b.examLabel}</span>
      <h3 className="pb-card-title">{b.name}</h3>
      <div className="pb-card-meta">
        {empty
          ? t("card_papers_soon")
          : `${b.testCount} ${b.testCount === 1 ? t("card_mock_one") : t("card_mock_many")}`}
        {!empty && b.freeTestCount > 0 ? ` · ${b.freeTestCount} ${t("card_free_try")}` : ""}
        {b.durationDays ? ` · ${Math.round(b.durationDays / 30)} ${t("card_months")}` : ` · ${t("card_lifetime")}`}
      </div>
      <p className="pb-card-desc">{b.tagline || b.description}</p>
      <div className="pb-price-row">
        <span className="pb-price">{money(b.price)}</span>
        {off > 0 && <><span className="pb-price-mrp">{money(b.mrp)}</span><span className="pb-off">{off}% off</span></>}
      </div>
      <div className="pb-card-btns">
        {owned ? (
          <button className="pb-btn pb-btn-block pb-owned" onClick={onView}>
            <CheckCircle2 size={16} />{t("card_owned")}
          </button>
        ) : empty ? (
          <button className="pb-btn pb-btn-block pb-soon" disabled title="No papers in this series yet">
            <Timer size={16} />{t("card_soon")}
          </button>
        ) : (
          <>
            <button className="pb-btn pb-btn-maroon" style={{ flex: 1 }} onClick={onEnroll}>
              {t("card_enroll")}<ArrowRight size={15} />
            </button>
            <button className="pb-btn pb-btn-ghost pb-btn-sm" onClick={onView}>{t("card_details")}</button>
          </>
        )}
      </div>
    </div>
  );
}

/* Only the profiles that are actually configured are rendered. An icon that
   opens a 404 — or somebody else's account — is worse than no icon, so the
   defaults in legal.js are empty and this filters them out. */
const SOCIAL_DEFS = [
  { key: "instagram", label: "Instagram", Icon: Instagram },
  { key: "youtube",   label: "YouTube",   Icon: YouTube },
  { key: "telegram",  label: "Telegram",  Icon: Telegram },
  { key: "whatsapp",  label: "WhatsApp",  Icon: WhatsApp },
  { key: "linkedin",  label: "LinkedIn",  Icon: LinkedIn },
  { key: "x",         label: "X",         Icon: XMark },
];
/* Every icon is placed so the row is designed and spaced now; the ones
   without a URL yet render as inert placeholders rather than links to
   nowhere. Fill a handle in SOCIAL_LINKS and that icon becomes live with no
   further change here. */
const SOCIALS = SOCIAL_DEFS.map((d) => ({ ...d, href: (SOCIAL_LINKS[d.key] || "").trim() }));

/* ---------------------------------------------------------------- detail -- */
function BundleDetail({ code, owned, onBack, onEnroll }) {
  const { t } = useLang();
  const [bundle, setBundle] = useState(null);
  const [tests, setTests] = useState([]);
  const [err, setErr] = useState("");
  const [reloadKey, setReloadKey] = useState(0);

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const [b, t] = await Promise.all([DB.getBundle(code), DB.bundleTests(code)]);
        if (!alive) return;
        if (!b) { setErr("This test series is no longer available."); return; }
        setErr(""); setBundle(b); setTests(t);
      } catch (e) {
        console.error(e);
        if (alive) setErr(e?.message || "Couldn't load this test series.");
      }
    })();
    return () => { alive = false; };
  }, [code, reloadKey]);

  if (err) {
    return (
      <div className="pb-sec pb-sec-narrow">
        <div className="pb-panel"><ErrorState message={err} onRetry={() => setReloadKey((k) => k + 1)} /></div>
      </div>
    );
  }
  if (!bundle) {
    return (
      <div className="pb-sec pb-sec-narrow">
        <Skeleton h={24} w="42%" /><Skeleton h={14} w="66%" style={{ marginTop: 14 }} />
        <Skeleton h={280} style={{ marginTop: 26 }} />
      </div>
    );
  }

  const off = bundle.mrp && bundle.mrp > bundle.price ? Math.round((1 - bundle.price / bundle.mrp) * 100) : 0;

  return (
    <div className="pb-sec pb-sec-narrow">
      <button className="pb-btn pb-btn-ghost pb-btn-sm" style={{ marginBottom: 24 }} onClick={onBack}>
        <ArrowLeft size={15} />All test series
      </button>

      <div className="pb-detail">
        <div>
          <span className="pb-card-exam" title={bundle.examFullName || undefined}>{bundle.examLabel}</span>
          <h1 className="pb-h2" style={{ textAlign: "left", marginTop: 12 }}>{bundle.name}</h1>
          {bundle.conductedBy && (
            <div style={{ fontSize: 13, color: "var(--ink-400)", marginBottom: 10 }}>
              Conducted by <b style={{ color: "var(--ink-600)" }}>{bundle.conductedBy}</b>
              {bundle.examFullName ? ` · ${bundle.examFullName}` : ""}
            </div>
          )}
          <p className="pb-sub" style={{ margin: "0 0 26px" }}>{bundle.description || bundle.tagline}</p>

          <div className="pb-panel" style={{ marginBottom: 20 }}>
            <div className="pb-kicker">{t("card_included")}</div>
            <ul className="pb-list">
              {bundle.features.map((f, i) => <li key={i}><CheckCircle2 size={17} />{f}</li>)}
            </ul>
          </div>

          <div className="pb-panel">
            <div className="pb-kicker">{t("card_tests_in")}</div>
            <div className="pb-h3">{tests.length} test{tests.length === 1 ? "" : "s"} published</div>
            {tests.length === 0 ? (
              <p style={{ fontSize: 14, color: "var(--ink-400)", lineHeight: 1.7, margin: 0 }}>
                Tests for this series are being finalised. Enrolling now locks in the current price and
                gives you every test as it is released.
              </p>
            ) : tests.map((t, i) => (
              <div className="pb-trow" key={t.id}>
                <span className="pb-tnum">{i + 1}</span>
                <div className="pb-tname">
                  {t.title}
                  <div className="pb-tmeta">
                    {t.totalQuestions} questions · {t.durationMin} min
                    {t.totalMarks > 0 ? ` · ${t.totalMarks} marks` : ""}
                  </div>
                </div>
                {t.isFree
                  ? <span className="pb-off">{t("card_free_sample")}</span>
                  : <Lock size={15} style={{ color: "var(--ink-400)", flex: "0 0 auto" }} />}
              </div>
            ))}
          </div>
        </div>

        <div className="pb-panel pb-buy">
          <div className="pb-price-row" style={{ marginBottom: 8 }}>
            <span className="pb-price" style={{ fontSize: 32 }}>{money(bundle.price)}</span>
            {off > 0 && <span className="pb-price-mrp">{money(bundle.mrp)}</span>}
          </div>
          {off > 0 && <div className="pb-off" style={{ display: "inline-block", marginBottom: 14 }}>{off}% off</div>}
          <p style={{ fontSize: 13.5, color: "var(--ink-600)", margin: "0 0 20px", lineHeight: 1.6 }}>
            {bundle.durationDays
              ? `One-time payment · valid for ${Math.round(bundle.durationDays / 30)} months`
              : "One-time payment · lifetime access"}
          </p>
          <button className={"pb-btn pb-btn-block " + (owned ? "pb-owned" : "pb-btn-gold")} onClick={onEnroll}>
            {owned ? <><CheckCircle2 size={16} />{t("card_goto_dash")}</> : <>Enroll now<ArrowRight size={15} /></>}
          </button>
          <div style={{ display: "flex", flexDirection: "column", gap: 9, marginTop: 18 }}>
            <span style={{ fontSize: 12.5, color: "var(--ink-400)", display: "flex", alignItems: "center", gap: 7 }}>
              <Lock size={12} />Secure payment via Razorpay
            </span>
            <span style={{ fontSize: 12.5, color: "var(--ink-400)", display: "flex", alignItems: "center", gap: 7 }}>
              <ShieldCheck size={12} />Coupons apply at checkout
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}

/* ------------------------------------------------------------------ site -- */
export default function PublicSite({ onLogin, onEnroll, onDashboard, session, page, onNavigate }) {
  const { t } = useLang();
  const [bundles, setBundles] = useState(null);
  const [err, setErr] = useState("");
  const [exam, setExam] = useState("all");
  const tabsRef = useRef(null);

  /* Footer newsletter. Deliberately available to signed-out visitors — that is
     the entire point of a footer form. */
  const [email, setEmail] = useState("");
  const [newsBusy, setNewsBusy] = useState(false);
  const [news, setNews] = useState(null);

  const subscribe = async (e) => {
    e.preventDefault();
    if (newsBusy) return;
    setNewsBusy(true);
    setNews(null);
    try {
      const r = await DB.subscribeEmail(email);
      if (r.ok) {
        // "Already on the list" is a success to the reader, not an error.
        setNews({ ok: true, msg: r.reason === "already" ? t("news_already") : t("news_ok") });
        setEmail("");
      } else {
        setNews({ ok: false, msg: r.reason === "invalid" ? t("news_bad") : t("news_fail") });
      }
    } catch {
      setNews({ ok: false, msg: t("news_fail") });
    } finally {
      setNewsBusy(false);
    }
  };

  /* Filtering removes cards, so the page gets shorter while the browser keeps
     scrollY exactly where it was — on a phone that silently pushes the whole
     catalogue up off the top of the screen. Re-anchor the tab row whenever it
     ends up outside the viewport after a filter change. */
  const pickExam = (code) => {
    setExam(code);
    requestAnimationFrame(() => {
      const el = tabsRef.current;
      if (!el) return;
      const { top } = el.getBoundingClientRect();
      if (top < 64 || top > window.innerHeight - 140) {
        el.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  };
  const [detail, setDetail] = useState(null);
  const [owned, setOwned] = useState(new Set());
  const [contact, setContact] = useState(false);
  const [navOpen, setNavOpen] = useState(false);
  const [reloadKey, setReloadKey] = useState(0);

  const userId = session?.user?.id ?? null;
  const revealRoot = useReveal([page, detail, bundles]);

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const list = await DB.listBundles();
        if (!alive) return;
        setErr(""); setBundles(list);
        if (userId) {
          const mine = await DB.myPlanCodes(userId);
          if (alive) setOwned(mine);
        }
      } catch (e) {
        console.error("catalog load failed", e);
        if (alive) { setErr(e?.message || "Couldn't load the catalogue."); setBundles([]); }
      }
    })();
    return () => { alive = false; };
  }, [userId, reloadKey]);

  // One tab per exam that actually has a bundle, ordered by the exam's own
  // sort_order so UPSC leads and "Other" trails.
  const examTabs = [];
  const seen = new Set();
  (bundles || []).forEach((b) => {
    if (seen.has(b.exam)) return;
    seen.add(b.exam);
    examTabs.push({ code: b.exam, label: b.examLabel, sort: b.examSort });
  });
  examTabs.sort((a, b) => a.sort - b.sort);
  const shown = (bundles || []).filter((b) => exam === "all" || b.exam === exam);
  const totalTests = (bundles || []).reduce((s, b) => s + b.testCount, 0);
  const freeTests = (bundles || []).reduce((s, b) => s + b.freeTestCount, 0);

  const scrollTo = (id) => setTimeout(() => document.getElementById(id)?.scrollIntoView({ behavior: "smooth" }), 70);
  const goCatalog = () => { setDetail(null); if (page) onNavigate(null); scrollTo("catalog"); };
  const goResources = () => { setDetail(null); if (page) onNavigate(null); scrollTo("resources"); };
  const enroll = (code) => (owned.has(code) ? onDashboard() : onEnroll(code));
  const home = () => { setDetail(null); onNavigate(null); window.scrollTo({ top: 0, behavior: "smooth" }); };

  return (
    <div className="pb-root" ref={revealRoot}>
      <style>{CSS}</style>

      <header className="pb-head">
        <div className="pb-head-in">
          <button className="pb-brand" onClick={home}>
            <BrandMark />
            <span>
              <span className="pb-name">JUNOON<span>IAS</span></span>
              <span className="pb-tagline">{t("tagline")}</span>
            </span>
          </button>

          <button className="pb-burger" onClick={() => setNavOpen(!navOpen)} aria-label="Menu" aria-expanded={navOpen}>
            {navOpen ? <X size={19} /> : <Menu size={19} />}
          </button>

          <nav className={"pb-nav" + (navOpen ? " open" : "")}>
            <button className="link" onClick={() => { setNavOpen(false); goCatalog(); }}>{t("nav_tests")}</button>
            <button className="link" onClick={() => { setNavOpen(false); onNavigate("syllabus"); }}>{t("nav_syllabus")}</button>
            <button className="link" onClick={() => { setNavOpen(false); goResources(); }}>{t("nav_free")}</button>
            <button className="link" onClick={() => { setNavOpen(false); onNavigate("faq"); }}>{t("nav_faq")}</button>
            <ChromeControls palettePicker />
            {session
              ? <button className="pb-btn pb-btn-maroon pb-btn-sm" onClick={onDashboard}>{t("nav_dashboard")}<ArrowRight size={15} /></button>
              : (
                <>
                  <button className="pb-btn pb-btn-ghost pb-btn-sm" onClick={onLogin}>{t("nav_login")}</button>
                  <button className="pb-btn pb-btn-gold pb-btn-sm" onClick={goCatalog}>{t("nav_start")}</button>
                </>
              )}
          </nav>
        </div>
      </header>

      {page ? (
        <div className="pb-sec pb-sec-narrow">
          <button className="pb-btn pb-btn-ghost pb-btn-sm" style={{ marginBottom: 24 }} onClick={home}>
            <ArrowLeft size={15} />{t("back_home")}
          </button>
          {/* Legal pages carry their own heading and a different tone —
              "Free · no login needed" over a refund policy reads as a joke. */}
          {RESOURCE_TITLES[page] && (
            <div style={{ marginBottom: 28 }}>
              <div className="pb-eyebrow">{t("free_no_login")}</div>
              <h1 className="pb-h2" style={{ margin: "10px 0 10px" }}>{t(RESOURCE_TITLES[page]?.tKey)}</h1>
              <p className="pb-sub">{t(RESOURCE_TITLES[page]?.sKey)}</p>
            </div>
          )}
          <ContentPage page={page} />
        </div>
      ) : detail ? (
        <BundleDetail code={detail} owned={owned.has(detail)} onBack={goCatalog} onEnroll={() => enroll(detail)} />
      ) : (
        <>
          {/* ---------------- HERO ---------------- */}
          <section className="pb-hero">
            <div className="pb-hero-grid">
              <div>
                <div className="pb-hero-deva">तमसो मा ज्योतिर्गमय</div>
                <h1 className="pb-h1">{t("hero_h1_a")}{" "}<br /><em>{t("hero_h1_b")}</em></h1>
                <p className="pb-lede">{t("hero_lede")}</p>
                <div className="pb-hero-ctas">
                  <button className="pb-btn pb-btn-gold" onClick={goCatalog}>
                    {t("cta_explore")}<ArrowRight size={17} />
                  </button>
                  <button className="pb-btn pb-btn-onDark" onClick={goResources}>{t("cta_browse_free")}</button>
                </div>
                <ul className="pb-ticks">
                  <li><CheckCircle2 size={16} />{t("tick_pattern")}</li>
                  <li><CheckCircle2 size={16} />{t("tick_rank")}</li>
                  <li><CheckCircle2 size={16} />{t("tick_nologin")}</li>
                </ul>
              </div>
              <div className="pb-stage"><Diya size={330} /></div>
            </div>
          </section>

          {/* ---------------- STRIP ----------------
              Every line here is checkable against the product. The old site
              claimed "1000+ aspirants" against 12 registered accounts; that
              claim is gone rather than restyled. */}
          <div className="pb-strip">
            <div className="pb-strip-in">
              <div className="pb-strip-item"><b>{t("strip1_t")}</b>{t("strip1_d")}</div>
              <div className="pb-strip-item"><b>{t("strip2_t")}</b>{t("strip2_d")}</div>
              <div className="pb-strip-item"><b>{t("strip3_t")}</b>{t("strip3_d")}</div>
              <div className="pb-strip-item"><b>{t("strip4_t")}</b>{t("strip4_d")}</div>
            </div>
          </div>

          {/* ---------------- CATALOG ---------------- */}
          <section className="pb-sec" id="catalog">
            <div className="pb-sec-narrow">
              <div className="pb-sec-head reveal">
                <Mandala className="pb-sec-mandala" />
                <div className="pb-eyebrow">{t("nav_tests")}</div>
                <h2 className="pb-h2">{t("cat_h2")}</h2>
                <p className="pb-sub">{t("cat_sub")}</p>
              </div>

              {examTabs.length > 1 && (
                <div className="pb-tabs reveal" ref={tabsRef}>
                  <button className={"pb-tab" + (exam === "all" ? " on" : "")} onClick={() => pickExam("all")}>
                    {t("tab_all")}
                  </button>
                  {examTabs.map((e) => (
                    <button key={e.code} className={"pb-tab" + (exam === e.code ? " on" : "")}
                            onClick={() => pickExam(e.code)}>
                      {e.label}
                    </button>
                  ))}
                </div>
              )}

              {err ? (
                <div className="pb-panel"><ErrorState message={err} onRetry={() => setReloadKey((k) => k + 1)} /></div>
              ) : bundles === null ? (
                <div className="pb-grid">
                  {[0, 1, 2].map((i) => (
                    <div className="pb-card" key={i}>
                      <Skeleton h={18} w="40%" /><Skeleton h={24} w="86%" style={{ marginTop: 14 }} />
                      <Skeleton h={13} w="66%" style={{ marginTop: 10 }} /><Skeleton h={64} style={{ marginTop: 20 }} />
                    </div>
                  ))}
                </div>
              ) : shown.length === 0 ? (
                <div className="pb-panel" style={{ textAlign: "center", color: "var(--ink-600)" }}>
                  {t("cat_empty")}
                </div>
              ) : (
                <div className="pb-grid">
                  {shown.map((b, i) => (
                    <BundleCard key={b.code} b={b} owned={owned.has(b.code)} delay={(i % 3) + 1}
                      onView={() => { setDetail(b.code); window.scrollTo({ top: 0, behavior: "smooth" }); }}
                      onEnroll={() => enroll(b.code)} />
                  ))}
                </div>
              )}
            </div>
          </section>

          {/* ---------------- HOW IT WORKS ---------------- */}
          <section className="pb-sec" style={{ paddingTop: 0 }}>
            <div className="pb-sec-narrow">
              <div className="pb-sec-head reveal">
                <div className="pb-eyebrow">{t("how_eyebrow")}</div>
                <h2 className="pb-h2">{t("how_h2")}</h2>
                <p className="pb-sub">{t("how_sub")}</p>
              </div>
              <div className="pb-steps">
                {[
                  { k: "step1" }, { k: "step2" }, { k: "step3" },
                ].map((s, i) => (
                  <div className={`pb-step reveal reveal-d${i + 1}`} key={s.k}>
                    <span className="pb-step-n">{i + 1}</span>
                    <StepArt step={i + 1} />
                    <h3>{t(`${s.k}_t`)}</h3>
                    <p>{t(`${s.k}_d`)}</p>
                  </div>
                ))}
              </div>
            </div>
          </section>

          {/* ---------------- REPORT SHOWCASE ---------------- */}
          <section className="pb-show">
            <div className="pb-show-grid">
              <div className="reveal">
                <div className="pb-eyebrow">{t("rep_eyebrow")}</div>
                <h2 className="pb-h2" style={{ textAlign: "left" }}>{t("rep_h2")}</h2>
                <p className="pb-sub">{t("rep_sub")}</p>
                <ul className="pb-show-list">
                  <li>
                    <span className="pb-show-ic"><Target size={17} /></span>
                    <span><b>{t("rep1_t")}</b><em>{t("rep1_d")}</em></span>
                  </li>
                  <li>
                    <span className="pb-show-ic"><Timer size={17} /></span>
                    <span><b>{t("rep2_t")}</b><em>{t("rep2_d")}</em></span>
                  </li>
                  <li>
                    <span className="pb-show-ic"><Layers size={17} /></span>
                    <span><b>{t("rep3_t")}</b><em>{t("rep3_d")}</em></span>
                  </li>
                  <li>
                    <span className="pb-show-ic"><CheckCircle2 size={17} /></span>
                    <span><b>{t("rep4_t")}</b><em>{t("rep4_d")}</em></span>
                  </li>
                </ul>
              </div>
              <div className="reveal reveal-d2"><ReportArt /></div>
            </div>
          </section>

          {/* ---------------- FREE RESOURCES ---------------- */}
          <section className="pb-res" id="resources">
            <Mandala className="pb-res-mandala" />
            <div className="pb-sec pb-sec-narrow" style={{ position: "relative", zIndex: 2 }}>
              <div className="pb-sec-head reveal">
                <div className="pb-eyebrow">{t("res_eyebrow")}</div>
                <h2 className="pb-h2">{t("res_h2")}</h2>
                <p className="pb-sub">{t("res_sub")}</p>
              </div>
              <div className="pb-resgrid">
                {RESOURCES.map((r, i) => {
                  const Icon = r.icon;
                  return (
                    <button className={`pb-rescard reveal reveal-d${(i % 4) + 1}`} key={r.key}
                            onClick={() => onNavigate(r.key)}>
                      <Icon size={26} />
                      <h4>{t(r.labelKey)}</h4>
                      <p>{t(r.blurbKey)}</p>
                    </button>
                  );
                })}
              </div>
              {totalTests > 0 && (
                <p style={{ textAlign: "center", marginTop: 30, fontSize: 13.5, color: "#c9b998" }}>
                  {totalTests} {totalTests === 1 ? t("card_mock_one") : t("card_mock_many")}{" "}
                  {t("res_published")} {bundles?.length ?? 0} {t("res_series_word")}
                  {freeTests > 0 ? ` · ${freeTests} ${t("res_free_try")}` : ""}
                </p>
              )}
            </div>
          </section>

          {/* ---------------- COUPON ---------------- */}
          <div className="pb-sec pb-sec-narrow pb-sec-coupon">
            <div className="pb-ticket-wrap"><div className="pb-ticket reveal">
              <span className="pb-notch pb-notch-l" />
              <span className="pb-ticket-ic"><TicketIcon size={24} /></span>
              <div style={{ flex: 1, minWidth: 0 }}>
                <h4>{t("coupon_h4")}</h4>
                <p>{t("coupon_p")}</p>
              </div>
              <button className="pb-btn pb-btn-maroon" style={{ flex: "0 0 auto" }} onClick={goCatalog}>
                {t("coupon_cta")}<ArrowRight size={15} />
              </button>
              <span className="pb-notch pb-notch-r" />
            </div></div>
          </div>

          {/* ---------------- QUOTE ---------------- */}
          <div className="pb-quote">
            <Divider className="pb-quote-rule" />
            <div className="deva">तमसो मा ज्योतिर्गमय</div>
            <p>{t("shloka_en")}</p>
            <div className="src">{t("shloka_src")}</div>
          </div>
        </>
      )}

      {/* ---------------- FOOTER ----------------
          One inset card rather than a full-bleed band, so the page ends
          deliberately. Left half carries who we are and the newsletter; right
          half the link columns; the legal line sits outside the card. */}
      <footer className="pb-foot">
        <div className="pb-foot-card">
          <div className="pb-foot-in">

            <div className="pb-foot-brand">
              <div className="pb-foot-logo">
                <BrandMark size={40} />
                <span>
                  <span className="pb-name">JUNOON<span>IAS</span></span>
                  <span className="pb-tagline">{t("tagline")}</span>
                </span>
              </div>
              <p className="pb-foot-blurb">{t("foot_blurb")}</p>

              <div className="pb-news">
                <h5>{t("news_h")}</h5>
                <p>{t("news_p")}</p>
                <form className="pb-news-row" onSubmit={subscribe}>
                  <input
                    type="email" inputMode="email" autoComplete="email"
                    value={email} onChange={(e) => { setEmail(e.target.value); setNews(null); }}
                    placeholder={t("news_ph")} aria-label={t("news_h")}
                  />
                  <button className="pb-news-btn" type="submit" disabled={newsBusy}>
                    {newsBusy ? t("news_sending") : t("news_btn")}
                  </button>
                </form>
                {news && (
                  <p className={"pb-news-msg " + (news.ok ? "ok" : "bad")} role="status">
                    {news.ok ? <CheckCircle2 size={14} style={{ flex: "0 0 auto", marginTop: 1 }} /> : null}
                    <span>{news.msg}</span>
                  </p>
                )}
              </div>

              <div className="pb-socials">
                {SOCIALS.map((sc) => (sc.href ? (
                  <a className="pb-social" key={sc.label} href={sc.href} aria-label={sc.label}
                     target="_blank" rel="noreferrer noopener">
                    <sc.Icon size={17} />
                  </a>
                ) : (
                  <span className="pb-social pb-social-soon" key={sc.label}
                        title={sc.label + " — " + t("soc_soon")} aria-hidden="true">
                    <sc.Icon size={17} />
                  </span>
                )))}
              </div>
            </div>

            <div className="pb-foot-links">
              <div>
                <h5>{t("foot_explore")}</h5>
                <button className="flink" onClick={goCatalog}>{t("nav_tests")}</button>
                <button className="flink" onClick={() => onNavigate("syllabus")}>{t("nav_syllabus")}</button>
                <button className="flink" onClick={() => onNavigate("pyq")}>{t("foot_pyq")}</button>
                <button className="flink" onClick={session ? onDashboard : onLogin}>
                  {session ? t("foot_mydash") : t("nav_login")}
                </button>
              </div>
              <div>
                <h5>{t("foot_free")}</h5>
                <button className="flink" onClick={() => onNavigate("materials")}>{t("foot_material")}</button>
                <button className="flink" onClick={() => onNavigate("ncert")}>{t("foot_ncert")}</button>
                <button className="flink" onClick={() => onNavigate("news")}>{t("foot_news")}</button>
                <button className="flink" onClick={() => onNavigate("faq")}>{t("nav_faq")}</button>
              </div>
              <div>
                <h5>{t("foot_support")}</h5>
                <p className="pb-foot-contact">
                  <a href={"mailto:" + COMPANY.email}>{COMPANY.email}</a>
                </p>
                <button className="flink" style={{ marginTop: 10 }} onClick={() => setContact(true)}>
                  <Headphones size={13} style={{ verticalAlign: -2, marginRight: 6 }} />{t("foot_help")}
                </button>
                <button className="flink" onClick={() => onNavigate("contact")}>{t("lg_contact")}</button>
                <button className="flink" onClick={() => onNavigate("refund")}>{t("lg_refund")}</button>
              </div>
            </div>

          </div>
        </div>

        <div className="pb-foot-bottom">
          <span>&copy; {new Date().getFullYear()} JUNOONIAS. {t("foot_rights")}</span>
          <div className="pb-foot-legal">
            <button onClick={() => onNavigate("privacy")}>{t("lg_privacy")}</button>
            <button onClick={() => onNavigate("terms")}>{t("lg_terms")}</button>
            <button onClick={() => onNavigate("refund")}>{t("lg_refund")}</button>
            <span>{t("foot_made")}</span>
          </div>
        </div>
      </footer>

      {contact && <ContactModal onClose={() => setContact(false)} />}
    </div>
  );
}
