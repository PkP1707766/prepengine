import { useState, useEffect, useMemo, useCallback } from "react";
import { ChevronLeft, ChevronRight, Lock, ExternalLink, BookOpen, Search, X, PenLine } from "lucide-react";
import { useLang } from "../lib/contexts.js";
import { EmptyState, ErrorState, SkeletonCards } from "../ui/Feedback.jsx";
import CopyViewer from "../ui/CopyViewer.jsx";
import * as DB from "../lib/db.js";
import { loadKey, saveKey } from "../lib/storage.js";

/* ============================================================
   VIEW: ESSAY  (Mains, slice 1)

   The Essay paper has no syllabus, so the themes are the syllabus:
   pick one, see every UPSC topic in it, and read how toppers wrote
   on that topic or a close cousin of it. Each essay opens at the
   page where it starts -- in the in-app reader when we host the
   copy, or in the publisher's own PDF at #page=N when we only
   link to it.

   Two tabs: Essay PYQs (theme or year rail + cards → one PYQ's
   topper essays) and Topper essays (the whole library, by marks or
   year). Everything a student reads here is either UPSC's own text
   or the topper's own copy; nothing is generated yet.
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
.es-rail-item .n{font-size:11.5px;font-weight:700;opacity:.7;font-variant-numeric:tabular-nums}
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
@media(max-width:860px){
  .es-grid{grid-template-columns:minmax(0,1fr)}
  .es-rail{display:none}
  .es-pick{display:block}
}
@media(max-width:560px){
  .es-entry{flex-direction:column;align-items:stretch;gap:10px}
  .es-entry .btn{width:100%}
}
`;

const fill = (s, vars) => Object.entries(vars).reduce((out, [k, v]) => out.split(`{${k}}`).join(String(v)), s);

export default function EssayView({ onBrowse }) {
  const { t, lang } = useLang();
  const [tab, setTab] = useState(() => (loadKey("essay:tab", "pyqs") === "copies" ? "copies" : "pyqs"));
  const [data, setData] = useState(null);
  const [err, setErr] = useState("");
  const [reload, setReload] = useState(0);
  const [openPyq, setOpenPyq] = useState(null);
  const [reader, setReader] = useState(null);
  const [locked, setLocked] = useState(null);

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const [themes, pyqs, access] = await Promise.all([DB.essayThemes(), DB.essayPyqs(), DB.mainsAccess()]);
        if (alive) { setData({ themes, pyqs, access }); setErr(""); }
      } catch (e) {
        console.error("essay load failed", e);
        if (alive) setErr(e?.message || t("es_load_fail"));
      }
    })();
    return () => { alive = false; };
    // t is left out on purpose: a language toggle must not refetch.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [reload]);

  const switchTab = (k) => { setTab(k); saveKey("essay:tab", k); setOpenPyq(null); };

  const themeName = useCallback((th) => (lang === "hi" && th?.nameHi ? th.nameHi : th?.name || ""), [lang]);
  const topicOf = useCallback((p) => (lang === "hi" && p.topicHi ? p.topicHi : p.topic), [lang]);

  const open = useCallback((entry) => {
    if (!entry.isFree && !data?.access) { setLocked(entry); return; }
    if (entry.hosted) setReader(entry);
  }, [data]);

  if (err) return <div className="card card-pad"><ErrorState message={err} onRetry={() => { setErr(""); setData(null); setReload((n) => n + 1); }} /></div>;
  if (!data) return <SkeletonCards count={3} height={120} />;

  const ctx = { t, lang, themeName, topicOf, access: data.access, open };

  return (
    <div>
      <style>{ES_CSS}</style>
      <div className="es-head">
        <div className="tabs">
          {[["pyqs", "es_tab_pyqs"], ["copies", "es_tab_copies"]].map(([k, key]) => (
            <button key={k} className={"tab" + (tab === k ? " active" : "")} onClick={() => switchTab(k)}>{t(key)}</button>
          ))}
        </div>
      </div>
      {!data.access && (
        <div className="es-note">
          <Lock size={15} /><span style={{ flex: 1, minWidth: 200 }}>{t("es_access_note")}</span>
          {onBrowse && <button className="btn btn-sm btn-ghost" onClick={onBrowse}>{t("es_see_bundles")}</button>}
        </div>
      )}

      {tab === "pyqs" && (openPyq
        ? <PyqDetail pyq={openPyq} themes={data.themes} onBack={() => setOpenPyq(null)} {...ctx} />
        : <PyqList themes={data.themes} pyqs={data.pyqs} onOpen={setOpenPyq} {...ctx} />)}
      {tab === "copies" && <CopiesTab {...ctx} />}

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
    </div>
  );
}

/* ---------------------------------------------------------------- PYQs -- */

