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
      l.href = "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700;800&family=Marcellus&family=Cormorant+Garamond:ital,wght@0,600;1,400;1,500;1,600&family=Tiro+Devanagari+Hindi:ital@0;1&family=Noto+Serif+Devanagari:wght@500;700&family=Rozha+One&family=Noto+Sans+Devanagari:wght@400;500;600;700&display=swap";
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
          /* Calligraphic italic, for the half-line of a headline that should
             feel written rather than set, and for pull quotes. */
          --font-quote:"Cormorant Garamond",Georgia,serif;
          /* Classical Roman capitals — used only for small tracked-out labels,
             where its lack of a lowercase companion does not matter. */
          --font-roman:"Marcellus",Georgia,serif;
          --font-deva:"Noto Serif Devanagari",serif;
          /* Headline Devanagari. Noto Serif Devanagari is a text face and sets
             headlines flat; Rozha One is the display cut -- high contrast, a
             heavy shirorekha -- and it is what Fraunces is for the Latin side.
             Fraunces carries no Devanagari at all, so a Hindi heading was
             falling through to whatever serif the device happened to have. */
          --font-deva-display:"Rozha One","Noto Serif Devanagari",serif;
          /* A true Devanagari text serif for the shloka. Noto is the safe
             choice for Hindi UI; this is the one worth looking at. */
          --font-shloka:"Tiro Devanagari Hindi","Noto Serif Devanagari",serif;
          --font-body:"Inter",system-ui,-apple-system,sans-serif;

          /* ---- BRAND SCALE ----------------------------------------------
             The brand ramp is a variable, not a fixed colour: data-palette
             on <html> swaps it. Ember (maroon + gold) is the default because
             it is the identity that already existed in the login screen, but
             the whole site re-grades cleanly to any of the alternates below.

             Gold, cream and ink stay constant across palettes — they are what
             make every variant still feel like the same product.           */
          --brand-900:#3d0d16; --foot-ground:#250e10; --brand-800:#4a0f19; --brand-700:#631322;
          --brand-600:#7d1a28; --brand-500:#9b2a38;

          --gold-600:#b5871f;  --gold-500:#c9a227;  --gold-300:#e3c877; --gold-100:#f5e6bd;
          --cream-50:#fbf6ec;  --cream-100:#f3ead8; --cream-200:#eadfc7;
          /* Foreground for surfaces that are dark in BOTH themes — the hero,
             the free-resources band, the buttons sitting on them. Those used
             --cream-50, which the dark palettes flip to a near-black: in dark
             mode the hero headline was rendering #1a0f0b on a #150609
             gradient, i.e. invisible. Deliberately never redefined below. */
          --on-dark:#fbf6ec;
          --on-dark-soft:#e6d8be;
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
          --brand-900:#141a3a; --foot-ground:#14131f; --brand-800:#1b2350; --brand-700:#2b3a76;
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
          --brand-900:#07293f; --foot-ground:#0f1921; --brand-800:#0a3552; --brand-700:#0f5079;
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
          --brand-900:#2a1038; --foot-ground:#1d0f1e; --brand-800:#38154a; --brand-700:#552271;
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
          --brand-900:#0f2a1e; --foot-ground:#121a13; --brand-800:#153626; --brand-700:#215139;
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
          --brand-900:#0b0f22; --foot-ground:#070a18; --brand-800:#121737; --brand-700:#8f9ede; --brand-600:#a3b0e6;
          --cream-50:#0f1120; --cream-100:#171a2d; --cream-200:#1f2338;
          --ink-900:#eceef8; --ink-600:#a8adc6; --ink-400:#7d829b; --line:#2a2f48;
        }
        [data-theme="dark"] [data-palette="sapphire"],
        [data-theme="dark"][data-palette="sapphire"]{
          --brand-900:#04161f; --foot-ground:#020e15; --brand-800:#072230; --brand-700:#5fb3dd; --brand-600:#7cc4e8;
          --cream-50:#08161c; --cream-100:#0e2028; --cream-200:#152b34;
          --ink-900:#e6f2f6; --ink-600:#9fb6bf; --ink-400:#748a93; --line:#1e333d;
        }
        [data-theme="dark"] [data-palette="amethyst"],
        [data-theme="dark"][data-palette="amethyst"]{
          --brand-900:#160a1d; --foot-ground:#0f0614; --brand-800:#221031; --brand-700:#b585d8; --brand-600:#c69ce4;
          --cream-50:#140d1a; --cream-100:#1d1425; --cream-200:#261c30;
          --ink-900:#f2eaf6; --ink-600:#b6a6c0; --ink-400:#8a7d94; --line:#31243c;
        }
        [data-theme="dark"] [data-palette="forest"],
        [data-theme="dark"][data-palette="forest"]{
          --brand-900:#07160f; --foot-ground:#040e09; --brand-800:#0d2118; --brand-700:#6fbf93; --brand-600:#8bd0aa;
          --cream-50:#0a150f; --cream-100:#101d16; --cream-200:#17261d;
          --ink-900:#e8f3ec; --ink-600:#a3b8ab; --ink-400:#7a8c81; --line:#213026;
        }

        [data-theme="dark"]:root{
          --brand-900:#1c0a0e; --foot-ground:#100407; --brand-800:#2a0d13; --brand-700:#c4566a;
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

        /* Inter carries no Devanagari glyph, so this stack used to hand every
           Hindi sentence straight to system-ui -- Nirmala UI on Windows, Noto on
           Android, Devanagari MT on a Mac. The same paragraph was set in a
           different face on every device, and none of them were chosen. Noto
           Sans Devanagari sits in front of that fallback now. Inter stays first
           because font fallback is per glyph: Latin and digits still come from
           Inter, and only the Devanagari is served by Noto. */
        [lang="hi"] body, [data-applang="hi"]{
          --font-body:"Inter","Noto Sans Devanagari",system-ui,sans-serif;
        }
        .deva{ font-family:var(--font-deva); }

        /* ---- DEVANAGARI DISPLAY HEADINGS --------------------------------
           Rozha One with a brand gradient washed through the letterforms, for
           page and section titles when the site is in Hindi.

           Two things make this safe rather than clever:

           - The transparent fill lives inside @supports. background-clip:text
             is what makes the gradient visible AT ALL; where it is missing,
             -webkit-text-fill-color:transparent on its own does not degrade to
             plain text, it degrades to INVISIBLE text. So the solid colour is
             the base rule and the gradient is the enhancement on top.
           - font-weight is pinned to 400. Rozha One ships one weight, and the
             600/700 our headings ask for would be synthesised -- a fake bold
             smeared across an already high-contrast face.

           .on-dark is the same treatment for a heading standing on the maroon:
           the light gradient's tail is a gold that only reads against cream. */
        .deva-display{
          font-family:var(--font-deva-display);
          font-weight:400;
          letter-spacing:0;
          color:var(--brand-700);
          background-image:linear-gradient(100deg,
            var(--brand-800) 0%, var(--brand-700) 38%, var(--gold-600) 92%);
        }
        .deva-display.on-dark{
          color:var(--on-dark);
          background-image:linear-gradient(100deg,
            var(--on-dark) 0%, var(--gold-100) 46%, var(--gold-300) 100%);
        }
        @supports (background-clip:text) or (-webkit-background-clip:text){
          .deva-display{
            -webkit-background-clip:text; background-clip:text;
            -webkit-text-fill-color:transparent; color:transparent;
          }
        }

        /* Applied by language, not by hand. data-applang sits on <html>, so one
           rule reaches every title on every screen and no heading can be
           forgotten -- which is the whole point of asking for this everywhere
           rather than in the two places it started. The selectors below are the
           page- and section-level titles: the public hero and section heads,
           legal page titles, and the auth screens' headings.

           Deliberately NOT the dashboard and admin panel headers. Those are
           data ("12 tests", "All referrals"), sized as UI at 15-19px, and a
           display gradient on a row counter reads as a mistake. */
        [data-applang="hi"] .pb-h1,
        [data-applang="hi"] .pb-h2,
        [data-applang="hi"] .lg-head h1,
        [data-applang="hi"] .jn-h,
        [data-applang="hi"] .pb-h1 em,
        [data-applang="hi"] .pb-h2 em{
          font-family:var(--font-deva-display);
          font-weight:400;
          letter-spacing:0;
        }
        /* The italic runs are set in a Latin quote face that carries no
           Devanagari, and Rozha One has no italic to slant to. */
        [data-applang="hi"] .pb-h1 em,
        [data-applang="hi"] .pb-h2 em{ font-style:normal; font-size:1em; }

        /* The gradient goes on whatever element actually holds the text.

           For most headings that is the heading itself. NOT for the hero: its
           two lines are child spans carrying the swoosh's clip-path, and a
           clipped child paints in its own context -- the parent's text-clipped
           gradient never reaches it, while the transparent fill inherits into
           it regardless. The headline came out invisible. So the hero's lines
           each carry their own gradient, and the h1 carries none. */
        [data-applang="hi"] .pb-h2,
        [data-applang="hi"] .lg-head h1,
        [data-applang="hi"] .jn-h{
          background-image:linear-gradient(100deg,
            var(--brand-800) 0%, var(--brand-700) 38%, var(--gold-600) 92%);
        }
        [data-applang="hi"] .pb-h1-l1,
        [data-applang="hi"] .pb-h1-l2,
        [data-applang="hi"] .pb-res .pb-h2{
          background-image:linear-gradient(100deg,
            var(--on-dark) 0%, var(--gold-100) 46%, var(--gold-300) 100%);
        }
        @supports (background-clip:text) or (-webkit-background-clip:text){
          [data-applang="hi"] .pb-h2,
          [data-applang="hi"] .lg-head h1,
          [data-applang="hi"] .jn-h,
          [data-applang="hi"] .pb-h1-l1,
          [data-applang="hi"] .pb-h1-l2{
            -webkit-background-clip:text; background-clip:text;
            -webkit-text-fill-color:transparent; color:transparent;
          }
        }

        /* The dashboard, the profile and the result screens take the same face
           and NOT the gradient. Their headings are UI-scale -- 15 to 21px --
           and a wash of maroon-into-gold across sixteen pixels of type stops
           being a treatment and starts being a legibility problem; the gradient
           belongs to the display sizes it was drawn for. The face still carries
           across, which is what makes the two halves of the site look related.
           Weight 400 because Rozha One has no other, and 800 would be faked. */
        [data-applang="hi"] .sd-root h1,
        [data-applang="hi"] .sd-root h2,
        [data-applang="hi"] .sd-root .sec-head h2,
        [data-applang="hi"] .ee-root h1,
        [data-applang="hi"] .ee-root h2{
          font-family:var(--font-deva-display);
          font-weight:400;
          letter-spacing:0;
        }
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
        /* ---- SEGMENTED CHROME (mobile header) ---- */
        /* Visually 34px, but every segment still answers to a 44px finger —
           the ::after below extends the hit area past the drawn edge. Sizing
           the control itself at 44px is what made the row feel stuffed; a
           touch target does not have to be a visible box.

           Squircle rather than a full pill: at this size a 100px radius reads
           as a lozenge and fights the round brand mark next to it.

           Glass, because the header behind it is already translucent — a solid
           cream block sat on top of that looked pasted on. */
        .jn-seg{
          display:inline-flex; align-items:stretch; flex:0 0 auto;
          height:34px; box-sizing:border-box; border-radius:11px; overflow:visible;
          background:color-mix(in srgb,var(--cream-50) 62%,transparent);
          border:1px solid color-mix(in srgb,var(--line) 78%,transparent);
          -webkit-backdrop-filter:blur(10px) saturate(1.5);
          backdrop-filter:blur(10px) saturate(1.5);
          box-shadow:inset 0 1px 0 rgba(255,255,255,.5), 0 1px 3px rgba(70,40,20,.07);
        }
        .jn-seg .jn-seg-btn{ min-height:0; height:100% }
        .jn-seg .jn-seg-btn:first-child{ border-radius:10px 0 0 10px }
        .jn-seg .jn-seg-btn:last-child{ border-radius:0 10px 10px 0 }
        .jn-seg-btn{
          position:relative;
          display:inline-flex; align-items:center; justify-content:center; gap:4px;
          background:none; border:0; cursor:pointer; font:inherit;
          padding:0 9px; color:var(--ink-600);
          transition:background .16s, color .16s;
        }
        /* Hit area only — invisible, and it reaches the 44px floor from a 34px
           control. */
        .jn-seg-btn::after{ content:""; position:absolute; left:0; right:0; top:-5px; bottom:-5px }
        .jn-seg-btn:hover{ background:color-mix(in srgb,var(--gold-300) 26%,transparent); color:var(--brand-700) }
        .jn-seg-btn:active{ background:color-mix(in srgb,var(--gold-300) 38%,transparent) }
        .jn-seg-btn:focus-visible{ outline:2px solid var(--gold-500); outline-offset:-2px }
        .jn-seg-icon{ padding:0 8px }
        .jn-seg-label{ font-size:11.5px; font-weight:800; letter-spacing:.02em; line-height:1 }
        .jn-seg-div{ width:1px; background:color-mix(in srgb,var(--line) 70%,transparent);
          flex:0 0 auto; align-self:stretch }

        .jn-pill-short{ display:none }
        @media (max-width:560px){
          .jn-pill-long{ display:none }
          .jn-pill-short{ display:inline }
        }

        .reveal{ opacity:0; transform:translateY(16px); }
        .reveal.in{ opacity:1; transform:none;
          transition:opacity .62s cubic-bezier(.22,.7,.3,1), transform .62s cubic-bezier(.22,.7,.3,1); }
        .reveal-d1.in{ transition-delay:.07s } .reveal-d2.in{ transition-delay:.14s }
        .reveal-d3.in{ transition-delay:.21s } .reveal-d4.in{ transition-delay:.28s }
        @media (prefers-reduced-motion: reduce){
          .reveal{ opacity:1 !important; transform:none !important; }
          /* Everything decorative stops: the button sheen, the lift on hover,
             the arrow nudge, the drawn chart strokes. Nothing that carries
             meaning depends on any of them. */
          .pb-btn::after{ display:none !important; }
          .pb-btn, .pb-card, .pb-btn svg{ transition:none !important; }
          .pb-btn:hover, .pb-card:hover, .pb-btn:active{ transform:none !important; }
          .pb-nav .link::after{ transition:none !important; }
          .in .ill-line-draw, .in .ill-ring-draw{ animation:none !important;
            stroke-dashoffset:0 !important; }
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
          .pb-head-in, .pb-sec, .pb-foot-bottom {
            padding-left: max(22px, env(safe-area-inset-left));
            padding-right: max(22px, env(safe-area-inset-right));
          }
          /* .pb-foot-in belonged in the list above until it was measured. The
             others each carry their own horizontal padding, so max() only
             ever preserves it. This one has none -- it is a bare grid whose
             two children do the padding -- so max() was not protecting a
             floor, it was inventing 22px that the design never had, on top of
             the 22px its children already apply. On a 375px phone that put
             88px of a 375px screen into margins and squeezed the footer's
             link columns to 122px, which is why "Previous year papers" could
             not fit on one line. Invisible on desktop, where the card is
             capped at 1180px and 22px is a rounding error.

             It still needs the inset itself, for a notched phone held
             sideways -- but as the inset, with no floor under it. */
          .pb-foot-in {
            padding-left: env(safe-area-inset-left);
            padding-right: env(safe-area-inset-right);
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
  intro_sub: { en: "Your complete preparation platform for the civil services.", hi: "सिविल सेवा की तैयारी का आपका पूरा प्लेटफ़ॉर्म।" },
  feat_tests: { en: "Real exam-style mock tests", hi: "असली परीक्षा जैसे मॉक टेस्ट" },
  feat_analytics: { en: "Deep performance analytics", hi: "गहराई से प्रदर्शन विश्लेषण" },
  feat_rank: { en: "Rank, percentile & leaderboard", hi: "रैंक, पर्सेंटाइल और लीडरबोर्ड" },
  feat_material: { en: "Expert study material", hi: "विशेषज्ञों की अध्ययन सामग्री" },
  welcome_back: { en: "Welcome back", hi: "फिर से स्वागत है" },
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
  or: { en: "or", hi: "या" },
  google: { en: "Continue with Google", hi: "Google से जारी रखें" },
  use_phone: { en: "Login with phone OTP", hi: "फ़ोन OTP से लॉगिन करें" },
  use_email: { en: "Back to email login", hi: "ईमेल लॉगिन पर वापस" },
  resend: { en: "Resend code", hi: "कोड पुनः भेजें" },
  admin_console: { en: "Admin console", hi: "एडमिन कंसोल" },
  please_wait: { en: "Please wait…", hi: "कृपया प्रतीक्षा करें…" },
  contact_us: { en: "Contact us", hi: "संपर्क करें" },
  need_help: { en: "Need help?", hi: "मदद चाहिए?" },
  help_sub: { en: "Our team usually replies within a few hours.", hi: "हमारी टीम आमतौर पर कुछ घंटों में जवाब दे देती है।" },
  close: { en: "Close", hi: "बंद करें" },
  // validation / auth messages
  err_email_req: { en: "Please enter your email.", hi: "कृपया अपना ईमेल भरिए।" },
  err_pwd_req: { en: "Please enter your password.", hi: "कृपया अपना पासवर्ड भरिए।" },
  err_name_req: { en: "Please enter your name.", hi: "कृपया अपना नाम भरिए।" },
  err_pwd_short: { en: "Password must be at least 8 characters.", hi: "पासवर्ड कम से कम 8 अक्षरों का होना चाहिए।" },
  err_phone: { en: "Please enter a valid phone number.", hi: "कृपया सही फ़ोन नंबर भरिए।" },
  err_otp: { en: "Please enter a valid code.", hi: "कृपया सही कोड भरिए।" },
  err_bad_login: { en: "Email or password is incorrect.", hi: "ईमेल या पासवर्ड ग़लत है।" },
  err_bad_otp: { en: "The code is invalid or has expired.", hi: "कोड ग़लत है या उसकी मियाद ख़त्म हो गई।" },
  ok_acc_created: { en: "Account created! Please sign in.", hi: "खाता बन गया! कृपया साइन इन करें।" },
  ok_otp_sent: { en: "Code sent to", hi: "कोड भेजा गया" },
  // ----- join / paywall -----
  join_hi: { en: "Hello", hi: "नमस्ते" },
  join_title: { en: "One step left to begin", hi: "शुरू करने के लिए बस एक कदम" },
  join_sub: { en: "Unlock the full test series and start preparing today.", hi: "पूरी टेस्ट सीरीज़ अनलॉक करें और आज ही तैयारी शुरू करें।" },
  plan_name: { en: "Prelims Test Series 2026", hi: "प्रीलिम्स टेस्ट सीरीज़ 2026" },
  plan_tests: { en: "30 full-length mock tests", hi: "30 फ़ुल-लेंथ मॉक टेस्ट" },
  plan_analytics: { en: "Detailed performance analytics", hi: "विस्तृत प्रदर्शन विश्लेषण" },
  plan_solutions: { en: "Solutions & explanations for every question", hi: "हर प्रश्न का हल और व्याख्या" },
  plan_rank: { en: "All-India rank & percentile", hi: "अखिल भारतीय रैंक और पर्सेंटाइल" },
  plan_validity: { en: "Valid till the 2026 exam", hi: "2026 परीक्षा तक मान्य" },
  plan_best: { en: "BEST VALUE", hi: "सबसे फ़ायदेमंद" },
  pay_join: { en: "Pay & Join now", hi: "भुगतान करें और जुड़ें" },
  secure_pay: { en: "Secure payment via Razorpay · UPI, cards, netbanking", hi: "Razorpay से सुरक्षित भुगतान · UPI, कार्ड, नेटबैंकिंग" },
  already_enrolled: { en: "Checking your access…", hi: "आपका एक्सेस जाँच रहे हैं…" },
  pay_failed: { en: "Payment could not be started. Please try again.", hi: "भुगतान शुरू नहीं हो सका। कृपया दोबारा कोशिश कीजिए।" },
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
  err_rate:        { en: "Too many attempts. Please wait a minute and try again.", hi: "बहुत ज़्यादा कोशिशें। एक मिनट रुककर दोबारा कोशिश कीजिए।" },
  err_network:     { en: "Network problem. Check your connection and try again.", hi: "नेटवर्क में दिक़्क़त। कनेक्शन जाँचिए और दोबारा कोशिश कीजिए।" },
  agree_terms:     { en: "By continuing you agree to our Terms and Privacy Policy.", hi: "जारी रखकर आप हमारी शर्तों और गोपनीयता नीति से सहमत होते हैं।" },
  pay_success:     { en: "Payment confirmed. Welcome to JUNOONIAS! 🪔", hi: "भुगतान की पुष्टि हुई। JUNOONIAS में आपका स्वागत है! 🪔" },
  pay_pending:     { en: "Payment received — activating your access. This can take a few seconds.", hi: "भुगतान मिल गया — आपका एक्सेस चालू हो रहा है। कुछ पल लग सकते हैं।" },
  loading:         { en: "Loading…", hi: "लोड हो रहा है…" },
  retry:           { en: "Try again", hi: "दोबारा कोशिश करें" },
  refund_note:     { en: "7-day refund if you're not satisfied.", hi: "संतुष्ट न हों तो 7 दिन में रिफ़ंड।" },
});


/* ---------------------------------------------------------------------------
 * Public storefront + student shell.
 *
 * The language toggle shipped working, but only the login and checkout screens
 * were ever translated — every page a Hindi-medium student actually reads was
 * English, so flipping the switch appeared to do nothing. These are the strings
 * that were missing.
 *
 * Written as a Hindi-medium aspirant reads, not as a dictionary translates:
 * ordinary words where they exist, and the English term in Devanagari where
 * that is genuinely what people say (टेस्ट सीरीज़, रैंक, सिलेबस).
 * ------------------------------------------------------------------------ */
Object.assign(STR, {
  /* --- header / nav --- */
  nav_tests:      { en: "Test Series", hi: "टेस्ट सीरीज़" },
  nav_syllabus:   { en: "Syllabus", hi: "सिलेबस" },
  nav_free:       { en: "Free Resources", hi: "निःशुल्क संसाधन" },
  nav_faq:        { en: "FAQ", hi: "सामान्य प्रश्न" },
  nav_dashboard:  { en: "Dashboard", hi: "डैशबोर्ड" },
  nav_login:      { en: "Log in", hi: "लॉगिन" },
  nav_start:      { en: "Get started", hi: "शुरू करें" },
  nav_colour:     { en: "Colour theme", hi: "रंग थीम" },
  foot_follow:    { en: "Follow us", hi: "हमें फ़ॉलो करें" },
  nav_colour_change: { en: "Change colour theme", hi: "रंग थीम बदलें" },
  back_home:      { en: "Back to home", hi: "होम पर वापस" },
  free_no_login:  { en: "Free · no login needed", hi: "निःशुल्क · लॉगिन ज़रूरी नहीं" },

  /* --- hero --- */
  hero_eyebrow:   { en: "Real pattern. Real competition. Real progress.",
                    hi: "असली पैटर्न। असली मुक़ाबला। असली प्रगति।" },
  hero_lede_a:    { en: "We don\u2019t just hand you papers.", hi: "हम सिर्फ़ पेपर नहीं थमाते।" },
  hero_lede_b1:   { en: "We show you the ", hi: "हम आपको दिखाते हैं " },
  hero_lede_bh:   { en: "real exam", hi: "असली परीक्षा" },
  hero_lede_b2:   { en: " pattern.", hi: " का पैटर्न।" },
  hero_lede_c:    { en: "Find your weak topics, measure your accuracy, and see where you stand against everyone who sat the same paper.",
                    hi: "अपने कमज़ोर टॉपिक पहचानिए, अपनी सटीकता नापिए, और देखिए कि उसी पेपर को देने वाले सबके बीच आप कहाँ हैं।" },
  hero_lede_d:    { en: "Your race starts here.", hi: "आपकी दौड़ यहीं से शुरू होती है।" },
  tick_pattern_s: { en: "As real as it gets.", hi: "जितना असली हो सकता है।" },
  tick_rank_s:    { en: "See where you stand.", hi: "देखिए आप कहाँ हैं।" },
  tick_nologin_s: { en: "Just choose and start.", hi: "बस चुनिए और शुरू कीजिए।" },
  hero_h1_a:      { en: "Lead your prep", hi: "अपनी तैयारी को ले चलिए" },
  hero_h1_b:      { en: "from darkness, unto light.", hi: "अंधकार से प्रकाश की ओर।" },
  hero_lede:      { en: "Papers on the real pattern. Analysis that names your weak topics. And a rank measured against everyone who sat the same paper — not invented.",
                    hi: "असली पैटर्न पर पेपर। ऐसा विश्लेषण जो आपके कमज़ोर टॉपिक का नाम बताए। और रैंक जो उसी पेपर को देने वाले हर अभ्यर्थी के सामने नापी जाती है — गढ़ी नहीं।" },
  cta_explore:    { en: "Explore test series", hi: "टेस्ट सीरीज़ देखें" },
  cta_browse_free:{ en: "Browse free resources", hi: "निःशुल्क संसाधन देखें" },
  tick_pattern:   { en: "Exam-pattern papers", hi: "परीक्षा-पैटर्न पेपर" },
  tick_rank:      { en: "All-India rank & percentile", hi: "अखिल भारतीय रैंक और पर्सेंटाइल" },
  tick_nologin:   { en: "No login needed to browse", hi: "देखने के लिए लॉगिन ज़रूरी नहीं" },

  /* --- claim strip --- */
  strip1_t: { en: "Written to the pattern", hi: "पैटर्न के अनुसार बने" },
  strip1_d: { en: "Same sections, same negative marking", hi: "वही सेक्शन, वही नेगेटिव मार्किंग" },
  strip2_t: { en: "Weakness, named", hi: "कमज़ोरी, नाम के साथ" },
  strip2_d: { en: "Topic-level accuracy after every paper", hi: "हर पेपर के बाद टॉपिक-स्तर की सटीकता" },
  strip3_t: { en: "Pay for one exam", hi: "एक ही परीक्षा का भुगतान" },
  strip3_d: { en: "Bundles never bundle you into extras", hi: "बंडल आपको बेवजह की चीज़ों में नहीं बाँधते" },
  strip4_t: { en: "Look before you buy", hi: "खरीदने से पहले देखिए" },
  strip4_d: { en: "Whole catalogue open, no login wall", hi: "पूरा कैटलॉग खुला, कोई लॉगिन दीवार नहीं" },

  /* --- catalogue --- */
  cat_h2:    { en: "One exam. One price. Nothing extra.", hi: "एक परीक्षा। एक क़ीमत। कुछ भी अतिरिक्त नहीं।" },
  cat_sub:   { en: "Each series stands on its own. You pay for the exam you are actually writing — and buying one never quietly unlocks, or charges for, another.",
               hi: "हर सीरीज़ अपने आप में पूरी है। आप उसी परीक्षा का भुगतान करते हैं जो आप वाकई दे रहे हैं — और एक खरीदने पर दूसरी न चुपचाप खुलती है, न उसका पैसा लगता है।" },
  tab_all:   { en: "All exams", hi: "सभी परीक्षाएँ" },
  cat_empty: { en: "No test series published for this exam yet.", hi: "इस परीक्षा के लिए अभी कोई टेस्ट सीरीज़ नहीं आई है।" },

  /* --- cards --- */
  card_enroll:     { en: "Enroll now", hi: "अभी जुड़ें" },
  card_details:    { en: "Details", hi: "विवरण" },
  card_owned:      { en: "You own this", hi: "यह आपके पास है" },
  card_soon:       { en: "Coming soon", hi: "जल्द आ रहा है" },
  card_papers_soon:{ en: "Papers being finalised", hi: "पेपर तैयार हो रहे हैं" },
  card_mock_one:   { en: "mock test", hi: "मॉक टेस्ट" },
  card_mock_many:  { en: "mock tests", hi: "मॉक टेस्ट" },
  card_free_try:   { en: "free to try", hi: "मुफ़्त आज़माने को" },
  card_months:     { en: "months", hi: "महीने" },
  card_lifetime:   { en: "lifetime", hi: "आजीवन" },
  card_included:   { en: "What's included", hi: "इसमें क्या शामिल है" },
  card_tests_in:   { en: "Tests in this series", hi: "इस सीरीज़ के टेस्ट" },
  card_free_sample:{ en: "Free sample", hi: "मुफ़्त सैंपल" },
  card_goto_dash:  { en: "Go to your dashboard", hi: "अपने डैशबोर्ड पर जाएँ" },

  /* --- how it works --- */
  how_eyebrow: { en: "How it works", hi: "यह कैसे काम करता है" },
  how_h2:      { en: "Sit. Read. Fix. Again.", hi: "दीजिए। पढ़िए। सुधारिए। फिर दीजिए।" },
  how_sub:     { en: "A mock is not the exam — it is the rehearsal. What you do in the hour after it is where the marks actually come from.",
                 hi: "मॉक परीक्षा नहीं है — वह रिहर्सल है। असली अंक उस एक घंटे से आते हैं जो आप उसके बाद लगाते हैं।" },
  step1_t: { en: "Choose without signing up", hi: "बिना साइन-अप चुनिए" },
  step1_d: { en: "Every series, every price, every test list — open. Make the decision first, create the account after.",
             hi: "हर सीरीज़, हर क़ीमत, हर टेस्ट सूची — खुली हुई। पहले फ़ैसला कीजिए, खाता बाद में बनाइए।" },
  step2_t: { en: "Write it like the real thing", hi: "असली की तरह दीजिए" },
  step2_d: { en: "Same sections, same clock, same negative marking. A mock that is easier than the exam teaches you nothing.",
             hi: "वही सेक्शन, वही घड़ी, वही नेगेटिव मार्किंग। परीक्षा से आसान मॉक कुछ नहीं सिखाता।" },
  step3_t: { en: "Find out what went wrong", hi: "जानिए कहाँ चूक हुई" },
  step3_d: { en: "Which topics leaked marks, which questions ate your clock, and what to open tonight.",
             hi: "किन टॉपिक में अंक गए, किन सवालों ने घड़ी खा ली, और आज रात कौन-सी किताब खोलनी है।" },

  /* --- report showcase --- */
  rep_eyebrow: { en: "After every test", hi: "हर टेस्ट के बाद" },
  rep_h2:      { en: "A diagnosis, not a scoreboard", hi: "निदान, न कि स्कोरबोर्ड" },
  rep_sub:     { en: "Any site can hand you a number. The useful part is knowing which twenty minutes of tonight's revision will earn the most marks next time.",
                 hi: "नंबर तो कोई भी साइट दे देगी। काम की बात यह जानना है कि आज रात की बीस मिनट की रिवीज़न कहाँ लगाई जाए ताकि अगली बार सबसे ज़्यादा अंक मिलें।" },
  rep1_t: { en: "Topic-level accuracy", hi: "टॉपिक-स्तर की सटीकता" },
  rep1_d: { en: "Polity strong, Economy weak — graded from your attempts, not a guess.",
            hi: "पॉलिटी मज़बूत, इकोनॉमी कमज़ोर — आपके ही प्रयासों से निकाला गया, अंदाज़े से नहीं।" },
  rep2_t: { en: "Time per question", hi: "प्रति प्रश्न समय" },
  rep2_d: { en: "The four questions that quietly cost you the last section, named.",
            hi: "वे चार सवाल जिन्होंने चुपचाप आपका आख़िरी सेक्शन छीन लिया — नाम के साथ।" },
  rep3_t: { en: "Section-wise split", hi: "सेक्शन-वार ब्योरा" },
  rep3_d: { en: "Where the marks came from — and exactly where they drained out.",
            hi: "अंक कहाँ से आए — और ठीक कहाँ बह गए।" },
  rep4_t: { en: "Full solutions", hi: "पूरे हल" },
  rep4_d: { en: "Every answer reasoned out, including why the tempting wrong option is wrong.",
            hi: "हर उत्तर तर्क सहित — यह भी कि लुभाने वाला ग़लत विकल्प ग़लत क्यों है।" },

  /* --- free resources band --- */
  res_eyebrow: { en: "No login needed", hi: "लॉगिन ज़रूरी नहीं" },
  res_h2:      { en: "Take what's free first", hi: "पहले वह लीजिए जो मुफ़्त है" },
  res_sub:     { en: "Syllabus, past papers, NCERTs, daily current affairs — all of it open, no account, no email. Judge us on this before you judge us on the price.",
                 hi: "सिलेबस, पिछले पेपर, NCERT, रोज़ के करेंट अफेयर्स — सब खुला, न खाता, न ईमेल। क़ीमत पर राय बनाने से पहले इस पर बनाइए।" },
  res_published:   { en: "published across", hi: "प्रकाशित, कुल" },
  res_series_word: { en: "series", hi: "सीरीज़ में" },
  res_free_try:    { en: "free to try without paying", hi: "बिना भुगतान आज़माने को मुफ़्त" },

  /* --- coupon ticket --- */
  coupon_h4:  { en: "Have a coupon code?", hi: "कूपन कोड है?" },
  coupon_p:   { en: "Enter it on the payment screen. The reduced price appears before you pay — never a surprise afterwards.",
                hi: "भुगतान वाली स्क्रीन पर डालिए। घटी हुई क़ीमत भुगतान से पहले दिखती है — बाद में कोई चौंकाने वाली बात नहीं।" },
  /* The short line the phone shows in place of the one above — the strip is a
     thin band there and has room for a clause, not a sentence. */
  coupon_p_s: { en: "Use it at payment.", hi: "भुगतान के समय लगाइए।" },
  coupon_cta: { en: "See test series", hi: "टेस्ट सीरीज़ देखें" },

  /* --- refer & earn ticket, alongside the coupon one ---
     Every claim here is one the code actually keeps: the bonus is the ₹99 in
     app_settings.referral_bonus_paise, it is credited only once the invited
     friend's payment goes through, it lands in the wallet rather than in hand,
     and nothing anywhere limits how many people you invite. */
  refer_h4:   { en: "Refer a friend, get ₹99", hi: "साथी को बुलाइए, ₹99 पाइए" },
  refer_p:    { en: "Share your invite link. Every friend who buys a test series puts ₹99 cashback in your wallet — and there is no cap on how many you invite.",
                hi: "अपना इनवाइट लिंक भेजिए। जो भी साथी टेस्ट सीरीज़ खरीदे, ₹99 कैशबैक आपके वॉलेट में — और कितने लोगों को बुलाएँ, इसकी कोई सीमा नहीं।" },
  /* The title already carries the number, so the phone's second line spends
     itself on the condition instead of repeating it. */
  refer_p_s:  { en: "When a friend buys.", hi: "जब कोई साथी ख़रीदे।" },
  refer_cta:  { en: "Start earning", hi: "कमाना शुरू करें" },

  /* --- footer --- */
  foot_blurb:   { en: "UPSC, BPSC and UPPCS \u2014 papers on the real pattern, honest analysis, and an All-India rank. In Hindi and English, both.",
                  hi: "UPSC, BPSC और UPPCS — असली पैटर्न पर पेपर, ईमानदार विश्लेषण और अखिल भारतीय रैंक। हिन्दी और अंग्रेज़ी, दोनों में।" },
  foot_explore: { en: "Explore", hi: "एक्सप्लोर" },
  foot_free:    { en: "Free resources", hi: "निःशुल्क संसाधन" },
  foot_support: { en: "Support", hi: "सहायता" },
  foot_pyq:     { en: "PYQ papers", hi: "PYQ पेपर" },
  foot_mydash:  { en: "My dashboard", hi: "मेरा डैशबोर्ड" },
  foot_material:{ en: "Study material", hi: "अध्ययन सामग्री" },
  foot_ncert:   { en: "NCERT books", hi: "NCERT किताबें" },
  foot_news:    { en: "Daily current affairs", hi: "रोज़ाना करेंट अफेयर्स" },
  foot_help:    { en: "Help & refunds", hi: "सहायता और रिफ़ंड" },
  foot_refunds: { en: "Refunds & access", hi: "रिफ़ंड और एक्सेस" },
  foot_rights:  { en: "All rights reserved.", hi: "सर्वाधिकार सुरक्षित।" },
  foot_made:    { en: "Made for aspirants, in India.", hi: "अभ्यर्थियों के लिए, भारत में बना।" },
});


/* Free-resources hub: card labels and the standalone page headers. */
Object.assign(STR, {
  res_syllabus_l:  { en: "Syllabus", hi: "सिलेबस" },
  res_syllabus_b:  { en: "Full UPSC / BPSC / UPPCS syllabus, topic by topic.", hi: "UPSC / BPSC / UPPCS का पूरा सिलेबस, टॉपिक दर टॉपिक।" },
  res_pyq_l:       { en: "Previous Year Papers", hi: "पिछले वर्षों के पेपर" },
  res_pyq_b:       { en: "Solved papers going back several attempts.", hi: "कई वर्षों के हल किए हुए पेपर।" },
  res_materials_l: { en: "Free Materials", hi: "निःशुल्क सामग्री" },
  res_materials_b: { en: "Notes and PDFs, free to download.", hi: "नोट्स और PDF, मुफ़्त डाउनलोड।" },
  res_ncert_l:     { en: "NCERT Books", hi: "NCERT किताबें" },
  res_ncert_b:     { en: "Class 6–12 NCERTs, organised by subject.", hi: "कक्षा 6–12 की NCERT, विषय के अनुसार।" },
  res_news_l:      { en: "Daily Current Affairs", hi: "रोज़ाना करेंट अफेयर्स" },
  res_news_b:      { en: "Today's news, filtered for what's exam-relevant.", hi: "आज की ख़बरें, परीक्षा के लिहाज़ से छाँटी हुई।" },
  res_faq_l:       { en: "FAQ", hi: "सामान्य प्रश्न" },
  res_faq_b:       { en: "Tests, payments, access and refunds.", hi: "टेस्ट, भुगतान, एक्सेस और रिफ़ंड।" },

  rt_syllabus_t:  { en: "Syllabus", hi: "सिलेबस" },
  rt_syllabus_s:  { en: "What each exam actually asks of you", hi: "हर परीक्षा असल में आपसे क्या माँगती है" },
  rt_pyq_t:       { en: "Previous Year Papers", hi: "पिछले वर्षों के पेपर" },
  rt_pyq_s:       { en: "The best predictor of what comes next", hi: "आगे क्या आएगा, इसका सबसे भरोसेमंद संकेत" },
  rt_materials_t: { en: "Free Study Material", hi: "निःशुल्क अध्ययन सामग्री" },
  rt_materials_s: { en: "Open to everyone, no account needed", hi: "सबके लिए खुली, खाता ज़रूरी नहीं" },
  rt_ncert_t:     { en: "NCERT Books", hi: "NCERT किताबें" },
  rt_ncert_s:     { en: "The foundation every serious aspirant starts from", hi: "हर गंभीर अभ्यर्थी की शुरुआत यहीं से होती है" },
  rt_news_t:      { en: "Daily Current Affairs", hi: "रोज़ाना करेंट अफेयर्स" },
  rt_news_s:      { en: "Filtered for what the exam actually asks", hi: "परीक्षा जो पूछती है, उसी के हिसाब से छाँटी हुई" },
  rt_faq_t:       { en: "Frequently Asked Questions", hi: "अक्सर पूछे जाने वाले प्रश्न" },
  rt_faq_s:       { en: "Tests, payments, access and refunds", hi: "टेस्ट, भुगतान, एक्सेस और रिफ़ंड" },

  shloka_src:     { en: "Br\u0325hada\u0304ran\u0323yaka Upanis\u0323ad \u00b7 1.3.28", hi: "बृहदारण्यक उपनिषद् · १.३.२८" },
});


/* ---------------------------------------------------------------------------
 * The exam hall and the report that follows it.
 *
 * This is the screen a paying student is inside for two hours, under time
 * pressure. If any of it is in a language they do not read, that is not a
 * cosmetic problem — it is the difference between attempting a question and
 * skipping it.
 * ------------------------------------------------------------------------ */
Object.assign(STR, {
  /* --- instructions --- */
  ex_online:      { en: "Online Examination", hi: "ऑनलाइन परीक्षा" },
  ex_duration:    { en: "Duration:", hi: "अवधि:" },
  ex_questions:   { en: "Questions:", hi: "प्रश्न:" },
  ex_maxmarks:    { en: "Max Marks:", hi: "अधिकतम अंक:" },
  ex_sections:    { en: "Sections:", hi: "सेक्शन:" },
  ex_min:         { en: "min", hi: "मिनट" },
  ex_gen_inst:    { en: "General Instructions", hi: "सामान्य निर्देश" },
  ex_i1a:         { en: "The countdown timer at the top right shows the time remaining. When it reaches zero, the test is ", hi: "ऊपर दाईं ओर का टाइमर शेष समय दिखाता है। शून्य होते ही टेस्ट " },
  ex_i1b:         { en: "submitted automatically", hi: "अपने आप जमा हो जाता है" },
  ex_i2a:         { en: "The timer turns ", hi: "टाइमर " },
  ex_i2b:         { en: "red in the last 60 seconds", hi: "आख़िरी 60 सेकंड में लाल" },
  ex_i2c:         { en: " as a final warning.", hi: " हो जाता है — यह आख़िरी चेतावनी है।" },
  ex_i3:          { en: "The question palette on the right shows the status of every question using the colour codes below.", hi: "दाईं ओर का प्रश्न पैलेट नीचे दिए रंगों से हर प्रश्न की स्थिति दिखाता है।" },
  ex_i4:          { en: "You may move between sections and questions freely using the palette or the navigation buttons.", hi: "आप पैलेट या नेविगेशन बटन से सेक्शन और प्रश्नों के बीच स्वतंत्र रूप से आ-जा सकते हैं।" },
  ex_i5a:         { en: "Use ", hi: "उत्तर सहेजने के लिए " },
  ex_i5b:         { en: " to save your answer, ", hi: " दबाइए, प्रश्न पर निशान लगाने के लिए " },
  ex_i5c:         { en: " to flag a question, and ", hi: ", और अपना चयन हटाने के लिए " },
  ex_i5d:         { en: " to remove your selection.", hi: " दबाइए।" },
  ex_i6:          { en: "Question and option order is randomised per candidate to maintain exam integrity.", hi: "परीक्षा की निष्पक्षता बनाए रखने के लिए हर अभ्यर्थी के लिए प्रश्नों और विकल्पों का क्रम बदला जाता है।" },
  ex_marking:     { en: "Marking Scheme", hi: "अंकन योजना" },
  ex_for_correct: { en: "for each correct answer", hi: "प्रत्येक सही उत्तर के लिए" },
  ex_for_wrong:   { en: "for each wrong answer", hi: "प्रत्येक ग़लत उत्तर के लिए" },
  ex_no_negative: { en: "no negative marking", hi: "कोई नेगेटिव मार्किंग नहीं" },
  ex_multi_t:     { en: "Multiple-correct questions:", hi: "बहु-सही प्रश्न:" },
  ex_multi_d:     { en: "full marks only if every correct option — and no incorrect one — is selected.", hi: "पूरे अंक तभी जब हर सही विकल्प चुना गया हो और कोई ग़लत विकल्प न चुना गया हो।" },
  ex_legend:      { en: "Question Palette Legend", hi: "प्रश्न पैलेट संकेत" },
  ex_answered:    { en: "Answered", hi: "उत्तर दिया" },
  ex_notanswered: { en: "Not Answered", hi: "उत्तर नहीं दिया" },
  ex_notvisited:  { en: "Not Visited", hi: "देखा नहीं" },
  ex_marked:      { en: "Marked for Review", hi: "समीक्षा के लिए चिह्नित" },
  ex_ansmarked:   { en: "Answered & Marked", hi: "उत्तर दिया और चिह्नित" },
  ex_consent:     { en: "I have read and understood all the instructions. I declare that I am not in possession of any prohibited material and I agree to abide by the examination rules.", hi: "मैंने सभी निर्देश पढ़ और समझ लिए हैं। मैं घोषणा करता/करती हूँ कि मेरे पास कोई प्रतिबंधित सामग्री नहीं है और मैं परीक्षा के नियमों का पालन करूँगा/करूँगी।" },
  ex_begin:       { en: "I am ready to begin", hi: "मैं शुरू करने के लिए तैयार हूँ" },
  ex_dashboard:   { en: "Dashboard", hi: "डैशबोर्ड" },

  /* --- in the exam --- */
  ex_save_next:   { en: "Save & Next", hi: "सहेजें और आगे" },
  ex_mark_next:   { en: "Mark for Review & Next", hi: "चिह्नित करें और आगे" },
  ex_clear:       { en: "Clear Response", hi: "उत्तर हटाएँ" },
  ex_previous:    { en: "Previous", hi: "पिछला" },
  ex_enter_ans:   { en: "Enter your answer", hi: "अपना उत्तर लिखिए" },
  ex_type_number: { en: "Type a number…", hi: "एक संख्या लिखिए…" },
  ex_submit_test: { en: "Submit Test", hi: "टेस्ट जमा करें" },
  ex_submit_q:    { en: "Submit your test?", hi: "टेस्ट जमा करें?" },
  ex_resume:      { en: "Resume Test", hi: "टेस्ट जारी रखें" },
  ex_submit_now:  { en: "Submit Now", hi: "अभी जमा करें" },
  ex_submit_warn: { en: "Once submitted, you cannot change your answers. Please review the summary below.", hi: "जमा करने के बाद आप उत्तर नहीं बदल सकते। कृपया नीचे का सारांश देख लीजिए।" },
  ex_preparing:   { en: "Preparing your question paper…", hi: "आपका प्रश्नपत्र तैयार हो रहा है…" },
  ex_scoring:     { en: "Scoring your paper…", hi: "आपका पेपर जाँचा जा रहा है…" },
  ex_scoring_sub: { en: "Your answers are being checked on our servers.", hi: "आपके उत्तर हमारे सर्वर पर जाँचे जा रहे हैं।" },
  ex_sub_failed:  { en: "Submission failed", hi: "जमा नहीं हो सका" },
  ex_answers_safe:{ en: "Your answers are safe — nothing has been lost.", hi: "आपके उत्तर सुरक्षित हैं — कुछ भी नहीं गया।" },
  ex_try_again:   { en: "Try again", hi: "दोबारा कोशिश करें" },
  ex_back_paper:  { en: "Back to paper", hi: "पेपर पर वापस" },
  ex_in_progress: { en: "Attempt in progress", hi: "प्रयास जारी है" },
  ex_time_left:   { en: "Time Left", hi: "शेष समय" },
  ex_question_n:  { en: "Question", hi: "प्रश्न" },
  ex_single:      { en: "Single Correct", hi: "एक सही विकल्प" },
  ex_multiple:    { en: "Multiple Correct", hi: "एक से अधिक सही" },
  ex_numerical:   { en: "Numerical", hi: "संख्यात्मक" },
  ex_ansmarked_l: { en: "Answered & Marked for Review", hi: "उत्तर दिया और समीक्षा हेतु चिह्नित" },
  ex_candidate:   { en: "Candidate", hi: "अभ्यर्थी" },
  ex_candidate_id:{ en: "Candidate ID", hi: "अभ्यर्थी क्रमांक" },

  /* --- report --- */
  ex_report:      { en: "Performance Report", hi: "प्रदर्शन रिपोर्ट" },
  ex_correct:     { en: "Correct", hi: "सही" },
  ex_wrong:       { en: "Wrong", hi: "ग़लत" },
  ex_skipped:     { en: "Skipped", hi: "छोड़े गए" },
  ex_accuracy:    { en: "Accuracy", hi: "सटीकता" },
  ex_all:         { en: "All", hi: "सभी" },
  ex_benchmark:   { en: "Benchmark", hi: "तुलना" },
  ex_breakdown:   { en: "Breakdown", hi: "ब्योरा" },
  ex_diagnosis:   { en: "Diagnosis", hi: "निदान" },
  ex_deep_review: { en: "Deep Review", hi: "विस्तृत समीक्षा" },
  ex_action_plan: { en: "Action Plan", hi: "कार्य योजना" },
  ex_sec_perf:    { en: "Section-wise Performance", hi: "सेक्शन-वार प्रदर्शन" },
  ex_sec_sub:     { en: "Score in each section as a share of its maximum.", hi: "हर सेक्शन में अधिकतम के मुक़ाबले आपका स्कोर।" },
  ex_topic_sub:   { en: "Each topic graded by your accuracy.", hi: "हर टॉपिक आपकी सटीकता के आधार पर।" },
  ex_coverage:    { en: "Accuracy across every topic tested.", hi: "जितने टॉपिक पूछे गए, सबमें सटीकता।" },
  ex_qbyq:        { en: "Question-by-Question Analysis", hi: "प्रश्न-दर-प्रश्न विश्लेषण" },
  ex_qbyq_sub:    { en: "Your answer, the correct answer, marks awarded, time spent, and a full explanation for every question.", hi: "हर प्रश्न पर आपका उत्तर, सही उत्तर, मिले अंक, लगा समय और पूरी व्याख्या।" },
  ex_correct_ans: { en: "Correct answer", hi: "सही उत्तर" },
  ex_your_answer: { en: "Your answer", hi: "आपका उत्तर" },
  ex_explanation: { en: "Explanation:", hi: "व्याख्या:" },
  ex_back_dash:   { en: "Back to dashboard", hi: "डैशबोर्ड पर वापस" },
  ex_come_back:   { en: "Come back after others attempt it to see where you stand.", hi: "दूसरों के प्रयास के बाद लौटिए, तब पता चलेगा आप कहाँ खड़े हैं।" },
  ex_slow_note:   { en: "Bars in red took noticeably longer than your average — target these for speed.", hi: "लाल पट्टियों में आपने औसत से काफ़ी ज़्यादा समय लिया — गति के लिए इन्हीं पर काम कीजिए।" },
  ex_prio:        { en: "Priority — Weak areas to fix first", hi: "प्राथमिकता — पहले ये कमज़ोरियाँ सुधारिए" },
  ex_strengthen:  { en: "Strengthen — Almost there", hi: "मज़बूत कीजिए — बस थोड़ा और" },
  ex_keepitup:    { en: "Keep it up — Your strengths", hi: "बनाए रखिए — आपकी मज़बूती" },
  ex_speed:       { en: "Speed — Manage your time better", hi: "गति — समय बेहतर सँभालिए" },
  ex_cov_head:    { en: "Coverage — Don't leave marks on the table", hi: "कवरेज — अंक छोड़कर मत आइए" },
});


/* ---------------------------------------------------------------------------
 * Student dashboard: navigation, page headers and the labels that repeat on
 * every screen. This is the shell a paying student moves through daily.
 * ------------------------------------------------------------------------ */
Object.assign(STR, {
  sd_home:        { en: "Home", hi: "होम" },
  sd_home_s:      { en: "Your preparation command centre", hi: "आपकी पूरी तैयारी, एक जगह" },
  sd_tests:       { en: "Test Series", hi: "टेस्ट सीरीज़" },
  sd_tests_s:     { en: "Attempt mocks and review past tests", hi: "मॉक दीजिए और पुराने टेस्ट देखिए" },
  sd_perf:        { en: "My Performance", hi: "मेरा प्रदर्शन" },
  sd_perf_s:      { en: "Deep analytics across every attempt", hi: "हर प्रयास का गहरा विश्लेषण" },
  sd_batches:     { en: "My Batches", hi: "मेरे बैच" },
  sd_batches_s:   { en: "Courses you're enrolled in", hi: "जिन कोर्स में आपका नामांकन है" },
  sd_materials:   { en: "Study Material", hi: "अध्ययन सामग्री" },
  sd_materials_s: { en: "PDFs, notes and videos", hi: "PDF, नोट्स और वीडियो" },
  sd_leaderboard: { en: "Leaderboard", hi: "लीडरबोर्ड" },
  sd_leaderboard_s:{ en: "See where you rank", hi: "देखिए आपकी रैंक कहाँ है" },
  sd_refer:       { en: "Refer & Earn", hi: "रेफ़र करें, कमाएँ" },
  sd_refer_s:     { en: "Invite friends and earn rewards", hi: "दोस्तों को बुलाइए और इनाम पाइए" },
  sd_profile:     { en: "Profile", hi: "प्रोफ़ाइल" },
  sd_profile_s:   { en: "Your account and achievements", hi: "आपका खाता और उपलब्धियाँ" },

  /* repeated labels */
  sd_notifications:{ en: "Notifications", hi: "सूचनाएँ" },
  sd_nothing_new: { en: "Nothing new right now.", hi: "अभी कुछ नया नहीं है।" },
  sd_logout:      { en: "Log out", hi: "लॉग आउट" },
  sd_view_all:    { en: "View all", hi: "सभी देखें" },
  sd_close:       { en: "Close", hi: "बंद करें" },
  sd_free:        { en: "Free", hi: "निःशुल्क" },
  sd_rank:        { en: "Rank", hi: "रैंक" },
  sd_accuracy:    { en: "Accuracy", hi: "सटीकता" },
  sd_browse_tests:{ en: "Browse tests", hi: "टेस्ट देखें" },
  sd_full_analytics:{ en: "Full analytics", hi: "पूरा विश्लेषण" },
  sd_last_attempt:{ en: "Last attempt", hi: "पिछला प्रयास" },
  sd_available:   { en: "Available tests", hi: "उपलब्ध टेस्ट" },
  sd_all_series:  { en: "All test series", hi: "सभी टेस्ट सीरीज़" },
  sd_achievements:{ en: "Achievements", hi: "उपलब्धियाँ" },
  sd_milestones:  { en: "Milestones", hi: "पड़ाव" },
  sd_active_enrol:{ en: "Active enrollment", hi: "सक्रिय नामांकन" },
  sd_expired:     { en: "Expired", hi: "समाप्त" },
  sd_full_name:   { en: "Full name", hi: "पूरा नाम" },
  sd_email:       { en: "Email", hi: "ईमेल" },
  sd_city:        { en: "City", hi: "शहर" },

  /* --- profile view ---
     The whole panel was hardcoded English, so a Hindi profile showed a Hindi
     sidebar wrapped around an English form. */
  sd_pf_settings:  { en: "Settings", hi: "सेटिंग्स" },
  sd_pf_details:   { en: "Your details", hi: "आपका विवरण" },
  sd_pf_name:      { en: "Full name", hi: "पूरा नाम" },
  sd_pf_target:    { en: "Target exam", hi: "लक्ष्य परीक्षा" },
  sd_pf_tdate:     { en: "Target exam date", hi: "परीक्षा की तारीख़" },
  sd_pf_city:      { en: "City", hi: "शहर" },
  sd_pf_email:     { en: "Email", hi: "ईमेल" },
  sd_pf_emailnote: { en: "Your sign-in email can't be changed here — contact support if you need it updated.",
                     hi: "साइन-इन ईमेल यहाँ से नहीं बदला जा सकता — बदलवाना हो तो सहायता से संपर्क कीजिए।" },
  sd_pf_save:      { en: "Save changes", hi: "बदलाव सहेजें" },
  sd_pf_saving:    { en: "Saving…", hi: "सहेजा जा रहा है…" },
  sd_pf_saved:     { en: "Profile updated", hi: "प्रोफ़ाइल अपडेट हो गई" },
  sd_pf_needname:  { en: "Please enter your name", hi: "कृपया अपना नाम भरिए" },
  sd_pf_savefail:  { en: "Couldn't save — check your connection and try again",
                     hi: "सहेजा नहीं जा सका — कनेक्शन जाँचिए और दोबारा कोशिश कीजिए" },
  sd_pf_notif:     { en: "Notifications", hi: "सूचनाएँ" },
  /* "याददहानी" is the correct spelling of the Urdu word, and it was misspelt
     here as "याद-दिहानी" -- but even spelt right it is a formal word nobody
     uses in an app. Aspirants say रिमाइंडर. */
  sd_pf_reminders: { en: "Reminders & alerts", hi: "रिमाइंडर और अलर्ट" },
  sd_pf_n_email:   { en: "Test reminders & results", hi: "टेस्ट के रिमाइंडर और नतीजे" },
  sd_pf_n_sms:     { en: "Important updates only", hi: "सिर्फ़ ज़रूरी सूचनाएँ" },
  sd_pf_n_wa:      { en: "Daily practice nudges", hi: "रोज़ अभ्यास के रिमाइंडर" },
  sd_pf_photo:     { en: "Change photo", hi: "फ़ोटो बदलिए" },
  sd_pf_photoup:   { en: "Uploading photo…", hi: "फ़ोटो चढ़ाई जा रही है…" },
  sd_pf_photodone: { en: "Profile photo updated", hi: "प्रोफ़ाइल फ़ोटो बदल गई" },
  sd_pf_photorm:   { en: "Remove photo", hi: "फ़ोटो हटाइए" },
  sd_pf_photormd:  { en: "Photo removed", hi: "फ़ोटो हट गई" },
  sd_pf_photofail: { en: "That image couldn't be uploaded", hi: "यह तस्वीर अपलोड नहीं हो सकी" },
  /* A pattern, not two halves glued in a fixed order: English puts the date
     last ("Member since 6 Feb") and Hindi puts it first ("6 फ़र॰ से सदस्य"). */
  sd_pf_member:    { en: "Member since {d}", hi: "{d} से सदस्य" },
  sd_pf_badges:    { en: "badges", hi: "बैज" },
  sd_pf_streak:    { en: "day streak", hi: "दिन लगातार" },
  sd_pf_bestrank:  { en: "Best rank", hi: "सर्वश्रेष्ठ रैंक" },

  /* --- profile: milestones ---
     These were hardcoded English and stayed English in Hindi, which is what
     left "Century Rank" and "Quarter Century" sitting untranslated on the
     profile. The cricket metaphors do not carry into Hindi as loanwords, so
     they are rewritten to say the same thing in Hindi rather than transliterated. */
  sd_ach_h:        { en: "Achievements", hi: "उपलब्धियाँ" },
  sd_ach_eyebrow:  { en: "Milestones", hi: "पड़ाव" },
  /* One pattern, not three pieces concatenated. English counts up from the
     earned number ("2 of 10 unlocked"); Hindi puts the total first, so gluing
     the words in English order produced "2 में से 10 हासिल" -- which reads as
     ten out of two. */
  sd_ach_count:    { en: "{a} of {b} unlocked", hi: "{b} में से {a} हासिल" },

  ach_first_t:  { en: "First Step", hi: "पहला क़दम" },
  ach_first_d:  { en: "Completed your first test", hi: "आपका पहला टेस्ट पूरा हुआ" },
  ach_ten_t:    { en: "Mock Marathoner", hi: "लगातार अभ्यास" },
  ach_ten_d:    { en: "Completed 10 tests", hi: "10 टेस्ट पूरे किए" },
  ach_score_t:  { en: "Strong Scorer", hi: "मज़बूत स्कोर" },
  ach_score_d:  { en: "Scored 70%+ in a test", hi: "किसी टेस्ट में 70%+ अंक" },
  ach_fire_t:   { en: "On Fire", hi: "जोश बरक़रार" },
  ach_fire_d:   { en: "7-day study streak", hi: "7 दिन लगातार पढ़ाई" },
  ach_pct_t:    { en: "Top Percentile", hi: "शीर्ष पर्सेंटाइल" },
  ach_pct_d:    { en: "Crossed the 80th percentile", hi: "80वें पर्सेंटाइल के पार" },
  ach_rank_t:   { en: "Century Rank", hi: "शतक रैंक" },
  ach_rank_d:   { en: "Ranked inside the top 100", hi: "टॉप 100 में जगह बनाई" },
  ach_acc_t:    { en: "Sniper", hi: "अचूक निशाना" },
  ach_acc_d:    { en: "90%+ accuracy in a test", hi: "किसी टेस्ट में 90%+ सटीकता" },
  ach_25_t:     { en: "Quarter Century", hi: "पच्चीस का पड़ाव" },
  ach_25_d:     { en: "Complete 25 tests", hi: "25 टेस्ट पूरे किए" },
  ach_top10_t:  { en: "Elite Ten", hi: "शीर्ष दस" },
  ach_top10_d:  { en: "Rank inside the top 10", hi: "टॉप 10 में रैंक" },
  ach_un_t:     { en: "Unstoppable", hi: "अजेय" },
  ach_un_d:     { en: "30-day study streak", hi: "30 दिन लगातार पढ़ाई" },

  /* refer & earn view */
  sd_ref_invite:  { en: "Invite friends, earn", hi: "दोस्तों को बुलाइए, कमाइए" },
  sd_ref_lede:    { en: "Share your link with someone preparing for the same exam. The moment they buy any test series, the bonus lands in your wallet. There is no limit on how many you invite.",
                    hi: "अपना लिंक उसी परीक्षा की तैयारी करने वाले किसी साथी को भेजिए। जैसे ही वे कोई टेस्ट सीरीज़ खरीदते हैं, बोनस आपके वॉलेट में आ जाता है। कितने लोगों को बुलाएँ, इसकी कोई सीमा नहीं।" },
  sd_ref_fine:    { en: "A balance and one currently active course are required to withdraw. The bonus is credited only when your friend actually pays — self-referrals and duplicate accounts do not count, and the bonus is taken back if the payment is refunded.",
                    hi: "निकासी के लिए ज़रूरी बैलेंस और एक चालू कोर्स होना आवश्यक है। बोनस तभी मिलता है जब आपका साथी वाकई भुगतान करे — सेल्फ़-रेफ़रल और डुप्लिकेट खाते नहीं गिने जाते, और भुगतान वापस होने पर बोनस भी वापस ले लिया जाता है।" },
  sd_ref_copy:    { en: "Copy", hi: "कॉपी" },
  sd_ref_share:   { en: "Share", hi: "शेयर" },
  sd_ref_copied:  { en: "Invite link copied", hi: "इनवाइट लिंक कॉपी हो गया" },
  sd_ref_joined:  { en: "Friends joined", hi: "जुड़े हुए साथी" },
  sd_ref_joined_s:{ en: "Signed up on your link", hi: "आपके लिंक से साइन अप किया" },
  sd_ref_bought:  { en: "Bought a series", hi: "सीरीज़ खरीदी" },
  sd_ref_bought_s:{ en: "These are the ones that pay", hi: "इन्हीं पर बोनस मिलता है" },
  sd_ref_lifetime:{ en: "Lifetime earned", hi: "कुल कमाई" },
  sd_ref_lifetime_s:{ en: "Before any withdrawals", hi: "निकासी से पहले" },
  sd_ref_s1_t:    { en: "Send your link", hi: "अपना लिंक भेजिए" },
  sd_ref_s1_d:    { en: "WhatsApp it to a study group or a friend sitting the same exam.", hi: "किसी स्टडी ग्रुप या उसी परीक्षा के साथी को WhatsApp कीजिए।" },
  sd_ref_s2_t:    { en: "They join", hi: "वे जुड़ते हैं" },
  sd_ref_s2_d:    { en: "The link tags their account automatically — they never type a code.", hi: "लिंक उनका खाता अपने आप जोड़ देता है — उन्हें कोई कोड नहीं लिखना पड़ता।" },
  sd_ref_s3_t:    { en: "You earn", hi: "आप कमाते हैं" },
  sd_ref_s3_d:    { en: "The bonus lands in your wallet the moment they buy.", hi: "जैसे ही वे खरीदते हैं, बोनस आपके वॉलेट में आ जाता है।" },
  sd_ref_people:  { en: "People you invited", hi: "जिन्हें आपने बुलाया" },
  sd_ref_masked:  { en: "Names are shortened — we don't share your friends' contact details.", hi: "नाम छोटे कर दिए गए हैं — हम आपके साथियों की संपर्क जानकारी साझा नहीं करते।" },
  sd_ref_none:    { en: "No one has joined on your link yet. Share it and they'll show up here.", hi: "अभी आपके लिंक से कोई नहीं जुड़ा। लिंक भेजिए, वे यहाँ दिखेंगे।" },
  sd_ref_browsing:{ en: "Browsing", hi: "देख रहे हैं" },
  sd_wallet_bal:  { en: "Wallet balance", hi: "वॉलेट बैलेंस" },
  sd_wallet_unlock:{ en: "Withdrawal unlocks at", hi: "निकासी तब खुलेगी जब" },
  sd_wallet_hist: { en: "Wallet history", hi: "वॉलेट इतिहास" },
  sd_wallet_hist_s:{ en: "Every credit and debit, including anything reversed", hi: "हर जमा और निकासी, वापस लिए गए सहित" },
  sd_wallet_payouts:{ en: "Payouts open shortly. Your balance keeps growing either way — earning is never blocked.", hi: "भुगतान जल्द शुरू होंगे। आपका बैलेंस बढ़ता रहेगा — कमाई कभी नहीं रुकती।" },
  sd_wallet_bonus:{ en: "Referral bonus", hi: "रेफ़रल बोनस" },
  sd_wallet_wd:   { en: "Withdrawal", hi: "निकासी" },
  sd_wallet_adj:  { en: "Manual adjustment", hi: "मैनुअल बदलाव" },
  sd_wallet_rev:  { en: "Reversal", hi: "वापसी" },
  sd_wallet_revd: { en: "reversed after refund", hi: "रिफ़ंड के बाद वापस" },
  sd_ref_loading: { en: "Loading your invite link…", hi: "आपका इनवाइट लिंक लोड हो रहा है…" },
  sd_earned_from: { en: "earned in total from", hi: "कुल कमाए —" },
  sd_paid_refs:   { en: "paid referrals", hi: "सफल रेफ़रल से" },
  sd_paid_ref_one:{ en: "paid referral", hi: "सफल रेफ़रल से" },
  sd_you_have:    { en: "you have", hi: "आपके पास है" },
  sd_one_active:  { en: "One currently active course", hi: "एक चालू कोर्स" },
  sd_buy_unlock:  { en: "buy or renew any series to unlock", hi: "खोलने के लिए कोई भी सीरीज़ लीजिए या रिन्यू कीजिए" },
});


/* Legal pages: the "who you are dealing with" block every policy needs. */
Object.assign(STR, {
  lg_en_only:    { en: "This page is available in English only.",
                   hi: "यह पृष्ठ केवल अंग्रेज़ी में उपलब्ध है। किसी भी बात पर संदेह हो तो हमें हिन्दी में लिखिए — हम हिन्दी में समझा देंगे।" },
  soc_soon:      { en: "coming soon", hi: "जल्द आ रहा है" },
  lg_privacy:    { en: "Privacy Policy", hi: "गोपनीयता नीति" },
  lg_terms:      { en: "Terms & Conditions", hi: "नियम एवं शर्तें" },
  lg_refund:     { en: "Refund Policy", hi: "रिफ़ंड नीति" },
  lg_contact:    { en: "Contact Us", hi: "संपर्क करें" },
});


/* Footer newsletter. */
Object.assign(STR, {
  news_h:       { en: "Free test papers & updates", hi: "मुफ़्त टेस्ट पेपर और अपडेट" },
  news_p:       { en: "A free paper now and then, and word when a new test series opens. Nothing else, and never spam.",
                  hi: "बीच-बीच में एक मुफ़्त पेपर, और नई टेस्ट सीरीज़ आने पर ख़बर। इसके अलावा कुछ नहीं, स्पैम कभी नहीं।" },
  news_ph:      { en: "you@email.com", hi: "aap@email.com" },
  news_btn:     { en: "Subscribe", hi: "जुड़िए" },
  news_sending: { en: "Adding…", hi: "जोड़ रहे हैं…" },
  news_ok:      { en: "Done — we'll write when there's something worth reading.",
                  hi: "हो गया — जब कुछ पढ़ने लायक होगा, हम लिखेंगे।" },
  news_already: { en: "You're already on the list.", hi: "आप पहले से सूची में हैं।" },
  news_bad:     { en: "That doesn't look like an email address.", hi: "यह ईमेल पते जैसा नहीं लग रहा।" },
  news_fail:    { en: "Couldn't add you just now. Please try again.", hi: "अभी जोड़ नहीं सके। कृपया दोबारा कोशिश कीजिए।" },
});


/* Student feedback. */
Object.assign(STR, {
  sd_feedback:   { en: "Feedback", hi: "प्रतिक्रिया" },
  sd_feedback_s: { en: "Tell us what is working and what is not", hi: "बताइए क्या ठीक चल रहा है और क्या नहीं" },

  fb_h:        { en: "Tell us something", hi: "हमें कुछ बताइए" },
  fb_sub:      { en: "A person reads every one of these.", hi: "इनमें से हर एक को एक व्यक्ति पढ़ता है।" },
  fb_what:     { en: "What is this about?", hi: "बात किस बारे में है?" },
  fb_rate:     { en: "How is JUNOONIAS working for you? (optional)", hi: "JUNOONIAS आपके लिए कैसा चल रहा है? (वैकल्पिक)" },
  fb_msg:      { en: "Your message", hi: "आपका संदेश" },
  fb_ph:       { en: "The more exact you are, the faster we can fix it. Test name, question number, what you expected and what happened.",
                 hi: "जितना सटीक बताएँगे, उतनी जल्दी ठीक होगा। टेस्ट का नाम, प्रश्न संख्या, आपने क्या सोचा था और क्या हुआ।" },
  fb_tip:      { en: "Hindi or English — whichever is easier for you.", hi: "हिन्दी या अंग्रेज़ी — जो आपको आसान लगे।" },
  fb_send:     { en: "Send", hi: "भेजें" },
  fb_sending:  { en: "Sending…", hi: "भेजा जा रहा है…" },
  fb_sent:     { en: "Sent — thank you. We read these properly.", hi: "भेज दिया — धन्यवाद। हम इन्हें ध्यान से पढ़ते हैं।" },
  fb_failed:   { en: "Could not send just now. Please try again.", hi: "अभी भेज नहीं सके। कृपया दोबारा कोशिश कीजिए।" },
  fb_too_short:{ en: "Please write a little more so we can act on it.", hi: "थोड़ा और लिखिए ताकि हम उस पर काम कर सकें।" },
  fb_mine:     { en: "What you have sent", hi: "आपने जो भेजा" },
  fb_mine_sub: { en: "With our reply, when there is one", hi: "जहाँ उत्तर आया है, वहाँ उत्तर सहित" },
  fb_none:     { en: "Nothing yet. If something is broken or confusing, tell us — it genuinely helps.",
                 hi: "अभी कुछ नहीं। कुछ टूटा हुआ या उलझन भरा लगे तो बताइए — इससे सचमुच मदद मिलती है।" },
  fb_reply:    { en: "Our reply", hi: "हमारा उत्तर" },

  fb_k_bug:        { en: "Something is broken", hi: "कुछ टूटा हुआ है" },
  fb_k_content:    { en: "Question or answer", hi: "प्रश्न या उत्तर" },
  fb_k_test:       { en: "A test", hi: "कोई टेस्ट" },
  fb_k_payment:    { en: "Payment or access", hi: "भुगतान या एक्सेस" },
  fb_k_suggestion: { en: "A suggestion", hi: "एक सुझाव" },
  fb_k_general:    { en: "Something else", hi: "कुछ और" },

  fb_s_new:         { en: "Sent", hi: "भेजा गया" },
  fb_s_seen:        { en: "Read", hi: "पढ़ा गया" },
  fb_s_in_progress: { en: "Being fixed", hi: "ठीक किया जा रहा है" },
  fb_s_resolved:    { en: "Resolved", hi: "हल हो गया" },
  fb_s_wont_fix:    { en: "Closed", hi: "बंद" },
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
export function ChromeControls({ light = false, palettePicker = false, segmented = false, paletteOnly = false }) {
  const { lang, t, setLang } = useLang();
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
  const paletteMenu = (
    <div className="jn-pal-wrap" onMouseLeave={() => setOpen(false)}>
      <button type="button" className="jn-pill jn-pill-icon" style={pill}
              onClick={() => setOpen(!open)} aria-label={t("nav_colour_change")} aria-expanded={open}>
        <Palette size={14} />
      </button>
      {open && (
        <div className="jn-palettes" role="menu">
          <div className="jn-palettes-t">{t("nav_colour")}</div>
          {PALETTES.map((p) => (
            <button key={p.key} role="menuitemradio" aria-checked={palette === p.key}
                    className={"jn-pal" + (palette === p.key ? " on" : "")}
                    onClick={() => { setPalette(p.key); setOpen(false); }}>
              <span className="jn-pal-sw" style={{ background: p.brand, borderColor: p.cream }} />
              <span>
                <b>{lang === "hi" ? p.labelHi : p.label}</b>
                <em>{lang === "hi" ? p.hintHi : p.hint}</em>
              </span>
              {palette === p.key && <Check size={14} />}
            </button>
          ))}
        </div>
      )}
    </div>
  );

  /* Just the colour chooser. On a phone language and theme live in the header
     capsule, so the menu shows only what the header does not — the palette
     picker was briefly lost when the whole block was hidden to avoid showing
     language and theme twice. */
  if (paletteOnly) {
    return <div style={{ display: "flex", gap: 6 }}>{paletteMenu}</div>;
  }

  /* Segmented: language and theme read as one object with a hairline between
     them, rather than two separate circles competing with the primary action
     beside them. Same buttons, same behaviour — only the chrome differs. */
  if (segmented) {
    return (
      <div className="jn-seg">
        <button type="button" className="jn-seg-btn" onClick={() => setLang(lang === "en" ? "hi" : "en")}
                aria-label={lang === "en" ? "Switch to Hindi" : "Switch to English"}>
          <Globe size={13} />
          <span className="jn-seg-label">{lang === "en" ? "हि" : "EN"}</span>
        </button>
        <span className="jn-seg-div" aria-hidden="true" />
        <button type="button" className="jn-seg-btn jn-seg-icon" onClick={toggle}
                aria-label={theme === "light" ? "Switch to dark theme" : "Switch to light theme"}>
          {theme === "light" ? <Moon size={14} /> : <Sun size={14} />}
        </button>
      </div>
    );
  }

  return (
    <div style={{ display: "flex", gap: 6 }}>
      <button type="button" className="jn-pill" style={pill} onClick={() => setLang(lang === "en" ? "hi" : "en")}
              aria-label={lang === "en" ? "Switch to Hindi" : "Switch to English"}>
        <Globe size={13} />{" "}
        <span className="jn-pill-label jn-pill-long">{lang === "en" ? "हिन्दी" : "English"}</span>
        <span className="jn-pill-label jn-pill-short">{lang === "en" ? "हि" : "EN"}</span>
      </button>
      <button type="button" className="jn-pill jn-pill-icon" style={pill} onClick={toggle}
              aria-label={theme === "light" ? "Switch to dark theme" : "Switch to light theme"}>
        {theme === "light" ? <Moon size={14} /> : <Sun size={14} />}
      </button>

      {palettePicker && paletteMenu}
    </div>
  );
}
