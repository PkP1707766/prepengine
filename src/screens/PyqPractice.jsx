import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import {
  ArrowLeft, ArrowRight, BookmarkCheck, Bookmark, Check, ChevronLeft, ChevronRight, Clock, Flag,
  Flame, Lock, Play, RotateCcw, Shuffle, Sparkles, Target, Timer, Trophy, Unlock, X, Keyboard, ListChecks,
  CalendarRange, Layers, SlidersHorizontal, CheckCircle2, XCircle, MinusCircle, AlertTriangle,
} from "lucide-react";
import { useLang } from "../lib/contexts.js";
import * as DB from "../lib/db.js";
import { loadKey, saveKey } from "../lib/storage.js";
import { COMPANY } from "../lib/legal.js";
import { openPyqSubject, takePyqSubject } from "../lib/pyqNav.js";

/* ============================================================
   PRELIMS PYQ PRACTICE  (#/pyq)

   One page, four states: the hub (subjects, your progress, the unlock), the
   set builder for one subject (by topic, by paper, by exam, refined by year,
   question style and your own history), the player (practice with instant
   checking, or a timed test with UPSC marking), and the result.

   The browser picks the set from pyq_meta(), which carries no text or
   answers, then asks pyq_fetch() for exactly those questions. A visitor
   without the plan only ever draws from the free ones, so a locked question
   is never requested. Answers are recorded on the server when signed in and
   kept on this device otherwise.
   ============================================================ */

export const PYQ_PLAN = "pyq-practice";
const SEC_PER_Q = 72; // UPSC GS I: 120 minutes for 100 questions

/* ---------------------------------------------------------------- copy -- */
const S = {
  eyebrow:      { en: "Prelims · Previous Year Questions", hi: "प्रीलिम्स · पिछले वर्षों के प्रश्न" },
  h1a:          { en: "Practise what they have", hi: "वही अभ्यास करें जो" },
  h1em:         { en: "already asked.", hi: "पहले पूछा जा चुका है।" },
  lede:         { en: "{n} questions from {p} papers, {y0} to {y1}: UPSC CSE, CDS, CAPF and the state commissions. By topic, by year, or as a timed test.",
                  hi: "{p} पेपरों से {n} प्रश्न, {y0} से {y1} तक: UPSC CSE, CDS, CAPF और राज्य आयोग। टॉपिक के अनुसार, वर्ष के अनुसार, या टाइम्ड टेस्ट के रूप में।" },
  st_q:         { en: "questions", hi: "प्रश्न" },
  st_p:         { en: "papers", hi: "पेपर" },
  st_y:         { en: "years", hi: "वर्ष" },
  st_e:         { en: "exams", hi: "परीक्षाएँ" },
  unlocked:     { en: "Everything unlocked", hi: "सब कुछ खुला है" },
  unlocked_s:   { en: "Every question in every subject, as each is added.", hi: "हर विषय का हर प्रश्न, जैसे-जैसे जुड़ते जाएँ।" },
  unlock_t:     { en: "Unlock every question", hi: "हर प्रश्न खोलें" },
  unlock_s:     { en: "All subjects, every exam and year, timed tests and your accuracy by topic. {d} days.",
                  hi: "सभी विषय, हर परीक्षा और वर्ष, टाइम्ड टेस्ट और टॉपिक के अनुसार आपकी सटीकता। {d} दिन।" },
  unlock_free:  { en: "{n} questions are free to try first, no card needed.", hi: "पहले {n} प्रश्न मुफ़्त आज़माएँ, कार्ड की ज़रूरत नहीं।" },
  unlock_btn:   { en: "Unlock for ₹{p}", hi: "₹{p} में खोलें" },
  try_free:     { en: "Try the free questions", hi: "मुफ़्त प्रश्न आज़माएँ" },
  subjects:     { en: "Choose a subject", hi: "विषय चुनें" },
  subjects_s:   { en: "Each one by topic, by paper and by exam. More subjects are on the way.", hi: "हर विषय टॉपिक, पेपर और परीक्षा के अनुसार। और विषय जल्द आ रहे हैं।" },
  free_n:       { en: "{n} free", hi: "{n} मुफ़्त" },
  upsc_n:       { en: "{n} from UPSC CSE", hi: "{n} UPSC CSE से" },
  practise:     { en: "Practise", hi: "अभ्यास करें" },
  soon:         { en: "Coming next", hi: "जल्द आ रहे हैं" },
  soon_list:    { en: ["Polity", "Modern History", "Geography", "Economy", "Environment", "Science & Tech"],
                  hi: ["राजव्यवस्था", "आधुनिक इतिहास", "भूगोल", "अर्थव्यवस्था", "पर्यावरण", "विज्ञान एवं तकनीक"] },
  your:         { en: "Your practice", hi: "आपका अभ्यास" },
  solved:       { en: "solved", hi: "हल किए" },
  accuracy:     { en: "accuracy", hi: "सटीकता" },
  marked:       { en: "bookmarked", hi: "बुकमार्क" },
  days28:       { en: "Last 4 weeks", hi: "पिछले 4 सप्ताह" },
  recent:       { en: "Recent sets", hi: "हाल के सेट" },
  guest_note:   { en: "You're practising as a guest. Answers stay on this device; sign in to keep them everywhere.",
                  hi: "आप अतिथि के रूप में अभ्यास कर रहे हैं। उत्तर इसी डिवाइस पर रहेंगे; हर जगह रखने के लिए लॉग इन करें।" },
  signin:       { en: "Sign in", hi: "लॉग इन करें" },
  back:         { en: "Back", hi: "वापस" },
  all_subjects: { en: "All subjects", hi: "सभी विषय" },
  tab_topic:    { en: "By topic", hi: "टॉपिक से" },
  tab_paper:    { en: "By paper", hi: "पेपर से" },
  tab_exam:     { en: "By exam", hi: "परीक्षा से" },
  all_topics:   { en: "All topics", hi: "सभी टॉपिक" },
  pick_topics:  { en: "Pick one topic or several. None picked means all.", hi: "एक या कई टॉपिक चुनें। कोई न चुनें तो सभी।" },
  pick_paper:   { en: "Tap a paper to practise exactly what it asked in this subject.", hi: "किसी पेपर पर टैप करें और इस विषय में उसके प्रश्नों का अभ्यास करें।" },
  pick_exam:    { en: "Pick the exams to draw from. None picked means all.", hi: "किन परीक्षाओं से प्रश्न लें, चुनें। कोई न चुनें तो सभी।" },
  state_pcs:    { en: "All state PCS", hi: "सभी राज्य PCS" },
  refine:       { en: "Refine", hi: "छाँटें" },
  years:        { en: "Years", hi: "वर्ष" },
  from:         { en: "From", hi: "से" },
  to:           { en: "To", hi: "तक" },
  style:        { en: "Question style", hi: "प्रश्न का प्रकार" },
  status:       { en: "Your history", hi: "आपका इतिहास" },
  st_all:       { en: "All", hi: "सभी" },
  st_new:       { en: "Not attempted", hi: "जो नहीं किए" },
  st_wrong:     { en: "Got wrong", hi: "जो गलत हुए" },
  st_marked:    { en: "Bookmarked", hi: "बुकमार्क" },
  size:         { en: "How many", hi: "कितने" },
  all:          { en: "All", hi: "सभी" },
  order:        { en: "Order", hi: "क्रम" },
  o_shuffle:    { en: "Shuffled", hi: "मिश्रित" },
  o_new:        { en: "Newest first", hi: "नए पहले" },
  o_old:        { en: "Oldest first", hi: "पुराने पहले" },
  mode:         { en: "Mode", hi: "मोड" },
  m_practice:   { en: "Practice", hi: "अभ्यास" },
  m_practice_s: { en: "Check each answer as you go.", hi: "हर उत्तर तुरंत जाँचें।" },
  m_test:       { en: "Timed test", hi: "टाइम्ड टेस्ट" },
  m_test_s:     { en: "72 s a question, +2 / −⅔, answers at the end.", hi: "प्रति प्रश्न 72 सेकंड, +2 / −⅔, उत्तर अंत में।" },
  match_n:      { en: "{n} questions match", hi: "{n} प्रश्न मेल खाते हैं" },
  match_free:   { en: "{f} of them are free. Unlock the other {l} for ₹{p}.", hi: "इनमें {f} मुफ़्त हैं। बाकी {l} ₹{p} में खोलें।" },
  match_none:   { en: "Nothing matches. Loosen a filter.", hi: "कुछ मेल नहीं खाता। कोई फ़िल्टर ढीला करें।" },
  start:        { en: "Start {n} questions", hi: "{n} प्रश्न शुरू करें" },
  ty_mcq:       { en: "Direct", hi: "सीधे" },
  ty_statement_based: { en: "Statements", hi: "कथन" },
  ty_pairs:     { en: "Pairs", hi: "युग्म" },
  ty_match_the_following: { en: "Match the lists", hi: "सूची मिलान" },
  ty_assertion_reason: { en: "Assertion–Reason", hi: "अभिकथन–कारण" },
  q_of:         { en: "Question {i} of {n}", hi: "प्रश्न {i} / {n}" },
  exit:         { en: "Exit", hi: "बाहर" },
  exit_q:       { en: "Leave this set? Answers so far are kept.", hi: "यह सेट छोड़ें? अब तक के उत्तर रखे रहेंगे।" },
  prev:         { en: "Previous", hi: "पिछला" },
  next:         { en: "Next", hi: "अगला" },
  finish:       { en: "Finish", hi: "समाप्त" },
  submit:       { en: "Submit test", hi: "टेस्ट जमा करें" },
  submit_q:     { en: "Submit with {n} unanswered?", hi: "{n} प्रश्न बिना उत्तर के जमा करें?" },
  review_later: { en: "Mark for review", hi: "समीक्षा के लिए चिह्नित" },
  clear:        { en: "Clear", hi: "हटाएँ" },
  correct:      { en: "Correct", hi: "सही" },
  wrong_ans:    { en: "Not quite. The answer is ({a}).", hi: "सही नहीं। उत्तर ({a}) है।" },
  streak:       { en: "{n} in a row", hi: "लगातार {n}" },
  bookmark:     { en: "Bookmark", hi: "बुकमार्क" },
  report:       { en: "Report a problem", hi: "समस्या बताएँ" },
  keys:         { en: "Keys: A–E or 1–5 to answer · ← → to move", hi: "कुंजियाँ: उत्तर के लिए A–E या 1–5 · आगे-पीछे ← →" },
  palette:      { en: "Questions", hi: "प्रश्न" },
  lg_ans:       { en: "Answered", hi: "उत्तर दिए" },
  lg_mark:      { en: "Marked", hi: "चिह्नित" },
  lg_none:      { en: "Not answered", hi: "उत्तर नहीं" },
  time_up:      { en: "Time is up. Your test has been submitted.", hi: "समय समाप्त। आपका टेस्ट जमा हो गया।" },
  res_title:    { en: "Your result", hi: "आपका परिणाम" },
  res_score:    { en: "UPSC-style score", hi: "UPSC जैसा स्कोर" },
  res_acc:      { en: "Accuracy", hi: "सटीकता" },
  res_time:     { en: "Time", hi: "समय" },
  res_per:      { en: "{s} s a question", hi: "{s} सेकंड प्रति प्रश्न" },
  res_right:    { en: "Right", hi: "सही" },
  res_wrong:    { en: "Wrong", hi: "गलत" },
  res_skip:     { en: "Skipped", hi: "छोड़े" },
  res_topics:   { en: "By topic", hi: "टॉपिक के अनुसार" },
  res_review:   { en: "Review the answers", hi: "उत्तरों की समीक्षा" },
  res_retry:    { en: "Retry the ones I missed", hi: "जो छूटे उन्हें दोबारा" },
  res_new:      { en: "New set", hi: "नया सेट" },
  res_saved:    { en: "Saved to your progress.", hi: "आपकी प्रगति में सहेजा गया।" },
  res_guest:    { en: "Sign in to keep this result and track your topics.", hi: "यह परिणाम रखने और टॉपिक ट्रैक करने के लिए लॉग इन करें।" },
  f_all:        { en: "All", hi: "सभी" },
  f_wrong:      { en: "Wrong", hi: "गलत" },
  f_skip:       { en: "Skipped", hi: "छोड़े" },
  your_ans:     { en: "Your answer", hi: "आपका उत्तर" },
  right_ans:    { en: "Answer", hi: "उत्तर" },
  none_ans:     { en: "not answered", hi: "उत्तर नहीं दिया" },
  loading:      { en: "Loading questions…", hi: "प्रश्न लोड हो रहे हैं…" },
  err:          { en: "Couldn't load PYQ Practice. Check your connection and try again.", hi: "PYQ अभ्यास लोड नहीं हुआ। कनेक्शन जाँचें और फिर कोशिश करें।" },
  retry:        { en: "Try again", hi: "फिर कोशिश करें" },
  en_only:      { en: "", hi: "प्रश्न अभी अंग्रेज़ी में हैं; हिंदी अनुवाद जल्द।" },
  stmt:         { en: "Statement", hi: "कथन" },
  assertion:    { en: "Assertion (A)", hi: "अभिकथन (A)" },
  reason:       { en: "Reason (R)", hi: "कारण (R)" },
  list1:        { en: "List-I", hi: "सूची-I" },
  list2:        { en: "List-II", hi: "सूची-II" },
  locked_left:  { en: "{n} more questions in this subject are waiting.", hi: "इस विषय में {n} और प्रश्न इंतज़ार कर रहे हैं।" },
};

