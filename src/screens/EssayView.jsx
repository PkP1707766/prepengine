import { useState, useEffect, useMemo, useCallback } from "react";
import { ChevronLeft, ChevronRight, ChevronDown, Lock, ExternalLink, BookOpen, Search, X, PenLine, FileText, GraduationCap, Check, Filter, BarChart3 } from "lucide-react";
import { useLang } from "../lib/contexts.js";
import { EmptyState, ErrorState, SkeletonCards } from "../ui/Feedback.jsx";
import CopyViewer from "../ui/CopyViewer.jsx";
import * as DB from "../lib/db.js";
import { loadKey, saveKey } from "../lib/storage.js";
import {
  STUDY_CSS, StudyStrip, StarButton, NoteButton, DoneButton, NoteModal,
  LtwPanel, PyqSnippets, WikiTab, NotesTab,
} from "./EssayStudy.jsx";

/* ============================================================
   VIEW: ESSAY  (Mains, slice 1)

   The Essay paper has no syllabus, so the themes are the syllabus:
   pick one, see every UPSC topic in it, and read how toppers wrote
   on that topic or a close cousin of it. Each essay opens at the
   page where it starts -- in the in-app reader when we host the
   copy, or in the publisher's own PDF at #page=N when we only
   link to it.

   Four tabs: Essay PYQs (theme or year rail + cards → one PYQ's
   topper essays, Learn to Write and wiki), Topper essays (the whole
   library, by marks or year), the Essay Wiki (openings, quotes,
   stories by theme) and My notes (stars and the student's notes).
   The study tools live in EssayStudy.jsx.
   ============================================================ */

