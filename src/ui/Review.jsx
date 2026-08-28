/**
 * The shared post-test review card (spec §7: "one reusable component, two
 * contexts"). The per-test result screen (ExamApp) and the My-Performance
 * cross-attempt drill-down (StudentApp) both render <ReviewCard>, so an answer
 * shown one way in the result can never diverge from the same answer in the
 * drill-down.
 *
 * ExamApp already carries the `.rev-*` / `.stem-*` styles in its own stylesheet,
 * so it renders these components as-is. StudentApp does not, so it renders
 * <ReviewStyles/> once. That is the only duplication — the markup lives here.
 */
import { useState } from "react";
import { useLang } from "../lib/contexts.js";

const inLang = (lang, en, hi) => (lang === "hi" && hi ? hi : en);
const SEM = { strong: "#1f8a4c", weak: "#c0392b" };
const fmt = (s) => {
  const sec = Math.max(0, Math.round(Number(s) || 0));
  const m = Math.floor(sec / 60);
  return m > 0 ? `${m}m ${sec % 60}s` : `${sec}s`;
};

/**
 * The type-specific stem between the prompt and the options — numbered
 * statements, the List-I/List-II pairing, the Assertion/Reason block, a series,
 * and the trailing "which is correct?" line. Answer-free, bilingual. Used by the
 * live paper, the result review, and the drill-down.
 */
export function StemData({ data }) {
  const { t, lang } = useLang();
  if (!data || typeof data !== "object") return null;
  const statements = Array.isArray(data.statements) ? data.statements : null;
  const list1 = Array.isArray(data.list_1) ? data.list_1 : null;
  const list2 = Array.isArray(data.list_2) ? data.list_2 : null;
  const hasMatch = list1 && list2 && (list1.length > 0 || list2.length > 0);
  const hasAR = data.assertion || data.reason;
  const series = data.series;
  const closing = data.closing;
  if (!statements && !hasMatch && !hasAR && !series && !closing) return null;

  return (
    <div className="stem-data">
      {statements && statements.length > 0 && (
        <ol className="stmt-list">
          {statements.map((s, i) => (
            <li key={i}>{inLang(lang, s, (data.statements_hi || [])[i])}</li>
          ))}
        </ol>
      )}
      {hasMatch && (
        <div className="match-grid">
          <div className="match-col">
            <div className="match-head">{t("ex_list_i")}</div>
            {list1.map((x, i) => <div className="match-cell" key={i}>{inLang(lang, x, (data.list_1_hi || [])[i])}</div>)}
          </div>
          <div className="match-col">
            <div className="match-head">{t("ex_list_ii")}</div>
            {list2.map((x, i) => <div className="match-cell" key={i}>{inLang(lang, x, (data.list_2_hi || [])[i])}</div>)}
          </div>
        </div>
      )}
      {hasAR && (
        <div className="ar-block">
          {data.assertion && <div className="ar-row"><span className="ar-key">{t("ex_assertion")}:</span> {inLang(lang, data.assertion, data.assertion_hi)}</div>}
          {data.reason && <div className="ar-row"><span className="ar-key">{t("ex_reason")}:</span> {inLang(lang, data.reason, data.reason_hi)}</div>}
        </div>
      )}
      {series && <div className="series-line">{inLang(lang, series, data.series_hi)}</div>}
      {closing && <div className="stem-closing">{inLang(lang, closing, data.closing_hi)}</div>}
    </div>
  );
}

/**
 * One expandable review row. `r` is the review-row shape submit-attempt and the
 * my_review RPC both produce: text/text_hi, data, type, options[+_hi] in the
 * shown frame, correctVal/yourVal (indices into that frame), attempted/correct,
 * explanation, sourceCitation, correctRate, and optionally num/time/awarded.
 */
