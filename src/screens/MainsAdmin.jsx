import { useState, useEffect, useMemo, useRef, useCallback } from "react";
import { Upload, FileText, Search, Pencil, Trash2, X, Eye, ExternalLink, Plus, Save, AlertCircle, CheckCircle2, BookOpen } from "lucide-react";
import * as DB from "../lib/db.js";
import { parseImportFiles, cleanBody, wordCount } from "../lib/mainsImport.js";
import CopyViewer from "../ui/CopyViewer.jsx";
import { ErrorState, SkeletonCards } from "../ui/Feedback.jsx";
import { useLang } from "../lib/contexts.js";
import { LtwDoc, STUDY_CSS } from "./EssayStudy.jsx";

/* ============================================================
   ADMIN: MAINS & ESSAY  (slice 1, migration 0028)

   Three jobs, one tab each:
   1. Import -- the spreadsheets we already keep, exported as CSV.
      A preview says what will be created and which rows were
      skipped and why, before anything is written.
   2. Copies -- every copy, link or hosted. Upload a PDF to host it
      (rendered page by page in this browser), mark where each
      answer starts and ends, and link essay answers to PYQs.
   3. Essay PYQs and themes -- the syllabus students browse by.

   Loaded on demand from AdminApp, so none of this (nor pdf.js,
   which the upload pulls in) reaches a student's bundle.
   ============================================================ */

const MA_CSS = `
.ma-tabs{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:18px}
.ma-tab{font-size:13px;font-weight:700;padding:9px 16px;border-radius:20px;border:1.5px solid var(--line);
  color:var(--ink);background:var(--card);cursor:pointer;transition:.13s}
.ma-tab.on{background:var(--navy);border-color:var(--navy);color:#ffffff}
.ma-tab:hover:not(.on){border-color:var(--gold-2)}
.ma-steps{display:flex;flex-direction:column;gap:6px;font-size:13px;color:var(--muted);margin-top:12px}
.ma-steps b{color:var(--ink)}
.ma-bar{height:8px;border-radius:99px;background:var(--line);overflow:hidden;margin-top:8px}
.ma-bar span{display:block;height:100%;background:var(--navy);transition:width .2s}
.ma-pre{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:10px;margin:14px 0}
.ma-stat{background:var(--hair,#fdf6e3);border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.ma-stat b{display:block;font-size:20px;font-weight:800;color:var(--ink);font-variant-numeric:tabular-nums}
.ma-stat span{font-size:12px;color:var(--muted)}
.ma-skip{font-size:12.5px;color:var(--muted);margin:6px 0 0;padding-left:18px}
.ma-skip li{margin:2px 0}
.ma-chips{display:flex;flex-wrap:wrap;gap:6px}
.ma-chip{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:600;border:1.5px solid var(--line);
  border-radius:999px;padding:3px 4px 3px 10px;background:var(--card);color:var(--ink);max-width:100%}
.ma-chip .t{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:420px}
.ma-chip button{border:0;background:none;cursor:pointer;color:var(--muted);display:grid;place-items:center;padding:2px}
.ma-kind{font-size:10.5px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;border-radius:99px;padding:2px 7px;cursor:pointer;border:0;
  white-space:nowrap;flex:0 0 auto}
.ma-kind.exact{background:#e8f6ee;color:#1f7a4c}
.ma-kind.related{background:#faf2dc;color:#8a6a14}
.ma-sugg{display:flex;flex-direction:column;gap:6px;margin-top:8px}
.ma-sugg-row{display:flex;align-items:center;gap:8px;font-size:13px;padding:6px 8px;border:1px solid var(--line);border-radius:9px}
.ma-sugg-row .t{flex:1;min-width:0}
.ma-sugg-row .s{font-size:11px;color:var(--muted);font-variant-numeric:tabular-nums;white-space:nowrap}
.ma-ans{border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin-bottom:10px;background:var(--card)}
.ma-ans-top{display:flex;align-items:flex-start;gap:10px}
.ma-ans-q{flex:1;min-width:0;font-size:14px;font-weight:700;color:var(--ink);line-height:1.4}
.ma-ans-meta{font-size:12px;color:var(--muted);margin-top:3px}
.ma-split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:18px;align-items:start}
.ma-stack{display:flex;flex-direction:column;gap:18px}
.ma-theme-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));column-gap:20px}
@media(max-width:980px){.ma-split{grid-template-columns:minmax(0,1fr)}}
`;

const PAPERS = [
  ["essay", "Essay"], ["gs1", "GS 1"], ["gs2", "GS 2"], ["gs3", "GS 3"], ["gs4", "GS 4"],
  ["optional", "Optional"], ["other", "Other"],
];
const PAPER_LABEL = Object.fromEntries(PAPERS);

const FORMAT_LABEL = {
  pyq_categories: "Essay PYQs with categories",
  topper_answers: "Topper answers (subject, topper, page, link)",
  topper_essays: "Topper essays with their copies",
  topic_map: "Similar-PYQ map (topic → similar PYQs)",
  essay_texts: "Essay texts (typed transcripts)",
};
const FORMAT_UNIT = {
  pyq_categories: ["PYQ", "PYQs"], topper_answers: ["answer", "answers"], topper_essays: ["essay", "essays"],
  topic_map: ["topic", "topics"], essay_texts: ["essay text", "essay texts"],
};

/* Word overlap, for suggesting which PYQs an essay answers. Crude next to an
   embedding, but the bank is ~100 PYQs and the admin decides. */
const STOP = new Set(("a an the of is are was be to in on for and or not but with as by it its this that what which who " +
  "whom your you we our their his her than then there from at into only all any can will would should may might must " +
  "no nor so too very just one more most much many have has had do does did").split(" "));
function words(s) {
  return new Set(String(s || "").toLowerCase().replace(/[^a-z0-9\s]/g, " ").split(/\s+/).filter((w) => w.length > 2 && !STOP.has(w)));
}
function overlap(a, b) {
  const A = words(a);
  const B = words(b);
  if (!A.size || !B.size) return 0;
  let n = 0;
  A.forEach((w) => { if (B.has(w)) n++; });
  return n / Math.sqrt(A.size * B.size);
}

/* Shared shells, the same markup AdminApp's own Modal and Field produce. */
function Modal({ title, onClose, children, footer, wide }) {
  return (
    <div className="overlay" onClick={onClose}>
      <div className={"modal" + (wide ? " wide" : "")} onClick={(e) => e.stopPropagation()} role="dialog" aria-modal="true">
        <div className="modal-head">
          <h3>{title}</h3>
          <button className="x" onClick={onClose} aria-label="Close"><X size={19} /></button>
        </div>
        <div className="modal-body">{children}</div>
        {footer && <div className="modal-foot">{footer}</div>}
      </div>
    </div>
  );
}
function Field({ label, req, hint, children }) {
  return (
    <div className="field">
      {label && <label>{label}{req && <span className="req"> *</span>}</label>}
      {children}
      {hint && <div className="hint">{hint}</div>}
    </div>
  );
}
const num = (v) => (v === "" || v == null ? "" : String(v));

/** Load something whenever `key` changes. The result remembers its key, so
 *  "loading" is just a result for an older key -- no state reset in effects. */
function useLoad(load, key) {
  const [res, setRes] = useState({ key: null, data: null, err: "" });
  const loadRef = useRef(load);
  useEffect(() => { loadRef.current = load; });
  useEffect(() => {
    let alive = true;
    loadRef.current().then(
      (data) => { if (alive) setRes({ key, data, err: "" }); },
      (e) => { console.error(e); if (alive) setRes({ key, data: null, err: e?.message || "Couldn't load this." }); },
    );
    return () => { alive = false; };
  }, [key]);
  return { loading: res.key !== key, data: res.key === key ? res.data : null, err: res.key === key ? res.err : "" };
}

export default function MainsAdmin({ toast, askDelete }) {
  const [tab, setTab] = useState("import");
  return (
    <div>
      <style>{MA_CSS}</style>
      {/* Own classes: the admin stylesheet defines no .tabs/.tab (those live
          in the student dashboard's CSS), so those render as bare buttons. */}
      <div className="ma-tabs" role="tablist">
        {[["import", "Import sheets"], ["copies", "Copies"], ["pyqs", "Essay PYQs & themes"], ["wiki", "Essay Wiki"], ["ltw", "Learn to Write"]].map(([k, l]) => (
          <button key={k} role="tab" aria-selected={tab === k} className={"ma-tab" + (tab === k ? " on" : "")} onClick={() => setTab(k)}>{l}</button>
        ))}
      </div>
      {tab === "import" && <ImportPanel toast={toast} />}
      {tab === "copies" && <CopiesPanel toast={toast} askDelete={askDelete} />}
      {tab === "pyqs" && <PyqsPanel toast={toast} askDelete={askDelete} />}
      {tab === "wiki" && <WikiPanel toast={toast} askDelete={askDelete} />}
      {tab === "ltw" && <LtwAdminPanel toast={toast} askDelete={askDelete} />}
    </div>
  );
}

/* ================================================================ IMPORT == */