const ES_CSS = `
.es-head{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:14px}
.es-head .tabs{margin-bottom:0}
.es-note{display:flex;align-items:center;gap:10px;flex-wrap:wrap;font-size:12.5px;color:var(--muted);
  background:var(--amb-bg);border:1px solid var(--line);border-radius:10px;padding:9px 12px;margin-bottom:16px}
.es-note .btn{width:auto}
.es-grid{display:grid;grid-template-columns:250px minmax(0,1fr);gap:18px;align-items:start}
.es-rail{position:sticky;top:84px;max-height:calc(100vh - 110px);overflow:auto;padding:12px}
.es-seg{display:grid;grid-template-columns:1fr 1fr;gap:4px;background:var(--hair);border:1px solid var(--line);border-radius:10px;padding:3px;margin-bottom:10px}
.es-seg button{font-size:12.5px;font-weight:700;padding:7px 6px;border-radius:7px;color:var(--muted)}
.es-seg button.on{background:var(--card);color:var(--ink);box-shadow:0 1px 3px rgba(0,0,0,.08)}
.es-rail-item{display:flex;align-items:center;justify-content:space-between;gap:8px;width:100%;text-align:left;
  font-size:13px;font-weight:600;color:var(--ink);padding:8px 10px;border-radius:8px;line-height:1.35}
.es-rail-item:hover{background:var(--hair)}
.es-rail-item.on{background:var(--navy);color:#ffffff}
.es-rail-item .n{font-size:11px;font-weight:700;font-variant-numeric:tabular-nums;flex-shrink:0;white-space:nowrap;
  padding:2px 8px;border-radius:999px;background:var(--hair);border:1px solid var(--line);color:var(--ink)}
/* A rail item: its name, then "x% completed" and its count, then a bar. */
.es-rail-item{flex-direction:column;align-items:stretch;gap:6px;padding:10px 10px 11px;border-bottom:1px solid var(--line);border-radius:0}
.es-rail-item.on{border-radius:8px;border-bottom-color:transparent}
.es-ri-name{display:block}
.es-ri-meta{display:flex;align-items:center;justify-content:space-between;gap:8px}
.es-ri-pct{font-size:11px;font-weight:700;padding:2px 8px;border-radius:999px;border:1px solid var(--line);color:var(--muted);background:var(--card)}
.es-rail-item.on .es-ri-pct,.es-rail-item.on .n{background:rgba(255,255,255,.14);border-color:rgba(255,255,255,.3);color:#fff}
.es-ri-bar{display:block;height:4px;border-radius:999px;background:var(--line);overflow:hidden}
.es-ri-bar span{display:block;height:100%;border-radius:inherit;background:var(--green);transition:width .3s}
.es-rail-item.on .es-ri-bar{background:rgba(255,255,255,.25)}
.es-rail-item.on .es-ri-bar span{background:#fff}
.es-ri-bar.big{height:6px;margin-top:8px}
.es-rail-search{margin-bottom:8px}
.es-rail-search input{padding:8px 0;font-size:13px}
.es-rail-search button{display:grid;place-items:center;color:var(--muted)}
.es-grid.rail-shut{grid-template-columns:minmax(0,1fr)}
.es-sel-head{display:flex;align-items:flex-start;gap:12px;padding:2px 2px 14px;margin-bottom:14px;border-bottom:1px solid var(--line)}
.es-rail-toggle{flex:none;width:30px;height:30px;border-radius:50%;display:grid;place-items:center;border:1px solid var(--line);
  background:var(--card);color:var(--ink);margin-top:2px}
.es-rail-toggle:hover{border-color:var(--gold-2)}
.es-sel-main{flex:1;min-width:0}
.es-sel-title{font-size:15px;font-weight:800;color:var(--ink);line-height:1.4}
.es-sel-title span{font-weight:600;color:var(--muted)}
.es-sel-prog{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:6px;font-size:12.5px;font-weight:700;color:var(--muted)}
.es-sel-prog span{display:inline-flex;align-items:center;gap:5px}
.es-sel-count{color:var(--green)}
.es-prog-btn{flex:none;width:auto}
.es-filters{padding:0;margin-bottom:14px;overflow:hidden}
.es-filters-h{display:flex;align-items:center;gap:8px;width:100%;padding:11px 14px;font-size:13.5px;font-weight:700;color:var(--ink);text-align:left}
.es-filters-on{font-size:11px;font-weight:800;padding:2px 8px;border-radius:999px;background:var(--amb-bg);color:var(--gold-2)}
.es-chev{margin-left:auto;transition:transform .2s;color:var(--muted)}
.es-chev.up{transform:rotate(180deg)}
.es-filters-body{display:flex;flex-direction:column;gap:10px;padding:2px 14px 14px;border-top:1px solid var(--line);padding-top:12px}
.es-fgroup{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.es-fgroup > span{font-size:12px;font-weight:700;color:var(--muted);min-width:64px}
.es-pill{font-size:12.5px;font-weight:700;padding:5px 12px;border-radius:999px;border:1.5px solid var(--line);color:var(--muted);background:var(--card)}
.es-pill.on{border-color:var(--navy-2);color:var(--navy-2);background:var(--amb-bg)}
.es-clear{align-self:flex-start;font-size:12.5px;font-weight:700;color:var(--navy);text-decoration:underline}
.es-year-btn{display:flex;align-items:center;gap:10px;width:100%;text-align:left}
.es-year-line{flex:1;height:1px;background:var(--line)}
.es-tags{font-size:12px;font-weight:600;color:var(--muted);line-height:1.45;min-width:0}
.es-done-tick{display:inline-flex;align-items:center;gap:6px;flex:none;font-size:12.5px;font-weight:700;color:var(--muted)}
.es-done-tick .o{width:16px;height:16px;border-radius:50%;border:1.5px solid currentColor;display:grid;place-items:center}
.es-done-tick.on{color:var(--green)}
.es-done-tick.on .o{background:var(--green);border-color:var(--green);color:#fff}
.es-card.is-done{border-color:color-mix(in srgb,var(--green) 40%,var(--line))}
.es-qsuffix{font-weight:600;color:var(--muted);white-space:nowrap}
.es-card .es-actions{border-top:1px solid var(--line);padding-top:12px;align-items:center}
.modal.es-prog-modal{max-width:560px;width:calc(100% - 28px);max-height:calc(100vh - 40px);display:flex;flex-direction:column}
.es-prog-modal .modal-body{overflow:auto;flex:1;min-height:0}
.es-prog-total{margin-bottom:14px;font-size:14px;color:var(--ink)}
.es-prog-row{display:grid;grid-template-columns:minmax(0,1fr) 110px 52px;align-items:center;gap:10px;width:100%;text-align:left;
  padding:9px 4px;border-bottom:1px solid var(--line);font-size:13px;color:var(--ink)}
.es-prog-row:hover{background:var(--hair)}
.es-prog-row .c{font-size:12px;font-weight:700;color:var(--muted);text-align:right;font-variant-numeric:tabular-nums}
.es-pick{display:none;margin-bottom:12px}
.es-pick select,.es-tool select{width:100%;padding:10px 12px;border:1.5px solid var(--line);border-radius:9px;
  background:var(--card);color:var(--ink);font:inherit;font-size:13.5px}
.es-year{font-size:12px;font-weight:800;letter-spacing:.12em;color:var(--gold-2);margin:18px 2px 8px}
.es-year:first-child{margin-top:0}
.es-cards{display:flex;flex-direction:column;gap:10px}
.es-card{padding:16px 18px}
.es-card-top{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:8px}
.es-chip{display:inline-flex;align-items:center;font-size:11.5px;font-weight:700;padding:3px 9px;border-radius:999px;
  background:var(--hair);color:var(--muted);border:1px solid var(--line);line-height:1.4}
.es-chip.es-lead{background:var(--amb-bg);color:var(--ink);border-color:transparent}
.es-yr{font-size:12px;font-weight:700;color:var(--muted);font-variant-numeric:tabular-nums}
.es-topic{font-size:15.5px;font-weight:700;line-height:1.45;color:var(--ink)}
.es-topic.hi{font-family:var(--font-deva,serif)}
.es-also{display:flex;align-items:center;gap:6px;flex-wrap:wrap;margin-top:8px;font-size:12px;color:var(--muted)}
.es-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}
.es-actions .btn{width:auto}
.es-back{display:inline-flex;align-items:center;gap:4px;font-size:13px;font-weight:700;color:var(--navy);margin-bottom:12px}
.es-detail-head{padding:18px 20px;margin-bottom:14px}
.es-detail-head .es-topic{font-size:18px}
/* A GS question can be a 400-word case study: a card shows its opening, the
   question page all of it at reading size. */
.es-clamp{display:-webkit-box;-webkit-line-clamp:4;line-clamp:4;-webkit-box-orient:vertical;overflow:hidden}
.es-detail-head .es-topic.es-long{font-size:16px;font-weight:600;line-height:1.6}
.es-qmeta{font-size:12.5px;font-weight:700;color:var(--muted);margin-top:6px}
.es-group{margin-bottom:14px;overflow:hidden}
.es-group-head{display:flex;align-items:baseline;justify-content:space-between;gap:10px;flex-wrap:wrap;
  padding:12px 18px;background:var(--hair);border-bottom:1px solid var(--line)}
.es-group-head .k{font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--gold-2)}
.es-group-head .q{font-size:14px;font-weight:700;color:var(--ink);margin-top:2px}
.es-group-head .c{font-size:12px;color:var(--muted);white-space:nowrap}
.es-entry{display:flex;align-items:center;gap:14px;padding:12px 18px;border-bottom:1px solid var(--line)}
.es-entry:last-child{border-bottom:none}
.es-entry-main{flex:1;min-width:0}
.es-entry-q{font-size:14px;font-weight:700;color:var(--ink);line-height:1.4;margin-bottom:3px}
.es-entry-name{font-size:13.5px;font-weight:700;color:var(--ink)}
.es-entry-meta{display:flex;flex-wrap:wrap;gap:4px 12px;font-size:12px;color:var(--muted);margin-top:3px}
.es-entry-meta .marks{color:var(--ink);font-weight:700}
.es-entry .btn{width:auto;flex:0 0 auto}
.es-free{color:var(--green);font-weight:700}
.es-foot{font-size:12px;color:var(--muted);margin:4px 2px 0}
.es-tools{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:14px}
.es-tool{min-width:150px}
.es-tool.grow{flex:1;min-width:200px}
.es-search{display:flex;align-items:center;gap:8px;border:1.5px solid var(--line);border-radius:9px;background:var(--card);padding:0 10px;color:var(--muted)}
.es-search input{flex:1;border:0;background:transparent;color:var(--ink);font:inherit;font-size:13.5px;padding:10px 0;outline:none;min-width:0}
.es-more{display:flex;justify-content:center;margin-top:14px}
.es-more .btn{width:auto}
.es-entry-acts{display:flex;align-items:center;gap:8px;flex:0 0 auto}
.modal.es-text-modal{max-width:760px;width:calc(100% - 28px);max-height:calc(100vh - 40px);display:flex;flex-direction:column}
.es-text-modal .modal-body{overflow:auto;flex:1;min-height:0}
.es-text-modal .modal-head h3{line-height:1.35}
.es-text-by{font-size:12.5px;color:var(--muted);margin-top:4px}
.es-text-note{font-size:12.5px;line-height:1.55;color:var(--muted);background:var(--amb-bg);border:1px solid var(--line);
  border-radius:9px;padding:8px 11px;margin:0 0 18px}
.es-text p{font-family:Georgia,"Times New Roman",serif;font-size:16.5px;line-height:1.75;color:var(--ink);margin:0 0 14px}
.es-text p:last-child{margin-bottom:0}
.es-text-none{font-size:14px;color:var(--muted)}
@media(max-width:860px){
  .es-grid{grid-template-columns:minmax(0,1fr)}
  .es-rail{display:none}
  .es-pick{display:block}
}
@media(max-width:560px){
  .es-entry{flex-direction:column;align-items:stretch;gap:10px}
  .es-entry .btn{width:100%}
  .es-entry-acts{flex-direction:column;align-items:stretch}
  .es-text p{font-size:16px;line-height:1.7}
}
`;

/* A PYQ page leads with this many topic groups; the rest are one tap away. */
const PYQ_GROUPS_SHOWN = 6;

const fill = (s, vars) => Object.entries(vars).reduce((out, [k, v]) => out.split(`{${k}}`).join(String(v)), s);

const TABS = [["pyqs", "es_tab_pyqs"], ["copies", "es_tab_copies"], ["wiki", "es_tab_wiki"], ["notes", "es_tab_notes"]];
/* A GS paper is the same screen with its own words: toppers write answers
   there, not essays, and PYQs are filed under syllabus topics, not themes.
   Each key on the left reads as the key on the right when the paper is GS. */