/** t() for this module: picks the language and fills {placeholders}. */
function useT() {
  const { lang } = useLang();
  return useCallback((k, vars) => {
    const e = S[k];
    let s = e ? (e[lang] ?? e.en) : k;
    if (typeof s === "string" && vars) s = s.replace(/\{(\w+)\}/g, (_, v) => (vars[v] ?? ""));
    return s;
  }, [lang]);
}

const nf = (n) => Number(n || 0).toLocaleString("en-IN");
/* Read in event handlers only: a fresh seed and key for each set started. */
const stamp = () => Date.now();
const rupees = (p) => (Number(p) % 1 === 0 ? String(Number(p)) : Number(p).toFixed(2));

/* ---------------------------------------------------------- emblems -- */
/* Line art for the three subjects, drawn on a 48-unit grid in currentColor. */
export function SubjectEmblem({ code, size = 44 }) {
  const p = { width: size, height: size, viewBox: "0 0 48 48", fill: "none", stroke: "currentColor",
              strokeWidth: 1.8, strokeLinecap: "round", strokeLinejoin: "round", "aria-hidden": true };
  if (code === "ancient") return ( // a stupa: drum, dome, harmika, chhatra
    <svg {...p}>
      <path d="M6 41h36M9 41v-4h30v4M12 37c0-9.5 5.4-16 12-16s12 6.5 12 16" />
      <path d="M21 21v-3h6v3M24 18v-6M19.5 14h9M20.5 11h7M22 8.5h4" />
      <path d="M17 31h14" opacity=".55" />
    </svg>
  );
  if (code === "medieval") return ( // a domed gateway between minarets
    <svg {...p}>
      <path d="M5 41h38M13 41V24h22v17M13 24c0-6.5 5-11 11-11s11 4.5 11 11M24 13V8M22 9.5h4" />
      <path d="M20 41v-8a4 4 0 0 1 8 0v8" />
      <path d="M8 41V19M6.5 19h3l-1.5-4-1.5 4M40 41V19M38.5 19h3L40 15l-1.5 4" />
    </svg>
  );
  return ( // a lotus
    <svg {...p}>
      <path d="M24 37c-3.5-3-5.5-7.5-5.5-12.5S21 14 24 10c3 4 5.5 9.5 5.5 14.5S27.5 34 24 37Z" />
      <path d="M24 37c-6 .5-12-2.5-14.5-8.5 4-1.5 8.5-.5 12 2.5M24 37c6 .5 12-2.5 14.5-8.5-4-1.5-8.5-.5-12 2.5" />
      <path d="M24 37c-7.5 1.5-14.5.5-19-4M24 37c7.5 1.5 14.5.5 19-4M14 41h20" />
    </svg>
  );
}

/* --------------------------------------------------------- the stem -- */
const ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"];
const numberOf = (i, numbering) => (numbering === "roman" ? ROMAN[i] : numbering === "alpha" ? "ABCDEFGH"[i] : String(i + 1));
const splitNum = (s) => {
  const m = /^\s*([0-9]+|[A-H]|[IVX]+)[.)]\s+(.*)$/.exec(s || "");
  return m ? [m[1], m[2]] : [null, s];
};

