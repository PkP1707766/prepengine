import { useState, useEffect } from "react";
import { Globe, Moon, Sun, Palette, Check } from "lucide-react";
import { loadKey, saveKey } from "./storage.js";
import { LangCtx, ThemeCtx, useLang, useTheme, PALETTES } from "./contexts.js";

/* ============================================================
   JUNOONIAS — fonts, brand chrome, language and theme.
   Every screen pulls its copy from here so a wording change is
   made once, in both languages.
   ============================================================ */

function useBrandChrome() {
  useEffect(() => {
    if (typeof document === "undefined") return;
    if (!document.getElementById("junoon-fonts")) {
      const pre1 = document.createElement("link");
      pre1.rel = "preconnect"; pre1.href = "https://fonts.googleapis.com";
      document.head.appendChild(pre1);
      const pre2 = document.createElement("link");
      pre2.rel = "preconnect"; pre2.href = "https://fonts.gstatic.com"; pre2.crossOrigin = "anonymous";
      document.head.appendChild(pre2);
      const l = document.createElement("link");
      l.id = "junoon-fonts";
      l.rel = "stylesheet";
      // Fraunces (display) + Inter (body) + Noto Serif Devanagari, per the
      // agreed design direction. Fraunces is a variable optical-size serif, so
      // headings stay characterful at 48px without turning mushy at 16px.
      l.href = "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700;800&family=Noto+Serif+Devanagari:wght@500;700&display=swap";
      document.head.appendChild(l);
    }
    if (!document.getElementById("junoon-base")) {
      const s = document.createElement("style");
      s.id = "junoon-base";
      s.textContent = `
        html,body,#root{margin:0;background:#fdf6e3}
        *{ -webkit-tap-highlight-color: transparent; }
        :root{
          --font-display:"Fraunces",Georgia,serif;
          --font-quote:"Fraunces",Georgia,serif;
          --font-deva:"Noto Serif Devanagari",serif;
          --font-body:"Inter",system-ui,-apple-system,sans-serif;

          /* ---- BRAND SCALE ----------------------------------------------
             The brand ramp is a variable, not a fixed colour: data-palette
             on <html> swaps it. Ember (maroon + gold) is the default because
             it is the identity that already existed in the login screen, but
             the whole site re-grades cleanly to any of the alternates below.

             Gold, cream and ink stay constant across palettes — they are what
             make every variant still feel like the same product.           */
          --brand-900:#3d0d16; --brand-800:#4a0f19; --brand-700:#631322;
          --brand-600:#7d1a28; --brand-500:#9b2a38;

          --gold-600:#b5871f;  --gold-500:#c9a227;  --gold-300:#e3c877; --gold-100:#f5e6bd;
          --cream-50:#fbf6ec;  --cream-100:#f3ead8; --cream-200:#eadfc7;
          --ink-900:#241a15;   --ink-600:#5a4a3f;   --ink-400:#8a7a6c;
          --line:#e7dcc4;
          --ok-600:#1f7a4c;    --warn-600:#b5871f;  --bad-600:#a3312a;

          /* Illustration-only ramps. The flame must stay warm and bright in
             every palette — a blue flame on a blue page disappears — and the
             lamp stays terracotta so the two never merge into one shape. */
          --flame-hi:#FFF1C4; --flame-mid:#F7C948; --flame-lo:#EE9A2E; --flame-base:#C9521F;
          --clay-hi:#C9814E;  --clay-mid:#93502A;  --clay-lo:#5C2C15;
          --clay-rim:#A8632F; --clay-rim-hi:#DFA06A;

          --radius-lg:22px; --radius-md:14px; --radius-sm:10px;
          --shadow-soft:0 24px 48px -24px rgba(61,13,22,.35);
          --shadow-card:0 10px 30px -12px rgba(61,13,22,.18);
          --shadow-lift:0 22px 44px -18px rgba(61,13,22,.28);
        }

        /* ---- PALETTE VARIANTS -------------------------------------------
           Each one re-grades the brand ramp and the neutrals it sits on.
           Cream/ink shift slightly with the hue so the page reads as one
           designed thing rather than a maroon layout wearing a purple hat. */

        /* Indigo — the most "classic exam hall" of the set. */
        [data-palette="indigo"]{
          --brand-900:#141a3a; --brand-800:#1b2350; --brand-700:#2b3a76;
          --brand-600:#3a4c92; --brand-500:#5162ac;
          --cream-50:#f7f6f0; --cream-100:#eeecdf; --cream-200:#e2dfcd;
          --ink-900:#1b1c28; --ink-600:#4b4c5c; --ink-400:#7c7d8e;
          --line:#ddd9c8;
          --shadow-soft:0 24px 48px -24px rgba(20,26,58,.36);
          --shadow-card:0 10px 30px -12px rgba(20,26,58,.20);
          --shadow-lift:0 22px 44px -18px rgba(20,26,58,.30);
        }
        /* Sapphire — the आसमानी / sky variant. */
        [data-palette="sapphire"]{
          --brand-900:#07293f; --brand-800:#0a3552; --brand-700:#0f5079;
          --brand-600:#1a6b9c; --brand-500:#2f8bbd;
          --gold-600:#c08a1c; --gold-500:#d8a92a; --gold-300:#eed189; --gold-100:#f7ead0;
          --cream-50:#f6f8f6; --cream-100:#e9efee; --cream-200:#dbe4e3;
          --ink-900:#12222a; --ink-600:#42555e; --ink-400:#75868f;
          --line:#d3dedd;
          --shadow-soft:0 24px 48px -24px rgba(7,41,63,.34);
          --shadow-card:0 10px 30px -12px rgba(7,41,63,.18);
          --shadow-lift:0 22px 44px -18px rgba(7,41,63,.28);
        }
        /* Amethyst — deep aubergine, still warm enough for the gold. */
        [data-palette="amethyst"]{
          --brand-900:#2a1038; --brand-800:#38154a; --brand-700:#552271;
          --brand-600:#6d3190; --brand-500:#8a4cae;
          --cream-50:#faf6f6; --cream-100:#f0e9ee; --cream-200:#e4dae2;
          --ink-900:#221a25; --ink-600:#524a58; --ink-400:#847b8b;
          --line:#e2d7de;
          --shadow-soft:0 24px 48px -24px rgba(42,16,56,.36);
          --shadow-card:0 10px 30px -12px rgba(42,16,56,.20);
          --shadow-lift:0 22px 44px -18px rgba(42,16,56,.30);
        }
        /* Forest — quieter, for a calmer look. */
        [data-palette="forest"]{
          --brand-900:#0f2a1e; --brand-800:#153626; --brand-700:#215139;
          --brand-600:#2d6b4b; --brand-500:#438a64;
          --cream-50:#f8f7ee; --cream-100:#edeedd; --cream-200:#dfe2cd;
          --ink-900:#1a2119; --ink-600:#47533f; --ink-400:#79856f;
          --line:#d9ddc6;
          --shadow-soft:0 24px 48px -24px rgba(15,42,30,.34);
          --shadow-card:0 10px 30px -12px rgba(15,42,30,.18);
          --shadow-lift:0 22px 44px -18px rgba(15,42,30,.28);
        }

        /* Dark is a genuine re-grade, not an inversion: the cream becomes a
           warm near-black so the gold still reads as firelight. */
        [data-theme="dark"] [data-palette="indigo"],
        [data-theme="dark"][data-palette="indigo"]{
          --brand-900:#0b0f22; --brand-800:#121737; --brand-700:#8f9ede; --brand-600:#a3b0e6;
          --cream-50:#0f1120; --cream-100:#171a2d; --cream-200:#1f2338;
          --ink-900:#eceef8; --ink-600:#a8adc6; --ink-400:#7d829b; --line:#2a2f48;
        }
        [data-theme="dark"] [data-palette="sapphire"],
        [data-theme="dark"][data-palette="sapphire"]{
          --brand-900:#04161f; --brand-800:#072230; --brand-700:#5fb3dd; --brand-600:#7cc4e8;
          --cream-50:#08161c; --cream-100:#0e2028; --cream-200:#152b34;
          --ink-900:#e6f2f6; --ink-600:#9fb6bf; --ink-400:#748a93; --line:#1e333d;
        }
        [data-theme="dark"] [data-palette="amethyst"],
        [data-theme="dark"][data-palette="amethyst"]{
          --brand-900:#160a1d; --brand-800:#221031; --brand-700:#b585d8; --brand-600:#c69ce4;
          --cream-50:#140d1a; --cream-100:#1d1425; --cream-200:#261c30;
          --ink-900:#f2eaf6; --ink-600:#b6a6c0; --ink-400:#8a7d94; --line:#31243c;
        }
        [data-theme="dark"] [data-palette="forest"],
        [data-theme="dark"][data-palette="forest"]{
          --brand-900:#07160f; --brand-800:#0d2118; --brand-700:#6fbf93; --brand-600:#8bd0aa;
          --cream-50:#0a150f; --cream-100:#101d16; --cream-200:#17261d;
          --ink-900:#e8f3ec; --ink-600:#a3b8ab; --ink-400:#7a8c81; --line:#213026;
        }

        [data-theme="dark"]:root{
          --brand-900:#1c0a0e; --brand-800:#2a0d13; --brand-700:#c4566a;
          --brand-600:#d4707f; --brand-500:#e08a95;
          --gold-600:#d4a63a;  --gold-500:#e0b652;  --gold-300:#f0d68f; --gold-100:#3a2c12;
          --cream-50:#1a0f0b;  --cream-100:#241611; --cream-200:#2e1c15;
          --ink-900:#f6ece0;   --ink-600:#c4ab94;   --ink-400:#96806c;
          --line:#3b2a20;
          --ok-600:#5cc98a;    --warn-600:#e0b652;  --bad-600:#f08a7a;
          --shadow-soft:0 24px 48px -24px rgba(0,0,0,.6);
          --shadow-card:0 10px 30px -12px rgba(0,0,0,.5);
          --shadow-lift:0 22px 44px -18px rgba(0,0,0,.55);
        }

        [lang="hi"] body, [data-applang="hi"]{ --font-body:"Inter",system-ui,sans-serif; }
        .deva{ font-family:var(--font-deva); }
        .display{ font-family:var(--font-display); font-optical-sizing:auto; }

        /* Shared motion. Every animation below is disabled for anyone who has
           asked their system for reduced motion. */
        @keyframes jn-breathe { 0%,100%{ transform:scale(1); opacity:.92 } 50%{ transform:scale(1.06); opacity:1 } }
        @keyframes jn-shimmer { 0%{ background-position:100% 50% } 100%{ background-position:0 50% } }
        @keyframes jn-spin    { to { transform: rotate(360deg) } }
        @keyframes jn-rise    { from { opacity:0; transform: translateY(10px) } to { opacity:1; transform:none } }
        .jn-spin { animation: jn-spin .9s linear infinite; }

        /* Visible focus for keyboard users, invisible for mouse users. */
        :focus-visible { outline: 2px solid #b8923a; outline-offset: 2px; border-radius: 6px; }

        /* ---- ILLUSTRATION MOTION ---------------------------------------
           Every animation here is decorative and every one of them stops
           under prefers-reduced-motion (handled globally further down).   */
        @keyframes ill-flicker{
          0%,100%{ transform:scale(1) translateY(0); opacity:1 }
          28%    { transform:scale(1.035) translateY(-2px); opacity:.94 }
          52%    { transform:scale(.985) translateY(1.5px); opacity:1 }
          74%    { transform:scale(1.02) translateY(-1px); opacity:.97 }
        }
        @keyframes ill-spin{ to{ transform:rotate(360deg) } }
        @keyframes ill-spin-rev{ to{ transform:rotate(-360deg) } }
        @keyframes ill-rise{
          0%  { opacity:0; transform:translateY(6px) scale(.6) }
          25% { opacity:.9 }
          100%{ opacity:0; transform:translateY(-34px) scale(1.15) }
        }
        @keyframes ill-draw{ to{ stroke-dashoffset:0 } }
        @keyframes ill-glow{ 0%,100%{ opacity:.85 } 50%{ opacity:1 } }

        .ill-flame{ transform-origin:120px 118px; animation:ill-flicker 2.9s ease-in-out infinite; }
        .ill-ring{ transform-origin:120px 110px; }
        .ill-ring-a{ animation:ill-spin 52s linear infinite; }
        .ill-ring-b{ animation:ill-spin-rev 74s linear infinite; }
        .ill-ring-c{ animation:ill-spin 120s linear infinite; }
        .ill-ember{ animation:ill-rise 3.6s ease-out infinite; }
        .ill-ember-2{ animation-delay:.9s; animation-duration:4.2s }
        .ill-ember-3{ animation-delay:1.8s; animation-duration:3.1s }
        .ill-ember-4{ animation-delay:2.6s; animation-duration:4.6s }
        .ill-mandala{ color:var(--gold-300); }
        .ill-divider{ color:var(--gold-600); width:120px; height:20px; }

        /* Chart strokes draw themselves in once, when revealed. */
        .in .ill-line-draw{ stroke-dasharray:600; stroke-dashoffset:600; animation:ill-draw 1.6s .2s ease-out forwards; }
        .in .ill-ring-draw{ animation:ill-draw 1.3s .2s ease-out forwards; }

        /* ---- SCROLL REVEAL ----------------------------------------------
           Used sparingly — section headers and cards, not every element. */
        .reveal{ opacity:0; transform:translateY(16px); }
        .reveal.in{ opacity:1; transform:none;
          transition:opacity .62s cubic-bezier(.22,.7,.3,1), transform .62s cubic-bezier(.22,.7,.3,1); }
        .reveal-d1.in{ transition-delay:.07s } .reveal-d2.in{ transition-delay:.14s }
        .reveal-d3.in{ transition-delay:.21s } .reveal-d4.in{ transition-delay:.28s }
        @media (prefers-reduced-motion: reduce){
          .reveal{ opacity:1 !important; transform:none !important; }
        }

        /* Language / theme pills, shared by every shell. */
        .jn-pill{
          display:inline-flex; align-items:center; justify-content:center; gap:5px;
          min-height:34px; padding:6px 12px; border-radius:999px;
          font-size:12.5px; font-weight:700; line-height:1; white-space:nowrap;
          cursor:pointer; backdrop-filter:blur(8px); font-family:inherit;
        }
        .jn-pill-icon{ padding:6px 10px; min-width:34px; }

        /* Colour-theme picker */
        .jn-pal-wrap{ position:relative; }
        .jn-palettes{
          position:absolute; right:0; top:calc(100% + 8px); z-index:80;
          background:var(--cream-50,#fff); border:1px solid var(--line,#e7dcc4);
          border-radius:14px; padding:8px; min-width:216px;
          box-shadow:0 18px 40px -16px rgba(0,0,0,.32);
        }
        .jn-palettes-t{
          font-size:10.5px; font-weight:800; letter-spacing:.12em; text-transform:uppercase;
          color:var(--ink-400,#8a7a6c); padding:6px 10px 8px;
        }
        .jn-pal{
          display:flex; align-items:center; gap:11px; width:100%; text-align:left;
          background:none; border:0; font-family:inherit; cursor:pointer;
          padding:9px 10px; border-radius:10px; color:var(--ink-900,#241a15);
        }
        .jn-pal:hover{ background:var(--cream-100,#f3ead8); }
        .jn-pal.on{ background:var(--cream-200,#eadfc7); }
        .jn-pal b{ display:block; font-size:13.5px; font-weight:700; line-height:1.2; }
        .jn-pal em{ display:block; font-style:normal; font-size:11.5px; color:var(--ink-400,#8a7a6c); margin-top:2px; }
        .jn-pal-sw{
          width:24px; height:24px; border-radius:50%; flex:0 0 auto;
          border:2.5px solid; box-shadow:0 2px 6px rgba(0,0,0,.18);
        }
        .jn-pal svg{ margin-left:auto; color:var(--brand-700,#631322); }

        /* On a phone the trigger sits inside a narrow dropdown column, so a
           right-anchored menu ran off the left edge.

           Note the trap: the public header carries backdrop-filter, and any
           of transform / filter / backdrop-filter on an ancestor makes THAT
           element the containing block for position:fixed — not the viewport.
           So a "fixed bottom sheet" here resolved against the header and
           landed above the fold. Anchoring left/right instead, under the
           header, is both correct and simpler. */
        @media (max-width:860px){
          /* Dropping the wrapper out of the positioning chain lets the menu
             anchor to the full-width nav panel instead of a 38px button. */
          .jn-pal-wrap{ position:static; }
          .jn-palettes{
            left:12px; right:12px; min-width:0; width:auto;
            border-radius:18px; padding:10px;
          }
          .jn-pal{ padding:12px; }
          .jn-pal-sw{ width:28px; height:28px; }
        }

        /* ================= RESPONSIVE BASELINE =========================
           Applies to every screen, public and authenticated. Written once
           here rather than per-shell, because the failures below were
           identical on all five shells.                                  */

        /* iOS Safari zooms the whole page whenever you focus an input whose
           font-size is under 16px. Every input in this app was 13–14.5px,
           which is why the site "didn't render at proper size" on a phone —
           one tap on any field and the viewport was left zoomed in. 16px is
           the only reliable prevention; desktop keeps the tighter sizing. */
        /* Triggered on pointer, not width: an iPad in landscape is 1024px wide
           and still zooms on focus, so a max-width rule would miss it. */
        @media (pointer: coarse) {
          .jn-root input, .jn-root select, .jn-root textarea,
          .pb-root input, .pb-root select, .pb-root textarea,
          .sd-root input, .sd-root select, .sd-root textarea,
          .ad-root input, .ad-root select, .ad-root textarea,
          .ee-root input, .ee-root select, .ee-root textarea {
            font-size: 16px;
          }
        }

        /* Touch targets. On a touch device the WCAG floor is 44px; the audit
           found controls at 23–38px throughout. Only padding and min-height
           are raised, so nothing re-flows on a mouse-driven screen. */
        @media (pointer: coarse) {
          .jn-root button, .pb-root button, .sd-root button,
          .ad-root button, .ee-root button,
          .jn-root a[role="button"], .pb-root a[role="button"] {
            min-height: 44px;
          }
          .jn-root a, .pb-root a, .sd-root a, .ad-root a, .ee-root a {
            padding-block: 4px;
          }
          .pb-root .pb-nav button.link,
          .pb-root .pb-foot button.flink,
          .sd-root .sd-foot button.flink { min-height: 44px; }
          .jn-pill { min-height: 44px; }
          .jn-pill-icon { min-width: 44px; }
          /* Search boxes wrap a bare input in a styled div; the wrapper is the
             real tap target, so it is the one that has to clear 44px. */
          .sd-root .lb-search, .ad-root .search, .pb-root .pb-search { min-height: 44px; }
          .sd-root .lb-search input, .ad-root .search input { min-height: 40px; }
        }

        /* The student/admin topbar is a non-wrapping flex row carrying a
           hamburger, a title, the bell, the language + theme pills, logout and
           an avatar. Adding the pills made it tight on a phone, so on small
           screens the descriptive sub-line is dropped and the title is allowed
           to shrink rather than shove the controls off-screen. */
        @media (max-width: 620px) {
          .sd-root .topbar, .ad-root .topbar { padding-inline: 14px; gap: 8px; }
          .sd-root .topbar .sub, .ad-root .topbar .sub { display: none; }
          .sd-root .topbar h1, .ad-root .topbar h1 {
            font-size: 17px; min-width: 0;
            overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
          }
          .ad-root .tb-admin-name, .ad-root .tb-admin-role { display: none; }
          .sd-root .tb-right, .ad-root .tb-right { gap: 6px; flex: 0 0 auto; }
          .sd-root .jn-pill-label, .ad-root .jn-pill-label { display: none; }
          .sd-root .jn-pill, .ad-root .jn-pill { padding-inline: 10px; }
        }

        /* A flex item defaults to min-width:auto, which means it refuses to
           shrink below its content. Setting min-width:0 down the topbar's left
           branch is what actually lets a long page title ellipsis instead of
           shoving the whole right-hand cluster off the screen — the h1 alone
           was not enough, because its two ancestors were still unshrinkable. */
        .sd-root .topbar > *, .ad-root .topbar > *,
        .sd-root .topbar > * > *, .ad-root .topbar > * > * { min-width: 0; }
        .sd-root .topbar .tb-right, .ad-root .topbar .tb-right { flex: 0 0 auto; }
        .sd-root .topbar h1, .ad-root .topbar h1 {
          overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
        }

        /* Grid blowout guard.
           grid-template-columns:1fr is really minmax(auto, 1fr), and auto
           resolves to min-content. A child with white-space:nowrap therefore
           forces its whole track to the width of the un-wrapped string — the
           admin dashboard's single column computed to 1286px on a 375px screen
           because one "Recently added" question title was nowrap + ellipsis.
           min-width:0 on the children is what lets the track shrink and the
           ellipsis do its job. Same root cause as the topbar above. */
        :where(.pb-root, .sd-root, .ad-root, .ee-root, .jn-root)
        :where(.cols, .stats, .grid2, .grid2b, .test-grid, .mat-grid, .sw-grid,
               .ach-grid, .field-row, .pb-grid, .pb-feat, .pb-detail, .res-grid,
               .foot-grid, .bd-row, .lb-row, .toggle-row, .prof-head,
               .exam-body, .res-grid, .picked-q, .picker-item) > * {
          min-width: 0;
        }

        /* Long unbroken strings — an email, a URL, a Devanagari compound —
           were the one thing that could still push a card past the viewport.
           :where() keeps specificity at zero so no existing rule is
           disturbed. */
        :where(.jn-root, .pb-root, .sd-root, .ad-root, .ee-root)
        :where(p, h1, h2, h3, h4, h5, li, td, th, span, div, a, label) {
          overflow-wrap: anywhere;
        }

        /* Media never outgrows its column. */
        :where(.jn-root, .pb-root, .sd-root, .ad-root, .ee-root)
        :where(img, svg, video, canvas, iframe) { max-width: 100%; }

        /* Stop iOS inflating text in landscape. */
        html { -webkit-text-size-adjust: 100%; }

        /* Respect notches and home indicators. Each selector keeps its own
           horizontal padding as the floor, so nothing shifts on a device
           without insets. */
        @supports (padding: max(0px)) {
          .pb-head-in, .pb-sec, .pb-foot-in, .pb-foot-bottom {
            padding-left: max(22px, env(safe-area-inset-left));
            padding-right: max(22px, env(safe-area-inset-right));
          }
          .sd-root .content, .ad-root .content, .sd-foot {
            padding-left: max(26px, env(safe-area-inset-left));
            padding-right: max(26px, env(safe-area-inset-right));
          }
          .sd-root, .ad-root, .ee-root, .pb-root {
            padding-bottom: env(safe-area-inset-bottom);
          }
        }

        @media (prefers-reduced-motion: reduce) {
          *, *::before, *::after {
            animation-duration: .001ms !important;
            animation-iteration-count: 1 !important;
            transition-duration: .001ms !important;
            scroll-behavior: auto !important;
          }
        }
      `;
      document.head.appendChild(s);
    }
  }, []);
}

