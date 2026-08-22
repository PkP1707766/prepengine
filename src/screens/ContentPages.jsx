import { useState, useEffect } from "react";
import {
  BookOpen, FileText, FolderOpen, Newspaper, HelpCircle, GraduationCap,
  ArrowRight, ChevronDown, Download, ExternalLink, Search, Calendar, Play, Eye,
} from "lucide-react";
import { ErrorState, Skeleton } from "../ui/Feedback.jsx";
import * as DB from "../lib/db.js";

/* ============================================================
   PUBLIC CONTENT HUB — Syllabus, PYQ, Free Materials, NCERT,
   Daily Current Affairs, FAQ.

   Every page reads from a real table with an admin screen behind
   it. None of this content is hardcoded here: a syllabus baked
   into a JSX file is the same "demo mode" problem this project
   spent weeks removing, wearing a different hat.
   ============================================================ */

/* Shared loading hook — every page here is "fetch once, render". */
function useContent(loader, deps = []) {
  const [data, setData] = useState(null);
  const [err, setErr] = useState("");
  const [key, setKey] = useState(0);

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const d = await loader();
        if (!alive) return;
        setErr("");
        setData(d);
      } catch (e) {
        console.error(e);
        if (alive) { setErr(e?.message || "Couldn't load this page."); setData([]); }
      }
    })();
    return () => { alive = false; };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [key, ...deps]);

  return { data, err, retry: () => setKey((k) => k + 1) };
}

function Loading({ rows = 5 }) {
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
      {Array.from({ length: rows }, (_, i) => <Skeleton key={i} h={58} />)}
    </div>
  );
}

function Empty({ icon, title, text }) {
  return (
    <div className="pb-panel" style={{ textAlign: "center", padding: "48px 24px" }}>
      <div style={{
        width: 54, height: 54, borderRadius: 16, margin: "0 auto 14px", display: "grid",
        placeItems: "center", background: "color-mix(in srgb, var(--gold) 18%, transparent)", color: "var(--gold-2)",
      }}>{icon}</div>
      <div style={{ fontFamily: "var(--font-display,serif)", fontSize: 19, color: "var(--ink)" }}>{title}</div>
      <p style={{ fontSize: 14, color: "var(--sub)", lineHeight: 1.7, maxWidth: "44ch", margin: "10px auto 0" }}>{text}</p>
    </div>
  );
}

/* ------------------------------------------------------------- syllabus -- */
function SyllabusPage() {
  const [exam, setExam] = useState("upsc");
  const { data: exams } = useContent(() => DB.syllabusExams());
  const { data, err, retry } = useContent(() => DB.syllabus(exam), [exam]);

  const available = exams && exams.length ? exams : ["upsc"];

  return (
    <>
      {available.length > 1 && (
        <div className="pb-tabs">
          {available.map((e) => (
            <button key={e} className={"pb-tab" + (exam === e ? " on" : "")} onClick={() => setExam(e)}>
              {e.toUpperCase()}
            </button>
          ))}
        </div>
      )}

      {/* A syllabus is not something to take on trust from any coaching site,
          including this one. */}
      <div className="pb-note">
        Always cross-check against the official notification before you plan your
        preparation around it — commissions revise the syllabus from time to time.
      </div>

      {err ? <div className="pb-panel"><ErrorState message={err} onRetry={retry} /></div>
        : data === null ? <Loading />
        : data.length === 0 ? (
          <Empty icon={<BookOpen size={25} />} title={`${exam.toUpperCase()} syllabus not published yet`}
                 text="This exam's syllabus hasn't been added yet. It'll appear here as soon as it's published." />
        ) : data.map((paper) => (
          <div className="pb-panel" key={paper.paper} style={{ marginBottom: 18 }}>
            <div className="pb-kicker">Paper</div>
            <h3 className="pb-h3">{paper.paper}</h3>
            <ol className="pb-syl">
              {paper.topics.map((t) => (
                <li key={t.id}>
                  {t.section && <span className="pb-syl-sec">{t.section}</span>}
                  <span className="pb-syl-topic">{t.topic}</span>
                  {t.detail && <span className="pb-syl-detail">{t.detail}</span>}
                </li>
              ))}
            </ol>
          </div>
        ))}
    </>
  );
}