/** Everything above the options: the question, its statements, pairs, lists or A/R, and the closing line. */
export function PyqStem({ q }) {
  const t = useT();
  const d = q.data || {};
  const statements = Array.isArray(d.statements) ? d.statements : [];
  const pairs = Array.isArray(d.pairs) ? d.pairs : [];
  const l1 = Array.isArray(d.list_1) ? d.list_1 : [];
  const l2 = Array.isArray(d.list_2) ? d.list_2 : [];
  const isAR = q.type === "assertion_reason" && (d.assertion || d.reason);
  const stmtLabels = d.ar_labels === "statement";
  return (
    <div className="pq-stem">
      <p className="pq-body">{q.body}</p>

      {statements.length > 0 && (
        <ol className="pq-stmts">
          {statements.map((s, i) => (
            <li key={i}>
              <span className="pq-num">{d.numbering === "roman" && /^Statement/.test(q.body) ? `${t("stmt")} ${ROMAN[i]}` : numberOf(i, d.numbering)}.</span>
              <span>{s}</span>
            </li>
          ))}
        </ol>
      )}

      {pairs.length > 0 && (
        <div className="pq-table-wrap">
          <table className="pq-table">
            {Array.isArray(d.pairs_head) && (
              <thead><tr><th aria-hidden="true" />{d.pairs_head.map((h, i) => <th key={i}>{h}</th>)}</tr></thead>
            )}
            <tbody>
              {pairs.map((row, i) => {
                const [n, first] = splitNum(row[0]);
                return (
                  <tr key={i}>
                    <td className="pq-td-n">{n || i + 1}.</td>
                    <td>{first}</td>
                    {row.slice(1).map((c, j) => <td key={j}>{c}</td>)}
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}

      {l1.length > 0 && (
        <div className="pq-table-wrap">
          <table className="pq-table pq-lists">
            <thead>
              <tr>
                <th>{d.list_heads?.[0] || t("list1")}</th>
                <th>{d.list_heads?.[1] || t("list2")}</th>
              </tr>
            </thead>
            <tbody>
              {Array.from({ length: Math.max(l1.length, l2.length) }).map((_, i) => {
                const [a, at] = splitNum(l1[i] || "");
                const [b, bt] = splitNum(l2[i] || "");
                return (
                  <tr key={i}>
                    <td>{l1[i] ? <><b className="pq-li">{a}</b>{at}</> : null}</td>
                    <td>{l2[i] ? <><b className="pq-li">{b}</b>{bt}</> : null}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}

      {isAR && (
        <div className="pq-ar">
          <div><span className="pq-ar-tag">{stmtLabels ? `${t("stmt")} I` : t("assertion")}</span><p>{d.assertion}</p></div>
          <div><span className="pq-ar-tag">{stmtLabels ? `${t("stmt")} II` : t("reason")}</span><p>{d.reason}</p></div>
        </div>
      )}

      {d.closing && <p className="pq-closing">{d.closing}</p>}
    </div>
  );
}

/** The options. state: "open" (pickable), "checked" (show right and wrong), "review" (show both, no picking). */
export function PyqOptions({ q, chosen, state = "open", onPick }) {
  return (
    <div className="pq-opts" role="radiogroup">
      {(q.options || []).map((o) => {
        const isChosen = chosen === o.id;
        const isAns = q.answer === o.id;
        let cls = "pq-opt";
        if (state === "open" && isChosen) cls += " chosen";
        if (state !== "open") {
          if (isAns) cls += " right";
          else if (isChosen) cls += " wrong";
          else cls += " dim";
        }
        return (
          <button key={o.id} type="button" className={cls} role="radio" aria-checked={isChosen}
                  disabled={state !== "open"} onClick={() => onPick?.(o.id)}>
            <span className="pq-opt-k">{o.id}</span>
            <span className="pq-opt-t">{o.body}</span>
            {state !== "open" && isAns && <Check size={17} className="pq-opt-i" />}
            {state !== "open" && isChosen && !isAns && <X size={17} className="pq-opt-i" />}
          </button>
        );
      })}
    </div>
  );
}

/* ----------------------------------------------------- local (guest) -- */
const LOCAL = "pyq:guest";
const loadLocal = () => loadKey(LOCAL, { r: {}, b: {} }) || { r: {}, b: {} };
const saveLocal = (v) => saveKey(LOCAL, v);

/* -------------------------------------------------------- set picking -- */
const BIG3 = ["upsc", "cds", "capf"];
const STYLES = ["mcq", "statement_based", "pairs", "match_the_following", "assertion_reason"];

function rng(seed) { // mulberry32
  let a = seed >>> 0;
  return () => {
    a |= 0; a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function filterMeta(meta, f) {
  return meta.filter((m) => {
    if (f.topics.length && !m.t.some((x) => f.topics.includes(x))) return false;
    if (f.exams.length && !f.exams.includes(m.e)) return false;
    if (m.y < f.y0 || m.y > f.y1) return false;
    if (f.styles.length && !f.styles.includes(m.ty)) return false;
    if (f.status === "new" && m.r) return false;
    if (f.status === "wrong" && m.r !== "w") return false;
    if (f.status === "marked" && !m.b) return false;
    if (f.paper && m.l !== f.paper) return false;
    return true;
  });
}

function orderSet(list, order, seed) {
  const a = list.slice();
  if (order === "new") return a.sort((x, y) => y.y - x.y);
  if (order === "old") return a.sort((x, y) => x.y - y.y);
  const r = rng(seed);
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}

/** "UPPCS (Mains) 2014" -> group "UPPCS", chip "Mains 2014"; "UPSC CSE Pre 2024" -> "UPSC CSE Pre", "2024". */
function paperParts(label, examLabel) {
  const m = /^([^\d(]*?)\s*(?=\(|\d)/.exec(label);
  const group = (m && m[1].trim()) || examLabel || label;
  const chip = label.slice(m ? m[0].length : 0).replace(/[()]/g, "").replace(/\s+/g, " ").trim() || label;
  return { group, chip };
}

/* ------------------------------------------------------------- page -- */
export default function PyqPractice({ session, onLogin, onEnroll, onHome, initialSubject = null }) {
  const t = useT();
  const { lang } = useLang();
  const signedIn = !!session;
  const [cat, setCat] = useState(null);
  const [err, setErr] = useState("");
  const [progress, setProgress] = useState(null);
  const [reload, setReload] = useState(0);
  // A subject picked on the home page arrives through storage, read once.
  const [view, setView] = useState(() => {
    const s = initialSubject || takePyqSubject();
    return s ? { name: "subject", subject: s } : { name: "hub" };
  });

  useEffect(() => {
    let alive = true;
    DB.pyqCatalog()
      .then((c) => { if (alive) setCat(c); })
      .catch((e) => { console.error("pyq catalog", e); if (alive) setErr(t("err")); });
    if (signedIn) DB.pyqProgress().then((p) => { if (alive) setProgress(p); });
    return () => { alive = false; };
  }, [signedIn, reload, t]);

  const go = (v) => { setView(v); window.scrollTo({ top: 0, behavior: "smooth" }); };
  const unlock = () => onEnroll?.(PYQ_PLAN);
  const subjects = cat?.subjects || [];
  const subj = view.subject ? subjects.find((s) => s.code === view.subject) : null;
  const name = (o) => (lang === "hi" && o?.nameHi ? o.nameHi : o?.name || "");

  return (
    <div className="pq-root">
      <style>{CSS}</style>
      {err ? (
        <div className="pq-wrap pq-pad">
          <div className="pq-panel pq-center">
            <AlertTriangle size={28} />
            <p>{err}</p>
            <button className="pq-btn pq-btn-ghost" onClick={() => { setErr(""); setReload((k) => k + 1); }}><RotateCcw size={15} />{t("retry")}</button>
          </div>
        </div>
      ) : !cat ? (
        <HubSkeleton />
      ) : view.name === "hub" ? (
        <Hub cat={cat} progress={progress} signedIn={signedIn} name={name} onLogin={onLogin} onUnlock={unlock}
             onHome={onHome} onOpen={(code) => go({ name: "subject", subject: code })} />
      ) : view.name === "subject" && subj ? (
        <Builder key={subj.code} subj={subj} cat={cat} signedIn={signedIn} name={name} progress={progress}
                 onBack={() => go({ name: "hub" })} onUnlock={unlock}
                 onStart={(run) => go({ name: "play", subject: subj.code, run })} />
      ) : view.name === "play" && subj ? (
        <Player key={view.run.key} run={view.run} subj={subj} signedIn={signedIn} name={name}
                onExit={() => { setReload((k) => k + 1); go({ name: "subject", subject: subj.code }); }}
                onDone={(result) => go({ name: "result", subject: subj.code, run: view.run, result })} />
      ) : view.name === "result" && subj ? (
        <Result result={view.result} run={view.run} subj={subj} signedIn={signedIn} onLogin={onLogin}
                onRetry={(ids) => go({ name: "play", subject: subj.code,
                  run: { ...view.run, key: Date.now(), ids, title: view.run.title } })}
                onNew={() => { setReload((k) => k + 1); go({ name: "subject", subject: subj.code }); }}
                onUnlock={cat.access ? null : unlock} plan={cat.plan} />
      ) : (
        <Hub cat={cat} progress={progress} signedIn={signedIn} name={name} onLogin={onLogin} onUnlock={unlock}
             onHome={onHome} onOpen={(code) => go({ name: "subject", subject: code })} />
      )}
    </div>
  );
}

function HubSkeleton() {
  return (
    <>
      <section className="pq-hero"><div className="pq-wrap pq-hero-in"><div className="pq-sk" style={{ height: 180, maxWidth: 560 }} /></div></section>
      <div className="pq-wrap pq-pad"><div className="pq-grid3">{[0, 1, 2].map((i) => <div key={i} className="pq-sk" style={{ height: 230 }} />)}</div></div>
    </>
  );
}

/* --------------------------------------------------------------- hub -- */
function Hub({ cat, progress, signedIn, name, onLogin, onUnlock, onHome, onOpen }) {
  const t = useT();
  const { lang } = useLang();
  const plan = cat.plan;
  const freeTotal = (cat.subjects || []).reduce((n, s) => n + (s.free || 0), 0);
  const span = cat.years?.[0] && cat.years?.[1] ? cat.years[1] - cat.years[0] + 1 : 0;
  const pBy = Object.fromEntries((progress?.subjects || []).map((s) => [s.code, s]));
  const guest = !signedIn ? loadLocal() : null;
  const solved = signedIn ? (progress?.subjects || []).reduce((n, s) => n + s.done, 0) : Object.keys(guest.r).length;
  const right = signedIn ? (progress?.subjects || []).reduce((n, s) => n + s.right, 0)
                         : Object.values(guest.r).filter((v) => v === "c").length;

  return (
    <>
      <section className="pq-hero">
        <div className="pq-hero-glow" aria-hidden="true" />
        <div className="pq-wrap pq-hero-in">
          <div className="pq-hero-copy">
            {onHome && (
              <button className="pq-crumb" onClick={onHome}><ArrowLeft size={14} />JUNOONIAS</button>
            )}
            <div className="pq-eyebrow">{t("eyebrow")}</div>
            <h1 className="pq-h1">{t("h1a")} <em>{t("h1em")}</em></h1>
            <p className="pq-lede">{t("lede", { n: nf(cat.total), p: nf(cat.papers), y0: cat.years?.[0], y1: cat.years?.[1] })}</p>
            <div className="pq-stats">
              <Stat n={nf(cat.total)} l={t("st_q")} />
              <Stat n={nf(cat.papers)} l={t("st_p")} />
              <Stat n={span} l={t("st_y")} />
              <Stat n={(cat.exams || []).length} l={t("st_e")} />
            </div>
            <div className="pq-exam-row" aria-label={t("st_e")}>
              {(cat.exams || []).map((e) => <span key={e.code} className="pq-exam-pill">{e.label}<i>{nf(e.count)}</i></span>)}
            </div>
          </div>

          <div className="pq-hero-side">
            <FannedCards />
            {cat.access ? (
              <div className="pq-unlock pq-unlock-on">
                <Unlock size={20} />
                <div><strong>{t("unlocked")}</strong><span>{t("unlocked_s")}</span></div>
              </div>
            ) : plan ? (
              <div className="pq-unlock">
                <div className="pq-unlock-price">
                  <span className="pq-rupee">₹{rupees(plan.price)}</span>
                  {plan.mrp > plan.price && <s>₹{rupees(plan.mrp)}</s>}
                </div>
                <strong>{t("unlock_t")}</strong>
                <span>{t("unlock_s", { d: plan.days || 365 })}</span>
                <button className="pq-btn pq-btn-gold" onClick={onUnlock}><Lock size={15} />{t("unlock_btn", { p: rupees(plan.price) })}</button>
                <small><Sparkles size={13} />{t("unlock_free", { n: freeTotal })}</small>
              </div>
            ) : null}
          </div>
        </div>
      </section>

      <div className="pq-wrap pq-pad">
        {lang === "hi" && <p className="pq-note">{t("en_only")}</p>}

        {(signedIn ? progress : solved > 0) && (
          <section className="pq-panel pq-me">
            <div className="pq-me-head">
              <h2 className="pq-h3">{t("your")}</h2>
              {!signedIn && <button className="pq-link" onClick={onLogin}>{t("signin")}<ArrowRight size={14} /></button>}
            </div>
            <div className="pq-me-grid">
              <Stat dark n={nf(solved)} l={t("solved")} />
              <Stat dark n={solved ? Math.round((right / solved) * 100) + "%" : "–"} l={t("accuracy")} />
              {signedIn && <Stat dark n={nf(progress?.marked || 0)} l={t("marked")} />}
              {signedIn && <Days days={progress?.days || []} />}
            </div>
            {!signedIn && <p className="pq-muted">{t("guest_note")}</p>}
            {signedIn && progress?.sessions?.length > 0 && (
              <div className="pq-recent">
                <div className="pq-label">{t("recent")}</div>
                {progress.sessions.slice(0, 4).map((s) => (
                  <div key={s.id} className="pq-recent-row">
                    {s.mode === "test" ? <Timer size={15} /> : <Target size={15} />}
                    <span className="pq-recent-t">{s.title || (s.mode === "test" ? t("m_test") : t("m_practice"))}</span>
                    <span className="pq-recent-s">{s.correct}/{s.total}</span>
                    <span className="pq-recent-d">{new Date(s.created_at).toLocaleDateString(lang === "hi" ? "hi-IN" : "en-IN", { day: "numeric", month: "short" })}</span>
                  </div>
                ))}
              </div>
            )}
          </section>
        )}

        <div className="pq-sec-head">
          <h2 className="pq-h2">{t("subjects")}</h2>
          <p className="pq-sub">{t("subjects_s")}</p>
        </div>

        <div className="pq-grid3">
          {(cat.subjects || []).map((s, i) => {
            const mine = signedIn ? pBy[s.code] : null;
            const pct = mine && s.total ? Math.min(100, Math.round((mine.done / s.total) * 100)) : 0;
            return (
              <button key={s.code} className={"pq-subj pq-subj-" + (i % 3)} onClick={() => onOpen(s.code)}>
                <div className="pq-subj-top">
                  <span className="pq-subj-emb"><SubjectEmblem code={s.code} /></span>
                  {signedIn && <Ring pct={pct} label={`${pct}%`} />}
                </div>
                <h3>{name(s)}</h3>
                <p>{lang === "hi" && s.blurbHi ? s.blurbHi : s.blurb}</p>
                <div className="pq-subj-nums">
                  <span><b>{nf(s.total)}</b> {t("st_q")}</span>
                  <span>{t("upsc_n", { n: nf(s.upsc) })}</span>
                  {!cat.access && <span className="pq-free">{t("free_n", { n: s.free })}</span>}
                </div>
                <div className="pq-subj-topics">
                  {(s.topics || []).slice(0, 4).map((tp) => <span key={tp.code}>{name(tp)}</span>)}
                  {(s.topics || []).length > 4 && <span>+{s.topics.length - 4}</span>}
                </div>
                <span className="pq-subj-go">{t("practise")}<ArrowRight size={16} /></span>
              </button>
            );
          })}
        </div>

        <div className="pq-soon">
          <span className="pq-label">{t("soon")}</span>
          {S.soon_list[lang === "hi" ? "hi" : "en"].map((x) => <span key={x} className="pq-soon-chip">{x}</span>)}
        </div>
      </div>
    </>
  );
}

function Stat({ n, l, dark = false }) {
  return <div className={"pq-stat" + (dark ? " pq-stat-dark" : "")}><b>{n}</b><span>{l}</span></div>;
}

function Ring({ pct, label, size = 46 }) {
  const r = (size - 6) / 2, c = 2 * Math.PI * r;
  return (
    <span className="pq-ring" style={{ width: size, height: size }} aria-label={label}>
      <svg width={size} height={size}>
        <circle cx={size / 2} cy={size / 2} r={r} className="pq-ring-bg" />
        <circle cx={size / 2} cy={size / 2} r={r} className="pq-ring-fg"
                strokeDasharray={c} strokeDashoffset={c - (c * pct) / 100} />
      </svg>
      <i>{label}</i>
    </span>
  );
}

function Days({ days }) {
  const set = new Set(days);
  const cells = [];
  const [now] = useState(() => Date.now());
  const today = new Date(now);
  for (let i = 27; i >= 0; i--) {
    const d = new Date(today); d.setDate(today.getDate() - i);
    const k = d.toLocaleDateString("en-CA", { timeZone: "Asia/Kolkata" });
    cells.push(<i key={k} className={set.has(k) ? "on" : ""} title={k} />);
  }
  const t = useT();
  return <div className="pq-days"><span className="pq-label">{t("days28")}</span><div>{cells}</div></div>;
}

/* A fan of three paper slips: the look of the page in one glance. */
function FannedCards() {
  return (
    <div className="pq-fan" aria-hidden="true">
      {[
        { l: "UPSC CSE · 2025", q: "The irrigation device called ‘Araghatta’ was…" },
        { l: "CDS · 2023", q: "Where is the Vikramkhol Cave located?" },
        { l: "UPPCS · 2016", q: "Who got ‘Purana Qila’ of Delhi built in the present form?" },
      ].map((c, i) => (
        <div key={i} className={"pq-slip pq-slip-" + i}>
          <span className="pq-slip-l">{c.l}</span>
          <span className="pq-slip-q">{c.q}</span>
          <span className="pq-slip-o"><i>a</i><i>b</i><i className="on">c</i><i>d</i></span>
        </div>
      ))}
    </div>
  );
}

/* ----------------------------------------------------------- builder -- */
function Builder({ subj, cat, signedIn, name, progress, onBack, onStart, onUnlock }) {
  const t = useT();
  const [meta, setMeta] = useState(null);
  const [err, setErr] = useState("");
  const [tab, setTab] = useState("topic");
  const y0 = cat.years?.[0] || 1990, y1 = cat.years?.[1] || new Date().getFullYear();
  const [f, setF] = useState({ topics: [], exams: [], y0, y1, styles: [], status: "all", paper: null });
  const [size, setSize] = useState(20);
  const [order, setOrder] = useState("shuffle");
  const [mode, setMode] = useState("practice");
  const [refine, setRefine] = useState(false);

  useEffect(() => {
    let alive = true;
    DB.pyqMeta(subj.code).then((m) => {
      if (!alive) return;
      if (!signedIn) { // a guest's own history lives on this device
        const g = loadLocal();
        m = m.map((x) => ({ ...x, r: g.r[x.id] || null, b: !!g.b[x.id] }));
      }
      setMeta(m);
    }).catch((e) => { console.error(e); if (alive) setErr(t("err")); });
    return () => { alive = false; };
  }, [subj.code, signedIn, t]);

  const examLabel = useMemo(() => Object.fromEntries((cat.exams || []).map((e) => [e.code, e.label])), [cat.exams]);
  const topicName = useMemo(() => Object.fromEntries((subj.topics || []).map((x) => [x.code, name(x)])), [subj.topics, name]);
  const myTopics = useMemo(() => Object.fromEntries((progress?.topics || []).filter((x) => x.subject === subj.code)
    .map((x) => [x.code, x])), [progress, subj.code]);

  const matched = useMemo(() => (meta ? filterMeta(meta, f) : []), [meta, f]);
  const open = useMemo(() => (cat.access ? matched : matched.filter((m) => m.f)), [matched, cat.access]);
  const n = size === "all" ? open.length : Math.min(size, open.length);

  const counts = useMemo(() => {
    const c = { topic: {}, exam: {}, style: {} };
    (meta || []).forEach((m) => {
      m.t.forEach((x) => { c.topic[x] = (c.topic[x] || 0) + 1; });
      c.exam[m.e] = (c.exam[m.e] || 0) + 1;
      c.style[m.ty] = (c.style[m.ty] || 0) + 1;
    });
    return c;
  }, [meta]);

  const papers = useMemo(() => {
    const g = new Map();
    (meta || []).forEach((m) => {
      const { group, chip } = paperParts(m.l, examLabel[m.e]);
      const key = m.e + "|" + group;
      if (!g.has(key)) g.set(key, { exam: m.e, group, items: new Map() });
      const it = g.get(key).items;
      if (!it.has(m.l)) it.set(m.l, { label: m.l, chip, year: m.y, n: 0, free: 0 });
      const p = it.get(m.l); p.n++; if (m.f) p.free++;
    });
    const sortE = (e) => { const i = BIG3.indexOf(e); return i < 0 ? 10 : i; };
    return [...g.values()]
      .map((x) => ({ ...x, items: [...x.items.values()].sort((a, b) => b.year - a.year) }))
      .sort((a, b) => sortE(a.exam) - sortE(b.exam) || b.items.length - a.items.length);
  }, [meta, examLabel]);

  const toggle = (key, v) => setF((o) => ({ ...o, paper: null, [key]: o[key].includes(v) ? o[key].filter((x) => x !== v) : [...o[key], v] }));
  const states = (cat.exams || []).filter((e) => !BIG3.includes(e.code) && counts.exam[e.code]).map((e) => e.code);

  const start = (opts = {}) => {
    const fil = { ...f, ...opts };
    const pool = (cat.access ? filterMeta(meta, fil) : filterMeta(meta, fil).filter((m) => m.f));
    const ordered = orderSet(pool, opts.paper ? "new" : order, stamp() % 2147483647);
    const take = opts.paper ? ordered : ordered.slice(0, size === "all" ? ordered.length : size);
    if (!take.length) return;
    const title = opts.paper ? `${opts.paper} · ${name(subj)}`
      : `${name(subj)}${fil.topics.length === 1 ? " · " + topicName[fil.topics[0]] : ""}`;
    onStart({
      key: stamp(), ids: take.map((m) => m.id), mode, title,
      filters: { subject: subj.code, topics: fil.topics, exams: fil.exams, y0: fil.y0, y1: fil.y1, paper: fil.paper || null },
      topicName,
    });
  };

  if (err) return <div className="pq-wrap pq-pad"><div className="pq-panel pq-center"><p>{err}</p></div></div>;

  const years = []; for (let y = y1; y >= y0; y--) years.push(y);
  const locked = matched.length - open.length;

  return (
    <div className="pq-wrap pq-pad pq-builder">
      <button className="pq-crumb pq-crumb-dark" onClick={onBack}><ArrowLeft size={14} />{t("all_subjects")}</button>
      <header className="pq-b-head">
        <span className="pq-b-emb"><SubjectEmblem code={subj.code} size={52} /></span>
        <div>
          <h1 className="pq-h2">{name(subj)}</h1>
          <p className="pq-sub">{nf(subj.total)} {t("st_q")} · {t("upsc_n", { n: nf(subj.upsc) })}</p>
        </div>
      </header>

      <div className="pq-b-grid">
        <div className="pq-b-main">
          <div className="pq-tabs" role="tablist">
            {[["topic", Layers, t("tab_topic")], ["paper", CalendarRange, t("tab_paper")], ["exam", ListChecks, t("tab_exam")]].map(([k, Icon, l]) => (
              <button key={k} role="tab" aria-selected={tab === k} className={"pq-tab" + (tab === k ? " on" : "")} onClick={() => setTab(k)}>
                <Icon size={15} />{l}
              </button>
            ))}
          </div>

          {!meta ? (
            <div className="pq-grid2">{[0, 1, 2, 3].map((i) => <div key={i} className="pq-sk" style={{ height: 76 }} />)}</div>
          ) : tab === "topic" ? (
            <>
              <p className="pq-hint">{t("pick_topics")}</p>
              <div className="pq-grid2">
                <button className={"pq-topic" + (f.topics.length === 0 ? " on" : "")} onClick={() => setF((o) => ({ ...o, topics: [], paper: null }))}>
                  <span className="pq-topic-n">{t("all_topics")}</span>
                  <span className="pq-topic-c">{nf(meta.length)}</span>
                </button>
                {(subj.topics || []).filter((x) => counts.topic[x.code]).map((x) => {
                  const mine = myTopics[x.code];
                  const acc = mine?.done ? Math.round((mine.right / mine.done) * 100) : null;
                  const on = f.topics.includes(x.code);
                  return (
                    <button key={x.code} className={"pq-topic" + (on ? " on" : "")} onClick={() => toggle("topics", x.code)} aria-pressed={on}>
                      <span className="pq-topic-n">{name(x)}</span>
                      <span className="pq-topic-c">{nf(counts.topic[x.code])}</span>
                      {acc !== null && (
                        <span className="pq-topic-bar" title={`${acc}%`}><i style={{ width: Math.min(100, (mine.done / counts.topic[x.code]) * 100) + "%" }} className={acc >= 60 ? "ok" : acc >= 40 ? "mid" : "low"} /></span>
                      )}
                    </button>
                  );
                })}
              </div>
            </>
          ) : tab === "paper" ? (
            <>
              <p className="pq-hint">{t("pick_paper")}</p>
              <div className="pq-papers">
                {papers.map((g) => (
                  <div key={g.exam + g.group} className="pq-paper-g">
                    <div className="pq-paper-h"><span className="pq-exam-tag" data-e={g.exam}>{examLabel[g.exam]}</span>{g.group !== examLabel[g.exam] && <span>{g.group}</span>}</div>
                    <div className="pq-paper-chips">
                      {g.items.map((p) => {
                        const can = cat.access || p.free > 0;
                        return (
                          <button key={p.label} className={"pq-chip" + (can ? "" : " locked")} title={p.label}
                                  onClick={() => (can ? start({ paper: p.label, topics: [], exams: [], styles: [], status: "all", y0, y1 }) : onUnlock())}>
                            {!can && <Lock size={11} />}{p.chip}<i>{cat.access ? p.n : can ? `${p.free}/${p.n}` : p.n}</i>
                          </button>
                        );
                      })}
                    </div>
                  </div>
                ))}
              </div>
            </>
          ) : (
            <>
              <p className="pq-hint">{t("pick_exam")}</p>
              <div className="pq-chips">
                {(cat.exams || []).filter((e) => counts.exam[e.code]).map((e) => (
                  <button key={e.code} className={"pq-chip" + (f.exams.includes(e.code) ? " on" : "")} onClick={() => toggle("exams", e.code)}
                          aria-pressed={f.exams.includes(e.code)}>
                    {e.label}<i>{nf(counts.exam[e.code])}</i>
                  </button>
                ))}
                {states.length > 1 && (
                  <button className={"pq-chip pq-chip-alt" + (states.every((s) => f.exams.includes(s)) ? " on" : "")}
                          onClick={() => setF((o) => {
                            const all = states.every((s) => o.exams.includes(s));
                            return { ...o, exams: all ? o.exams.filter((x) => !states.includes(x)) : [...new Set([...o.exams, ...states])] };
                          })}>
                    {t("state_pcs")}
                  </button>
                )}
              </div>
            </>
          )}

          <button className="pq-refine-t" onClick={() => setRefine((v) => !v)} aria-expanded={refine}>
            <SlidersHorizontal size={15} />{t("refine")}<ChevronRight size={15} className={refine ? "rot" : ""} />
          </button>
          {refine && meta && (
            <div className="pq-refine">
              <div className="pq-field">
                <span className="pq-label">{t("years")}</span>
                <div className="pq-years">
                  <label>{t("from")}
                    <select value={f.y0} onChange={(e) => setF((o) => ({ ...o, y0: Math.min(+e.target.value, o.y1) }))}>
                      {years.slice().reverse().map((y) => <option key={y} value={y}>{y}</option>)}
                    </select>
                  </label>
                  <label>{t("to")}
                    <select value={f.y1} onChange={(e) => setF((o) => ({ ...o, y1: Math.max(+e.target.value, o.y0) }))}>
                      {years.map((y) => <option key={y} value={y}>{y}</option>)}
                    </select>
                  </label>
                  <button className="pq-chip" onClick={() => setF((o) => ({ ...o, y0: Math.max(y0, y1 - 9), y1 }))}>10 yrs</button>
                </div>
              </div>
              <div className="pq-field">
                <span className="pq-label">{t("style")}</span>
                <div className="pq-chips">
                  {STYLES.filter((s) => counts.style[s]).map((s) => (
                    <button key={s} className={"pq-chip" + (f.styles.includes(s) ? " on" : "")} onClick={() => toggle("styles", s)}>
                      {t("ty_" + s)}<i>{counts.style[s]}</i>
                    </button>
                  ))}
                </div>
              </div>
              <div className="pq-field">
                <span className="pq-label">{t("status")}</span>
                <div className="pq-chips">
                  {[["all", t("st_all")], ["new", t("st_new")], ["wrong", t("st_wrong")], ["marked", t("st_marked")]].map(([k, l]) => (
                    <button key={k} className={"pq-chip" + (f.status === k ? " on" : "")} onClick={() => setF((o) => ({ ...o, status: k }))}>{l}</button>
                  ))}
                </div>
              </div>
            </div>
          )}
        </div>

        <aside className="pq-b-side">
          <div className="pq-panel pq-launch">
            <div className="pq-field">
              <span className="pq-label">{t("mode")}</span>
              <div className="pq-modes">
                <button className={"pq-mode" + (mode === "practice" ? " on" : "")} onClick={() => setMode("practice")}>
                  <Target size={18} /><b>{t("m_practice")}</b><span>{t("m_practice_s")}</span>
                </button>
                <button className={"pq-mode" + (mode === "test" ? " on" : "")} onClick={() => setMode("test")}>
                  <Timer size={18} /><b>{t("m_test")}</b><span>{t("m_test_s")}</span>
                </button>
              </div>
            </div>
            <div className="pq-field">
              <span className="pq-label">{t("size")}</span>
              <div className="pq-seg">
                {[10, 20, 30, 50, "all"].map((s) => (
                  <button key={s} className={size === s ? "on" : ""} onClick={() => setSize(s)}>{s === "all" ? t("all") : s}</button>
                ))}
              </div>
            </div>
            <div className="pq-field">
              <span className="pq-label">{t("order")}</span>
              <div className="pq-seg">
                {[["shuffle", t("o_shuffle")], ["new", t("o_new")], ["old", t("o_old")]].map(([k, l]) => (
                  <button key={k} className={order === k ? "on" : ""} onClick={() => setOrder(k)}>{l}</button>
                ))}
              </div>
            </div>
            <div className="pq-count">
              {meta ? (matched.length ? (
                <>
                  <b>{t("match_n", { n: nf(matched.length) })}</b>
                  {locked > 0 && cat.plan && (
                    <span>{t("match_free", { f: nf(open.length), l: nf(locked), p: rupees(cat.plan.price) })}</span>
                  )}
                </>
              ) : <span>{t("match_none")}</span>) : <span>{t("loading")}</span>}
            </div>
            <button className="pq-btn pq-btn-maroon pq-btn-block" disabled={!n} onClick={() => start()}>
              {mode === "test" ? <Timer size={16} /> : <Play size={16} />}{t("start", { n })}
            </button>
            {locked > 0 && cat.plan && (
              <button className="pq-btn pq-btn-gold pq-btn-block" onClick={onUnlock}><Lock size={15} />{t("unlock_btn", { p: rupees(cat.plan.price) })}</button>
            )}
          </div>
        </aside>
      </div>
    </div>
  );
}

/* ------------------------------------------------------------ player -- */
function Player({ run, subj, signedIn, name, onExit, onDone }) {
  const t = useT();
  const [qs, setQs] = useState(null);
  const [err, setErr] = useState("");
  const [i, setI] = useState(0);
  const [ans, setAns] = useState({});         // id -> letter
  const [checked, setChecked] = useState({}); // practice: id -> true once checked
  const [rev, setRev] = useState({});         // test: id -> marked for review
  const [marks, setMarks] = useState({});     // bookmarks
  const [streak, setStreak] = useState(0);
  const [pal, setPal] = useState(false);
  const [now, setNow] = useState(() => Date.now());
  const [t0] = useState(() => Date.now());
  const done = useRef(false);
  // The site header is sticky too; the player's bar docks right under it.
  const [barTop, setBarTop] = useState(0);
  useEffect(() => {
    const read = () => setBarTop(document.querySelector(".pb-head")?.offsetHeight || 0);
    read();
    window.addEventListener("resize", read);
    return () => window.removeEventListener("resize", read);
  }, []);
  const isTest = run.mode === "test";
  const limit = isTest ? run.ids.length * SEC_PER_Q : 0;

  useEffect(() => {
    let alive = true;
    DB.pyqFetch(run.ids).then((list) => {
      if (!alive) return;
      const readable = list.filter((q) => !q.locked);
      const g = !signedIn ? loadLocal() : null;
      setMarks(Object.fromEntries(readable.map((q) => [q.id, signedIn ? !!q.marked : !!g.b[q.id]])));
      setQs(readable);
    }).catch((e) => { console.error(e); if (alive) setErr(t("err")); });
    return () => { alive = false; };
  }, [run.ids, signedIn, t]);

  useEffect(() => {
    const h = setInterval(() => setNow(Date.now()), 1000);
    return () => clearInterval(h);
  }, []);

  const elapsed = Math.floor((now - t0) / 1000);
  const left = isTest ? Math.max(0, limit - elapsed) : 0;

  const finish = useCallback(async (auto = false) => {
    if (done.current || !qs) return;
    done.current = true;
    const items = qs.map((q) => ({ id: q.id, choice: ans[q.id] || null }));
    const right = qs.filter((q) => ans[q.id] === q.answer).length;
    const wrong = qs.filter((q) => ans[q.id] && ans[q.id] !== q.answer).length;
    const local = { total: qs.length, correct: right, wrong, skipped: qs.length - right - wrong,
                    score: Math.round((right * 2 - (wrong * 2) / 3) * 100) / 100, max: qs.length * 2 };
    let saved = false;
    if (signedIn) {
      try {
        const r = await DB.pyqFinish({ mode: run.mode, title: run.title, filters: run.filters, items,
                                       seconds: Math.floor((Date.now() - t0) / 1000) });
        saved = !!r?.ok;
      } catch (e) { console.warn("pyq finish not saved", e); }
    } else {
      const g = loadLocal();
      qs.forEach((q) => { if (ans[q.id]) g.r[q.id] = ans[q.id] === q.answer ? "c" : "w"; });
      saveLocal(g);
    }
    onDone({ ...local, saved, auto, qs, ans, seconds: Math.floor((Date.now() - t0) / 1000) });
  }, [qs, ans, signedIn, run, onDone, t0]);

  useEffect(() => { if (isTest && qs && left === 0) finish(true); }, [isTest, qs, left, finish]);

  const q = qs?.[i];
  const pick = useCallback((letter) => {
    if (!q) return;
    if (!isTest && checked[q.id]) return;
    setAns((a) => ({ ...a, [q.id]: letter }));
    if (!isTest) {
      setChecked((c) => ({ ...c, [q.id]: true }));
      const ok = letter === q.answer;
      setStreak((s) => (ok ? s + 1 : 0));
      if (signedIn) DB.pyqAnswer(q.id, letter).catch((e) => console.warn("answer not saved", e));
    }
  }, [q, isTest, checked, signedIn]);

  const toggleMark = useCallback(() => {
    if (!q) return;
    const on = !marks[q.id];
    setMarks((m) => ({ ...m, [q.id]: on }));
    if (signedIn) DB.pyqMark(q.id, on).catch(() => {});
    else { const g = loadLocal(); if (on) g.b[q.id] = 1; else delete g.b[q.id]; saveLocal(g); }
  }, [q, marks, signedIn]);

  const move = useCallback((d) => setI((x) => Math.max(0, Math.min((qs?.length || 1) - 1, x + d))), [qs]);
  const submit = useCallback(() => {
    const blank = (qs || []).filter((x) => !ans[x.id]).length;
    if (blank && !window.confirm(t("submit_q", { n: blank }))) return;
    finish(false);
  }, [qs, ans, finish, t]);

  useEffect(() => {
    const onKey = (e) => {
      if (e.target && /input|select|textarea/i.test(e.target.tagName)) return;
      const k = e.key.toLowerCase();
      const opts = (q?.options || []).map((o) => o.id);
      if (opts.includes(k)) { pick(k); e.preventDefault(); return; }
      if (/^[1-5]$/.test(k) && opts[+k - 1]) { pick(opts[+k - 1]); e.preventDefault(); return; }
      if (k === "arrowright" || (k === "enter" && (!isTest ? checked[q?.id] : true))) { move(1); e.preventDefault(); }
      else if (k === "arrowleft") { move(-1); e.preventDefault(); }
      else if (k === "m" && isTest && q) setRev((r) => ({ ...r, [q.id]: !r[q.id] }));
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [q, pick, move, isTest, checked]);

  const exit = () => { if (Object.keys(ans).length === 0 || window.confirm(t("exit_q"))) onExit(); };

  if (err) return <div className="pq-wrap pq-pad"><div className="pq-panel pq-center"><p>{err}</p><button className="pq-btn pq-btn-ghost" onClick={onExit}>{t("back")}</button></div></div>;
  if (!qs) return <div className="pq-wrap pq-pad"><div className="pq-sk" style={{ height: 420 }} /></div>;
  if (!qs.length) return <div className="pq-wrap pq-pad"><div className="pq-panel pq-center"><p>{t("match_none")}</p><button className="pq-btn pq-btn-ghost" onClick={onExit}>{t("back")}</button></div></div>;

  const isChecked = !isTest && checked[q.id];
  const answeredN = Object.keys(ans).filter((k) => qs.some((x) => x.id === k)).length;
  const last = i === qs.length - 1;
  const mmss = (s) => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}`;

  return (
    <div className="pq-play">
      <div className="pq-bar" style={{ top: barTop }}>
        <div className="pq-wrap pq-bar-in">
          <button className="pq-icon-btn" onClick={exit} aria-label={t("exit")}><X size={18} /></button>
          <div className="pq-bar-t">
            <span className="pq-bar-s">{name(subj)} · {isTest ? t("m_test") : t("m_practice")}</span>
            <span className="pq-bar-n">{t("q_of", { i: i + 1, n: qs.length })}</span>
          </div>
          {!isTest && streak >= 3 && <span className="pq-streak"><Flame size={15} />{t("streak", { n: streak })}</span>}
          <span className={"pq-clock" + (isTest && left < 60 ? " warn" : "")}>
            <Clock size={15} />{isTest ? mmss(left) : mmss(elapsed)}
          </span>
          {isTest && <button className="pq-btn pq-btn-maroon pq-btn-sm" onClick={submit}>{t("submit")}</button>}
        </div>
        <div className="pq-track" aria-hidden="true">
          {qs.map((x, k) => {
            let c = "";
            if (!isTest && checked[x.id]) c = ans[x.id] === x.answer ? "ok" : "bad";
            else if (ans[x.id]) c = "done";
            if (isTest && rev[x.id]) c += " rev";
            return <i key={x.id} className={c + (k === i ? " cur" : "")} onClick={() => setI(k)} />;
          })}
        </div>
      </div>

      <div className="pq-wrap pq-play-in">
        <article className="pq-card" key={q.id}>
          <div className="pq-card-meta">
            <span className="pq-exam-tag" data-e={q.exam}>{q.label}</span>
            <span className="pq-topic-tag">{run.topicName?.[q.topic] || q.topic}</span>
            <span className="pq-spacer" />
            <button className={"pq-icon-btn" + (marks[q.id] ? " on" : "")} onClick={toggleMark}
                    aria-pressed={!!marks[q.id]} aria-label={t("bookmark")} title={t("bookmark")}>
              {marks[q.id] ? <BookmarkCheck size={18} /> : <Bookmark size={18} />}
            </button>
          </div>

          <PyqStem q={q} />
          <PyqOptions q={q} chosen={ans[q.id]} state={isChecked ? "checked" : "open"} onPick={pick} />

          {isChecked && (
            <div className={"pq-verdict " + (ans[q.id] === q.answer ? "ok" : "bad")} role="status">
              {ans[q.id] === q.answer
                ? <><CheckCircle2 size={18} /><b>{t("correct")}</b></>
                : <><XCircle size={18} /><b>{t("wrong_ans", { a: q.answer })}</b></>}
              {q.explanation && <p>{q.explanation}</p>}
            </div>
          )}

          <div className="pq-card-foot">
            <a className="pq-link pq-link-soft" href={`mailto:${COMPANY.email}?subject=${encodeURIComponent("PYQ issue " + q.id)}&body=${encodeURIComponent(q.label + "\n" + q.body.slice(0, 160) + "\n\n")}`}>
              <Flag size={13} />{t("report")}
            </a>
            <span className="pq-keys"><Keyboard size={13} />{t("keys")}</span>
          </div>
        </article>

        <div className="pq-nav">
          <button className="pq-btn pq-btn-ghost" onClick={() => move(-1)} disabled={i === 0}><ChevronLeft size={16} />{t("prev")}</button>
          {isTest && (
            <>
              <button className={"pq-btn pq-btn-ghost" + (rev[q.id] ? " on" : "")} onClick={() => setRev((r) => ({ ...r, [q.id]: !r[q.id] }))}>
                <Flag size={15} />{t("review_later")}
              </button>
              {ans[q.id] && <button className="pq-btn pq-btn-ghost" onClick={() => setAns((a) => { const b = { ...a }; delete b[q.id]; return b; })}>{t("clear")}</button>}
              <button className="pq-btn pq-btn-ghost pq-pal-t" onClick={() => setPal((v) => !v)}>
                <ListChecks size={15} />{answeredN}/{qs.length}
              </button>
            </>
          )}
          <span className="pq-spacer" />
          {last ? (
            isTest ? <button className="pq-btn pq-btn-maroon" onClick={submit}>{t("submit")}</button>
                   : <button className="pq-btn pq-btn-maroon" onClick={() => finish(false)}><Trophy size={16} />{t("finish")}</button>
          ) : (
            <button className="pq-btn pq-btn-maroon" onClick={() => move(1)}>{t("next")}<ChevronRight size={16} /></button>
          )}
        </div>

        {isTest && pal && (
          <div className="pq-palette">
            <div className="pq-pal-h"><b>{t("palette")}</b>
              <span><i className="done" />{t("lg_ans")}</span><span><i className="rev" />{t("lg_mark")}</span><span><i />{t("lg_none")}</span>
            </div>
            <div className="pq-pal-grid">
              {qs.map((x, k) => (
                <button key={x.id} className={(ans[x.id] ? "done" : "") + (rev[x.id] ? " rev" : "") + (k === i ? " cur" : "")}
                        onClick={() => { setI(k); setPal(false); }}>{k + 1}</button>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

/* ------------------------------------------------------------ result -- */
function Result({ result, run, signedIn, onLogin, onRetry, onNew, onUnlock, plan }) {
  const t = useT();
  const [filter, setFilter] = useState("all");
  const [open, setOpen] = useState(null);
  const { qs, ans } = result;
  const acc = result.correct + result.wrong ? Math.round((result.correct / (result.correct + result.wrong)) * 100) : 0;
  const pct = result.max ? Math.max(0, Math.round((result.score / result.max) * 100)) : 0;
  const missed = qs.filter((q) => ans[q.id] !== q.answer).map((q) => q.id);

  const byTopic = useMemo(() => {
    const m = new Map();
    qs.forEach((q) => {
      const k = q.topic;
      if (!m.has(k)) m.set(k, { k, n: 0, r: 0 });
      const x = m.get(k); x.n++; if (ans[q.id] === q.answer) x.r++;
    });
    return [...m.values()].sort((a, b) => b.n - a.n);
  }, [qs, ans]);

  const shown = qs.filter((q) => filter === "all" || (filter === "wrong" ? ans[q.id] && ans[q.id] !== q.answer : !ans[q.id]));
  const mm = Math.floor(result.seconds / 60), ss = result.seconds % 60;

  return (
    <div className="pq-wrap pq-pad pq-result">
      {result.auto && <div className="pq-banner"><Timer size={16} />{t("time_up")}</div>}
      <section className="pq-res-hero">
        <div className="pq-res-ring">
          <Ring pct={pct} size={132} label={`${result.score}`} />
          <span>/ {result.max}</span>
        </div>
        <div className="pq-res-copy">
          <div className="pq-eyebrow pq-eyebrow-dark">{t("res_title")}</div>
          <h1 className="pq-h2">{run.title}</h1>
          <p className="pq-sub">{t("res_score")}: <b>{result.score}</b> / {result.max}</p>
          <div className="pq-res-stats">
            <span className="ok"><CheckCircle2 size={16} />{result.correct} {t("res_right")}</span>
            <span className="bad"><XCircle size={16} />{result.wrong} {t("res_wrong")}</span>
            <span className="skip"><MinusCircle size={16} />{result.skipped} {t("res_skip")}</span>
          </div>
          <div className="pq-res-stats pq-res-stats-2">
            <span><Target size={15} />{t("res_acc")} {acc}%</span>
            <span><Clock size={15} />{t("res_time")} {mm}:{String(ss).padStart(2, "0")} · {t("res_per", { s: Math.round(result.seconds / Math.max(1, result.total)) })}</span>
          </div>
          <p className="pq-muted">
            {signedIn ? (result.saved ? t("res_saved") : null)
              : <>{t("res_guest")} <button className="pq-link" onClick={onLogin}>{t("signin")}<ArrowRight size={13} /></button></>}
          </p>
          <div className="pq-res-acts">
            {missed.length > 0 && <button className="pq-btn pq-btn-maroon" onClick={() => onRetry(missed)}><RotateCcw size={15} />{t("res_retry")}</button>}
            <button className="pq-btn pq-btn-ghost" onClick={onNew}><Shuffle size={15} />{t("res_new")}</button>
            {onUnlock && plan && <button className="pq-btn pq-btn-gold" onClick={onUnlock}><Lock size={15} />{t("unlock_btn", { p: rupees(plan.price) })}</button>}
          </div>
        </div>
      </section>

      {byTopic.length > 1 && (
        <section className="pq-panel">
          <h2 className="pq-h3">{t("res_topics")}</h2>
          <div className="pq-bars">
            {byTopic.map((x) => (
              <div key={x.k} className="pq-bar-row">
                <span className="pq-bar-l">{run.topicName?.[x.k] || x.k}</span>
                <span className="pq-bar-track"><i style={{ width: (x.r / x.n) * 100 + "%" }} /></span>
                <span className="pq-bar-v">{x.r}/{x.n}</span>
              </div>
            ))}
          </div>
        </section>
      )}

      <section className="pq-review">
        <div className="pq-review-h">
          <h2 className="pq-h3">{t("res_review")}</h2>
          <div className="pq-seg">
            {[["all", t("f_all")], ["wrong", t("f_wrong")], ["skip", t("f_skip")]].map(([k, l]) => (
              <button key={k} className={filter === k ? "on" : ""} onClick={() => setFilter(k)}>{l}</button>
            ))}
          </div>
        </div>
        {shown.map((q) => {
          const k = qs.indexOf(q) + 1;
          const mine = ans[q.id];
          const st = !mine ? "skip" : mine === q.answer ? "ok" : "bad";
          return (
            <div key={q.id} className={"pq-rv pq-rv-" + st}>
              <button className="pq-rv-head" onClick={() => setOpen(open === q.id ? null : q.id)} aria-expanded={open === q.id}>
                <span className="pq-rv-n">{k}</span>
                <span className="pq-rv-q">{q.body}</span>
                <span className="pq-rv-a">{mine ? `(${mine})` : "–"} → <b>({q.answer})</b></span>
                <ChevronRight size={16} className={open === q.id ? "rot" : ""} />
              </button>
              {open === q.id && (
                <div className="pq-rv-body">
                  <div className="pq-card-meta"><span className="pq-exam-tag" data-e={q.exam}>{q.label}</span>
                    <span className="pq-topic-tag">{run.topicName?.[q.topic] || q.topic}</span></div>
                  <PyqStem q={q} />
                  <PyqOptions q={q} chosen={mine} state="review" />
                  {!mine && <p className="pq-muted">{t("your_ans")}: {t("none_ans")}</p>}
                  {q.explanation && <p className="pq-expl">{q.explanation}</p>}
                </div>
              )}
            </div>
          );
        })}
      </section>
    </div>
  );
}

/* --------------------------------------------------------------- CSS -- */
const CSS = `
.pq-root{background:var(--cream-50);color:var(--ink-900);font-family:var(--font-body);min-height:60vh}
.pq-wrap{max-width:1160px;margin:0 auto;padding-left:20px;padding-right:20px}
.pq-pad{padding-top:34px;padding-bottom:64px}
.pq-center{text-align:center;display:flex;flex-direction:column;align-items:center;gap:12px;color:var(--ink-600)}
.pq-panel{background:var(--cream-50);border:1px solid var(--line);border-radius:var(--radius-lg);padding:22px;
  box-shadow:var(--shadow-card)}
.pq-sk{border-radius:var(--radius-md);background:linear-gradient(90deg,var(--cream-100),var(--cream-200),var(--cream-100));
  background-size:200% 100%;animation:pq-sh 1.3s linear infinite}
@keyframes pq-sh{to{background-position:-200% 0}}
.pq-eyebrow{font-family:var(--font-roman);font-size:12.5px;letter-spacing:.24em;text-transform:uppercase;color:var(--gold-300)}
.pq-eyebrow-dark{color:var(--gold-600)}
.pq-h1{font-family:var(--font-display);font-size:clamp(34px,4.6vw,56px);line-height:1.05;margin:12px 0 14px;font-weight:700;letter-spacing:-.01em}
.pq-h1 em{font-family:var(--font-quote);font-style:italic;font-weight:600;color:var(--gold-300)}
.pq-h2{font-family:var(--font-display);font-size:clamp(25px,2.6vw,34px);line-height:1.15;margin:0;font-weight:700;color:var(--ink-900)}
.pq-h3{font-family:var(--font-display);font-size:19px;margin:0;font-weight:700;color:var(--ink-900)}
:lang(hi) .pq-h1,:lang(hi) .pq-h2,:lang(hi) .pq-h3{font-family:var(--font-deva-display)}
:lang(hi) .pq-h1 em{font-family:var(--font-deva-display);font-style:normal}
.pq-sub{color:var(--ink-600);font-size:15.5px;line-height:1.6;margin:6px 0 0}
.pq-muted{color:var(--ink-400);font-size:13.5px;line-height:1.6;margin:10px 0 0}
.pq-note{font-size:13.5px;color:var(--ink-600);background:var(--cream-100);border:1px dashed var(--line);padding:9px 14px;border-radius:var(--radius-sm);margin:0 0 18px}
.pq-label{font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-400);font-weight:600}
.pq-link{background:none;border:0;color:var(--brand-600);font:inherit;font-weight:600;font-size:14px;cursor:pointer;
  display:inline-flex;align-items:center;gap:5px;padding:0;text-decoration:none}
.pq-link-soft{color:var(--ink-400);font-weight:500;font-size:12.5px}
.pq-link-soft:hover{color:var(--brand-600)}
.pq-crumb{display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.22);
  color:var(--on-dark);border-radius:999px;padding:6px 13px;font:inherit;font-size:12.5px;font-weight:600;letter-spacing:.06em;cursor:pointer;margin-bottom:18px}
.pq-crumb-dark{background:var(--cream-100);border-color:var(--line);color:var(--ink-600)}

/* buttons */
.pq-btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;border-radius:999px;padding:12px 20px;
  font:inherit;font-weight:700;font-size:14.5px;border:1.5px solid transparent;cursor:pointer;transition:transform .15s ease,box-shadow .2s ease,background .2s ease;line-height:1.1}
.pq-btn:hover:not(:disabled){transform:translateY(-1px)}
.pq-btn:disabled{opacity:.45;cursor:not-allowed}
.pq-btn:focus-visible,.pq-opt:focus-visible,.pq-topic:focus-visible,.pq-chip:focus-visible,.pq-subj:focus-visible{outline:2.5px solid var(--gold-500);outline-offset:3px}
.pq-btn-sm{padding:8px 14px;font-size:13px}
.pq-btn-block{width:100%}
.pq-btn-gold{background:linear-gradient(155deg,var(--gold-500),var(--gold-600));color:#2a1e05;box-shadow:0 10px 24px -14px rgba(181,135,31,.9)}
.pq-btn-maroon{background:var(--brand-700);color:#fff;box-shadow:0 10px 24px -14px rgba(99,19,34,.8)}
[data-theme="dark"] .pq-btn-maroon{color:#1a0f0b}
.pq-btn-ghost{background:var(--cream-100);border-color:var(--line);color:var(--brand-700)}
.pq-btn-ghost.on{border-color:var(--gold-500);background:var(--gold-100)}
.pq-icon-btn{width:38px;height:38px;border-radius:12px;border:1px solid var(--line);background:var(--cream-50);color:var(--ink-600);
  display:inline-flex;align-items:center;justify-content:center;cursor:pointer;flex:none}
.pq-icon-btn.on{color:var(--gold-600);border-color:var(--gold-500);background:var(--gold-100)}

/* hero */
.pq-hero{position:relative;overflow:hidden;color:var(--on-dark);
  background:linear-gradient(170deg,var(--brand-800) 0%,var(--brand-900) 100%)}
.pq-hero-glow{position:absolute;inset:0;pointer-events:none;
  background:radial-gradient(60% 80% at 82% 40%,rgba(227,200,119,.18),transparent 70%),
             radial-gradient(40% 60% at 10% 100%,rgba(155,42,56,.35),transparent 70%)}
.pq-hero-in{position:relative;display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);gap:40px;align-items:center;
  padding-top:44px;padding-bottom:56px}
.pq-lede{font-size:17px;line-height:1.65;color:var(--on-dark-soft);max-width:560px;margin:0}
.pq-stats{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
.pq-stat{display:flex;flex-direction:column;padding:11px 16px;border-radius:14px;background:rgba(255,255,255,.07);
  border:1px solid rgba(255,255,255,.14);min-width:92px}
.pq-stat b{font-family:var(--font-display);font-size:24px;line-height:1.1;color:var(--gold-300)}
.pq-stat span{font-size:12px;letter-spacing:.06em;color:var(--on-dark-soft);text-transform:uppercase}
.pq-stat-dark{background:var(--cream-100);border-color:var(--line)}
.pq-stat-dark b{color:var(--brand-600)}
.pq-stat-dark span{color:var(--ink-400)}
.pq-exam-row{display:flex;flex-wrap:wrap;gap:6px;margin-top:16px}
.pq-exam-pill{font-size:12px;font-weight:600;letter-spacing:.03em;padding:4px 10px;border-radius:999px;
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.16);color:var(--on-dark)}
.pq-exam-pill i{font-style:normal;margin-left:6px;color:var(--gold-300);font-weight:500}
.pq-hero-side{display:flex;flex-direction:column;align-items:stretch;gap:18px}
.pq-unlock{position:relative;z-index:2;display:flex;flex-direction:column;gap:6px;padding:20px 22px;border-radius:20px;
  background:#fbf6ec;color:#241a15;box-shadow:0 30px 60px -28px rgba(0,0,0,.6)}
.pq-unlock strong{font-family:var(--font-display);font-size:19px}
.pq-unlock > span{font-size:13.5px;color:#5a4a3f;line-height:1.55}
.pq-unlock .pq-btn{margin-top:10px}
.pq-unlock small{display:flex;align-items:center;gap:6px;font-size:12.5px;color:#8a7a6c;margin-top:4px}
.pq-unlock-price{display:flex;align-items:baseline;gap:10px}
.pq-rupee{font-family:var(--font-display);font-weight:800;font-size:44px;line-height:1;color:#631322}
.pq-unlock-price s{color:#8a7a6c;font-size:16px}
.pq-unlock-on{flex-direction:row;align-items:center;gap:14px}
.pq-unlock-on svg{color:#1f7a4c;flex:none}
.pq-unlock-on div{display:flex;flex-direction:column}
.pq-unlock-on span{font-size:13.5px;color:#5a4a3f}

/* the fan of slips */
.pq-fan{position:relative;height:150px;margin:0 12px}
.pq-slip{position:absolute;left:50%;top:10px;width:min(300px,82%);padding:13px 15px;border-radius:14px;background:#fffaf0;color:#241a15;
  box-shadow:0 18px 36px -18px rgba(0,0,0,.55);display:flex;flex-direction:column;gap:7px;transform-origin:50% 120%;
  animation:pq-float 6s ease-in-out infinite}
.pq-slip-0{transform:translateX(-50%) rotate(-9deg) translateX(-34px);opacity:.82;animation-delay:-2s}
.pq-slip-1{transform:translateX(-50%) rotate(7deg) translateX(34px);opacity:.9;animation-delay:-4s}
.pq-slip-2{transform:translateX(-50%) translateY(14px);z-index:1}
@keyframes pq-float{50%{margin-top:-5px}}
.pq-slip-l{font-size:10.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#b5871f}
.pq-slip-q{font-family:var(--font-display);font-size:14px;line-height:1.35}
.pq-slip-o{display:flex;gap:6px}
.pq-slip-o i{font-style:normal;width:22px;height:22px;border-radius:7px;border:1px solid #e7dcc4;font-size:11px;font-weight:700;
  display:grid;place-items:center;color:#8a7a6c;text-transform:uppercase}
.pq-slip-o i.on{background:#1f7a4c;border-color:#1f7a4c;color:#fff}
@media (prefers-reduced-motion:reduce){.pq-slip{animation:none}}

/* my progress */
.pq-me{margin-bottom:34px}
.pq-me-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px}
.pq-me-grid{display:flex;flex-wrap:wrap;gap:12px;align-items:stretch}
.pq-days{display:flex;flex-direction:column;gap:7px;padding:10px 14px;border-radius:14px;border:1px solid var(--line);background:var(--cream-100)}
.pq-days div{display:grid;grid-template-columns:repeat(14,12px);gap:4px}
.pq-days i{width:12px;height:12px;border-radius:3px;background:var(--cream-200)}
.pq-days i.on{background:var(--gold-500)}
.pq-recent{margin-top:16px;display:flex;flex-direction:column;gap:6px}
.pq-recent-row{display:flex;align-items:center;gap:10px;font-size:14px;padding:8px 2px;border-top:1px solid var(--line);color:var(--ink-600)}
.pq-recent-t{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--ink-900)}
.pq-recent-s{font-weight:700;color:var(--brand-600)}
.pq-recent-d{font-size:12.5px;color:var(--ink-400)}

/* subjects */
.pq-sec-head{margin:6px 0 20px}
.pq-grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}
.pq-subj{position:relative;text-align:left;font:inherit;color:inherit;cursor:pointer;border-radius:var(--radius-lg);
  border:1px solid var(--line);background:var(--cream-50);padding:22px 22px 20px;display:flex;flex-direction:column;gap:10px;
  box-shadow:var(--shadow-card);transition:transform .2s ease,box-shadow .2s ease,border-color .2s ease;overflow:hidden}
.pq-subj::before{content:"";position:absolute;inset:0 0 auto 0;height:4px;background:linear-gradient(90deg,var(--gold-500),var(--brand-600))}
.pq-subj:hover{transform:translateY(-3px);box-shadow:var(--shadow-lift);border-color:var(--gold-500)}
.pq-subj-top{display:flex;justify-content:space-between;align-items:flex-start}
.pq-subj-emb{width:62px;height:62px;border-radius:18px;display:grid;place-items:center;color:var(--brand-600);
  background:linear-gradient(150deg,var(--gold-100),var(--cream-100));border:1px solid var(--line)}
.pq-subj-1 .pq-subj-emb{color:#7a4a12}
.pq-subj-2 .pq-subj-emb{color:#1f6a5a}
[data-theme="dark"] .pq-subj-1 .pq-subj-emb,[data-theme="dark"] .pq-subj-2 .pq-subj-emb{color:var(--gold-300)}
.pq-subj h3{font-family:var(--font-display);font-size:22px;margin:4px 0 0;font-weight:700}
:lang(hi) .pq-subj h3{font-family:var(--font-deva-display)}
.pq-subj p{margin:0;color:var(--ink-600);font-size:14px;line-height:1.55;min-height:44px}
.pq-subj-nums{display:flex;flex-wrap:wrap;gap:6px 12px;font-size:13px;color:var(--ink-600)}
.pq-subj-nums b{font-family:var(--font-display);font-size:18px;color:var(--ink-900)}
.pq-free{color:#1f7a4c;font-weight:700}
[data-theme="dark"] .pq-free{color:var(--ok-600)}
.pq-subj-topics{display:flex;flex-wrap:wrap;gap:6px}
.pq-subj-topics span{font-size:12px;padding:3px 9px;border-radius:999px;background:var(--cream-100);border:1px solid var(--line);color:var(--ink-600)}
.pq-subj-go{margin-top:auto;padding-top:8px;display:inline-flex;align-items:center;gap:6px;font-weight:700;color:var(--brand-600)}
.pq-ring{position:relative;display:inline-grid;place-items:center;flex:none}
.pq-ring svg{transform:rotate(-90deg)}
.pq-ring circle{fill:none;stroke-width:5}
.pq-ring-bg{stroke:var(--cream-200)}
.pq-ring-fg{stroke:var(--gold-500);stroke-linecap:round;transition:stroke-dashoffset .8s ease}
.pq-ring i{position:absolute;font-style:normal;font-size:11.5px;font-weight:700;color:var(--ink-600)}
.pq-soon{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-top:26px}
.pq-soon-chip{font-size:12.5px;padding:5px 11px;border-radius:999px;border:1px dashed var(--line);color:var(--ink-400)}

/* builder */
.pq-b-head{display:flex;align-items:center;gap:16px;margin:4px 0 26px}
.pq-b-emb{width:76px;height:76px;border-radius:22px;display:grid;place-items:center;color:var(--brand-600);
  background:linear-gradient(150deg,var(--gold-100),var(--cream-100));border:1px solid var(--line);flex:none}
.pq-b-grid{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:26px;align-items:start}
.pq-b-side{position:sticky;top:84px}
.pq-tabs{display:flex;gap:6px;padding:5px;border-radius:999px;background:var(--cream-100);border:1px solid var(--line);width:max-content;max-width:100%;overflow-x:auto}
.pq-tab{display:inline-flex;align-items:center;gap:7px;border:0;background:none;font:inherit;font-weight:600;font-size:14px;color:var(--ink-600);
  padding:9px 16px;border-radius:999px;cursor:pointer;white-space:nowrap}
.pq-tab.on{background:var(--cream-50);color:var(--brand-700);box-shadow:var(--shadow-card)}
.pq-hint{color:var(--ink-400);font-size:13.5px;margin:16px 0 12px}
.pq-grid2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.pq-topic{position:relative;display:flex;align-items:center;gap:10px;text-align:left;font:inherit;cursor:pointer;
  padding:15px 16px 17px;border-radius:var(--radius-md);border:1.5px solid var(--line);background:var(--cream-50);color:var(--ink-900);
  transition:border-color .15s ease,background .15s ease,transform .15s ease}
.pq-topic:hover{border-color:var(--gold-500)}
.pq-topic.on{border-color:var(--brand-600);background:var(--gold-100)}
.pq-topic-n{flex:1;font-weight:600;font-size:14.5px;line-height:1.35}
.pq-topic-c{font-family:var(--font-display);font-weight:700;color:var(--brand-600);font-size:17px}
.pq-topic-bar{position:absolute;left:16px;right:16px;bottom:7px;height:3px;border-radius:3px;background:var(--cream-200);overflow:hidden}
.pq-topic-bar i{display:block;height:100%;border-radius:3px}
.pq-topic-bar i.ok{background:var(--ok-600)}.pq-topic-bar i.mid{background:var(--gold-500)}.pq-topic-bar i.low{background:var(--bad-600)}
.pq-chips{display:flex;flex-wrap:wrap;gap:8px}
.pq-chip{display:inline-flex;align-items:center;gap:6px;font:inherit;font-size:13.5px;font-weight:600;padding:7px 13px;border-radius:999px;
  border:1.5px solid var(--line);background:var(--cream-50);color:var(--ink-900);cursor:pointer}
.pq-chip i{font-style:normal;font-weight:500;color:var(--ink-400);font-size:12px}
.pq-chip.on{border-color:var(--brand-600);background:var(--gold-100);color:var(--brand-700)}
.pq-chip.locked{color:var(--ink-400);background:var(--cream-100)}
.pq-chip-alt{border-style:dashed}
.pq-papers{display:flex;flex-direction:column;gap:16px}
.pq-paper-g{padding:14px 16px;border-radius:var(--radius-md);border:1px solid var(--line);background:var(--cream-50)}
.pq-paper-h{display:flex;align-items:center;gap:8px;margin-bottom:10px;font-size:13.5px;font-weight:600;color:var(--ink-600)}
.pq-paper-chips{display:flex;flex-wrap:wrap;gap:7px}
.pq-paper-chips .pq-chip{padding:5px 11px;font-size:13px}
.pq-exam-tag{display:inline-flex;align-items:center;font-size:11.5px;font-weight:700;letter-spacing:.06em;padding:4px 10px;border-radius:999px;
  background:var(--brand-700);color:#fff}
[data-theme="dark"] .pq-exam-tag{color:#1a0f0b}
.pq-exam-tag[data-e="cds"],.pq-exam-tag[data-e="capf"]{background:#2d5a3d;color:#fff}
.pq-exam-tag:not([data-e="upsc"]):not([data-e="cds"]):not([data-e="capf"]){background:var(--gold-600);color:#241a15}
.pq-topic-tag{font-size:12px;font-weight:600;padding:4px 10px;border-radius:999px;background:var(--cream-100);border:1px solid var(--line);color:var(--ink-600)}
.pq-refine-t{display:inline-flex;align-items:center;gap:7px;margin-top:22px;border:0;background:none;font:inherit;font-weight:700;color:var(--brand-600);cursor:pointer;padding:4px 0}
.pq-refine-t .rot,.pq-rv-head .rot{transform:rotate(90deg)}
.pq-refine{display:flex;flex-direction:column;gap:16px;margin-top:12px;padding:16px;border-radius:var(--radius-md);background:var(--cream-100);border:1px solid var(--line)}
.pq-field{display:flex;flex-direction:column;gap:9px}
.pq-years{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.pq-years label{display:inline-flex;align-items:center;gap:7px;font-size:13.5px;color:var(--ink-600)}
.pq-years select{font:inherit;font-size:14px;padding:7px 10px;border-radius:10px;border:1px solid var(--line);background:var(--cream-50);color:var(--ink-900)}
.pq-launch{display:flex;flex-direction:column;gap:18px}
.pq-modes{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.pq-mode{display:flex;flex-direction:column;align-items:flex-start;gap:4px;text-align:left;font:inherit;cursor:pointer;padding:12px;border-radius:var(--radius-md);
  border:1.5px solid var(--line);background:var(--cream-50);color:var(--ink-900)}
.pq-mode svg{color:var(--brand-600)}
.pq-mode b{font-size:14px}
.pq-mode span{font-size:12px;color:var(--ink-400);line-height:1.4}
.pq-mode.on{border-color:var(--brand-600);background:var(--gold-100)}
.pq-seg{display:flex;flex-wrap:wrap;gap:4px;padding:4px;border-radius:12px;background:var(--cream-100);border:1px solid var(--line)}
.pq-seg button{flex:1;border:0;background:none;font:inherit;font-size:13px;font-weight:600;color:var(--ink-600);padding:7px 8px;border-radius:9px;cursor:pointer;white-space:nowrap}
.pq-seg button.on{background:var(--cream-50);color:var(--brand-700);box-shadow:var(--shadow-card)}
.pq-count{display:flex;flex-direction:column;gap:4px;font-size:13.5px;color:var(--ink-600);line-height:1.5}
.pq-count b{font-size:15px;color:var(--ink-900)}

/* player */
.pq-play{min-height:80vh;background:var(--cream-100)}
.pq-bar{position:sticky;top:0;z-index:40;background:var(--cream-50);border-bottom:1px solid var(--line)}
.pq-bar-in{display:flex;align-items:center;gap:12px;padding-top:10px;padding-bottom:10px}
.pq-bar-t{flex:1;min-width:0;display:flex;flex-direction:column}
.pq-bar-s{font-size:12px;color:var(--ink-400);letter-spacing:.04em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.pq-bar-n{font-weight:700;font-size:15px}
.pq-clock{display:inline-flex;align-items:center;gap:6px;font-variant-numeric:tabular-nums;font-weight:700;padding:7px 11px;border-radius:10px;
  background:var(--cream-100);border:1px solid var(--line);color:var(--ink-600)}
.pq-clock.warn{color:#fff;background:var(--bad-600);border-color:var(--bad-600)}
.pq-streak{display:inline-flex;align-items:center;gap:5px;font-size:13px;font-weight:700;color:#c9521f;animation:pq-pop .4s ease}
@keyframes pq-pop{0%{transform:scale(.6);opacity:0}70%{transform:scale(1.1)}100%{transform:scale(1);opacity:1}}
.pq-track{display:flex;gap:3px;padding:0 20px 8px;max-width:1160px;margin:0 auto}
.pq-track i{flex:1;height:5px;border-radius:5px;background:var(--cream-200);cursor:pointer;min-width:4px}
.pq-track i.done{background:var(--gold-300)}.pq-track i.ok{background:var(--ok-600)}.pq-track i.bad{background:var(--bad-600)}
.pq-track i.rev{box-shadow:inset 0 -2px 0 var(--brand-600)}
.pq-track i.cur{outline:2px solid var(--brand-600);outline-offset:1px}
.pq-play-in{max-width:820px;padding-top:24px;padding-bottom:60px}
.pq-card{background:var(--cream-50);border:1px solid var(--line);border-radius:var(--radius-lg);padding:24px 26px;box-shadow:var(--shadow-card);
  animation:pq-in .28s ease}
@keyframes pq-in{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.pq-card-meta{display:flex;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:16px}
.pq-spacer{flex:1}
.pq-stem{display:flex;flex-direction:column;gap:12px;margin-bottom:18px}
.pq-body{margin:0;font-size:17.5px;line-height:1.6;font-weight:500;color:var(--ink-900)}
.pq-stmts{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}
.pq-stmts li{display:flex;gap:10px;font-size:15.5px;line-height:1.6;padding:10px 14px;border-radius:12px;background:var(--cream-100);border:1px solid var(--line)}
.pq-num{font-weight:700;color:var(--brand-600);flex:none;min-width:22px}
.pq-table-wrap{overflow-x:auto;border-radius:12px;border:1px solid var(--line)}
.pq-table{width:100%;border-collapse:collapse;font-size:15px;line-height:1.5}
.pq-table th{background:var(--cream-100);text-align:left;font-size:12.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-600);padding:10px 14px;font-weight:700}
.pq-table td{padding:10px 14px;border-top:1px solid var(--line);vertical-align:top}
.pq-td-n{width:1%;white-space:nowrap;font-weight:700;color:var(--brand-600)}
.pq-lists td{width:50%}
.pq-li{color:var(--brand-600);margin-right:8px}
.pq-ar{display:flex;flex-direction:column;gap:8px}
.pq-ar div{padding:12px 14px;border-radius:12px;background:var(--cream-100);border:1px solid var(--line)}
.pq-ar-tag{font-size:11.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--brand-600)}
.pq-ar p{margin:4px 0 0;font-size:15.5px;line-height:1.6}
.pq-closing{margin:0;font-weight:600;font-size:15.5px;color:var(--ink-900)}
.pq-opts{display:flex;flex-direction:column;gap:10px}
.pq-opt{display:flex;align-items:center;gap:14px;text-align:left;font:inherit;cursor:pointer;padding:14px 16px;border-radius:14px;
  border:1.5px solid var(--line);background:var(--cream-50);color:var(--ink-900);font-size:15.5px;line-height:1.5;
  transition:border-color .15s ease,background .15s ease,transform .12s ease}
.pq-opt:hover:not(:disabled){border-color:var(--gold-500);transform:translateX(2px)}
.pq-opt-k{flex:none;width:32px;height:32px;border-radius:10px;display:grid;place-items:center;font-weight:800;text-transform:uppercase;
  background:var(--cream-100);border:1px solid var(--line);color:var(--ink-600);font-size:13.5px}
.pq-opt-t{flex:1}
.pq-opt-i{flex:none}
.pq-opt.chosen{border-color:var(--brand-600);background:var(--gold-100)}
.pq-opt.chosen .pq-opt-k{background:var(--brand-700);color:#fff;border-color:var(--brand-700)}
.pq-opt.right{border-color:var(--ok-600);background:rgba(31,122,76,.09);animation:pq-pop .35s ease}
.pq-opt.right .pq-opt-k{background:var(--ok-600);color:#fff;border-color:var(--ok-600)}
.pq-opt.right .pq-opt-i{color:var(--ok-600)}
.pq-opt.wrong{border-color:var(--bad-600);background:rgba(163,49,42,.08);animation:pq-shake .35s ease}
.pq-opt.wrong .pq-opt-k{background:var(--bad-600);color:#fff;border-color:var(--bad-600)}
.pq-opt.wrong .pq-opt-i{color:var(--bad-600)}
.pq-opt.dim{opacity:.6}
.pq-opt:disabled{cursor:default}
@keyframes pq-shake{25%{transform:translateX(-4px)}75%{transform:translateX(4px)}}
.pq-verdict{margin-top:16px;padding:14px 16px;border-radius:14px;display:flex;flex-wrap:wrap;align-items:center;gap:8px;animation:pq-in .25s ease}
.pq-verdict.ok{background:rgba(31,122,76,.1);color:var(--ok-600)}
.pq-verdict.bad{background:rgba(163,49,42,.09);color:var(--bad-600)}
.pq-verdict p{flex-basis:100%;margin:4px 0 0;color:var(--ink-900);font-size:14.5px;line-height:1.6}
.pq-card-foot{display:flex;flex-wrap:wrap;justify-content:space-between;gap:10px;margin-top:18px;padding-top:14px;border-top:1px solid var(--line)}
.pq-keys{display:inline-flex;align-items:center;gap:6px;font-size:12px;color:var(--ink-400)}
.pq-nav{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px;align-items:center}
.pq-palette{margin-top:14px;padding:16px;border-radius:var(--radius-md);background:var(--cream-50);border:1px solid var(--line);box-shadow:var(--shadow-card)}
.pq-pal-h{display:flex;flex-wrap:wrap;gap:12px;align-items:center;font-size:12.5px;color:var(--ink-600);margin-bottom:12px}
.pq-pal-h b{font-size:14px;color:var(--ink-900);margin-right:auto}
.pq-pal-h span{display:inline-flex;align-items:center;gap:5px}
.pq-pal-h i{width:12px;height:12px;border-radius:4px;background:var(--cream-200);display:inline-block}
.pq-pal-h i.done{background:var(--gold-500)}.pq-pal-h i.rev{background:var(--brand-600)}
.pq-pal-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(40px,1fr));gap:6px}
.pq-pal-grid button{height:38px;border-radius:10px;border:1px solid var(--line);background:var(--cream-100);font:inherit;font-weight:700;color:var(--ink-600);cursor:pointer}
.pq-pal-grid button.done{background:var(--gold-300);color:#241a15;border-color:var(--gold-500)}
.pq-pal-grid button.rev{box-shadow:inset 0 -3px 0 var(--brand-600)}
.pq-pal-grid button.cur{outline:2px solid var(--brand-600)}

/* result */
.pq-banner{display:flex;align-items:center;gap:8px;padding:12px 16px;border-radius:12px;background:var(--gold-100);color:var(--ink-900);margin-bottom:18px;font-weight:600}
.pq-res-hero{display:grid;grid-template-columns:auto 1fr;gap:30px;align-items:center;padding:26px;border-radius:var(--radius-lg);
  background:var(--cream-50);border:1px solid var(--line);box-shadow:var(--shadow-card);margin-bottom:22px}
.pq-res-ring{display:flex;flex-direction:column;align-items:center;gap:4px}
.pq-res-ring .pq-ring circle{stroke-width:9}
.pq-res-ring .pq-ring i{font-family:var(--font-display);font-size:30px;color:var(--ink-900)}
.pq-res-ring > span{color:var(--ink-400);font-size:13px}
.pq-res-stats{display:flex;flex-wrap:wrap;gap:8px 18px;margin-top:14px;font-weight:600;font-size:14.5px}
.pq-res-stats span{display:inline-flex;align-items:center;gap:6px}
.pq-res-stats .ok{color:var(--ok-600)}.pq-res-stats .bad{color:var(--bad-600)}.pq-res-stats .skip{color:var(--ink-400)}
.pq-res-stats-2{font-weight:500;color:var(--ink-600);font-size:13.5px;margin-top:8px}
.pq-res-acts{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}
.pq-bars{display:flex;flex-direction:column;gap:10px;margin-top:14px}
.pq-bar-row{display:grid;grid-template-columns:minmax(120px,240px) 1fr 52px;gap:12px;align-items:center;font-size:14px}
.pq-bar-l{color:var(--ink-600)}
.pq-bar-track{height:9px;border-radius:9px;background:var(--cream-200);overflow:hidden}
.pq-bar-track i{display:block;height:100%;border-radius:9px;background:linear-gradient(90deg,var(--gold-500),var(--ok-600))}
.pq-bar-v{font-weight:700;text-align:right}
.pq-result .pq-panel{margin-bottom:22px}
.pq-review-h{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:12px;margin:8px 0 14px}
.pq-rv{border:1px solid var(--line);border-radius:var(--radius-md);background:var(--cream-50);margin-bottom:8px;overflow:hidden;border-left-width:4px}
.pq-rv-ok{border-left-color:var(--ok-600)}.pq-rv-bad{border-left-color:var(--bad-600)}.pq-rv-skip{border-left-color:var(--line)}
.pq-rv-head{width:100%;display:flex;align-items:center;gap:12px;padding:12px 14px;border:0;background:none;font:inherit;color:inherit;text-align:left;cursor:pointer}
.pq-rv-n{flex:none;width:28px;height:28px;border-radius:9px;display:grid;place-items:center;background:var(--cream-100);font-weight:700;font-size:13px}
.pq-rv-q{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-size:14.5px}
.pq-rv-a{flex:none;font-size:13px;color:var(--ink-400)}
.pq-rv-a b{color:var(--ok-600)}
.pq-rv-body{padding:4px 18px 18px}
.pq-expl{font-size:14.5px;line-height:1.65;color:var(--ink-600);margin:14px 0 0}

@media (max-width:980px){
  .pq-hero-in{grid-template-columns:1fr;gap:26px}
  .pq-b-grid{grid-template-columns:1fr}
  .pq-b-side{position:static}
  .pq-grid3{grid-template-columns:repeat(2,minmax(0,1fr))}
}
@media (max-width:640px){
  .pq-wrap{padding-left:16px;padding-right:16px}
  .pq-pad{padding-top:24px}
  .pq-hero-in{padding-top:30px;padding-bottom:36px}
  .pq-grid3,.pq-grid2{grid-template-columns:1fr}
  .pq-stat{min-width:0;flex:1 1 40%}
  .pq-fan{display:none}
  .pq-card{padding:18px 16px}
  .pq-body{font-size:16.5px}
  .pq-opt{padding:12px 13px;gap:11px;font-size:15px}
  .pq-res-hero{grid-template-columns:1fr;text-align:left;padding:20px}
  .pq-bar-row{grid-template-columns:1fr 46px}
  .pq-bar-l{grid-column:1 / -1}
  .pq-keys{display:none}
  .pq-nav .pq-btn{padding:11px 14px}
  .pq-track{padding:0 16px 8px}
  .pq-bar-s{display:none}
}
`;

/* ============================================================
   HOME TEASER

   Sits under the quote band on the home page. Counts from pyq_catalog(), and
   one live free question the visitor can answer on the spot, fetched only
   once the section scrolls near the screen so the home page stays light.
   ============================================================ */

const T2 = {
  eyebrow: { en: "New · PYQ Practice", hi: "नया · PYQ अभ्यास" },
  h2a:     { en: "Practise what UPSC has", hi: "वही अभ्यास करें जो UPSC" },
  h2em:    { en: "already asked.", hi: "पहले पूछ चुका है।" },
  sub:     { en: "Every Prelims question by subject, topic, exam and year, with instant checking or a timed test. {f} questions are free; ₹{p} unlocks all {n}.",
             hi: "प्रीलिम्स का हर प्रश्न विषय, टॉपिक, परीक्षा और वर्ष के अनुसार, तुरंत जाँच या टाइम्ड टेस्ट के साथ। {f} प्रश्न मुफ़्त; ₹{p} में सभी {n} खुलते हैं।" },
  cta:     { en: "Start practising free", hi: "मुफ़्त अभ्यास शुरू करें" },
  try:     { en: "Try one now", hi: "अभी एक आज़माएँ" },
  another: { en: "Another question", hi: "दूसरा प्रश्न" },
  more:    { en: "Open PYQ Practice", hi: "PYQ अभ्यास खोलें" },
  right:   { en: "Correct. That was a real {l} question.", hi: "सही। यह {l} का असली प्रश्न था।" },
  wrong:   { en: "The answer is ({a}). That was {l}.", hi: "उत्तर ({a}) है। यह {l} का प्रश्न था।" },
};

export function PyqTeaser({ onOpen }) {
  const { lang } = useLang();
  const tt = useT();
  const t = (k, v) => {
    const e = T2[k];
    let s = e ? (e[lang] ?? e.en) : tt(k, v);
    if (e && v) s = s.replace(/\{(\w+)\}/g, (_, x) => v[x] ?? "");
    return s;
  };
  const [cat, setCat] = useState(null);
  const [pool, setPool] = useState(null);
  const [k, setK] = useState(0);
  const [pick, setPick] = useState(null);
  const root = useRef(null);
  const wanted = useRef(false);

  useEffect(() => {
    let alive = true;
    DB.pyqCatalog().then((c) => { if (alive) setCat(c); }).catch(() => {});
    return () => { alive = false; };
  }, []);

  /* One free question set, loaded when the section is about to be seen. */
  useEffect(() => {
    if (!cat?.subjects?.length) return undefined;
    const el = root.current;
    let alive = true;
    const load = async () => {
      if (wanted.current) return;
      wanted.current = true;
      try {
        const subj = cat.subjects[Math.floor(Math.random() * cat.subjects.length)];
        const meta = await DB.pyqMeta(subj.code);
        const free = meta.filter((m) => m.f);
        const easy = free.filter((m) => m.ty === "mcq");
        const ids = orderSet(easy.length >= 3 ? easy : free, "shuffle", Date.now() % 99991).slice(0, 6).map((m) => m.id);
        const qs = (await DB.pyqFetch(ids)).filter((q) => !q.locked);
        if (alive) setPool(qs);
      } catch (e) { console.warn("pyq teaser", e); }
    };
    if (!el || typeof IntersectionObserver === "undefined") { load(); return () => { alive = false; }; }
    const io = new IntersectionObserver((es) => { if (es.some((x) => x.isIntersecting)) { io.disconnect(); load(); } }, { rootMargin: "300px" });
    io.observe(el);
    return () => { alive = false; io.disconnect(); };
  }, [cat]);

  if (cat && !cat.total) return null;
  const q = pool?.length ? pool[k % pool.length] : null;
  const free = (cat?.subjects || []).reduce((n, s) => n + (s.free || 0), 0);
  const span = cat?.years?.[0] ? cat.years[1] - cat.years[0] + 1 : 0;
  const name = (o) => (lang === "hi" && o?.nameHi ? o.nameHi : o?.name || "");

  return (
    <section className="pqt" ref={root} id="pyq">
      <style>{CSS + TEASER_CSS}</style>
      <div className="pq-wrap pqt-in">
        <div className="pqt-copy">
          <div className="pq-eyebrow pq-eyebrow-dark">{t("eyebrow")}</div>
          <h2 className="pq-h2 pqt-h2">{t("h2a")} <em>{t("h2em")}</em></h2>
          <p className="pq-sub">{cat ? t("sub", { f: free, p: rupees(cat.plan?.price ?? 9), n: nf(cat.total) }) : " "}</p>
          <div className="pqt-stats">
            <Stat dark n={cat ? nf(cat.total) : "–"} l={tt("st_q")} />
            <Stat dark n={cat ? nf(cat.papers) : "–"} l={tt("st_p")} />
            <Stat dark n={cat ? (cat.exams || []).length : "–"} l={tt("st_e")} />
            <Stat dark n={cat ? span : "–"} l={tt("st_y")} />
          </div>
          <div className="pqt-subjects">
            {(cat?.subjects || []).map((s) => (
              <button key={s.code} className="pqt-subj" onClick={() => { openPyqSubject(s.code); onOpen(); }}>
                <span className="pqt-subj-emb"><SubjectEmblem code={s.code} size={30} /></span>
                <span className="pqt-subj-t"><b>{name(s)}</b><i>{nf(s.total)} {tt("st_q")}</i></span>
                <ArrowRight size={15} />
              </button>
            ))}
          </div>
          <div className="pqt-ctas">
            <button className="pq-btn pq-btn-maroon" onClick={() => onOpen()}><Play size={16} />{t("cta")}</button>
            {cat?.plan && !cat.access && (
              <span className="pqt-price"><Lock size={14} />₹{rupees(cat.plan.price)} · {tt("all_subjects").toLowerCase()}</span>
            )}
          </div>
        </div>

        <div className="pqt-try">
          <div className="pqt-try-head"><Sparkles size={15} />{t("try")}</div>
          {!q ? (
            <div className="pq-card">
              <div className="pq-sk" style={{ height: 22, width: "40%" }} />
              <div className="pq-sk" style={{ height: 56, marginTop: 16 }} />
              {[0, 1, 2, 3].map((i) => <div key={i} className="pq-sk" style={{ height: 46, marginTop: 10 }} />)}
            </div>
          ) : (
            <div className="pq-card" key={q.id}>
              <div className="pq-card-meta">
                <span className="pq-exam-tag" data-e={q.exam}>{q.label}</span>
              </div>
              <PyqStem q={q} />
              <PyqOptions q={q} chosen={pick} state={pick ? "checked" : "open"} onPick={setPick} />
              {pick && (
                <div className={"pq-verdict " + (pick === q.answer ? "ok" : "bad")} role="status">
                  {pick === q.answer ? <CheckCircle2 size={18} /> : <XCircle size={18} />}
                  <b>{pick === q.answer ? t("right", { l: q.label }) : t("wrong", { a: q.answer, l: q.label })}</b>
                </div>
              )}
              <div className="pqt-try-acts">
                <button className="pq-btn pq-btn-ghost pq-btn-sm" onClick={() => { setPick(null); setK((x) => x + 1); }}>
                  <Shuffle size={14} />{t("another")}
                </button>
                <button className="pq-link" onClick={() => onOpen()}>{t("more")}<ArrowRight size={14} /></button>
              </div>
            </div>
          )}
        </div>
      </div>
    </section>
  );
}

const TEASER_CSS = `
.pqt{position:relative;background:linear-gradient(180deg,var(--cream-100),var(--cream-50));border-top:1px solid var(--line);border-bottom:1px solid var(--line);overflow:hidden}
.pqt::before{content:"";position:absolute;right:-120px;top:-140px;width:460px;height:460px;border-radius:50%;
  background:radial-gradient(circle,rgba(201,162,39,.16),transparent 65%);pointer-events:none}
.pqt-in{position:relative;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:44px;align-items:center;padding-top:72px;padding-bottom:76px}
.pqt-h2{margin-top:10px;font-size:clamp(28px,3.4vw,42px)}
.pqt-h2 em{font-family:var(--font-quote);font-style:italic;font-weight:600;color:var(--brand-600)}
:lang(hi) .pqt-h2 em{font-family:var(--font-deva-display);font-style:normal}
.pqt-stats{display:flex;flex-wrap:wrap;gap:10px;margin:22px 0}
.pqt-subjects{display:flex;flex-direction:column;gap:8px;max-width:460px}
.pqt-subj{display:flex;align-items:center;gap:12px;padding:10px 14px;border-radius:14px;border:1px solid var(--line);background:var(--cream-50);
  font:inherit;color:var(--ink-900);cursor:pointer;text-align:left;transition:border-color .15s ease,transform .15s ease}
.pqt-subj:hover{border-color:var(--gold-500);transform:translateX(3px)}
.pqt-subj > svg{color:var(--brand-600)}
.pqt-subj-emb{width:42px;height:42px;border-radius:12px;display:grid;place-items:center;color:var(--brand-600);background:var(--gold-100);flex:none}
.pqt-subj-t{flex:1;display:flex;flex-direction:column}
.pqt-subj-t b{font-size:15px}
.pqt-subj-t i{font-style:normal;font-size:12.5px;color:var(--ink-400)}
.pqt-ctas{display:flex;flex-wrap:wrap;align-items:center;gap:14px;margin-top:22px}
.pqt-price{display:inline-flex;align-items:center;gap:6px;font-size:14px;font-weight:600;color:var(--ink-600)}
.pqt-try{position:relative}
.pqt-try::before{content:"";position:absolute;inset:18px -10px -14px 18px;border-radius:var(--radius-lg);background:var(--gold-100);transform:rotate(2.2deg);z-index:0}
.pqt-try .pq-card{position:relative;z-index:1;box-shadow:var(--shadow-lift)}
.pqt-try-head{position:relative;z-index:1;display:inline-flex;align-items:center;gap:7px;font-size:12px;font-weight:700;letter-spacing:.14em;
  text-transform:uppercase;color:var(--gold-600);margin-bottom:10px}
.pqt-try-acts{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-top:16px}
@media (max-width:980px){.pqt-in{grid-template-columns:1fr;gap:34px;padding-top:54px;padding-bottom:56px}}
@media (max-width:640px){.pqt-try::before{display:none}.pqt-in{padding-top:44px;padding-bottom:46px}}
`;