function ImportPanel({ toast }) {
  const fileRef = useRef(null);
  const [name, setName] = useState("");
  const [parsed, setParsed] = useState(null);
  const [paste, setPaste] = useState("");
  const [papers, setPapers] = useState(() => new Set(PAPERS.map(([k]) => k)));
  const [run, setRun] = useState(null);   // { step } while running, { result } or { err } after

  const read = (files) => {
    setName(files.map((f) => f.name).join(", "));
    setRun(null);
    setParsed(parseImportFiles(files));
  };
  const onFile = async (e) => {
    const picked = [...(e.target.files || [])];
    if (fileRef.current) fileRef.current.value = "";
    if (!picked.length) return;
    read(await Promise.all(picked.map(async (f) => ({ name: f.name, text: await f.text() }))));
  };

  const items = useMemo(() => {
    if (!parsed) return [];
    return parsed.format === "topper_answers" ? parsed.items.filter((it) => papers.has(it.paper)) : parsed.items;
  }, [parsed, papers]);

  const paperCounts = useMemo(() => {
    const m = new Map();
    if (parsed?.format === "topper_answers") parsed.items.forEach((it) => m.set(it.paper, (m.get(it.paper) || 0) + 1));
    return m;
  }, [parsed]);

  const start = async () => {
    const step = (s) => setRun({ step: s });
    setRun({ step: "starting" });
    try {
      let result;
      if (parsed.format === "pyq_categories") result = await DB.importEssayPyqs(items, step);
      else if (parsed.format === "topper_answers") result = await DB.importTopperAnswers(items, step);
      else if (parsed.format === "topper_essays") result = await DB.importTopperEssays(items, parsed.topics, step);
      else if (parsed.format === "essay_texts") result = await DB.importEssayTexts(items, step);
      else result = await DB.importTopicMap(items, step);
      setRun({ result });
      toast("Import finished");
    } catch (e) {
      console.error(e);
      setRun({ err: e?.message || "The import stopped part-way. Re-running it is safe: rows already saved are skipped." });
      toast(e?.message || "Import failed", "err");
    }
  };

  const running = run && run.step;
  const unit = (parsed && FORMAT_UNIT[parsed.format]) || ["row", "rows"];
  const similarCount = parsed?.topics?.reduce((n, t) => n + t.similar.length, 0) || 0;
  // The essay tab alone still carries its similar-PYQ map.
  const canImport = items.length > 0 || (parsed?.format === "topper_essays" && similarCount > 0);
  const skipReasons = Object.entries((parsed?.skipped || []).reduce((m, s) => ((m[s.reason] = (m[s.reason] || 0) + 1), m), {}));
  return (
    <div>
      <div className="banner">
        <AlertCircle size={17} />
        <span>
          Export each Google Sheet tab as CSV (File → Download → Comma-separated values) and add it here.
          Import the <b>PYQs</b> first. For <b>topper essays</b>, add the essay tab together with its <b>HandwrittenLinks</b> tab
          (select both files): the essay tab&apos;s links are formulas, which a CSV keeps only as the word &quot;Link&quot;.
          Essay texts (typed transcripts) go in after the topper essays.
          Re-importing a newer export is safe: existing rows are kept, new ones are added.
        </span>
      </div>

      <div className="panel panel-pad" style={{ marginBottom: 16 }}>
        <div style={{ display: "flex", gap: 10, flexWrap: "wrap", alignItems: "center" }}>
          <button className="btn btn-primary" onClick={() => fileRef.current?.click()} disabled={running}><Upload size={16} />Choose CSV files</button>
          <input ref={fileRef} type="file" accept=".csv,text/csv" multiple style={{ display: "none" }} onChange={onFile} />
          {name && <span style={{ fontSize: 13, color: "var(--muted)" }}><FileText size={14} style={{ verticalAlign: -2 }} /> {name}</span>}
        </div>
        <details style={{ marginTop: 12 }}>
          <summary style={{ cursor: "pointer", fontSize: 13, color: "var(--muted)" }}>…or paste CSV text</summary>
          <textarea className="inp" rows={6} value={paste} onChange={(e) => setPaste(e.target.value)}
                    placeholder="Subject,Year,Rank,Topper,Coaching,Question,Page,Link" style={{ marginTop: 8, fontFamily: "ui-monospace,monospace", fontSize: 12.5 }} />
          <button className="btn btn-ghost btn-sm" style={{ marginTop: 8 }} disabled={!paste.trim() || running}
                  onClick={() => read([{ name: "pasted text", text: paste }])}>Read pasted text</button>
        </details>
      </div>

      {parsed && (
        <div className="panel panel-pad">
          {parsed.files.length > 1 && (
            <ul className="ma-skip" style={{ marginTop: 0, marginBottom: 12 }}>
              {parsed.files.map((f, i) => <li key={i}><b>{f.name}</b> · {f.role}{f.rows ? ` · ${f.rows} rows` : ""}</li>)}
            </ul>
          )}
          {!parsed.format ? (
            <div className="form-err"><AlertCircle size={16} />{parsed.notes[0]}</div>
          ) : (
            <>
              <div className="sec-head" style={{ marginBottom: 6 }}>
                <div>
                  <h2>{FORMAT_LABEL[parsed.format]}</h2>
                  <div className="note">{parsed.notes.filter(Boolean).join(" · ")}</div>
                </div>
              </div>

              {parsed.format === "topper_answers" && (
                <Field label="Papers to import" hint="GS rows are stored now and used when the GS sections are built; only Essay shows to students today.">
                  <div className="chip-pick">
                    {PAPERS.filter(([k]) => paperCounts.get(k)).map(([k, l]) => (
                      <button key={k} type="button" className={"chip-opt" + (papers.has(k) ? " on" : "")}
                              onClick={() => setPapers((s) => { const n = new Set(s); if (n.has(k)) n.delete(k); else n.add(k); return n; })}>
                        {l} · {paperCounts.get(k)}
                      </button>
                    ))}
                  </div>
                </Field>
              )}

              <div className="ma-pre">
                <div className="ma-stat"><b>{items.length}</b><span>{unit[1]} to import</span></div>
                {parsed.format === "topper_essays" && <div className="ma-stat"><b>{similarCount}</b><span>similar-PYQ entries</span></div>}
                <div className="ma-stat"><b>{parsed.skipped.length}</b><span>rows skipped</span></div>
              </div>

              {parsed.skipped.length > 0 && (
                <details>
                  <summary style={{ cursor: "pointer", fontSize: 13, color: "var(--muted)" }}>
                    Why rows were skipped: {skipReasons.map(([r, n]) => `${r} (${n})`).join("; ")}
                  </summary>
                  <ul className="ma-skip">
                    {parsed.skipped.slice(0, 12).map((s, i) => <li key={i}>Row {s.row}: {s.reason}{s.text ? ` — ${s.text.slice(0, 90)}` : ""}</li>)}
                    {parsed.skipped.length > 12 && <li>…and {parsed.skipped.length - 12} more</li>}
                  </ul>
                </details>
              )}

              <ImportSample format={parsed.format} items={items} />

              <div style={{ display: "flex", gap: 10, alignItems: "center", marginTop: 16, flexWrap: "wrap" }}>
                <button className="btn btn-primary" onClick={start} disabled={!canImport || running}>
                  <Upload size={16} />
                  {running ? "Importing…" : items.length ? `Import ${items.length} ${unit[items.length === 1 ? 0 : 1]}` : "Import the similar-PYQ map"}
                </button>
                {running && <span style={{ fontSize: 13, color: "var(--muted)" }}>Step: <b>{run.step}</b></span>}
              </div>
              {run?.err && <div className="form-err" style={{ marginTop: 12 }}><AlertCircle size={16} />{run.err}</div>}
              {run?.result && (
                <div className="ma-steps">
                  <div><CheckCircle2 size={15} style={{ verticalAlign: -3, color: "var(--green)" }} /> <b>Imported.</b></div>
                  {Object.entries(run.result).filter(([k]) => k !== "unmatched" && k !== "missing").map(([k, v]) => <div key={k}>{k}: <b>{v}</b></div>)}
                  {run.result.unmatched?.length > 0 && (
                    <details>
                      <summary style={{ cursor: "pointer" }}>{run.result.unmatched.length} similar PYQs not found in the PYQ list</summary>
                      <ul className="ma-skip">{run.result.unmatched.slice(0, 20).map((u) => <li key={u}>{u}</li>)}</ul>
                    </details>
                  )}
                  {run.result.missing?.length > 0 && (
                    <details>
                      <summary style={{ cursor: "pointer" }}>{run.result.missing.length} rows matched no imported essay</summary>
                      <ul className="ma-skip">{run.result.missing.slice(0, 20).map((u) => <li key={u}>{u}</li>)}</ul>
                    </details>
                  )}
                </div>
              )}
            </>
          )}
        </div>
      )}
    </div>
  );
}

function ImportSample({ format, items }) {
  const rows = items.slice(0, 5);
  if (!rows.length) return null;
  if (format === "pyq_categories") {
    return (
      <div className="tbl-wrap" style={{ marginTop: 12 }}>
        <table className="tbl">
          <thead><tr><th>Year</th><th>Topic</th><th>Themes (confidence)</th></tr></thead>
          <tbody>{rows.map((it, i) => (
            <tr key={i}><td className="nowrap">{it.year}</td><td>{it.topic}</td><td>{it.themes.map((t) => `${t.name} (${t.confidence})`).join(", ")}</td></tr>
          ))}</tbody>
        </table>
      </div>
    );
  }
  if (format === "topper_answers") {
    return (
      <div className="tbl-wrap" style={{ marginTop: 12 }}>
        <table className="tbl">
          <thead><tr><th>Paper</th><th>Topper</th><th>Question</th><th>Page</th><th>Source</th></tr></thead>
          <tbody>{rows.map((it, i) => (
            <tr key={i}>
              <td className="nowrap">{PAPER_LABEL[it.paper]}{it.paperLabel ? ` · ${it.paperLabel}` : ""}</td>
              <td>{it.topper.name}{it.topper.rank ? ` · AIR ${it.topper.rank}` : ""}{it.topper.cseYear ? ` (${it.topper.cseYear})` : ""}</td>
              <td>{it.question}</td>
              <td className="nowrap">{it.page ?? "—"}</td>
              <td>{it.coaching}</td>
            </tr>
          ))}</tbody>
        </table>
      </div>
    );
  }
  if (format === "essay_texts") {
    return (
      <div className="tbl-wrap" style={{ marginTop: 12 }}>
        <table className="tbl">
          <thead><tr><th>Essay topic</th><th>Copy</th><th>Words</th><th>Opening</th></tr></thead>
          <tbody>{rows.map((it, i) => (
            <tr key={i}>
              <td>{it.question}</td>
              <td>{(it.file || "").replace(/\.pdf$/i, "") || "—"}</td>
              <td className="nowrap">{it.words.toLocaleString("en-IN")}</td>
              <td style={{ color: "var(--muted)" }}>{it.body.slice(0, 140)}{it.body.length > 140 ? "…" : ""}</td>
            </tr>
          ))}</tbody>
        </table>
      </div>
    );
  }
  if (format === "topper_essays") {
    return (
      <div className="tbl-wrap" style={{ marginTop: 12 }}>
        <table className="tbl">
          <thead><tr><th>Writer</th><th>Essay topic</th><th>Copy</th></tr></thead>
          <tbody>{rows.map((it, i) => (
            <tr key={i}>
              <td>
                {it.topper.name}{it.topper.rank ? ` · AIR ${it.topper.rank}` : ""}
                {it.topper.essayMarks ? ` · Essay ${it.topper.essayMarks}` : ""}{it.coaching ? ` · ${it.coaching}` : ""}
              </td>
              <td>{it.question}</td>
              <td><a href={it.url} target="_blank" rel="noopener noreferrer">{it.title || "PDF"}</a></td>
            </tr>
          ))}</tbody>
        </table>
      </div>
    );
  }
  return (
    <div className="tbl-wrap" style={{ marginTop: 12 }}>
      <table className="tbl">
        <thead><tr><th>Topic in the copy</th><th>Similar PYQs (confidence)</th></tr></thead>
        <tbody>{rows.map((it, i) => (
          <tr key={i}><td>{it.topic}</td><td>{it.similar.map((s) => `${s.topic} (${s.year}, ${s.confidence})`).join("; ")}</td></tr>
        ))}</tbody>
      </table>
    </div>
  );
}

/* ================================================================ COPIES == */

