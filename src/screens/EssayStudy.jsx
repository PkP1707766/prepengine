import { useState, useEffect, useMemo } from "react";
import { Star, Check, StickyNote, Lock, BookOpen, FileText, ChevronDown, ChevronUp, Search, X, Flame, Trash2, Plus, ListChecks } from "lucide-react";
import { EmptyState, ErrorState, SkeletonCards } from "../ui/Feedback.jsx";
import * as DB from "../lib/db.js";

/* ============================================================
   ESSAY: the study tools around the library (migration 0030)

   - Stars and "done" on PYQs, essays and wiki snippets, a streak,
     and the student's own notes (My notes tab).
   - Learn to Write on a PYQ: the core idea, three sides, arguments
     with model paragraphs citing the toppers' essays, openings,
     closings and pitfalls. Mains holders read it; others see a
     preview.
   - The Essay Wiki: openings, closings, quotes, anecdotes, examples
     and statistics from toppers' essays, by theme, each with the
     topics it fits and how to use it there.
   ============================================================ */

export const STUDY_CSS = `
.st-strip{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-bottom:16px}
.st-stat{display:flex;align-items:center;gap:11px;padding:12px 14px;text-align:left;width:100%}
.st-stat .ic{width:34px;height:34px;border-radius:10px;display:grid;place-items:center;background:var(--amb-bg);color:var(--gold-2);flex:0 0 auto}
.st-stat .v{font-size:17px;font-weight:800;color:var(--ink);font-variant-numeric:tabular-nums;line-height:1.2}
.st-stat .l{font-size:12px;color:var(--muted);line-height:1.35}
.st-bar{height:5px;border-radius:99px;background:var(--hair);margin-top:6px;overflow:hidden}
.st-bar i{display:block;height:100%;background:var(--gold-2);border-radius:99px}
button.st-stat:hover{border-color:var(--gold-2)}
.st-icon{display:inline-grid;place-items:center;width:34px;height:34px;border-radius:9px;border:1.5px solid var(--line);
  background:var(--card);color:var(--muted);flex:0 0 auto}
.st-icon:hover{border-color:var(--gold-2);color:var(--ink)}
.st-icon.on{color:#b7791f;border-color:#e8c27a;background:var(--amb-bg)}
.st-done{display:inline-flex;align-items:center;gap:6px}
.st-done.on{background:var(--green-bg,#e6f4ea);color:var(--green);border-color:transparent}
.st-chip-done{display:inline-flex;align-items:center;gap:4px;font-size:11.5px;font-weight:700;color:var(--green)}
.st-sec{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 14px}
.st-sec button{font-size:13px;font-weight:700;padding:8px 14px;border-radius:999px;border:1.5px solid var(--line);background:var(--card);color:var(--muted)}
.st-sec button.on{background:var(--navy);border-color:var(--navy);color:#ffffff}
.st-sec button .n{opacity:.7;margin-left:5px;font-variant-numeric:tabular-nums}
.st-head-acts{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}
.st-head-acts .btn{width:auto}
.ltw-card{padding:18px 20px;margin-bottom:14px}
.ltw-k{font-size:11px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--gold-2);margin-bottom:8px}
.ltw-spine{font-family:Georgia,"Times New Roman",serif;font-size:19px;line-height:1.55;color:var(--ink)}
.ltw-list{margin:0;padding-left:18px;display:flex;flex-direction:column;gap:8px;font-size:14px;line-height:1.6;color:var(--ink)}
.ltw-dims{display:flex;gap:6px;flex-wrap:wrap;margin-top:12px}
.ltw-dims span{display:inline-flex;align-items:center;font-size:11.5px;font-weight:700;padding:3px 9px;border-radius:999px;background:var(--hair);color:var(--muted);border:1px solid var(--line);line-height:1.4}
.ltw-sides{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.ltw-side{border:1px solid var(--line);border-radius:10px;padding:12px 14px;background:var(--hair)}
.ltw-side .h{font-size:13px;font-weight:800;color:var(--ink);margin-bottom:4px}
.ltw-side p{margin:0;font-size:13.5px;line-height:1.55;color:var(--ink)}
.ltw-group-h{display:flex;align-items:baseline;gap:10px;margin:22px 2px 10px}
.ltw-group-h .s{font-size:16px;font-weight:800;color:var(--ink)}
.ltw-group-h .b{font-size:13px;color:var(--muted)}
.ltw-arg{padding:16px 18px;margin-bottom:10px}
.ltw-arg-top{display:flex;gap:10px;align-items:baseline}
.ltw-num{font-family:Georgia,serif;font-size:18px;font-weight:700;color:var(--gold-2);min-width:26px}
.ltw-title{font-size:15px;font-weight:800;color:var(--ink);line-height:1.4}
.ltw-point{font-size:13.5px;color:var(--muted);margin-top:3px;line-height:1.55}
.ltw-para{font-family:Georgia,"Times New Roman",serif;font-size:15.5px;line-height:1.75;color:var(--ink);margin:12px 0 0;padding-left:36px}
.ltw-src{display:flex;align-items:center;gap:6px;flex-wrap:wrap;margin-top:10px;padding-left:36px;font-size:12px;color:var(--muted)}
.ltw-src button{font-size:12px;font-weight:700;color:var(--navy);background:var(--hair);border:1px solid var(--line);border-radius:999px;padding:3px 10px}
.ltw-src button:hover{border-color:var(--gold-2)}
.ltw-tabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px}
.ltw-tabs button{font-size:12.5px;font-weight:700;padding:6px 12px;border-radius:999px;border:1.5px solid var(--line);color:var(--muted);background:var(--card)}
.ltw-tabs button.on{border-color:var(--gold-2);color:var(--ink);background:var(--amb-bg)}
.ltw-text{font-family:Georgia,"Times New Roman",serif;font-size:15.5px;line-height:1.75;color:var(--ink);margin:0}
.ltw-meta{font-size:12px;color:var(--muted);margin-top:8px}
.ltw-lock{display:flex;gap:12px;align-items:flex-start;padding:16px 18px;margin-bottom:14px;background:var(--amb-bg)}
.ltw-lock .btn{width:auto}
.ltw-blur{filter:blur(3.5px);user-select:none;pointer-events:none;color:var(--muted)}
.ltw-foot{font-size:12px;color:var(--muted);margin:6px 2px 0;line-height:1.55}
.sn-card{padding:16px 18px;margin-bottom:10px}
.sn-top{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:10px}
.sn-kind{font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--gold-2)}
.sn-body{font-family:Georgia,"Times New Roman",serif;font-size:16px;line-height:1.7;color:var(--ink);margin:0;
  border-left:3px solid var(--gold-2);padding:2px 0 2px 14px}
.sn-by{font-size:13px;font-weight:700;color:var(--ink);margin-top:8px;padding-left:17px}
.sn-src{display:flex;align-items:center;gap:8px;flex-wrap:wrap;font-size:12.5px;color:var(--muted);margin-top:10px}
.sn-src button{font-weight:700;color:var(--navy);font-size:12.5px}
.sn-use{font-size:13.5px;line-height:1.6;color:var(--ink);margin-top:10px;background:var(--hair);border-radius:9px;padding:9px 12px}
.sn-use b{color:var(--gold-2)}
.sn-why{font-size:13px;line-height:1.55;color:var(--muted);margin-top:8px}
.sn-fits{margin-top:10px}
.sn-fits-btn{display:inline-flex;align-items:center;gap:4px;font-size:12.5px;font-weight:700;color:var(--navy)}
.sn-fit{border-top:1px solid var(--line);padding:9px 0 0;margin-top:9px;font-size:13px;line-height:1.55}
.sn-fit .q{font-weight:700;color:var(--ink)}
.sn-fit .u{color:var(--muted)}
.sn-acts{display:flex;gap:6px}
.wk-kinds{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px}
.wk-kinds button{font-size:12.5px;font-weight:700;padding:6px 12px;border-radius:999px;border:1.5px solid var(--line);color:var(--muted);background:var(--card)}
.wk-kinds button.on{background:var(--navy);border-color:var(--navy);color:#ffffff}
.nt-row{padding:14px 18px;border-bottom:1px solid var(--line)}
.nt-row:last-child{border-bottom:none}
.nt-label{font-size:12px;font-weight:700;color:var(--gold-2);margin-bottom:4px;line-height:1.4}
.nt-body{font-size:14px;line-height:1.6;color:var(--ink);white-space:pre-wrap;overflow-wrap:anywhere}
.nt-meta{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-top:8px;font-size:12px;color:var(--muted)}
.nt-meta button{font-weight:700;color:var(--navy);font-size:12px}
.nt-star{display:flex;align-items:center;gap:12px;padding:12px 18px;border-bottom:1px solid var(--line)}
.nt-star:last-child{border-bottom:none}
.nt-star .m{flex:1;min-width:0;font-size:14px;font-weight:700;color:var(--ink);line-height:1.45}
.nt-star .s{font-size:12px;color:var(--muted);font-weight:500;margin-top:2px}
.nt-h{display:flex;align-items:center;justify-content:space-between;gap:10px;margin:18px 2px 8px}
.nt-h:first-child{margin-top:0}
.nt-h h3{font-size:15px;font-weight:800;color:var(--ink);margin:0}
.nt-h .btn{width:auto}
.modal.st-note-modal{max-width:560px;width:calc(100% - 28px)}
.st-note-modal textarea{width:100%;min-height:150px;resize:vertical;padding:11px 12px;border:1.5px solid var(--line);border-radius:10px;
  background:var(--card);color:var(--ink);font:inherit;font-size:14.5px;line-height:1.6}
.st-note-about{font-size:12.5px;color:var(--muted);margin-bottom:10px;line-height:1.5}
.st-err{color:var(--red,#c0392b);font-size:13px;margin-top:8px}
@media(max-width:860px){
  .ltw-sides{grid-template-columns:minmax(0,1fr)}
}
@media(max-width:560px){
  .st-strip{grid-template-columns:minmax(0,1fr)}
  .es-entry-acts .st-icon{align-self:flex-start}
  .ltw-para,.ltw-src{padding-left:0}
  .ltw-spine{font-size:17px}
}
`;