export function ReviewCard({ r, defaultOpen = false }) {
  const { t, lang } = useLang();
  const [open, setOpen] = useState(defaultOpen);
  const col = !r.attempted ? "#b0a080" : r.correct ? SEM.strong : SEM.weak;

  return (
    <div className="rev-item">
      <div className="rev-bar" onClick={() => setOpen((o) => !o)}>
        <div className="rev-idx" style={{ background: col }}>{r.num ?? "•"}</div>
        <div className="rev-q">{(r.text || "").split("\n")[0]}</div>
        <div className="rev-meta">
          {r.time != null && <span className="rev-time">⏱ {fmt(r.time)}</span>}
          {r.awarded != null && (
            <span className="rev-marks" style={{ color: r.awarded > 0 ? SEM.strong : r.awarded < 0 ? SEM.weak : "var(--muted)" }}>
              {r.awarded > 0 ? "+" : ""}{Number(r.awarded).toFixed(2)}
            </span>
          )}
          <span className={"rev-chev" + (open ? " open" : "")}>▶</span>
        </div>
      </div>
      {open && (
        <div className="rev-body">
          <div className="rev-qfull">{inLang(lang, r.text, r.text_hi)}</div>
          <StemData data={r.data} />
          {r.type !== "numerical" ? (
            <div className="rev-opts">
              {(r.options || []).map((opt, i) => {
                const isCorrect = r.type === "multiple" ? (Array.isArray(r.correctVal) && r.correctVal.includes(i)) : r.correctVal === i;
                const isYour = r.type === "multiple" ? (Array.isArray(r.yourVal) && r.yourVal.includes(i)) : r.yourVal === i;
                let cls = "neutral";
                if (isCorrect) cls = "correct";
                else if (isYour && !isCorrect) cls = "wrong";
                return (
                  <div key={i} className={"rev-opt " + cls}>
                    <span className="rev-opt-key">{String.fromCharCode(65 + i)}.</span>
                    <span>{inLang(lang, opt, r.options_hi?.[i])}</span>
                    {isCorrect && <span className="rev-flag flag-c">{t("ex_correct_ans")}</span>}
                    {isYour && !isCorrect && <span className="rev-flag flag-w">{t("ex_your_answer")}</span>}
                  </div>
                );
              })}
            </div>
          ) : (
            <div className="rev-opts">
              <div className="rev-opt correct"><span className="rev-opt-key">✓</span><span>{t("ex_correct_ans")}: {r.correctVal}</span></div>
              <div className={"rev-opt " + (r.correct ? "correct" : r.attempted ? "wrong" : "neutral")}>
                <span className="rev-opt-key">{r.attempted ? (r.correct ? "✓" : "✗") : "—"}</span>
                <span>{t("ex_your_answer")}: {r.attempted ? r.yourVal : t("ex_not_attempted")}</span>
              </div>
            </div>
          )}
          <div className="expl"><b>{t("ex_explanation")}</b> {inLang(lang, r.explanation, r.explanation_hi)}</div>
          {(r.sourceCitation || r.correctRate != null) && (
            <div className="rev-foot-meta">
              {r.sourceCitation && <span className="rev-source">{t("ex_source")}: {r.sourceCitation}</span>}
              {r.correctRate != null && <span className="rev-crowd">{r.correctRate}% {t("ex_got_correct")}</span>}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

/**
 * The card's styles, for hosts that don't already carry them (StudentApp).
 * ExamApp has its own copy in its stylesheet, so it does NOT render this.
 * Kept theme-aware (var(--ink)/--line) so the drill-down works in dark mode.
 */
export const REVIEW_CSS = `
.rev-item{border:1px solid var(--line);border-radius:12px;margin-bottom:12px;overflow:hidden}
.rev-bar{display:flex;align-items:center;gap:12px;padding:14px 16px;cursor:pointer;background:var(--card);transition:.13s}
.rev-bar:hover{background:var(--line)}
.rev-idx{width:34px;height:34px;border-radius:8px;display:grid;place-items:center;font-weight:800;font-size:13px;color:#ffffff;flex:0 0 auto}
.rev-q{flex:1;min-width:0;font-size:14px;color:var(--ink);font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.rev-meta{display:flex;align-items:center;gap:14px;flex:0 0 auto}
.rev-marks{font-size:13px;font-weight:800}
.rev-time{font-size:11.5px;color:var(--muted);display:flex;align-items:center;gap:4px}
.rev-chev{color:var(--muted);font-size:13px;transition:.2s}
.rev-chev.open{transform:rotate(90deg)}
.rev-body{padding:0 16px 18px;border-top:1px solid var(--line)}
.rev-qfull{font-size:14.5px;color:var(--ink);line-height:1.6;white-space:pre-wrap;padding:16px 0 14px}
.rev-opts{display:flex;flex-direction:column;gap:8px;margin-bottom:14px}
.rev-opt{display:flex;align-items:flex-start;gap:10px;padding:10px 13px;border-radius:9px;font-size:14px;border:1.5px solid transparent}
.rev-opt.correct{background:var(--grn-bg);border-color:#bfe3cd;color:#176437}
.rev-opt.wrong{background:var(--red-bg);border-color:#f1cccc;color:#a32f24}
.rev-opt.neutral{background:var(--line);color:var(--ink)}
.rev-opt-key{font-weight:800;flex:0 0 auto}
.rev-flag{margin-left:auto;font-size:11px;font-weight:800;padding:2px 9px;border-radius:20px;flex:0 0 auto}
.flag-c{background:#cdeedb;color:#176437}
.flag-w{background:#f6d6d6;color:#a32f24}
.expl{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--navy);border-radius:8px;padding:13px 15px;font-size:13.5px;color:var(--ink);line-height:1.6}
.expl b{color:var(--navy)}
.rev-foot-meta{display:flex;flex-wrap:wrap;gap:8px 16px;margin-top:10px;font-size:12px;color:var(--muted);font-weight:600}
.rev-crowd{color:var(--navy)}
.stem-data{display:flex;flex-direction:column;gap:12px;padding:2px 0 10px}
.stmt-list{margin:0;padding-left:24px;display:flex;flex-direction:column;gap:7px;font-size:14.5px;line-height:1.55;color:var(--ink)}
.match-grid{display:grid;grid-template-columns:1fr 1fr;border:1px solid var(--line);border-radius:9px;overflow:hidden;font-size:14px;color:var(--ink)}
.match-col{display:flex;flex-direction:column}
.match-col+.match-col{border-left:1px solid var(--line)}
.match-head{padding:8px 12px;font-weight:700;background:rgba(140,110,60,.08);border-bottom:1px solid var(--line)}
.match-cell{padding:8px 12px;border-bottom:1px solid var(--line);line-height:1.45}
.match-cell:last-child{border-bottom:none}
.ar-block{display:flex;flex-direction:column;gap:8px;font-size:14.5px;line-height:1.55;color:var(--ink);border-left:3px solid var(--line);padding:2px 0 2px 14px}
.ar-key{font-weight:700;margin-right:4px}
.series-line{font-size:15.5px;letter-spacing:.4px;font-weight:600;color:var(--ink)}
.stem-closing{font-size:14.5px;line-height:1.55;color:var(--ink);font-weight:600}
`;

export function ReviewStyles() {
  return <style>{REVIEW_CSS}</style>;
}