function CopiesPanel({ toast, askDelete }) {
  const [q, setQ] = useState("");
  const [needle, setNeedle] = useState("");
  const [paper, setPaper] = useState("");
  const [limit, setLimit] = useState(40);
  const [reload, setReload] = useState(0);
  const [editing, setEditing] = useState(null);
  const [uploading, setUploading] = useState(null);   // {} for a new copy, { copy } to attach pages
  const [viewing, setViewing] = useState(null);

  useEffect(() => { const id = setTimeout(() => setNeedle(q.trim()), 300); return () => clearTimeout(id); }, [q]);
  const list = useLoad(() => DB.adminCopies({ q: needle, paper, offset: 0, limit }), `${needle}|${paper}|${limit}|${reload}`);
  const refresh = () => setReload((n) => n + 1);

  const remove = (c) => askDelete(
    `Delete this copy by ${c.topper.name}? Its answers, their PYQ links and any hosted pages go with it.`,
    async () => {
      try { await DB.deleteCopy(c.id); toast("Copy deleted"); refresh(); }
      catch (e) { console.error(e); toast(e?.message || "Couldn't delete", "err"); }
    });

  const toggle = async (c, field) => {
    try { await DB.updateCopy(c.id, { [field]: !c[field] }); refresh(); }
    catch (e) { console.error(e); toast(e?.message || "Couldn't update", "err"); }
  };

  const items = list.data?.items ?? [];
  return (
    <div>
      <div className="sec-head">
        <div>
          <h2>{list.data ? `${list.data.total} copies` : "Copies"}</h2>
          <div className="note">A copy is a link to a publisher's PDF, a hosted scan, or both</div>
        </div>
        <div style={{ display: "flex", gap: 8, alignItems: "center", flexWrap: "wrap" }}>
          <div className="search"><Search size={15} /><input placeholder="Search toppers…" value={q} onChange={(e) => setQ(e.target.value)} /></div>
          <select className="sel" value={paper} onChange={(e) => setPaper(e.target.value)} aria-label="Paper">
            <option value="">Every paper</option>
            {PAPERS.map(([k, l]) => <option key={k} value={k}>{l}</option>)}
          </select>
          <button className="btn btn-primary" onClick={() => setUploading({})}><Upload size={16} />Upload a PDF copy</button>
        </div>
      </div>

      {list.err ? <div className="panel"><ErrorState message={list.err} onRetry={refresh} /></div>
        : list.loading && !items.length ? <SkeletonCards count={2} height={110} />
        : items.length === 0 ? (
          <div className="panel panel-pad" style={{ textAlign: "center", color: "var(--muted)" }}>
            {needle || paper ? "No copies match." : "No copies yet. Import the topper sheet, or upload a PDF."}
          </div>
        ) : (
          <>
            <div className="tbl-wrap">
              <table className="tbl">
                <thead><tr><th>Topper</th><th>Source</th><th>Answers</th><th>Kind</th><th>Free</th><th>Live</th><th></th></tr></thead>
                <tbody>
                  {items.map((c) => (
                    <tr key={c.id}>
                      <td>
                        <div style={{ fontWeight: 700 }}>{c.topper.name}</div>
                        <div style={{ fontSize: 12, color: "var(--muted)" }}>
                          {[c.topper.rank != null && `AIR ${c.topper.rank}`, c.topper.cseYear, c.topper.essayMarks != null && `Essay ${c.topper.essayMarks}/250`].filter(Boolean).join(" · ")}
                        </div>
                      </td>
                      <td>
                        <div>{c.source || "—"}</div>
                        <div style={{ fontSize: 12, color: "var(--muted)" }}>{[c.title, c.writtenYear].filter(Boolean).join(" · ")}</div>
                      </td>
                      <td className="nowrap">{c.answerCount}</td>
                      <td className="nowrap">{c.hosted ? `Hosted · ${c.pageCount} pages` : ""}{c.hosted && c.sourceUrl ? " + link" : ""}{!c.hosted && c.sourceUrl ? "Link" : ""}{!c.hosted && !c.sourceUrl ? "—" : ""}</td>
                      <td><input type="checkbox" checked={c.isFree} onChange={() => toggle(c, "isFree")} aria-label="Free copy" /></td>
                      <td><input type="checkbox" checked={c.isPublished} onChange={() => toggle(c, "isPublished")} aria-label="Published" /></td>
                      <td>
                        <div className="row-actions">
                          {c.hosted && <button className="btn-icon" title="Read" onClick={() => setViewing(c)}><Eye size={15} /></button>}
                          {!c.hosted && c.sourceUrl && <a className="btn-icon" title="Open the publisher's PDF" href={c.sourceUrl} target="_blank" rel="noopener noreferrer"><ExternalLink size={15} /></a>}
                          <button className="btn-icon" title="Edit" onClick={() => setEditing(c)}><Pencil size={15} /></button>
                          <button className="btn-icon danger" title="Delete" onClick={() => remove(c)}><Trash2 size={15} /></button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            {list.data && items.length < list.data.total && (
              <div style={{ display: "flex", justifyContent: "center", marginTop: 14 }}>
                <button className="btn btn-ghost" onClick={() => setLimit((n) => n + 40)} disabled={list.loading}>
                  Show more ({items.length} of {list.data.total})
                </button>
              </div>
            )}
          </>
        )}

      {uploading && (
        <UploadCopy
          attach={uploading.copy || null}
          toast={toast}
          onClose={() => setUploading(null)}
          onDone={(id) => { setUploading(null); refresh(); setEditing({ id }); }}
        />
      )}
      {editing && (
        <CopyEditor
          copyId={editing.id}
          toast={toast}
          askDelete={askDelete}
          onUploadPages={(copy) => setUploading({ copy })}
          onRead={(copy) => setViewing(copy)}
          onClose={() => { setEditing(null); refresh(); }}
        />
      )}
      {viewing && (
        <CopyViewer copyId={viewing.id} pageCount={viewing.pageCount} title={viewing.topper?.name || "Copy"}
                    subtitle={[viewing.source, viewing.writtenYear].filter(Boolean).join(" · ")} onClose={() => setViewing(null)} />
      )}
    </div>
  );
}

/* Upload a PDF and host it: hash, save the row, keep the original, then
   render and store every page. `attach` adds pages to an existing copy. */
function UploadCopy({ attach, toast, onClose, onDone }) {
  const fileRef = useRef(null);
  const cancelRef = useRef(false);
  const [file, setFile] = useState(null);
  const [f, setF] = useState({ name: "", rank: "", cseYear: "", essayMarks: "", source: "", title: "", writtenYear: "", isFree: false, isPublished: true });
  const [progress, setProgress] = useState(null);   // { label, done, total }
  const [err, setErr] = useState("");
  const set = (k, v) => setF((p) => ({ ...p, [k]: v }));
  const busy = !!progress;

  const go = async () => {
    if (!file) return setErr("Choose a PDF first.");
    if (!attach && !f.name.trim()) return setErr("The topper's name is required.");
    setErr("");
    cancelRef.current = false;
    let copyId = attach?.id || null;
    try {
      const R = await import("../lib/copyRender.js");
      setProgress({ label: "Checking the file" });
      const sha = await R.sha256Hex(file);
      const dup = await DB.copyBySha(sha);
      if (dup && dup.id !== copyId) throw new Error(`This PDF is already in the library${dup.topper ? ` (copy by ${dup.topper})` : ""}.`);
      const pdf = await R.openPdf(file);

      if (!copyId) {
        setProgress({ label: "Saving the copy" });
        const topperId = await DB.findOrCreateTopper({
          name: f.name, rank: f.rank === "" ? null : Number(f.rank), cseYear: f.cseYear === "" ? null : Number(f.cseYear),
          essayMarks: f.essayMarks === "" ? null : Number(f.essayMarks),
        });
        copyId = await DB.createCopy({
          topperId, source: f.source.trim(), title: f.title.trim() || file.name.replace(/\.pdf$/i, ""), writtenYear: f.writtenYear,
          sha256: sha, isFree: f.isFree, isPublished: false,   // published at the end, once every page is in
        });
      }

      setProgress({ label: "Storing the original PDF" });
      let pdfPath = null;
      try { pdfPath = await DB.uploadCopyPdf(copyId, file); }
      catch (e) { console.warn("original PDF not stored", e); toast("The original PDF was too large to keep; the pages are still hosted.", "err"); }

      const total = pdf.numPages;
      for (let n = 1; n <= total; n++) {
        if (cancelRef.current) throw new Error("Stopped. The pages done so far are kept; upload again to finish.");
        setProgress({ label: `Rendering page ${n} of ${total}`, done: n - 1, total });
        const blob = await R.renderPage(pdf, n);
        await DB.uploadCopyPage(copyId, n, blob);
      }
      await DB.updateCopy(copyId, {
        pageCount: total, hosted: true, sha256: sha, pdfPath,
        ...(attach ? {} : { isPublished: f.isPublished }),
      });
      setProgress({ label: "Done", done: total, total });
      toast(`Hosted ${total} pages`);
      onDone(copyId);
    } catch (e) {
      console.error(e);
      setErr(e?.message || "The upload stopped.");
      setProgress(null);
    }
  };

  return (
    <Modal title={attach ? `Host pages for ${attach.topper?.name || "this copy"}` : "Upload a PDF copy"} onClose={busy ? () => {} : onClose} wide
           footer={busy
             ? <button className="btn btn-ghost" onClick={() => { cancelRef.current = true; }}>Stop after this page</button>
             : <><button className="btn btn-ghost" onClick={onClose}>Cancel</button><button className="btn btn-primary" onClick={go}><Upload size={16} />Upload and render</button></>}>
      {err && <div className="form-err"><AlertCircle size={16} />{err}</div>}
      <Field label="PDF" req hint="Rendered page by page in this browser to images 1240 px wide. A 30-page scan takes a minute or two.">
        <div style={{ display: "flex", gap: 10, alignItems: "center", flexWrap: "wrap" }}>
          <button type="button" className="btn btn-ghost btn-sm" onClick={() => fileRef.current?.click()} disabled={busy}><Upload size={15} />{file ? "Choose another" : "Choose PDF"}</button>
          <input ref={fileRef} type="file" accept="application/pdf,.pdf" style={{ display: "none" }} onChange={(e) => setFile(e.target.files?.[0] || null)} />
          {file && <span style={{ fontSize: 13 }}>{file.name} · {(file.size / 1024 / 1024).toFixed(1)} MB</span>}
        </div>
      </Field>
      {!attach && (
        <>
          <div className="field-row">
            <Field label="Topper" req><input className="inp" value={f.name} onChange={(e) => set("name", e.target.value)} placeholder="Name as on the result list" /></Field>
            <Field label="Source" hint="The coaching or publisher, e.g. Vision IAS"><input className="inp" value={f.source} onChange={(e) => set("source", e.target.value)} /></Field>
          </div>
          <div className="field-row">
            <Field label="AIR"><input className="inp" type="number" min="1" value={f.rank} onChange={(e) => set("rank", e.target.value)} /></Field>
            <Field label="CSE year of that rank"><input className="inp" type="number" min="2000" value={f.cseYear} onChange={(e) => set("cseYear", e.target.value)} /></Field>
          </div>
          <div className="field-row">
            <Field label="UPSC Essay marks (/250)" hint="The topper's real Essay paper score, if known. Students are told it is not a mark for this copy.">
              <input className="inp" type="number" min="0" max="250" value={f.essayMarks} onChange={(e) => set("essayMarks", e.target.value)} />
            </Field>
            <Field label="Year written"><input className="inp" type="number" min="2000" value={f.writtenYear} onChange={(e) => set("writtenYear", e.target.value)} /></Field>
          </div>
          <Field label="Title" hint="Defaults to the file name."><input className="inp" value={f.title} onChange={(e) => set("title", e.target.value)} /></Field>
          <div style={{ display: "flex", gap: 18, flexWrap: "wrap" }}>
            <label style={{ fontSize: 13.5 }}><input type="checkbox" checked={f.isFree} onChange={(e) => set("isFree", e.target.checked)} /> Free for every student</label>
            <label style={{ fontSize: 13.5 }}><input type="checkbox" checked={f.isPublished} onChange={(e) => set("isPublished", e.target.checked)} /> Live once the pages are in</label>
          </div>
        </>
      )}
      {progress && (
        <div className="ma-steps">
          <div><b>{progress.label}</b></div>
          {progress.total ? <div className="ma-bar"><span style={{ width: `${Math.round((progress.done / progress.total) * 100)}%` }} /></div> : null}
        </div>
      )}
    </Modal>
  );
}

function CopyEditor({ copyId, toast, askDelete, onUploadPages, onRead, onClose }) {
  const [reload, setReload] = useState(0);
  const copyRow = useLoad(() => DB.adminCopy(copyId), `copy|${copyId}|${reload}`);
  const copy = copyRow.data;
  const answers = useLoad(() => DB.copyAnswers(copyId), `${copyId}|${reload}`);
  const pyqs = useLoad(() => DB.essayPyqs({ includeDrafts: true }), "pyqs");
  const [form, setForm] = useState(null);
  const [answer, setAnswer] = useState(null);   // the answer being edited, or {} for new
  const [picking, setPicking] = useState(false);
  const refresh = () => setReload((n) => n + 1);

  // The form starts from the copy once it has loaded, and stays the admin's after that.
  const f = form || (copy && {
    source: copy.source, title: copy.title, writtenYear: num(copy.writtenYear), sourceUrl: copy.sourceUrl,
    isFree: copy.isFree, isPublished: copy.isPublished,
    name: copy.topper.name, rank: num(copy.topper.rank), cseYear: num(copy.topper.cseYear), essayMarks: num(copy.topper.essayMarks),
  });
  const set = (k, v) => setForm((p) => ({ ...(p || f), [k]: v }));

  const saveCopy = async () => {
    try {
      await DB.updateCopy(copyId, {
        source: f.source.trim(), title: f.title.trim(), writtenYear: f.writtenYear === "" ? "" : Number(f.writtenYear),
        sourceUrl: f.sourceUrl.trim() ? DB.copyLinkAt(f.sourceUrl.trim()) : "", isFree: f.isFree, isPublished: f.isPublished,
      });
      await DB.updateTopper(copy.topper.id, { name: f.name, rank: f.rank, cseYear: f.cseYear, essayMarks: f.essayMarks });
      toast("Copy saved");
      setForm(null);
      refresh();
    } catch (e) { console.error(e); toast(e?.message || "Couldn't save", "err"); }
  };

  const removeAnswer = (a) => askDelete("Delete this answer and its PYQ links?", async () => {
    try { await DB.deleteAnswer(a.id); toast("Answer deleted"); refresh(); }
    catch (e) { console.error(e); toast(e?.message || "Couldn't delete", "err"); }
  });

  const pyqById = useMemo(() => new Map((pyqs.data || []).map((p) => [p.id, p])), [pyqs.data]);

  return (
    <Modal title={copy ? `Copy · ${copy.topper.name}` : "Copy"} onClose={onClose} wide
           footer={<button className="btn btn-ghost" onClick={onClose}>Close</button>}>
      {copyRow.err ? <ErrorState message={copyRow.err} onRetry={refresh} />
        : !copy ? <SkeletonCards count={1} height={120} />
        : (
          <div className="ma-split">
            <div>
              <Field label="Topper"><input className="inp" value={f.name} onChange={(e) => set("name", e.target.value)} /></Field>
              <div className="field-row">
                <Field label="AIR"><input className="inp" type="number" value={f.rank} onChange={(e) => set("rank", e.target.value)} /></Field>
                <Field label="CSE year"><input className="inp" type="number" value={f.cseYear} onChange={(e) => set("cseYear", e.target.value)} /></Field>
              </div>
              <Field label="UPSC Essay marks (/250)"><input className="inp" type="number" value={f.essayMarks} onChange={(e) => set("essayMarks", e.target.value)} /></Field>
              <Field label="Source"><input className="inp" value={f.source} onChange={(e) => set("source", e.target.value)} /></Field>
              <Field label="Title"><input className="inp" value={f.title} onChange={(e) => set("title", e.target.value)} /></Field>
              <Field label="Year written"><input className="inp" type="number" value={f.writtenYear} onChange={(e) => set("writtenYear", e.target.value)} /></Field>
              <Field label="Publisher's PDF link" hint="Students open it at each answer's page (#page=N).">
                <input className="inp" value={f.sourceUrl} onChange={(e) => set("sourceUrl", e.target.value)} placeholder="https://…" />
              </Field>
              <div style={{ display: "flex", gap: 16, flexWrap: "wrap", marginBottom: 14 }}>
                <label style={{ fontSize: 13.5 }}><input type="checkbox" checked={f.isFree} onChange={(e) => set("isFree", e.target.checked)} /> Free</label>
                <label style={{ fontSize: 13.5 }}><input type="checkbox" checked={f.isPublished} onChange={(e) => set("isPublished", e.target.checked)} /> Live</label>
              </div>
              <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
                <button className="btn btn-primary btn-sm" onClick={saveCopy} disabled={!form}><Save size={15} />Save copy</button>
                <button className="btn btn-ghost btn-sm" onClick={() => onUploadPages(copy)}><Upload size={15} />{copy.hosted ? "Replace pages" : "Host pages from a PDF"}</button>
                {copy.hosted && <button className="btn btn-ghost btn-sm" onClick={() => onRead(copy)}><Eye size={15} />Read</button>}
              </div>
            </div>

            <div>
              <div className="sec-head" style={{ marginBottom: 10 }}>
                <div>
                  <h2>{answers.data ? `${answers.data.length} answers` : "Answers"}</h2>
                  <div className="note">Where each answer starts, and which essay PYQs it answers</div>
                </div>
                <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
                  {answers.data?.length > 0 && (
                    <button className="btn btn-ghost btn-sm" onClick={() => setPicking(true)} title="Open the copy's PDF from this computer and click where each answer starts">
                      <FileText size={15} />Find start pages
                    </button>
                  )}
                  <button className="btn btn-ghost btn-sm" onClick={() => setAnswer({})}><Plus size={15} />Add answer</button>
                </div>
              </div>
              {answers.err ? <ErrorState compact message={answers.err} onRetry={refresh} />
                : answers.loading ? <SkeletonCards count={2} height={70} />
                : answers.data.length === 0 ? <div style={{ fontSize: 13, color: "var(--muted)" }}>No answers marked in this copy yet.</div>
                : answers.data.map((a) => (
                  <div className="ma-ans" key={a.id}>
                    <div className="ma-ans-top">
                      <div className="ma-ans-q">{a.question}</div>
                      <button className="btn-icon" title="Edit" onClick={() => setAnswer(a)}><Pencil size={14} /></button>
                      <button className="btn-icon danger" title="Delete" onClick={() => removeAnswer(a)}><Trash2 size={14} /></button>
                    </div>
                    <div className="ma-ans-meta">
                      {PAPER_LABEL[a.paper]}{a.paperLabel ? ` · ${a.paperLabel}` : ""}
                      {a.startPage !== "" ? ` · pages ${a.startPage}${a.endPage !== "" ? `–${a.endPage}` : ""}` : " · no page marked"}
                      {a.words ? ` · ${a.words.toLocaleString("en-IN")} words` : " · no text"}
                    </div>
                    {a.paper === "essay" && (
                      <div className="ma-chips" style={{ marginTop: 8 }}>
                        {a.links.length === 0 ? <span style={{ fontSize: 12, color: "var(--muted)" }}>Not linked to any PYQ yet</span>
                          : a.links.map((l) => {
                            const p = pyqById.get(l.pyqId);
                            return <span key={l.pyqId} className="ma-chip"><span className={"ma-kind " + l.kind}>{l.kind}</span><span className="t">{p ? `${p.topic} (${p.year})` : "PYQ"}</span></span>;
                          })}
                      </div>
                    )}
                  </div>
                ))}
            </div>
          </div>
        )}

      {answer && (
        <AnswerForm
          copyId={copyId}
          initial={answer}
          pyqs={pyqs.data || []}
          toast={toast}
          onClose={() => setAnswer(null)}
          onSaved={() => { setAnswer(null); refresh(); }}
        />
      )}
      {picking && copy && answers.data && (
        <PagePicker copy={copy} answers={answers.data} toast={toast}
                    onClose={() => setPicking(false)} onSaved={() => { setPicking(false); refresh(); }} />
      )}
    </Modal>
  );
}

function AnswerForm({ copyId, initial, pyqs, toast, onClose, onSaved }) {
  const [a, setA] = useState({
    paper: initial.paper || "essay", paperLabel: initial.paperLabel || "", question: initial.question || "",
    startPage: num(initial.startPage), endPage: num(initial.endPage),
  });
  const [links, setLinks] = useState(initial.links || []);
  // The essay's text: loaded for an existing answer, the admin's once edited.
  const textLoad = useLoad(() => (initial.id ? DB.essayText(initial.id) : Promise.resolve(null)), `text|${initial.id || "new"}`);
  const [text, setText] = useState(null);
  const textValue = text ?? textLoad.data?.body ?? "";
  const [find, setFind] = useState("");
  const [err, setErr] = useState("");
  const set = (k, v) => setA((p) => ({ ...p, [k]: v }));

  const suggestions = useMemo(() => {
    const linked = new Set(links.map((l) => l.pyqId));
    const needle = find.trim().toLowerCase();
    return pyqs
      .filter((p) => !linked.has(p.id))
      .map((p) => ({ p, score: needle ? (p.topic.toLowerCase().includes(needle) ? 1 : 0) : overlap(a.question, p.topic) }))
      .filter((x) => x.score > 0)
      .sort((x, y) => y.score - x.score || y.p.year - x.p.year)
      .slice(0, 8);
  }, [pyqs, a.question, find, links]);

  const add = (p, kind) => setLinks((ls) => [...ls, { pyqId: p.id, kind, confidence: null }]);
  const flip = (id) => setLinks((ls) => ls.map((l) => (l.pyqId === id ? { ...l, kind: l.kind === "exact" ? "related" : "exact" } : l)));
  const drop = (id) => setLinks((ls) => ls.filter((l) => l.pyqId !== id));
  const byId = new Map(pyqs.map((p) => [p.id, p]));

  const save = async () => {
    if (!a.question.trim()) return setErr("The question is required.");
    if (a.startPage !== "" && a.endPage !== "" && Number(a.endPage) < Number(a.startPage)) return setErr("The end page is before the start page.");
    setErr("");
    try {
      const id = await DB.upsertAnswer({ ...a, id: initial.id, copyId });
      if (a.paper === "essay") await DB.setAnswerLinks(id, links);
      if (text !== null) {
        const body = cleanBody(text);
        const had = !!textLoad.data;
        if (body || had) await DB.saveEssayText(id, body, { isNew: !had });
      }
      toast("Answer saved");
      onSaved();
    } catch (e) { console.error(e); setErr(e?.message || "Couldn't save"); }
  };

  return (
    <Modal title={initial.id ? "Edit answer" : "Add answer"} onClose={onClose} wide
           footer={<><button className="btn btn-ghost" onClick={onClose}>Cancel</button><button className="btn btn-primary" onClick={save}><Save size={16} />Save answer</button></>}>
      {err && <div className="form-err"><AlertCircle size={16} />{err}</div>}
      <div className="field-row">
        <Field label="Paper">
          <select className="sel" style={{ width: "100%" }} value={a.paper} onChange={(e) => set("paper", e.target.value)}>
            {PAPERS.map(([k, l]) => <option key={k} value={k}>{l}</option>)}
          </select>
        </Field>
        {a.paper === "optional" && <Field label="Optional subject"><input className="inp" value={a.paperLabel} onChange={(e) => set("paperLabel", e.target.value)} /></Field>}
      </div>
      <Field label="Question, as written in the copy" req>
        <textarea className="inp" rows={2} value={a.question} onChange={(e) => set("question", e.target.value)} />
      </Field>
      <Field label={`Essay text${textValue.trim() ? ` · ${wordCount(cleanBody(textValue)).toLocaleString("en-IN")} words` : ""}`}
             hint="What students read under Read as text. Split paragraphs with a blank line; leave it empty for no text.">
        <textarea className="inp" rows={8} value={textValue} disabled={textLoad.loading}
                  onChange={(e) => setText(e.target.value)} placeholder={textLoad.loading ? "Loading…" : "No text yet"}
                  style={{ fontFamily: "Georgia, serif", fontSize: 14, lineHeight: 1.6 }} />
      </Field>
      <div className="field-row">
        <Field label="Starts on page" hint="The PDF page, not the booklet's printed number."><input className="inp" type="number" min="1" value={a.startPage} onChange={(e) => set("startPage", e.target.value)} /></Field>
        <Field label="Ends on page"><input className="inp" type="number" min="1" value={a.endPage} onChange={(e) => set("endPage", e.target.value)} /></Field>
      </div>

      {a.paper === "essay" && (
        <>
          <Field label="Linked essay PYQs" hint="Exact: the same topic. Related: a different topic a student could reuse this essay for. Click a tag to switch it.">
            <div className="ma-chips">
              {links.length === 0 ? <span style={{ fontSize: 12.5, color: "var(--muted)" }}>None yet</span> : links.map((l) => {
                const p = byId.get(l.pyqId);
                return (
                  <span key={l.pyqId} className="ma-chip">
                    <button type="button" className={"ma-kind " + l.kind} onClick={() => flip(l.pyqId)}>{l.kind}</button>
                    <span className="t">{p ? `${p.topic} (${p.year})` : "PYQ"}</span>
                    <button type="button" onClick={() => drop(l.pyqId)} aria-label="Remove link"><X size={13} /></button>
                  </span>
                );
              })}
            </div>
          </Field>
          <Field label={find ? "Search results" : "Suggested from the question's wording"}>
            <div className="search" style={{ marginBottom: 6 }}><Search size={15} /><input placeholder="Search PYQs…" value={find} onChange={(e) => setFind(e.target.value)} /></div>
            <div className="ma-sugg">
              {suggestions.length === 0 ? <span style={{ fontSize: 12.5, color: "var(--muted)" }}>{find ? "No PYQ matches." : "No suggestion; search instead."}</span>
                : suggestions.map(({ p, score }) => (
                  <div key={p.id} className="ma-sugg-row">
                    <span className="t">{p.topic} <span style={{ color: "var(--muted)" }}>({p.year})</span></span>
                    {!find && <span className="s">{Math.round(score * 100)}%</span>}
                    <button type="button" className="btn btn-ghost btn-sm" onClick={() => add(p, "exact")}>Exact</button>
                    <button type="button" className="btn btn-ghost btn-sm" onClick={() => add(p, "related")}>Related</button>
                  </div>
                ))}
            </div>
          </Field>
        </>
      )}
    </Modal>
  );
}

/* ========================================================== PYQS & THEMES == */

function PyqsPanel({ toast, askDelete }) {
  const [reload, setReload] = useState(0);
  const themes = useLoad(() => DB.essayThemes(), `themes|${reload}`);
  const pyqs = useLoad(() => DB.essayPyqs({ includeDrafts: true }), `pyqs|${reload}`);
  const [q, setQ] = useState("");
  const [year, setYear] = useState("");
  const [editPyq, setEditPyq] = useState(null);
  const [editTheme, setEditTheme] = useState(null);
  const refresh = useCallback(() => setReload((n) => n + 1), []);

  const themeById = useMemo(() => new Map((themes.data || []).map((t) => [t.id, t])), [themes.data]);
  const counts = useMemo(() => {
    const m = new Map();
    (pyqs.data || []).forEach((p) => p.themes.forEach((t) => m.set(t.id, (m.get(t.id) || 0) + 1)));
    return m;
  }, [pyqs.data]);
  const years = useMemo(() => [...new Set((pyqs.data || []).map((p) => p.year))].sort((a, b) => b - a), [pyqs.data]);
  const needle = q.trim().toLowerCase();
  const shown = (pyqs.data || []).filter((p) => (!year || String(p.year) === year) && (!needle || p.topic.toLowerCase().includes(needle)));

  const removePyq = (p) => askDelete(`Delete "${p.topic}" (${p.year})? Its theme tags and essay links go with it.`, async () => {
    try { await DB.deleteEssayPyq(p.id); toast("PYQ deleted"); refresh(); }
    catch (e) { console.error(e); toast(e?.message || "Couldn't delete", "err"); }
  });
  const removeTheme = (t) => askDelete(`Delete the theme "${t.name}"? PYQs keep their other themes.`, async () => {
    try { await DB.deleteEssayTheme(t.id); toast("Theme deleted"); refresh(); }
    catch (e) { console.error(e); toast(e?.message || "Couldn't delete", "err"); }
  });

  if (themes.err || pyqs.err) return <div className="panel"><ErrorState message={themes.err || pyqs.err} onRetry={refresh} /></div>;
  if (themes.loading || pyqs.loading) return <SkeletonCards count={2} height={120} />;

  return (
    <div className="ma-stack">
      <div className="panel panel-pad">
        <div className="sec-head" style={{ marginBottom: 10 }}>
          <div><h2>{themes.data.length} themes</h2><div className="note">What students browse essays by</div></div>
          <button className="btn btn-ghost btn-sm" onClick={() => setEditTheme({})}><Plus size={15} />Add</button>
        </div>
        {themes.data.length === 0 ? <div style={{ fontSize: 13, color: "var(--muted)" }}>Import the PYQ sheet and its categories become themes.</div>
          : <div className="ma-theme-grid">{themes.data.map((t) => (
            <div className="row-item" key={t.id}>
              <div style={{ flex: 1, minWidth: 0 }}>
                <div style={{ fontWeight: 700, fontSize: 13.5 }}>{t.name}</div>
                <div style={{ fontSize: 12, color: t.nameHi ? "var(--muted)" : "var(--red)" }}>{t.nameHi || "No Hindi name yet"} · {counts.get(t.id) || 0} PYQs</div>
              </div>
              <button className="btn-icon" title="Edit" onClick={() => setEditTheme(t)}><Pencil size={14} /></button>
              <button className="btn-icon danger" title="Delete" onClick={() => removeTheme(t)}><Trash2 size={14} /></button>
            </div>
          ))}</div>}
      </div>

      <div>
        <div className="sec-head">
          <div><h2>{shown.length} essay PYQs</h2><div className="note">UPSC's topics; the first theme is the main one</div></div>
          <div style={{ display: "flex", gap: 8, alignItems: "center", flexWrap: "wrap" }}>
            <div className="search"><Search size={15} /><input placeholder="Search topics…" value={q} onChange={(e) => setQ(e.target.value)} /></div>
            <select className="sel" value={year} onChange={(e) => setYear(e.target.value)} aria-label="Year">
              <option value="">Every year</option>
              {years.map((y) => <option key={y} value={y}>{y}</option>)}
            </select>
            <button className="btn btn-primary" onClick={() => setEditPyq({})}><Plus size={16} />Add PYQ</button>
          </div>
        </div>
        {shown.length === 0 ? (
          <div className="panel panel-pad" style={{ textAlign: "center", color: "var(--muted)" }}>
            {pyqs.data.length ? "No PYQ matches." : "No essay PYQs yet. Import the PYQ sheet, or add one."}
          </div>
        ) : (
          <div className="tbl-wrap">
            <table className="tbl">
              <thead><tr><th>Year</th><th>Topic</th><th>Themes</th><th>Essays</th><th>Live</th><th></th></tr></thead>
              <tbody>
                {shown.map((p) => (
                  <tr key={p.id}>
                    <td className="nowrap">{p.year}</td>
                    <td>
                      <div>{p.topic}</div>
                      <div style={{ fontSize: 12, color: p.topicHi ? "var(--muted)" : "var(--red)" }}>{p.topicHi || "No Hindi yet"}</div>
                    </td>
                    <td>{p.themes.map((t) => themeById.get(t.id)).filter(Boolean).map((t, i) =>
                      <div key={t.id} style={{ fontSize: 12.5, fontWeight: i === 0 ? 700 : 400 }}>{t.name}{p.themes[i].confidence != null ? ` (${p.themes[i].confidence})` : ""}</div>)}</td>
                    <td className="nowrap">{p.essayCount}</td>
                    <td>{p.isPublished ? "Yes" : "No"}</td>
                    <td>
                      <div className="row-actions">
                        <button className="btn-icon" title="Edit" onClick={() => setEditPyq(p)}><Pencil size={15} /></button>
                        <button className="btn-icon danger" title="Delete" onClick={() => removePyq(p)}><Trash2 size={15} /></button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

      {editPyq && <PyqForm initial={editPyq} themes={themes.data} toast={toast} onClose={() => setEditPyq(null)} onSaved={() => { setEditPyq(null); refresh(); }} />}
      {editTheme && <ThemeForm initial={editTheme} toast={toast} onClose={() => setEditTheme(null)} onSaved={() => { setEditTheme(null); refresh(); }} />}
    </div>
  );
}

function PyqForm({ initial, themes, toast, onClose, onSaved }) {
  const [f, setF] = useState({
    year: num(initial.year) || String(new Date().getFullYear()), section: initial.section || "", qNo: num(initial.qNo),
    topic: initial.topic || "", topicHi: initial.topicHi || "", isPublished: initial.isPublished !== false,
  });
  const [tags, setTags] = useState(initial.themes || []);
  const [err, setErr] = useState("");
  const set = (k, v) => setF((p) => ({ ...p, [k]: v }));
  const used = new Set(tags.map((t) => t.id));

  const save = async () => {
    const y = Number(f.year);
    if (!Number.isInteger(y) || y < 1990 || y > 2100) return setErr("Enter the year of the paper.");
    if (!f.topic.trim()) return setErr("The topic is required.");
    setErr("");
    try {
      await DB.upsertEssayPyq({ ...f, id: initial.id, themes: tags });
      toast("PYQ saved");
      onSaved();
    } catch (e) { console.error(e); setErr(e?.message || "Couldn't save"); }
  };

  return (
    <Modal title={initial.id ? "Edit essay PYQ" : "Add essay PYQ"} onClose={onClose} wide
           footer={<><button className="btn btn-ghost" onClick={onClose}>Cancel</button><button className="btn btn-primary" onClick={save}><Save size={16} />Save</button></>}>
      {err && <div className="form-err"><AlertCircle size={16} />{err}</div>}
      <div className="field-row">
        <Field label="Year" req><input className="inp" type="number" value={f.year} onChange={(e) => set("year", e.target.value)} /></Field>
        <Field label="Section" hint="A or B, where the paper has them"><input className="inp" value={f.section} onChange={(e) => set("section", e.target.value)} /></Field>
      </div>
      <Field label="Topic (English)" req><textarea className="inp" rows={2} value={f.topic} onChange={(e) => set("topic", e.target.value)} /></Field>
      <Field label="Topic (Hindi)" hint="UPSC's own Hindi wording where available. Students in Hindi mode see this; without it they see the English.">
        <textarea className="inp" rows={2} value={f.topicHi} onChange={(e) => set("topicHi", e.target.value)} />
      </Field>
      <Field label="Themes" hint="Highest confidence first; the first is the main theme, the rest show as 'also under'.">
        {tags.map((t) => (
          <div key={t.id} style={{ display: "flex", gap: 8, alignItems: "center", marginBottom: 6 }}>
            <span style={{ flex: 1, fontSize: 13.5 }}>{themes.find((x) => x.id === t.id)?.name || "Theme"}</span>
            <input className="inp" style={{ width: 90 }} type="number" min="0" max="100" value={t.confidence ?? ""} aria-label="Confidence"
                   onChange={(e) => setTags((ts) => ts.map((x) => (x.id === t.id ? { ...x, confidence: e.target.value === "" ? null : Number(e.target.value) } : x)))} />
            <button type="button" className="btn-icon danger" onClick={() => setTags((ts) => ts.filter((x) => x.id !== t.id))} aria-label="Remove theme"><X size={14} /></button>
          </div>
        ))}
        <select className="sel" style={{ width: "100%" }} value="" onChange={(e) => e.target.value && setTags((ts) => [...ts, { id: e.target.value, confidence: null }])}>
          <option value="">Add a theme…</option>
          {themes.filter((t) => !used.has(t.id)).map((t) => <option key={t.id} value={t.id}>{t.name}</option>)}
        </select>
      </Field>
      <label style={{ fontSize: 13.5 }}><input type="checkbox" checked={f.isPublished} onChange={(e) => set("isPublished", e.target.checked)} /> Live</label>
    </Modal>
  );
}

function ThemeForm({ initial, toast, onClose, onSaved }) {
  const [f, setF] = useState({ name: initial.name || "", nameHi: initial.nameHi || "", sortOrder: num(initial.sortOrder) || "0" });
  const [err, setErr] = useState("");
  const save = async () => {
    if (!f.name.trim()) return setErr("The theme needs a name.");
    setErr("");
    try {
      await DB.upsertEssayTheme({ ...f, id: initial.id, slug: initial.slug });
      toast("Theme saved");
      onSaved();
    } catch (e) { console.error(e); setErr(e?.message || "Couldn't save"); }
  };
  return (
    <Modal title={initial.id ? "Edit theme" : "Add theme"} onClose={onClose}
           footer={<><button className="btn btn-ghost" onClick={onClose}>Cancel</button><button className="btn btn-primary" onClick={save}><Save size={16} />Save</button></>}>
      {err && <div className="form-err"><AlertCircle size={16} />{err}</div>}
      <Field label="Name" req><input className="inp" value={f.name} onChange={(e) => setF((p) => ({ ...p, name: e.target.value }))} /></Field>
      <Field label="Hindi name" hint="Shown to students in Hindi mode; without it they see the English name.">
        <input className="inp" value={f.nameHi} onChange={(e) => setF((p) => ({ ...p, nameHi: e.target.value }))} />
      </Field>
      <Field label="Display order" hint="Lower numbers first; ties sort by name."><input className="inp" type="number" value={f.sortOrder} onChange={(e) => setF((p) => ({ ...p, sortOrder: e.target.value }))} /></Field>
      <div style={{ fontSize: 12.5, color: "var(--muted)" }}><BookOpen size={13} style={{ verticalAlign: -2 }} /> Students see themes with at least one PYQ, busiest first.</div>
    </Modal>
  );
}

/* ============================================================ START PAGES == */
/* Mark where each answer starts and ends by looking at the copy itself. The
   admin picks the copy's PDF from this computer; pages are drawn right here
   (nothing is uploaded), so this works for link copies we do not host. */

const firstLine = (body) => String(body || "").split(/\n+/).map((s) => s.trim()).find(Boolean)?.slice(0, 180) || "";

function PagePicker({ copy, answers, toast, onClose, onSaved }) {
  const fileRef = useRef(null);
  const urlsRef = useRef([]);
  const cancelRef = useRef(false);
  const [pages, setPages] = useState([]);   // [{ n, url }]
  const [total, setTotal] = useState(0);
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState("");
  const [warn, setWarn] = useState("");
  const [size, setSize] = useState(200);
  const [saving, setSaving] = useState(false);
  const orig = useMemo(() => Object.fromEntries(answers.map((a) => [a.id, {
    start: a.startPage === "" || a.startPage == null ? null : Number(a.startPage),
    end: a.endPage === "" || a.endPage == null ? null : Number(a.endPage),
  }])), [answers]);
  const [marks, setMarks] = useState(orig);
  const [sel, setSel] = useState(() => (answers.find((a) => orig[a.id].start == null) || answers[0])?.id || null);
  const [step, setStep] = useState("start");
  const heads = useLoad(async () => {
    const list = await Promise.all(answers.map((a) => (a.words
      ? DB.essayText(a.id).then((x) => [a.id, firstLine(x?.body)], () => [a.id, ""])
      : Promise.resolve([a.id, ""]))));
    return Object.fromEntries(list);
  }, `heads|${answers.map((a) => a.id).join(",")}`);

  useEffect(() => {
    const urls = urlsRef;
    return () => {
      cancelRef.current = true;
      urls.current.forEach((u) => URL.revokeObjectURL(u));
    };
  }, []);

  const choose = async (file) => {
    if (!file) return;
    setErr(""); setWarn("");
    cancelRef.current = true;                     // stop a render still running
    urlsRef.current.forEach((u) => URL.revokeObjectURL(u));
    urlsRef.current = [];
    setPages([]);
    try {
      const R = await import("../lib/copyRender.js");
      const pdf = await R.openPdf(file);
      cancelRef.current = false;
      setTotal(pdf.numPages);
      if (copy.pageCount && copy.pageCount !== pdf.numPages) {
        setWarn(`This PDF has ${pdf.numPages} pages; the hosted copy has ${copy.pageCount}. Check it is the same copy.`);
      }
      setBusy(true);
      for (let n = 1; n <= pdf.numPages; n++) {
        if (cancelRef.current) break;
        const blob = await R.renderPage(pdf, n, { width: 520, quality: 0.7 });
        const url = URL.createObjectURL(blob);
        urlsRef.current.push(url);
        setPages((p) => [...p, { n, url }]);
      }
    } catch (e) {
      console.error(e);
      setErr(e?.message || "Couldn't open this PDF.");
    }
    setBusy(false);
  };

  const pick = (n) => {
    if (!sel) return;
    const cur = marks[sel] || { start: null, end: null };
    if (step === "start" || (cur.start != null && n < cur.start)) {
      setMarks((m) => ({ ...m, [sel]: { start: n, end: cur.end != null && cur.end >= n ? cur.end : null } }));
      setStep("end");
      return;
    }
    const next = { ...marks, [sel]: { ...cur, end: n } };
    setMarks(next);
    // On to the next answer: the next one still without a page, else simply
    // the next one, else an earlier one still without a page.
    const idx = answers.findIndex((a) => a.id === sel);
    const blank = (a) => next[a.id]?.start == null;
    const after = answers.slice(idx + 1).find(blank) || answers[idx + 1] || answers.slice(0, idx).find(blank);
    if (after) setSel(after.id);
    setStep("start");
  };

  const changed = answers.filter((a) => marks[a.id].start !== orig[a.id].start || marks[a.id].end !== orig[a.id].end);
  const save = async () => {
    setSaving(true);
    try {
      await DB.setAnswerPages(changed.map((a) => ({ id: a.id, startPage: marks[a.id].start ?? "", endPage: marks[a.id].end ?? "" })));
      toast(`Saved pages for ${changed.length} answer${changed.length === 1 ? "" : "s"}`);
      onSaved();
    } catch (e) { console.error(e); toast(e?.message || "Couldn't save", "err"); setSaving(false); }
  };

  const selIdx = answers.findIndex((a) => a.id === sel);
  const selM = sel ? marks[sel] : null;
  const badge = (n) => answers.flatMap((a, i) => {
    const m = marks[a.id];
    const out = [];
    if (m.start === n) out.push(<span key={`s${a.id}`} className="ma-pg-tag s">{i + 1} starts</span>);
    if (m.end === n) out.push(<span key={`e${a.id}`} className="ma-pg-tag e">{i + 1} ends</span>);
    return out;
  });

  return (
    <Modal title={`Start pages · ${copy.topper.name}`} onClose={saving ? () => {} : onClose} wide
           footer={<>
             <span style={{ marginRight: "auto", fontSize: 12.5, color: "var(--muted)" }}>
               {changed.length ? `${changed.length} answer${changed.length === 1 ? "" : "s"} changed` : "No changes yet"}
             </span>
             <button className="btn btn-ghost" onClick={onClose} disabled={saving}>Cancel</button>
             <button className="btn btn-primary" onClick={save} disabled={!changed.length || saving}><Save size={16} />Save pages</button>
           </>}>
      <style>{PICKER_CSS}</style>
      {err && <div className="form-err"><AlertCircle size={16} />{err}</div>}
      {warn && <div className="form-err" style={{ background: "var(--amb-bg)", color: "var(--ink)" }}><AlertCircle size={16} />{warn}</div>}
      <div className="ma-picker">
        <div className="ma-pick-side">
          <div style={{ display: "flex", gap: 8, alignItems: "center", flexWrap: "wrap", marginBottom: 10 }}>
            <button type="button" className="btn btn-ghost btn-sm" onClick={() => fileRef.current?.click()}>
              <Upload size={15} />{pages.length ? "Choose another PDF" : "Choose the copy's PDF"}
            </button>
            <input ref={fileRef} type="file" accept="application/pdf,.pdf" style={{ display: "none" }}
                   onChange={(e) => { choose(e.target.files?.[0] || null); e.target.value = ""; }} />
          </div>
          <div className="ma-pick-help">
            {sel
              ? <>Answer {selIdx + 1}: click the page where it <b>{step === "start" ? "starts" : "ends"}</b>.</>
              : "Pick an answer below."}
            {" "}The PDF stays on this computer.
          </div>
          {answers.map((a, i) => {
            const m = marks[a.id];
            return (
              <button key={a.id} className={"ma-pick-ans" + (sel === a.id ? " on" : "")} onClick={() => { setSel(a.id); setStep("start"); }}>
                <span className="n">{i + 1}</span>
                <span style={{ flex: 1, minWidth: 0 }}>
                  <span className="q">{a.question}</span>
                  {heads.data?.[a.id] && <span className="h">Text begins: “{heads.data[a.id]}”</span>}
                  <span className="p">{m.start != null ? `pages ${m.start}${m.end != null ? `–${m.end}` : "–?"}` : "no page yet"}</span>
                </span>
              </button>
            );
          })}
          {sel && selM?.start != null && (
            <button className="btn btn-ghost btn-sm" style={{ marginTop: 8 }} onClick={() => { setMarks((m) => ({ ...m, [sel]: { start: null, end: null } })); setStep("start"); }}>
              Clear answer {selIdx + 1}
            </button>
          )}
        </div>
        <div style={{ minWidth: 0 }}>
          {pages.length > 0 && (
            <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 10, fontSize: 12.5, color: "var(--muted)" }}>
              <span>{busy ? `Drawing page ${pages.length} of ${total}…` : `${total} pages`}</span>
              <span style={{ marginLeft: "auto" }}>Size</span>
              {[[150, "S"], [200, "M"], [300, "L"]].map(([w, l]) => (
                <button key={w} className={"ma-tab" + (size === w ? " on" : "")} style={{ padding: "4px 10px" }} onClick={() => setSize(w)}>{l}</button>
              ))}
            </div>
          )}
          {pages.length === 0
            ? <div className="ma-pick-empty">{busy ? "Opening the PDF…" : "Choose the copy's PDF to see its pages here."}</div>
            : (
              <div className="ma-pages" style={{ gridTemplateColumns: `repeat(auto-fill, minmax(${size}px, 1fr))` }}>
                {pages.map(({ n, url }) => {
                  const inSel = selM && selM.start != null && n >= selM.start && n <= (selM.end ?? selM.start);
                  return (
                    <button key={n} className={"ma-page" + (inSel ? " in" : "")} onClick={() => pick(n)} title={`Page ${n}`}>
                      <img src={url} alt={`Page ${n}`} loading="lazy" />
                      <span className="pn">{n}</span>
                      <span className="tags">{badge(n)}</span>
                    </button>
                  );
                })}
              </div>
            )}
        </div>
      </div>
    </Modal>
  );
}

const PICKER_CSS = `
.overlay .modal.wide:has(.ma-picker){max-width:min(1400px,calc(100vw - 32px));width:calc(100vw - 32px)}
.ma-picker{display:grid;grid-template-columns:300px minmax(0,1fr);gap:18px;align-items:start}
.ma-pick-side{position:sticky;top:0}
.ma-pick-help{font-size:12.5px;color:var(--muted);line-height:1.5;margin-bottom:10px}
.ma-pick-ans{display:flex;gap:10px;width:100%;text-align:left;border:1.5px solid var(--line);border-radius:10px;padding:9px 10px;margin-bottom:8px;background:var(--card);color:var(--ink)}
.ma-pick-ans.on{border-color:var(--gold-2);background:var(--amb-bg)}
.ma-pick-ans .n{font-weight:800;color:var(--gold-2);min-width:16px}
.ma-pick-ans .q{display:block;font-size:13px;font-weight:700;line-height:1.35}
.ma-pick-ans .h{display:block;font-size:11.5px;color:var(--muted);margin-top:3px;line-height:1.4}
.ma-pick-ans .p{display:block;font-size:11.5px;font-weight:700;color:var(--navy);margin-top:4px}
.ma-pick-empty{border:1.5px dashed var(--line);border-radius:12px;padding:40px 16px;text-align:center;color:var(--muted);font-size:13.5px}
.ma-pages{display:grid;gap:10px}
.ma-page{position:relative;border:2px solid var(--line);border-radius:8px;overflow:hidden;background:#ffffff;padding:0;cursor:pointer}
.ma-page:hover{border-color:var(--gold-2)}
.ma-page.in{border-color:var(--navy);box-shadow:0 0 0 2px var(--navy)}
.ma-page img{display:block;width:100%;height:auto}
.ma-page .pn{position:absolute;top:6px;left:6px;background:rgba(0,0,0,.65);color:#ffffff;font-size:11px;font-weight:800;border-radius:6px;padding:2px 6px}
.ma-page .tags{position:absolute;bottom:6px;left:6px;right:6px;display:flex;flex-wrap:wrap;gap:4px}
.ma-pg-tag{font-size:10.5px;font-weight:800;border-radius:6px;padding:2px 6px;color:#ffffff}
.ma-pg-tag.s{background:#1f7a4c}
.ma-pg-tag.e{background:#9b2c2c}
@media(max-width:900px){.ma-picker{grid-template-columns:minmax(0,1fr)}.ma-pick-side{position:static}}
`;

/* ================================================================== WIKI == */
/* Review the drafted wiki: each passage is verbatim from a topper's essay,
   with our note on why it works and the PYQs it suits. Students see only
   published ones. */

const SN_KINDS = ["opening", "closing", "quote", "anecdote", "example", "statistic"];

function WikiPanel({ toast, askDelete }) {
  const [status, setStatus] = useState("draft");
  const [kind, setKind] = useState("");
  const [q, setQ] = useState("");
  const [needle, setNeedle] = useState("");
  const [offset, setOffset] = useState(0);
  const [reload, setReload] = useState(0);
  const refresh = () => setReload((n) => n + 1);
  useEffect(() => { const id = setTimeout(() => { setNeedle(q.trim()); setOffset(0); }, 300); return () => clearTimeout(id); }, [q]);
  const stats = useLoad(() => DB.adminStudyStats(), `stats|${reload}`);
  const list = useLoad(() => DB.adminSnippets({ status, kind, q: needle, offset, limit: 30 }), `${status}|${kind}|${needle}|${offset}|${reload}`);
  const pyqs = useLoad(() => DB.essayPyqs({ includeDrafts: true }), "pyqs");
  const pyqById = useMemo(() => new Map((pyqs.data || []).map((p) => [p.id, p])), [pyqs.data]);
  const items = list.data?.items || [];

  const publishPage = async () => {
    const ids = items.filter((s) => s.status === "draft").map((s) => s.id);
    if (!ids.length) return;
    try { await DB.setSnippetsStatus(ids, "published"); toast(`Published ${ids.length}`); refresh(); }
    catch (e) { console.error(e); toast(e?.message || "Couldn't publish", "err"); }
  };

  const s = stats.data;
  return (
    <div>
      {s?.missing && <div className="form-err"><AlertCircle size={16} />Migration 0030 is not applied yet, so there is nothing to review.</div>}
      <div className="ma-pre">
        <div className="ma-stat"><b>{s ? s.snippets.draft : "–"}</b><span>drafts to review</span></div>
        <div className="ma-stat"><b>{s ? s.snippets.published : "–"}</b><span>published</span></div>
      </div>
      <div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginBottom: 12 }}>
        <select className="sel" value={status} onChange={(e) => { setStatus(e.target.value); setOffset(0); }} aria-label="Status">
          <option value="draft">Drafts</option><option value="published">Published</option><option value="">All</option>
        </select>
        <select className="sel" value={kind} onChange={(e) => { setKind(e.target.value); setOffset(0); }} aria-label="Kind">
          <option value="">Every kind</option>{SN_KINDS.map((k) => <option key={k} value={k}>{k}</option>)}
        </select>
        <div className="search" style={{ flex: 1, minWidth: 200 }}>
          <Search size={15} /><input value={q} onChange={(e) => setQ(e.target.value)} placeholder="Search the passages" aria-label="Search" />
        </div>
        {status === "draft" && items.length > 0 && (
          <button className="btn btn-primary btn-sm" onClick={publishPage}><CheckCircle2 size={15} />Publish these {items.length}</button>
        )}
      </div>
      {list.err ? <ErrorState message={list.err} onRetry={refresh} />
        : list.loading ? <SkeletonCards count={3} height={150} />
        : items.length === 0 ? <div className="card card-pad" style={{ fontSize: 13.5, color: "var(--muted)" }}>Nothing here.</div>
        : items.map((sn) => <SnippetAdminRow key={sn.id} sn={sn} pyqById={pyqById} toast={toast} askDelete={askDelete} onChanged={refresh} />)}
      {list.data && list.data.total > 30 && (
        <div style={{ display: "flex", gap: 8, justifyContent: "center", alignItems: "center", marginTop: 12, fontSize: 13 }}>
          <button className="btn btn-ghost btn-sm" disabled={offset === 0} onClick={() => setOffset((o) => Math.max(0, o - 30))}>Previous</button>
          <span>{offset + 1}–{Math.min(offset + 30, list.data.total)} of {list.data.total}</span>
          <button className="btn btn-ghost btn-sm" disabled={offset + 30 >= list.data.total} onClick={() => setOffset((o) => o + 30)}>Next</button>
        </div>
      )}
    </div>
  );
}

function SnippetAdminRow({ sn, pyqById, toast, askDelete, onChanged }) {
  const [f, setF] = useState({ kind: sn.kind, body: sn.body, attribution: sn.attribution, why: sn.why, reviewNote: sn.reviewNote });
  const dirty = ["kind", "body", "attribution", "why", "reviewNote"].some((k) => (f[k] || "") !== (sn[k] || ""));
  const set = (k, v) => setF((p) => ({ ...p, [k]: v }));
  const save = async (status) => {
    try {
      await DB.updateSnippet(sn.id, { ...f, ...(status ? { status } : {}) });
      toast(status === "published" ? "Published" : status === "draft" ? "Moved back to drafts" : "Saved");
      onChanged();
    } catch (e) { console.error(e); toast(e?.message || "Couldn't save", "err"); }
  };
  const remove = () => askDelete("Delete this passage from the wiki?", async () => {
    try { await DB.deleteSnippet(sn.id); toast("Deleted"); onChanged(); }
    catch (e) { console.error(e); toast(e?.message || "Couldn't delete", "err"); }
  });
  return (
    <div className="ma-ans">
      <div className="ma-ans-top" style={{ alignItems: "center", flexWrap: "wrap" }}>
        <select className="sel" value={f.kind} onChange={(e) => set("kind", e.target.value)} aria-label="Kind">
          {SN_KINDS.map((k) => <option key={k} value={k}>{k}</option>)}
        </select>
        <span className={"ma-kind " + (sn.status === "published" ? "exact" : "related")}>{sn.status}</span>
        <span className="ma-ans-meta" style={{ flex: 1, minWidth: 160, marginTop: 0 }}>{sn.answerId ? `${sn.topperName} · ${sn.question}` : "Editor's pick (no topper essay)"}</span>
        <button className="btn-icon danger" title="Delete" onClick={remove}><Trash2 size={14} /></button>
      </div>
      {f.reviewNote && <div className="form-err" style={{ marginTop: 8, background: "var(--amb-bg)", color: "var(--ink)" }}><AlertCircle size={15} />{f.reviewNote}</div>}
      <textarea className="inp" rows={Math.min(8, Math.max(2, Math.ceil(f.body.length / 110)))} value={f.body} onChange={(e) => set("body", e.target.value)}
                style={{ marginTop: 8, fontFamily: "Georgia,serif", fontSize: 14.5, lineHeight: 1.6 }} aria-label="Passage" />
      <div className="field-row" style={{ marginTop: 8 }}>
        {f.kind === "quote" && <Field label="Said by (as the topper credits it)"><input className="inp" value={f.attribution} onChange={(e) => set("attribution", e.target.value)} /></Field>}
        <Field label="Why it works"><input className="inp" value={f.why} onChange={(e) => set("why", e.target.value)} /></Field>
      </div>
      <Field label="Note for reviewers" hint="Not shown to students. Clear it once checked.">
        <input className="inp" value={f.reviewNote} onChange={(e) => set("reviewNote", e.target.value)} />
      </Field>
      <div style={{ fontSize: 12.5, color: "var(--muted)", marginBottom: 8 }}>
        Fits {sn.fits.length} topic{sn.fits.length === 1 ? "" : "s"}:
        <ul style={{ margin: "4px 0 0", paddingLeft: 18 }}>
          {sn.fits.map((x) => <li key={x.pyqId}><b style={{ color: "var(--ink)" }}>{pyqById.get(x.pyqId)?.topic || "PYQ"}</b> — {x.use}</li>)}
        </ul>
      </div>
      <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
        {dirty && <button className="btn btn-ghost btn-sm" onClick={() => save()}><Save size={15} />Save edits</button>}
        {sn.status === "draft"
          ? <button className="btn btn-primary btn-sm" onClick={() => save("published")}><CheckCircle2 size={15} />{dirty ? "Save and publish" : "Publish"}</button>
          : <button className="btn btn-ghost btn-sm" onClick={() => save("draft")}>Unpublish</button>}
      </div>
    </div>
  );
}

/* ======================================================== LEARN TO WRITE == */

function ltwProblems(doc) {
  const out = [];
  if (!doc || typeof doc !== "object" || Array.isArray(doc)) return ["The guide must be a JSON object."];
  if (typeof doc.spine !== "string" || !doc.spine.trim()) out.push("spine is missing");
  if (!Array.isArray(doc.sides) || doc.sides.length !== 3) out.push("sides needs Thesis, Antithesis, Synthesis");
  if (!Array.isArray(doc.arguments) || doc.arguments.length < 3) out.push("arguments needs at least 3");
  (doc.arguments || []).forEach((a, i) => {
    if (![0, 1, 2].includes(a?.side)) out.push(`argument ${i + 1}: side must be 0, 1 or 2`);
    if (!a?.title) out.push(`argument ${i + 1}: title is missing`);
  });
  if (!Array.isArray(doc.introductions) || !doc.introductions.length) out.push("introductions is empty");
  if (!Array.isArray(doc.conclusions) || !doc.conclusions.length) out.push("conclusions is empty");
  return out;
}

function LtwAdminPanel({ toast, askDelete }) {
  const [reload, setReload] = useState(0);
  const [filter, setFilter] = useState("draft");
  const [editing, setEditing] = useState(null);
  const pyqs = useLoad(() => DB.essayPyqs({ includeDrafts: true }), "pyqs");
  const states = useLoad(() => DB.adminLtwList(), `ltw|${reload}`);
  const stateOf = (id) => states.data?.get(id)?.status || "none";
  const rows = (pyqs.data || []).filter((p) => !filter || stateOf(p.id) === filter);
  const count = (s) => (pyqs.data || []).filter((p) => stateOf(p.id) === s).length;
  return (
    <div>
      <div className="ma-pre">
        <div className="ma-stat"><b>{states.data ? count("draft") : "–"}</b><span>drafts to review</span></div>
        <div className="ma-stat"><b>{states.data ? count("published") : "–"}</b><span>published</span></div>
        <div className="ma-stat"><b>{states.data ? count("none") : "–"}</b><span>PYQs without a guide</span></div>
      </div>
      <div className="ma-tabs" style={{ marginBottom: 12 }}>
        {[["draft", "Drafts"], ["published", "Published"], ["none", "No guide"], ["", "All"]].map(([k, l]) => (
          <button key={k} className={"ma-tab" + (filter === k ? " on" : "")} onClick={() => setFilter(k)}>{l}</button>
        ))}
      </div>
      {pyqs.err || states.err ? <ErrorState message={pyqs.err || states.err} onRetry={() => setReload((n) => n + 1)} />
        : pyqs.loading || states.loading ? <SkeletonCards count={3} height={60} />
        : rows.length === 0 ? <div className="card card-pad" style={{ fontSize: 13.5, color: "var(--muted)" }}>Nothing here.</div>
        : (
          <div className="tbl-wrap">
            <table className="tbl">
              <thead><tr><th>Year</th><th>Topic</th><th>Guide</th><th /></tr></thead>
              <tbody>
                {rows.map((p) => (
                  <tr key={p.id}>
                    <td>{p.year}</td>
                    <td style={{ maxWidth: 520 }}>{p.topic}</td>
                    <td><span className={"ma-kind " + (stateOf(p.id) === "published" ? "exact" : "related")}>{stateOf(p.id)}</span></td>
                    <td style={{ textAlign: "right" }}>
                      {stateOf(p.id) !== "none" && <button className="btn btn-ghost btn-sm" onClick={() => setEditing(p)}><Eye size={14} />Review</button>}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      {editing && (
        <LtwEditor pyq={editing} toast={toast} askDelete={askDelete} onClose={() => setEditing(null)}
                   onSaved={() => { setEditing(null); setReload((n) => n + 1); }} />
      )}
    </div>
  );
}

function LtwEditor({ pyq, toast, askDelete, onClose, onSaved }) {
  const { t } = useLang();
  const row = useLoad(() => DB.adminLtw(pyq.id), `ltwdoc|${pyq.id}`);
  const essays = useLoad(() => DB.essaysForPyq(pyq.id), `ess|${pyq.id}`);
  const entries = useMemo(() => new Map((essays.data || []).flatMap((g) => g.entries.map((e) => [e.answerId, e]))), [essays.data]);
  const [text, setText] = useState(null);
  const [view, setView] = useState("preview");
  const value = text ?? (row.data ? JSON.stringify(row.data.doc, null, 2) : "");
  const parsed = useMemo(() => {
    try { return { doc: value ? JSON.parse(value) : null, err: "" }; } catch (e) { return { doc: null, err: e.message }; }
  }, [value]);
  const problems = parsed.err ? [`Not valid JSON: ${parsed.err}`] : ltwProblems(parsed.doc);
  const status = row.data?.status || "draft";

  const save = async (next) => {
    try { await DB.saveLtw(pyq.id, parsed.doc, next); toast(next === "published" ? "Published" : "Saved as draft"); onSaved(); }
    catch (e) { console.error(e); toast(e?.message || "Couldn't save", "err"); }
  };
  const remove = () => askDelete("Delete this Learn to Write guide?", async () => {
    try { await DB.deleteLtw(pyq.id); toast("Deleted"); onSaved(); }
    catch (e) { console.error(e); toast(e?.message || "Couldn't delete", "err"); }
  });

  return (
    <Modal title={`Learn to Write · ${pyq.topic} (${pyq.year})`} onClose={onClose} wide
           footer={<>
             <button className="btn btn-ghost" style={{ marginRight: "auto" }} onClick={remove}><Trash2 size={15} />Delete</button>
             <button className="btn btn-ghost" onClick={() => save("draft")} disabled={!!problems.length}>{status === "published" ? "Unpublish" : "Save draft"}</button>
             <button className="btn btn-primary" onClick={() => save("published")} disabled={!!problems.length}><CheckCircle2 size={16} />{status === "published" ? "Save" : "Publish"}</button>
           </>}>
      <style>{STUDY_CSS}</style>
      <div className="ma-tabs" style={{ marginBottom: 12 }}>
        {[["preview", "Preview"], ["json", "Edit"]].map(([k, l]) => (
          <button key={k} className={"ma-tab" + (view === k ? " on" : "")} onClick={() => setView(k)}>{l}</button>
        ))}
        <span className={"ma-kind " + (status === "published" ? "exact" : "related")} style={{ alignSelf: "center" }}>{status}</span>
      </div>
      {problems.length > 0 && <div className="form-err"><AlertCircle size={16} />{problems.slice(0, 4).join("; ")}</div>}
      {row.err ? <ErrorState message={row.err} />
        : row.loading ? <SkeletonCards count={2} height={120} />
        : view === "json"
          ? (
            <Field hint="The guide as JSON: spine, how_to, dimensions, sides, arguments (side 0 thesis, 1 antithesis, 2 synthesis; sources are essay ids), introductions, conclusions, pitfalls.">
              <textarea className="inp" rows={26} value={value} onChange={(e) => setText(e.target.value)} spellCheck={false}
                        style={{ fontFamily: "ui-monospace,Consolas,monospace", fontSize: 12.5, lineHeight: 1.5 }} aria-label="Guide JSON" />
            </Field>
          )
          : parsed.doc ? <LtwDoc doc={parsed.doc} entries={entries} onText={() => {}} onOpen={() => {}} t={t} />
          : null}
    </Modal>
  );
}