/* ------------------------------------------------------------------ pyq -- */
function PyqPage() {
  const { data, err, retry } = useContent(() => DB.pyqPapers());
  const [exam, setExam] = useState("all");

  if (err) return <div className="pb-panel"><ErrorState message={err} onRetry={retry} /></div>;
  if (data === null) return <Loading />;
  if (data.length === 0) {
    return <Empty icon={<FileText size={25} />} title="No papers published yet"
      text="Previous-year question papers and their solutions will appear here as they're uploaded." />;
  }

  const exams = ["all", ...new Set(data.map((p) => p.exam))];
  const shown = data.filter((p) => exam === "all" || p.exam === exam);
  const byYear = {};
  shown.forEach((p) => { (byYear[p.year] ||= []).push(p); });

  return (
    <>
      {exams.length > 2 && (
        <div className="pb-tabs">
          {exams.map((e) => (
            <button key={e} className={"pb-tab" + (exam === e ? " on" : "")} onClick={() => setExam(e)}>
              {e === "all" ? "All exams" : e.toUpperCase()}
            </button>
          ))}
        </div>
      )}
      {Object.keys(byYear).sort((a, b) => b - a).map((year) => (
        <div className="pb-panel" key={year} style={{ marginBottom: 18 }}>
          <div className="pb-kicker">{year}</div>
          <h3 className="pb-h3">{byYear[year].length} paper{byYear[year].length === 1 ? "" : "s"}</h3>
          {byYear[year].map((p) => (
            <div className="pb-listrow" key={p.id}>
              <div style={{ flex: 1, minWidth: 0 }}>
                <div className="pb-listrow-t">{p.title}</div>
                <div className="pb-listrow-s">
                  {p.exam.toUpperCase()} · {p.paper}{p.questionCount ? ` · ${p.questionCount} questions` : ""}
                </div>
              </div>
              <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
                {p.paperUrl && (
                  <a className="pb-b-ghost pb-b-tight" href={p.paperUrl} target="_blank" rel="noreferrer">
                    <Download size={14} />Paper
                  </a>
                )}
                {p.solutionUrl && (
                  <a className="pb-b-primary pb-b-tight" href={p.solutionUrl} target="_blank" rel="noreferrer">
                    <Eye size={14} />Solutions
                  </a>
                )}
              </div>
            </div>
          ))}
        </div>
      ))}
    </>
  );
}

/* ------------------------------------------------------------ materials -- */
const MAT_ICON = { pdf: FileText, note: BookOpen, video: Play, link: ExternalLink };

function MaterialsPage() {
  const { data, err, retry } = useContent(() => DB.freeMaterials());
  const [q, setQ] = useState("");

  if (err) return <div className="pb-panel"><ErrorState message={err} onRetry={retry} /></div>;
  if (data === null) return <Loading />;
  if (data.length === 0) {
    return <Empty icon={<FolderOpen size={25} />} title="No free material published yet"
      text="Free notes, PDFs and videos will appear here. Paid material lives inside your dashboard once you enrol." />;
  }

  const needle = q.trim().toLowerCase();
  const shown = data.filter((m) => !needle || m.title.toLowerCase().includes(needle) || (m.subject || "").toLowerCase().includes(needle));

  return (
    <>
      <div className="pb-search-wrap">
        <div className="pb-search"><Search size={15} />
          <input placeholder="Search notes and subjects…" value={q} onChange={(e) => setQ(e.target.value)} />
        </div>
      </div>
      {shown.length === 0 ? (
        <div className="pb-panel" style={{ textAlign: "center", color: "var(--sub)" }}>Nothing matches "{q}".</div>
      ) : (
        <div className="pb-grid">
          {shown.map((m) => {
            const Icon = MAT_ICON[m.type] || BookOpen;
            return (
              <a className="pb-card pb-card-link" key={m.id} href={m.url} target="_blank" rel="noreferrer">
                <div className="pb-res-ic"><Icon size={22} /></div>
                <div className="pb-card-title" style={{ fontSize: 16 }}>{m.title}</div>
                {m.subject && <div className="pb-card-tag" style={{ minHeight: 0 }}>{m.subject}</div>}
                {m.description && <p className="pb-card-tag">{m.description}</p>}
                <span className="pb-openlink">Open <ArrowRight size={14} /></span>
              </a>
            );
          })}
        </div>
      )}
    </>
  );
}

/* ---------------------------------------------------------------- ncert -- */
function NcertPage() {
  const { data, err, retry } = useContent(() => DB.ncertBooks());
  const [cls, setCls] = useState("all");

  if (err) return <div className="pb-panel"><ErrorState message={err} onRetry={retry} /></div>;
  if (data === null) return <Loading />;
  if (data.length === 0) {
    return <Empty icon={<GraduationCap size={25} />} title="No books listed yet"
      text="NCERT titles will appear here organised by class and subject." />;
  }

  const classes = ["all", ...new Set(data.map((b) => b.classLevel))];
  const shown = data.filter((b) => cls === "all" || b.classLevel === cls);
  const byClass = {};
  shown.forEach((b) => { (byClass[b.classLevel] ||= []).push(b); });

  return (
    <>
      <div className="pb-tabs">
        {classes.map((c) => (
          <button key={c} className={"pb-tab" + (cls === c ? " on" : "")} onClick={() => setCls(c)}>
            {c === "all" ? "All classes" : "Class " + c}
          </button>
        ))}
      </div>
      {Object.keys(byClass).sort((a, b) => a - b).map((c) => (
        <div className="pb-panel" key={c} style={{ marginBottom: 18 }}>
          <div className="pb-kicker">Class {c}</div>
          <h3 className="pb-h3">{byClass[c].length} book{byClass[c].length === 1 ? "" : "s"}</h3>
          <div className="pb-chipwrap">
            {byClass[c].map((b) => (
              <a className="pb-chip-link" key={b.id} href={b.url} target="_blank" rel="noreferrer">
                <BookOpen size={14} />{b.subject}
                {b.language === "hi" && <span className="pb-lang">हिन्दी</span>}
              </a>
            ))}
          </div>
        </div>
      ))}
    </>
  );
}