const fill = (s, vars) => Object.entries(vars).reduce((out, [k, v]) => out.split(`{${k}}`).join(String(v)), s);
const KINDS = ["opening", "closing", "quote", "anecdote", "example", "statistic"];
const words = (s) => (String(s || "").match(/\S+/g) || []).length;

/* ------------------------------------------------------------ the strip -- */

export function StudyStrip({ pyqs, marks, streak, notesCount, onNotes, t }) {
  const done = pyqs.filter((p) => marks.pyq.get(p.id)?.done).length;
  const starred = ["pyq", "answer", "snippet"].reduce((n, k) => n + [...marks[k].values()].filter((m) => m.starred).length, 0);
  const pct = pyqs.length ? Math.round((done / pyqs.length) * 100) : 0;
  return (
    <div className="st-strip">
      <div className="card st-stat">
        <span className="ic"><ListChecks size={18} /></span>
        <span style={{ flex: 1, minWidth: 0 }}>
          <span className="v">{done}<span style={{ fontSize: 13, color: "var(--muted)", fontWeight: 700 }}> / {pyqs.length}</span></span>
          <span className="l" style={{ display: "block" }}>{t("st_done_pyqs")}</span>
          <span className="st-bar"><i style={{ width: `${pct}%` }} /></span>
        </span>
      </div>
      <div className="card st-stat">
        <span className="ic"><Flame size={18} /></span>
        <span>
          <span className="v">{streak === 1 ? t("st_streak_one") : fill(t("st_streak_n"), { n: streak })}</span>
          <span className="l" style={{ display: "block" }}>{t("st_streak_hint")}</span>
        </span>
      </div>
      <button className="card st-stat" onClick={onNotes}>
        <span className="ic"><StickyNote size={18} /></span>
        <span>
          <span className="v">{fill(t(notesCount === 1 ? "st_saved_one" : "st_saved_n"), { s: starred, n: notesCount })}</span>
          <span className="l" style={{ display: "block" }}>{t("st_saved_hint")}</span>
        </span>
      </button>
    </div>
  );
}

