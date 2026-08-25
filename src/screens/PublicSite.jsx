import { Fragment, useState, useEffect, useRef, useMemo, useLayoutEffect } from "react";
import {
  CheckCircle2, ArrowRight, ArrowLeft, Lock, Headphones, Menu, X,
  ShieldCheck, Layers, Target, Timer, Compass, BookOpen, BarChart3, Gift, Calculator, History,
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

/* A target with an arrow in the bullseye -- built to the real pattern, and it
   hits. Drawn to sit with the lucide icons around it: 24 viewBox, 2px round
   strokes, currentColor, no fill. */
function TargetArrow({ size = 18 }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none"
         stroke="currentColor" strokeWidth="2" strokeLinecap="round"
         strokeLinejoin="round" aria-hidden="true" role="presentation">
      <circle cx="10.5" cy="13.5" r="8.2" />
      <circle cx="10.5" cy="13.5" r="3.3" />
      <path d="M21.5 2.5 10.5 13.5" />
      <path d="M14.8 13.5 10.5 13.5 10.5 9.2" />
    </svg>
  );
}

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
/* The header reacts to the page moving under it: translucent and weightless
   at the top, denser and lifted once you scroll. That one change is most of
   what separates a header that feels built from one that feels placed. */
.pb-head{position:sticky;top:0;z-index:50;
  -webkit-backdrop-filter:blur(12px) saturate(1.2);
  backdrop-filter:blur(12px) saturate(1.2);
  /* Solid first, translucent second. A browser without color-mix() drops
     the second line and keeps a usable opaque header; without the first it
     would drop the only background it has and leave dark nav text sitting
     on the dark hero. Same trap the footer fell into. */
  background:var(--cream-50);
  background:color-mix(in srgb,var(--cream-50) 84%,transparent);
  transition:background .3s ease, box-shadow .3s ease}
/* A hairline that is line-coloured at the ends and gold through the middle,
   so the header is closed off by something belonging to the brand rather
   than by a grey rule. */
.pb-head::after{content:"";position:absolute;left:0;right:0;bottom:0;height:1px;pointer-events:none;
  background:linear-gradient(90deg,transparent,
    color-mix(in srgb,var(--line) 92%,transparent) 16%,
    color-mix(in srgb,var(--gold-500) 60%,transparent) 50%,
    color-mix(in srgb,var(--line) 92%,transparent) 84%,transparent);
  opacity:.85;transition:opacity .3s ease}
.pb-head-on{
  background:var(--cream-50);
  background:color-mix(in srgb,var(--cream-50) 95%,transparent);
  -webkit-backdrop-filter:blur(20px) saturate(1.45);
  backdrop-filter:blur(20px) saturate(1.45);
  box-shadow:0 8px 26px -16px rgba(70,40,20,.55)}
.pb-head-on::after{opacity:1}
.pb-head-in{max-width:1180px;margin:0 auto;padding:12px 24px;display:flex;align-items:center;gap:16px}
.pb-brand{display:flex;align-items:center;gap:11px;background:none;border:0;padding:0;cursor:pointer;font-family:inherit}
.pb-mark{border-radius:11px;flex:0 0 auto;display:grid;place-items:center;
  background:linear-gradient(155deg,var(--brand-700),var(--brand-900));box-shadow:var(--shadow-card)}
/* The mark is a diya. A lamp that sits perfectly still is a logo; one that
   breathes is a lamp. Slow enough (5.6s) to be felt rather than watched, and
   drawn with box-shadow so it glows around the tile instead of over it. */
@keyframes pb-mark-glow{
  0%,58%,100%{box-shadow:var(--shadow-card),0 0 10px -3px rgba(201,162,39,.28)}
  79%        {box-shadow:var(--shadow-card),0 0 20px -2px rgba(201,162,39,.62)}
}
.pb-head .pb-mark{animation:pb-mark-glow 7.4s ease-in-out infinite}
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
/* Desktop login. It sits beside the gold "Get started", so it must not shout
   in the same voice — but a bare outline is not worth clicking either. A warm
   tinted ground and a gold rim that lights up under the pointer. */
.pb-btn-ghost{border-color:color-mix(in srgb,var(--gold-600) 55%,transparent);
  color:var(--brand-700);
  background:color-mix(in srgb,var(--gold-100) 45%,transparent);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.5)}
.pb-btn-ghost:hover{border-color:var(--gold-500);
  background:color-mix(in srgb,var(--gold-100) 85%,transparent);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.7),0 6px 16px -8px rgba(201,162,39,.6)}
@keyframes pb-ghost-halo{
  0%,62%{ box-shadow:inset 0 1px 0 rgba(255,255,255,.5), 0 0 0 0 rgba(201,162,39,.45) }
  81%   { box-shadow:inset 0 1px 0 rgba(255,255,255,.65),0 0 0 6px rgba(201,162,39,.15) }
  100%  { box-shadow:inset 0 1px 0 rgba(255,255,255,.5), 0 0 0 11px rgba(201,162,39,0) }
}
.pb-nav .pb-btn-ghost{ animation:pb-ghost-halo 5.6s ease-out infinite }
.pb-nav .pb-btn-ghost:hover{ animation:none }
@media (prefers-reduced-motion: reduce){ .pb-nav .pb-btn-ghost{ animation:none } }
.pb-btn-onDark{border:1.5px solid rgba(255,255,255,.34);color:var(--on-dark);background:rgba(255,255,255,.06)}
.pb-btn-onDark:hover{background:rgba(255,255,255,.13)}
.pb-btn-sm{padding:9px 16px;font-size:13.5px}
.pb-btn-block{width:100%}

/* ---------- HERO ---------- */
.pb-hero{position:relative;overflow:hidden;color:var(--on-dark);
  background:linear-gradient(175deg,var(--brand-800) 0%,var(--brand-900) 100%)}