const STR = {
  brand: { en: "JUNOONIAS", hi: "जुनूनIAS" },
  tagline: { en: "An Academy of Inner Fire", hi: "अंतर्ज्वाला की अकादमी" },
  shloka_en: { en: "Lead me from darkness, unto light.", hi: "मुझे अंधकार से प्रकाश की ओर ले चलो।" },
  intro_sub: { en: "Your complete preparation platform for the civil services.", hi: "सिविल सेवा की तैयारी का आपका सम्पूर्ण मंच।" },
  feat_tests: { en: "Real exam-style mock tests", hi: "वास्तविक परीक्षा-शैली मॉक टेस्ट" },
  feat_analytics: { en: "Deep performance analytics", hi: "गहन प्रदर्शन विश्लेषण" },
  feat_rank: { en: "Rank, percentile & leaderboard", hi: "रैंक, पर्सेंटाइल और लीडरबोर्ड" },
  feat_material: { en: "Expert study material", hi: "विशेषज्ञ अध्ययन सामग्री" },
  welcome_back: { en: "Welcome back", hi: "पुनः स्वागत है" },
  signin_sub: { en: "Sign in to continue your preparation", hi: "तैयारी जारी रखने के लिए साइन इन करें" },
  create_acc: { en: "Create your account", hi: "अपना खाता बनाएँ" },
  create_sub: { en: "Begin your journey today — it's free", hi: "आज ही अपनी यात्रा शुरू करें — निःशुल्क" },
  phone_login: { en: "Login with phone", hi: "फ़ोन से लॉगिन" },
  phone_sub: { en: "We'll send a one-time code to your phone", hi: "हम आपके फ़ोन पर एक OTP भेजेंगे" },
  verify_otp: { en: "Verify OTP", hi: "OTP सत्यापित करें" },
  tab_signin: { en: "Sign In", hi: "साइन इन" },
  tab_signup: { en: "Sign Up", hi: "साइन अप" },
  full_name: { en: "Full name", hi: "पूरा नाम" },
  email_addr: { en: "Email address", hi: "ईमेल पता" },
  password: { en: "Password", hi: "पासवर्ड" },
  min8: { en: "Minimum 8 characters", hi: "कम से कम 8 अक्षर" },
  pwd_hint: { en: "At least 8 characters, including a number or symbol.", hi: "कम से कम 8 अक्षर, जिनमें एक अंक या चिह्न हो।" },
  phone_no: { en: "Phone number", hi: "फ़ोन नंबर" },
  phone_hint: { en: "+91 is added automatically if omitted.", hi: "यदि न लिखें तो +91 स्वतः जुड़ जाएगा।" },
  otp_code: { en: "6-digit code", hi: "6-अंकों का कोड" },
  btn_signin: { en: "Sign in", hi: "साइन इन करें" },
  btn_create: { en: "Create account", hi: "खाता बनाएँ" },
  btn_send_otp: { en: "Send OTP", hi: "OTP भेजें" },
  btn_verify: { en: "Verify & Login", hi: "सत्यापित करें और लॉगिन" },
  or: { en: "or", hi: "अथवा" },
  google: { en: "Continue with Google", hi: "Google से जारी रखें" },
  use_phone: { en: "Login with phone OTP", hi: "फ़ोन OTP से लॉगिन करें" },
  use_email: { en: "Back to email login", hi: "ईमेल लॉगिन पर वापस" },
  resend: { en: "Resend code", hi: "कोड पुनः भेजें" },
  admin_console: { en: "Admin console", hi: "एडमिन कंसोल" },
  please_wait: { en: "Please wait…", hi: "कृपया प्रतीक्षा करें…" },
  contact_us: { en: "Contact us", hi: "संपर्क करें" },
  need_help: { en: "Need help?", hi: "मदद चाहिए?" },
  help_sub: { en: "Our team usually replies within a few hours.", hi: "हमारी टीम आमतौर पर कुछ घंटों में उत्तर देती है।" },
  close: { en: "Close", hi: "बंद करें" },
  // validation / auth messages
  err_email_req: { en: "Please enter your email.", hi: "कृपया अपना ईमेल दर्ज करें।" },
  err_pwd_req: { en: "Please enter your password.", hi: "कृपया अपना पासवर्ड दर्ज करें।" },
  err_name_req: { en: "Please enter your name.", hi: "कृपया अपना नाम दर्ज करें।" },
  err_pwd_short: { en: "Password must be at least 8 characters.", hi: "पासवर्ड कम से कम 8 अक्षरों का होना चाहिए।" },
  err_phone: { en: "Please enter a valid phone number.", hi: "कृपया एक मान्य फ़ोन नंबर दर्ज करें।" },
  err_otp: { en: "Please enter a valid code.", hi: "कृपया एक मान्य कोड दर्ज करें।" },
  err_bad_login: { en: "Email or password is incorrect.", hi: "ईमेल या पासवर्ड ग़लत है।" },
  err_bad_otp: { en: "The code is invalid or has expired.", hi: "कोड अमान्य है या समाप्त हो चुका है।" },
  ok_acc_created: { en: "Account created! Please sign in.", hi: "खाता बन गया! कृपया साइन इन करें।" },
  ok_otp_sent: { en: "Code sent to", hi: "कोड भेजा गया" },
  // ----- join / paywall -----
  join_hi: { en: "Hello", hi: "नमस्ते" },
  join_title: { en: "One step left to begin", hi: "शुरू करने के लिए बस एक कदम" },
  join_sub: { en: "Unlock the full test series and start preparing today.", hi: "पूरी टेस्ट सीरीज़ अनलॉक करें और आज ही तैयारी शुरू करें।" },
  plan_name: { en: "Prelims Test Series 2026", hi: "प्रीलिम्स टेस्ट सीरीज़ 2026" },
  plan_tests: { en: "30 full-length mock tests", hi: "30 पूर्ण-लंबाई मॉक टेस्ट" },
  plan_analytics: { en: "Detailed performance analytics", hi: "विस्तृत प्रदर्शन विश्लेषण" },
  plan_solutions: { en: "Solutions & explanations for every question", hi: "हर प्रश्न का हल और व्याख्या" },
  plan_rank: { en: "All-India rank & percentile", hi: "अखिल भारतीय रैंक और पर्सेंटाइल" },
  plan_validity: { en: "Valid till the 2026 exam", hi: "2026 परीक्षा तक मान्य" },
  plan_best: { en: "BEST VALUE", hi: "सर्वोत्तम मूल्य" },
  pay_join: { en: "Pay & Join now", hi: "भुगतान करें और जुड़ें" },
  secure_pay: { en: "Secure payment via Razorpay · UPI, cards, netbanking", hi: "Razorpay से सुरक्षित भुगतान · UPI, कार्ड, नेटबैंकिंग" },
  already_enrolled: { en: "Checking your access…", hi: "आपकी पहुँच जाँच रहे हैं…" },
  pay_failed: { en: "Payment could not be started. Please try again.", hi: "भुगतान शुरू नहीं हो सका। कृपया पुनः प्रयास करें।" },
  pay_processing: { en: "Confirming your payment…", hi: "आपके भुगतान की पुष्टि हो रही है…" },
  logout: { en: "Log out", hi: "लॉग आउट" },
  one_time: { en: "one-time", hi: "एकमुश्त" },
};