/* ------------------------------------------------------- small controls -- */

export function StarButton({ on, onClick, t }) {
  return (
    <button className={"st-icon" + (on ? " on" : "")} onClick={onClick} aria-pressed={on}
            title={on ? t("st_unstar") : t("st_star")} aria-label={on ? t("st_unstar") : t("st_star")}>
      <Star size={16} fill={on ? "currentColor" : "none"} />
    </button>
  );
}

export function NoteButton({ count = 0, onClick, t }) {
  return (
    <button className={"st-icon" + (count ? " on" : "")} onClick={onClick}
            title={count ? fill(t("st_notes_n"), { n: count }) : t("st_add_note")} aria-label={t("st_add_note")}>
      <StickyNote size={16} />
    </button>
  );
}

export function DoneButton({ on, onClick, t, small = true }) {
  return (
    <button className={"btn " + (small ? "btn-sm " : "") + "btn-ghost st-done" + (on ? " on" : "")} onClick={onClick} aria-pressed={on}>
      <Check size={15} />{on ? t("st_done") : t("st_mark_done")}
    </button>
  );
}

/* ---------------------------------------------------------- note editor -- */

export function NoteModal({ draft, onClose, onSaved, onDeleted, t }) {
  const [body, setBody] = useState(draft.body || "");
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState("");

  useEffect(() => {
    const onKey = (ev) => { if (ev.key === "Escape") onClose(); };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onClose]);

  const save = async () => {
    if (!body.trim()) return;
    setBusy(true); setErr("");
    try { onSaved(await DB.saveEssayNote({ ...draft, body })); }
    catch (e) { setErr(e?.message || t("st_note_fail")); setBusy(false); }
  };
  const remove = async () => {
    setBusy(true); setErr("");
    try { await DB.deleteEssayNote(draft.id); onDeleted(draft.id); }
    catch (e) { setErr(e?.message || t("st_note_fail")); setBusy(false); }
  };

  return (
    <div className="overlay" onClick={onClose}>
      <div className="modal st-note-modal" onClick={(ev) => ev.stopPropagation()} role="dialog" aria-modal="true" aria-labelledby="st-note-title">
        <div className="modal-head">
          <h3 id="st-note-title">{draft.id ? t("st_edit_note") : t("st_new_note")}</h3>
          <button className="x" onClick={onClose} aria-label={t("es_v_close")}><X size={19} /></button>
        </div>
        <div className="modal-body">
          {draft.label && <div className="st-note-about">{fill(t("st_note_about"), { x: draft.label })}</div>}
          <textarea value={body} onChange={(e) => setBody(e.target.value)} maxLength={5000} autoFocus
                    placeholder={t("st_note_ph")} aria-label={t("st_new_note")} />
          {err && <div className="st-err">{err}</div>}
        </div>
        <div className="modal-foot">
          {draft.id && <button className="btn btn-ghost btn-sm" onClick={remove} disabled={busy} style={{ marginRight: "auto" }}><Trash2 size={14} />{t("st_delete")}</button>}
          <button className="btn btn-ghost btn-sm" onClick={onClose} disabled={busy}>{t("st_cancel")}</button>
          <button className="btn btn-primary btn-sm" onClick={save} disabled={busy || !body.trim()}>{t("st_save")}</button>
        </div>
      </div>
    </div>
  );
}