const GS_TEXT = {
  es_rail_search: "gs_rail_search", es_tab_pyqs: "gs_tab_pyqs", es_tab_copies: "gs_tab_copies", es_by_theme: "gs_by_topic", es_all_themes: "gs_all_topics",
  es_theme_label: "gs_topic_label", es_read_n: "gs_read_n", es_read_one: "gs_read_one", es_no_essays: "gs_no_answers",
  es_empty_title: "gs_empty_title", es_empty_text: "gs_empty_text", es_theme_empty: "gs_topic_empty",
  es_related_q: "gs_test_q", es_n_essays: "gs_n_answers", es_one_essay: "gs_one_answer", es_marks_note: "gs_answers_note",
  es_pyq_no_essays: "gs_pyq_no_answers", es_more_topics: "gs_more_questions", es_access_note: "gs_access_note",
  es_locked_title: "gs_locked_title", es_locked_text: "gs_locked_text",
  st_sec_essays: "gs_sec_answers", st_sec_essays_n: "gs_sec_answers_n",
  es_copies_empty_text: "gs_copies_empty_text", es_copies_empty_title: "gs_copies_empty_title", es_load_fail: "gs_load_fail",
  es_search_copies: "gs_search_copies", st_done_pyqs: "gs_done_pyqs", st_streak_hint: "gs_streak_hint",
  es_tab_wiki: "gs_tab_wiki", st_sec_wiki: "gs_sec_wiki", wk_editor_pick: "gs_wk_editor_pick", wk_pyq_none: "gs_wk_pyq_none",
  wk_none_here: "gs_wk_none_here", wk_empty_title: "gs_wk_empty_title", wk_empty_text: "gs_wk_empty_text", wk_search: "gs_wk_search",
  wk_locked: "gs_wk_locked", wk_locked_text: "gs_wk_locked_text", wk_fail: "gs_wk_fail",
  wk_fits_one: "gs_wk_fits_one", wk_fits_n: "gs_wk_fits_n",
};
/* A GS topic gathers a hundred or more test questions: shown a dozen at a time. */
const GS_GROUPS_STEP = 12;
const EMPTY_MARKS = { pyq: new Map(), answer: new Map(), snippet: new Map() };

export default function EssayView({ onBrowse, paper = "essay" }) {
  const { t: t0, lang } = useLang();
  const gs = paper !== "essay";
  const t = useCallback((k) => t0(gs && GS_TEXT[k] ? GS_TEXT[k] : k), [gs, t0]);
  // A GS paper's wiki is its Fact Bank: the same tab, with GS card types.
  const tabs = TABS;
  const [tab, setTab] = useState(() => {
    const k = loadKey(`${paper}:tab`, "pyqs");
    return tabs.some(([x]) => x === k) ? k : "pyqs";
  });
  const [data, setData] = useState(null);
  const [err, setErr] = useState("");
  const [reload, setReload] = useState(0);
  const [openPyq, setOpenPyq] = useState(null);   // { pyq, section }
  const [reader, setReader] = useState(null);
  const [locked, setLocked] = useState(null);
  const [textOf, setTextOf] = useState(null);
  const [marks, setMarks] = useState(EMPTY_MARKS);
  const [notes, setNotes] = useState([]);
  const [streak, setStreak] = useState(0);
  const [noteDraft, setNoteDraft] = useState(null);

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        // The study tools are extras: if they fail, the library still opens.
        const soft = (p, empty) => p.catch((e) => { console.warn("essay study data unavailable", e); return empty; });
        const [themes, pyqs, access, ltwReady, myMarks, myNotes, days] = await Promise.all([
          DB.essayThemes(paper), DB.essayPyqs({ paper }), DB.paperAccess(paper),
          soft(DB.essayLtwReady(), new Set()), soft(DB.essayMyMarks(), EMPTY_MARKS),
          soft(DB.essayNotes(), []), soft(DB.essayActivityDays(), []),
        ]);
        if (alive) {
          setData({ themes, pyqs, access, ltwReady });
          setMarks(myMarks); setNotes(myNotes); setStreak(DB.essayStreak(days)); setErr("");
        }
      } catch (e) {
        console.error("essay load failed", e);
        if (alive) setErr(e?.message || t("es_load_fail"));
      }
    })();
    return () => { alive = false; };
    // t is left out on purpose: a language toggle must not refetch.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [reload]);

  const switchTab = (k) => { setTab(k); saveKey(`${paper}:tab`, k); setOpenPyq(null); };
  const openPyqAt = useCallback((pyq, section = "essays") => {
    setTab("pyqs"); saveKey(`${paper}:tab`, "pyqs"); setOpenPyq({ pyq, section });
  }, [paper]);

  const themeName = useCallback((th) => (lang === "hi" && th?.nameHi ? th.nameHi : th?.name || ""), [lang]);
  const topicOf = useCallback((p) => (lang === "hi" && p.topicHi ? p.topicHi : p.topic), [lang]);

  const open = useCallback((entry) => {
    if (!entry.isFree && !data?.access) { setLocked(entry); return; }
    if (entry.hosted) setReader(entry);
  }, [data]);
  // The text is the copy, so it carries the copy's lock.
  const openText = useCallback((entry) => {
    if (!entry.isFree && !data?.access) { setLocked(entry); return; }
    setTextOf(entry);
  }, [data]);

  const refreshStreak = useCallback(() => {
    DB.essayActivityDays().then((days) => setStreak(DB.essayStreak(days)), () => {});
  }, []);

  /* Star or finish something: shown at once, undone if the save fails. */
  const toggleMark = useCallback((kind, id, field) => {
    const before = marks[kind].get(id) || null;
    const cur = before || { starred: false, done: false, doneAt: null };
    const next = { ...cur, [field]: !cur[field] };
    const apply = (val) => setMarks((m) => {
      const map = new Map(m[kind]);
      if (!val || (!val.starred && !val.done)) map.delete(id); else map.set(id, val);
      return { ...m, [kind]: map };
    });
    apply(next);
    DB.setEssayMark(kind, id, next).then(
      () => { if (field === "done") refreshStreak(); },
      (e) => { console.error("essay mark failed", e); apply(before); },
    );
  }, [marks, refreshStreak]);

  const notesFor = useCallback((kind, id) => notes.filter((n) => n.kind === kind && n.itemId === id), [notes]);
  // One note per item: the pencil opens the existing one if there is one.
  const editNote = useCallback((draft) => {
    const existing = !draft.id && draft.kind !== "free" ? notes.find((n) => n.kind === draft.kind && n.itemId === draft.itemId) : null;
    setNoteDraft(existing || draft);
  }, [notes]);
  const onNoteSaved = (n) => {
    setNotes((list) => [n, ...list.filter((x) => x.id !== n.id)]);
    setNoteDraft(null);
  };
  const onNoteDeleted = (id) => { setNotes((list) => list.filter((x) => x.id !== id)); setNoteDraft(null); };

  const pyqById = useMemo(() => new Map((data?.pyqs || []).map((p) => [p.id, p])), [data]);

  if (err) return <div className="card card-pad"><ErrorState message={err} onRetry={() => { setErr(""); setData(null); setReload((n) => n + 1); }} /></div>;
  if (!data) return <SkeletonCards count={3} height={120} />;

  const ctx = {
    t, lang, paper, gs, themeName, topicOf, access: data.access, open, openText, onBrowse,
    marks, toggleMark, notes, notesFor, editNote, openPyq: openPyqAt, pyqById, ltwReady: data.ltwReady,
  };

  return (
    <div>
      <style>{ES_CSS}</style>
      <style>{STUDY_CSS}</style>
      <div className="es-head">
        <div className="tabs">
          {tabs.map(([k, key]) => (
            <button key={k} className={"tab" + (tab === k ? " active" : "")} onClick={() => switchTab(k)}>{t(key)}</button>
          ))}
        </div>
      </div>
      {!data.access && tab !== "notes" && tab !== "wiki" && (
        <div className="es-note">
          <Lock size={15} /><span style={{ flex: 1, minWidth: 200 }}>{t("es_access_note")}</span>
          {onBrowse && <button className="btn btn-sm btn-ghost" onClick={onBrowse}>{t("es_see_bundles")}</button>}
        </div>
      )}

      {tab === "pyqs" && (openPyq
        ? <PyqDetail key={openPyq.pyq.id} pyq={openPyq.pyq} section={openPyq.section} themes={data.themes}
                     onSection={(s) => setOpenPyq((o) => ({ ...o, section: s }))} onBack={() => setOpenPyq(null)} ctx={ctx} {...ctx} />
        : (
          <>
            <StudyStrip pyqs={data.pyqs} marks={marks} streak={streak} notesCount={notes.length} onNotes={() => switchTab("notes")} t={t} />
            <PyqList themes={data.themes} pyqs={data.pyqs} onOpen={openPyqAt} {...ctx} />
          </>
        ))}
      {tab === "copies" && <CopiesTab {...ctx} />}
      {tab === "wiki" && <WikiTab themes={data.themes} pyqs={data.pyqs} ctx={ctx} />}
      {tab === "notes" && <NotesTab pyqs={data.pyqs} ctx={ctx} />}

      {reader && (
        <CopyViewer
          copyId={reader.copyId}
          pageCount={reader.pageCount}
          startPage={reader.startPage}
          endPage={reader.endPage}
          title={reader.question}
          subtitle={[reader.topper.name, reader.source, reader.writtenYear].filter(Boolean).join(" · ")}
          onClose={() => setReader(null)}
        />
      )}
      {locked && <LockedModal entry={locked} onClose={() => setLocked(null)} onBrowse={onBrowse} t={t} />}
      {textOf && (
        <TextReader entry={textOf} t={t} onClose={() => setTextOf(null)}
          onOpenCopy={(e) => { setTextOf(null); open(e); }}
          starred={!!marks.answer.get(textOf.answerId)?.starred}
          onStar={() => toggleMark("answer", textOf.answerId, "starred")}
          noteCount={notesFor("answer", textOf.answerId).length}
          onNote={() => editNote({ kind: "answer", itemId: textOf.answerId, label: `${textOf.question} · ${textOf.topper.name}` })}
          onRead={refreshStreak} />
      )}
      {/* Last, so it sits above the text reader it can be opened from. */}
      {noteDraft && <NoteModal draft={noteDraft} t={t} onClose={() => setNoteDraft(null)} onSaved={onNoteSaved} onDeleted={onNoteDeleted} />}
    </div>
  );
}