function PyqList({ themes, pyqs, onOpen, t, themeName, topicOf, lang }) {
  const [mode, setMode] = useState(() => (loadKey("essay:mode", "theme") === "year" ? "year" : "theme"));
  const [pick, setPick] = useState(() => loadKey("essay:pick", "all"));
  const byId = useMemo(() => new Map(themes.map((th) => [th.id, th])), [themes]);

  const themeCounts = useMemo(() => {
    const m = new Map();
    pyqs.forEach((p) => p.themes.forEach((x) => m.set(x.id, (m.get(x.id) || 0) + 1)));
    return m;
  }, [pyqs]);
  const railThemes = useMemo(() => themes
    .filter((th) => themeCounts.get(th.id))
    .sort((a, b) => (themeCounts.get(b.id) - themeCounts.get(a.id)) || themeName(a).localeCompare(themeName(b))),
  [themes, themeCounts, themeName]);
  const years = useMemo(() => {
    const m = new Map();
    pyqs.forEach((p) => m.set(p.year, (m.get(p.year) || 0) + 1));
    return [...m].sort((a, b) => b[0] - a[0]);
  }, [pyqs]);

  const setModeKeep = (m) => { setMode(m); setPick("all"); saveKey("essay:mode", m); saveKey("essay:pick", "all"); };
  const choose = (v) => { setPick(v); saveKey("essay:pick", v); };
  // A remembered pick that no longer exists (a theme renamed away) falls back to all.
  const valid = pick === "all"
    || (mode === "theme" ? themeCounts.has(pick) : years.some(([y]) => String(y) === String(pick)));
  const active = valid ? pick : "all";

  const shown = pyqs.filter((p) => active === "all"
    || (mode === "theme" ? p.themes.some((x) => x.id === active) : String(p.year) === String(active)));
  const groups = [];
  shown.forEach((p) => {
    const last = groups[groups.length - 1];
    if (last && last.year === p.year) last.items.push(p);
    else groups.push({ year: p.year, items: [p] });
  });

  if (pyqs.length === 0) {
    return <div className="card card-pad"><EmptyState icon={<PenLine size={26} />} title={t("es_empty_title")} text={t("es_empty_text")} /></div>;
  }

  const railItems = mode === "theme"
    ? [["all", t("es_all_themes"), pyqs.length], ...railThemes.map((th) => [th.id, themeName(th), themeCounts.get(th.id)])]
    : [["all", t("es_all_years"), pyqs.length], ...years.map(([y, n]) => [String(y), String(y), n])];

  return (
    <div className="es-grid">
      <aside className="card es-rail">
        <div className="es-seg" role="tablist">
          <button className={mode === "theme" ? "on" : ""} onClick={() => setModeKeep("theme")}>{t("es_by_theme")}</button>
          <button className={mode === "year" ? "on" : ""} onClick={() => setModeKeep("year")}>{t("es_by_year")}</button>
        </div>
        {railItems.map(([id, label, n]) => (
          <button key={id} className={"es-rail-item" + (active === id ? " on" : "")} onClick={() => choose(id)}
                  aria-current={active === id ? "true" : undefined}>
            <span>{label}</span><span className="n">{n}</span>
          </button>
        ))}
      </aside>

      <div style={{ minWidth: 0 }}>
        <div className="es-pick">
          <div className="es-seg">
            <button className={mode === "theme" ? "on" : ""} onClick={() => setModeKeep("theme")}>{t("es_by_theme")}</button>
            <button className={mode === "year" ? "on" : ""} onClick={() => setModeKeep("year")}>{t("es_by_year")}</button>
          </div>
          <select value={active} onChange={(e) => choose(e.target.value)} aria-label={mode === "theme" ? t("es_theme_label") : t("es_year_label")}>
            {railItems.map(([id, label, n]) => <option key={id} value={id}>{label} ({n})</option>)}
          </select>
        </div>

        {shown.length === 0 ? (
          <div className="card card-pad"><EmptyState compact title={t("es_theme_empty")} /></div>
        ) : groups.map((g) => (
          <div key={g.year}>
            <div className="es-year">{g.year}</div>
            <div className="es-cards">
              {g.items.map((p) => {
                const [main, ...rest] = p.themes.map((x) => byId.get(x.id)).filter(Boolean);
                const n = p.essayCount;
                return (
                  <article className="card es-card" key={p.id}>
                    <div className="es-card-top">
                      {/* Not "main": StudentApp's layout column is .main, and the two collided. */}
                      {main ? <span className="es-chip es-lead">{themeName(main)}</span> : <span />}
                      <span className="es-yr">{p.section ? `${p.year} · ${p.section}` : p.year}</span>
                    </div>
                    <div className={"es-topic" + (lang === "hi" && p.topicHi ? " hi" : "")}>{topicOf(p)}</div>
                    {rest.length > 0 && (
                      <div className="es-also">{t("es_also_under")}{rest.map((th) => <span key={th.id} className="es-chip">{themeName(th)}</span>)}</div>
                    )}
                    <div className="es-actions">
                      <button className={"btn btn-sm " + (n ? "btn-primary" : "btn-ghost")} disabled={!n} onClick={() => onOpen(p)}
                              style={n ? undefined : { opacity: 0.7, cursor: "default" }}>
                        <BookOpen size={15} />
                        {n === 0 ? t("es_no_essays") : n === 1 ? t("es_read_one") : fill(t("es_read_n"), { n })}
                        {n > 0 && <ChevronRight size={15} />}
                      </button>
                    </div>
                  </article>
                );
              })}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function PyqDetail({ pyq, themes, onBack, t, lang, themeName, topicOf, access, open }) {
  const [groups, setGroups] = useState(null);
  const [err, setErr] = useState("");
  const [reload, setReload] = useState(0);
  const byId = useMemo(() => new Map(themes.map((th) => [th.id, th])), [themes]);

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const g = await DB.essaysForPyq(pyq.id);
        if (alive) { setGroups(g); setErr(""); }
      } catch (e) {
        console.error("essays for pyq failed", e);
        if (alive) setErr(e?.message || "");
      }
    })();
    return () => { alive = false; };
  }, [pyq.id, reload]);

  useEffect(() => { window.scrollTo({ top: 0 }); }, [pyq.id]);

  const total = (groups || []).reduce((n, g) => n + g.entries.length, 0);
  return (
    <div>
      <button className="es-back" onClick={onBack}><ChevronLeft size={16} />{t("es_back")}</button>
      <div className="card es-detail-head">
        <div className="es-card-top">
          <span style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
            {pyq.themes.map((x) => byId.get(x.id)).filter(Boolean).map((th, i) =>
              <span key={th.id} className={"es-chip" + (i === 0 ? " es-lead" : "")}>{themeName(th)}</span>)}
          </span>
          <span className="es-yr">{pyq.year}</span>
        </div>
        <div className={"es-topic" + (lang === "hi" && pyq.topicHi ? " hi" : "")}>{topicOf(pyq)}</div>
      </div>

      {err ? <div className="card card-pad"><ErrorState message={err} onRetry={() => { setErr(""); setGroups(null); setReload((n) => n + 1); }} /></div>
        : groups === null ? <SkeletonCards count={2} height={140} />
        : total === 0 ? <div className="card card-pad"><EmptyState compact icon={<BookOpen size={24} />} title={t("es_pyq_no_essays")} /></div>
        : (
          <>
            {groups.map((g) => (
              <section className="card es-group" key={g.key}>
                <div className="es-group-head">
                  <div>
                    <div className="k">{g.kind === "exact" ? t("es_same_q") : t("es_related_q")}</div>
                    <div className="q">{g.question}</div>
                  </div>
                  <span className="c">{g.entries.length === 1 ? t("es_one_essay") : fill(t("es_n_essays"), { n: g.entries.length })}</span>
                </div>
                {g.entries.map((e) => <EntryRow key={e.answerId} e={e} access={access} onOpen={open} t={t} />)}
              </section>
            ))}
            <p className="es-foot">{t("es_marks_note")}</p>
          </>
        )}
    </div>
  );
}