[data-theme="dark"] .pb-hero{background:linear-gradient(175deg,#2a0d13 0%,#150609 100%)}
/* The ground was carrying a 2px diagonal pinstripe every 26px. On a desktop
   it is a faint texture; on a phone at 2x it lands as visible hairlines
   crawling across the maroon, which is what makes the panel look like a
   rendering fault rather than a surface. Gone.

   What replaces it is the one thing the section is about: the lamp lighting
   the space it sits in. A warm pool centred where the diya actually is, and a
   second, wider and much fainter one lifting the top edge so the band does
   not read as flat paint. */
.pb-hero::before{content:"";position:absolute;inset:0;pointer-events:none;
  background:radial-gradient(460px 380px at 78% 34%, rgba(224,178,64,.22), transparent 66%),
             radial-gradient(760px 300px at 50% -18%, rgba(255,255,255,.05), transparent 70%)}
.pb-hero-grid{position:relative;z-index:2;display:grid;grid-template-columns:1.08fr .92fr;gap:0 44px;
  grid-template-areas:"head diya" "body diya" "ticks ticks";
  align-items:center;max-width:1180px;margin:0 auto;padding:74px 24px 66px}
.pb-hero-head{grid-area:head}
.pb-stage{grid-area:diya}
.pb-hero-body{grid-area:body}
.pb-hero-deva{font-family:var(--font-shloka);font-size:19px;letter-spacing:.03em;color:var(--gold-300);
  opacity:.95;margin-bottom:12px;line-height:1.5}
.pb-h1{font-family:var(--font-display);font-optical-sizing:auto;font-size:clamp(36px,5vw,60px);
  line-height:1.07;font-weight:600;letter-spacing:-.012em;margin:0 0 18px;text-wrap:balance}
.pb-h1 em{font-family:var(--font-quote);font-style:italic;font-weight:500;color:var(--gold-300);
  font-size:1.14em;letter-spacing:-.005em}
/* The headline arrives one line at a time. Each line is a block that sweeps
   in as a whole -- a left-to-right wipe with a small lift and fade -- rather
   than a letter at a time. The first line lands, then a beat later the gold
   second line follows. Only opacity, clip-path and transform animate, so the
   two lines hold their final space from the first frame and nothing below the
   headline shifts. */
.pb-h1-anim .pb-h1-l1,
.pb-h1-anim .pb-h1-l2{display:block}
.pb-h1-anim .pb-h1-l1{animation:pb-swoosh .62s cubic-bezier(.2,.75,.3,1) .12s both}
.pb-h1-anim .pb-h1-l2{animation:pb-swoosh .62s cubic-bezier(.2,.75,.3,1) .74s both}
/* Every inset but the right one is NEGATIVE, and that is the whole point.
   fill-mode holds the last frame forever, so a flat inset(0) would keep
   clipping to the line box for the life of the page -- and these glyphs paint
   5px outside it: the descender of "your", the g of "light.", the overhang of
   the italic. Both were visibly sliced. Opening the box on three sides leaves
   the wipe to the right edge alone, which is the only edge that should cut. */
@keyframes pb-swoosh{
  0%  {opacity:0;clip-path:inset(-.4em 100% -.4em -.2em);transform:translateY(.16em)}
  32% {opacity:1}
  100%{opacity:1;clip-path:inset(-.4em -.2em -.4em -.2em);transform:none}
}
/* Reduced motion: both lines are simply present, no sweep. */
@media (prefers-reduced-motion: reduce){
  .pb-h1-anim .pb-h1-l1,.pb-h1-anim .pb-h1-l2{
    animation:none;opacity:1;clip-path:none;transform:none}
}

/* The lede first types itself in, character by character. Once complete, a
   glassmorphism sheen then sweeps across it a line at a time, left to right,
   one line after another, each line taking the same time typing it did.

   A ghost of the finished paragraph is laid out but not painted, holding the
   full block open so the buttons and ticks below never jump; the live copy is
   painted over it. */
.pb-lede-type{position:relative}
.pb-lede-ghost{visibility:hidden}
.pb-lede-live{position:absolute;top:0;left:0;right:0}
.pb-lede-main{display:block}
/* Act two: one visual line during the sheen pass. The text is already there
   (it was typed); only a frosted band crosses it. --d is the line's duration
   and --delay its start, so the lines light one after another. overflow clips
   the band to the line; nowrap keeps the pre-measured line on one row. */
.pb-glass-sheen-line{display:block;position:relative;white-space:nowrap;overflow:hidden}
.pb-glass-sheen-line::after{content:"";position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(100deg,
    transparent 40%,
    rgba(255,255,255,.20) 47%,
    rgba(255,247,224,.60) 50%,
    rgba(240,214,138,.36) 53%,
    transparent 60%);
  mix-blend-mode:screen;transform:translateX(-105%);
  animation:pb-glass-sheen var(--d) linear var(--delay) both}
@keyframes pb-glass-sheen{to{transform:translateX(105%)}}
/* The closing line is mounted only once the typing lands, and fades up from
   that fresh mount so the fade always plays from the start. */
.pb-glass-close-in{animation:pb-fade-up .5s ease both}
@keyframes pb-fade-up{from{opacity:0;transform:translateY(.24em)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion: reduce){
  .pb-glass-sheen-line::after{display:none}
  .pb-glass-close-in{animation:none}
}
/* Read by assistive tech only -- the ghost is visibility:hidden (out of the
   a11y tree) and the live copy is aria-hidden, so this carries the full text. */
.pb-sr{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;
  clip:rect(0 0 0 0);white-space:nowrap;border:0}
/* The lede was 15.5px Inter on a dark ground -- correct, and characterless
   next to two serifs above it. A little more size, a little more line, and a
   measure that stops at 42 characters so it sets in even lines rather than
   one long grey block. */

/* One flowing paragraph in the display serif, so it reads with the same
   voice as the headline rather than as plain UI text -- kept at the lede's
   own size, not the headline's. The four parts run inline with normal word
   spacing and wrap edge to edge; only "real exam" is gold, and the closing
   line stays a gold italic the way the headline's second line is. */
.pb-lede{font-family:var(--font-display);font-optical-sizing:auto;
  font-size:16.5px;line-height:1.58;font-weight:400;color:#ecdfca;max-width:46ch;
  margin:0 0 26px;letter-spacing:.002em}
.pb-lede-hi{font-weight:700;color:var(--gold-300)}
/* On its own line below the paragraph, back at the size and style it had
   before the flow change: a block, a step larger, in the quote italic. The
   paragraph flows; this one line stands apart as the close. */
.pb-lede-close{display:block;margin-top:13px;font-family:var(--font-quote);font-style:italic;
  font-weight:500;font-size:1.14em;color:var(--gold-300)}
.pb-hero-ctas{display:flex;gap:13px;flex-wrap:wrap;margin-bottom:26px}
/* The leading icon is quieter than the label and the trailing arrow; it
   identifies the action rather than competing with it. */
.pb-hero-ctas .pb-btn svg:first-child{opacity:.8}
/* Three claims in a bordered strip rather than three loose checkmarks: an
   icon that says which claim it is, the claim, and one line of what it means.
   The dividers are the strip's own, so the group reads as one object. */
/* Six things the series is, as their own small cards rather than one divided
   strip: a gold icon chip, the claim, a line of what it means. Cards lift on
   hover -- gold on the dark ground is where the strip earns a second look.
   Three across on a wide screen, two on a tablet, two on a phone. */
.pb-ticks{grid-area:ticks;margin-top:28px;list-style:none;padding:0;
  display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.pb-ticks li{display:grid;grid-template-columns:auto 1fr;column-gap:12px;row-gap:3px;
  align-items:center;padding:13px 15px;border-radius:13px;
  border:1px solid rgba(255,255,255,.12);background:rgba(255,255,255,.045);
  transition:background .2s ease,border-color .2s ease,transform .2s ease}
.pb-ticks li:hover{background:rgba(255,255,255,.075);transform:translateY(-2px);
  border-color:rgba(227,200,119,.4);
  border-color:color-mix(in srgb,var(--gold-300) 42%,transparent)}
.pb-ticks .tick-ic{grid-row:span 2;align-self:center;width:36px;height:36px;flex:none;
  border-radius:10px;display:grid;place-items:center;color:var(--gold-300);
  background:rgba(227,200,119,.14);
  background:color-mix(in srgb,var(--gold-300) 15%,transparent)}
.pb-ticks b{font-size:13.5px;font-weight:700;color:var(--on-dark);line-height:1.25;letter-spacing:-.005em}
.pb-ticks .tick-s{font-size:11.5px;color:#c8b696;line-height:1.32}
@media (max-width:980px){ .pb-ticks{grid-template-columns:repeat(2,1fr)} }
.pb-stage{display:flex;align-items:center;justify-content:center;min-height:340px;position:relative}

/* ---------- FEATURE STRIP ---------- */
/* A marketing beat between the hero and the catalogue: one hook, one line,
   centred on the cream. It replaced four small feature columns that repeated
   the hero's ticks and the catalogue heading. A short gold rule above it gives
   the moment a top rather than starting cold. */
/* On the page cream, textured with a faint mandala like the offer carousel it
   borrows its swipe from -- not the flat cream block it used to be. */
.pb-band{background:var(--cream-50);text-align:center;position:relative;overflow:hidden}
.pb-band-mandala{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
  width:520px;height:520px;opacity:.09;color:var(--gold-300);pointer-events:none;z-index:0}
.pb-band-in{position:relative;z-index:1;max-width:760px;margin:0 auto;padding:54px 24px}
/* The stack swaps under the static gold rule; clipped horizontally so a leaving
   quote slides off rather than showing beside the one arriving. */
.pb-band-wrap{overflow-x:clip}
.pb-band-wrap .pb-ticket-slide{align-content:center}
.pb-band-quote{max-width:640px;margin:0 auto}
.pb-band-rule{width:44px;height:2px;margin:0 auto 22px;border-radius:2px;
  background:linear-gradient(90deg,transparent,var(--gold-500),transparent)}
.pb-band-h{font-family:var(--font-display);font-optical-sizing:auto;
  font-size:clamp(23px,3.2vw,32px);line-height:1.18;font-weight:600;
  letter-spacing:-.01em;color:var(--ink-900);margin:0;text-wrap:balance}
.pb-band-h em{font-family:var(--font-quote);font-style:italic;font-weight:500;
  font-size:1.06em;color:var(--brand-600)}
.pb-band-p{font-size:16px;line-height:1.6;color:var(--ink-600);max-width:56ch;margin:15px auto 0}
/* The hook has no Devanagari in Fraunces; in Hindi it and its accent take the
   Rozha One display face, without the slant Rozha One does not carry. No
   gradient -- solid on cream keeps the gold accent legible against it. */
[data-applang="hi"] .pb-band-h,
[data-applang="hi"] .pb-band-h em{font-family:var(--font-deva-display);font-weight:400;letter-spacing:0}
[data-applang="hi"] .pb-band-h em{font-style:normal;font-size:1em}

/* ---------- SECTIONS ---------- */
.pb-sec{padding-block:76px;position:relative}
.pb-sec-head{max-width:660px;margin:0 auto 42px;text-align:center;position:relative;z-index:2}
.pb-h2{font-family:var(--font-display);font-optical-sizing:auto;font-size:clamp(27px,3.1vw,37px);
  margin:9px 0 12px;font-weight:600;line-height:1.16;color:var(--ink-900)}
.pb-sub{color:var(--ink-600);font-size:15.5px;line-height:1.65;margin:0}
.pb-h2 em{font-family:var(--font-quote);font-style:italic;font-weight:500;font-size:1.08em;color:var(--brand-600)}
/* Under a section title, a hook with some heat: the quote serif in italic,
   brand-coloured. Kept to ONE line -- it is an English tagline whose rhythm is
   the point, and a wrap breaks the two-beat cadence. The size is capped for a
   wide screen and driven off the viewport below it, so the line still fits on a
   phone; .pb-sec-narrow clips horizontally, so a slow-loading fallback face
   that runs a hair wide cannot push a scrollbar onto the page. */
.pb-hook{font-family:var(--font-quote);font-style:italic;font-weight:500;
  white-space:nowrap;font-size:clamp(17px,2.1vw,21px);line-height:1.45;
  color:var(--brand-600);margin:14px auto 0}

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
/* The cream side of the seam steps down too, so the ramp into the dark band
   is cream-100 -> cream-200 -> gold hairline -> the band's lighter shoulder,
   rather than one flat cream meeting one flat maroon. Its bottom border goes
   with it: a --line hairline directly above the gold one made the seam read as
   two rules, not one. */
.pb-show{background:var(--cream-100);
  background:linear-gradient(180deg,var(--cream-100) 0%,var(--cream-100) 68%,var(--cream-200) 100%);
  border-top:1px solid var(--line)}
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
/* This band is cream above it and cream below it, and a flat fill met both
   with a butt-join -- two pages stuck together rather than one page changing
   register. Three things fix it, none of them a fade from cream to maroon
   (that route only passes through mud):

   - the band is no longer flat. It carries its own lighter shoulders, so the
     edge that touches cream is the lightest maroon on the page and the middle
     is the deepest.
   - a warm bloom sits just inside each edge, so the seam looks lit.
   - each seam gets the gold hairline the header and footer already use.

   Solid first, gradient second: a browser that cannot parse the gradient list
   keeps a usable opaque band instead of dropping the only background it has
   and leaving cream text on cream -- the same trap the footer documents. */
.pb-res{background:var(--brand-900);
  background:
    radial-gradient(760px 150px at 50% 0%, rgba(224,178,64,.12), transparent 72%),
    radial-gradient(760px 150px at 50% 100%, rgba(224,178,64,.09), transparent 72%),
    linear-gradient(180deg,
      var(--brand-800) 0%, var(--brand-900) 34%,
      var(--brand-900) 66%, var(--brand-800) 100%);
  color:var(--on-dark);position:relative;overflow:hidden}
[data-theme="dark"] .pb-res{background:#150609;
  background:
    radial-gradient(760px 150px at 50% 0%, rgba(224,178,64,.10), transparent 72%),
    radial-gradient(760px 150px at 50% 100%, rgba(224,178,64,.07), transparent 72%),
    linear-gradient(180deg,#210c11 0%,#150609 36%,#150609 64%,#210c11 100%)}
/* The hairlines live on pseudo-elements, not in the background list above:
   color-mix() is the one thing here an older WebView may not parse, and a
   dropped decoration is nothing while a dropped background is a broken page. */
.pb-res::before,.pb-res::after{content:"";position:absolute;left:0;right:0;height:1px;
  z-index:3;pointer-events:none;
  background:linear-gradient(90deg,transparent,
    color-mix(in srgb,var(--gold-500) 62%,transparent) 50%,transparent)}
.pb-res::before{top:0}
.pb-res::after{bottom:0}
.pb-res .pb-h2{color:var(--on-dark)}
.pb-res .pb-sub{color:#d8c9ae}
.pb-res .pb-eyebrow{color:var(--gold-300)}
.pb-res-mandala{position:absolute;right:-170px;bottom:-190px;width:520px;height:520px;opacity:.10;color:var(--gold-300)}
/* Three across, because there are six of these. auto-fit fitted five on a wide
   screen and left FAQ alone on a row of its own -- a grid that ends in one
   stranded card reads as a card that failed to load. Three gives two full
   rows, and the wider card lets every blurb sit on two lines instead of three. */
.pb-resgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
@media (max-width:980px){ .pb-resgrid{grid-template-columns:repeat(2,1fr)} }
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
.pb-ticket-copy{flex:1;min-width:0}
.pb-ticket .pb-btn{flex:0 0 auto}
/* The phone's shorter line; swapped in for the sentence at the breakpoint. */
.pb-ticket-short{display:none}

/* Two tickets -- the coupon one and refer-and-earn -- share this one slot and
   swipe between themselves. Both are stacked in a single grid cell, so the slot
   is as tall as the taller of the two and neither can shift the page as they
   trade places; only transform and opacity animate. The wrap already clips
   horizontally, which is what turns the translate into a swipe.

   116%, not 100%: the ticket's notches hang 14px outside its own box, and at a
   flat 100% the outgoing notch was left sitting in the wrap's padding. */
.pb-ticket-stack{display:grid}
.pb-ticket-slide{grid-area:1/1;display:grid;min-width:0;
  transition:transform .62s cubic-bezier(.4,0,.2,1),opacity .46s ease}
.pb-ticket-slide[data-pos="cur"] {transform:none;opacity:1}
.pb-ticket-slide[data-pos="next"]{transform:translateX(116%);opacity:0;pointer-events:none}
.pb-ticket-slide[data-pos="prev"]{transform:translateX(-116%);opacity:0;pointer-events:none}
/* Which of the two is showing, and a way to choose. */
.pb-ticket-dots{display:flex;justify-content:center;gap:8px;margin-top:15px}
.pb-tdot{position:relative;width:8px;height:8px;min-height:0;padding:0;border:0;border-radius:50%;
  background:color-mix(in srgb,var(--gold-600) 34%,transparent);cursor:pointer;
  transition:background .2s,transform .2s}
/* Hit area only — invisible, and it lifts an 8px dot to a 26px target. */
.pb-tdot::after{content:"";position:absolute;inset:-9px}
.pb-tdot:hover{background:color-mix(in srgb,var(--gold-600) 62%,transparent)}
.pb-tdot.on{background:var(--brand-700);transform:scale(1.25)}
.pb-tdot:focus-visible{outline:2px solid var(--gold-500);outline-offset:3px}
/* The global coarse-pointer rule puts every button at 44px; these are 8px
   markers with their own 26px hit area, so they opt out of it. */
@media (pointer:coarse){ .pb-root .pb-tdot{min-height:8px} }
@media (prefers-reduced-motion: reduce){
  .pb-ticket-slide{transition:none}
}

/* ---------- QUOTE ---------- */
.pb-sec-coupon{padding-block:62px}
/* Coming out of the dark band is that seam in reverse: the cream picks up
   where the band left off and clears to the page colour over the first stretch
   below it.

   The ramp hangs off this full-width wrapper rather than off the section
   itself, and that is the whole reason the wrapper exists. The section is
   .pb-sec-narrow -- centred, max-width 1180 -- so a full-bleed ramp there
   needed 100vw, and 100vw counts the scrollbar: it measured 8px wider than the
   page and put a horizontal scrollbar under the whole site. left/right:0 on a
   block that is already full width has no such opinion about scrollbars. */
.pb-coupon-band{position:relative}
.pb-coupon-band::before{content:"";position:absolute;left:0;right:0;top:0;height:150px;
  pointer-events:none;z-index:0;
  background:linear-gradient(180deg,var(--cream-200),transparent)}
.pb-coupon-band > *{position:relative;z-index:1}
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
/* The footer was a cream card on a cream page: the same two values the whole
   site is built from, so it read as one more section rather than as the end
   of the page. It is now dark, on the brand colour the resources band already
   uses, and it follows whichever palette the reader picked. A page needs a
   floor. */
/* The colophon strip runs edge to edge while the rest of the footer is
   inset, so it has to cancel exactly the padding above it. Carried as a
   variable rather than repeated as a number in two media queries, which is
   how the two got out of step in the first place. */
/* Not brand-900 itself. That exact value is already the hero band and the
   free-resources band, so on a phone the scroll went dark maroon, cream,
   dark maroon again -- three of the same block, and the last of them read as
   a repeat rather than as an ending. --foot-ground is that colour taken down
   toward a near-black: it keeps the palette's hue (deep wine here, navy
   under Sapphire, green-black under Forest) while sitting clearly beneath
   the bands above it.

   It is a real token declared beside --brand-900 in every palette, NOT a
   color-mix() computed here, and that distinction is the whole reason this
   rule looks the way it does. Written as color-mix() it rendered correctly
   in this browser and vanished on a phone: a browser that does not
   understand the function drops the whole declaration, which left the
   footer with no background at all -- the cream page showing through, under
   cream text. Plenty of Android WebViews still do not have it. A background
   that carries every word in the footer is not the place to depend on a
   feature; hover tints elsewhere can degrade quietly, this cannot. */
.pb-foot{--foot-pad:24px;
  background:var(--foot-ground);
  color:var(--on-dark);padding:48px var(--foot-pad) 0;
  position:relative}
/* A gold hairline where the page meets it, the same gesture as the header. */
.pb-foot::before{content:"";position:absolute;left:0;right:0;top:0;height:1px;
  background:linear-gradient(90deg,transparent,color-mix(in srgb,var(--gold-500) 70%,transparent) 50%,transparent)}
.pb-foot-card{max-width:1180px;margin:0 auto;background:none;border:0;border-radius:0;
  box-shadow:none;overflow:visible}
/* Three blocks now, not two: identity, links, and the follow row. On a wide
   screen the follow row belongs under the newsletter it shares a column
   with; stacked on a phone it belongs after the links, which is the order it
   is actually read in -- who this is, subscribe, go somewhere, follow. Grid
   areas because that is a different order in each layout, and DOM order can
   only be one of them. */
.pb-foot-in{display:grid;grid-template-columns:1.05fr 1.35fr;
  grid-template-areas:"brand links" "social links";grid-template-rows:auto 1fr;gap:0}
.pb-foot-brand{grid-area:brand}
.pb-foot-social{grid-area:social;padding:0 40px 34px 0;
  border-right:1px solid rgba(255,255,255,.10)}
.pb-foot-links{grid-area:links}

/* -- left: identity + newsletter -- */
.pb-foot-brand{padding:8px 40px 34px 0;border-right:1px solid rgba(255,255,255,.10);min-width:0}
.pb-foot-logo{display:flex;align-items:center;gap:12px;margin-bottom:16px}
.pb-foot .pb-name{color:var(--on-dark)}
.pb-foot .pb-tagline{color:var(--on-dark-soft);opacity:.7}
.pb-foot-blurb{font-size:14px;line-height:1.7;color:var(--on-dark-soft);margin:0 0 30px;max-width:40ch}
/* Same label as EXPLORE and SUPPORT. It was 20px in the display face while
   they are 12px in the same face and the same gold -- one treatment at
   nearly twice the size, which read as shouting rather than as a heading. */
.pb-news h5{font-size:12px;letter-spacing:.13em;margin:0 0 7px}
.pb-news p{font-size:13px;color:var(--on-dark-soft);opacity:.78;margin:0 0 13px;line-height:1.6;
  max-width:46ch}
.pb-news-row{display:flex;align-items:stretch;background:rgba(255,255,255,.07);
  border:1.5px solid rgba(255,255,255,.16);
  border-radius:100px;padding:4px 4px 4px 6px;transition:border-color .18s,box-shadow .18s;max-width:420px}
.pb-news-row:focus-within{border-color:var(--gold-500);box-shadow:0 0 0 4px color-mix(in srgb,var(--gold-500) 16%,transparent)}
.pb-news-row input{flex:1;min-width:0;border:0;background:none;outline:none;font:inherit;font-size:14.5px;
  color:var(--on-dark);padding:8px 12px}
.pb-news-row input::placeholder{color:rgba(251,246,236,.45)}
.pb-news-btn{flex:0 0 auto;border:0;border-radius:100px;font:inherit;font-weight:700;font-size:14px;
  padding:9px 22px;cursor:pointer;color:#2a1e05;background:linear-gradient(155deg,var(--gold-500),var(--gold-600));
  transition:filter .16s,transform .16s}
.pb-news-btn:hover:not(:disabled){filter:brightness(1.06);transform:translateY(-1px)}
.pb-news-btn:disabled{opacity:.55;cursor:default}
/* On a touch device the global rule pins every button to a 44px tap target,
   which is what made this pill sit tall. The subscribe button is wide and
   clearly labelled, so it holds a slimmer 38px here -- still well clear of the
   WCAG AA 24px floor -- and the whole row reads leaner. */
@media (pointer:coarse){ .pb-root .pb-news-btn{min-height:38px} }
.pb-news-msg{margin:11px 2px 0;font-size:12.5px;line-height:1.5;display:flex;align-items:flex-start;gap:6px}
.pb-news-msg.ok{color:var(--ok-600)}
.pb-news-msg.bad{color:var(--bad-600)}
/* Six bordered circles, five of them dashed, read as five broken images
   rather than as five handles not yet filled in. Bare glyphs instead: the
   live one at full strength, the rest dimmed. Nothing is drawn around them,
   so there is no empty container to look unfinished. */
.pb-socials{display:flex;gap:6px;margin-top:24px;align-items:center}
.pb-foot-follow{display:none;font-size:11.5px;text-transform:uppercase;letter-spacing:.14em;
  color:var(--gold-300);margin:0 0 12px;font-weight:700}
/* Scoped under .pb-foot so it outranks the .pb-foot a rule (display:block,
   width:100%), which was turning the linked icon into a 240px-wide block and
   squeezing the rest of the row down to 25px. flex:0 0 auto stops them shrinking at all. */
.pb-foot .pb-social{flex:0 0 auto;width:40px;height:40px;margin:0;border-radius:11px;
  border:0;background:none;
  display:grid;place-items:center;color:var(--on-dark);cursor:pointer;text-align:center;
  transition:color .18s,transform .18s,background .18s}
.pb-foot .pb-social:hover{transform:translateY(-2px);background:rgba(255,255,255,.08)}
/* Placed but not yet linked. Dimmed and inert — nothing here opens a dead tab. */
.pb-foot .pb-social-soon{opacity:.42;cursor:default}
.pb-foot .pb-social-soon:hover{transform:none;background:none}

/* Instagram has no single colour, so its warm middle stands for it — a
   gradient inside a 17px glyph would read as mud. X is drawn in the
   foreground colour, since its own mark is black and would vanish here. */
.pb-foot .pb-social[data-net="instagram"]{color:#e1306c}
.pb-foot .pb-social[data-net="youtube"]  {color:#ff3d34}
.pb-foot .pb-social[data-net="telegram"] {color:#3aa8e0}
.pb-foot .pb-social[data-net="whatsapp"] {color:#3ecb5f}
.pb-foot .pb-social[data-net="linkedin"] {color:#4a9fe0}
.pb-foot .pb-social[data-net="x"]        {color:var(--on-dark)}

/* -- right: link columns -- */
.pb-foot-links{padding:8px 0 34px 40px;display:grid;grid-template-columns:1fr 1fr 1.35fr;gap:28px;min-width:0}
.pb-foot h5{font-size:12px;text-transform:uppercase;letter-spacing:.13em;color:var(--gold-300);
  margin:0 0 16px;font-weight:800;font-family:var(--font-roman)}
.pb-foot a,.pb-foot .flink{display:block;width:100%;font-size:14px;color:var(--on-dark-soft);margin-bottom:11px;
  background:none;border:0;font-family:inherit;padding:0;cursor:pointer;text-align:left;
  transition:color .16s,transform .16s;min-width:0;overflow-wrap:break-word}
.pb-foot a:hover,.pb-foot .flink:hover{color:var(--gold-300);transform:translateX(2px)}
.pb-foot-contact{font-size:13.5px;line-height:1.7;color:var(--on-dark-soft);margin:0}
.pb-foot-supl{margin-top:10px}
/* The support address is set in the quote italic serif, the same voice as the
   hero's "Your race starts here." -- a written line rather than plain UI text.
   The underline is kept for the hover only, so at rest it reads as the phrase
   it is styled to be. */
.pb-foot-contact a{display:inline;margin:0;color:var(--gold-300);
  font-family:var(--font-quote);font-style:italic;font-weight:500;
  font-size:15.5px;letter-spacing:.005em;text-decoration:none;
  overflow-wrap:break-word;word-break:normal;transition:color .16s}
.pb-foot-contact a:hover{color:var(--gold-500);text-decoration:underline;text-underline-offset:3px}

/* -- bottom bar --
   Its own darker strip running the full width, the way a colophon sits below
   a page rather than inside it. Full-bleed via negative margins because
   .pb-foot carries the horizontal padding the rest of the footer needs. */
.pb-foot-bottom{margin:34px calc(var(--foot-pad) * -1) 0;padding:18px var(--foot-pad);
  background:#08060a;border-top:1px solid rgba(255,255,255,.07);
  display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;
  font-size:12.5px;color:var(--on-dark-soft)}
/* Desktop keeps the copyright left and the links right; the DOM has them
   the other way round so a phone reads the links first. */
.pb-foot-bottom{flex-direction:row-reverse}
.pb-foot-cr{opacity:.72;display:inline-flex;align-items:center;flex-wrap:wrap;
  justify-content:center;gap:0 2px}
.pb-foot-legal{display:flex;gap:0;flex-wrap:wrap;align-items:center}
.pb-foot-legal button{background:none;border:0;font:inherit;font-size:12.5px;color:var(--on-dark-soft);
  cursor:pointer;padding:0;transition:color .16s}
.pb-foot-legal button:hover{color:var(--gold-300)}
/* Separators, not links: they sit outside the buttons so nothing enlarges a
   target or reads a stray character out to a screen reader. */
.pb-foot-dot{opacity:.55;padding:0 7px;user-select:none}

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
  /* Headline left, lamp right, sharing the top row -- the arrangement the
     desktop has. Only the lede, the buttons and the ticks drop to full width
     underneath, because a paragraph in a 190px column is not a paragraph. */
  .pb-hero-grid{padding:26px 20px 34px;gap:0 8px;
    grid-template-columns:1fr auto;
    grid-template-areas:"head diya" "body body" "ticks ticks";
    align-items:center}
  /* The lamp runs past the grid's padding toward the screen edge. That bleed
     is what lets it read large while costing the headline only part of its
     width -- the box is 45vw, the space it actually takes is 26px less, and
     .pb-hero clips so none of it becomes horizontal scroll. */
  .pb-stage{min-height:0;justify-self:end;align-self:center;margin:0 -30px 0 0}
  .ill-diya{width:min(43vw,168px);height:min(43vw,168px)}
  .pb-hero-head{align-self:center}
  .pb-hero-body{margin-top:18px}
  /* Measured against the column the lamp leaves, not chosen: "Lead your prep"
     wants 187px at this size and tracking, and the column is 196px. A step
     larger breaks it after "your" and orphans a word at the top of the page. */
  .pb-h1{font-size:28px;line-height:1.16;letter-spacing:-.022em;margin-bottom:0}
  /* The break belongs between the two halves of the line here, not inside
     one of them -- the column is 200px wide now. */
  .pb-h1 br{display:block}
  /* 330px of tracked capitals in a 320px row left "REAL PROGRESS." alone on
     a second line. A half point and a little tracking bring it to 305. */
  .pb-lede{font-size:15.5px;line-height:1.55;margin-bottom:20px;max-width:none}
  .pb-lede-close{font-size:1.2em;margin-top:12px}
  /* Two columns on a phone, and just the icon and the title -- the sub-lines
     are the first thing to go when six cards have to share a narrow screen;
     the titles are written to stand on their own. */
  .pb-ticks{grid-template-columns:1fr 1fr;gap:8px;margin-top:0}
  .pb-ticks li{padding:11px 12px;border-radius:11px;column-gap:10px}
  .pb-ticks .tick-ic{width:30px;height:30px;border-radius:8px}
  .pb-ticks b{font-size:12.5px}
  .pb-ticks .tick-s{display:none}
  .pb-hero-ctas{gap:9px;margin-bottom:20px}
  .pb-hero-ctas .pb-btn{flex:1 1 100%;padding:13px 20px;font-size:15px}
  /* The pool sits where the lamp sits -- upper right, beside the headline --
     and a shade stronger than the desktop's, because on a small screen it is
     doing the work of separating the lamp from the maroon behind it. */
  .pb-hero::before{background:
    radial-gradient(260px 230px at 84% 16%, rgba(224,178,64,.34), transparent 66%),
    radial-gradient(460px 220px at 50% -14%, rgba(255,255,255,.05), transparent 72%)}

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
  /* One line on a phone too. The section stacks two paddings (its own and the
     narrow wrapper's), leaving barely 240px at 320px, so the hook reclaims the
     wrapper's 18px on each side and the size is driven off the viewport to fit
     what is left. sec-narrow clips horizontally, so even a hair over cannot
     scroll the page. */
  .pb-hook{font-size:clamp(11px,3.55vw,20px);line-height:1.4;margin:12px -18px 0}
  .pb-eyebrow{font-size:11px;letter-spacing:.12em}

  .pb-grid{gap:16px;grid-template-columns:1fr}
  .pb-card{padding:22px 20px 20px;border-radius:18px}
  .pb-card-title{font-size:18px}
  .pb-card-desc{min-height:0;margin-bottom:14px}
  .pb-price{font-size:24px}
  /* Enroll and Details sit side by side on a phone too, not stacked. Stacked,
     two full-width buttons added ~50px of height to every card and made the
     catalogue feel like a long scroll. Enroll grows, Details stays compact; the
     lone "owned"/"coming soon" button keeps its own width:100%. nowrap keeps a
     label from breaking onto two lines when the pair is tight. */
  .pb-card-btns .pb-btn{white-space:nowrap}
  .pb-card-btns .pb-btn-sm{flex:0 0 auto}

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

  /* A horizontal band on a phone too, the way it reads on desktop: icon, text
     and the button in one row rather than a tall card with a full-width button
     under it. It carries a title and one short line here, so it sits a little
     thicker than a single-line strip -- which is the right trade for an offer
     that has a number in it.

     The wrap's 14px inset only existed to seat the notches, which are hidden
     on a phone; dropping it hands those 28px back to the text column. */
  .pb-ticket-wrap{padding-inline:0}
  /* Two rows rather than one cramped line. Squeezed into a single row the
     text column came to 127px and every line broke in two; given its own row
     the title gets the full width and the short line shares the row below with
     the button. Both columns are shared by the two rows, so the title spans
     the copy and button columns, and the line spans the icon and copy ones. */
  /* The icon spans both rows rather than sitting in the first: at 38px it was
     taller than the title line and set the whole row to its own height, which
     is 19px of nothing above the button. Spanning, it centres against the pair
     and the rows cost only what their text and the button actually need. */
  .pb-ticket{display:grid;grid-template-columns:auto 1fr auto;
    grid-template-areas:"ic copy copy" "ic note btn";
    column-gap:11px;row-gap:8px;align-items:center;padding:13px;border-radius:14px}
  .pb-ticket-ic{grid-area:ic;width:38px;height:38px;border-radius:11px}
  .pb-ticket-copy{grid-area:copy}
  .pb-ticket h4{font-size:15px;margin:0;line-height:1.25}
  .pb-ticket-long{display:none}
  /* Scoped under .pb-ticket, not left as a bare class: the base rule is
     .pb-ticket p, which carries an element on top of its class and would
     otherwise keep this line at the desktop's 13.5px -- which is what made it
     spill onto a second line beside the button. */
  .pb-ticket .pb-ticket-short{grid-area:note;display:block;font-size:11.5px;
    line-height:1.4;color:var(--ink-400);align-self:center}
  .pb-ticket .pb-btn{grid-area:btn;justify-self:end;width:auto;gap:5px;
    padding:8px 12px;font-size:11.5px;white-space:nowrap}
  .pb-ticket .pb-btn svg{width:14px;height:14px}
  .pb-notch{display:none}
  .pb-ticket-dots{margin-top:12px}

  .pb-quote{padding:48px 20px}
  .pb-quote .deva{font-size:23px}
  .pb-quote p{font-size:15.5px}

  /* No card any more, so the footer's own padding is the only horizontal
     inset on a phone -- which is what gave the link columns the room to hold
     "Previous year papers" on one line. The stacked rules above do the rest;
     all this breakpoint changes is how tight it all is. */
  .pb-foot{--foot-pad:18px;padding-top:32px}
  .pb-foot-card{border-radius:0}
  .pb-foot-links{column-gap:14px}
  .pb-foot-supl{column-gap:14px}
  /* The identity block was set to desktop rhythm: 30px under the blurb and
     16px under the logo, which on a phone is a gap you scroll past rather
     than a break you read. */
  .pb-foot-logo{margin-bottom:12px}
  .pb-foot-blurb{margin-bottom:20px}
  .pb-news p{margin-bottom:11px}
  .pb-foot-bottom{padding-top:4px}

  .pb-panel{padding:20px;border-radius:18px}
  .pb-h3{font-size:17px}
  .pb-syl li{padding-left:31px}
  .pb-listrow{padding:13px 0}
  .pb-detail{gap:22px}
}

/* Very narrow phones — 360px and below. The lamp scales with the viewport
   via min(58vw,…) above, so it needs no fixed size here. */
/* Narrower phones. The headline shares its row with the lamp, so each step
   down in width costs the text column real millimetres and the type has to
   follow -- these were LARGER than the base while the lamp sat on its own row,
   which is the wrong direction now that it is back beside the words. */
@media (max-width:365px){
  .pb-h1{font-size:26px}
}
/* Smallest phones — 320px and below. Here the lamp gives ground as well as the
   type: at 24px "Lead your prep" wants 167px, and only a smaller lamp leaves
   that much beside it. */
@media (max-width:340px){
  .pb-h1{font-size:24px}
  .pb-hero-grid{padding-inline:16px}
  .pb-stage{margin-right:-26px}
  .ill-diya{width:min(40vw,132px);height:min(40vw,132px)}
  .pb-resgrid{grid-template-columns:1fr}
}

/* Tablet hero. Text left, lamp right spanning both rows -- as on desktop.
   The phone (below 641) stacks to one column with the lamp centred on top;
   at tablet width there is room to set them side by side again.

   Written as a RANGE, not as max-width:980px. The phone block sits earlier in
   this sheet, so a plain max-width here would out-rank it at equal specificity
   and hand a 360px screen the 200px lamp meant for a tablet -- which is
   exactly what it did until this was measured at 640px. */
@media (min-width:641px) and (max-width:980px){
  /* The lamp spans BOTH rows here, as it does on desktop -- there is width
     for it at this size. */
  .pb-hero-grid{grid-template-columns:1fr auto;
    grid-template-areas:"head diya" "body diya" "ticks ticks";
    align-items:center;padding:52px 20px 46px;gap:0 32px}
  .pb-stage{min-height:0}
  /* 200, not 230. The two hero buttons gained leading icons and now want
     470px side by side; at 230 the text column was 451 and they wrapped into
     two rows. Thirty pixels off the lamp gives the column 481. */
  .ill-diya{width:200px;height:200px}
  .pb-hero-body{margin-top:18px}
}
@media (max-width:980px){
  .pb-lede{max-width:none}
  .pb-show-grid{grid-template-columns:1fr;gap:34px;padding:58px 24px}
  /* Three across on a tablet, one on a phone. Written as a range so it
     does not depend on where this block sits in the sheet. */
  .pb-steps{grid-template-columns:1fr;gap:26px}
  .pb-detail{grid-template-columns:1fr}
  .pb-buy{position:static}
}
@media (max-width:1000px){
  /* Three link columns stop fitting well before the footer stops being
     side-by-side. At 950px they were 117px wide and both "Previous year
     papers" and "Daily current affairs" wrapped -- so this pairing belongs
     to the width where the columns get tight, not to the width where the
     two halves stack. Getting that wrong is what broke 901-1000px. */
  .pb-foot-links{grid-template-columns:1fr 1fr;column-gap:22px;row-gap:0}
  .pb-foot-links > div:nth-child(3){grid-column:1 / -1;
    margin-top:12px;padding-top:12px;border-top:1px solid rgba(255,255,255,.10)}
  .pb-foot-supl{margin-top:2px;display:grid;grid-template-columns:1fr 1fr;column-gap:22px}

  .pb-nav{display:none}
  .pb-nav.open{display:flex;position:absolute;top:100%;left:0;right:0;flex-direction:column;
    align-items:stretch;background:var(--cream-50);border-bottom:1px solid var(--line);padding:12px;gap:5px;
    box-shadow:var(--shadow-card)}
  .pb-nav.open .link{text-align:left;width:100%}
  .pb-burger{display:flex}
  .pb-head-in{position:relative}

}
@media (max-width:560px){
  .pb-sec{padding-block:56px}
  .pb-band-in{padding:40px 20px}
  .pb-band-rule{margin-bottom:16px}
  .pb-band-h{font-size:22px;line-height:1.22}
  .pb-band-p{font-size:14.5px;margin-top:12px}
  .pb-ticket{padding:13px 14px}
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
  /* Below this width the footer stacks, and everything that follows from
     stacking belongs here rather than in a narrower phone breakpoint. That
     split is what left a tablet with the columns of a phone and the socials
     of a desktop: left-aligned under a heading that was still hidden, a
     Support group sitting in half a row, and a colophon that stopped short
     of both edges. */
  .pb-foot-in{grid-template-columns:1fr;grid-template-rows:none;
    grid-template-areas:"brand" "links" "social"}
  /* One rhythm for the whole stack: 18px from the last line of a section to
     its rule and 18px from the rule to the next heading, everywhere. The
     brand break was 45px and the other three were 26-29px, which is what
     made the sections feel unevenly spaced rather than any one of them
     being wrong. Support keeps a smaller 12px pair, because it divides two
     rows inside one block rather than two blocks. */
  .pb-foot-brand{padding:0 0 18px}
  .pb-foot-social{padding:0;border-right:0}
  .pb-foot-links{padding:18px 0 4px}

  .pb-foot-follow{display:block;text-align:center;margin:14px 0 8px;
    padding-top:18px;border-top:1px solid rgba(255,255,255,.10)}
  .pb-socials{justify-content:center;gap:4px;margin-top:0}
  /* Smaller boxes on a phone: a 17px glyph in a 40px box left a broad ring of
     dead space under the row. 34px still clears a comfortable tap target while
     sitting the icons close to the strip below. */
  .pb-foot .pb-social{width:34px;height:34px}

  /* The strip used to sit 22px below the icons and open with 14px of its own
     padding -- 36px of empty band between the icons and the legal line. Both
     are pulled in so the colophon sits directly under the row it follows. */
  .pb-foot-bottom{flex-direction:column;align-items:center;text-align:center;
    gap:5px;margin-top:10px;
    padding-bottom:calc(16px + env(safe-area-inset-bottom))}
  .pb-foot-legal{gap:0;width:100%;justify-content:center}
  /* .72, not the .55 this started at. Deepening the ground darkened this
     text with it -- opacity composites toward the background, so a darker
     floor costs contrast rather than gaining it; it measured 4.74 against a
     4.5 bar before the lift. */
  .pb-foot-cr{font-size:11.5px;justify-content:center}
  .pb-foot-brand{border-right:0;border-bottom:1px solid rgba(255,255,255,.10)}
}

/* Newsletter on a phone. Two fixes, both learned the hard way:
   - 16px on the input. The baseline rule .pb-root input{font-size:16px} and
     .pb-news-row input{font-size:14.5px} have identical specificity, so the
     later one won and iOS would have zoomed the whole page on focus — exactly
     the bug the baseline rule exists to prevent.
   - Stacked, because side by side the button took 114px of 257px and left the
     address field 130px to type an email into. */
@media (max-width:560px){
  /* The same single pill the desktop has: field and button in one row, the
     button carrying the only colour. It was stacked here, which turned one
     control into two objects and a lot of empty ground between them.

     Only two things change for the phone. The width cap comes off so it
     fills the column, and the input goes to 16px -- below that iOS zooms
     the whole page on focus, which is a far worse thing to fix afterwards
     than a half-point of type. The button loses a little side padding so
     the field keeps room to actually type an address in. */
  .pb-news-row{max-width:none;padding:3px 3px 3px 8px}
  .pb-news-row input{font-size:16px;padding:7px 6px 7px 4px}
  .pb-news-btn{padding:8px 18px;font-size:13.5px}
}

/* Footer links on a phone.

   Two problems, and the first one hid the second. The coarse-pointer
   baseline gives every button a 44px touch target, so an 11px margin on top
   of that pushed each link 55px apart. That was fixed by dropping the
   margin -- but the groups were still stacked one under another, twelve
   links in a single column, and the footer ran 1342px: one and two-thirds
   of the screen, for a list of links.

   Explore and Free resources now sit abreast, which halves eight rows into
   four, and Support runs across their foot with its own links paired. The
   rule that drew a divider above each group has gone: it was written for a
   single column and, once there were two, it was putting a line above the
   right-hand group for no reason -- which it had already been doing between
   561 and 640px, where this grid has been two columns all along.

   Only Support keeps a divider, and it earns it: it is a different kind of
   thing from the two navigation lists, and it is the one place the rule
   separates rows rather than columns. */
@media (max-width:640px){
  .pb-foot a,.pb-foot .flink{margin-bottom:0;display:flex;align-items:center}
  .pb-foot h5{margin-bottom:6px}
  .pb-foot-contact{padding:4px 0 0}

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

  /* The hero's padding, gap and stage height are set in the phone block
     above, which sits earlier in this sheet -- so a second copy here won at
     equal specificity and undid it. The 190px stage in particular was
     written when the lamp had a row to itself; beside a 104px lamp it was
     86px of dead height that pushed the lede down the screen. */
  .pb-steps{gap:18px}
  .pb-step{padding:20px 18px}
  .pb-sec-mandala{width:280px;height:280px;top:-40px}
}

/* ---------- MOBILE HEADER ----------
   Above 1000px the full nav carries login and the chrome controls, so this
   block is hidden. Below it, the nav collapses into the burger and these
   three things come out of it: language, theme, and one primary action.

   The brand is trimmed to make room — the tagline goes and the wordmark
   steps down a size. Measured at 375px there is 343px of usable header, and
   the burger, brand, pills and button have to share it. */
/* flex:0 0 auto on the group and nowrap on the button, or the button is the
   thing that gives way in a tight row — it collapsed to a one-letter column
   reading L / o / g / i / n. The brand yields instead, and truncates. */
.pb-head-mobile{display:none;align-items:center;gap:8px;margin-left:auto;flex:0 0 auto}
.pb-nav-palette{display:none}

/* The one thing in the header that should pull the eye. Gold, because that is
   the colour the page already uses for its primary action — a maroon button
   sitting between a cream capsule and a maroon burger read as a third
   unrelated control rather than the thing to press. */
.pb-head-mobile .pb-head-cta{ min-height:36px }
.pb-head-cta{
  position:relative; isolation:isolate;
  display:inline-flex; align-items:center; gap:6px; flex:0 0 auto; white-space:nowrap;
  border:0; cursor:pointer; font:inherit; font-weight:800; font-size:13px; letter-spacing:.02em;
  padding:0 15px; height:36px; border-radius:12px; color:#331a04;
  /* Two pixels taller than the capsule beside it, deliberately. Matching
     heights made the row read as four settings in a line; the small
     difference is what says one of these is the thing to press.

     Two gradients, stacked, because they do different jobs.

     The lower one carries the colour and runs LEFT TO RIGHT: it opens on
     the same gold as the page's "Explore test series" button, holds it
     across most of the face, then turns through amber into a sunset at the
     right edge. The upper one is only light -- a bright wash at the top
     fading to a shadow at the base -- which is what keeps the thing reading
     as struck metal rather than as a printed rectangle. Doing both in one
     gradient is not possible; a gradient has one axis.

     How far the sunset is allowed to darken is not a taste decision. The
     label sits ACROSS this ramp, roughly 18% to 82% of the width, so every
     stop under the text has to clear 4.5:1 against the ink -- 13px bold
     counts as normal-size text. The deep end of the sunset is therefore
     placed after 88%, inside the right padding where no glyph reaches.
     Measured on the composited result rather than on the stops, because
     the light wash above changes every one of them. */
  background:
    linear-gradient(180deg,rgba(255,249,228,.42) 0%,rgba(255,255,255,.05) 46%,rgba(74,28,4,.20) 100%),
    linear-gradient(90deg,#cfa829 0%,#c9a227 22%,#c79724 46%,#d08a21 64%,#dc7f1d 80%,#e0781c 90%,#c4501b 100%);
  box-shadow:
    inset 0 1px 0 rgba(255,244,214,.85),
    inset 0 0 0 1px rgba(255,220,158,.30),
    inset 0 -1px 0 rgba(74,30,4,.34),
    0 2px 5px -1px rgba(126,72,14,.48),
    0 7px 18px -7px rgba(190,120,28,.72);
  transition:transform .2s cubic-bezier(.2,.8,.3,1), box-shadow .22s ease, filter .16s;
}
/* Gold goes muddy against a dark ground, so it is lifted rather than reused. */
[data-theme="dark"] .pb-head-cta{
  color:#2b1503;
  background:
    linear-gradient(180deg,rgba(255,251,236,.46) 0%,rgba(255,255,255,.07) 46%,rgba(74,28,4,.16) 100%),
    linear-gradient(90deg,#dcb733 0%,#d7b02f 22%,#d5a52b 46%,#e09727 64%,#ec8a21 80%,#f0831f 90%,#d05a1e 100%);
}
/* The shine sweeps by moving the gradient WITHIN the box rather than sliding
   a strip across it. The strip needed overflow:hidden to stay inside the
   button, and overflow:hidden would also clip the ::after further down, which
   is the entire touch target. Moving the background costs nothing and cannot
   escape: at both ends of the travel the bright band sits outside the visible
   third of the image, so the loop point is invisible. */
.pb-head-cta::before{
  content:""; position:absolute; inset:0; z-index:-1; pointer-events:none;
  border-radius:inherit;
  background:linear-gradient(96deg,
    transparent 30%,
    rgba(255,255,255,.18) 42%,
    rgba(255,255,255,.85) 50%,
    rgba(255,255,255,.18) 58%,
    transparent 70%);
  background-size:300% 100%;
  background-position:100% 0;
}
@keyframes pb-cta-shine{
  0%,64%   { background-position:100% 0 }
  93%,100% { background-position:0% 0 }
}
.pb-head-cta:hover{ transform:translateY(-1.5px); filter:brightness(1.07) saturate(1.06);
  box-shadow:
    inset 0 1px 0 rgba(255,247,222,.95),
    inset 0 0 0 1px rgba(255,226,172,.44),
    inset 0 -1px 0 rgba(74,30,4,.36),
    0 4px 9px -2px rgba(126,72,14,.52),
    0 12px 26px -8px rgba(205,124,30,.92) }
/* Pressed metal: the lit edge moves to the bottom and the face darkens. */
.pb-head-cta:active{ transform:translateY(1px) scale(.975); transition-duration:.07s;
  filter:brightness(.96);
  box-shadow:
    inset 0 2px 5px rgba(64,28,3,.44),
    inset 0 -1px 0 rgba(255,240,208,.4) }
.pb-head-cta:focus-visible{ outline:2.5px solid var(--brand-700); outline-offset:2px }
.pb-head-cta::after{ content:""; position:absolute; left:0; right:0; top:-5px; bottom:-5px }
.pb-head-cta svg{ transition:transform .2s cubic-bezier(.2,.8,.3,1) }
.pb-head-cta:hover svg{ transform:translateX(2px) }

/* Shown only to a visitor who is not signed in: a halo that opens outward and
   fades, the way a ring spreads on water. It is drawn as the last box-shadow
   layer, so it needs no extra element and nothing can clip it — which matters,
   because the touch target is also a pseudo-element and the two would
   otherwise fight over overflow.

   4.9s, and most of that is rest. The point is to catch the corner of
   someone's eye once, not to flash at a person trying to read. */
@keyframes pb-cta-halo{
  0%,60%{ box-shadow:
    inset 0 1px 0 rgba(255,244,214,.85),
    inset 0 0 0 1px rgba(255,220,158,.30),
    inset 0 -1px 0 rgba(74,30,4,.34),
    0 2px 5px -1px rgba(126,72,14,.48),
    0 7px 18px -7px rgba(190,120,28,.72),
    0 0 0 0 rgba(202,126,30,.5) }
  78%{ box-shadow:
    inset 0 1px 0 rgba(255,247,222,.95),
    inset 0 0 0 1px rgba(255,226,172,.44),
    inset 0 -1px 0 rgba(74,30,4,.34),
    0 2px 5px -1px rgba(126,72,14,.48),
    0 10px 24px -6px rgba(205,124,30,.92),
    0 0 0 7px rgba(202,126,30,.18) }
  100%{ box-shadow:
    inset 0 1px 0 rgba(255,244,214,.85),
    inset 0 0 0 1px rgba(255,220,158,.30),
    inset 0 -1px 0 rgba(74,30,4,.34),
    0 2px 5px -1px rgba(126,72,14,.48),
    0 7px 18px -7px rgba(190,120,28,.72),
    0 0 0 13px rgba(202,126,30,0) }
}
.pb-head-cta-pulse{ animation:pb-cta-halo 4.9s ease-out infinite }
.pb-head-cta-pulse::before{ animation:pb-cta-shine 5.3s ease-in-out infinite }
/* Hover hands the shadow back to :hover, which a running animation would
   otherwise win. The shine lives on a different element and keeps going. */
.pb-head-cta-pulse:hover{ animation:none }
@media (prefers-reduced-motion: reduce){
  .pb-head-cta-pulse, .pb-head-cta-pulse::before, .pb-head .pb-mark{ animation:none }
  .pb-head-cta, .pb-head-cta svg, .pb-head, .pb-head::after{ transition:none }
  .pb-head-cta:hover, .pb-head-cta:active{ transform:none }
}

/* The burger is navigation, not an action — it should sit behind the gold,
   not compete with it in a bordered box of its own. */
@media (max-width:1000px){
  /* Same glass family as the capsule so the row reads as two materials —
     glass for navigation and settings, gold for the one action. */
  .pb-burger{
    width:34px; height:34px; min-height:34px; border-radius:11px;
    background:color-mix(in srgb,var(--cream-50) 62%,transparent);
    border:1px solid color-mix(in srgb,var(--line) 78%,transparent);
    -webkit-backdrop-filter:blur(10px) saturate(1.5);
    backdrop-filter:blur(10px) saturate(1.5);
    box-shadow:inset 0 1px 0 rgba(255,255,255,.5);
    color:var(--ink-600); position:relative;
  }
  .pb-head-in .pb-burger{ min-height:34px }
  .pb-burger::after{ content:""; position:absolute; left:-4px; right:-4px; top:-5px; bottom:-5px }
  .pb-burger:hover{ background:color-mix(in srgb,var(--gold-300) 26%,transparent);
    color:var(--brand-700) }
}
@media (max-width:1000px){
  .pb-head-mobile{display:flex}
  .pb-brand{flex:1 1 auto;min-width:0;overflow:hidden}
  .pb-brand > span{min-width:0}
  .pb-name{overflow:hidden;text-overflow:ellipsis}
  /* One copy of the controls, not two: the header copy is always visible, so
     the one inside the collapsed nav would only be a duplicate. */
  /* Language and theme are in the header capsule on a phone, so this copy
     would only duplicate them — but hiding the whole block took the colour
     chooser with it. The menu now shows the palette picker on its own. */
  .pb-nav-chrome{display:none}
  .pb-nav-palette{display:flex;align-items:center;justify-content:space-between;gap:10px;
    width:100%;padding:10px 12px;margin-top:2px;border-top:1px solid var(--line)}
  .pb-nav-palette-l{font-size:14px;font-weight:600;color:var(--ink-600)}
  .pb-head-in{gap:8px}
  .pb-nav{margin-left:0}
}
/* ---- HEADER AT PHONE WIDTHS ----------------------------------------
   Four things compete for one row: wordmark, language+theme capsule, the
   login action, and the burger. Nothing here may be dropped — each was put
   in the header on purpose — so the row gives up size in steps instead.

   Measured in Hindi, which is the tight case: "लॉगिन" is wider than "Log in"
   and it was Hindi that clipped the wordmark to "JUNOONIA". Every tier below
   was checked at 320/360/375/414 with the Hindi copy loaded. */
@media (max-width:560px){
  .pb-tagline{display:none}
  .pb-head-in{padding:8px 11px;gap:5px}
  .pb-head-mobile{gap:4px}
  .pb-brand{gap:8px}
  .pb-name{font-size:16px}
  .pb-mark{width:32px !important;height:32px !important}
  .pb-head-cta{padding:0 15px;font-size:13px}
  .jn-seg .jn-seg-btn{padding:0 8px}
  .pb-burger{width:34px}
}
@media (max-width:400px){
  .pb-brand{gap:7px}
  .pb-name{font-size:15px}
  .pb-mark{width:30px !important;height:30px !important}
  .pb-head-cta{padding:0 13px;font-size:12.5px}
  .jn-seg .jn-seg-btn{padding:0 7px}
}
/* 375px and 360px fitted the wordmark with nothing to spare — need and have
   were the same number to the pixel. That is not a fit, it is a coincidence:
   a device whose font metrics round the other way clips the "S". This tier
   buys a few pixels back from spacing rather than from the name itself. */
@media (max-width:380px){
  .pb-head-in{padding-inline:8px}
  .pb-brand{gap:6px}
  .jn-seg-label{font-size:11px}
}
@media (max-width:365px){
  /* The globe goes, not the label. "EN" / "हि" names the language outright;
     the globe only repeats it, and at this width repetition costs the
     wordmark its last two letters. The theme icon stays — an icon is all it
     has ever had. */
  .jn-seg-btn:first-child > svg{display:none}
  .pb-name{font-size:14.5px}
  .pb-mark{width:28px !important;height:28px !important}
  .pb-head-cta{padding:0 11px;font-size:12px}
  .pb-head-in{padding:8px 9px;gap:4px}
}
/* 320px — the narrowest phone still in use. The wordmark stays; it is the one
   thing on this row that cannot be replaced by an icon. Everything else gives
   up another pixel or two so it can. */
@media (max-width:340px){
  /* "One exam. One price." wants 253px of the 240px this screen offers, and
     falls to a line per sentence. Two pixels off the heading buys 20 and
     keeps the pair together -- cheaper than taking the room from the
     section's margins, which every other block on the page is using. */
  .pb-h2{font-size:23px}
  /* The footer needs nine more pixels a column here, and the reason is worth
     stating: "Previous year papers" fits at 375px and does not at 320px, and
     with only one of the two long labels wrapping the columns stop lining up
     row for row. Either both wrap or neither does; neither is achievable, so
     the margins give way instead. */
  .pb-foot{--foot-pad:12px}
  .pb-foot-links,.pb-foot-supl{column-gap:10px}
  /* The colophon's two rows want 314px and 296px is what this screen has,
     so both wrapped and it went back to being four ragged lines. A step
     down in size buys 33px and holds the pair. */
  .pb-foot-legal button{font-size:11.5px}
  .pb-foot-dot{padding:0 5px}
  .pb-foot-cr{font-size:11px}
  .pb-name{font-size:13.5px}
  .pb-mark{width:26px !important;height:26px !important}
  .pb-head-cta{padding:0 9px;font-size:11.5px}
  .pb-head-in{padding:8px 8px;gap:4px}
}
`;

const money = (n) => "₹" + Number(n || 0).toLocaleString("en-IN", { maximumFractionDigits: 0 });

/* A heading made of short sentences should break BETWEEN them. Left to
   itself the catalogue heading wrapped as

       One exam. One
       price. Nothing extra.

   which reads as a typo rather than a line -- text-wrap:balance is only
   trying to even out the two lines and has no idea a sentence is a unit.

   Each sentence becomes an unbreakable run, so the only break opportunities
   left are the spaces between them. On a phone that yields

       One exam. One price.
       Nothing extra.

   and on a wide screen it still sets on one line, because nothing here
   forces a break -- it only forbids the wrong ones. If a screen is ever
   too narrow even for the first pair, it falls to one sentence per line,
   which is still a sentence per line.

   Splitting on the character rather than with a regex lookbehind: Devanagari
   ends its sentences with a danda, and both marks are handled the same way.
   The heading is centred by .pb-sec-head, so each line centres itself. */
function Sentences({ text }) {
  const parts = [];
  let buf = "";
  for (const ch of text) {
    buf += ch;
    if (ch === "." || ch === "\u0964") { parts.push(buf.trim()); buf = ""; }
  }
  if (buf.trim()) parts.push(buf.trim());

  return parts.map((part, i) => (
    <Fragment key={i}>
      {i > 0 && " "}
      <span style={{ whiteSpace: "nowrap" }}>{part}</span>
    </Fragment>
  ));
}

/* The hero headline, revealed one line at a time. The first line "Lead your
   prep" sweeps in, then a beat later the gold second line "from darkness, unto
   light." follows. Both lines are real text and hold their space from the
   first frame -- the animation is pure CSS (a staggered wipe), so nothing
   below the headline shifts. Keyed on language by the caller, so switching
   EN/HI remounts it and the sweep plays again. */
function HeroHeadline({ a, b }) {
  return (
    <h1 className="pb-h1 pb-h1-anim">
      <span className="pb-h1-l1">{a}</span>
      <em className="pb-h1-l2">{b}</em>
    </h1>
  );
}

/* Reduced-motion preference, read live so a change to the OS setting turns the
   typed lede into plain text at once. */
function usePrefersReducedMotion() {
  const [reduced, setReduced] = useState(
    () => typeof window !== "undefined" && window.matchMedia
      ? window.matchMedia("(prefers-reduced-motion: reduce)").matches : false
  );
  useEffect(() => {
    if (typeof window === "undefined" || !window.matchMedia) return;
    const mq = window.matchMedia("(prefers-reduced-motion: reduce)");
    const on = () => setReduced(mq.matches);
    on();
    mq.addEventListener?.("change", on);
    return () => mq.removeEventListener?.("change", on);
  }, []);
  return reduced;
}

/* Split into what a reader sees as single characters. Intl.Segmenter keeps a
   Devanagari consonant and its matra together ("तै" is one step, not a base
   plus a mark that flashes in ahead of it); Array.from is the fallback. */
function splitGraphemes(str) {
  if (typeof Intl !== "undefined" && Intl.Segmenter) {
    const seg = new Intl.Segmenter(undefined, { granularity: "grapheme" });
    return Array.from(seg.segment(str), (s) => s.segment);
  }
  return Array.from(str);
}

/* The hero lede runs in two acts. First it TYPES itself in, character by
   character, from "We don't just" to "who sat the same paper" -- no caret.
   Then, once it is complete, a glassmorphism sheen SWEEPS across it a line at a
   time: left to right, one line after another, each line taking the same time
   typing it did (its length x the per-character pace). The closing line "Your
   race starts here." fades in when the typing lands, and is not part of the
   sheen.

   A ghost of the finished paragraph is laid out but never painted so it holds
   the block open -- nothing below jumps -- and the live copy is painted over
   it. The line wraps are measured off the ghost (present from the first frame)
   so the sheen pass knows where each visual line is. A visually-hidden copy
   carries the whole text for assistive tech. Keyed on language by the caller,
   so switching EN/HI replays both acts; reduced-motion readers get it whole. */
const LEDE_PER = 20, LEDE_START = 260;   // typing: ms per character, and the lead-in
/* The sheen keeps its own clock, slower than the typing it follows: that pass
   is a hand writing the words, this one is a light crossing them once they are
   written, and at the typewriter's pace it went by before the eye caught it.
   SHEEN_PAUSE is the rest between passes -- without it a loop reads as a
   stutter rather than as something that comes round again. */
const SHEEN_PER = 46, SHEEN_MIN = 320, SHEEN_PAUSE = 1500;

function LedeGlassReveal({ a, b1, bh, b2, c, close }) {
  const reduced = usePrefersReducedMotion();
  const ghostRef = useRef(null);
  const [lines, setLines] = useState(null);           // measured visual lines
  const [n, setN] = useState(0);                      // characters typed so far
  const [typingDone, setTypingDone] = useState(false); // act 1 complete -> sheen
  const [cycle, setCycle] = useState(0);              // which pass of the sheen
  const [measure, setMeasure] = useState(0);          // bumped on resize

  // Three runs in reading order for the typewriter: plain, gold highlight, plain.
  const segs = useMemo(() => [
    { g: splitGraphemes(`${a} ${b1}`), hi: false },
    { g: splitGraphemes(bh), hi: true },
    { g: splitGraphemes(`${b2} ${c}`), hi: false },
  ], [a, b1, bh, b2, c]);
  const total = useMemo(() => segs.reduce((s, x) => s + x.g.length, 0), [segs]);

  const fullText = `${a} ${b1}${bh}${b2} ${c}`;
  const hiStart = `${a} ${b1}`.length;
  const hiEnd = hiStart + bh.length;
  const fullMain = (
    <>{a}{" "}{b1}<b className="pb-lede-hi">{bh}</b>{b2}{" "}{c}</>
  );

  // Measure where the finished paragraph wraps (off the laid-out ghost), so the
  // sheen pass can light one visual line at a time.
  useLayoutEffect(() => {
    if (reduced) return;
    const host = ghostRef.current?.querySelector(".pb-lede-main");
    if (!host) return;
    const walker = document.createTreeWalker(host, NodeFilter.SHOW_TEXT);
    const range = document.createRange();
    const starts = [];
    let idx = 0, lastTop = null, node;
    while ((node = walker.nextNode())) {
      const len = node.nodeValue.length;
      for (let i = 0; i < len; i++) {
        range.setStart(node, i); range.setEnd(node, i + 1);
        const r = range.getBoundingClientRect();
        // A character whose top jumps down starts a new visual line. Collapsed
        // wrap-spaces have zero height and stay with the line before them.
        if (r.height > 0 && (lastTop === null || r.top > lastTop + 2)) {
          starts.push(idx); lastTop = r.top;
        }
        idx++;
      }
    }
    if (!starts.length) starts.push(0);
    setLines(starts.map((s, k) => {
      const e = k + 1 < starts.length ? starts[k + 1] : fullText.length;
      return { s, e, chars: e - s };
    }));
  }, [reduced, fullText, measure]);

  // Act 1: type the paragraph in, then hand off to the sheen after a short beat.
  useEffect(() => {
    if (reduced) return;
    const timers = [];
    let i = 0;
    const step = () => {
      setN(++i);
      if (i < total) timers.push(setTimeout(step, LEDE_PER));
      else timers.push(setTimeout(() => setTypingDone(true), 140));
    };
    timers.push(setTimeout(step, LEDE_START));
    return () => timers.forEach(clearTimeout);
  }, [reduced, total]);

  // Act 2 loops. When the sheen has crossed the last line it waits a beat and
  // runs the whole pass again. Bumping the cycle re-keys the lines below, and
  // that remount is what restarts their CSS animations from the top with the
  // per-line stagger intact -- iteration-count cannot do it, because after the
  // first pass every line would lose its delay and light in unison.
  useEffect(() => {
    if (reduced || !typingDone || !lines) return;
    const sweep = lines.reduce((t, l) => t + Math.max(l.chars * SHEEN_PER, SHEEN_MIN), 0);
    const id = setTimeout(() => setCycle((v) => v + 1), sweep + SHEEN_PAUSE);
    return () => clearTimeout(id);
  }, [reduced, typingDone, lines, cycle]);

  // The paragraph stays split into pre-measured, non-wrapping lines now that
  // the sheen runs forever -- it no longer swaps back to plain text after one
  // pass. So a resize has to re-measure, or those lines keep the wrapping of
  // the screen they were measured on.
  useEffect(() => {
    if (reduced) return;
    let t = 0;
    const onResize = () => { clearTimeout(t); t = setTimeout(() => setMeasure((v) => v + 1), 180); };
    window.addEventListener("resize", onResize);
    return () => { window.removeEventListener("resize", onResize); clearTimeout(t); };
  }, [reduced]);

  // Reduced motion gets the plain paragraph and no passes at all.
  if (reduced) {
    return (
      <p className="pb-lede">{fullMain}{" "}<em className="pb-lede-close">{close}</em></p>
    );
  }

  // Split a slice of the flattened text into plain / gold-highlight runs.
  const runs = (s, e) => {
    const hs = Math.max(s, hiStart), he = Math.min(e, hiEnd);
    const out = [];
    if (hs >= he) out.push({ t: fullText.slice(s, e), hi: false });
    else {
      if (s < hs) out.push({ t: fullText.slice(s, hs), hi: false });
      out.push({ t: fullText.slice(hs, he), hi: true });
      if (he < e) out.push({ t: fullText.slice(he, e), hi: false });
    }
    return out;
  };
  const renderRuns = (parts) => parts.map((p, j) => p.hi
    ? <b className="pb-lede-hi" key={j}>{p.t}</b>
    : <Fragment key={j}>{p.t}</Fragment>);

  let liveMain, closeEl = null;
  if (!typingDone) {
    // Act 1 — the characters typed so far, carrying the highlight through.
    let rem = n;
    liveMain = segs.map((seg, i) => {
      const take = Math.max(0, Math.min(rem, seg.g.length));
      rem -= take;
      const text = seg.g.slice(0, take).join("");
      return seg.hi
        ? <b className="pb-lede-hi" key={i}>{text}</b>
        : <Fragment key={i}>{text}</Fragment>;
    });
  } else {
    // Act 2 — the full text, split into visual lines, a sheen crossing each in
    // turn at the typewriter's pace.
    let acc = 0;
    liveMain = (lines || []).map((ln, i) => {
      const d = Math.max(ln.chars * SHEEN_PER, SHEEN_MIN);
      const delay = acc; acc += d;
      return (
        <span className="pb-glass-sheen-line" key={i}
              style={{ "--d": `${d}ms`, "--delay": `${delay}ms` }}>
          {renderRuns(runs(ln.s, ln.e))}
        </span>
      );
    });
    closeEl = <em className="pb-lede-close pb-glass-close-in">{close}</em>;
  }

  return (
    <p className="pb-lede pb-lede-type">
      {/* Laid out but never painted — holds the block open, and is what the
          line measurement reads. */}
      <span className="pb-lede-ghost" aria-hidden="true" ref={ghostRef}>
        <span className="pb-lede-main">{fullMain}</span>
        <em className="pb-lede-close">{close}</em>
      </span>
      {/* Painted over the ghost — act 1 types, act 2 sweeps line by line. */}
      <span className="pb-lede-live" aria-hidden="true">
        <span className="pb-lede-main" key={typingDone ? "sheen-" + cycle : "typing"}>{liveMain}</span>
        {closeEl}
      </span>
      {/* For screen readers, which get neither of the two above. */}
      <span className="pb-sr">{`${a} ${b1}${bh}${b2} ${c} ${close}`}</span>
    </p>
  );
}

/* The coupon ticket and the refer-and-earn ticket, sharing one slot and
   swiping between themselves on a loop.

   Both tickets stay mounted, stacked in one grid cell, so the slot never
   changes height as they trade places and the page below cannot shift. The
   rotation holds while a pointer is over the strip or a keyboard is inside it,
   because a control that moves out from under someone mid-reach is the whole
   reason auto-rotating banners have a bad name -- and it does not rotate at all
   under prefers-reduced-motion. The dots below say how many there are and let
   anyone pick one directly. Only the ticket on show is reachable by tab; the
   other's button is taken out of the tab order. */
/* The quote beat below the hero, on the same swipe as the ticket carousel:
   three quotes cycling, held while a pointer or keyboard is inside, still
   under prefers-reduced-motion. Reuses the ticket carousel's stack/slide/dots
   CSS -- only the content differs. */
function QuoteCarousel({ quotes, intervalMs = 6200 }) {
  const reduced = usePrefersReducedMotion();
  const [i, setI] = useState(0);
  const [held, setHeld] = useState(false);
  const n = quotes.length;

  useEffect(() => {
    if (reduced || held || n < 2) return;
    const id = setInterval(() => setI((v) => (v + 1) % n), intervalMs);
    return () => clearInterval(id);
  }, [reduced, held, n, intervalMs]);

  return (
    <div className="pb-band-wrap"
         onMouseEnter={() => setHeld(true)} onMouseLeave={() => setHeld(false)}
         onFocusCapture={() => setHeld(true)} onBlurCapture={() => setHeld(false)}>
      <div className="pb-ticket-stack">
        {quotes.map((q, k) => {
          const on = k === i;
          const pos = on ? "cur" : (k === (i - 1 + n) % n ? "prev" : "next");
          return (
            <div className="pb-ticket-slide" key={q.key} data-pos={pos} aria-hidden={!on}>
              <div className="pb-band-quote">
                <p className="pb-band-h">{q.a}<em>{q.em}</em>{q.b}</p>
                <p className="pb-band-p">{q.line}</p>
              </div>
            </div>
          );
        })}
      </div>
      {n > 1 && (
        <div className="pb-ticket-dots">
          {quotes.map((q, k) => (
            <button key={q.key} className={"pb-tdot" + (k === i ? " on" : "")}
                    aria-label={q.a + q.em + q.b} aria-current={k === i}
                    onClick={() => setI(k)} />
          ))}
        </div>
      )}
    </div>
  );
}

function TicketCarousel({ slides, intervalMs = 5600 }) {
  const reduced = usePrefersReducedMotion();
  const [i, setI] = useState(0);
  const [held, setHeld] = useState(false);
  const n = slides.length;

  useEffect(() => {
    if (reduced || held || n < 2) return;
    const id = setInterval(() => setI((v) => (v + 1) % n), intervalMs);
    return () => clearInterval(id);
  }, [reduced, held, n, intervalMs]);

  return (
    <div className="pb-ticket-wrap reveal"
         onMouseEnter={() => setHeld(true)} onMouseLeave={() => setHeld(false)}
         onFocusCapture={() => setHeld(true)} onBlurCapture={() => setHeld(false)}>
      <div className="pb-ticket-stack">
        {slides.map((s, k) => {
          const on = k === i;
          const pos = on ? "cur" : (k === (i - 1 + n) % n ? "prev" : "next");
          return (
            <div className="pb-ticket-slide" key={s.key} data-pos={pos} aria-hidden={!on}>
              <div className="pb-ticket">
                <span className="pb-notch pb-notch-l" />
                <span className="pb-ticket-ic">{s.icon}</span>
                <div className="pb-ticket-copy">
                  <h4>{s.title}</h4>
                  <p className="pb-ticket-long">{s.body}</p>
                </div>
                <button className="pb-btn pb-btn-maroon" onClick={s.onClick} tabIndex={on ? 0 : -1}>
                  {s.cta}<ArrowRight size={15} />
                </button>
                {/* The phone's line, and a direct child rather than part of the
                    copy block: down there the ticket becomes a two-row grid and
                    this line shares the second row with the button. */}
                <p className="pb-ticket-short">{s.bodyShort}</p>
                <span className="pb-notch pb-notch-r" />
              </div>
            </div>
          );
        })}
      </div>
      {n > 1 && (
        <div className="pb-ticket-dots">
          {slides.map((s, k) => (
            <button key={s.key} className={"pb-tdot" + (k === i ? " on" : "")}
                    aria-label={s.title} aria-current={k === i}
                    onClick={() => setI(k)} />
          ))}
        </div>
      )}
    </div>
  );
}

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
  const { t, lang } = useLang();
  const [bundles, setBundles] = useState(null);
  const [err, setErr] = useState("");
  const [exam, setExam] = useState("all");
  const tabsRef = useRef(null);

  /* The header densifies once the page moves under it. Read through rAF so a
     fast scroll cannot queue a state update per frame, and compared against
     the current value so React only re-renders on the two crossings rather
     than on every pixel. The threshold is 6px, far enough that a rubber-band
     bounce at the very top does not flicker it.

     Deliberately no height change on scroll: the header is sticky, so its box
     is in flow, and shrinking it would pull the whole page up by that many
     pixels the moment someone starts scrolling. */
  const [scrolled, setScrolled] = useState(false);
  useEffect(() => {
    let frame = 0, on = false;
    const read = () => {
      frame = 0;
      const next = window.scrollY > 6;
      if (next !== on) { on = next; setScrolled(next); }
    };
    const onScroll = () => { if (!frame) frame = requestAnimationFrame(read); };
    read();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => { window.removeEventListener("scroll", onScroll); if (frame) cancelAnimationFrame(frame); };
  }, []);

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

  const scrollTo = (id) => setTimeout(() => document.getElementById(id)?.scrollIntoView({ behavior: "smooth" }), 70);
  const goCatalog = () => { setDetail(null); if (page) onNavigate(null); scrollTo("catalog"); };
  const goResources = () => { setDetail(null); if (page) onNavigate(null); scrollTo("resources"); };
  const enroll = (code) => (owned.has(code) ? onDashboard() : onEnroll(code));
  const home = () => { setDetail(null); onNavigate(null); window.scrollTo({ top: 0, behavior: "smooth" }); };

  return (
    <div className="pb-root" ref={revealRoot}>
      <style>{CSS}</style>

      <header className={"pb-head" + (scrolled ? " pb-head-on" : "")}>
        <div className="pb-head-in">
          <button className="pb-brand" onClick={home}>
            <BrandMark />
            <span>
              <span className="pb-name">JUNOON<span>IAS</span></span>
              <span className="pb-tagline">{t("tagline")}</span>
            </span>
          </button>

          {/* Shown only on phones, where the nav collapses. A first-time
              visitor could otherwise find no way to sign in, and no way to
              switch to Hindi, without first discovering the burger — which is
              the one thing a Hindi-medium student needs before anything else. */}
          <div className="pb-head-mobile">
            <ChromeControls segmented />
            <button className={"pb-head-cta" + (session ? "" : " pb-head-cta-pulse")}
                    onClick={session ? onDashboard : onLogin}>
              <span>{session ? t("nav_dashboard") : t("nav_login")}</span>
              <ArrowRight size={14} />
            </button>
          </div>

          <button className="pb-burger" onClick={() => setNavOpen(!navOpen)} aria-label="Menu" aria-expanded={navOpen}>
            {navOpen ? <X size={19} /> : <Menu size={19} />}
          </button>

          <nav className={"pb-nav" + (navOpen ? " open" : "")}>
            <button className="link" onClick={() => { setNavOpen(false); goCatalog(); }}>{t("nav_tests")}</button>
            <button className="link" onClick={() => { setNavOpen(false); onNavigate("syllabus"); }}>{t("nav_syllabus")}</button>
            <button className="link" onClick={() => { setNavOpen(false); goResources(); }}>{t("nav_free")}</button>
            <button className="link" onClick={() => { setNavOpen(false); onNavigate("faq"); }}>{t("nav_faq")}</button>
            <span className="pb-nav-chrome"><ChromeControls palettePicker /></span>
            <span className="pb-nav-palette">
              <span className="pb-nav-palette-l">{t("nav_colour")}</span>
              <ChromeControls paletteOnly />
            </span>
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
            {/* Three areas rather than two columns of content. On a wide
                screen they resolve to the same thing -- text left, lamp right,
                lamp spanning both rows. On a phone the headline and the lamp
                share the top row so the lamp keeps the side it has on
                desktop, and everything below it runs the full width. Stacked,
                the lamp was a 190px block of its own before a word was read.

                The Upanisad line is not repeated here. It has its own section
                further down, with the translation and the citation, which is
                where it earns the room. */}
            <div className="pb-hero-grid">
              <div className="pb-hero-head">
                {/* keyed on language so switching EN/HI retypes the line */}
                <HeroHeadline key={lang} a={t("hero_h1_a")} b={t("hero_h1_b")} />
              </div>
              <div className="pb-stage"><Diya size={330} /></div>
              <div className="pb-hero-body">
                {/* keyed on language so switching EN/HI replays the reveal */}
                <LedeGlassReveal key={lang}
                  a={t("hero_lede_a")} b1={t("hero_lede_b1")} bh={t("hero_lede_bh")}
                  b2={t("hero_lede_b2")} c={t("hero_lede_c")} close={t("hero_lede_d")} />
                <div className="pb-hero-ctas">
                  <button className="pb-btn pb-btn-gold" onClick={goCatalog}>
                    <Compass size={17} />{t("cta_explore")}<ArrowRight size={17} />
                  </button>
                  <button className="pb-btn pb-btn-onDark" onClick={goResources}>
                    <BookOpen size={17} />{t("cta_browse_free")}
                  </button>
                </div>
              </div>
              {/* Its own row across the foot of the hero. Inside the text
                  column it was 490px carrying three claims, so every label
                  broke over two lines. */}
              <ul className="pb-ticks">
                <li><span className="tick-ic"><BarChart3 size={18} /></span><b>{t("tick_rank")}</b><span className="tick-s">{t("tick_rank_s")}</span></li>
                <li><span className="tick-ic"><TargetArrow size={18} /></span><b>{t("tick_pattern")}</b><span className="tick-s">{t("tick_pattern_s")}</span></li>
                <li><span className="tick-ic"><Layers size={18} /></span><b>{t("tick_gsca")}</b><span className="tick-s">{t("tick_gsca_s")}</span></li>
                <li><span className="tick-ic"><History size={18} /></span><b>{t("tick_pyq")}</b><span className="tick-s">{t("tick_pyq_s")}</span></li>
                <li><span className="tick-ic"><Calculator size={18} /></span><b>{t("tick_csat")}</b><span className="tick-s">{t("tick_csat_s")}</span></li>
                <li><span className="tick-ic"><ShieldCheck size={18} /></span><b>{t("tick_secure")}</b><span className="tick-s">{t("tick_secure_s")}</span></li>
              </ul>
            </div>
          </section>

          {/* ---------------- STRIP ----------------
              Every line here is checkable against the product. The old site
              claimed "1000+ aspirants" against 12 registered accounts; that
              claim is gone rather than restyled. */}
          <div className="pb-band">
            <Mandala className="pb-band-mandala" />
            <div className="pb-band-in reveal">
              <div className="pb-band-rule" />
              <QuoteCarousel quotes={[
                { key: "q1", a: t("band1_a"), em: t("band1_em"), b: t("band1_b"), line: t("band1_l") },
                { key: "q2", a: t("band2_a"), em: t("band2_em"), b: t("band2_b"), line: t("band2_l") },
                { key: "q3", a: t("band3_a"), em: t("band3_em"), b: t("band3_b"), line: t("band3_l") },
                { key: "q4", a: t("band4_a"), em: t("band4_em"), b: t("band4_b"), line: t("band4_l") },
              ]} />
            </div>
          </div>

          {/* ---------------- CATALOG ---------------- */}
          <section className="pb-sec" id="catalog">
            <div className="pb-sec-narrow">
              <div className="pb-sec-head reveal">
                <Mandala className="pb-sec-mandala" />
                <div className="pb-eyebrow">{t("nav_tests")}</div>
                <h2 className="pb-h2"><Sentences text={t("cat_h2")} /></h2>
                {/* An English tagline by design -- its punch does not survive a
                    translation, so it reads the same in both languages. */}
                <p className="pb-hook">You’ve chosen your battle. We won’t charge you for someone else’s.</p>
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
            </div>
          </section>

          {/* ---------------- COUPON ---------------- */}
          {/* The wrapper is full width and exists only to carry the cream ramp
              out of the dark band above; the section inside stays centred. */}
          <div className="pb-coupon-band">
          <div className="pb-sec pb-sec-narrow pb-sec-coupon">
            {/* Two offers in the one strip. Refer-and-earn needs an account —
                the invite link lives on the dashboard — so it sends a signed-in
                visitor there and everyone else to the login screen. */}
            <TicketCarousel slides={[
              { key: "coupon", icon: <TicketIcon size={24} />, title: t("coupon_h4"),
                body: t("coupon_p"), bodyShort: t("coupon_p_s"),
                cta: t("coupon_cta"), onClick: goCatalog },
              { key: "refer", icon: <Gift size={23} />, title: t("refer_h4"),
                body: t("refer_p"), bodyShort: t("refer_p_s"),
                cta: t("refer_cta"), onClick: session ? onDashboard : onLogin },
            ]} />
          </div>
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
          A dark band, not a card. It was a cream card on a cream page, which
          made the end of the site look like one more section of it.

          Three blocks: identity and the newsletter, the link columns, and the
          follow row. Grid areas place them, because a phone reads them in a
          different order than a desktop lays them out. The colophon is a
          darker strip below all three. */}
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

            </div>

            <div className="pb-foot-social">
              <p className="pb-foot-follow">{t("foot_follow")}</p>
              <div className="pb-socials">
                {SOCIALS.map((sc) => (sc.href ? (
                  <a className="pb-social" key={sc.label} href={sc.href} aria-label={sc.label}
                     data-net={sc.key} target="_blank" rel="noreferrer noopener">
                    <sc.Icon size={17} />
                  </a>
                ) : (
                  <span className="pb-social pb-social-soon" key={sc.label} data-net={sc.key}
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
                <div className="pb-foot-supl">
                  <button className="flink" onClick={() => setContact(true)}>
                    <Headphones size={13} style={{ verticalAlign: -2, marginRight: 6 }} />{t("foot_help")}
                  </button>
                  <button className="flink" onClick={() => onNavigate("contact")}>{t("lg_contact")}</button>
                </div>
              </div>
            </div>

          </div>
        </div>

        {/* Legal first in the DOM, because on a phone that is the row you
            read first. Desktop reverses the row so the copyright still sits
            left and the links right, which is where they were. */}
        <div className="pb-foot-bottom">
          <div className="pb-foot-legal">
            <button onClick={() => onNavigate("privacy")}>{t("lg_privacy")}</button>
            <span className="pb-foot-dot" aria-hidden="true">&middot;</span>
            <button onClick={() => onNavigate("terms")}>{t("lg_terms")}</button>
            <span className="pb-foot-dot" aria-hidden="true">&middot;</span>
            <button onClick={() => onNavigate("refund")}>{t("lg_refund")}</button>
          </div>
          {/* The copyright and the sign-off share a line. Separately they were
              two more centred rows of near-equal weight, which is the raggedness
              the rest of this footer was just cleaned of. */}
          <span className="pb-foot-cr">
            &copy; {new Date().getFullYear()} JUNOONIAS
            <span className="pb-foot-dot" aria-hidden="true">&middot;</span>
            {t("foot_made")}
          </span>
        </div>
      </footer>

      {contact && <ContactModal onClose={() => setContact(false)} />}
    </div>
  );
}