/* ---------------------------------------------------------------- PYQs -- */

/* "2025 · Q3(b)" for a GS question; "2025 · A" for an essay in a section. */
const pyqTag = (p, gs) => (gs
  ? `${p.year} · Q${p.qNo ?? ""}${p.section ? `(${p.section})` : ""}`
  : p.section ? `${p.year} · ${p.section}` : String(p.year));

function PyqList({ themes, pyqs, onOpen, t, themeName, topicOf, lang, marks, toggleMark, ltwReady, paper, gs }) {
  const [mode, setMode] = useState(() => (loadKey(`${paper}:mode`, "theme") === "year" ? "year" : "theme"));
  const [pick, setPick] = useState(() => loadKey(`${paper}:pick`, "all"));
  const [railOpen, setRailOpen] = useState(() => loadKey(`${paper}:rail`, "open") !== "closed");
  const [railQ, setRailQ] = useState("");
  const [filtersOpen, setFiltersOpen] = useState(false);
  const [status, setStatus] = useState("all");      // all | todo | done | starred
  const [guideOnly, setGuideOnly] = useState(false);
  const [markF, setMarkF] = useState("all");
  const [sort, setSort] = useState("new");
  const [shut, setShut] = useState(() => new Set()); // years folded away
  const [progressOpen, setProgressOpen] = useState(false);
  const byId = useMemo(() => new Map(themes.map((th) => [th.id, th])), [themes]);
  const isDone = useCallback((p) => !!marks.pyq.get(p.id)?.done, [marks]);

  const themeCounts = useMemo(() => {
    const m = new Map();
    pyqs.forEach((p) => p.themes.forEach((x) => m.set(x.id, (m.get(x.id) || 0) + 1)));
    return m;
  }, [pyqs]);
  const doneIn = useCallback((list) => list.filter(isDone).length, [isDone]);
  const railThemes = useMemo(() => themes
    .filter((th) => themeCounts.get(th.id))
    // Essay themes by size; GS topics in the order the syllabus lists them.
    .sort((a, b) => (gs ? a.sortOrder - b.sortOrder : themeCounts.get(b.id) - themeCounts.get(a.id)) || themeName(a).localeCompare(themeName(b))),
  [themes, themeCounts, themeName, gs]);
  const years = useMemo(() => {
    const m = new Map();
    pyqs.forEach((p) => m.set(p.year, (m.get(p.year) || 0) + 1));
    return [...m].sort((a, b) => b[0] - a[0]);
  }, [pyqs]);

  const setModeKeep = (m) => { setMode(m); setPick("all"); saveKey(`${paper}:mode`, m); saveKey(`${paper}:pick`, "all"); };
  const choose = (v) => { setPick(v); saveKey(`${paper}:pick`, v); };
  const toggleRail = () => setRailOpen((o) => { saveKey(`${paper}:rail`, o ? "closed" : "open"); return !o; });
  // A remembered pick that no longer exists (a theme renamed away) falls back to all.
  const valid = pick === "all"
    || (mode === "theme" ? themeCounts.has(pick) : years.some(([y]) => String(y) === String(pick)));
  const active = valid ? pick : "all";
  const inPick = (p) => active === "all"
    || (mode === "theme" ? p.themes.some((x) => x.id === active) : String(p.year) === String(active));
  const picked = pyqs.filter(inPick);

  const markOptions = useMemo(() => [...new Set(pyqs.map((p) => p.marks).filter(Boolean))].sort((a, b) => a - b), [pyqs]);
  const filtersOn = status !== "all" || guideOnly || markF !== "all";
  const shown = picked.filter((p) => (status === "all" || (status === "done" ? isDone(p)
      : status === "todo" ? !isDone(p) : !!marks.pyq.get(p.id)?.starred))
    && (!guideOnly || ltwReady.has(p.id))
    && (markF === "all" || String(p.marks) === markF));
  const groups = [];
  (sort === "old" ? [...shown].reverse() : shown).forEach((p) => {
    const last = groups[groups.length - 1];
    if (last && last.year === p.year) last.items.push(p);
    else groups.push({ year: p.year, items: [p] });
  });

  if (pyqs.length === 0) {
    return <div className="card card-pad"><EmptyState icon={<PenLine size={26} />} title={t("es_empty_title")} text={t("es_empty_text")} /></div>;
  }

  // [id, label, pyqs in it]
  const railItems = mode === "theme"
    ? [["all", t("es_all_themes"), pyqs], ...railThemes.map((th) => [th.id, themeName(th), pyqs.filter((p) => p.themes.some((x) => x.id === th.id))])]
    : [["all", t("es_all_years"), pyqs], ...years.map(([y]) => [String(y), String(y), pyqs.filter((p) => p.year === y)])];
  const needle = railQ.trim().toLowerCase();
  const railShown = needle ? railItems.filter(([id, label]) => id === "all" || label.toLowerCase().includes(needle)) : railItems;
  const activeLabel = railItems.find(([id]) => id === active)?.[1] || "";
  const pct = (list) => (list.length ? Math.round((doneIn(list) / list.length) * 100) : 0);
  const qTag = (p) => (gs && p.qNo ? `Q${p.qNo}${p.section ? `(${p.section})` : ""}) ` : "");

  return (
    <div className={"es-grid" + (railOpen ? "" : " rail-shut")}>
      {railOpen && (
        <aside className="card es-rail">
          <div className="es-seg" role="tablist">
            <button className={mode === "theme" ? "on" : ""} onClick={() => setModeKeep("theme")}>{t("es_by_theme")}</button>
            <button className={mode === "year" ? "on" : ""} onClick={() => setModeKeep("year")}>{t("es_by_year")}</button>
          </div>
          <label className="es-search es-rail-search">
            <Search size={14} />
            <input value={railQ} onChange={(e) => setRailQ(e.target.value)} placeholder={t(mode === "theme" ? "es_rail_search" : "es_rail_search_y")} />
            {railQ && <button onClick={() => setRailQ("")} aria-label={t("es_clear")}><X size={14} /></button>}
          </label>
          {railShown.map(([id, label, list]) => {
            const p = pct(list);
            return (
              <button key={id} className={"es-rail-item" + (active === id ? " on" : "")} onClick={() => choose(id)}
                      aria-current={active === id ? "true" : undefined}>
                <span className="es-ri-name">{label}</span>
                <span className="es-ri-meta">
                  <span className="es-ri-pct">{fill(t("es_pct_done"), { p })}</span>
                  <span className="n">{list.length === 1 ? t("es_n_pyq_one") : fill(t("es_n_pyqs"), { n: list.length })}</span>
                </span>
                <span className="es-ri-bar"><span style={{ width: `${p}%` }} /></span>
              </button>
            );
          })}
        </aside>
      )}

      <div style={{ minWidth: 0 }}>
        <div className="es-pick">
          <div className="es-seg">
            <button className={mode === "theme" ? "on" : ""} onClick={() => setModeKeep("theme")}>{t("es_by_theme")}</button>
            <button className={mode === "year" ? "on" : ""} onClick={() => setModeKeep("year")}>{t("es_by_year")}</button>
          </div>
          <select value={active} onChange={(e) => choose(e.target.value)} aria-label={mode === "theme" ? t("es_theme_label") : t("es_year_label")}>
            {railItems.map(([id, label, list]) => <option key={id} value={id}>{label} ({list.length})</option>)}
          </select>
        </div>

        <div className="es-sel-head">
          <button className="es-rail-toggle" onClick={toggleRail} aria-label={t(railOpen ? "es_hide_rail" : "es_show_rail")} title={t(railOpen ? "es_hide_rail" : "es_show_rail")}>
            {railOpen ? <ChevronLeft size={16} /> : <ChevronRight size={16} />}
          </button>
          <div className="es-sel-main">
            <div className="es-sel-title"><span>{t(mode === "theme" ? "es_theme_label" : "es_year_label")}:</span> {activeLabel}</div>
            <div className="es-sel-prog">
              <span><Check size={13} /> {t("es_pyqs_completed")}</span>
              <span className="es-sel-count">{fill(t("es_done_of"), { d: doneIn(picked), n: picked.length })}</span>
            </div>
            <span className="es-ri-bar big"><span style={{ width: `${pct(picked)}%` }} /></span>
          </div>
          <button className="btn btn-sm btn-ghost es-prog-btn" onClick={() => setProgressOpen(true)}><BarChart3 size={14} />{t("es_progress")}</button>
        </div>

        <div className="card es-filters">
          <button className="es-filters-h" onClick={() => setFiltersOpen((o) => !o)} aria-expanded={filtersOpen}>
            <Filter size={14} />{t("es_filter_sort")}
            {filtersOn && <span className="es-filters-on">{t("es_filters_on")}</span>}
            <ChevronDown size={16} className={"es-chev" + (filtersOpen ? " up" : "")} />
          </button>
          {filtersOpen && (
            <div className="es-filters-body">
              <div className="es-fgroup">
                <span>{t("es_f_status")}</span>
                {[["all", "es_f_all"], ["todo", "es_f_todo"], ["done", "es_f_done"], ["starred", "es_f_starred"]].map(([k, key]) => (
                  <button key={k} className={"es-pill" + (status === k ? " on" : "")} onClick={() => setStatus(k)}>{t(key)}</button>
                ))}
              </div>
              {markOptions.length > 1 && (
                <div className="es-fgroup">
                  <span>{t("es_f_marks")}</span>
                  <button className={"es-pill" + (markF === "all" ? " on" : "")} onClick={() => setMarkF("all")}>{t("es_f_all")}</button>
                  {markOptions.map((m) => <button key={m} className={"es-pill" + (markF === String(m) ? " on" : "")} onClick={() => setMarkF(String(m))}>{m}M</button>)}
                </div>
              )}
              <div className="es-fgroup">
                <span>{t("es_f_sort")}</span>
                <button className={"es-pill" + (sort === "new" ? " on" : "")} onClick={() => setSort("new")}>{t("es_sort_new")}</button>
                <button className={"es-pill" + (sort === "old" ? " on" : "")} onClick={() => setSort("old")}>{t("es_sort_old")}</button>
                <button className={"es-pill" + (guideOnly ? " on" : "")} onClick={() => setGuideOnly((g) => !g)}>{t("es_f_guide")}</button>
              </div>
              {filtersOn && <button className="es-clear" onClick={() => { setStatus("all"); setGuideOnly(false); setMarkF("all"); }}>{t("es_clear")}</button>}
            </div>
          )}
        </div>

        {shown.length === 0 ? (
          <div className="card card-pad"><EmptyState compact title={t(filtersOn ? "es_no_filter_match" : "es_theme_empty")} /></div>
        ) : groups.map((g) => {
          const folded = shut.has(g.year);
          return (
            <div key={g.year}>
              <button className="es-year es-year-btn" onClick={() => setShut((s) => { const n = new Set(s); if (n.has(g.year)) n.delete(g.year); else n.add(g.year); return n; })}
                      aria-expanded={!folded}>
                <span>{g.year}</span><span className="es-year-line" /><ChevronDown size={15} className={"es-chev" + (folded ? "" : " up")} />
              </button>
              {!folded && (
                <div className="es-cards">
                  {g.items.map((p) => {
                    const tags = p.themes.map((x) => byId.get(x.id)).filter(Boolean);
                    const n = p.essayCount;
                    const mk = marks.pyq.get(p.id);
                    const ltw = ltwReady.has(p.id);
                    return (
                      <article className={"card es-card" + (mk?.done ? " is-done" : "")} key={p.id}>
                        <div className="es-card-top">
                          {/* Not "main": StudentApp's layout column is .main, and the two collided. */}
                          <span className="es-tags">{tags.map((th) => themeName(th)).join(" · ") || " "}</span>
                          <button className={"es-done-tick" + (mk?.done ? " on" : "")} onClick={() => toggleMark("pyq", p.id, "done")} aria-pressed={!!mk?.done}>
                            <span className="o">{mk?.done && <Check size={11} />}</span>{mk?.done ? t("st_done") : t("st_mark_done")}
                          </button>
                        </div>
                        <div className={"es-topic" + (gs ? " es-clamp" : "") + (lang === "hi" && p.topicHi ? " hi" : "")}>
                          {qTag(p)}{topicOf(p)}
                          <span className="es-qsuffix">{gs && p.marks ? ` (${p.marks}M, ${p.year})` : ` (${p.section ? `${p.year} · ${p.section}` : p.year})`}</span>
                        </div>
                        <div className="es-actions">
                          <button className={"btn btn-sm " + (n ? "btn-primary" : "btn-ghost")} disabled={!n} onClick={() => onOpen(p, "essays")}
                                  style={n ? undefined : { opacity: 0.7, cursor: "default" }}>
                            <BookOpen size={15} />
                            {n === 0 ? t("es_no_essays") : n === 1 ? t("es_read_one") : fill(t("es_read_n"), { n })}
                            {n > 0 && <ChevronRight size={15} />}
                          </button>
                          {ltw && (
                            <button className="btn btn-sm btn-ghost" onClick={() => onOpen(p, "ltw")}>
                              <GraduationCap size={15} />{t("ltw_btn")}
                            </button>
                          )}
                          <span style={{ marginLeft: "auto" }}><StarButton on={!!mk?.starred} onClick={() => toggleMark("pyq", p.id, "starred")} t={t} /></span>
                        </div>
                      </article>
                    );
                  })}
                </div>
              )}
            </div>
          );
        })}
      </div>

      {progressOpen && (
        <div className="overlay" onClick={() => setProgressOpen(false)}>
          <div className="modal es-prog-modal" onClick={(e) => e.stopPropagation()} role="dialog" aria-modal="true">
            <div className="modal-head">
              <h3>{t("es_progress_title")}</h3>
              <button className="x" onClick={() => setProgressOpen(false)} aria-label={t("es_v_close")}><X size={19} /></button>
            </div>
            <div className="modal-body">
              <div className="es-prog-total">
                <b>{fill(t("es_done_of"), { d: doneIn(pyqs), n: pyqs.length })}</b>
                <span className="es-ri-bar big"><span style={{ width: `${pct(pyqs)}%` }} /></span>
              </div>
              {(mode === "theme" ? railItems.slice(1) : railItems.slice(1)).map(([id, label, list]) => (
                <button key={id} className="es-prog-row" onClick={() => { choose(id); setProgressOpen(false); }}>
                  <span className="l">{label}</span>
                  <span className="es-ri-bar"><span style={{ width: `${pct(list)}%` }} /></span>
                  <span className="c">{doneIn(list)}/{list.length}</span>
                </button>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

function PyqDetail({ pyq, section, onSection, themes, onBack, ctx, t, lang, themeName, topicOf, access, open, openText,
  marks, toggleMark, notesFor, editNote, ltwReady, onBrowse, gs }) {
  const [groups, setGroups] = useState(null);
  const [err, setErr] = useState("");
  const [reload, setReload] = useState(0);
  const [shownN, setShownN] = useState(PYQ_GROUPS_SHOWN);
  const [readers, setReaders] = useState(new Map());
  const byId = useMemo(() => new Map(themes.map((th) => [th.id, th])), [themes]);

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const g = gs ? await DB.answersForPyq(pyq) : await DB.essaysForPyq(pyq.id);
        if (alive) { setGroups(g); setErr(""); }
        const counts = await DB.essayReaderCounts(g.flatMap((x) => x.entries.map((e) => e.answerId)));
        if (alive) setReaders(counts);
      } catch (e) {
        console.error("essays for pyq failed", e);
        if (alive) setErr(e?.message || "");
      }
    })();
    return () => { alive = false; };
    // pyq is read whole for GS (its topic and wording); its id says when it changes.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [pyq.id, reload, gs]);

  useEffect(() => { window.scrollTo({ top: 0 }); }, [pyq.id]);

  const entries = useMemo(() => new Map((groups || []).flatMap((g) => g.entries.map((e) => [e.answerId, e]))), [groups]);
  const total = entries.size;
  // Half the PYQs gather more than six topics (up to 36). The page leads with
  // the strongest ones -- same question first, then by confidence -- and the
  // rest wait behind one button.
  const visible = (groups || []).slice(0, shownN);
  const hidden = (groups || []).slice(visible.length);
  const hiddenEssays = hidden.reduce((n, g) => n + g.entries.length, 0);
  const mk = marks.pyq.get(pyq.id);
  const label = `${pyq.topic} (${pyq.year})`;
  // A GS question has its topic's answers, and a guide once one is written.
  const sections = gs ? [
    ["essays", total ? fill(t("st_sec_essays_n"), { n: total }) : t("st_sec_essays")],
    ...(ltwReady.has(pyq.id) ? [["ltw", t("ltw_btn")]] : []),
    ["wiki", t("st_sec_wiki")],
  ] : [
    ["essays", total ? fill(t("st_sec_essays_n"), { n: total }) : t("st_sec_essays")],
    ["ltw", t("ltw_btn")],
    ["wiki", t("st_sec_wiki")],
  ];
  // A PYQ with no guide and no essays still opens on its essays (empty) view;
  // the guide tab says when one is coming.
  const sec = sections.some(([k]) => k === section) ? section : (ltwReady.has(pyq.id) ? "ltw" : "essays");
  return (
    <div>
      <button className="es-back" onClick={onBack}><ChevronLeft size={16} />{t("es_back")}</button>
      <div className="card es-detail-head">
        <div className="es-card-top">
          <span style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
            {pyq.themes.map((x) => byId.get(x.id)).filter(Boolean).map((th, i) =>
              <span key={th.id} className={"es-chip" + (i === 0 ? " es-lead" : "")}>{themeName(th)}</span>)}
          </span>
          <span className="es-yr">{pyqTag(pyq, gs)}</span>
        </div>
        <div className={"es-topic" + (gs ? " es-long" : "") + (lang === "hi" && pyq.topicHi ? " hi" : "")}>{topicOf(pyq)}</div>
        {gs && pyq.marks != null && <div className="es-qmeta">{fill(t("gs_marks_words"), { m: pyq.marks, w: pyq.wordLimit ?? "" })}</div>}
        <div className="st-head-acts">
          <DoneButton on={!!mk?.done} onClick={() => toggleMark("pyq", pyq.id, "done")} t={t} />
          <StarButton on={!!mk?.starred} onClick={() => toggleMark("pyq", pyq.id, "starred")} t={t} />
          <NoteButton count={notesFor("pyq", pyq.id).length} onClick={() => editNote({ kind: "pyq", itemId: pyq.id, label })} t={t} />
        </div>
      </div>

      <div className="st-sec" role="tablist">
        {sections.map(([k, text]) => (
          <button key={k} className={sec === k ? "on" : ""} onClick={() => onSection(k)} role="tab" aria-selected={sec === k}>
            {text}
          </button>
        ))}
      </div>

      {sec === "ltw" && <LtwPanel pyq={pyq} entries={entries} onText={openText} onOpen={open} onBrowse={onBrowse} t={t} />}
      {sec === "wiki" && <PyqSnippets pyq={pyq} ctx={ctx} />}

      {sec === "essays" && (err ? <div className="card card-pad"><ErrorState message={err} onRetry={() => { setErr(""); setGroups(null); setReload((n) => n + 1); }} /></div>
        : groups === null ? <SkeletonCards count={2} height={140} />
        : total === 0 ? <div className="card card-pad"><EmptyState compact icon={<BookOpen size={24} />} title={t("es_pyq_no_essays")} /></div>
        : (
          <>
            {visible.map((g) => (
              <section className="card es-group" key={g.key}>
                <div className="es-group-head">
                  <div>
                    <div className="k">{g.kind === "exact" ? t("es_same_q") : t("es_related_q")}</div>
                    <div className="q">{g.question}</div>
                  </div>
                  <span className="c">{g.entries.length === 1 ? t("es_one_essay") : fill(t("es_n_essays"), { n: g.entries.length })}</span>
                </div>
                {g.entries.map((e) => (
                  <EntryRow key={e.answerId} e={e} access={access} onOpen={open} onText={openText} t={t}
                            readers={readers.get(e.answerId) || 0}
                            starred={!!marks.answer.get(e.answerId)?.starred} onStar={() => toggleMark("answer", e.answerId, "starred")} />
                ))}
              </section>
            ))}
            {hidden.length > 0 && (
              <div className="es-more">
                <button className="btn btn-ghost" onClick={() => setShownN((n) => (gs ? n + GS_GROUPS_STEP : Infinity))}>
                  {fill(t("es_more_topics"), { n: hidden.length, m: hiddenEssays })}
                </button>
              </div>
            )}
            <p className="es-foot">{t("es_marks_note")}</p>
          </>
        ))}
    </div>
  );
}

/* --------------------------------------------------------- the library -- */

function CopiesTab({ t, access, open, openText, marks, toggleMark, paper = "essay", gs = false }) {
  const [sort, setSort] = useState(() => {
    // GS toppers carry no paper-wise marks to sort by: newest first.
    const s = loadKey(`${paper}:sort`, gs ? "newest" : "marks");
    return ["marks", "newest", "oldest"].includes(s) ? s : "marks";
  });
  const [year, setYear] = useState("");
  const [q, setQ] = useState("");
  const [needle, setNeedle] = useState("");
  const [years, setYears] = useState([]);
  const [busy, setBusy] = useState(false);
  const [reload, setReload] = useState(0);

  // Each result remembers the query that produced it; while it belongs to an
  // older query the list shows as loading. No state is reset in the effect.
  // Until some essay has a year, newest/oldest have nothing to order by.
  const effSort = years.length > 0 ? sort : "marks";
  const queryKey = `${effSort}|${year}|${needle}|${reload}`;
  const [page, setPage] = useState({ key: null, items: [], total: 0, err: "" });
  const loading = page.key !== queryKey;

  useEffect(() => { DB.topperLibraryYears(paper).then(setYears).catch(() => setYears([])); }, [paper]);
  // Typing should not fire a query per keystroke.
  useEffect(() => { const id = setTimeout(() => setNeedle(q.trim()), 300); return () => clearTimeout(id); }, [q]);

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const r = await DB.topperLibrary({ paper, sort: effSort, year: year ? Number(year) : null, q: needle, offset: 0, limit: 24 });
        const readers = await DB.essayReaderCounts(r.items.map((e) => e.answerId));
        if (alive) setPage({ key: queryKey, items: r.items, total: r.total, err: "", readers });
      } catch (e) {
        console.error("topper library failed", e);
        if (alive) setPage({ key: queryKey, items: [], total: 0, err: e?.message || " " });
      }
    })();
    return () => { alive = false; };
  }, [effSort, year, needle, queryKey, paper]);

  const more = async () => {
    setBusy(true);
    try {
      const r = await DB.topperLibrary({ paper, sort: effSort, year: year ? Number(year) : null, q: needle, offset: page.items.length, limit: 24 });
      const readers = await DB.essayReaderCounts(r.items.map((e) => e.answerId));
      setPage((p) => ({ ...p, items: [...p.items, ...r.items], total: r.total, readers: new Map([...(p.readers || []), ...readers]) }));
    } catch (e) { console.error(e); }
    setBusy(false);
  };

  const changeSort = (s) => { setSort(s); saveKey(`${paper}:sort`, s); };
  // A year filter with no years in it is noise: shown only once there are some.
  const hasYears = years.length > 0;

  return (
    <div>
      <div className="es-tools">
        <label className="es-tool grow es-search">
          <Search size={15} />
          <input value={q} onChange={(e) => setQ(e.target.value)} placeholder={t("es_search_copies")} aria-label={t("es_search_copies")} />
          {q && <button onClick={() => setQ("")} aria-label={t("es_v_close")} style={{ color: "var(--muted)", display: "grid" }}><X size={15} /></button>}
        </label>
        <div className="es-tool">
          <select value={effSort} onChange={(e) => changeSort(e.target.value)} aria-label={t("es_sort_label")}>
            {!gs && <option value="marks">{t("es_sort_marks")}</option>}
            {hasYears && <option value="newest">{t("es_sort_new")}</option>}
            {hasYears && <option value="oldest">{t("es_sort_old")}</option>}
          </select>
        </div>
        {hasYears && (
          <div className="es-tool">
            <select value={year} onChange={(e) => setYear(e.target.value)} aria-label={t("es_year_label")}>
              <option value="">{t("es_any_year")}</option>
              {years.map((y) => <option key={y} value={y}>{y}</option>)}
            </select>
          </div>
        )}
      </div>

      {loading ? <SkeletonCards count={3} height={100} />
        : page.err ? <div className="card card-pad"><ErrorState message={page.err.trim() || t("es_load_fail")} onRetry={() => setReload((n) => n + 1)} /></div>
        : page.items.length === 0 ? (
          <div className="card card-pad">
            {needle || year
              ? <EmptyState compact icon={<Search size={24} />} title={fill(t("es_no_match"), { q: needle || year })} />
              : <EmptyState icon={<BookOpen size={26} />} title={t("es_copies_empty_title")} text={t("es_copies_empty_text")} />}
          </div>
        ) : (
          <>
            <section className="card es-group">
              {page.items.map((e) => (
                <EntryRow key={e.answerId} e={e} headline access={access} onOpen={open} onText={openText} t={t}
                          readers={page.readers?.get(e.answerId) || 0}
                          starred={!!marks.answer.get(e.answerId)?.starred} onStar={() => toggleMark("answer", e.answerId, "starred")} />
              ))}
            </section>
            <p className="es-foot">{t("es_marks_note")}</p>
            {page.items.length < page.total && (
              <div className="es-more">
                <button className="btn btn-ghost" onClick={more} disabled={busy}>
                  {fill(t("es_show_more"), { n: page.items.length, t: page.total })}
                </button>
              </div>
            )}
          </>
        )}
    </div>
  );
}