/* ----------------------------------------------------------------- news -- */
function NewsPage() {
  const { data, err, retry } = useContent(() => DB.currentAffairs());
  const [open, setOpen] = useState(null);

  if (err) return <div className="pb-panel"><ErrorState message={err} onRetry={retry} /></div>;
  if (data === null) return <Loading />;
  if (data.length === 0) {
    return <Empty icon={<Newspaper size={25} />} title="No current affairs posted yet"
      text="A daily feed of exam-relevant news will appear here once it starts publishing." />;
  }

  const byDate = {};
  data.forEach((n) => { (byDate[n.date] ||= []).push(n); });

  return (
    <>
      {Object.keys(byDate).sort().reverse().map((d) => (
        <div className="pb-panel" key={d} style={{ marginBottom: 18 }}>
          <div className="pb-kicker" style={{ display: "flex", alignItems: "center", gap: 7 }}>
            <Calendar size={13} />{new Date(d).toLocaleDateString("en-IN", { day: "numeric", month: "long", year: "numeric" })}
          </div>
          {byDate[d].map((n) => {
            const isOpen = open === n.id;
            return (
              <div className="pb-news" key={n.id}>
                <button className="pb-news-head" onClick={() => setOpen(isOpen ? null : n.id)} aria-expanded={isOpen}>
                  <span style={{ flex: 1, minWidth: 0 }}>
                    <span className="pb-listrow-t">{n.title}</span>
                    {n.summary && <span className="pb-listrow-s">{n.summary}</span>}
                  </span>
                  <ChevronDown size={17} style={{ flex: "0 0 auto", transform: isOpen ? "rotate(180deg)" : "none", transition: "transform .18s" }} />
                </button>
                {isOpen && (
                  <div className="pb-news-body">
                    {n.body && <p>{n.body}</p>}
                    <div className="pb-tagrow">
                      {n.examTags.map((t) => <span className="pb-tag" key={t}>{t.toUpperCase()}</span>)}
                      {n.tags.map((t) => <span className="pb-tag pb-tag-soft" key={t}>{t}</span>)}
                    </div>
                    {n.sourceUrl && (
                      <a className="pb-openlink" href={n.sourceUrl} target="_blank" rel="noreferrer">
                        {n.sourceName || "Source"} <ExternalLink size={13} />
                      </a>
                    )}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      ))}
    </>
  );
}

/* ------------------------------------------------------------------ faq -- */
function FaqPage() {
  const { data, err, retry } = useContent(() => DB.faqs());
  const [open, setOpen] = useState(null);

  if (err) return <div className="pb-panel"><ErrorState message={err} onRetry={retry} /></div>;
  if (data === null) return <Loading />;
  if (data.length === 0) {
    return <Empty icon={<HelpCircle size={25} />} title="No questions published yet" text="Answers to common questions will appear here." />;
  }

  const CAT = { tests: "Tests & attempts", payments: "Payments & pricing", access: "Access & account", general: "General" };
  const byCat = {};
  data.forEach((f) => { (byCat[f.category] ||= []).push(f); });

  return (
    <>
      {Object.keys(byCat).map((cat) => (
        <div className="pb-panel" key={cat} style={{ marginBottom: 18 }}>
          <div className="pb-kicker">{CAT[cat] || cat}</div>
          {byCat[cat].map((f) => {
            const isOpen = open === f.id;
            return (
              <div className="pb-news" key={f.id}>
                <button className="pb-news-head" onClick={() => setOpen(isOpen ? null : f.id)} aria-expanded={isOpen}>
                  <span className="pb-listrow-t" style={{ flex: 1, minWidth: 0 }}>{f.question}</span>
                  <ChevronDown size={17} style={{ flex: "0 0 auto", transform: isOpen ? "rotate(180deg)" : "none", transition: "transform .18s" }} />
                </button>
                {isOpen && <div className="pb-news-body"><p>{f.answer}</p></div>}
              </div>
            );
          })}
        </div>
      ))}
      <div className="pb-note" style={{ textAlign: "center" }}>
        Didn't find your answer? Email <a href="mailto:junoonias123@gmail.com">junoonias123@gmail.com</a> — we usually reply within a few hours.
      </div>
    </>
  );
}

/* ---------------------------------------------------------------- router -- */
export default function ContentPage({ page }) {
  switch (page) {
    case "syllabus": return <SyllabusPage />;
    case "pyq": return <PyqPage />;
    case "materials": return <MaterialsPage />;
    case "ncert": return <NcertPage />;
    case "news": return <NewsPage />;
    case "faq": return <FaqPage />;
    default: return null;
  }
}
