import { FileText } from "lucide-react";
import { useLang } from "../lib/contexts.js";

/* ============================================================================
 * BrochureButton — one component, used on every catalogue card AND on the
 * bundle detail page. Zero surface when no PDF is uploaded yet.
 *
 * Anchor tag, not a button + window.open — mobile browsers (particularly iOS
 * Safari) are far more reliable at handing the tab to the native PDF viewer
 * when the trigger is a real <a target="_blank"> with a real href. window.open
 * mid-click gets popup-blocked in more places than the raw link does.
 *
 * `variant`:
 *   - "card"   : compact top-right pill sitting on the card (default).
 *   - "detail" : full-width block on the buy panel of the detail page.
 * Both share the same colours and the same pulsing halo, so a visitor sees
 * the same visual across catalogue → detail without re-learning.
 * ==========================================================================*/
export default function BrochureButton({ url, planName = "", examLabel = "", variant = "card" }) {
  const { t } = useLang();
  if (!url) return null;
  const label = examLabel ? `${examLabel} ${t("card_brochure")}` : t("card_brochure");
  const aria = t("card_brochure_aria").replace("{name}", planName || examLabel || t("card_brochure"));
  const cls = variant === "detail" ? "pb-brochure pb-brochure--detail" : "pb-brochure pb-brochure--card";
  return (
    <a
      className={cls}
      href={url}
      target="_blank"
      rel="noopener noreferrer"
      aria-label={aria}
      title={aria}
    >
      <FileText size={variant === "detail" ? 16 : 14} aria-hidden="true" />
      <span>{label}</span>
    </a>
  );
}

/* CSS — exported so PublicSite can splice it into its own <style> block
 * alongside the rest of the storefront CSS. Kept together with the component
 * so the JSX and its styles stay in lock-step. */
export const BROCHURE_CSS = `
/* ---------- BROCHURE BUTTON (shared) ---------- */
.pb-brochure{position:relative;isolation:isolate;display:inline-flex;align-items:center;gap:6px;
  font-size:11.5px;font-weight:800;letter-spacing:.02em;text-decoration:none;cursor:pointer;
  padding:7px 12px;border-radius:100px;
  color:var(--brand-700);
  background:color-mix(in srgb,var(--gold-300) 22%,var(--cream-50));
  border:1.5px solid color-mix(in srgb,var(--gold-500) 55%,transparent);
  transition:transform .18s ease, background .18s ease, border-color .18s ease}
.pb-brochure:hover{transform:translateY(-1px);
  background:color-mix(in srgb,var(--gold-300) 34%,var(--cream-50));
  border-color:var(--gold-500)}
.pb-brochure:focus-visible{outline:2.5px solid var(--gold-500);outline-offset:2px}
.pb-brochure svg{color:var(--brand-700);flex:0 0 auto}

/* A slow warm halo -- brand palette, low opacity, three-second loop, resets
 * to zero glow between pulses so it doesn't read as "broken" or "loading".
 * The keyframe uses two shadows layered: a tight inner gold and an outer
 * translucent maroon, so the pulse feels like part of the card colour, not
 * a stuck notification badge. */
@keyframes pb-brochure-halo{
  0%,100%{box-shadow:0 0 0 0 color-mix(in srgb,var(--gold-500) 0%,transparent),
                    0 0 0 0 color-mix(in srgb,var(--brand-700) 0%,transparent)}
  50%    {box-shadow:0 0 0 3px color-mix(in srgb,var(--gold-500) 32%,transparent),
                    0 0 18px 6px color-mix(in srgb,var(--brand-700) 18%,transparent)}
}
.pb-brochure{animation:pb-brochure-halo 3s ease-in-out infinite}
.pb-brochure:hover,.pb-brochure:focus-visible{animation:none}
@media (prefers-reduced-motion: reduce){
  .pb-brochure{animation:none}
}

/* ---------- Variant: card (top-right corner of a BundleCard) ----------
 * Absolute so the existing card grid doesn't have to reflow around it.
 * z-index over the ::before top ribbon (which is z:0/1). Meets a 40px
 * tap target on coarse pointers via extra padding, without visually
 * inflating on desktop. */
.pb-card{position:relative}
.pb-brochure--card{position:absolute;top:12px;right:12px;z-index:2}

/* Coarse pointers (touch): raise the entire tap zone to WCAG 44px. The site
 * ships a global coarse-pointer rule that sets padding-block:4px on every
 * .pb-root anchor -- that rule beats a plain .pb-brochure--card class selector
 * on specificity. The .pb-root a.pb-brochure--card selector below matches
 * that same specificity so this padding wins. Using the padding shorthand
 * (all four sides) means the padding-block rule loses regardless. */
@media (pointer:coarse){
  .pb-root a.pb-brochure--card{padding:10px 14px;font-size:12px;top:10px;right:10px;min-height:44px}
  .pb-root a.pb-brochure--card svg{width:15px;height:15px}
}

/* ---------- Variant: detail (inside the buy panel) ---------- */
.pb-brochure--detail{width:100%;justify-content:center;padding:11px 16px;font-size:13px;
  margin-top:12px}
@media (pointer:coarse){
  .pb-root a.pb-brochure--detail{padding:13px 16px;min-height:44px}
}
`;