/* ------------------------------------------------------- Learn to Write -- */

/* Loads a PYQ's guide. Keyed like the library: while the result belongs to
   another PYQ or attempt it shows as loading; nothing resets in the effect. */
function useLtw(pyqId) {
  const [tries, setTries] = useState(0);
  const key = `${pyqId}|${tries}`;
  const [res, setRes] = useState({ key: null, data: null, err: "" });
  useEffect(() => {
    let alive = true;
    DB.essayLtw(pyqId).then(
      (data) => { if (alive) setRes({ key, data, err: "" }); },
      (e) => { if (alive) setRes({ key, data: null, err: e?.message || " " }); },
    );
    return () => { alive = false; };
  }, [key, pyqId]);
  return { loading: res.key !== key, data: res.data, err: res.err, retry: () => setTries((n) => n + 1) };
}

function Sources({ ids, entries, onText, onOpen, t }) {
  const list = (ids || []).map((id) => entries.get(id)).filter(Boolean);
  if (!list.length) return null;
  return (
    <div className="ltw-src">
      <span>{t("ltw_from")}</span>
      {list.map((e) => (
        <button key={e.answerId} onClick={() => (e.words > 0 ? onText(e) : onOpen(e))} title={e.question}>
          {fill(t("ltw_essay_of"), { n: e.topper.name.split(" ")[0] })}
        </button>
      ))}
    </div>
  );
}

function Variants({ items, labels, entries, onText, onOpen, t }) {
  const [i, setI] = useState(0);
  const cur = items[Math.min(i, items.length - 1)];
  if (!cur) return null;
  return (
    <>
      <div className="ltw-tabs" role="tablist">
        {items.map((x, k) => (
          <button key={x.type + k} className={k === i ? "on" : ""} onClick={() => setI(k)} role="tab" aria-selected={k === i}>
            {labels[x.type] || x.type}
          </button>
        ))}
      </div>
      <p className="ltw-text">{cur.text}</p>
      <div className="ltw-meta">{fill(t("es_words"), { n: words(cur.text) })}</div>
      <Sources ids={cur.sources} entries={entries} onText={onText} onOpen={onOpen} t={t} />
    </>
  );
}

export function LtwPanel({ pyq, entries, onText, onOpen, onBrowse, t }) {
  const { loading, data, err, retry } = useLtw(pyq.id);
  if (loading) return <SkeletonCards count={3} height={110} />;
  if (err) return <div className="card card-pad"><ErrorState message={err.trim() || t("ltw_fail")} onRetry={retry} /></div>;
  if (!data) return <div className="card card-pad"><EmptyState compact icon={<BookOpen size={24} />} title={t("ltw_none")} text={t("ltw_none_text")} /></div>;

  const sideName = [t("ltw_thesis"), t("ltw_antithesis"), t("ltw_synthesis")];

  if (data.preview) {
    const p = data.preview;
    return (
      <div>
        <div className="card ltw-lock">
          <Lock size={18} style={{ flex: "0 0 auto", marginTop: 2 }} />
          <div style={{ flex: 1 }}>
            <div style={{ fontWeight: 800, marginBottom: 4 }}>{t("ltw_locked")}</div>
            <div style={{ fontSize: 13.5, color: "var(--muted)", lineHeight: 1.55 }}>{t("ltw_locked_text")}</div>
          </div>
          {onBrowse && <button className="btn btn-sm btn-primary" onClick={onBrowse}>{t("es_see_bundles")}</button>}
        </div>
        {p.spine && <div className="card ltw-card"><div className="ltw-k">{t("ltw_spine")}</div><div className="ltw-spine">{p.spine}</div></div>}
        {Array.isArray(p.sides) && p.sides.length > 0 && (
          <div className="card ltw-card">
            <div className="ltw-k">{t("ltw_sides")}</div>
            <div className="ltw-sides">{p.sides.map((s, i) => <div className="ltw-side" key={i}><div className="h">{sideName[i] || s.label}</div><p>{s.blurb}</p></div>)}</div>
          </div>
        )}
        {Array.isArray(p.titles) && p.titles.length > 0 && (
          <div className="card ltw-card">
            <div className="ltw-k">{fill(t("ltw_n_args"), { n: p.titles.length })}</div>
            <ol className="ltw-list">
              {p.titles.map((a, i) => <li key={i}><b>{a.title}</b> <span className="ltw-blur">{t("ltw_blur_line")}</span></li>)}
            </ol>
          </div>
        )}
      </div>
    );
  }

  return <LtwDoc doc={data.doc || {}} entries={entries} onText={onText} onOpen={onOpen} t={t} />;
}

