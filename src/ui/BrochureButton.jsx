import { FileText } from "lucide-react";
import { useLang } from "../lib/contexts.js";

/* ============================================================================
 * BrochureButton -- one component, two visual variants for the two places
 * it lives.
 *
 * variant="card" (default) is icon-only, ~36 px desktop / 44 px on touch,
 * sits in the card's action row alongside the primary CTA. Text label
 * omitted because the exam pill (BPSC / UPSC / ...) at the top of the card
 * already tells the reader which exam this is.
 *
 * variant="detail" is a full-width labelled pill placed directly UNDER the
 * Enroll button on the bundle detail page. There the exam name has room to
 * appear on the button itself, so a visitor scanning the buy panel sees
 * "BPSC Brochure" without also having to read the h1.
 *
 * Returns null when the plan has no PDF uploaded yet. Zero surface, zero
 * disabled button, no dead link.
 *
 * Anchor tag, not a button + window.open -- mobile browsers hand a real
 * <a target="_blank"> to the native PDF viewer far more reliably than a
 * scripted popup, and popup blockers hit fewer real anchors.
 * ==========================================================================*/
export default function BrochureButton({ url, planName = "", examLabel = "", variant = "card" }) {
  const { t } = useLang();
  if (!url) return null;
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
      <FileText size={variant === "detail" ? 16 : 16} aria-hidden="true" />
      {variant === "detail" ? (
        <span>{examLabel ? `${examLabel} ${t("card_brochure")}` : t("card_brochure")}</span>
      ) : (
        <span className="pb-brochure-sr">{aria}</span>
      )}
    </a>
  );
}

/* CSS -- exported so PublicSite can splice it into its own <style> block
 * alongside the rest of the storefront CSS. Kept together with the component
 * so the JSX and its styles stay in lock-step. */
export const BROCHURE_CSS = `
/* ---------- BROCHURE BUTTON (shared) ----------
 * Both variants share the outline + halo treatment so a visitor learns the
 * button once and recognises it on either surface. */
.pb-brochure{position:relative;isolation:isolate;text-decoration:none;cursor:pointer;
  color:var(--brand-700);
  background:var(--cream-50);
  border:1.5px solid color-mix(in srgb,var(--gold-500) 45%,transparent);
  transition:transform .18s ease, background .18s ease, border-color .18s ease}
.pb-brochure:hover{transform:translateY(-1px);
  background:color-mix(in srgb,var(--gold-300) 26%,var(--cream-50));
  border-color:var(--gold-500)}
.pb-brochure:focus-visible{outline:2.5px solid var(--gold-500);outline-offset:2px}
.pb-brochure svg{color:var(--brand-700);flex:0 0 auto}

/* A slow warm halo -- brand palette, low opacity, three-second loop, resets
 * to zero glow between pulses so it doesn't read as "broken" or "loading". */
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

/* ---------- Variant: card (icon-only pill in the action row) ---------- */
.pb-brochure--card{display:inline-flex;align-items:center;justify-content:center;
  flex:0 0 auto;width:36px;height:36px;padding:0;border-radius:100px}
.pb-brochure-sr{position:absolute;width:1px;height:1px;padding:0;margin:-1px;
  overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
/* Touch: raise to the WCAG 44 px floor. The site's global coarse-pointer
 * rule .pb-root a { padding-block:4px } would beat a plain .pb-brochure
 * class selector on specificity; the .pb-root a.pb-brochure selector below
 * matches that same specificity, and explicit width + min-height wins
 * regardless of any padding rule. */
@media (pointer:coarse){
  .pb-root a.pb-brochure--card{width:44px;height:44px;min-height:44px}
  .pb-root a.pb-brochure--card svg{width:18px;height:18px}
}

/* ---------- Variant: detail (full-width labelled pill under Enroll) ----------
 * Same outline treatment as pb-btn-ghost so it visually pairs with the
 * gold Enroll now button directly above it. Sits inside the buy panel;
 * the margin-top separates it from Enroll without needing a wrapper. */
.pb-brochure--detail{display:inline-flex;align-items:center;justify-content:center;gap:8px;
  width:100%;padding:11px 16px;font-size:13px;font-weight:800;letter-spacing:.02em;
  border-radius:100px;margin-top:12px}
@media (pointer:coarse){
  .pb-root a.pb-brochure--detail{padding:13px 16px;min-height:44px}
}
`;
