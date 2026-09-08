import { FileText } from "lucide-react";
import { useLang } from "../lib/contexts.js";

/* ============================================================================
 * BrochureButton -- icon-only pill that sits in the action row of both the
 * catalogue card AND the bundle detail page's buy panel. Returns null when
 * the plan has no PDF uploaded yet, so the row layout is byte-identical to
 * before for every plan without a flyer.
 *
 * Anchor tag, not a button + window.open -- mobile browsers (particularly
 * iOS Safari) hand a real <a target="_blank"> to the native PDF viewer far
 * more reliably than a scripted window.open, which gets popup-blocked in
 * more places than the raw link does.
 *
 * Icon-only, deliberately: the exam label ("BPSC", "UPSC", etc.) already
 * sits in a pill at the top of the card and inside the h1 on the detail
 * page, so repeating "BPSC Brochure" here would be noise. The exam name
 * travels only through the aria-label + title, where a screen reader can
 * still find it. That also lets the trigger stay compact enough to share
 * the action row with the primary CTA on a phone.
 * ==========================================================================*/
export default function BrochureButton({ url, planName = "", examLabel = "" }) {
  const { t } = useLang();
  if (!url) return null;
  const aria = t("card_brochure_aria").replace("{name}", planName || examLabel || t("card_brochure"));
  return (
    <a
      className="pb-brochure"
      href={url}
      target="_blank"
      rel="noopener noreferrer"
      aria-label={aria}
      title={aria}
    >
      <FileText size={16} aria-hidden="true" />
      <span className="pb-brochure-sr">{aria}</span>
    </a>
  );
}

/* CSS -- exported so PublicSite can splice it into its own <style> block
 * alongside the rest of the storefront CSS. Kept together with the component
 * so the JSX and its styles stay in lock-step. */
export const BROCHURE_CSS = `
/* ---------- BROCHURE BUTTON ----------
 * Icon-only pill matching the .pb-btn-ghost outline treatment so it visually
 * groups with Details / Enroll on the same row. Fixed square-ish footprint
 * (~36 px desktop, 40 px+ on touch) so it never bloats the row layout.
 *
 * Text-content span is visually hidden but reachable by screen readers -- the
 * FileText icon carries the meaning, and the aria-label carries the exam
 * name. Clip-based hide, not display:none, keeps the accessible name intact. */
.pb-brochure{position:relative;isolation:isolate;
  display:inline-flex;align-items:center;justify-content:center;flex:0 0 auto;
  width:36px;height:36px;padding:0;border-radius:100px;text-decoration:none;
  color:var(--brand-700);
  background:var(--cream-50);
  border:1.5px solid color-mix(in srgb,var(--gold-500) 45%,transparent);
  transition:transform .18s ease, background .18s ease, border-color .18s ease}
.pb-brochure:hover{transform:translateY(-1px);
  background:color-mix(in srgb,var(--gold-300) 26%,var(--cream-50));
  border-color:var(--gold-500)}
.pb-brochure:focus-visible{outline:2.5px solid var(--gold-500);outline-offset:2px}
.pb-brochure svg{color:var(--brand-700)}
.pb-brochure-sr{position:absolute;width:1px;height:1px;padding:0;margin:-1px;
  overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}

/* A slow warm halo -- brand palette, low opacity, three-second loop, resets
 * to zero glow between pulses so it doesn't read as "broken" or "loading".
 * Deliberately gentler than the earlier text-pill treatment: this button is
 * smaller, and the pulse must not out-shout Enroll now. */
@keyframes pb-brochure-halo{
  0%,100%{box-shadow:0 0 0 0 color-mix(in srgb,var(--gold-500) 0%,transparent)}
  50%    {box-shadow:0 0 0 3px color-mix(in srgb,var(--gold-500) 24%,transparent),
                    0 0 12px 4px color-mix(in srgb,var(--brand-700) 14%,transparent)}
}
.pb-brochure{animation:pb-brochure-halo 3s ease-in-out infinite}
.pb-brochure:hover,.pb-brochure:focus-visible{animation:none}
@media (prefers-reduced-motion: reduce){
  .pb-brochure{animation:none}
}

/* Coarse pointers (touch): raise the tap target to WCAG 44 px. The site
 * ships a global coarse-pointer rule that sets padding-block:4px on every
 * .pb-root anchor; a plain .pb-brochure class selector loses on
 * specificity, so this matches .pb-root a on specificity. Setting explicit
 * width + min-height wins even against that padding-block rule. */
@media (pointer:coarse){
  .pb-root a.pb-brochure{width:44px;height:44px;min-height:44px}
  .pb-root a.pb-brochure svg{width:18px;height:18px}
}

/* ---------- Details-page action row -----------------------------------
 * Same layout idea as the catalogue card's button row: brochure icon on
 * the left, primary CTA takes the remaining width. Enroll here is no
 * longer .pb-btn-block (that was 100% width, breaks the flex-row); a
 * scoped .pb-buy-cta class puts it on flex:1 with the same visual as
 * before (padding matches the site's pb-btn-block for pb-buy). */
.pb-buy-cta-row{display:flex;gap:10px;align-items:stretch}
.pb-buy-cta{flex:1 1 auto;width:auto;text-align:center;justify-content:center;
  display:inline-flex;align-items:center;gap:8px}
`;