/** A guide as students see it. Pure: the admin previews drafts with it too. */
export function LtwDoc({ doc, entries, onText, onOpen, t }) {
  const sideName = [t("ltw_thesis"), t("ltw_antithesis"), t("ltw_synthesis")];
  const d = doc || {};
  // Numbered across the whole guide, in thesis, antithesis, synthesis order.
  const args = (Array.isArray(d.arguments) ? d.arguments : [])
    .map((a, i) => ({ ...a, i }))
    .sort((a, b) => a.side - b.side || a.i - b.i)
    .map((a, k) => ({ ...a, num: k + 1 }));
  const sides = Array.isArray(d.sides) ? d.sides : [];
  return (
    <div>
      {d.spine && <div className="card ltw-card"><div className="ltw-k">{t("ltw_spine")}</div><div className="ltw-spine">{d.spine}</div></div>}
      {(d.how_to?.length > 0 || d.dimensions?.length > 0) && (
        <div className="card ltw-card">
          <div className="ltw-k">{t("ltw_how_to")}</div>
          {d.how_to?.length > 0 && <ul className="ltw-list">{d.how_to.map((h, i) => <li key={i}>{h}</li>)}</ul>}
          {d.dimensions?.length > 0 && <div className="ltw-dims">{d.dimensions.map((x) => <span key={x}>{x}</span>)}</div>}
        </div>
      )}
      {sides.length > 0 && (
        <div className="card ltw-card">
          <div className="ltw-k">{t("ltw_sides")}</div>
          <div className="ltw-sides">{sides.map((s, i) => <div className="ltw-side" key={i}><div className="h">{sideName[i] || s.label}</div><p>{s.blurb}</p></div>)}</div>
        </div>
      )}
      {[0, 1, 2].map((side) => {
        const list = args.filter((a) => a.side === side);
        if (!list.length) return null;
        return (
          <section key={side}>
            <div className="ltw-group-h"><span className="s">{sideName[side]}</span><span className="b">{fill(t("ltw_n_args"), { n: list.length })}</span></div>
            {list.map((a) => (
              <article className="card ltw-arg" key={a.num}>
                <div className="ltw-arg-top">
                  <span className="ltw-num">{String(a.num).padStart(2, "0")}</span>
                  <div><div className="ltw-title">{a.title}</div>{a.point && <div className="ltw-point">{a.point}</div>}</div>
                </div>
                {a.paragraph && <p className="ltw-para">{a.paragraph}</p>}
                <Sources ids={a.sources} entries={entries} onText={onText} onOpen={onOpen} t={t} />
              </article>
            ))}
          </section>
        );
      })}
      {d.introductions?.length > 0 && (
        <div className="card ltw-card" style={{ marginTop: 18 }}>
          <div className="ltw-k">{t("ltw_intros")}</div>
          <Variants items={d.introductions} entries={entries} onText={onText} onOpen={onOpen} t={t}
                    labels={{ story: t("ltw_story"), quote: t("ltw_quote"), context: t("ltw_context") }} />
        </div>
      )}
      {d.conclusions?.length > 0 && (
        <div className="card ltw-card">
          <div className="ltw-k">{t("ltw_closings")}</div>
          <Variants items={d.conclusions} entries={entries} onText={onText} onOpen={onOpen} t={t}
                    labels={{ wayforward: t("ltw_wayforward"), reconciliation: t("ltw_reconcile"), quote: t("ltw_quote") }} />
        </div>
      )}
      {d.pitfalls?.length > 0 && (
        <div className="card ltw-card">
          <div className="ltw-k">{t("ltw_pitfalls")}</div>
          <ul className="ltw-list">{d.pitfalls.map((x, i) => <li key={i}>{x}</li>)}</ul>
        </div>
      )}
      <p className="ltw-foot">{t("ltw_note")}</p>
    </div>
  );
}

/* ---------------------------------------------------------------- wiki -- */