/* ------------------------------------------------------------ one essay -- */

function EntryRow({ e, headline = false, access, onOpen, onText, t, readers = 0, starred = false, onStar = null }) {
  const locked = !e.isFree && !access;
  const tp = e.topper;
  const rank = tp.rank != null ? (tp.cseYear ? fill(t("es_rank_year"), { n: tp.rank, y: tp.cseYear }) : fill(t("es_rank_only"), { n: tp.rank })) : null;
  const label = e.startPage ? fill(t("es_open_at"), { p: e.startPage }) : t("es_open");

  let action;
  if (locked) {
    action = <button className="btn btn-sm btn-locked" onClick={() => onOpen(e)}><Lock size={14} />{t("es_locked_badge")}</button>;
  } else if (e.hosted) {
    action = <button className="btn btn-sm btn-primary" onClick={() => onOpen(e)}><BookOpen size={14} />{label}</button>;
  } else if (e.sourceUrl) {
    // A real anchor, not window.open: phones hand it to their own PDF viewer,
    // which is what honours #page.
    action = (
      <a className="btn btn-sm btn-ghost" href={DB.copyLinkAt(e.sourceUrl, e.startPage)} target="_blank" rel="noopener noreferrer" title={t("es_ext_hint")}>
        <ExternalLink size={14} />{label}
      </a>
    );
  } else {
    action = null;
  }
  // Locked, the one lock button explains both the copy and its text.
  const textBtn = !locked && e.words > 0 && onText
    ? <button className="btn btn-sm btn-ghost" onClick={() => onText(e)}><FileText size={14} />{t("es_read_text")}</button>
    : null;

  return (
    <div className="es-entry">
      <div className="es-entry-main">
        {headline && <div className="es-entry-q">{e.question}</div>}
        <div className="es-entry-name">{tp.name}</div>
        <div className="es-entry-meta">
          {rank && <span>{rank}</span>}
          {tp.essayMarks != null && <span className="marks">{fill(t("es_marks"), { m: tp.essayMarks })}</span>}
          {e.writtenYear && <span>{fill(t("es_written"), { y: e.writtenYear })}</span>}
          {e.source && <span>{e.source}</span>}
          {e.words > 0 && <span>{fill(t("es_words"), { n: e.words.toLocaleString("en-IN") })}</span>}
          {readers > 0 && <span>{readers === 1 ? t("st_read_one") : fill(t("st_read_n"), { n: readers })}</span>}
          {e.isFree && <span className="es-free">{t("sd_free")}</span>}
        </div>
      </div>
      {(textBtn || action || onStar) && (
        <div className="es-entry-acts">
          {onStar && <StarButton on={starred} onClick={onStar} t={t} />}
          {textBtn}{action}
        </div>
      )}
    </div>
  );
}