/* Additional copy added for the market build. */
Object.assign(STR, {
  forgot_pwd:      { en: "Forgot password?", hi: "पासवर्ड भूल गए?" },
  reset_title:     { en: "Reset your password", hi: "अपना पासवर्ड रीसेट करें" },
  reset_sub:       { en: "We'll email you a secure link to set a new password.", hi: "हम आपको नया पासवर्ड बनाने के लिए एक सुरक्षित लिंक ईमेल करेंगे।" },
  btn_send_reset:  { en: "Send reset link", hi: "रीसेट लिंक भेजें" },
  ok_reset_sent:   { en: "Check your inbox for the reset link.", hi: "रीसेट लिंक के लिए अपना इनबॉक्स देखें।" },
  ok_check_email:  { en: "Almost there — confirm your email to activate the account.", hi: "बस थोड़ा और — खाता सक्रिय करने के लिए अपना ईमेल सत्यापित करें।" },
  err_pwd_weak:    { en: "Add a number or a symbol to make this password stronger.", hi: "इस पासवर्ड को मज़बूत बनाने के लिए एक अंक या चिह्न जोड़ें।" },
  err_rate:        { en: "Too many attempts. Please wait a minute and try again.", hi: "बहुत अधिक प्रयास। कृपया एक मिनट प्रतीक्षा करें।" },
  err_network:     { en: "Network problem. Check your connection and try again.", hi: "नेटवर्क समस्या। कनेक्शन जाँचें और पुनः प्रयास करें।" },
  agree_terms:     { en: "By continuing you agree to our Terms and Privacy Policy.", hi: "जारी रखकर आप हमारी शर्तों और गोपनीयता नीति से सहमत होते हैं।" },
  pay_success:     { en: "Payment confirmed. Welcome to JUNOONIAS! 🪔", hi: "भुगतान की पुष्टि हुई। JUNOONIAS में आपका स्वागत है! 🪔" },
  pay_pending:     { en: "Payment received — activating your access. This can take a few seconds.", hi: "भुगतान प्राप्त — आपकी पहुँच सक्रिय हो रही है। कुछ क्षण लग सकते हैं।" },
  loading:         { en: "Loading…", hi: "लोड हो रहा है…" },
  retry:           { en: "Try again", hi: "पुनः प्रयास करें" },
  refund_note:     { en: "7-day refund if you're not satisfied.", hi: "संतुष्ट न होने पर 7 दिन में धन-वापसी।" },
});