/* --------------------------------------------------------- the library -- */

function CopiesTab({ t, access, open }) {
  const [sort, setSort] = useState(() => {
    const s = loadKey("essay:sort", "marks");
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
  const queryKey = `${sort}|${year}|${needle}|${reload}`;
  const [page, setPage] = useState({ key: null, items: [], total: 0, err: "" });
  const loading = page.key !== queryKey;

  useEffect(() => { DB.topperLibraryYears("essay").then(setYears).catch(() => setYears([])); }, []);
  // Typing should not fire a query per keystroke.
  useEffect(() => { const id = setTimeout(() => setNeedle(q.trim()), 300); return () => clearTimeout(id); }, [q]);

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const r = await DB.topperLibrary({ paper: "essay", sort, year: year ? Number(year) : null, q: needle, offset: 0, limit: 24 });
        if (alive) setPage({ key: queryKey, items: r.items, total: r.total, err: "" });
      } catch (e) {
        console.error("topper library failed", e);
        if (alive) setPage({ key: queryKey, items: [], total: 0, err: e?.message || " " });
      }
    })();
    return () => { alive = false; };
  }, [sort, year, needle, queryKey]);

  const more = async () => {
    setBusy(true);
    try {
      const r = await DB.topperLibrary({ paper: "essay", sort, year: year ? Number(year) : null, q: needle, offset: page.items.length, limit: 24 });
      setPage((p) => ({ ...p, items: [...p.items, ...r.items], total: r.total }));
    } catch (e) { console.error(e); }
    setBusy(false);
  };

  const changeSort = (s) => { setSort(s); saveKey("essay:sort", s); };

  return (
    <div>
      <div className="es-tools">
        <label className="es-tool grow es-search">
          <Search size={15} />
          <input value={q} onChange={(e) => setQ(e.target.value)} placeholder={t("es_search_copies")} aria-label={t("es_search_copies")} />
          {q && <button onClick={() => setQ("")} aria-label={t("es_v_close")} style={{ color: "var(--muted)", display: "grid" }}><X size={15} /></button>}
        </label>
        <div className="es-tool">
          <select value={sort} onChange={(e) => changeSort(e.target.value)} aria-label={t("es_sort_label")}>
            <option value="marks">{t("es_sort_marks")}</option>
            <option value="newest">{t("es_sort_new")}</option>
            <option value="oldest">{t("es_sort_old")}</option>
          </select>
        </div>
        <div className="es-tool">
          <select value={year} onChange={(e) => setYear(e.target.value)} aria-label={t("es_year_label")}>
            <option value="">{t("es_any_year")}</option>
            {years.map((y) => <option key={y} value={y}>{y}</option>)}
          </select>
        </div>
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
              {page.items.map((e) => <EntryRow key={e.answerId} e={e} headline access={access} onOpen={open} t={t} />)}
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

function EntryRow({ e, headline = false, access, onOpen, t }) {
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
          {e.isFree && <span className="es-free">{t("sd_free")}</span>}
        </div>
      </div>
      {action}
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