/* An essay as text: the typed transcript, behind the copy's own lock. */
/* Reading for this long counts the essay as read today (streak, reader count). */
const READ_AFTER_MS = 40000;

function TextReader({ entry, onClose, onOpenCopy, t, starred = false, onStar, noteCount = 0, onNote, onRead }) {
  // Keyed by answer and attempt, like the library: while the result belongs to
  // another request, this one shows as loading. Nothing is reset in the effect.
  const [tries, setTries] = useState(0);
  const key = `${entry.answerId}|${tries}`;
  const [res, setRes] = useState({ key: null, text: null, err: "" });
  const loading = res.key !== key;

  useEffect(() => {
    let alive = true;
    DB.essayText(entry.answerId).then(
      (text) => { if (alive) setRes({ key, text, err: "" }); },
      (e) => { if (alive) setRes({ key, text: null, err: e?.message || " " }); },
    );
    return () => { alive = false; };
  }, [key, entry.answerId]);

  useEffect(() => {
    const onKey = (ev) => { if (ev.key === "Escape") onClose(); };
    window.addEventListener("keydown", onKey);
    const prev = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => { window.removeEventListener("keydown", onKey); document.body.style.overflow = prev; };
  }, [onClose]);

  // Only a text that actually loaded, kept open for a while, counts as read.
  const hasText = !loading && !!res.text?.body;
  useEffect(() => {
    if (!hasText) return undefined;
    const id = setTimeout(() => { DB.logEssayRead(entry.answerId).then(() => onRead?.()); }, READ_AFTER_MS);
    return () => clearTimeout(id);
  }, [hasText, entry.answerId, onRead]);

  const paras = res.text?.body ? res.text.body.split(/\n{2,}/) : [];
  const by = [entry.topper.name, entry.source, entry.words > 0 ? fill(t("es_words"), { n: entry.words.toLocaleString("en-IN") }) : null]
    .filter(Boolean).join(" · ");
  let copyBtn = null;
  if (entry.hosted) {
    copyBtn = <button className="btn btn-sm btn-ghost" onClick={() => onOpenCopy(entry)}><BookOpen size={14} />{t("es_open_copy")}</button>;
  } else if (entry.sourceUrl) {
    copyBtn = (
      <a className="btn btn-sm btn-ghost" href={DB.copyLinkAt(entry.sourceUrl, entry.startPage)} target="_blank" rel="noopener noreferrer">
        <ExternalLink size={14} />{t("es_open_copy")}
      </a>
    );
  }

  return (
    <div className="overlay" onClick={onClose}>
      <div className="modal es-text-modal" onClick={(ev) => ev.stopPropagation()} role="dialog" aria-modal="true" aria-labelledby="es-text-title">
        <div className="modal-head">
          <div style={{ minWidth: 0 }}>
            <h3 id="es-text-title">{entry.question}</h3>
            {by && <div className="es-text-by">{by}</div>}
          </div>
          <button className="x" onClick={onClose} aria-label={t("es_v_close")}><X size={19} /></button>
        </div>
        <div className="modal-body es-text-body">
          <p className="es-text-note">{t("es_text_note")}</p>
          {loading ? <SkeletonCards count={3} height={70} />
            : res.err ? <ErrorState message={res.err.trim() || t("es_load_fail")} onRetry={() => setTries((n) => n + 1)} />
            : !paras.length ? <p className="es-text-none">{t("es_text_none")}</p>
            : <article className="es-text">{paras.map((p, i) => <p key={i}>{p}</p>)}</article>}
        </div>
        <div className="modal-foot">
          {onStar && <StarButton on={starred} onClick={onStar} t={t} />}
          {onNote && <NoteButton count={noteCount} onClick={onNote} t={t} />}
          <span style={{ flex: 1 }} />
          {copyBtn}
          <button className="btn btn-primary btn-sm" onClick={onClose}>{t("es_v_close")}</button>
        </div>
      </div>
    </div>
  );
}

function LockedModal({ entry, onClose, onBrowse, t }) {
  useEffect(() => {
    const onKey = (ev) => { if (ev.key === "Escape") onClose(); };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onClose]);
  return (
    <div className="overlay" onClick={onClose}>
      <div className="modal" style={{ maxWidth: 440 }} onClick={(ev) => ev.stopPropagation()} role="dialog" aria-modal="true" aria-labelledby="es-locked-title">
        <div className="modal-head">
          <h3 id="es-locked-title">{t("es_locked_title")}</h3>
          <button className="x" onClick={onClose} aria-label={t("es_v_close")}><X size={19} /></button>
        </div>
        <div className="modal-body">
          <div style={{ fontSize: 14, fontWeight: 700, marginBottom: 6 }}>{entry.question}</div>
          <div style={{ fontSize: 13.5, color: "var(--muted)", lineHeight: 1.6 }}>{t("es_locked_text")}</div>
        </div>
        <div className="modal-foot">
          <button className="btn btn-ghost btn-sm" onClick={onClose}>{t("es_v_close")}</button>
          {onBrowse && <button className="btn btn-primary btn-sm" onClick={onBrowse}>{t("es_see_bundles")}</button>}
        </div>
      </div>
    </div>
  );
}