export function AppProviders({ children }) {
  useBrandChrome();
  const [lang, setLangRaw] = useState(() => loadKey("lang", "en"));
  const [theme, setTheme] = useState(() => loadKey("theme", "light"));
  const [palette, setPaletteRaw] = useState(() => loadKey("palette", "ember"));

  const setLang = (l) => { setLangRaw(l); saveKey("lang", l); };
  const setPalette = (p) => { setPaletteRaw(p); saveKey("palette", p); };
  const toggle = () => setTheme((p) => { const n = p === "light" ? "dark" : "light"; saveKey("theme", n); return n; });
  const t = (k) => (STR[k] && (STR[k][lang] ?? STR[k].en)) ?? k;

  useEffect(() => {
    if (typeof document === "undefined") return;
    const el = document.documentElement;
    el.setAttribute("data-theme", theme);
    el.setAttribute("data-applang", lang);
    el.setAttribute("lang", lang);
    el.setAttribute("data-palette", palette);
    // Keep the browser chrome in step with the page, per palette.
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) {
      const p = PALETTES.find((x) => x.key === palette) || PALETTES[0];
      meta.setAttribute("content", theme === "light" ? p.cream : "#150609");
    }
  }, [theme, lang, palette]);

  return (
    <ThemeCtx.Provider value={{ theme, toggle, palette, setPalette }}>
      <LangCtx.Provider value={{ lang, t, setLang }}>{children}</LangCtx.Provider>
    </ThemeCtx.Provider>
  );
}

