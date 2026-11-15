import { useState } from "react";
import EssayView from "./EssayView.jsx";
import { useLang } from "../lib/contexts.js";
import { loadKey, saveKey } from "../lib/storage.js";

/* General Studies I-IV. Each paper is the Essay section's screen in its GS
   form (EssayView with a paper): PYQs filed under syllabus topics, topper
   answers from test series, notes. The paper picked is remembered. */
const PAPERS = [["gs1", "gs_p1"], ["gs2", "gs_p2"], ["gs3", "gs_p3"], ["gs4", "gs_p4"]];

const GS_CSS = `
.gs-papers{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 16px}
.gs-paper{font:inherit;cursor:pointer;display:flex;flex-direction:column;align-items:flex-start;gap:2px;min-width:120px;flex:1 1 120px;
  padding:10px 14px;border-radius:12px;border:1px solid var(--line);background:var(--card);color:var(--ink);text-align:left;
  transition:border-color .15s,background .15s}
.gs-paper b{font-size:14px}
.gs-paper span{font-size:12px;color:var(--muted);line-height:1.35}
.gs-paper:hover{border-color:var(--gold)}
.gs-paper.on{border-color:var(--navy-2);background:color-mix(in srgb,var(--navy-2) 8%,var(--card))}
.gs-paper.on b{color:var(--navy-2)}
.gs-paper:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
@media(max-width:560px){ .gs-paper{min-width:0;flex:1 1 40%} .gs-paper span{display:none} }
`;

export default function GsView({ onBrowse }) {
  const { t } = useLang();
  const [paper, setPaper] = useState(() => {
    const p = loadKey("gs:paper", "gs1");
    return PAPERS.some(([k]) => k === p) ? p : "gs1";
  });
  const pick = (p) => { setPaper(p); saveKey("gs:paper", p); };
  return (
    <div>
      <style>{GS_CSS}</style>
      <div className="gs-papers" role="tablist" aria-label={t("sd_gs")}>
        {PAPERS.map(([k, key]) => (
          <button key={k} className={"gs-paper" + (paper === k ? " on" : "")} role="tab" aria-selected={paper === k} onClick={() => pick(k)}>
            <b>{t(key)}</b><span>{t(`${key}_s`)}</span>
          </button>
        ))}
      </div>
      {/* Keyed by paper: switching papers starts that paper's screen afresh. */}
      <EssayView key={paper} paper={paper} onBrowse={onBrowse} />
    </div>
  );
}