export function SnippetCard({ s, focusPyqId = null, pyqById, topicOf, starred, onStar, noteCount, onNote, onText, t }) {
  const [open, setOpen] = useState(false);
  const here = focusPyqId ? s.fits.find((f) => f.pyqId === focusPyqId) : null;
  const others = s.fits.filter((f) => f.pyqId !== focusPyqId && pyqById.has(f.pyqId));
  const e = s.entry;
  return (
    <article className="card sn-card">
      <div className="sn-top">
        <span className="sn-kind">{t(`wk_k_${s.kind}`)}</span>
        <span className="sn-acts">
          <StarButton on={starred} onClick={onStar} t={t} />
          <NoteButton count={noteCount} onClick={onNote} t={t} />
        </span>
      </div>
      <blockquote className="sn-body">{s.body}</blockquote>
      {s.kind === "quote" && s.attribution && <div className="sn-by">— {s.attribution}</div>}
      {e ? (
        <div className="sn-src">
          <span>{fill(t("wk_from"), { n: e.topper.name, q: e.question })}</span>
          {e.words > 0 && <button onClick={() => onText(e)}><FileText size={13} style={{ verticalAlign: -2 }} /> {t("wk_read_essay")}</button>}
        </div>
      ) : !s.answerId && (
        <div className="sn-src"><span>{t("wk_editor_pick")}</span></div>
      )}
      {here && <div className="sn-use"><b>{t("wk_use_here")}</b> {here.use}</div>}
      {s.why && <div className="sn-why">{fill(t("wk_why"), { x: s.why })}</div>}
      {others.length > 0 && (
        <div className="sn-fits">
          <button className="sn-fits-btn" onClick={() => setOpen((v) => !v)} aria-expanded={open}>
            {open ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
            {others.length === 1 ? t("wk_fits_one") : fill(t("wk_fits_n"), { n: others.length })}
          </button>
          {open && others.map((f) => {
            const p = pyqById.get(f.pyqId);
            return <div className="sn-fit" key={f.pyqId}><div className="q">{topicOf(p)} <span className="es-yr">({p.year})</span></div><div className="u">{f.use}</div></div>;
          })}
        </div>
      )}
    </article>
  );
}

/* Snippets that fit these PYQs, keyed like the other loaders. */
function useSnippets(pyqIds) {
  const [tries, setTries] = useState(0);
  const ids = pyqIds.join(",");
  const key = `${ids}|${tries}`;
  const [res, setRes] = useState({ key: null, list: [], err: "" });
  useEffect(() => {
    let alive = true;
    DB.essaySnippetsForPyqs(ids ? ids.split(",") : []).then(
      (list) => { if (alive) setRes({ key, list, err: "" }); },
      (e) => { if (alive) setRes({ key, list: [], err: e?.message || " " }); },
    );
    return () => { alive = false; };
  }, [key, ids]);
  return { loading: res.key !== key, list: res.list, err: res.err, retry: () => setTries((n) => n + 1) };
}

function KindChips({ list, kind, setKind, counts, t }) {
  const n = (k) => (counts ? counts[k] || 0 : list.filter((s) => s.kind === k).length);
  const total = counts ? KINDS.reduce((a, k) => a + (counts[k] || 0), 0) : list.length;
  return (
    <div className="wk-kinds" role="tablist">
      <button className={kind === "" ? "on" : ""} onClick={() => setKind("")}>{t("wk_all")} · {total}</button>
      {KINDS.filter((k) => n(k) > 0).map((k) => (
        <button key={k} className={kind === k ? "on" : ""} onClick={() => setKind(k)}>{t(`wk_ks_${k}`)} · {n(k)}</button>
      ))}
    </div>
  );
}

/** A PYQ's wiki: every snippet that fits this topic, with how to use it here. */
export function PyqSnippets({ pyq, ctx }) {
  const { t, access, onBrowse } = ctx;
  const { loading, list, err, retry } = useSnippets([pyq.id]);
  const [kind, setKind] = useState("");
  if (loading) return <SkeletonCards count={3} height={120} />;
  if (err) return <div className="card card-pad"><ErrorState message={err.trim() || t("wk_fail")} onRetry={retry} /></div>;
  if (!list.length) {
    return (
      <div className="card card-pad">
        <EmptyState compact icon={access ? <BookOpen size={24} /> : <Lock size={22} />}
                    title={access ? t("wk_pyq_none") : t("wk_locked")} text={access ? "" : t("wk_locked_text")} />
        {!access && onBrowse && <div style={{ display: "flex", justifyContent: "center", marginTop: 10 }}><button className="btn btn-sm btn-primary" style={{ width: "auto" }} onClick={onBrowse}>{t("es_see_bundles")}</button></div>}
      </div>
    );
  }
  const shown = list.filter((s) => !kind || s.kind === kind).sort((a, b) => KINDS.indexOf(a.kind) - KINDS.indexOf(b.kind));
  return (
    <div>
      <KindChips list={list} kind={kind} setKind={setKind} t={t} />
      {shown.map((s) => <SnippetRow key={s.id} s={s} focusPyqId={pyq.id} ctx={ctx} />)}
    </div>
  );
}

export function SnippetRow({ s, focusPyqId = null, ctx }) {
  const { t, marks, toggleMark, notesFor, editNote, openText, pyqById, topicOf } = ctx;
  const m = marks.snippet.get(s.id);
  return (
    <SnippetCard s={s} focusPyqId={focusPyqId} pyqById={pyqById} topicOf={topicOf} t={t}
                 starred={!!m?.starred} onStar={() => toggleMark("snippet", s.id, "starred")}
                 noteCount={notesFor("snippet", s.id).length}
                 onNote={() => editNote({ kind: "snippet", itemId: s.id, label: s.body.slice(0, 140) + (s.body.length > 140 ? "…" : "") })}
                 onText={openText} />
  );
}

/** The Essay Wiki tab: by theme, by kind, with search. */
export function WikiTab({ themes, pyqs, ctx }) {
  const { t, themeName, access, onBrowse } = ctx;
  const [counts, setCounts] = useState(null);
  const [theme, setTheme] = useState("");
  const [kind, setKind] = useState("");
  const [q, setQ] = useState("");

  useEffect(() => {
    let alive = true;
    DB.essayWikiCounts().then((c) => { if (alive) setCounts(c); }, () => { if (alive) setCounts([]); });
    return () => { alive = false; };
  }, []);

  const perTheme = useMemo(() => {
    const m = new Map();
    (counts || []).forEach((c) => {
      const x = m.get(c.themeId) || { total: 0 };
      x[c.kind] = c.n; x.total += c.n;
      m.set(c.themeId, x);
    });
    return m;
  }, [counts]);
  const railThemes = useMemo(() => themes.filter((th) => perTheme.get(th.id)?.total)
    .sort((a, b) => perTheme.get(b.id).total - perTheme.get(a.id).total || themeName(a).localeCompare(themeName(b))),
  [themes, perTheme, themeName]);
  const active = theme && perTheme.has(theme) ? theme : railThemes[0]?.id || "";
  const pyqIds = useMemo(() => pyqs.filter((p) => p.themes.some((x) => x.id === active)).map((p) => p.id), [pyqs, active]);

  if (counts === null) return <SkeletonCards count={3} height={110} />;
  if (!railThemes.length) {
    return <div className="card card-pad"><EmptyState icon={<BookOpen size={26} />} title={t("wk_empty_title")} text={t("wk_empty_text")} /></div>;
  }
  const items = railThemes.map((th) => [th.id, themeName(th), perTheme.get(th.id).total]);
  return (
    <div className="es-grid">
      <aside className="card es-rail">
        {items.map(([id, label, n]) => (
          <button key={id} className={"es-rail-item" + (active === id ? " on" : "")} onClick={() => { setTheme(id); setKind(""); }}
                  aria-current={active === id ? "true" : undefined}>
            <span>{label}</span><span className="n">{n}</span>
          </button>
        ))}
      </aside>
      <div style={{ minWidth: 0 }}>
        <div className="es-pick">
          <select value={active} onChange={(e) => { setTheme(e.target.value); setKind(""); }} aria-label={t("es_theme_label")}>
            {items.map(([id, label, n]) => <option key={id} value={id}>{label} ({n})</option>)}
          </select>
        </div>
        {!access && (
          <div className="es-note">
            <Lock size={15} /><span style={{ flex: 1, minWidth: 200 }}>{t("wk_locked_text")}</span>
            {onBrowse && <button className="btn btn-sm btn-ghost" onClick={onBrowse}>{t("es_see_bundles")}</button>}
          </div>
        )}
        <WikiList key={active} pyqIds={pyqIds} counts={perTheme.get(active)} kind={kind} setKind={setKind} q={q} setQ={setQ} ctx={ctx} />
      </div>
    </div>
  );
}

const WIKI_PAGE = 20;

function WikiList({ pyqIds, counts, kind, setKind, q, setQ, ctx }) {
  const { t } = ctx;
  const { loading, list, err, retry } = useSnippets(pyqIds);
  const [shownN, setShownN] = useState(WIKI_PAGE);
  const needle = q.trim().toLowerCase();
  const matches = list
    .filter((s) => (!kind || s.kind === kind)
      && (!needle || s.body.toLowerCase().includes(needle) || (s.attribution || "").toLowerCase().includes(needle)
        || (s.entry?.topper.name || "").toLowerCase().includes(needle)))
    .sort((a, b) => KINDS.indexOf(a.kind) - KINDS.indexOf(b.kind) || b.fits.length - a.fits.length);
  return (
    <div>
      <div className="es-tools">
        <label className="es-tool grow es-search">
          <Search size={15} />
          <input value={q} onChange={(e) => { setQ(e.target.value); setShownN(WIKI_PAGE); }} placeholder={t("wk_search")} aria-label={t("wk_search")} />
          {q && <button onClick={() => setQ("")} aria-label={t("es_v_close")} style={{ color: "var(--muted)", display: "grid" }}><X size={15} /></button>}
        </label>
      </div>
      <KindChips list={list} kind={kind} setKind={(k) => { setKind(k); setShownN(WIKI_PAGE); }} counts={loading || !list.length ? counts : null} t={t} />
      {loading ? <SkeletonCards count={3} height={120} />
        : err ? <div className="card card-pad"><ErrorState message={err.trim() || t("wk_fail")} onRetry={retry} /></div>
        : !matches.length ? <div className="card card-pad"><EmptyState compact icon={<Search size={22} />} title={needle ? fill(t("es_no_match"), { q }) : t("wk_none_here")} /></div>
        : (
          <>
            {matches.slice(0, shownN).map((s) => <SnippetRow key={s.id} s={s} ctx={ctx} />)}
            {matches.length > shownN && (
              <div className="es-more">
                <button className="btn btn-ghost" onClick={() => setShownN((n) => n + WIKI_PAGE)}>
                  {fill(t("es_show_more"), { n: shownN, t: matches.length })}
                </button>
              </div>
            )}
          </>
        )}
    </div>
  );
}

/* ------------------------------------------------------------ My notes -- */

export function NotesTab({ pyqs, ctx }) {
  const { t, lang, marks, notes, editNote, openPyq, topicOf, toggleMark, openText, open } = ctx;
  const [filter, setFilter] = useState("");
  const starredIds = (k) => [...marks[k]].filter(([, m]) => m.starred).map(([id]) => id);
  const ansIds = starredIds("answer").join(",");
  const snipIds = starredIds("snippet").join(",");
  const key = `${ansIds}|${snipIds}`;
  const [res, setRes] = useState({ key: null, answers: [], snippets: [] });

  useEffect(() => {
    let alive = true;
    Promise.all([DB.libraryEntries(ansIds ? ansIds.split(",") : []), DB.snippetsByIds(snipIds ? snipIds.split(",") : [])])
      .then(([answers, snippets]) => { if (alive) setRes({ key, answers, snippets }); },
        () => { if (alive) setRes({ key, answers: [], snippets: [] }); });
    return () => { alive = false; };
  }, [key, ansIds, snipIds]);

  const pyqStars = pyqs.filter((p) => marks.pyq.get(p.id)?.starred);
  const shownNotes = notes.filter((n) => !filter || n.kind === filter);
  const when = (iso) => new Date(iso).toLocaleDateString(lang === "hi" ? "hi-IN" : "en-IN", { day: "numeric", month: "short", year: "numeric" });
  const pyqById = new Map(pyqs.map((p) => [p.id, p]));

  const goto = (n) => {
    if (n.kind === "pyq" && pyqById.has(n.itemId)) openPyq(pyqById.get(n.itemId), "essays");
  };

  return (
    <div>
      <div className="nt-h">
        <h3>{fill(t("st_my_notes_n"), { n: notes.length })}</h3>
        <button className="btn btn-sm btn-primary" onClick={() => editNote({ kind: "free", itemId: null, label: "" })}><Plus size={14} />{t("st_new_note")}</button>
      </div>
      {notes.length > 0 && (
        <div className="wk-kinds">
          {[["", "wk_all"], ["pyq", "st_f_pyq"], ["answer", "st_f_answer"], ["snippet", "st_f_snippet"], ["free", "st_f_free"]].map(([k, key2]) => (
            <button key={k} className={filter === k ? "on" : ""} onClick={() => setFilter(k)}>{t(key2)}</button>
          ))}
        </div>
      )}
      <section className="card es-group">
        {shownNotes.length === 0
          ? <div className="card-pad"><EmptyState compact icon={<StickyNote size={22} />} title={t("st_no_notes")} text={t("st_no_notes_text")} /></div>
          : shownNotes.map((n) => (
            <div className="nt-row" key={n.id}>
              {n.label && <div className="nt-label">{n.label}</div>}
              <div className="nt-body">{n.body}</div>
              <div className="nt-meta">
                <span>{when(n.updatedAt)}</span>
                <button onClick={() => editNote(n)}>{t("st_edit")}</button>
                {n.kind === "pyq" && pyqById.has(n.itemId) && <button onClick={() => goto(n)}>{t("st_open_pyq")}</button>}
              </div>
            </div>
          ))}
      </section>

      <div className="nt-h"><h3>{fill(t("st_star_pyqs_n"), { n: pyqStars.length })}</h3></div>
      <section className="card es-group">
        {pyqStars.length === 0
          ? <div className="card-pad"><EmptyState compact icon={<Star size={22} />} title={t("st_no_stars")} /></div>
          : pyqStars.map((p) => (
            <div className="nt-star" key={p.id}>
              <div className="m">{topicOf(p)}<div className="s">{p.year}{marks.pyq.get(p.id)?.done ? ` · ${t("st_done")}` : ""}</div></div>
              <button className="btn btn-sm btn-ghost" style={{ width: "auto" }} onClick={() => openPyq(p, "essays")}>{t("st_open_pyq")}</button>
              <StarButton on onClick={() => toggleMark("pyq", p.id, "starred")} t={t} />
            </div>
          ))}
      </section>

      {res.key === key && res.answers.length > 0 && (
        <>
          <div className="nt-h"><h3>{fill(t("st_star_essays_n"), { n: res.answers.length })}</h3></div>
          <section className="card es-group">
            {res.answers.map((e) => (
              <div className="nt-star" key={e.answerId}>
                <div className="m">{e.question}<div className="s">{e.topper.name}{e.source ? ` · ${e.source}` : ""}</div></div>
                {e.words > 0
                  ? <button className="btn btn-sm btn-ghost" style={{ width: "auto" }} onClick={() => openText(e)}><FileText size={14} />{t("es_read_text")}</button>
                  : <button className="btn btn-sm btn-ghost" style={{ width: "auto" }} onClick={() => open(e)}>{t("es_open")}</button>}
                <StarButton on onClick={() => toggleMark("answer", e.answerId, "starred")} t={t} />
              </div>
            ))}
          </section>
        </>
      )}

      {res.key === key && res.snippets.length > 0 && (
        <>
          <div className="nt-h"><h3>{fill(t("st_star_snips_n"), { n: res.snippets.length })}</h3></div>
          {res.snippets.map((s) => <SnippetRow key={s.id} s={s} ctx={ctx} />)}
        </>
      )}
    </div>
  );
}