/* Floating language + theme toggles. */
export function ChromeControls({ light = false, palettePicker = false }) {
  const { lang, setLang } = useLang();
  const { theme, toggle, palette, setPalette } = useTheme();
  const [open, setOpen] = useState(false);
  // These are inline-styled, and inline styles beat the stylesheet — so the
  // touch-target floor has to be set here rather than in the CSS baseline.
  // The audit measured them at 28px tall on both phone and tablet.
  // Only the colours are inline; all sizing lives in .jn-pill so the
  // coarse-pointer touch-target rule can raise it. An inline minHeight would
  // beat the stylesheet and pin these at the wrong size on a phone.
  const pill = {
    border: "1px solid " + (light ? "rgba(255,255,255,.38)" : "rgba(107,26,26,.22)"),
    background: light ? "rgba(0,0,0,.22)" : "rgba(255,255,255,.82)",
    color: light ? "#fdeecb" : "#5c3018",
  };
  return (
    <div style={{ display: "flex", gap: 6 }}>
      <button type="button" className="jn-pill" style={pill} onClick={() => setLang(lang === "en" ? "hi" : "en")}
              aria-label={lang === "en" ? "Switch to Hindi" : "Switch to English"}>
        <Globe size={13} /> <span className="jn-pill-label">{lang === "en" ? "हिन्दी" : "EN"}</span>
      </button>
      <button type="button" className="jn-pill jn-pill-icon" style={pill} onClick={toggle}
              aria-label={theme === "light" ? "Switch to dark theme" : "Switch to light theme"}>
        {theme === "light" ? <Moon size={14} /> : <Sun size={14} />}
      </button>

      {palettePicker && (
        <div className="jn-pal-wrap" onMouseLeave={() => setOpen(false)}>
          <button type="button" className="jn-pill jn-pill-icon" style={pill}
                  onClick={() => setOpen(!open)} aria-label="Change colour theme" aria-expanded={open}>
            <Palette size={14} />
          </button>
          {open && (
            <div className="jn-palettes" role="menu">
              <div className="jn-palettes-t">Colour theme</div>
              {PALETTES.map((p) => (
                <button key={p.key} role="menuitemradio" aria-checked={palette === p.key}
                        className={"jn-pal" + (palette === p.key ? " on" : "")}
                        onClick={() => { setPalette(p.key); setOpen(false); }}>
                  <span className="jn-pal-sw" style={{ background: p.brand, borderColor: p.cream }} />
                  <span>
                    <b>{p.label}</b>
                    <em>{p.hint}</em>
                  </span>
                  {palette === p.key && <Check size={14} />}
                </button>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
