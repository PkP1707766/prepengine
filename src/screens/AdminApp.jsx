import { useState, useEffect, useMemo, useRef, useCallback } from "react";
import { LayoutDashboard, ListChecks, FileText, GraduationCap, FolderOpen, Users, IndianRupee, Plus, Search, Pencil, Trash2, X, Upload, Check, ChevronRight, Menu, AlertCircle, CheckCircle2, Clock, Layers, Eye, EyeOff, Save, ArrowLeft, TrendingUp, Sparkles, Newspaper, Tag, LogOut, Download, Gift, MessageSquare, Star } from "lucide-react";
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts";
import { DiyaLogo } from "../ui/Brand.jsx";
import { ChromeControls } from "../lib/i18n.jsx";

import * as DB from "../lib/db.js";
import { generateTest } from "../lib/generate.js";
import { fmtINR, fmtLongDate, initials, uid } from "../lib/format.js";
import { ErrorState, SkeletonCards } from "../ui/Feedback.jsx";

const AdminApp = (() => {
/* ============================================================
   HELPERS + PERSISTENCE (browser storage; falls back to memory)
   ============================================================ */
/* Everything the admin creates is written straight to Postgres through
   src/lib/db.js. The previous build called `window.storage` — a browser API
   that does not exist — so every course, batch, test and material an admin
   created was thrown away the moment the tab closed. */

const TYPE_LABEL = {
  mcq: "Single Correct", multiple: "Multiple Correct", numerical: "Numerical",
  statement_based: "Statement-based", match_the_following: "Match the Following",
  assertion_reason: "Assertion–Reason", reasoning_aptitude: "Reasoning / Aptitude",
};
const TYPE_COLOR = {
  mcq: { bg: "#f2e9d4", fg: "#a07c2a" }, multiple: { bg: "#f6ecd2", fg: "#7a1f1f" }, numerical: { bg: "#f4ecd6", fg: "#1a6b3c" },
  statement_based: { bg: "#e9eff6", fg: "#3a5a7a" }, match_the_following: { bg: "#eeeee4", fg: "#5a5a34" },
  assertion_reason: { bg: "#f2e9f2", fg: "#6a3a6a" }, reasoning_aptitude: { bg: "#e7f2ec", fg: "#2a6a52" },
};
// The four BPSC formats all score as a single correct option — only their stem
// shape (question_data) and rendering differ.
const SINGLE_CORRECT = (ty) => ty !== "multiple" && ty !== "numerical";
const DIFF_COLOR = { easy: { bg: "#e8f6ee", fg: "#1f8a4c" }, medium: { bg: "#fcf3df", fg: "#d4a64a" }, hard: { bg: "#fbeaea", fg: "#c0392b" } };
// Matches the PYQ-derived distribution_config exactly (subject_weights /
// sub_topic_weights keys) — see pyq-analysis/ANALYSIS_NOTES.md. Sub-topics are
// nested under their subject (QuestionForm's Topic field), not top-level, so
// era splits like Ancient/Medieval/Modern live inside History, not beside it.
const SUBJECTS = ["History", "Geography", "Polity", "Economy", "Science & Technology", "Environment & Ecology", "Current Affairs", "Bihar-Specific", "Reasoning & Aptitude"];
const SUBTOPICS_BY_SUBJECT = {
  "History": ["Ancient", "Medieval", "Modern"],
  "Geography": ["Physical", "World", "Economic", "Human"],
  "Polity": ["Constitutional provisions", "Panchayati Raj & local governance"],
  "Economy": ["Macroeconomic concepts", "Five-year plans & policy", "Banking & finance"],
  "Science & Technology": ["Physics", "Chemistry", "Biology", "Tech & Innovation"],
  "Environment & Ecology": ["Biodiversity", "Climate & Pollution", "Conservation & Policy"],
  "Current Affairs": ["International", "National", "Sports", "Schemes & Indices", "Awards & Appointments"],
  "Bihar-Specific": ["History & Culture", "Geography", "Economy", "Polity & Governance", "Recent Developments"],
  "Reasoning & Aptitude": ["Quantitative/Numerical", "Logical/Verbal"],
};

/* ============================================================
   STARTER CONTENT — never written automatically.
   An admin loads it deliberately from the empty-state button, so a live
   database is never silently seeded with demo questions.
   ============================================================ */
const SEED = {
  questions: [
    { id: uid(), subject: "Polity", topic: "Constitutional provisions", type: "mcq", difficulty: "medium",
      body: "Which Article of the Indian Constitution is described by Dr. B. R. Ambedkar as the 'heart and soul' of the Constitution?",
      options: [{ id: uid(), body: "Article 14", isCorrect: false }, { id: uid(), body: "Article 19", isCorrect: false }, { id: uid(), body: "Article 32", isCorrect: true }, { id: uid(), body: "Article 21", isCorrect: false }],
      numericAnswer: null, numericTolerance: 0.01, marksCorrect: 2, marksWrong: 0.66,
      explanation: "Article 32 (Right to Constitutional Remedies) lets citizens move the Supreme Court directly to enforce Fundamental Rights." },
    { id: uid(), subject: "History", topic: "Modern", type: "mcq", difficulty: "easy",
      body: "The Non-Cooperation Movement was formally launched by Mahatma Gandhi in which year?",
      options: [{ id: uid(), body: "1919", isCorrect: false }, { id: uid(), body: "1920", isCorrect: true }, { id: uid(), body: "1922", isCorrect: false }, { id: uid(), body: "1930", isCorrect: false }],
      numericAnswer: null, numericTolerance: 0.01, marksCorrect: 2, marksWrong: 0.66,
      explanation: "Launched in 1920 (Nagpur session) and withdrawn in February 1922 after Chauri Chaura." },
    { id: uid(), subject: "Geography", topic: "Physical", type: "mcq", difficulty: "medium",
      body: "Which is the longest river of Peninsular India?",
      options: [{ id: uid(), body: "Krishna", isCorrect: false }, { id: uid(), body: "Godavari", isCorrect: true }, { id: uid(), body: "Cauvery", isCorrect: false }, { id: uid(), body: "Narmada", isCorrect: false }],
      numericAnswer: null, numericTolerance: 0.01, marksCorrect: 2, marksWrong: 0.66,
      explanation: "The Godavari (~1465 km) is the longest peninsular river, called 'Dakshina Ganga'." },
    { id: uid(), subject: "Economy", topic: "Macroeconomic concepts", type: "multiple", difficulty: "medium",
      body: "Which of the following are DIRECT taxes? (Select all that apply)",
      options: [{ id: uid(), body: "Income Tax", isCorrect: true }, { id: uid(), body: "GST", isCorrect: false }, { id: uid(), body: "Corporate Tax", isCorrect: true }, { id: uid(), body: "Customs Duty", isCorrect: false }],
      numericAnswer: null, numericTolerance: 0.01, marksCorrect: 2, marksWrong: 0.66,
      explanation: "Income Tax and Corporate Tax are direct taxes; GST and Customs are indirect." },
    { id: uid(), subject: "Environment & Ecology", topic: "Conservation & Policy", type: "mcq", difficulty: "easy",
      body: "In which year was 'Project Tiger' launched in India?",
      options: [{ id: uid(), body: "1972", isCorrect: false }, { id: uid(), body: "1973", isCorrect: true }, { id: uid(), body: "1985", isCorrect: false }, { id: uid(), body: "1991", isCorrect: false }],
      numericAnswer: null, numericTolerance: 0.01, marksCorrect: 2, marksWrong: 0.66,
      explanation: "Project Tiger was launched in 1973 from Jim Corbett National Park." },
    { id: uid(), subject: "Reasoning & Aptitude", topic: "Quantitative/Numerical", type: "mcq", difficulty: "medium",
      body: "What is the unit (last) digit of 7^105?",
      options: [{ id: uid(), body: "1", isCorrect: false }, { id: uid(), body: "3", isCorrect: false }, { id: uid(), body: "7", isCorrect: true }, { id: uid(), body: "9", isCorrect: false }],
      numericAnswer: null, numericTolerance: 0.01, marksCorrect: 2.5, marksWrong: 0.83,
      explanation: "Unit digit of 7 cycles 7,9,3,1 (period 4). 105 mod 4 = 1 → 7." },
    { id: uid(), subject: "Reasoning & Aptitude", topic: "Quantitative/Numerical", type: "numerical", difficulty: "medium",
      body: "A train 150 m long crosses a pole in 15 seconds. What is its speed in km/h?",
      options: [], numericAnswer: 36, numericTolerance: 0.01, marksCorrect: 2.5, marksWrong: 0,
      explanation: "150/15 = 10 m/s = 10 × 18/5 = 36 km/h." },
    { id: uid(), subject: "Reasoning & Aptitude", topic: "Logical/Verbal", type: "mcq", difficulty: "hard",
      body: "Passage: 'Economic growth without equitable distribution deepens social fault lines...' What does it most strongly imply?",
      options: [{ id: uid(), body: "GDP growth should be every nation's primary goal", isCorrect: false }, { id: uid(), body: "Development should be judged by how widely benefits are shared", isCorrect: true }, { id: uid(), body: "The poor cause slow growth", isCorrect: false }, { id: uid(), body: "Social fault lines are unrelated to economics", isCorrect: false }],
      numericAnswer: null, numericTolerance: 0.01, marksCorrect: 2.5, marksWrong: 0.83,
      explanation: "The inference is that real development is about distribution, not aggregate output alone." },
  ],
};


/* ============================================================
   STYLES
   ============================================================ */
const CSS = `
:root{
  --navy:#b8923a; --navy-2:#5b1414; --navy-3:#5e4610; --gold:#dca84a; --gold-2:#d4a64a;
  --bg:#fdf6e3; --card:#ffffff; --ink:#2a1810; --muted:#7a6450; --line:#e8dcc0;
  --green:#1f8a4c; --amber:#d4a64a; --red:#c0392b; --blue:#c39d44;
  --grn-bg:#e8f6ee; --amb-bg:#fcf3df; --red-bg:#fbeaea;
  --hair:#fdf6e3;
}

/* ---- DARK THEME ----------------------------------------------------------
   The toggle already set data-theme on <html>; there was simply nothing here
   listening for it. Only surface tokens are redefined — the semantic accents
   (green / amber / red) keep their meaning in both themes, just on darker
   tinted backgrounds so they stay legible.                                  */
[data-theme="dark"]{
  --bg:#221109; --card:#2e1a10; --ink:#f6e9d2; --muted:#a89272; --line:#3f2718;
  --hair:#2a160c;
  --navy:#e0b45f; --navy-2:#c9603f; --gold:#e8c375; --gold-2:#dcb45f;
  --green:#5cc98a; --amber:#e8c375; --red:#f08a7a; --blue:#d9b877; --purple:#e07a52;
  --grn-bg:#12301f; --amb-bg:#33260d; --red-bg:#3a1614;
}
[data-theme="dark"] .sd-root,
[data-theme="dark"] .ad-root,
[data-theme="dark"] .ee-root{ color-scheme:dark; }
[data-theme="dark"] .sd-root input,
[data-theme="dark"] .sd-root select,
[data-theme="dark"] .sd-root textarea,
[data-theme="dark"] .ad-root input,
[data-theme="dark"] .ad-root select,
[data-theme="dark"] .ad-root textarea,
[data-theme="dark"] .ee-root input{
  background:var(--card); color:var(--ink); border-color:var(--line);
}
[data-theme="dark"] .sd-root .card,
[data-theme="dark"] .ad-root .panel,
[data-theme="dark"] .ee-root .panel{ box-shadow:0 6px 22px rgba(0,0,0,.34); }
[data-theme="dark"] .modal,
[data-theme="dark"] .notif{ background:var(--card); border-color:var(--line); }
[data-theme="dark"] .overlay,
[data-theme="dark"] .scrim{ background:rgba(0,0,0,.62); }
[data-theme="dark"] .tbl thead th{ background:var(--hair); color:var(--muted); }
[data-theme="dark"] .tbl tbody tr:hover{ background:var(--hair); }
*{box-sizing:border-box}
.ad-root{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--ink);
  font-variant-numeric:tabular-nums;line-height:1.5;background:var(--bg);min-height:100vh;display:flex}
.ad-root :where(button){font-family:inherit;cursor:pointer;border:none;background:none}
.ad-root input,.ad-root textarea,.ad-root select{font-family:inherit}

/* SIDEBAR */
.sb{width:248px;background:linear-gradient(180deg,#7c5e16,#5e4610);color:#ecdcb6;flex:0 0 auto;display:flex;flex-direction:column;position:sticky;top:0;height:100vh;z-index:40}
.sb-brand{padding:20px 20px 16px;border-bottom:1px solid rgba(255,255,255,.08)}
.sb-logo{display:flex;align-items:center;gap:11px}
.sb-logo-mark{width:36px;height:36px;border-radius:9px;background:linear-gradient(135deg,var(--gold) 0%,var(--gold-2) 100%);display:grid;place-items:center;color:#ffffff;font-weight:800;font-size:16px;flex:0 0 auto}
.sb-name{font-weight:800;font-size:15px;color:#ffffff;line-height:1.15}
.sb-tag{font-size:11px;color:#e8d8b0}
.sb-nav{flex:1;padding:12px 12px;overflow-y:auto}
.sb-group{font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:#b0a282;font-weight:700;margin:16px 10px 8px}
.sb-item{display:flex;align-items:center;gap:11px;padding:10px 12px;border-radius:9px;font-size:14px;font-weight:600;color:#d8cba6;width:100%;text-align:left;transition:.13s;margin-bottom:2px;position:relative}
.sb-item:hover{background:rgba(255,255,255,.06);color:#ffffff}
.sb-item.active{background:rgba(255,255,255,.1);color:#ffffff}
.sb-item.active::before{content:"";position:absolute;left:0;top:8px;bottom:8px;width:3px;border-radius:3px;background:var(--gold)}
.sb-badge{margin-left:auto;background:rgba(255,255,255,.14);font-size:11px;font-weight:700;padding:1px 8px;border-radius:20px}
.sb-foot{padding:14px 16px;border-top:1px solid rgba(255,255,255,.08);font-size:11.5px;color:#e8d8b0}

/* MAIN */
.main{flex:1;min-width:0;display:flex;flex-direction:column}
.topbar{background:#ffffff;border-bottom:1px solid var(--line);padding:14px 26px;display:flex;align-items:center;justify-content:space-between;gap:14px;position:sticky;top:0;z-index:30}
.topbar h1{margin:0;font-size:19px;font-weight:800;letter-spacing:-.01em}
.topbar .sub{font-size:12.5px;color:var(--muted);margin-top:1px}
.tb-right{display:flex;align-items:center;gap:12px}
.tb-admin{display:flex;align-items:center;gap:10px}
.tb-av{width:36px;height:36px;border-radius:9px;background:var(--navy);color:#ffffff;display:grid;place-items:center;font-weight:800;font-size:13px}
.tb-admin-name{font-size:13.5px;font-weight:700;line-height:1.1}
.tb-admin-role{font-size:11px;color:var(--muted)}
.hamburger{display:none;width:38px;height:38px;border-radius:9px;border:1px solid var(--line);align-items:center;justify-content:center}
.content{padding:26px;max-width:1240px;width:100%;margin:0 auto}

/* BUTTONS */
.btn{display:inline-flex;align-items:center;gap:7px;font-size:13.5px;font-weight:700;padding:10px 16px;border-radius:9px;transition:.14s;border:1.5px solid transparent;white-space:nowrap}
.btn-primary{background:linear-gradient(135deg,#8a2222,#6b1a1a);color:#ffffff;box-shadow:0 5px 16px rgba(20,150,180,.38)}
.btn-primary:hover{background:linear-gradient(135deg,#c8a24a,#a8842f);box-shadow:0 8px 22px rgba(20,150,180,.48)}
.btn-gold{background:var(--gold-2);color:#ffffff}
.btn-gold:hover{filter:brightness(.94)}
.btn-ghost{background:#ffffff;border-color:#e6d6b2;color:#5c4636}
.btn-ghost:hover{border-color:#d8c79c;background:#fdf6e3}
.btn-danger{background:var(--red);color:#ffffff}
.btn-danger:hover{filter:brightness(.94)}
.btn-sm{padding:7px 12px;font-size:12.5px}
.btn-icon{width:34px;height:34px;padding:0;justify-content:center;border-radius:8px;border:1.5px solid var(--line);background:#ffffff;color:#7a6450}
.btn-icon:hover{border-color:#d8c79c;color:var(--navy);background:#fdf6e3}
.btn-icon.danger:hover{border-color:#e8b4b4;color:var(--red);background:var(--red-bg)}

/* CARDS / SECTIONS */
.panel{background:var(--card);border:1px solid var(--line);border-radius:14px;box-shadow:0 1px 3px rgba(20,120,140,.05)}
.panel-pad{padding:22px}
.row-item{display:flex;align-items:center;gap:12px;padding:12px 2px;border-bottom:1px solid var(--line)}
.row-item:last-child{border-bottom:none}
.gen-stats{display:flex;gap:14px;margin-bottom:16px;flex-wrap:wrap}
.gen-stat{flex:1;min-width:120px;border:1px solid var(--line);border-radius:11px;padding:12px 14px}
.gen-stat span{display:block;font-size:20px;font-weight:800;color:var(--ink)}
.gen-stat span.ok{color:var(--green)}
.gen-stat span.warn{color:var(--red)}
.gen-stat label{font-size:12px;color:var(--muted);font-weight:600}
.gen-row{display:flex;gap:10px;align-items:flex-start;margin:10px 0}
.gen-row-label{flex:0 0 140px;font-size:12.5px;font-weight:700;color:var(--muted);padding-top:4px}
.gen-chips{display:flex;flex-wrap:wrap;gap:6px}
.gen-gaps{display:flex;flex-direction:column;gap:6px}
.gen-gap{font-size:12.5px;color:var(--red);background:var(--red-bg);border-radius:7px;padding:6px 10px}
.sec-head{display:flex;align-items:center;justify-content:space-between;gap:14px;margin-bottom:18px;flex-wrap:wrap}
.sec-head h2{margin:0;font-size:16px;font-weight:800}
.sec-head .note{font-size:12.5px;color:var(--muted);margin-top:2px}

/* STAT CARDS */
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(168px,1fr));gap:16px;margin-bottom:22px}
.stat{background:#ffffff;border:1px solid var(--line);border-radius:13px;padding:18px;box-shadow:0 1px 3px rgba(20,120,140,.05)}
.stat-ic{width:40px;height:40px;border-radius:10px;display:grid;place-items:center;margin-bottom:13px}
.stat-n{font-size:27px;font-weight:800;line-height:1;letter-spacing:-.02em}
.stat-l{font-size:12.5px;color:var(--muted);margin-top:6px;font-weight:600}
.stat-sub{font-size:11.5px;color:#aa9a7a;margin-top:3px}

/* TWO-COL */
.cols{display:grid;grid-template-columns:1fr 1fr;gap:18px}
@media(max-width:900px){.cols{grid-template-columns:1fr}}

/* TOOLBAR (filters) */
.toolbar{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:18px}
.search{flex:1;min-width:200px;display:flex;align-items:center;gap:9px;background:#ffffff;border:1.5px solid var(--line);border-radius:9px;padding:9px 13px}
.search input{border:none;outline:none;flex:1;font-size:14px;background:transparent;color:var(--ink)}
.search svg{color:#bcae94;flex:0 0 auto}
.sel{background:#ffffff;border:1.5px solid var(--line);border-radius:9px;padding:9px 12px;font-size:13.5px;color:#5c4636;outline:none;cursor:pointer}
.sel:focus{border-color:var(--navy)}

/* TABLE */
.tbl-wrap{overflow-x:auto;border:1px solid var(--line);border-radius:13px;background:#ffffff}
table.tbl{width:100%;border-collapse:collapse;min-width:640px}
.tbl thead th{text-align:left;font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);font-weight:700;padding:13px 16px;border-bottom:1px solid var(--line);background:#fffaef;white-space:nowrap}
.tbl tbody td{padding:14px 16px;border-bottom:1px solid #fdf6e3;font-size:13.5px;vertical-align:middle}
.tbl tbody tr:last-child td{border-bottom:none}
.tbl tbody tr:hover{background:#fbf5e7}
.q-cell{max-width:440px}
.q-body{font-weight:600;color:#2e1c12;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.q-sub{font-size:11.5px;color:var(--muted);margin-top:4px}
.row-actions{display:flex;gap:8px;justify-content:flex-end}

/* BADGES */
.badge{display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:700;padding:3px 9px;border-radius:20px;white-space:nowrap}
.badge-topic{background:#f6ecd2;color:#7a1f1f}
.marks{font-weight:800;font-size:13px}
.marks .pos{color:var(--green)}
.marks .neg{color:var(--red)}
.dot-pub{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:700}
.dot{width:8px;height:8px;border-radius:50%}

/* EMPTY */
.empty{text-align:center;padding:48px 20px;color:var(--muted)}
.empty-ic{width:56px;height:56px;border-radius:14px;background:#fdf6e3;display:grid;place-items:center;margin:0 auto 14px;color:#bcae94}
.empty h3{margin:0 0 5px;font-size:16px;color:var(--ink);font-weight:700}
.empty p{margin:0 0 16px;font-size:13.5px}

/* MODAL */
.overlay{position:fixed;inset:0;background:rgba(13,27,42,.55);display:flex;align-items:flex-start;justify-content:center;z-index:60;padding:30px 18px;overflow-y:auto;backdrop-filter:blur(2px)}
.modal{background:#ffffff;border-radius:16px;width:100%;max-width:600px;box-shadow:0 24px 60px rgba(0,0,0,.3);margin:auto}
.modal.wide{max-width:820px}
.modal-head{display:flex;align-items:center;justify-content:space-between;padding:20px 24px;border-bottom:1px solid var(--line);position:sticky;top:0;background:#ffffff;border-radius:16px 16px 0 0;z-index:2}
.modal-head h3{margin:0;font-size:17px;font-weight:800}
.modal-head .x{width:34px;height:34px;border-radius:8px;display:grid;place-items:center;color:#9c8c70}
.modal-head .x:hover{background:#f7efdd;color:var(--ink)}
.modal-body{padding:22px 24px}
.modal-foot{padding:16px 24px;display:flex;gap:11px;justify-content:flex-end;border-top:1px solid var(--line);background:#fffaef;border-radius:0 0 16px 16px;position:sticky;bottom:0}

/* FORM */
.field{margin-bottom:16px}
.field-row{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:560px){.field-row{grid-template-columns:1fr}}
.field label{display:block;font-size:12.5px;font-weight:700;color:#4a3322;margin-bottom:6px}
.field .req{color:var(--red)}
/* font-family must be stated: a <textarea> otherwise keeps the browser's
   monospace default, which the question body, the explanation and the new
   Hindi fields all render in — Devanagari especially badly. */
.inp{width:100%;padding:11px 13px;border:1.5px solid #e6d6b2;border-radius:9px;font-size:14px;
  color:var(--ink);outline:none;transition:.13s;background:var(--card,#ffffff);
  font-family:inherit;line-height:1.55}
.inp::placeholder{color:var(--muted);opacity:1}
textarea.inp{resize:vertical;min-height:80px}
.inp:focus{border-color:var(--navy);box-shadow:0 0 0 3px rgba(20,150,180,.1)}
textarea.inp{resize:vertical;min-height:74px;line-height:1.55}
.hint{font-size:11.5px;color:var(--muted);margin-top:5px}
.seg{display:flex;gap:8px;flex-wrap:wrap}
.seg button{flex:1;min-width:90px;padding:10px;border:1.5px solid #e6d6b2;border-radius:9px;font-size:13px;font-weight:700;color:#7a6450;background:#ffffff;transition:.13s}
.seg button.on{border-color:var(--navy);background:#faf2dc;color:var(--navy)}
.opt-edit-hi{margin-top:6px;margin-left:38px}
.opt-hi-tag{flex:0 0 auto;font-size:10.5px;font-weight:800;letter-spacing:.06em;color:var(--muted);
  background:var(--bg2,#faf5e9);border:1px solid var(--line);border-radius:6px;padding:4px 7px}
.opt-edit{display:flex;align-items:center;gap:10px;margin-bottom:9px}
.opt-edit .pick{width:36px;height:36px;border-radius:8px;border:1.5px solid #e6d6b2;display:grid;place-items:center;flex:0 0 auto;color:#ffffff;background:#ffffff;transition:.13s}
.opt-edit .pick.on{background:var(--green);border-color:var(--green)}
.opt-edit .inp{flex:1}
.opt-edit .rm{width:34px;height:34px;border-radius:8px;display:grid;place-items:center;color:#bdae8e;flex:0 0 auto}
.opt-edit .rm:hover{color:var(--red);background:var(--red-bg)}
.opt-edit .stmt-num{width:26px;height:26px;border-radius:7px;display:grid;place-items:center;flex:0 0 auto;font-size:13px;font-weight:800;color:var(--navy);background:#f3ecdb}
.add-opt{font-size:13px;font-weight:700;color:var(--navy);display:inline-flex;align-items:center;gap:6px;padding:7px 0}
.form-err{display:flex;align-items:center;gap:8px;background:var(--red-bg);border:1px solid #f1cccc;color:#a32f24;font-size:13px;font-weight:600;padding:11px 14px;border-radius:9px;margin-bottom:16px}

/* TEST BUILDER */
.tb-section{border:1px solid var(--line);border-radius:12px;margin-bottom:14px;overflow:hidden}
.tb-section-head{display:flex;align-items:center;gap:12px;padding:13px 16px;background:#fffaef;border-bottom:1px solid var(--line)}
.tb-section-head .inp{max-width:280px}
.tb-section-body{padding:14px 16px}
.picked-q{display:flex;align-items:center;gap:11px;padding:10px 12px;border:1px solid #fdf6e3;border-radius:9px;margin-bottom:8px;background:#ffffff}
.picked-q .n{width:26px;height:26px;border-radius:7px;background:var(--navy);color:#ffffff;display:grid;place-items:center;font-size:12px;font-weight:800;flex:0 0 auto}
.picked-q .t{flex:1;min-width:0;font-size:13px;color:#4a3322;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.picker-item{display:flex;align-items:flex-start;gap:11px;padding:11px 13px;border:1.5px solid #fdf6e3;border-radius:9px;margin-bottom:8px;cursor:pointer;transition:.12s}
.picker-item:hover{border-color:#d8cba6;background:#fffaef}
.picker-item.on{border-color:var(--navy);background:#faf2dc}
.picker-check{width:22px;height:22px;border-radius:6px;border:2px solid #cfc3a4;display:grid;place-items:center;flex:0 0 auto;margin-top:1px;color:#ffffff}
.picker-item.on .picker-check{background:var(--navy);border-color:var(--navy)}

/* BANNER */
.banner{display:flex;align-items:center;gap:11px;background:#faf2dc;border:1px solid #e6dcc4;color:#b8923a;font-size:13px;padding:12px 16px;border-radius:11px;margin-bottom:20px}
.banner-warn{background:#fbeaea;border-color:#f0c5c5;color:#a83232}
.banner-warn b{color:#8a2222}
.banner.sample{background:var(--amb-bg);border-color:#efdfba;color:#8a6a14}

/* BREAKDOWN LIST */
.bd-row{display:flex;align-items:center;gap:12px;margin-bottom:11px}
.bd-name{font-size:13px;font-weight:600;width:160px;flex:0 0 auto;color:#4a3322;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bd-track{flex:1;height:9px;background:#fdf6e3;border-radius:6px;overflow:hidden}
.bd-fill{height:100%;border-radius:6px;background:var(--navy)}
.bd-val{font-size:12.5px;font-weight:700;color:var(--muted);width:30px;text-align:right;flex:0 0 auto}

/* TOAST */
.toasts{position:fixed;bottom:22px;right:22px;display:flex;flex-direction:column;gap:10px;z-index:90}
.toast{display:flex;align-items:center;gap:10px;background:var(--ink);color:#ffffff;font-size:13.5px;font-weight:600;padding:12px 16px;border-radius:11px;box-shadow:0 10px 30px rgba(0,0,0,.25);animation:slideIn .25s ease}
.toast svg{color:#7fe0a3;flex:0 0 auto}
.chip-pick{display:flex;flex-wrap:wrap;gap:8px}
.chip-opt{display:inline-flex;align-items:center;gap:6px;border:1.5px solid var(--line);border-radius:999px;
  background:var(--card);color:var(--muted);font:inherit;font-size:13px;font-weight:600;
  padding:8px 14px;cursor:pointer;transition:.15s}
.chip-opt:hover{border-color:var(--gold-2)}
.chip-opt.on{background:var(--navy);border-color:var(--navy);color:#fff}
.toast.toast-err{background:#7a1f1f}
.toast.toast-err svg{color:#f9c9c9}
@keyframes slideIn{from{transform:translateX(20px);opacity:0}to{transform:translateX(0);opacity:1}}

/* loading */
.loader{display:grid;place-items:center;min-height:100vh;width:100%;color:var(--muted);font-size:14px}

/* responsive sidebar */
@media(max-width:860px){
  .sb{position:fixed;left:0;top:0;transform:translateX(-100%);transition:transform .22s ease;box-shadow:8px 0 30px rgba(0,0,0,.2)}
  .sb.open{transform:translateX(0)}
  .hamburger{display:flex}
  .content{padding:18px}
  .scrim{position:fixed;inset:0;background:rgba(0,0,0,.4);z-index:39}
}
`;

/* ============================================================
   SMALL COMPONENTS
   ============================================================ */
function Modal({ title, onClose, children, footer, wide }) {
  return (
    <div className="overlay" onClick={onClose}>
      <div className={"modal" + (wide ? " wide" : "")} onClick={(e) => e.stopPropagation()}>
        <div className="modal-head">
          <h3>{title}</h3>
          <button className="x" onClick={onClose}><X size={19} /></button>
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
function Badge({ color, children }) {
  return <span className="badge" style={{ background: color.bg, color: color.fg }}>{children}</span>;
}
function StatCard({ icon, color, n, label, sub }) {
  return (
    <div className="stat">
      <div className="stat-ic" style={{ background: color.bg, color: color.fg }}>{icon}</div>
      <div className="stat-n">{n}</div>
      <div className="stat-l">{label}</div>
      {sub && <div className="stat-sub">{sub}</div>}
    </div>
  );
}
function Empty({ icon, title, text, action }) {
  return (
    <div className="empty">
      <div className="empty-ic">{icon}</div>
      <h3>{title}</h3>
      <p>{text}</p>
      {action}
    </div>
  );
}

/* ============================================================
   QUESTION FORM (add / edit)
   ============================================================ */
/* Trim question_data down to just what the chosen format uses, so a plain MCQ
   never carries a stray statements array and a match question never keeps an
   empty assertion. Parallel *_hi lists are kept only when they hold something. */
function buildCleanData(type, d) {
  const arr = (a) => (Array.isArray(a) ? a.map((x) => String(x ?? "")) : []);
  const nonEmpty = (a) => arr(a).filter((x) => x.trim());
  if (type === "statement_based") {
    const statements = nonEmpty(d.statements);
    const out = { statements };
    if (arr(d.statements_hi).some((x) => x.trim())) out.statements_hi = arr(d.statements_hi).slice(0, statements.length);
    if (String(d.closing || "").trim()) out.closing = d.closing.trim();
    if (String(d.closing_hi || "").trim()) out.closing_hi = d.closing_hi.trim();
    return out;
  }
  if (type === "match_the_following") {
    const list_1 = nonEmpty(d.list_1), list_2 = nonEmpty(d.list_2);
    const out = { list_1, list_2 };
    if (arr(d.list_1_hi).some((x) => x.trim())) out.list_1_hi = arr(d.list_1_hi).slice(0, list_1.length);
    if (arr(d.list_2_hi).some((x) => x.trim())) out.list_2_hi = arr(d.list_2_hi).slice(0, list_2.length);
    return out;
  }
  if (type === "assertion_reason") {
    const out = { assertion: String(d.assertion || "").trim(), reason: String(d.reason || "").trim() };
    if (String(d.assertion_hi || "").trim()) out.assertion_hi = d.assertion_hi.trim();
    if (String(d.reason_hi || "").trim()) out.reason_hi = d.reason_hi.trim();
    return out;
  }
  if (type === "reasoning_aptitude") {
    const out = {};
    if (String(d.series || "").trim()) out.series = d.series.trim();
    if (String(d.series_hi || "").trim()) out.series_hi = d.series_hi.trim();
    return out;
  }
  return {};
}

function QuestionForm({ initial, onSave, onClose }) {
  const blank = {
    id: null, subject: "", topic: "", type: "mcq", difficulty: "medium", body: "",
    options: [{ id: uid(), body: "", isCorrect: true }, { id: uid(), body: "", isCorrect: false }, { id: uid(), body: "", isCorrect: false }, { id: uid(), body: "", isCorrect: false }],
    numericAnswer: "", numericTolerance: 0.01, marksCorrect: 2, marksWrong: 0.66, explanation: "",
    questionData: {}, conceptGroupId: "", sourceType: "", sourceCitation: "", status: "published",
  };
  const [f, setF] = useState(() => initial ? JSON.parse(JSON.stringify(initial)) : blank);
  const [err, setErr] = useState("");
  const set = (k, v) => setF((p) => ({ ...p, [k]: v }));

  const AR_OPTIONS = [
    "Both A and R are true and R is the correct explanation of A",
    "Both A and R are true but R is NOT the correct explanation of A",
    "A is true but R is false",
    "A is false but R is true",
  ];

  const setType = (ty) => {
    setF((p) => {
      let opts = p.options;
      if (SINGLE_CORRECT(ty)) {
        // Keep exactly one correct option for any single-answer format.
        let seen = false;
        opts = p.options.map((o) => {
          if (o.isCorrect && !seen) { seen = true; return o; }
          return { ...o, isCorrect: false };
        });
        if (!seen && opts[0]) opts = opts.map((o, i) => i === 0 ? { ...o, isCorrect: true } : o);
      }
      // Assertion–Reason has a fixed 4-option key — seed it when the options are
      // still blank, so the author only picks which one is right.
      if (ty === "assertion_reason" && opts.every((o) => !o.body.trim())) {
        opts = AR_OPTIONS.map((body, i) => ({ id: uid(), body, isCorrect: i === 0 }));
      }
      return { ...p, type: ty, options: opts };
    });
  };
  const setOpt = (id, body) => set("options", f.options.map((o) => o.id === id ? { ...o, body } : o));
  const setOptHi = (id, v) => set("options", f.options.map((o) => o.id === id ? { ...o, body_hi: v } : o));
  const toggleCorrect = (id) => set("options", f.options.map((o) => {
    if (SINGLE_CORRECT(f.type)) return { ...o, isCorrect: o.id === id };
    return o.id === id ? { ...o, isCorrect: !o.isCorrect } : o;
  }));
  const addOpt = () => set("options", [...f.options, { id: uid(), body: "", isCorrect: false }]);

  // question_data editing: a merge-patch, plus list helpers that keep each
  // English list and its parallel *_hi list aligned when an item is removed.
  const d = f.questionData || {};
  const setData = (patch) => setF((p) => ({ ...p, questionData: { ...(p.questionData || {}), ...patch } }));
  const listOf = (k) => (Array.isArray(d[k]) ? d[k] : []);
  const setListItem = (k, i, v) => { const a = [...listOf(k)]; a[i] = v; setData({ [k]: a }); };
  const addListItem = (k) => setData({ [k]: [...listOf(k), ""] });
  const rmListItem = (k, i) => setData({
    [k]: listOf(k).filter((_, j) => j !== i),
    [k + "_hi"]: listOf(k + "_hi").filter((_, j) => j !== i),
  });

  /* Hindi is optional per question — English is the fallback everywhere — so
     the fields stay out of the way until asked for, and open automatically for
     a question that already has a translation. */
  const [showHi, setShowHi] = useState(() =>
    !!(f.bodyHi || f.explanationHi || (f.options || []).some((o) => o.body_hi)
       || (f.questionData && Object.keys(f.questionData).some((k) => k.endsWith("_hi")))));
  const rmOpt = (id) => { if (f.options.length <= 2) return; set("options", f.options.filter((o) => o.id !== id)); };

  const submit = () => {
    if (!f.body.trim()) return setErr("Question text is required.");

    // Format-specific stem checks.
    if (f.type === "statement_based" && listOf("statements").filter((s) => (s || "").trim()).length < 1)
      return setErr("Add at least one statement.");
    if (f.type === "match_the_following" &&
        (listOf("list_1").filter((s) => (s || "").trim()).length < 2 ||
         listOf("list_2").filter((s) => (s || "").trim()).length < 2))
      return setErr("Match the Following needs at least two items in each list.");
    if (f.type === "assertion_reason" && (!(d.assertion || "").trim() || !(d.reason || "").trim()))
      return setErr("Both the Assertion and the Reason are required.");

    if (f.type === "numerical") {
      if (f.numericAnswer === "" || isNaN(parseFloat(f.numericAnswer))) return setErr("Enter a valid numerical answer.");
    } else {
      const filled = f.options.filter((o) => o.body.trim());
      if (filled.length < 2) return setErr("Add at least 2 options with text.");
      const correct = f.options.filter((o) => o.isCorrect && o.body.trim());
      if (SINGLE_CORRECT(f.type) && correct.length !== 1) return setErr("Mark exactly one correct option.");
      if (f.type === "multiple" && correct.length < 1) return setErr("Mark at least one correct option.");
    }
    const clean = {
      ...f,
      id: f.id || uid(),
      subject: f.subject.trim() || "General",
      topic: f.topic.trim(),
      conceptGroupId: (f.conceptGroupId || "").trim(),
      sourceCitation: (f.sourceCitation || "").trim(),
      marksCorrect: parseFloat(f.marksCorrect) || 0,
      marksWrong: parseFloat(f.marksWrong) || 0,
      numericAnswer: f.type === "numerical" ? parseFloat(f.numericAnswer) : null,
      numericTolerance: parseFloat(f.numericTolerance) || 0.01,
      options: f.type === "numerical" ? [] : f.options.filter((o) => o.body.trim()),
      questionData: buildCleanData(f.type, d),
      createdAt: f.createdAt || Date.now(),
    };
    onSave(clean);
  };

  return (
    <Modal wide title={initial ? "Edit question" : "Add question"} onClose={onClose}
      footer={<>
        <button className="btn btn-ghost" onClick={onClose}>Cancel</button>
        <button className="btn btn-primary" onClick={submit}><Save size={16} />Save question</button>
      </>}>
      {err && <div className="form-err"><AlertCircle size={17} />{err}</div>}

      <div className="field-row">
        <Field label="Subject" req>
          <input className="inp" list="subjects" value={f.subject} placeholder="e.g. Polity"
            onChange={(e) => set("subject", e.target.value)} />
          <datalist id="subjects">{SUBJECTS.map((s) => <option key={s} value={s} />)}</datalist>
        </Field>
        <Field label="Topic">
          <input className="inp" list="topics-for-subject" value={f.topic} placeholder="e.g. Constitutional provisions"
            onChange={(e) => set("topic", e.target.value)} />
          <datalist id="topics-for-subject">{(SUBTOPICS_BY_SUBJECT[f.subject] || []).map((t) => <option key={t} value={t} />)}</datalist>
        </Field>
      </div>

      <Field label="Question type" req>
        <select className="inp" value={f.type} onChange={(e) => setType(e.target.value)}>
          {Object.keys(TYPE_LABEL).map((ty) => <option key={ty} value={ty}>{TYPE_LABEL[ty]}</option>)}
        </select>
      </Field>

      <div style={{ display: "flex", justifyContent: "flex-end", marginBottom: -6 }}>
        <button className="btn btn-ghost btn-sm" onClick={() => setShowHi((v) => !v)}>
          {showHi ? "Hide Hindi fields" : "+ Add Hindi translation"}
        </button>
      </div>

      <Field label="Question text" req>
        <textarea className="inp" rows={3} value={f.body} placeholder="Type the full question…" onChange={(e) => set("body", e.target.value)} />
        {showHi && (
          <textarea className="inp" rows={3} lang="hi" style={{ marginTop: 8 }} value={f.bodyHi || ""}
                    placeholder="हिन्दी में पूरा प्रश्न लिखिए… (खाली छोड़ने पर अंग्रेज़ी दिखेगी)"
                    onChange={(e) => set("bodyHi", e.target.value)} />
        )}
      </Field>

      {/* Format-specific stem. The options below still hold the answer (the
          combination / mapping / A-R verdict); this is only the material the
          options refer to. */}
      {f.type === "statement_based" && (
        <Field label="Statements" hint="The numbered statements the options refer to (Only 1 and 2, All of the above…).">
          {listOf("statements").map((s, i) => (
            <div key={i}>
              <div className="opt-edit">
                <span className="stmt-num">{i + 1}</span>
                <input className="inp" value={s} placeholder={"Statement " + (i + 1)} onChange={(e) => setListItem("statements", i, e.target.value)} />
                <button className="rm" onClick={() => rmListItem("statements", i)} title="Remove"><Trash2 size={16} /></button>
              </div>
              {showHi && (
                <div className="opt-edit opt-edit-hi">
                  <span className="opt-hi-tag">हिन्दी</span>
                  <input className="inp" lang="hi" value={listOf("statements_hi")[i] || ""} placeholder={"कथन " + (i + 1) + " (वैकल्पिक)"} onChange={(e) => setListItem("statements_hi", i, e.target.value)} />
                </div>
              )}
            </div>
          ))}
          <button className="add-opt" onClick={() => addListItem("statements")}><Plus size={15} />Add statement</button>
        </Field>
      )}

      {f.type === "statement_based" && (
        <Field label="Closing line" hint="Renders AFTER the statements (not before) — the line that turns them into a question.">
          <input className="inp" value={d.closing || ""} placeholder="Which of the statements given above is/are correct?" onChange={(e) => setData({ closing: e.target.value })} />
          {showHi && (
            <input className="inp" lang="hi" style={{ marginTop: 8 }} value={d.closing_hi || ""}
                   placeholder="उपर्युक्त कथनों में से कौन-सा/से सही है/हैं? (वैकल्पिक)"
                   onChange={(e) => setData({ closing_hi: e.target.value })} />
          )}
        </Field>
      )}

      {f.type === "match_the_following" && (
        <div className="field-row">
          {[["list_1", "List I", "e.g. a. Charaka"], ["list_2", "List II", "e.g. 1. Medicine"]].map(([k, label, ph]) => (
            <Field key={k} label={label} hint={ph}>
              {listOf(k).map((s, i) => (
                <div key={i}>
                  <div className="opt-edit">
                    <input className="inp" value={s} placeholder={label + " item " + (i + 1)} onChange={(e) => setListItem(k, i, e.target.value)} />
                    <button className="rm" onClick={() => rmListItem(k, i)} title="Remove"><Trash2 size={16} /></button>
                  </div>
                  {showHi && (
                    <div className="opt-edit opt-edit-hi">
                      <span className="opt-hi-tag">हिन्दी</span>
                      <input className="inp" lang="hi" value={listOf(k + "_hi")[i] || ""} placeholder="(वैकल्पिक)" onChange={(e) => setListItem(k + "_hi", i, e.target.value)} />
                    </div>
                  )}
                </div>
              ))}
              <button className="add-opt" onClick={() => addListItem(k)}><Plus size={15} />Add item</button>
            </Field>
          ))}
        </div>
      )}

      {f.type === "assertion_reason" && (
        <div className="field-row">
          <Field label="Assertion (A)" req>
            <textarea className="inp" rows={2} value={d.assertion || ""} onChange={(e) => setData({ assertion: e.target.value })} />
            {showHi && <textarea className="inp" rows={2} lang="hi" style={{ marginTop: 8 }} value={d.assertion_hi || ""} placeholder="अभिकथन (वैकल्पिक)" onChange={(e) => setData({ assertion_hi: e.target.value })} />}
          </Field>
          <Field label="Reason (R)" req>
            <textarea className="inp" rows={2} value={d.reason || ""} onChange={(e) => setData({ reason: e.target.value })} />
            {showHi && <textarea className="inp" rows={2} lang="hi" style={{ marginTop: 8 }} value={d.reason_hi || ""} placeholder="कारण (वैकल्पिक)" onChange={(e) => setData({ reason_hi: e.target.value })} />}
          </Field>
        </div>
      )}

      {f.type === "reasoning_aptitude" && (
        <Field label="Series / prompt" hint="Optional — a number series or figure prompt, if it is separate from the question text.">
          <input className="inp" value={d.series || ""} placeholder="e.g. 2, 6, 12, 20, ?" onChange={(e) => setData({ series: e.target.value })} />
          {showHi && <input className="inp" lang="hi" style={{ marginTop: 8 }} value={d.series_hi || ""} placeholder="(वैकल्पिक)" onChange={(e) => setData({ series_hi: e.target.value })} />}
        </Field>
      )}

      {f.type === "numerical" ? (
        <div className="field-row">
          <Field label="Correct numerical answer" req><input className="inp" type="number" value={f.numericAnswer} placeholder="e.g. 36" onChange={(e) => set("numericAnswer", e.target.value)} /></Field>
          <Field label="Tolerance (±)" hint="How much deviation counts as correct"><input className="inp" type="number" value={f.numericTolerance} onChange={(e) => set("numericTolerance", e.target.value)} /></Field>
        </div>
      ) : (
        <Field label={SINGLE_CORRECT(f.type) ? "Options (tap the box to mark the correct one)" : "Options (tap boxes to mark all correct ones)"} req>
          {f.options.map((o, i) => (
            <div key={o.id}>
              <div className="opt-edit">
                <button className={"pick" + (o.isCorrect ? " on" : "")} onClick={() => toggleCorrect(o.id)} title="Mark correct">
                  {o.isCorrect && <Check size={16} />}
                </button>
                <input className="inp" value={o.body} placeholder={"Option " + String.fromCharCode(65 + i)} onChange={(e) => setOpt(o.id, e.target.value)} />
                <button className="rm" onClick={() => rmOpt(o.id)} title="Remove"><Trash2 size={16} /></button>
              </div>
              {showHi && (
                <div className="opt-edit opt-edit-hi">
                  <span className="opt-hi-tag">हिन्दी</span>
                  <input className="inp" lang="hi" value={o.body_hi || ""}
                         placeholder={"विकल्प " + String.fromCharCode(65 + i) + " (वैकल्पिक)"}
                         onChange={(e) => setOptHi(o.id, e.target.value)} />
                </div>
              )}
            </div>
          ))}
          <button className="add-opt" onClick={addOpt}><Plus size={15} />Add option</button>
        </Field>
      )}

      <div className="field-row">
        <Field label="Difficulty">
          <div className="seg">
            {["easy", "medium", "hard"].map((d) => (
              <button key={d} className={f.difficulty === d ? "on" : ""} onClick={() => set("difficulty", d)} style={{ textTransform: "capitalize" }}>{d}</button>
            ))}
          </div>
        </Field>
        <div className="field-row">
          <Field label="Marks (correct)"><input className="inp" type="number" value={f.marksCorrect} onChange={(e) => set("marksCorrect", e.target.value)} /></Field>
          <Field label="Negative (wrong)" hint="0 = no negative"><input className="inp" type="number" value={f.marksWrong} onChange={(e) => set("marksWrong", e.target.value)} /></Field>
        </div>
      </div>

      <Field label="Explanation" hint="Shown to students in the deep review after submission">
        <textarea className="inp" rows={3} value={f.explanation} placeholder="Explain why the answer is correct…" onChange={(e) => set("explanation", e.target.value)} />
        {showHi && (
          <textarea className="inp" rows={3} lang="hi" style={{ marginTop: 8 }} value={f.explanationHi || ""}
                    placeholder="हिन्दी में व्याख्या… (वैकल्पिक)"
                    onChange={(e) => set("explanationHi", e.target.value)} />
        )}
      </Field>

      <div className="field-row">
        <Field label="Concept group" hint="A slug shared by questions on the same fact. The generator never repeats a concept in one test — or across a theme (Bihar Special I/II/III).">
          <input className="inp" value={f.conceptGroupId || ""} placeholder="e.g. bihar-first-governor" onChange={(e) => set("conceptGroupId", e.target.value)} />
        </Field>
        <Field label="Source citation" hint="Required for Bihar-specific static facts (Economic Survey, gazette, NCERT…).">
          <input className="inp" value={f.sourceCitation || ""} placeholder="e.g. Bihar Economic Survey 2024–25" onChange={(e) => set("sourceCitation", e.target.value)} />
        </Field>
      </div>
    </Modal>
  );
}

/* ============================================================
   BULK IMPORT
   ============================================================ */
const IMPORT_EXAMPLE = `[
  {
    "subject": "Polity",
    "topic": "Parliament",
    "type": "mcq",
    "difficulty": "medium",
    "body": "Who presides over the Rajya Sabha?",
    "options": ["President", "Vice-President", "Speaker", "PM"],
    "correct": 1,
    "marksCorrect": 2,
    "marksWrong": 0.66,
    "explanation": "The Vice-President is the ex-officio Chairman of the Rajya Sabha."
  },
  {
    "subject": "Reasoning & Aptitude",
    "topic": "Quantitative/Numerical",
    "type": "numerical",
    "body": "12 × 12 = ?",
    "numericAnswer": 144,
    "marksCorrect": 2.5,
    "marksWrong": 0
  }
]`;

function BulkImport({ onImport, onClose }) {
  const [text, setText] = useState("");
  const [err, setErr] = useState("");

  const run = () => {
    let arr;
    try { arr = JSON.parse(text); }
    catch { return setErr("Invalid JSON. Check for missing commas or brackets."); }
    if (!Array.isArray(arr)) return setErr("Top level must be an array [ ... ].");
    const out = [];
    for (let i = 0; i < arr.length; i++) {
      const q = arr[i];
      if (!q.body) return setErr(`Item ${i + 1}: "body" is required.`);
      const type = q.type || "mcq";
      let options = [], numericAnswer = null;
      if (type === "numerical") {
        if (q.numericAnswer === undefined || isNaN(parseFloat(q.numericAnswer))) return setErr(`Item ${i + 1}: numerical needs "numericAnswer".`);
        numericAnswer = parseFloat(q.numericAnswer);
      } else {
        if (!Array.isArray(q.options) || q.options.length < 2) return setErr(`Item ${i + 1}: needs an "options" array of at least 2.`);
        const correctIdx = Array.isArray(q.correct) ? q.correct : [q.correct];
        options = q.options.map((body, idx) => ({ id: uid(), body: String(body), isCorrect: correctIdx.includes(idx) }));
        if (!options.some((o) => o.isCorrect)) return setErr(`Item ${i + 1}: "correct" index doesn't match any option.`);
      }
      out.push({
        id: uid(), subject: q.subject || "General", topic: q.topic || "", type,
        difficulty: q.difficulty || "medium", body: String(q.body), options,
        numericAnswer, numericTolerance: q.numericTolerance || 0.01,
        marksCorrect: q.marksCorrect ?? 2, marksWrong: q.marksWrong ?? 0,
        explanation: q.explanation || "", createdAt: Date.now(),
      });
    }
    onImport(out);
  };

  return (
    <Modal wide title="Bulk import questions" onClose={onClose}
      footer={<>
        <button className="btn btn-ghost" onClick={onClose}>Cancel</button>
        <button className="btn btn-primary" onClick={run}><Upload size={16} />Import</button>
      </>}>
      {err && <div className="form-err"><AlertCircle size={17} />{err}</div>}
      <div className="banner"><AlertCircle size={17} />Paste a JSON array of questions. For multiple-correct, use <code style={{ margin: "0 4px" }}>"correct": [0, 2]</code>. For MCQ use a single index.</div>
      <Field label="Questions JSON">
        <textarea className="inp" rows={9} value={text} placeholder="Paste your JSON array here…" style={{ fontFamily: "ui-monospace,Menlo,monospace", fontSize: 12.5 }} onChange={(e) => setText(e.target.value)} />
      </Field>
      <Field label="Format example">
        <pre style={{ margin: 0, background: "#5b1414", color: "#f1e4c4", padding: 16, borderRadius: 10, fontSize: 12, overflowX: "auto", lineHeight: 1.5 }}>{IMPORT_EXAMPLE}</pre>
      </Field>
    </Modal>
  );
}

/* ============================================================
   QUESTION PICKER (for test builder)
   ============================================================ */
function QuestionPicker({ bank, selectedIds, onConfirm, onClose }) {
  const [sel, setSel] = useState(new Set(selectedIds));
  const [q, setQ] = useState("");
  const [subj, setSubj] = useState("all");
  const subjects = useMemo(() => ["all", ...Array.from(new Set(bank.map((x) => x.subject)))], [bank]);
  const filtered = bank.filter((x) =>
    (subj === "all" || x.subject === subj) &&
    (q === "" || x.body.toLowerCase().includes(q.toLowerCase()) || x.topic.toLowerCase().includes(q.toLowerCase()))
  );
  const toggle = (id) => setSel((s) => { const n = new Set(s); n.has(id) ? n.delete(id) : n.add(id); return n; });

  return (
    <Modal wide title="Add questions to section" onClose={onClose}
      footer={<>
        <span style={{ marginRight: "auto", fontSize: 13, color: "var(--muted)", fontWeight: 600 }}>{sel.size} selected</span>
        <button className="btn btn-ghost" onClick={onClose}>Cancel</button>
        <button className="btn btn-primary" onClick={() => onConfirm(Array.from(sel))}><Check size={16} />Add selected</button>
      </>}>
      <div className="toolbar">
        <div className="search"><Search size={17} /><input value={q} placeholder="Search questions…" onChange={(e) => setQ(e.target.value)} /></div>
        <select className="sel" value={subj} onChange={(e) => setSubj(e.target.value)}>
          {subjects.map((s) => <option key={s} value={s}>{s === "all" ? "All subjects" : s}</option>)}
        </select>
      </div>
      {filtered.length === 0 ? (
        <Empty icon={<ListChecks size={26} />} title="No questions found" text="Adjust your search or add questions to the bank first." />
      ) : filtered.map((x) => (
        <div key={x.id} className={"picker-item" + (sel.has(x.id) ? " on" : "")} onClick={() => toggle(x.id)}>
          <span className="picker-check">{sel.has(x.id) && <Check size={15} />}</span>
          <div style={{ minWidth: 0 }}>
            <div style={{ fontSize: 13.5, fontWeight: 600, color: "var(--ink)" }}>{x.body}</div>
            <div style={{ display: "flex", gap: 7, marginTop: 6, flexWrap: "wrap" }}>
              <Badge color={{ bg: "#fdf6e3", fg: "#7a6450" }}>{x.subject}</Badge>
              <Badge color={TYPE_COLOR[x.type]}>{TYPE_LABEL[x.type]}</Badge>
              <Badge color={DIFF_COLOR[x.difficulty]}>{x.difficulty}</Badge>
            </div>
          </div>
        </div>
      ))}
    </Modal>
  );
}

/* ============================================================
   TEST EDITOR (full view)
   ============================================================ */
function TestEditor({ initial, bank, seriesList = [], onSave, onCancel, toast, saving }) {
  const blank = {
    id: null, title: "", description: "", seriesId: "", durationMin: 20,
    shuffleQuestions: true, shuffleOptions: true, isFree: false, isPublished: false,
    scheduledFor: "", sections: [{ id: uid(), name: "Section 1", questionIds: [] }],
  };
  const [t, setT] = useState(() => initial ? JSON.parse(JSON.stringify(initial)) : blank);
  const [picker, setPicker] = useState(null); // sectionId being edited
  const [err, setErr] = useState("");
  const set = (k, v) => setT((p) => ({ ...p, [k]: v }));

  const addSection = () => set("sections", [...t.sections, { id: uid(), name: "Section " + (t.sections.length + 1), questionIds: [] }]);
  const rmSection = (id) => set("sections", t.sections.filter((s) => s.id !== id));
  const renameSection = (id, name) => set("sections", t.sections.map((s) => s.id === id ? { ...s, name } : s));
  const setSectionQs = (id, ids) => set("sections", t.sections.map((s) => s.id === id ? { ...s, questionIds: ids } : s));
  const rmQ = (sid, qid) => set("sections", t.sections.map((s) => s.id === sid ? { ...s, questionIds: s.questionIds.filter((x) => x !== qid) } : s));

  const totals = useMemo(() => {
    const ids = t.sections.flatMap((s) => s.questionIds);
    const marks = ids.reduce((sum, id) => { const q = bank.find((x) => x.id === id); return sum + (q ? q.marksCorrect : 0); }, 0);
    return { count: ids.length, marks };
  }, [t.sections, bank]);

  const submit = (publish) => {
    if (!t.title.trim()) return setErr("Test title is required.");
    if (totals.count === 0) return setErr("Add at least one question before saving.");
    const duration = parseInt(t.durationMin, 10);
    if (!duration || duration < 1) return setErr("Duration must be at least 1 minute.");
    const empty = t.sections.filter((s) => s.questionIds.length === 0).map((s) => s.name);
    if (empty.length) return setErr(`Remove or fill the empty section${empty.length > 1 ? "s" : ""}: ${empty.join(", ")}.`);
    setErr("");
    onSave({
      ...t,
      id: t.id || uid(),
      title: t.title.trim(),
      durationMin: duration,
      seriesId: t.seriesId || null,
      scheduledFor: t.scheduledFor ? new Date(t.scheduledFor).toISOString() : null,
      isPublished: publish ?? t.isPublished,
    });
  };

  const pickerSection = t.sections.find((s) => s.id === picker);

  return (
    <div>
      <button className="btn btn-ghost btn-sm" onClick={onCancel} style={{ marginBottom: 16 }}><ArrowLeft size={15} />Back to tests</button>

      {err && <div className="form-err"><AlertCircle size={17} />{err}</div>}

      <div className="panel panel-pad" style={{ marginBottom: 18 }}>
        <div className="field-row">
          <Field label="Test title" req><input className="inp" value={t.title} placeholder="e.g. BPSC Full Mock 02" onChange={(e) => set("title", e.target.value)} /></Field>
          <Field label="Test series" hint={seriesList.length === 0 ? "Create a series under Courses & Batches to group tests." : undefined}>
            <select className="inp" value={t.seriesId || ""} onChange={(e) => set("seriesId", e.target.value)}>
              <option value="">Standalone test (no series)</option>
              {seriesList.map((sr) => <option key={sr.id} value={sr.id}>{sr.title}</option>)}
            </select>
          </Field>
        </div>
        <div className="field-row">
          <Field label="Duration (minutes)" req><input className="inp" type="number" min="1" value={t.durationMin} onChange={(e) => set("durationMin", e.target.value)} /></Field>
          <Field label="Opens on" hint="Leave empty to publish immediately. A future date lists it under 'Upcoming'.">
            <input className="inp" type="datetime-local" value={t.scheduledFor ? String(t.scheduledFor).slice(0, 16) : ""}
                   onChange={(e) => set("scheduledFor", e.target.value)} />
          </Field>
        </div>
        <div className="field-row">
          <Field label="Access">
            <div className="seg">
              <button type="button" className={!t.isFree ? "on" : ""} onClick={() => set("isFree", false)}>Paid students only</button>
              <button type="button" className={t.isFree ? "on" : ""} onClick={() => set("isFree", true)}>Free sample</button>
            </div>
          </Field>
          <Field label="Anti-cheating">
            <div className="seg">
              <button className={t.shuffleQuestions ? "on" : ""} onClick={() => set("shuffleQuestions", !t.shuffleQuestions)}>Shuffle questions {t.shuffleQuestions ? "✓" : ""}</button>
              <button className={t.shuffleOptions ? "on" : ""} onClick={() => set("shuffleOptions", !t.shuffleOptions)}>Shuffle options {t.shuffleOptions ? "✓" : ""}</button>
            </div>
          </Field>
        </div>
        <div style={{ display: "flex", gap: 18, fontSize: 13, color: "var(--muted)", fontWeight: 600, marginTop: 4 }}>
          <span><Layers size={14} style={{ verticalAlign: -2, marginRight: 5 }} />{t.sections.length} sections</span>
          <span><ListChecks size={14} style={{ verticalAlign: -2, marginRight: 5 }} />{totals.count} questions</span>
          <span><TrendingUp size={14} style={{ verticalAlign: -2, marginRight: 5 }} />{totals.marks} total marks</span>
        </div>
      </div>

      {t.sections.map((s) => (
        <div className="tb-section" key={s.id}>
          <div className="tb-section-head">
            <input className="inp" value={s.name} onChange={(e) => renameSection(s.id, e.target.value)} />
            <span style={{ fontSize: 12.5, color: "var(--muted)", fontWeight: 600 }}>{s.questionIds.length} Qs</span>
            <button className="btn btn-ghost btn-sm" onClick={() => setPicker(s.id)} style={{ marginLeft: "auto" }}><Plus size={14} />Add questions</button>
            {t.sections.length > 1 && <button className="btn-icon danger" onClick={() => rmSection(s.id)}><Trash2 size={15} /></button>}
          </div>
          <div className="tb-section-body">
            {s.questionIds.length === 0 ? (
              <div style={{ fontSize: 13, color: "var(--muted)", textAlign: "center", padding: "14px 0" }}>No questions yet — click “Add questions”.</div>
            ) : s.questionIds.map((qid, qi) => {
              const q = bank.find((x) => x.id === qid);
              if (!q) return null;
              return (
                <div className="picked-q" key={qid}>
                  <span className="n">{qi + 1}</span>
                  <span className="t">{q.body}</span>
                  <Badge color={TYPE_COLOR[q.type]}>{TYPE_LABEL[q.type]}</Badge>
                  <button className="rm" onClick={() => rmQ(s.id, qid)} style={{ width: 30, height: 30, borderRadius: 7, display: "grid", placeItems: "center", color: "#bdae8e" }}><X size={16} /></button>
                </div>
              );
            })}
          </div>
        </div>
      ))}

      <button className="btn btn-ghost" onClick={addSection} style={{ marginBottom: 22 }}><Plus size={15} />Add section</button>

      <div style={{ display: "flex", gap: 11, justifyContent: "flex-end", flexWrap: "wrap", alignItems: "center" }}>
        <span style={{ marginRight: "auto", fontSize: 12.5, color: "var(--muted)" }}>
          Published tests are visible to every enrolled student immediately.
        </span>
        <button className="btn btn-ghost" onClick={() => submit(false)} disabled={saving}><Save size={16} />Save as draft</button>
        <button className="btn btn-gold" onClick={() => submit(true)} disabled={saving}>
          <Eye size={16} />{saving ? "Saving…" : "Save & publish"}
        </button>
      </div>

      {picker && pickerSection && (
        <QuestionPicker bank={bank} selectedIds={pickerSection.questionIds}
          onConfirm={(ids) => { setSectionQs(picker, ids); setPicker(null); toast("Questions updated"); }}
          onClose={() => setPicker(null)} />
      )}
    </div>
  );
}

/* ============================================================
   COURSE / BATCH / MATERIAL FORMS
   ============================================================ */
function CourseForm({ initial, onSave, onClose }) {
  const [f, setF] = useState(initial || { id: null, title: "", examTarget: "", description: "", isPublished: false });
  const [err, setErr] = useState("");
  const set = (k, v) => setF((p) => ({ ...p, [k]: v }));
  const submit = () => {
    if (!f.title.trim()) return setErr("Course title is required.");
    onSave({ ...f, id: f.id || uid(), title: f.title.trim(), createdAt: f.createdAt || Date.now() });
  };
  return (
    <Modal title={initial ? "Edit course" : "New course"} onClose={onClose}
      footer={<><button className="btn btn-ghost" onClick={onClose}>Cancel</button><button className="btn btn-primary" onClick={submit}><Save size={16} />Save</button></>}>
      {err && <div className="form-err"><AlertCircle size={17} />{err}</div>}
      <Field label="Course title" req><input className="inp" value={f.title} placeholder="e.g. BPSC Prelims 2026 — Foundation" onChange={(e) => set("title", e.target.value)} /></Field>
      <Field label="Exam target"><input className="inp" value={f.examTarget} placeholder="e.g. BPSC Prelims 2026" onChange={(e) => set("examTarget", e.target.value)} /></Field>
      <Field label="Description"><textarea className="inp" rows={3} value={f.description} onChange={(e) => set("description", e.target.value)} /></Field>
      <Field label="Status">
        <div className="seg">
          <button className={!f.isPublished ? "on" : ""} onClick={() => set("isPublished", false)}>Draft</button>
          <button className={f.isPublished ? "on" : ""} onClick={() => set("isPublished", true)}>Published</button>
        </div>
      </Field>
    </Modal>
  );
}
function BatchForm({ initial, courseId, onSave, onClose }) {
  const [f, setF] = useState(initial || { id: null, courseId, name: "", price: 0, seatLimit: "", startDate: "", endDate: "", isActive: true });
  const [err, setErr] = useState("");
  const set = (k, v) => setF((p) => ({ ...p, [k]: v }));
  const submit = () => {
    if (!f.name.trim()) return setErr("Batch name is required.");
    onSave({ ...f, id: f.id || uid(), courseId: f.courseId || courseId, name: f.name.trim(), price: parseFloat(f.price) || 0, seatLimit: f.seatLimit === "" ? null : parseInt(f.seatLimit) });
  };
  return (
    <Modal title={initial ? "Edit batch" : "New batch"} onClose={onClose}
      footer={<><button className="btn btn-ghost" onClick={onClose}>Cancel</button><button className="btn btn-primary" onClick={submit}><Save size={16} />Save</button></>}>
      {err && <div className="form-err"><AlertCircle size={17} />{err}</div>}
      <Field label="Batch name" req><input className="inp" value={f.name} placeholder="e.g. Foundation Batch — Jan 2026" onChange={(e) => set("name", e.target.value)} /></Field>
      <div className="field-row">
        <Field label="Price (₹)" hint="0 = free batch"><input className="inp" type="number" value={f.price} onChange={(e) => set("price", e.target.value)} /></Field>
        <Field label="Seat limit" hint="Blank = unlimited"><input className="inp" type="number" value={f.seatLimit} onChange={(e) => set("seatLimit", e.target.value)} /></Field>
      </div>
      <div className="field-row">
        <Field label="Start date"><input className="inp" type="date" value={f.startDate} onChange={(e) => set("startDate", e.target.value)} /></Field>
        <Field label="End date"><input className="inp" type="date" value={f.endDate} onChange={(e) => set("endDate", e.target.value)} /></Field>
      </div>
      <Field label="Status">
        <div className="seg">
          <button className={f.isActive ? "on" : ""} onClick={() => set("isActive", true)}>Active</button>
          <button className={!f.isActive ? "on" : ""} onClick={() => set("isActive", false)}>Inactive</button>
        </div>
      </Field>
    </Modal>
  );
}
function MaterialForm({ initial, batches, onSave, onClose }) {
  const [f, setF] = useState(initial || {
    id: null, title: "", description: "", subject: "", type: "pdf",
    url: "", isFree: true, isPublished: true, batchId: null,
  });
  const [err, setErr] = useState("");
  const [uploading, setUploading] = useState(false);
  const fileRef = useRef(null);
  const set = (k, v) => setF((p) => ({ ...p, [k]: v }));

  const onFile = async (e) => {
    const file = e.target.files?.[0];
    e.target.value = "";
    if (!file) return;
    setErr(""); setUploading(true);
    try {
      const { url } = await DB.uploadMaterialFile(file);
      setF((p) => ({ ...p, url, title: p.title || file.name.replace(/\.[^.]+$/, "") }));
    } catch (ex) {
      console.error(ex);
      setErr(ex?.message || "Upload failed. Check the file type and size, then try again.");
    }
    setUploading(false);
  };

  const submit = () => {
    if (!f.title.trim()) return setErr("Title is required.");
    if (!f.url?.trim()) return setErr("Upload a file or paste a link — students need something to open.");
    if (!/^https?:\/\//i.test(f.url.trim())) return setErr("The link must start with http:// or https://");
    onSave({ ...f, id: f.id || uid(), title: f.title.trim(), url: f.url.trim(), batchId: f.batchId || null });
  };
  return (
    <Modal title={initial ? "Edit material" : "Add material"} onClose={onClose}
      footer={<><button className="btn btn-ghost" onClick={onClose}>Cancel</button><button className="btn btn-primary" onClick={submit}><Save size={16} />Save</button></>}>
      {err && <div className="form-err"><AlertCircle size={17} />{err}</div>}
      <Field label="File" hint="Upload a PDF, image or video (max 50 MB) — or paste a link below instead.">
        <div style={{ display: "flex", gap: 10, alignItems: "center", flexWrap: "wrap" }}>
          <button type="button" className="btn btn-ghost btn-sm" style={{ width: "auto" }}
                  onClick={() => fileRef.current?.click()} disabled={uploading}>
            <Upload size={15} />{uploading ? "Uploading…" : "Choose file"}
          </button>
          <input ref={fileRef} type="file" style={{ display: "none" }} onChange={onFile}
                 accept=".pdf,.png,.jpg,.jpeg,.webp,.mp4,.webm,.txt,.docx" />
          {f.url && !uploading && (
            <a href={f.url} target="_blank" rel="noreferrer"
               style={{ fontSize: 12.5, color: "var(--navy)", fontWeight: 600, wordBreak: "break-all" }}>
              File attached ↗
            </a>
          )}
        </div>
      </Field>
      <Field label="Title" req><input className="inp" value={f.title} placeholder="e.g. Polity NCERT Quick Notes" onChange={(e) => set("title", e.target.value)} /></Field>
      <div className="field-row">
        <Field label="Type">
          <select className="sel" style={{ width: "100%" }} value={f.type} onChange={(e) => set("type", e.target.value)}>
            <option value="pdf">PDF</option><option value="note">Note</option><option value="video">Video</option><option value="link">Link</option>
          </select>
        </Field>
        <Field label="Access">
          <div className="seg">
            <button className={f.isFree ? "on" : ""} onClick={() => set("isFree", true)}>Free</button>
            <button className={!f.isFree ? "on" : ""} onClick={() => set("isFree", false)}>Paid</button>
          </div>
        </Field>
      </div>
      <Field label="Or paste a link" hint="A YouTube video, Google Drive file or any public URL.">
        <input className="inp" value={f.url} placeholder="https://…" onChange={(e) => set("url", e.target.value)} />
      </Field>
      <div className="field-row">
        <Field label="Subject"><input className="inp" value={f.subject || ""} placeholder="e.g. Polity" onChange={(e) => set("subject", e.target.value)} /></Field>
        <Field label="Visibility">
          <div className="seg">
            <button type="button" className={f.isPublished !== false ? "on" : ""} onClick={() => set("isPublished", true)}>Visible</button>
            <button type="button" className={f.isPublished === false ? "on" : ""} onClick={() => set("isPublished", false)}>Hidden</button>
          </div>
        </Field>
      </div>
      {batches.length > 0 && (
        <Field label="Batch (optional)">
          <select className="sel" style={{ width: "100%" }} value={f.batchId} onChange={(e) => set("batchId", e.target.value)}>
            <option value="">— Public / no batch —</option>
            {batches.map((b) => <option key={b.id} value={b.id}>{b.name}</option>)}
          </select>
        </Field>
      )}
    </Modal>
  );
}

/* ============================================================
   CONFIRM
   ============================================================ */
function Confirm({ message, onYes, onClose }) {
  return (
    <Modal title="Please confirm" onClose={onClose}
      footer={<><button className="btn btn-ghost" onClick={onClose}>Cancel</button><button className="btn btn-danger" onClick={() => { onYes(); onClose(); }}><Trash2 size={16} />Delete</button></>}>
      <p style={{ margin: 0, fontSize: 14.5, color: "var(--ink)" }}>{message}</p>
    </Modal>
  );
}

/* ============================================================
   SERIES, BLUEPRINTS & GENERATION
   ============================================================ */
const PATTERN_LABEL = { sectional: "Sectional", half_length: "Half Length", full_length: "Full Length" };
const JSON_STYLE = { fontFamily: "ui-monospace, SFMono-Regular, Menlo, monospace", fontSize: 12.5 };

// Returns the parsed object, or null when the text is not valid JSON — the
// caller turns null into a form error rather than saving garbage.
function jsonParseOr(text) {
  try { const v = JSON.parse(text || "{}"); return v && typeof v === "object" ? v : null; }
  catch { return null; }
}

function ConfigForm({ initial, onSave, onClose }) {
  const src = initial || { name: "", subjectWeights: {}, difficultyWeights: { easy: 0.3, medium: 0.5, hard: 0.2 }, questionTypeWeights: {}, subTopicWeights: {} };
  const [name, setName] = useState(src.name || "");
  const [subj, setSubj] = useState(JSON.stringify(src.subjectWeights || {}, null, 2));
  const [diff, setDiff] = useState(JSON.stringify(src.difficultyWeights || {}, null, 2));
  const [types, setTypes] = useState(JSON.stringify(src.questionTypeWeights || {}, null, 2));
  const [subtop, setSubtop] = useState(JSON.stringify(src.subTopicWeights || {}, null, 2));
  const [err, setErr] = useState("");

  const submit = () => {
    if (!name.trim()) return setErr("Name is required.");
    const sw = jsonParseOr(subj), dw = jsonParseOr(diff), tw = jsonParseOr(types), stw = jsonParseOr(subtop);
    if (!sw || !dw || !tw || !stw) return setErr("One of the weight maps is not valid JSON.");
    onSave({ id: src.id || undefined, name: name.trim(), subjectWeights: sw, difficultyWeights: dw, questionTypeWeights: tw, subTopicWeights: stw });
  };

  return (
    <Modal wide title={initial ? "Edit distribution config" : "New distribution config"} onClose={onClose}
      footer={<><button className="btn btn-ghost" onClick={onClose}>Cancel</button><button className="btn btn-primary" onClick={submit}><Save size={16} />Save</button></>}>
      {err && <div className="form-err"><AlertCircle size={17} />{err}</div>}
      <Field label="Name" req><input className="inp" value={name} placeholder="e.g. BPSC Prelims — full mix" onChange={(e) => setName(e.target.value)} /></Field>
      <Field label="Subject weights" hint="Keys are your own subject values; weights are normalised, so they need not sum to 1.">
        <textarea className="inp" style={JSON_STYLE} rows={5} value={subj} onChange={(e) => setSubj(e.target.value)} />
      </Field>
      <div className="field-row">
        <Field label="Difficulty weights" hint='e.g. {"easy":0.3,"medium":0.5,"hard":0.2}'>
          <textarea className="inp" style={JSON_STYLE} rows={4} value={diff} onChange={(e) => setDiff(e.target.value)} />
        </Field>
        <Field label="Question-type weights" hint='Per-subject {"Polity":{"statement_based":0.3,…}} or flat {"statement_based":0.3}'>
          <textarea className="inp" style={JSON_STYLE} rows={4} value={types} onChange={(e) => setTypes(e.target.value)} />
        </Field>
      </div>
      <Field label="Sub-topic weights" hint='Sectional papers, per subject: {"History":{"Ancient":0.25,"Medieval":0.35,"Modern":0.4}}'>
        <textarea className="inp" style={JSON_STYLE} rows={4} value={subtop} onChange={(e) => setSubtop(e.target.value)} />
      </Field>
    </Modal>
  );
}

function BlueprintForm({ initial, seriesList, configs, onSave, onClose }) {
  const blank = { id: null, seriesId: "", sequencePosition: 1, title: "", patternType: "full_length", questionCount: 150, subjectScope: {}, distributionConfigId: "", themeGroupId: "", themePartIndex: "" };
  const [b, setB] = useState(() => ({ ...blank, ...(initial || {}) }));
  const [scope, setScope] = useState(JSON.stringify((initial || blank).subjectScope || {}, null, 2));
  const [err, setErr] = useState("");
  const set = (k, v) => setB((p) => ({ ...p, [k]: v }));

  const submit = () => {
    if (!b.title.trim()) return setErr("Title is required.");
    const sc = jsonParseOr(scope);
    if (!sc) return setErr("Subject scope is not valid JSON.");
    onSave({ ...b, id: b.id || undefined, title: b.title.trim(), questionCount: Number(b.questionCount) || 150, sequencePosition: Number(b.sequencePosition) || 1, subjectScope: sc });
  };

  return (
    <Modal wide title={initial ? "Edit blueprint" : "New blueprint"} onClose={onClose}
      footer={<><button className="btn btn-ghost" onClick={onClose}>Cancel</button><button className="btn btn-primary" onClick={submit}><Save size={16} />Save</button></>}>
      {err && <div className="form-err"><AlertCircle size={17} />{err}</div>}
      <div className="field-row">
        <Field label="Title" req><input className="inp" value={b.title} placeholder="e.g. Bihar Special – I" onChange={(e) => set("title", e.target.value)} /></Field>
        <Field label="Series">
          <select className="inp" value={b.seriesId || ""} onChange={(e) => set("seriesId", e.target.value)}>
            <option value="">— none —</option>
            {seriesList.map((s) => <option key={s.id} value={s.id}>{s.title}</option>)}
          </select>
        </Field>
      </div>
      <div className="field-row">
        <Field label="Pattern">
          <select className="inp" value={b.patternType} onChange={(e) => set("patternType", e.target.value)}>
            {Object.keys(PATTERN_LABEL).map((p) => <option key={p} value={p}>{PATTERN_LABEL[p]}</option>)}
          </select>
        </Field>
        <Field label="Question count"><input className="inp" type="number" value={b.questionCount} onChange={(e) => set("questionCount", e.target.value)} /></Field>
        <Field label="Sequence #"><input className="inp" type="number" value={b.sequencePosition} onChange={(e) => set("sequencePosition", e.target.value)} /></Field>
      </div>
      <div className="field-row">
        <Field label="Distribution config">
          <select className="inp" value={b.distributionConfigId || ""} onChange={(e) => set("distributionConfigId", e.target.value)}>
            <option value="">— none —</option>
            {configs.map((c) => <option key={c.id} value={c.id}>{c.name}</option>)}
          </select>
        </Field>
        <Field label="Theme group" hint="Same slug on parts of one theme — dedup spans them.">
          <input className="inp" value={b.themeGroupId || ""} placeholder="e.g. bihar-special" onChange={(e) => set("themeGroupId", e.target.value)} />
        </Field>
        <Field label="Theme part #"><input className="inp" type="number" value={b.themePartIndex} onChange={(e) => set("themePartIndex", e.target.value)} /></Field>
      </div>
      <Field label="Subject scope" hint='Sectional: {"subject":"History","sub_topic_weights":{…}} · Half: {"subject":"Current Affairs","ca_date_range":{"from":"2026-01-01","to":"2026-02-28"}} · Full: {} uses the config'>
        <textarea className="inp" style={JSON_STYLE} rows={5} value={scope} onChange={(e) => setScope(e.target.value)} />
      </Field>
    </Modal>
  );
}

// The count map { key: n } rendered as a row of badges — used for the
// subject / difficulty / type breakdowns of what the generator actually hit.
function CountRow({ label, map }) {
  const entries = Object.entries(map || {}).sort((a, b) => b[1] - a[1]);
  if (entries.length === 0) return null;
  return (
    <div className="gen-row">
      <span className="gen-row-label">{label}</span>
      <div className="gen-chips">{entries.map(([k, n]) => <Badge key={k} color={{ bg: "#f3ecdb", fg: "#7a6450" }}>{k} · {n}</Badge>)}</div>
    </div>
  );
}

function GenReport({ blueprint, result, committing, onCommit, onClose }) {
  const r = result.report;
  const seqOk = r.sequence && r.sequence.ok;
  return (
    <Modal wide title={"Generated: " + blueprint.title} onClose={onClose}
      footer={<>
        <button className="btn btn-ghost" onClick={onClose}>Discard</button>
        <button className="btn btn-primary" onClick={onCommit} disabled={committing || result.questionIds.length === 0}>
          <Save size={16} />{committing ? "Saving…" : "Save as draft test"}
        </button>
      </>}>
      <div className="gen-stats">
        <div className="gen-stat"><span>{r.selected} / {r.target}</span><label>questions</label></div>
        <div className="gen-stat"><span>{r.poolSize}</span><label>eligible pool</label></div>
        <div className="gen-stat"><span className={seqOk ? "ok" : "warn"}>{seqOk ? "clean" : (r.sequence?.residualViolations ?? "—") + " left"}</span><label>sequencing</label></div>
      </div>

      {r.warnings && r.warnings.length > 0 && (
        <div className="form-err"><AlertCircle size={17} />{r.warnings.join(" ")}</div>
      )}

      <CountRow label="By subject" map={r.distribution?.subject} />
      <CountRow label="By difficulty" map={r.distribution?.difficulty} />
      <CountRow label="By type" map={r.distribution?.type} />
      <CountRow label="Answer letter (as authored)" map={r.answerBalance} />

      {r.gaps && r.gaps.length > 0 && (
        <Field label={"Bank gaps (" + r.gaps.length + ")"} hint="Cells the bank could not fill — aim content here.">
          <div className="gen-gaps">
            {r.gaps.map((g, i) => (
              <div key={i} className="gen-gap">{g.subject} · {g.difficulty} · {g.type}{g.subTopic && g.subTopic !== "*" ? " · " + g.subTopic : ""} — short {g.short}</div>
            ))}
          </div>
        </Field>
      )}
      {(!r.gaps || r.gaps.length === 0) && (
        <p style={{ fontSize: 13, color: "var(--muted)", margin: "6px 2px 0" }}>Every target cell was filled from the bank. Saves as an unpublished draft you can review and publish under Tests &amp; Series.</p>
      )}
    </Modal>
  );
}

function Blueprints({ questions, seriesList, toast, askDelete }) {
  const [configs, setConfigs] = useState([]);
  const [blueprints, setBlueprints] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [cfgEditor, setCfgEditor] = useState(null);   // config obj | {} for new
  const [bpEditor, setBpEditor] = useState(null);     // blueprint obj | {} for new
  const [gen, setGen] = useState(null);               // { blueprint, result }
  const [committing, setCommitting] = useState(false);

  const load = useCallback(async () => {
    setError("");
    try {
      const [c, b] = await Promise.all([DB.distributionConfigs.list(), DB.listBlueprints()]);
      setConfigs(c); setBlueprints(b);
    } catch (e) {
      setError(e?.message || "Could not load blueprints. Has migration 0016 been applied?");
    }
    setLoading(false);
  }, []);
  useEffect(() => { load(); }, [load]);

  const saveConfig = async (c) => {
    try { await DB.distributionConfigs.upsert(c); toast("Config saved"); setCfgEditor(null); load(); }
    catch (e) { toast(e?.message || "Save failed", "err"); }
  };
  const saveBlueprint = async (b) => {
    try { await DB.upsertBlueprint(b); toast("Blueprint saved"); setBpEditor(null); load(); }
    catch (e) { toast(e?.message || "Save failed", "err"); }
  };
  const removeBlueprint = (id) => askDelete("Delete this blueprint? Generated tests are not affected.", async () => {
    try { await DB.deleteBlueprint(id); toast("Blueprint deleted"); load(); }
    catch (e) { toast(e?.message || "Delete failed", "err"); }
  });

  const runGenerate = async (bp) => {
    try {
      const cfg = configs.find((c) => c.id === bp.distributionConfigId) || {};
      const [usages, recent] = await Promise.all([DB.questionUsages(), DB.recentTestIds(5)]);
      const result = generateTest({ blueprint: bp, config: cfg, bank: questions, usages, options: { cooldownTestIds: recent } });
      setGen({ blueprint: bp, result });
    } catch (e) {
      toast(e?.message || "Generation failed", "err");
    }
  };

  const commit = async () => {
    if (!gen) return;
    setCommitting(true);
    try {
      const { blueprint: bp, result } = gen;
      const count = result.questionIds.length;
      const test = {
        id: uid(),
        title: bp.title + " — " + new Date().toLocaleDateString(),
        seriesId: bp.seriesId || null,
        durationMin: Math.max(1, Math.round(count * 0.8)),
        sections: result.sections,
        isFree: false, isPublished: false, shuffleQuestions: true, shuffleOptions: true,
      };
      await DB.commitGeneratedTest(test, { blueprintId: bp.id, themeGroupId: bp.themeGroupId || null });
      toast("Draft test created — review it under Tests & Series");
      setGen(null);
    } catch (e) {
      toast(e?.message || "Could not save the test", "err");
    }
    setCommitting(false);
  };

  if (loading) return <SkeletonCards />;

  return (
    <div>
      {error && <div className="form-err" style={{ marginBottom: 16 }}><AlertCircle size={17} />{error}</div>}

      {/* Distribution configs */}
      <div className="panel panel-pad" style={{ marginBottom: 18 }}>
        <div style={{ display: "flex", alignItems: "center", marginBottom: 12 }}>
          <div>
            <h3 style={{ margin: 0, fontSize: 16 }}>Distribution configs</h3>
            <p style={{ margin: "3px 0 0", fontSize: 13, color: "var(--muted)" }}>PYQ-derived target weights the generator matches.</p>
          </div>
          <button className="btn btn-ghost btn-sm" style={{ marginLeft: "auto" }} onClick={() => setCfgEditor({})}><Plus size={14} />New config</button>
        </div>
        {configs.length === 0 ? (
          <Empty icon={<TrendingUp size={24} />} title="No configs yet" text="A config holds the subject / difficulty / question-type weights for a paper." />
        ) : configs.map((c) => (
          <div key={c.id} className="row-item">
            <div style={{ minWidth: 0 }}>
              <div style={{ fontWeight: 700, fontSize: 14 }}>{c.name}</div>
              <div style={{ fontSize: 12.5, color: "var(--muted)", marginTop: 3 }}>{Object.keys(c.subjectWeights || {}).length} subjects · {Object.keys(c.questionTypeWeights || {}).length} type rules</div>
            </div>
            <button className="btn-icon" style={{ marginLeft: "auto" }} onClick={() => setCfgEditor(c)}><Pencil size={15} /></button>
          </div>
        ))}
      </div>

      {/* Blueprints */}
      <div className="panel panel-pad">
        <div style={{ display: "flex", alignItems: "center", marginBottom: 12 }}>
          <div>
            <h3 style={{ margin: 0, fontSize: 16 }}>Blueprints</h3>
            <p style={{ margin: "3px 0 0", fontSize: 13, color: "var(--muted)" }}>Each blueprint is one test in the series. Generate turns it into a draft paper.</p>
          </div>
          <button className="btn btn-primary btn-sm" style={{ marginLeft: "auto", width: "auto" }} onClick={() => setBpEditor({})}><Plus size={14} />New blueprint</button>
        </div>
        {blueprints.length === 0 ? (
          <Empty icon={<Sparkles size={24} />} title="No blueprints yet" text="Define the pattern, question count and scope for each test in your series." />
        ) : blueprints.map((b) => (
          <div key={b.id} className="row-item">
            <div style={{ minWidth: 0 }}>
              <div style={{ fontWeight: 700, fontSize: 14, display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
                <span>{b.sequencePosition}. {b.title}</span>
                <Badge color={{ bg: "#eef3f8", fg: "#3a5a7a" }}>{PATTERN_LABEL[b.patternType] || b.patternType}</Badge>
                {b.themeGroupId && <Badge color={{ bg: "#f2e9f2", fg: "#6a3a6a" }}>{b.themeGroupId}{b.themePartIndex ? " · " + b.themePartIndex : ""}</Badge>}
              </div>
              <div style={{ fontSize: 12.5, color: "var(--muted)", marginTop: 3 }}>{b.questionCount} questions{b.distributionConfigId ? " · " + (configs.find((c) => c.id === b.distributionConfigId)?.name || "config") : " · no config"}</div>
            </div>
            <div style={{ marginLeft: "auto", display: "flex", gap: 6 }}>
              <button className="btn btn-ghost btn-sm" onClick={() => runGenerate(b)}><Sparkles size={14} />Generate</button>
              <button className="btn-icon" onClick={() => setBpEditor(b)}><Pencil size={15} /></button>
              <button className="btn-icon danger" onClick={() => removeBlueprint(b.id)}><Trash2 size={15} /></button>
            </div>
          </div>
        ))}
      </div>

      {cfgEditor && <ConfigForm initial={cfgEditor.id ? cfgEditor : null} onSave={saveConfig} onClose={() => setCfgEditor(null)} />}
      {bpEditor && <BlueprintForm initial={bpEditor.id ? bpEditor : null} seriesList={seriesList} configs={configs} onSave={saveBlueprint} onClose={() => setBpEditor(null)} />}
      {gen && <GenReport blueprint={gen.blueprint} result={gen.result} committing={committing} onCommit={commit} onClose={() => setGen(null)} />}
    </div>
  );
}

/* ============================================================
   APP
   ============================================================ */
const NAV = [
  { group: "Overview", items: [{ id: "overview", label: "Dashboard", icon: LayoutDashboard }] },
  { group: "Content", items: [
    { id: "questions", label: "Question Bank", icon: ListChecks },
    { id: "tests", label: "Tests & Series", icon: FileText },
    { id: "blueprints", label: "Series & Blueprints", icon: Sparkles },
    { id: "bundles", label: "Bundles & Pricing", icon: Layers },
    { id: "exams", label: "Exams & Categories", icon: GraduationCap },
    { id: "coupons", label: "Coupons", icon: Tag },
    { id: "courses", label: "Courses & Batches", icon: GraduationCap },
    { id: "materials", label: "Free Materials", icon: FolderOpen },
    { id: "content", label: "Public Content", icon: Newspaper },
  ]},
  { group: "People & Revenue", items: [
    { id: "students", label: "Students", icon: Users },
    { id: "referrals", label: "Referrals", icon: Gift },
    { id: "feedback", label: "Feedback", icon: MessageSquare },
    { id: "sales", label: "Sales", icon: IndianRupee },
  ]},
];
const PAGE_META = {
  overview: { title: "Dashboard", sub: "Your platform at a glance" },
  questions: { title: "Question Bank", sub: "Create and manage all questions" },
  tests: { title: "Tests & Series", sub: "Build tests from your question bank" },
  blueprints: { title: "Series & Blueprints", sub: "Auto-generate a test series from PYQ-matched blueprints" },
  bundles: { title: "Bundles & Pricing", sub: "What students can buy, and what it costs" },
  referrals: { title: "Referrals", sub: "Who invited whom, and what it converted to" },
  feedback: { title: "Feedback", sub: "What students are telling you — read it" },
  exams: { title: "Exams & Categories", sub: "The exams your bundles and content are filed under" },
  coupons: { title: "Coupons", sub: "Discount codes students apply at checkout" },
  courses: { title: "Courses & Batches", sub: "Organise your offerings and pricing" },
  materials: { title: "Free Materials", sub: "PDFs, notes and videos for students" },
  content: { title: "Public Content", sub: "Syllabus, PYQ, NCERT, current affairs and FAQ" },
  students: { title: "Students", sub: "Enrolled learners and their activity" },
  sales: { title: "Sales", sub: "Revenue and transactions" },
};

function App({ onLogout }) {
  const [view, setView] = useState("overview");
  const [loading, setLoading] = useState(true);
  const [loadError, setLoadError] = useState("");
  const [sbOpen, setSbOpen] = useState(false);
  const [admin, setAdmin] = useState({ name: "Administrator", email: "" });

  const [questions, setQuestions] = useState([]);
  const [courses, setCourses] = useState([]);
  const [batches, setBatches] = useState([]);
  const [tests, setTests] = useState([]);
  const [materials, setMaterials] = useState([]);
  const [seriesList, setSeriesList] = useState([]);

  const [toasts, setToasts] = useState([]);
  const [confirm, setConfirm] = useState(null);

  const toast = useCallback((msg, tone = "ok") => {
    const id = uid();
    setToasts((t) => [...t, { id, msg, tone }]);
    setTimeout(() => setToasts((t) => t.filter((x) => x.id !== id)), 3000);
  }, []);
  const askDelete = (message, onYes) => setConfirm({ message, onYes });

  /* ---- Load everything from the database. No seeding, no local shadow copy. */
  const loadAll = useCallback(async () => {
    setLoadError("");
    try {
      const [q, c, b, t, m, sr] = await Promise.all([
        DB.listQuestions(),
        DB.courses.list(),
        DB.batches.list(),
        DB.listTests(),
        DB.materials.list(),
        DB.series.list(),
      ]);
      setQuestions(q); setCourses(c); setBatches(b);
      setTests(t); setMaterials(m); setSeriesList(sr);
    } catch (e) {
      console.error("admin load failed", e);
      setLoadError(e?.message || "Could not reach the database.");
    }
    setLoading(false);
  }, []);

  useEffect(() => { loadAll(); }, [loadAll]);

  /* Real identity in the topbar — it used to say "Priyadarshee / PK" for
     every administrator, whoever was signed in. */
  useEffect(() => {
    (async () => {
      try {
        const user = await DB.currentUser();
        if (!user) return;
        const p = await DB.getProfile(user.id);
        setAdmin({ name: (p?.full_name || "").trim() || user.email?.split("@")[0] || "Administrator", email: p?.email || user.email || "" });
      } catch { /* topbar falls back to the generic label */ }
    })();
  }, []);

  /* ---- Mutations. Each one writes first, then updates local state from the
     row the database actually returned, so what is on screen is what is
     stored. A failure is surfaced instead of being silently swallowed. ---- */

  const saveQuestion = async (item) => {
    try {
      const isNew = !questions.some((x) => x.id === item.id);
      const saved = await DB.upsertQuestion(item);
      setQuestions((prev) => prev.some((x) => x.id === saved.id)
        ? prev.map((x) => (x.id === saved.id ? saved : x))
        : [saved, ...prev]);
      toast(isNew ? "Question saved" : "Question updated");
      return true;
    } catch (e) {
      console.error(e);
      toast(e?.message || "Couldn't save — check your connection and try again", "err");
      return false;
    }
  };

  const deleteQuestion = async (id) => {
    const usedIn = tests.filter((t) => (t.sections || []).some((sec) => (sec.questionIds || []).includes(id)));
    try {
      await DB.deleteQuestion(id);
      setQuestions((p) => p.filter((x) => x.id !== id));
      toast(usedIn.length
        ? `Question removed. It stays visible in ${usedIn.length} past test${usedIn.length > 1 ? "s" : ""} for students who already attempted it.`
        : "Question deleted");
    } catch (e) {
      console.error(e);
      toast(e?.message || "Couldn't delete — check your connection and try again", "err");
    }
  };

  const importQuestions = async (arr) => {
    try {
      const saved = await DB.insertQuestions(arr);
      setQuestions((prev) => [...saved, ...prev]);
      toast(`${saved.length} question${saved.length === 1 ? "" : "s"} imported`);
    } catch (e) {
      console.error(e);
      toast(e?.message || "Import failed — check the file format and try again", "err");
    }
  };

  /* Opt-in starter pack. Deliberate, one-click, and clearly labelled — never
     something that writes itself into a live database on first load. */
  const loadStarterPack = async () => {
    if (questions.length > 0) return;
    try {
      const saved = await DB.insertQuestions(SEED.questions.map((q) => ({ ...q, id: undefined })));
      setQuestions(saved);
      toast(`${saved.length} starter questions added — edit or delete them freely`);
    } catch (e) {
      console.error(e);
      toast(e?.message || "Couldn't add the starter questions", "err");
    }
  };

  /* Generic persist/remove helpers shared by courses, batches, tests,
     materials and series. */
  const makeSaver = (api, setter, label) => async (item) => {
    try {
      const saved = await api.upsert(item);
      setter((prev) => prev.some((x) => x.id === saved.id)
        ? prev.map((x) => (x.id === saved.id ? saved : x))
        : [saved, ...prev]);
      toast(`${label} saved`);
      return saved;
    } catch (e) {
      console.error(e);
      toast(e?.message || `Couldn't save this ${label.toLowerCase()}`, "err");
      return null;
    }
  };
  const makeRemover = (api, setter, label) => async (id) => {
    try {
      await api.remove(id);
      setter((prev) => prev.filter((x) => x.id !== id));
      toast(`${label} deleted`);
    } catch (e) {
      console.error(e);
      toast(e?.message || `Couldn't delete this ${label.toLowerCase()}`, "err");
    }
  };

  const saveCourse   = makeSaver(DB.courses,   setCourses,   "Course");
  const removeCourse = makeRemover(DB.courses, setCourses,   "Course");
  const saveBatch    = makeSaver(DB.batches,   setBatches,   "Batch");
  const removeBatch  = makeRemover(DB.batches, setBatches,   "Batch");
  const saveMaterial   = makeSaver(DB.materials,   setMaterials, "Material");
  const removeMaterial = makeRemover(DB.materials, setMaterials, "Material");

  const saveTest = async (item) => {
    try {
      const saved = await DB.upsertTest(item);
      setTests((prev) => prev.some((x) => x.id === saved.id)
        ? prev.map((x) => (x.id === saved.id ? saved : x))
        : [saved, ...prev]);
      toast("Test saved");
      return saved;
    } catch (e) {
      console.error(e);
      toast(e?.message || "Couldn't save this test", "err");
      return null;
    }
  };
  const removeTest = async (id) => {
    try {
      await DB.deleteTest(id);
      setTests((prev) => prev.filter((x) => x.id !== id));
      toast("Test deleted");
    } catch (e) {
      console.error(e);
      toast(e?.message || "Couldn't delete this test", "err");
    }
  };

  if (loading) {
    return (
      <div className="ad-root">
        <style>{CSS}</style>
        <div className="loader"><DiyaLogo size={40} ring /> Loading your admin console…</div>
      </div>
    );
  }

  if (loadError) {
    return (
      <div className="ad-root">
        <style>{CSS}</style>
        <div style={{ minHeight: "100vh", display: "grid", placeItems: "center", padding: 24 }}>
          <div style={{ maxWidth: 440, width: "100%" }}>
            <ErrorState message={loadError} onRetry={() => { setLoading(true); loadAll(); }} />
            <button className="btn btn-ghost" style={{ marginTop: 8 }} onClick={onLogout}>
              <LogOut size={16} /> Sign out
            </button>
          </div>
        </div>
      </div>
    );
  }

  const go = (v) => { setView(v); setSbOpen(false); };

  return (
    <div className="ad-root">
      <style>{CSS}</style>

      {/* SIDEBAR */}
      {sbOpen && <div className="scrim" onClick={() => setSbOpen(false)} />}
      <aside className={"sb" + (sbOpen ? " open" : "")}>
        <div className="sb-brand">
          <div className="sb-logo">
            <DiyaLogo size={36} boxed radius={9} />
            <div>
              <div className="sb-name" style={{ fontFamily: "var(--font-display)", letterSpacing: ".02em" }}>JUNOONIAS</div>
              <div className="sb-tag">Admin Console</div>
            </div>
          </div>
        </div>
        <nav className="sb-nav">
          {NAV.map((grp) => (
            <div key={grp.group}>
              <div className="sb-group">{grp.group}</div>
              {grp.items.map((it) => {
                const Icon = it.icon;
                const count = it.id === "questions" ? questions.length : it.id === "tests" ? tests.length : it.id === "courses" ? courses.length : it.id === "materials" ? materials.length : null;
                return (
                  <button key={it.id} className={"sb-item" + (view === it.id ? " active" : "")} onClick={() => go(it.id)}>
                    <Icon size={18} />{it.label}
                    {count != null && count > 0 && <span className="sb-badge">{count}</span>}
                  </button>
                );
              })}
            </div>
          ))}
        </nav>
        <div className="sb-foot">
          Signed in as<br /><b style={{ color: "#f0dfb8" }}>{admin.email || admin.name}</b>
        </div>
      </aside>

      {/* MAIN */}
      <div className="main">
        <header className="topbar">
          <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
            <button className="hamburger" onClick={() => setSbOpen(true)}><Menu size={20} /></button>
            <div>
              <h1>{PAGE_META[view].title}</h1>
              <div className="sub">{PAGE_META[view].sub}</div>
            </div>
          </div>
          <div className="tb-right">
            <ChromeControls />
            <div className="tb-admin">
              <button className="btn-icon" title="Log out" onClick={onLogout} style={{ width: 40, height: 40, marginRight: 4 }}><LogOut size={18} /></button>
              <div className="tb-av">{initials(admin.name)}</div>
              <div>
                <div className="tb-admin-name">{admin.name}</div>
                <div className="tb-admin-role">Administrator</div>
              </div>
            </div>
          </div>
        </header>

        <main className="content">
          {view === "overview" && <Overview {...{ questions, tests, courses, batches, go, loadStarterPack }} />}
          {view === "questions" && <QuestionBank {...{ questions, saveQuestion, deleteQuestion, importQuestions, loadStarterPack, askDelete }} />}
          {view === "tests" && <Tests {...{ tests, saveTest, removeTest, questions, seriesList, toast, askDelete }} />}
          {view === "blueprints" && <Blueprints {...{ questions, seriesList, toast, askDelete }} />}
          {view === "bundles" && <Bundles {...{ tests, toast }} />}
          {view === "courses" && <Courses {...{ courses, saveCourse, removeCourse, batches, saveBatch, removeBatch, askDelete }} />}
          {view === "materials" && <Materials {...{ materials, saveMaterial, removeMaterial, batches, askDelete }} />}
          {view === "exams" && <Exams {...{ toast, askDelete }} />}
          {view === "coupons" && <Coupons {...{ toast, askDelete }} />}
          {view === "content" && <Content {...{ toast, askDelete }} />}
          {view === "students" && <Students toast={toast} />}
          {view === "referrals" && <Referrals />}
          {view === "feedback" && <Feedback toast={toast} />}
          {view === "sales" && <Sales toast={toast} />}
        </main>
      </div>

      {/* TOASTS + CONFIRM */}
      <div className="toasts">
        {toasts.map((t) => (
          <div className={"toast" + (t.tone === "err" ? " toast-err" : "")} key={t.id} role="status">
            {t.tone === "err" ? <AlertCircle size={18} /> : <CheckCircle2 size={18} />}{t.msg}
          </div>
        ))}
      </div>
      {confirm && <Confirm message={confirm.message} onYes={confirm.onYes} onClose={() => setConfirm(null)} />}
    </div>
  );
}

/* ============================================================
   VIEW: OVERVIEW
   ============================================================ */
function Overview({ questions, tests, courses, batches, go, loadStarterPack }) {
  const [live, setLive] = useState(null);
  useEffect(() => {
    (async () => {
      try {
        const [students, payments] = await Promise.all([DB.adminStudents(), DB.adminPayments()]);
        setLive({
          students: students.length,
          enrolled: students.filter((x) => x.enrolled).length,
          revenue: payments.filter((x) => x.status === "paid").reduce((a, b) => a + b.amount, 0),
        });
      } catch (e) { console.error(e); setLive({ students: 0, enrolled: 0, revenue: 0, failed: true }); }
    })();
  }, []);

  const published = tests.filter((t) => t.isPublished).length;
  const bySubject = useMemo(() => {
    const m = {};
    questions.forEach((q) => { m[q.subject] = (m[q.subject] || 0) + 1; });
    return Object.entries(m).sort((a, b) => b[1] - a[1]);
  }, [questions]);
  const maxSub = bySubject.length ? bySubject[0][1] : 1;
  const recent = questions.slice(0, 5);
  const emptyBank = questions.length === 0;

  return (
    <div>
      {emptyBank && (
        <div className="banner banner-warn">
          <AlertCircle size={17} />
          Your question bank is empty. Tests are assembled from it, so start here.
          <span style={{ marginLeft: "auto", display: "flex", gap: 8 }}>
            <button className="btn btn-ghost btn-sm" style={{ width: "auto" }} onClick={loadStarterPack}>
              <Sparkles size={15} />Load 8 starter questions
            </button>
            <button className="btn btn-primary btn-sm" style={{ width: "auto" }} onClick={() => go("questions")}>
              <Plus size={15} />Add my own
            </button>
          </span>
        </div>
      )}

      <div className="stats">
        <StatCard icon={<ListChecks size={20} />} color={{ bg: "#faf2dc", fg: "#b8923a" }} n={questions.length} label="Questions" sub="in your bank" />
        <StatCard icon={<FileText size={20} />} color={{ bg: "#f6ecd2", fg: "#7a1f1f" }} n={tests.length} label="Tests" sub={`${published} published`} />
        <StatCard icon={<GraduationCap size={20} />} color={{ bg: "#f4ecd6", fg: "#1a6b3c" }} n={courses.length} label="Courses" sub={`${batches.length} batches`} />
        <StatCard icon={<Users size={20} />} color={{ bg: "#fcf3df", fg: "#d4a64a" }}
                  n={live ? live.students : "…"} label="Students"
                  sub={live ? live.enrolled + " enrolled" : "loading"} />
        <StatCard icon={<IndianRupee size={20} />} color={{ bg: "#e8f6ee", fg: "#1f8a4c" }}
                  n={live ? fmtINR(live.revenue) : "…"} label="Revenue" sub="verified payments" />
      </div>

      <div className="cols">
        <div className="panel panel-pad">
          <div className="sec-head"><div><h2>Questions by subject</h2><div className="note">Coverage across your bank</div></div></div>
          {bySubject.length === 0 ? <div style={{ fontSize: 13.5, color: "var(--muted)" }}>No questions yet.</div> :
            bySubject.map(([s, n]) => (
              <div className="bd-row" key={s}>
                <span className="bd-name">{s}</span>
                <div className="bd-track"><div className="bd-fill" style={{ width: (n / maxSub) * 100 + "%" }} /></div>
                <span className="bd-val">{n}</span>
              </div>
            ))}
        </div>

        <div className="panel panel-pad">
          <div className="sec-head"><div><h2>Recently added</h2><div className="note">Latest questions in the bank</div></div>
            <button className="btn btn-ghost btn-sm" onClick={() => go("questions")}>View all<ChevronRight size={15} /></button></div>
          {recent.length === 0 ? <div style={{ fontSize: 13.5, color: "var(--muted)" }}>Nothing yet.</div> :
            recent.map((q) => (
              <div key={q.id} style={{ padding: "11px 0", borderBottom: "1px solid var(--line)" }}>
                <div style={{ fontSize: 13.5, fontWeight: 600, color: "var(--ink)", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>{q.body}</div>
                <div style={{ display: "flex", gap: 7, marginTop: 6 }}>
                  <Badge color={{ bg: "#fdf6e3", fg: "#7a6450" }}>{q.subject}</Badge>
                  <Badge color={TYPE_COLOR[q.type]}>{TYPE_LABEL[q.type]}</Badge>
                </div>
              </div>
            ))}
        </div>
      </div>
    </div>
  );
}

/* ============================================================
   VIEW: QUESTION BANK
   ============================================================ */
function QuestionBank({ questions, saveQuestion, deleteQuestion, importQuestions, loadStarterPack, askDelete }) {
  const [q, setQ] = useState("");
  const [subj, setSubj] = useState("all");
  const [type, setType] = useState("all");
  const [editing, setEditing] = useState(null); // question or {} for new
  const [bulk, setBulk] = useState(false);

  const subjects = useMemo(() => ["all", ...Array.from(new Set(questions.map((x) => x.subject)))], [questions]);
  const filtered = questions.filter((x) =>
    (subj === "all" || x.subject === subj) && (type === "all" || x.type === type) &&
    (q === "" || x.body.toLowerCase().includes(q.toLowerCase()) || (x.topic || "").toLowerCase().includes(q.toLowerCase()))
  );

  const save = async (item) => {
    const ok = await saveQuestion(item);
    if (ok) setEditing(null);
  };
  const importQs = (arr) => { importQuestions(arr); setBulk(false); };
  const del = (item) => askDelete(`Delete this question? "${item.body.slice(0, 60)}…" This cannot be undone.`, () => deleteQuestion(item.id));

  return (
    <div>
      <div className="toolbar">
        <div className="search"><Search size={17} /><input value={q} placeholder="Search by question or topic…" onChange={(e) => setQ(e.target.value)} /></div>
        <select className="sel" value={subj} onChange={(e) => setSubj(e.target.value)}>{subjects.map((s) => <option key={s} value={s}>{s === "all" ? "All subjects" : s}</option>)}</select>
        <select className="sel" value={type} onChange={(e) => setType(e.target.value)}>
          <option value="all">All types</option>
          {Object.keys(TYPE_LABEL).map((ty) => <option key={ty} value={ty}>{TYPE_LABEL[ty]}</option>)}
        </select>
        <button className="btn btn-ghost" onClick={() => setBulk(true)}><Upload size={16} />Bulk import</button>
        <button className="btn btn-primary" onClick={() => setEditing({})}><Plus size={16} />Add question</button>
      </div>

      {filtered.length === 0 ? (
        <div className="panel"><Empty icon={<ListChecks size={26} />} title={questions.length === 0 ? "No questions yet" : "No matches"}
          text={questions.length === 0 ? "Add your first question or bulk-import a set." : "Try a different search or filter."}
          action={questions.length === 0 ? (
            <div style={{ display: "flex", gap: 10, justifyContent: "center", flexWrap: "wrap" }}>
              <button className="btn btn-primary" style={{ width: "auto" }} onClick={() => setEditing({})}><Plus size={16} />Add question</button>
              <button className="btn btn-ghost" style={{ width: "auto" }} onClick={() => setBulk(true)}><Upload size={16} />Bulk import</button>
              <button className="btn btn-ghost" style={{ width: "auto" }} onClick={loadStarterPack}><Sparkles size={16} />Load 8 samples</button>
            </div>
          ) : null} />
        </div>
      ) : (
        <div className="tbl-wrap">
          <table className="tbl">
            <thead><tr><th style={{ width: 40 }}>#</th><th>Question</th><th>Subject</th><th>Type</th><th>Level</th><th>Marks</th><th style={{ textAlign: "right" }}>Actions</th></tr></thead>
            <tbody>
              {filtered.map((x, i) => (
                <tr key={x.id}>
                  <td style={{ color: "var(--muted)", fontWeight: 700 }}>{i + 1}</td>
                  <td className="q-cell"><div className="q-body">{x.body}</div>{x.topic && <div className="q-sub">{x.topic}</div>}</td>
                  <td><Badge color={{ bg: "#fdf6e3", fg: "#7a6450" }}>{x.subject}</Badge></td>
                  <td><Badge color={TYPE_COLOR[x.type]}>{TYPE_LABEL[x.type]}</Badge></td>
                  <td><Badge color={DIFF_COLOR[x.difficulty]}>{x.difficulty}</Badge></td>
                  <td><span className="marks"><span className="pos">+{x.marksCorrect}</span>{x.marksWrong > 0 && <span className="neg"> / −{x.marksWrong}</span>}</span></td>
                  <td><div className="row-actions">
                    <button className="btn-icon" onClick={() => setEditing(x)} title="Edit"><Pencil size={15} /></button>
                    <button className="btn-icon danger" onClick={() => del(x)} title="Delete"><Trash2 size={15} /></button>
                  </div></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {editing && <QuestionForm initial={editing.id ? editing : null} onSave={save} onClose={() => setEditing(null)} />}
      {bulk && <BulkImport onImport={importQs} onClose={() => setBulk(false)} />}
    </div>
  );
}

/* ============================================================
   VIEW: TESTS
   ============================================================ */
function Tests({ tests, saveTest, removeTest, questions, seriesList, toast, askDelete }) {
  const [editor, setEditor] = useState(null); // null=list, {}=new, test=edit
  const [busy, setBusy] = useState(null);

  const save = async (t) => {
    setBusy("save");
    const saved = await saveTest(t);
    setBusy(null);
    if (saved) setEditor(null);
  };
  const del = (t) => askDelete(
    `Delete the test "${t.title}"? Students who already attempted it keep their reports, but the test disappears from the catalogue.`,
    () => removeTest(t.id),
  );
  const togglePublish = async (t) => {
    setBusy(t.id);
    await saveTest({ ...t, isPublished: !t.isPublished });
    setBusy(null);
  };

  if (editor !== null) {
    return <TestEditor initial={editor.id ? editor : null} bank={questions} seriesList={seriesList} onSave={save} onCancel={() => setEditor(null)} toast={toast} saving={busy === "save"} />;
  }

  const qCount = (t) => (t.sections || []).reduce((s, sec) => s + (sec.questionIds || []).length, 0);

  return (
    <div>
      <div className="sec-head">
        <div><h2>{tests.length} test{tests.length !== 1 ? "s" : ""}</h2><div className="note">Assemble tests from your question bank</div></div>
        <button className="btn btn-primary" onClick={() => setEditor({})} disabled={questions.length === 0}><Plus size={16} />Create test</button>
      </div>

      {questions.length === 0 && <div className="banner sample"><AlertCircle size={17} />Add some questions first — you’ll need them to build a test.</div>}

      {tests.length === 0 ? (
        <div className="panel"><Empty icon={<FileText size={26} />} title="No tests yet" text="Create your first test and add sections of questions." /></div>
      ) : (
        <div className="tbl-wrap">
          <table className="tbl">
            <thead><tr><th>Test</th><th>Sections</th><th>Questions</th><th>Duration</th><th>Status</th><th style={{ textAlign: "right" }}>Actions</th></tr></thead>
            <tbody>
              {tests.map((t) => (
                <tr key={t.id}>
                  <td><div style={{ fontWeight: 700, color: "var(--ink)" }}>{t.title}</div>{t.seriesTitle && <div className="q-sub">{t.seriesTitle}</div>}</td>
                  <td>{(t.sections || []).length}</td>
                  <td>{qCount(t)}</td>
                  <td><Clock size={13} style={{ verticalAlign: -2, marginRight: 4, color: "var(--muted)" }} />{t.durationMin} min</td>
                  <td>
                    <button className="dot-pub" onClick={() => togglePublish(t)} disabled={busy === t.id} title="Click to toggle">
                      <span className="dot" style={{ background: t.isPublished ? "var(--green)" : "#d2c6a8" }} />
                      <span style={{ color: t.isPublished ? "var(--green)" : "var(--muted)" }}>{t.isPublished ? "Published" : "Draft"}</span>
                    </button>
                  </td>
                  <td><div className="row-actions">
                    <button className="btn-icon" onClick={() => togglePublish(t)} title={t.isPublished ? "Unpublish" : "Publish"}>{t.isPublished ? <EyeOff size={15} /> : <Eye size={15} />}</button>
                    <button className="btn-icon" onClick={() => setEditor(t)} title="Edit"><Pencil size={15} /></button>
                    <button className="btn-icon danger" onClick={() => del(t)} title="Delete"><Trash2 size={15} /></button>
                  </div></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

/* ============================================================
   VIEW: COURSES & BATCHES
   ============================================================ */
function Courses({ courses, saveCourse, removeCourse, batches, saveBatch, removeBatch, askDelete }) {
  const [courseForm, setCourseForm] = useState(null);
  const [batchForm, setBatchForm] = useState(null); // {courseId, batch?}

  const onSaveCourse = async (c) => { if (await saveCourse(c)) setCourseForm(null); };
  const delCourse = (c) => {
    const owned = batches.filter((b) => b.courseId === c.id).length;
    askDelete(
      owned
        ? `Delete "${c.title}"? Its ${owned} batch${owned > 1 ? "es" : ""} will be deleted too, and students enrolled in them lose access.`
        : `Delete "${c.title}"?`,
      () => removeCourse(c.id),
    );
  };
  const onSaveBatch = async (b) => { if (await saveBatch(b)) setBatchForm(null); };
  const delBatch = (b) => askDelete(`Delete batch "${b.name}"? Enrolled students lose access to its material.`, () => removeBatch(b.id));

  return (
    <div>
      <div className="sec-head">
        <div><h2>{courses.length} course{courses.length !== 1 ? "s" : ""}</h2><div className="note">Each course holds one or more batches with pricing</div></div>
        <button className="btn btn-primary" onClick={() => setCourseForm({})}><Plus size={16} />New course</button>
      </div>

      {courses.length === 0 ? (
        <div className="panel"><Empty icon={<GraduationCap size={26} />} title="No courses yet" text="Create a course, then add batches under it." action={<button className="btn btn-primary" onClick={() => setCourseForm({})}><Plus size={16} />New course</button>} /></div>
      ) : courses.map((c) => {
        const cb = batches.filter((b) => b.courseId === c.id);
        return (
          <div className="panel panel-pad" key={c.id} style={{ marginBottom: 16 }}>
            <div className="sec-head" style={{ marginBottom: 14 }}>
              <div>
                <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
                  <h2 style={{ fontSize: 16 }}>{c.title}</h2>
                  <span className="dot-pub"><span className="dot" style={{ background: c.isPublished ? "var(--green)" : "#d2c6a8" }} /><span style={{ color: c.isPublished ? "var(--green)" : "var(--muted)", fontSize: 12 }}>{c.isPublished ? "Published" : "Draft"}</span></span>
                </div>
                {c.examTarget && <div className="note" style={{ marginTop: 4 }}>{c.examTarget}{c.description ? " · " + c.description : ""}</div>}
              </div>
              <div style={{ display: "flex", gap: 8 }}>
                <button className="btn-icon" onClick={() => setCourseForm(c)}><Pencil size={15} /></button>
                <button className="btn-icon danger" onClick={() => delCourse(c)}><Trash2 size={15} /></button>
              </div>
            </div>

            {cb.length === 0 ? (
              <div style={{ fontSize: 13, color: "var(--muted)", padding: "8px 0 14px" }}>No batches in this course yet.</div>
            ) : (
              <div className="tbl-wrap" style={{ marginBottom: 14 }}>
                <table className="tbl">
                  <thead><tr><th>Batch</th><th>Price</th><th>Seats</th><th>Dates</th><th>Status</th><th style={{ textAlign: "right" }}></th></tr></thead>
                  <tbody>
                    {cb.map((b) => (
                      <tr key={b.id}>
                        <td style={{ fontWeight: 700, color: "var(--ink)" }}>{b.name}</td>
                        <td>{b.price > 0 ? fmtINR(b.price) : <span style={{ color: "var(--green)", fontWeight: 700 }}>Free</span>}</td>
                        <td>{b.seatLimit ?? "∞"}</td>
                        <td style={{ fontSize: 12.5, color: "var(--muted)" }}>{b.startDate || "—"}{b.endDate ? " → " + b.endDate : ""}</td>
                        <td><span className="dot-pub"><span className="dot" style={{ background: b.isActive ? "var(--green)" : "#d2c6a8" }} /><span style={{ fontSize: 12, color: b.isActive ? "var(--green)" : "var(--muted)" }}>{b.isActive ? "Active" : "Inactive"}</span></span></td>
                        <td><div className="row-actions">
                          <button className="btn-icon" onClick={() => setBatchForm({ courseId: c.id, batch: b })}><Pencil size={15} /></button>
                          <button className="btn-icon danger" onClick={() => delBatch(b)}><Trash2 size={15} /></button>
                        </div></td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
            <button className="btn btn-ghost btn-sm" onClick={() => setBatchForm({ courseId: c.id })}><Plus size={14} />Add batch</button>
          </div>
        );
      })}

      {courseForm && <CourseForm initial={courseForm.id ? courseForm : null} onSave={onSaveCourse} onClose={() => setCourseForm(null)} />}
      {batchForm && <BatchForm initial={batchForm.batch || null} courseId={batchForm.courseId} onSave={onSaveBatch} onClose={() => setBatchForm(null)} />}
    </div>
  );
}

/* ============================================================
   VIEW: MATERIALS
   ============================================================ */
function Materials({ materials, saveMaterial, removeMaterial, batches, askDelete }) {
  const [form, setForm] = useState(null);
  const save = async (m) => { if (await saveMaterial(m)) setForm(null); };
  const del = (m) => askDelete(`Delete "${m.title}"? Students will no longer see it.`, () => removeMaterial(m.id));
  const batchName = (id) => batches.find((b) => b.id === id)?.name || "Public";
  const typeColor = { pdf: { bg: "#fbeaea", fg: "#c0392b" }, note: { bg: "#faf2dc", fg: "#b8923a" }, video: { bg: "#f6ecd2", fg: "#7a1f1f" }, link: { bg: "#f4ecd6", fg: "#1a6b3c" } };

  return (
    <div>
      <div className="sec-head">
        <div><h2>{materials.length} material{materials.length !== 1 ? "s" : ""}</h2><div className="note">Free PDFs, notes and videos for students</div></div>
        <button className="btn btn-primary" onClick={() => setForm({})}><Plus size={16} />Add material</button>
      </div>

      {materials.length === 0 ? (
        <div className="panel"><Empty icon={<FolderOpen size={26} />} title="No materials yet" text="Add a PDF, note or video link for your students." action={<button className="btn btn-primary" onClick={() => setForm({})}><Plus size={16} />Add material</button>} /></div>
      ) : (
        <div className="tbl-wrap">
          <table className="tbl">
            <thead><tr><th>Title</th><th>Type</th><th>Access</th><th>Batch</th><th>Link</th><th style={{ textAlign: "right" }}>Actions</th></tr></thead>
            <tbody>
              {materials.map((m) => (
                <tr key={m.id}>
                  <td style={{ fontWeight: 700, color: "var(--ink)" }}>{m.title}</td>
                  <td><Badge color={typeColor[m.type]}>{m.type.toUpperCase()}</Badge></td>
                  <td>{m.isFree ? <span style={{ color: "var(--green)", fontWeight: 700, fontSize: 13 }}>Free</span> : <span style={{ color: "var(--amber)", fontWeight: 700, fontSize: 13 }}>Paid</span>}</td>
                  <td style={{ fontSize: 13, color: "var(--muted)" }}>{batchName(m.batchId)}</td>
                  <td>{m.url ? <a href={m.url} target="_blank" rel="noreferrer" style={{ color: "var(--navy)", fontSize: 13, fontWeight: 600 }}>Open ↗</a> : <span style={{ color: "var(--muted)", fontSize: 13 }}>—</span>}</td>
                  <td><div className="row-actions">
                    <button className="btn-icon" onClick={() => setForm(m)}><Pencil size={15} /></button>
                    <button className="btn-icon danger" onClick={() => del(m)}><Trash2 size={15} /></button>
                  </div></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
      {form && <MaterialForm initial={form.id ? form : null} batches={batches} onSave={save} onClose={() => setForm(null)} />}
    </div>
  );
}

/* ============================================================
   VIEW: BUNDLES — the priced test series a student can buy.

   Price lives here and nowhere else. The checkout function
   re-reads it from the database on every order, so changing a
   price on this screen changes what the next buyer is charged,
   with no redeploy.
   ============================================================ */
function Bundles({ tests, toast }) {
  const [rows, setRows] = useState(null);
  const [exams, setExams] = useState([]);
  const [err, setErr] = useState("");
  const [reloadKey, setReloadKey] = useState(0);
  const [editing, setEditing] = useState(null);   // bundle or {} for new
  const [assigning, setAssigning] = useState(null); // bundle code
  const [counts, setCounts] = useState({});

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const list = await DB.adminListBundles();
        if (!alive) return;
        setErr("");
        setRows(list);
        const [pairs, cats] = await Promise.all([
          Promise.all(list.map(async (b) => [b.code, (await DB.bundleTestIds(b.code)).length])),
          DB.examCategories({ includeInactive: true }).catch(() => []),
        ]);
        if (alive) { setCounts(Object.fromEntries(pairs)); setExams(cats); }
      } catch (e) {
        console.error(e);
        if (alive) { setErr(e?.message || "Couldn't load bundles."); setRows([]); }
      }
    })();
    return () => { alive = false; };
  }, [reloadKey]);

  const reload = () => setReloadKey((k) => k + 1);

  const save = async (b) => {
    try {
      await DB.upsertBundle(b);
      toast(`"${b.name}" saved`);
      setEditing(null);
      reload();
    } catch (e) {
      console.error(e);
      toast(e?.message || "Couldn't save this bundle", "err");
    }
  };

  const toggleActive = async (b) => {
    try {
      await DB.upsertBundle({ ...b, isActive: !b.isActive });
      toast(b.isActive ? `"${b.name}" hidden from the site` : `"${b.name}" is now live`);
      reload();
    } catch (e) {
      console.error(e);
      toast(e?.message || "Couldn't update this bundle", "err");
    }
  };

  if (err) return <div className="panel"><ErrorState message={err} onRetry={reload} /></div>;
  if (!rows) return <SkeletonCards count={3} height={140} />;

  if (assigning) {
    const b = rows.find((x) => x.code === assigning);
    return (
      <BundleTests
        bundle={b}
        tests={tests}
        onDone={() => { setAssigning(null); reload(); }}
        toast={toast}
      />
    );
  }

  const live = rows.filter((b) => b.isActive).length;

  return (
    <div>
      <div className="stats">
        <StatCard icon={<Layers size={20} />} color={{ bg: "#faf2dc", fg: "#b8923a" }} n={rows.length} label="Bundles" sub={`${live} live on the site`} />
        <StatCard icon={<FileText size={20} />} color={{ bg: "#f6ecd2", fg: "#7a1f1f" }}
                  n={Object.values(counts).reduce((a, b) => a + b, 0)} label="Test assignments" sub="across all bundles" />
        <StatCard icon={<IndianRupee size={20} />} color={{ bg: "#e8f6ee", fg: "#1f8a4c" }}
                  n={rows.length ? fmtINR(Math.min(...rows.map((b) => b.price))) : "—"} label="Lowest price" sub="entry point" />
      </div>

      <div className="sec-head">
        <div><h2>{rows.length} test series bundle{rows.length !== 1 ? "s" : ""}</h2>
          <div className="note">Each is priced and sold separately — buying one never unlocks another</div></div>
        <button className="btn btn-primary" onClick={() => setEditing({})}><Plus size={16} />New bundle</button>
      </div>

      {rows.length === 0 ? (
        <div className="panel"><Empty icon={<Layers size={26} />} title="No bundles yet"
          text="Create a bundle for each exam you sell — UPSC, BPSC, UPPCS."
          action={<button className="btn btn-primary" onClick={() => setEditing({})}><Plus size={16} />New bundle</button>} /></div>
      ) : (
        <div className="tbl-wrap">
          <table className="tbl">
            <thead><tr>
              <th>Bundle</th><th>Exam</th><th>Price</th><th>Tests</th><th>Validity</th><th>Status</th>
              <th style={{ textAlign: "right" }}>Actions</th>
            </tr></thead>
            <tbody>
              {rows.map((b) => (
                <tr key={b.code}>
                  <td>
                    <div style={{ fontWeight: 700, color: "var(--ink)" }}>{b.name}</div>
                    <div className="q-sub">{b.code}</div>
                  </td>
                  <td><Badge color={{ bg: "#f6ecd2", fg: "#7a1f1f" }}>{String(b.exam).toUpperCase()}</Badge></td>
                  <td>
                    <div style={{ fontWeight: 800 }}>{fmtINR(b.price)}</div>
                    {b.mrp ? <div className="q-sub" style={{ textDecoration: "line-through" }}>{fmtINR(b.mrp)}</div> : null}
                  </td>
                  <td>
                    <button className="btn btn-ghost btn-sm" style={{ width: "auto" }} onClick={() => setAssigning(b.code)}>
                      {counts[b.code] ?? 0} assigned
                    </button>
                  </td>
                  <td style={{ color: "var(--muted)", fontSize: 13 }}>
                    {b.durationDays ? `${Math.round(b.durationDays / 30)} months` : "Lifetime"}
                  </td>
                  <td>
                    <button className="dot-pub" onClick={() => toggleActive(b)} title="Click to toggle">
                      <span className="dot" style={{ background: b.isActive ? "var(--green)" : "#d2c6a8" }} />
                      <span style={{ color: b.isActive ? "var(--green)" : "var(--muted)" }}>{b.isActive ? "Live" : "Hidden"}</span>
                    </button>
                  </td>
                  <td><div className="row-actions">
                    <button className="btn-icon" title="Assign tests" onClick={() => setAssigning(b.code)}><Layers size={15} /></button>
                    <button className="btn-icon" title="Edit" onClick={() => setEditing(b)}><Pencil size={15} /></button>
                  </div></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {editing && (
        <BundleForm
          initial={editing.code ? editing : null}
          exams={exams}
          existingCodes={rows.map((r) => r.code)}
          onSave={save}
          onClose={() => setEditing(null)}
        />
      )}
    </div>
  );
}

function BundleForm({ initial, exams = [], existingCodes, onSave, onClose }) {
  const [f, setF] = useState(initial || {
    code: "", name: "", exam: "upsc", tagline: "", description: "",
    price: "", mrp: "", durationDays: 365, features: [], isActive: true, sortOrder: 0,
  });
  const [featureText, setFeatureText] = useState((initial?.features || []).join("\n"));
  const [err, setErr] = useState("");
  const set = (k, v) => setF((p) => ({ ...p, [k]: v }));
  const isNew = !initial;

  const submit = () => {
    const code = String(f.code || "").trim().toLowerCase();
    if (!code) return setErr("A short code is required — it identifies this bundle forever.");
    if (!/^[a-z0-9-]+$/.test(code)) return setErr("The code may only contain lowercase letters, numbers and hyphens.");
    if (isNew && existingCodes.includes(code)) return setErr("That code is already used by another bundle.");
    if (!f.name.trim()) return setErr("Bundle name is required.");
    const price = Number(f.price);
    if (!Number.isFinite(price) || price < 0) return setErr("Enter a valid price.");
    if (f.mrp !== "" && Number(f.mrp) < price) return setErr("MRP can't be lower than the selling price.");
    setErr("");
    onSave({
      ...f,
      code,
      name: f.name.trim(),
      price,
      features: featureText.split("\n").map((x) => x.trim()).filter(Boolean),
    });
  };

  return (
    <Modal
      title={isNew ? "New bundle" : "Edit bundle"}
      onClose={onClose}
      wide
      footer={<>
        <button className="btn btn-ghost" onClick={onClose}>Cancel</button>
        <button className="btn btn-primary" onClick={submit}><Save size={16} />Save bundle</button>
      </>}
    >
      {err && <div className="form-err"><AlertCircle size={17} />{err}</div>}

      <div className="field-row">
        <Field label="Bundle name" req>
          <input className="inp" value={f.name} placeholder="e.g. BPSC Prelims 2026 — Full Test Series"
                 onChange={(e) => set("name", e.target.value)} />
        </Field>
        <Field label="Exam" req hint="Manage this list under Exams &amp; Categories.">
          <select className="inp" value={f.exam} onChange={(e) => set("exam", e.target.value)}>
            {exams.length === 0 && <option value={f.exam}>{f.exam}</option>}
            {exams.map((e) => (
              <option key={e.code} value={e.code}>
                {e.label}{e.conductedBy && e.conductedBy !== e.label ? ` — via ${e.conductedBy}` : ""}
                {e.isActive ? "" : " (hidden)"}
              </option>
            ))}
          </select>
        </Field>
      </div>

      <Field label="Short code" req
             hint={isNew
               ? "Lowercase, no spaces — e.g. bpsc-2026. This can never be changed once students have bought it."
               : "Locked: existing enrollments and payments reference this code."}>
        <input className="inp" value={f.code} placeholder="bpsc-2026" disabled={!isNew}
               style={!isNew ? { opacity: .6, cursor: "not-allowed" } : undefined}
               onChange={(e) => set("code", e.target.value)} />
      </Field>

      <Field label="One-line tagline" hint="Shown on the bundle card.">
        <input className="inp" value={f.tagline} placeholder="Bihar-focused GS with current affairs depth"
               onChange={(e) => set("tagline", e.target.value)} />
      </Field>

      <Field label="Description" hint="Shown on the bundle's detail page.">
        <textarea className="inp" rows={3} value={f.description} onChange={(e) => set("description", e.target.value)} />
      </Field>

      <div className="field-row">
        <Field label="Selling price (₹)" req hint="What the student actually pays.">
          <input className="inp" type="number" min="0" value={f.price} onChange={(e) => set("price", e.target.value)} />
        </Field>
        <Field label="MRP (₹)" hint="Struck-through price. Leave blank for no discount badge.">
          <input className="inp" type="number" min="0" value={f.mrp} onChange={(e) => set("mrp", e.target.value)} />
        </Field>
      </div>

      <div className="field-row">
        <Field label="Validity (days)" hint="Blank = lifetime access.">
          <input className="inp" type="number" min="1" value={f.durationDays}
                 onChange={(e) => set("durationDays", e.target.value)} />
        </Field>
        <Field label="Display order" hint="Lower numbers appear first on the site.">
          <input className="inp" type="number" value={f.sortOrder} onChange={(e) => set("sortOrder", e.target.value)} />
        </Field>
      </div>

      <Field label="What's included" hint="One benefit per line — these become the ticks on the sales page.">
        <textarea className="inp" rows={5} value={featureText} onChange={(e) => setFeatureText(e.target.value)}
                  placeholder={"20 full-length mock tests\nDetailed solutions for every question\nAll-India rank and percentile"} />
      </Field>

      <Field label="Visibility">
        <div className="seg">
          <button type="button" className={f.isActive ? "on" : ""} onClick={() => set("isActive", true)}>Live on the site</button>
          <button type="button" className={!f.isActive ? "on" : ""} onClick={() => set("isActive", false)}>Hidden</button>
        </div>
      </Field>
    </Modal>
  );
}

/* Assign which tests a bundle unlocks. This is what keeps bundles isolated —
   a test not listed here stays locked for that bundle's subscribers. */
function BundleTests({ bundle, tests, onDone, toast }) {
  const [selected, setSelected] = useState(null);
  const [q, setQ] = useState("");
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const ids = await DB.bundleTestIds(bundle.code);
        if (alive) setSelected(new Set(ids));
      } catch (e) {
        console.error(e);
        if (alive) setSelected(new Set());
      }
    })();
    return () => { alive = false; };
  }, [bundle.code]);

  if (!selected) return <SkeletonCards count={2} height={110} />;

  const needle = q.trim().toLowerCase();
  const shown = tests.filter((t) => !needle || t.title.toLowerCase().includes(needle));

  const toggle = (id) => {
    const next = new Set(selected);
    next.has(id) ? next.delete(id) : next.add(id);
    setSelected(next);
  };

  const save = async () => {
    setSaving(true);
    try {
      await DB.setBundleTests(bundle.code, [...selected]);
      toast(`${selected.size} test${selected.size === 1 ? "" : "s"} assigned to "${bundle.name}"`);
      onDone();
    } catch (e) {
      console.error(e);
      toast(e?.message || "Couldn't save the assignment", "err");
      setSaving(false);
    }
  };

  return (
    <div>
      <button className="btn btn-ghost btn-sm" onClick={onDone} style={{ marginBottom: 16 }}>
        <ArrowLeft size={15} />Back to bundles
      </button>

      <div className="sec-head">
        <div>
          <h2>Tests in "{bundle.name}"</h2>
          <div className="note">
            Only the tests ticked here unlock for someone who buys this bundle. Anything unticked
            stays locked for them, even if it's published.
          </div>
        </div>
        <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
          <div className="search"><Search size={15} /><input placeholder="Search tests…" value={q} onChange={(e) => setQ(e.target.value)} /></div>
          <button className="btn btn-primary" onClick={save} disabled={saving}>
            <Save size={16} />{saving ? "Saving…" : `Save (${selected.size})`}
          </button>
        </div>
      </div>

      {tests.length === 0 ? (
        <div className="panel"><Empty icon={<FileText size={26} />} title="No tests yet"
          text="Create and publish a test first, then come back to assign it to this bundle." /></div>
      ) : (
        <div className="panel panel-pad">
          {shown.map((t) => {
            const on = selected.has(t.id);
            return (
              <button
                key={t.id}
                className={"picker-item" + (on ? " on" : "")}
                onClick={() => toggle(t.id)}
                style={{ width: "100%", textAlign: "left" }}
              >
                <span className="picker-check">{on ? <Check size={14} /> : null}</span>
                <span style={{ flex: 1, minWidth: 0 }}>
                  <span style={{ display: "block", fontWeight: 700, color: "var(--ink)" }}>{t.title}</span>
                  <span className="q-sub">
                    {t.totalQuestions} questions · {t.durationMin} min
                    {t.isFree ? " · free sample" : ""}
                    {t.isPublished ? "" : " · draft (students can't see it)"}
                  </span>
                </span>
              </button>
            );
          })}
          {shown.length === 0 && (
            <div style={{ padding: "24px 0", textAlign: "center", color: "var(--muted)", fontSize: 13.5 }}>
              No test matches "{q}".
            </div>
          )}
        </div>
      )}
    </div>
  );
}

/* ============================================================
   VIEW: EXAMS & CATEGORIES

   This list used to be a CHECK constraint in the schema and a
   hardcoded map in the UI — which is why a JPSC bundle silently
   filed itself under "Other". Adding an exam here makes its tab
   appear on the public site immediately: no SQL, no deploy.
   ============================================================ */
function Exams({ toast, askDelete }) {
  const [rows, setRows] = useState(null);
  const [err, setErr] = useState("");
  const [reloadKey, setReloadKey] = useState(0);
  const [editing, setEditing] = useState(null);
  const [usage, setUsage] = useState({});

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const [cats, plans] = await Promise.all([
          DB.examCategories({ includeInactive: true }),
          DB.adminListBundles().catch(() => []),
        ]);
        if (!alive) return;
        setErr("");
        setRows(cats);
        const counts = {};
        plans.forEach((p) => { counts[p.exam] = (counts[p.exam] || 0) + 1; });
        setUsage(counts);
      } catch (e) {
        console.error(e);
        if (alive) { setErr(e?.message || "Couldn't load exams."); setRows([]); }
      }
    })();
    return () => { alive = false; };
  }, [reloadKey]);

  const reload = () => setReloadKey((k) => k + 1);

  const save = async (c) => {
    try {
      await DB.upsertExamCategory(c);
      toast(`"${c.label}" saved`);
      setEditing(null);
      reload();
    } catch (e) {
      console.error(e);
      toast(e?.message || "Couldn't save this exam", "err");
    }
  };

  const toggleActive = async (c) => {
    try {
      await DB.upsertExamCategory({ ...c, isActive: !c.isActive });
      toast(c.isActive ? `"${c.label}" hidden from the site` : `"${c.label}" is now visible`);
      reload();
    } catch (e) { console.error(e); toast(e?.message || "Couldn't update", "err"); }
  };

  const remove = (c) => {
    const used = usage[c.code] || 0;
    if (used > 0) {
      toast(`"${c.label}" is used by ${used} bundle${used > 1 ? "s" : ""} — move them first, or just hide it`, "err");
      return;
    }
    askDelete(
      `Delete the "${c.label}" exam category? No bundle is using it, so nothing else changes.`,
      async () => {
        try { await DB.deleteExamCategory(c.code); toast("Deleted"); reload(); }
        catch (e) { console.error(e); toast(e?.message || "Couldn't delete", "err"); }
      },
    );
  };

  if (err) return <div className="panel"><ErrorState message={err} onRetry={reload} /></div>;
  if (!rows) return <SkeletonCards count={2} height={110} />;

  const live = rows.filter((r) => r.isActive).length;
  const inUse = rows.filter((r) => (usage[r.code] || 0) > 0).length;

  return (
    <div>
      <div className="stats">
        <StatCard icon={<Layers size={20} />} color={{ bg: "#faf2dc", fg: "#b8923a" }} n={rows.length}
                  label="Exam categories" sub={`${live} visible on the site`} />
        <StatCard icon={<GraduationCap size={20} />} color={{ bg: "#e8f6ee", fg: "#1f8a4c" }} n={inUse}
                  label="With a bundle" sub="these become tabs" />
      </div>

      <div className="banner">
        <AlertCircle size={17} />
        An exam only becomes a tab on the public site once at least one bundle uses it.
      </div>

      <div className="sec-head">
        <div>
          <h2>{rows.length} exam{rows.length !== 1 ? "s" : ""}</h2>
          <div className="note">Used by bundles, syllabus entries and previous-year papers</div>
        </div>
        <button className="btn btn-primary" onClick={() => setEditing({
          code: "", label: "", fullName: "", conductedBy: "", region: "", sortOrder: 100, isActive: true,
        })}><Plus size={16} />Add exam</button>
      </div>

      <div className="tbl-wrap">
        <table className="tbl">
          <thead><tr>
            <th>Exam</th><th>Conducted by</th><th>Region</th><th>Bundles</th><th>Order</th>
            <th>Status</th><th style={{ textAlign: "right" }}>Actions</th>
          </tr></thead>
          <tbody>
            {rows.map((c) => (
              <tr key={c.code}>
                <td>
                  <div style={{ fontWeight: 700, color: "var(--ink)" }}>{c.label}</div>
                  <div className="q-sub">{c.fullName || c.code}</div>
                </td>
                <td style={{ color: "var(--muted)" }}>{c.conductedBy || "—"}</td>
                <td style={{ color: "var(--muted)" }}>{c.region || "—"}</td>
                <td>{usage[c.code] || 0}</td>
                <td style={{ color: "var(--muted)" }}>{c.sortOrder}</td>
                <td>
                  <button className="dot-pub" onClick={() => toggleActive(c)} title="Click to toggle">
                    <span className="dot" style={{ background: c.isActive ? "var(--green)" : "#d2c6a8" }} />
                    <span style={{ color: c.isActive ? "var(--green)" : "var(--muted)" }}>
                      {c.isActive ? "Visible" : "Hidden"}
                    </span>
                  </button>
                </td>
                <td><div className="row-actions">
                  <button className="btn-icon" title="Edit" onClick={() => setEditing(c)}><Pencil size={15} /></button>
                  <button className="btn-icon danger" title="Delete" onClick={() => remove(c)}><Trash2 size={15} /></button>
                </div></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {editing && (
        <ExamForm
          initial={editing.code ? editing : null}
          existingCodes={rows.map((r) => r.code)}
          value={editing}
          onSave={save}
          onClose={() => setEditing(null)}
        />
      )}
    </div>
  );
}

function ExamForm({ initial, existingCodes, value, onSave, onClose }) {
  const [f, setF] = useState(() => ({ ...value }));
  const [err, setErr] = useState("");
  const set = (k, v) => setF((p) => ({ ...p, [k]: v }));
  const isNew = !initial;

  const submit = () => {
    const code = String(f.code || "").trim().toLowerCase();
    if (!code) return setErr("A short code is required.");
    if (!/^[a-z0-9-]+$/.test(code)) return setErr("The code may only contain lowercase letters, numbers and hyphens.");
    if (isNew && existingCodes.includes(code)) return setErr("That code already exists.");
    if (!String(f.label || "").trim()) return setErr("A short label is required — it is what shows on the tab.");
    setErr("");
    onSave({ ...f, code, label: f.label.trim() });
  };

  return (
    <Modal
      title={isNew ? "New exam category" : `Edit ${f.label}`}
      onClose={onClose}
      footer={<>
        <button className="btn btn-ghost" onClick={onClose}>Cancel</button>
        <button className="btn btn-primary" onClick={submit}><Save size={16} />Save</button>
      </>}
    >
      {err && <div className="form-err"><AlertCircle size={17} />{err}</div>}

      <div className="field-row">
        <Field label="Short code" req
               hint={isNew ? "Lowercase, no spaces — e.g. rpsc. Bundles reference this." : "Renaming cascades to every bundle using it."}>
          <input className="inp" value={f.code} placeholder="rpsc" onChange={(e) => set("code", e.target.value)} />
        </Field>
        <Field label="Tab label" req hint="Short — this is the button text.">
          <input className="inp" value={f.label} placeholder="RPSC" onChange={(e) => set("label", e.target.value)} />
        </Field>
      </div>

      <Field label="Full name" hint="Shown on the bundle detail page.">
        <input className="inp" value={f.fullName || ""} placeholder="Rajasthan Administrative Service (RAS)"
               onChange={(e) => set("fullName", e.target.value)} />
      </Field>

      <div className="field-row">
        <Field label="Conducted by" hint="The commission that runs it — e.g. EPFO is conducted by UPSC.">
          <input className="inp" value={f.conductedBy || ""} placeholder="RPSC"
                 onChange={(e) => set("conductedBy", e.target.value)} />
        </Field>
        <Field label="Region">
          <input className="inp" value={f.region || ""} placeholder="Rajasthan"
                 onChange={(e) => set("region", e.target.value)} />
        </Field>
      </div>

      <Field label="Display order" hint="Lower numbers appear first in the tab row.">
        <input className="inp" type="number" value={f.sortOrder}
               onChange={(e) => set("sortOrder", e.target.value)} />
      </Field>

      <Field label="Visibility">
        <div className="seg">
          <button type="button" className={f.isActive !== false ? "on" : ""} onClick={() => set("isActive", true)}>Visible</button>
          <button type="button" className={f.isActive === false ? "on" : ""} onClick={() => set("isActive", false)}>Hidden</button>
        </div>
      </Field>
    </Modal>
  );
}

/* ============================================================
   VIEW: CONTENT — the public hub's back office.

   Syllabus, previous-year papers, NCERT, daily current affairs
   and FAQ all share the same shape (a flat table of rows, each
   with a handful of fields), so they share one screen driven by
   a field schema rather than five near-identical components.
   ============================================================ */
const CONTENT_TYPES = [
  {
    key: "syllabus", label: "Syllabus", api: () => DB.adminSyllabus,
    columns: [["exam", "Exam"], ["paper", "Paper"], ["section", "Section"], ["topic", "Topic"]],
    blank: { exam: "upsc", paper: "", section: "", topic: "", detail: "", sort_order: 0, is_published: true },
    fields: [
      { k: "exam", label: "Exam", req: true, type: "exam" },
      { k: "paper", label: "Paper", req: true, hint: "e.g. Prelims — General Studies Paper I" },
      { k: "section", label: "Section", hint: "e.g. Polity. Shown as a small label above the topic." },
      { k: "topic", label: "Topic", req: true, type: "textarea" },
      { k: "detail", label: "Extra detail", type: "textarea" },
      { k: "sort_order", label: "Order", type: "number" },
    ],
  },
  {
    key: "pyq", label: "Previous Year Papers", api: () => DB.adminPyq,
    columns: [["year", "Year"], ["exam", "Exam"], ["paper", "Paper"], ["title", "Title"]],
    blank: { exam: "upsc", year: new Date().getFullYear() - 1, paper: "", title: "", paper_url: "", solution_url: "", question_count: null, notes: "", is_published: true },
    fields: [
      { k: "exam", label: "Exam", req: true, type: "exam" },
      { k: "year", label: "Year", req: true, type: "number" },
      { k: "paper", label: "Paper", req: true, hint: "e.g. Prelims GS Paper I" },
      { k: "title", label: "Title", req: true },
      { k: "paper_url", label: "Question paper URL", type: "file", hint: "Upload the PDF, or paste a link." },
      { k: "solution_url", label: "Solutions URL", type: "file", hint: "Answer key or solved paper." },
      { k: "question_count", label: "Number of questions", type: "number" },
      { k: "notes", label: "Notes", type: "textarea" },
    ],
  },
  {
    key: "ncert", label: "NCERT Books", api: () => DB.adminNcert,
    columns: [["class_level", "Class"], ["subject", "Subject"], ["title", "Title"], ["language", "Lang"]],
    blank: { class_level: 6, subject: "", title: "", language: "en", url: "", sort_order: 0, is_published: true },
    fields: [
      { k: "class_level", label: "Class", req: true, type: "number", hint: "1–12" },
      { k: "subject", label: "Subject", req: true, hint: "e.g. History" },
      { k: "title", label: "Title", req: true },
      { k: "language", label: "Language", type: "select", options: ["en", "hi"] },
      { k: "url", label: "Book URL", type: "file", hint: "Upload the PDF, or link to the official NCERT page." },
      { k: "sort_order", label: "Order", type: "number" },
    ],
  },
  {
    key: "news", label: "Current Affairs", api: () => DB.adminCA,
    columns: [["published_on", "Date"], ["title", "Headline"]],
    blank: { published_on: new Date().toISOString().slice(0, 10), title: "", summary: "", body: "", tags: [], exam_tags: [], source_name: "", source_url: "", is_published: true },
    fields: [
      { k: "published_on", label: "Date", req: true, type: "date" },
      { k: "title", label: "Headline", req: true },
      { k: "summary", label: "One-line summary", hint: "Shown collapsed, before the reader expands the item." },
      { k: "body", label: "Full note", type: "textarea", rows: 7 },
      { k: "exam_tags", label: "Relevant exams", type: "tags", hint: "Comma separated — upsc, bpsc, uppcs" },
      { k: "tags", label: "Topic tags", type: "tags", hint: "Comma separated — Polity, Economy…" },
      { k: "source_name", label: "Source name", hint: "e.g. PIB, The Hindu" },
      { k: "source_url", label: "Source link" },
    ],
  },
  {
    key: "faq", label: "FAQ", api: () => DB.adminFaqs,
    columns: [["category", "Category"], ["question", "Question"]],
    blank: { category: "general", question: "", answer: "", sort_order: 0, is_published: true },
    fields: [
      { k: "category", label: "Category", type: "select", options: ["tests", "payments", "access", "general"] },
      { k: "question", label: "Question", req: true, type: "textarea" },
      { k: "answer", label: "Answer", req: true, type: "textarea", rows: 5 },
      { k: "sort_order", label: "Order", type: "number" },
    ],
  },
];

function Content({ toast, askDelete }) {
  const [type, setType] = useState(CONTENT_TYPES[0]);
  const [rows, setRows] = useState(null);
  const [err, setErr] = useState("");
  const [reloadKey, setReloadKey] = useState(0);
  const [editing, setEditing] = useState(null);
  const [q, setQ] = useState("");

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const list = await type.api().list();
        if (!alive) return;
        setErr(""); setRows(list);
      } catch (e) {
        console.error(e);
        if (alive) { setErr(e?.message || "Couldn't load this content."); setRows([]); }
      }
    })();
    return () => { alive = false; };
  }, [type, reloadKey]);

  const reload = () => setReloadKey((k) => k + 1);

  const save = async (row) => {
    try {
      await type.api().upsert(row);
      toast(`${type.label} entry saved`);
      setEditing(null);
      reload();
    } catch (e) {
      console.error(e);
      toast(e?.message || "Couldn't save this entry", "err");
    }
  };

  const remove = (row) => askDelete(
    "Delete this entry? It disappears from the public site immediately.",
    async () => {
      try { await type.api().remove(row.id); toast("Deleted"); reload(); }
      catch (e) { console.error(e); toast(e?.message || "Couldn't delete", "err"); }
    },
  );

  const togglePublish = async (row) => {
    try {
      await type.api().upsert({ ...row, is_published: !row.is_published });
      reload();
    } catch (e) { console.error(e); toast(e?.message || "Couldn't update", "err"); }
  };

  const needle = q.trim().toLowerCase();
  const shown = (rows || []).filter((r) =>
    !needle || type.columns.some(([k]) => String(r[k] ?? "").toLowerCase().includes(needle)));

  return (
    <div>
      <div className="tabs" style={{ marginBottom: 18 }}>
        {CONTENT_TYPES.map((ct) => (
          <button key={ct.key} className={"tab" + (type.key === ct.key ? " active" : "")}
                  onClick={() => { setType(ct); setRows(null); setQ(""); }}>
            {ct.label}
          </button>
        ))}
      </div>

      <div className="banner">
        <AlertCircle size={17} />
        Everything here is public — it appears on the site immediately, with no login required to read it.
      </div>

      <div className="sec-head">
        <div>
          <h2>{shown.length} {type.label.toLowerCase()} {shown.length === 1 ? "entry" : "entries"}</h2>
          <div className="note">Published entries are live on the public content hub</div>
        </div>
        <div style={{ display: "flex", gap: 8, alignItems: "center", flexWrap: "wrap" }}>
          <div className="search"><Search size={15} /><input placeholder="Search…" value={q} onChange={(e) => setQ(e.target.value)} /></div>
          <button className="btn btn-primary" onClick={() => setEditing({ ...type.blank })}><Plus size={16} />Add entry</button>
        </div>
      </div>

      {err ? <div className="panel"><ErrorState message={err} onRetry={reload} /></div>
        : rows === null ? <SkeletonCards count={2} height={110} />
        : shown.length === 0 ? (
          <div className="panel">
            <Empty icon={<FileText size={26} />} title={`No ${type.label.toLowerCase()} yet`}
                   text={`Add your first entry — it goes live on the public site straight away.`}
                   action={<button className="btn btn-primary" onClick={() => setEditing({ ...type.blank })}><Plus size={16} />Add entry</button>} />
          </div>
        ) : (
          <div className="tbl-wrap">
            <table className="tbl">
              <thead><tr>
                {type.columns.map(([k, label]) => <th key={k}>{label}</th>)}
                <th>Status</th><th style={{ textAlign: "right" }}>Actions</th>
              </tr></thead>
              <tbody>
                {shown.map((r) => (
                  <tr key={r.id}>
                    {type.columns.map(([k], i) => (
                      <td key={k} style={i === type.columns.length - 1
                        ? { fontWeight: 600, color: "var(--ink)", maxWidth: 380 }
                        : { color: "var(--muted)", whiteSpace: "nowrap" }}>
                        {String(r[k] ?? "—")}
                      </td>
                    ))}
                    <td>
                      <button className="dot-pub" onClick={() => togglePublish(r)} title="Click to toggle">
                        <span className="dot" style={{ background: r.is_published ? "var(--green)" : "#d2c6a8" }} />
                        <span style={{ color: r.is_published ? "var(--green)" : "var(--muted)" }}>
                          {r.is_published ? "Live" : "Hidden"}
                        </span>
                      </button>
                    </td>
                    <td><div className="row-actions">
                      <button className="btn-icon" title="Edit" onClick={() => setEditing(r)}><Pencil size={15} /></button>
                      <button className="btn-icon danger" title="Delete" onClick={() => remove(r)}><Trash2 size={15} /></button>
                    </div></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

      {editing && (
        <ContentForm type={type} initial={editing} onSave={save} onClose={() => setEditing(null)} toast={toast} />
      )}
    </div>
  );
}

function ContentForm({ type, initial, onSave, onClose, toast }) {
  const [f, setF] = useState(() => ({ ...initial }));
  const [err, setErr] = useState("");
  const [uploading, setUploading] = useState("");
  const [exams, setExams] = useState([]);
  const fileRefs = useRef({});

  useEffect(() => {
    let alive = true;
    DB.examCategories().then((c) => { if (alive) setExams(c); }).catch(() => {});
    return () => { alive = false; };
  }, []);
  const set = (k, v) => setF((p) => ({ ...p, [k]: v }));

  const onFile = async (key, e) => {
    const file = e.target.files?.[0];
    e.target.value = "";
    if (!file) return;
    setErr(""); setUploading(key);
    try {
      const { url } = await DB.uploadMaterialFile(file);
      set(key, url);
      toast("File uploaded");
    } catch (ex) {
      console.error(ex);
      setErr(ex?.message || "Upload failed.");
    }
    setUploading("");
  };

  const submit = () => {
    for (const fl of type.fields) {
      if (fl.req && !String(f[fl.k] ?? "").trim()) return setErr(`${fl.label} is required.`);
    }
    setErr("");
    // Numbers arrive from inputs as strings; the columns are integers.
    const row = { ...f };
    type.fields.forEach((fl) => {
      if (fl.type === "number") row[fl.k] = row[fl.k] === "" || row[fl.k] == null ? null : Number(row[fl.k]);
      if (fl.type === "tags" && typeof row[fl.k] === "string") {
        row[fl.k] = row[fl.k].split(",").map((x) => x.trim()).filter(Boolean);
      }
    });
    onSave(row);
  };

  return (
    <Modal
      title={initial.id ? `Edit ${type.label.toLowerCase()} entry` : `New ${type.label.toLowerCase()} entry`}
      onClose={onClose}
      wide
      footer={<>
        <button className="btn btn-ghost" onClick={onClose}>Cancel</button>
        <button className="btn btn-primary" onClick={submit}><Save size={16} />Save</button>
      </>}
    >
      {err && <div className="form-err"><AlertCircle size={17} />{err}</div>}

      {type.fields.map((fl) => {
        const val = f[fl.k];
        if (fl.type === "exam") {
          return (
            <Field key={fl.k} label={fl.label} req={fl.req} hint="Manage this list under Exams &amp; Categories.">
              <select className="inp" value={val ?? ""} onChange={(e) => set(fl.k, e.target.value)}>
                <option value="" disabled>Choose an exam…</option>
                {exams.map((e) => <option key={e.code} value={e.code}>{e.label}</option>)}
              </select>
            </Field>
          );
        }
        if (fl.type === "select") {
          return (
            <Field key={fl.k} label={fl.label} req={fl.req} hint={fl.hint}>
              <select className="inp" value={val ?? ""} onChange={(e) => set(fl.k, e.target.value)}>
                {fl.options.map((o) => <option key={o} value={o}>{o.toUpperCase()}</option>)}
              </select>
            </Field>
          );
        }
        if (fl.type === "textarea") {
          return (
            <Field key={fl.k} label={fl.label} req={fl.req} hint={fl.hint}>
              <textarea className="inp" rows={fl.rows || 3} value={val ?? ""} onChange={(e) => set(fl.k, e.target.value)} />
            </Field>
          );
        }
        if (fl.type === "tags") {
          const asText = Array.isArray(val) ? val.join(", ") : (val ?? "");
          return (
            <Field key={fl.k} label={fl.label} req={fl.req} hint={fl.hint}>
              <input className="inp" value={asText} onChange={(e) => set(fl.k, e.target.value)} />
            </Field>
          );
        }
        if (fl.type === "file") {
          return (
            <Field key={fl.k} label={fl.label} req={fl.req} hint={fl.hint}>
              <div style={{ display: "flex", gap: 9, alignItems: "center", flexWrap: "wrap" }}>
                <button type="button" className="btn btn-ghost btn-sm" style={{ width: "auto" }}
                        disabled={uploading === fl.k}
                        onClick={() => fileRefs.current[fl.k]?.click()}>
                  <Upload size={15} />{uploading === fl.k ? "Uploading…" : "Upload"}
                </button>
                <input ref={(el) => { fileRefs.current[fl.k] = el; }} type="file" style={{ display: "none" }}
                       accept=".pdf,.png,.jpg,.jpeg,.webp,.docx" onChange={(e) => onFile(fl.k, e)} />
                <input className="inp" style={{ flex: 1, minWidth: 180 }} placeholder="https://…"
                       value={val ?? ""} onChange={(e) => set(fl.k, e.target.value)} />
              </div>
            </Field>
          );
        }
        return (
          <Field key={fl.k} label={fl.label} req={fl.req} hint={fl.hint}>
            <input className="inp" type={fl.type === "number" ? "number" : fl.type === "date" ? "date" : "text"}
                   value={val ?? ""} onChange={(e) => set(fl.k, e.target.value)} />
          </Field>
        );
      })}

      <Field label="Visibility">
        <div className="seg">
          <button type="button" className={f.is_published !== false ? "on" : ""} onClick={() => set("is_published", true)}>Live</button>
          <button type="button" className={f.is_published === false ? "on" : ""} onClick={() => set("is_published", false)}>Hidden</button>
        </div>
      </Field>
    </Modal>
  );
}

/* ============================================================
   VIEW: COUPONS

   The discount a code is worth is never decided here — this
   screen only stores the rule. coupon_quote() in Postgres does
   the arithmetic, and the checkout and the order-creation
   function both read it, so what a student is shown and what
   they are charged cannot drift apart.
   ============================================================ */
function Coupons({ toast, askDelete }) {
  const [rows, setRows] = useState(null);
  const [bundles, setBundles] = useState([]);
  const [err, setErr] = useState("");
  const [reloadKey, setReloadKey] = useState(0);
  const [editing, setEditing] = useState(null);
  const [viewing, setViewing] = useState(null);
  const [q, setQ] = useState("");

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const [list, bs] = await Promise.all([
          DB.adminListCoupons(),
          DB.adminListBundles().catch(() => []),
        ]);
        if (!alive) return;
        setErr(""); setRows(list); setBundles(bs);
      } catch (e) {
        console.error(e);
        if (alive) { setErr(e?.message || "Couldn't load coupons."); setRows([]); }
      }
    })();
    return () => { alive = false; };
  }, [reloadKey]);

  const reload = () => setReloadKey((k) => k + 1);

  const save = async (c) => {
    try {
      await DB.upsertCoupon(c);
      toast(`${c.code.toUpperCase()} saved`);
      setEditing(null);
      reload();
    } catch (e) {
      console.error(e);
      const msg = /duplicate key|unique/i.test(e?.message || "")
        ? "That code already exists."
        : e?.message || "Couldn't save this coupon";
      toast(msg, "err");
    }
  };

  const toggleActive = async (c) => {
    try {
      await DB.upsertCoupon({ ...c, isActive: !c.isActive });
      toast(c.isActive ? `${c.code} switched off` : `${c.code} is live`);
      reload();
    } catch (e) { console.error(e); toast(e?.message || "Couldn't update", "err"); }
  };

  const remove = (c) => askDelete(
    c.usedCount > 0
      ? `Delete ${c.code}? It has been used ${c.usedCount} time${c.usedCount > 1 ? "s" : ""} — those redemption records go too. Switching it off instead keeps the history.`
      : `Delete ${c.code}? It has never been used, so nothing else changes.`,
    async () => {
      try { await DB.deleteCoupon(c.id); toast("Coupon deleted"); reload(); }
      catch (e) { console.error(e); toast(e?.message || "Couldn't delete", "err"); }
    },
  );

  if (err) return <div className="panel"><ErrorState message={err} onRetry={reload} /></div>;
  if (!rows) return <SkeletonCards count={3} height={120} />;

  if (viewing) {
    return <CouponRedemptions coupon={viewing} onBack={() => setViewing(null)} />;
  }

  const now = Date.now();
  const isLive = (c) => c.isActive
    && (!c.validUntil || new Date(c.validUntil).getTime() > now)
    && (c.maxUses === "" || c.maxUses == null || c.usedCount < c.maxUses);

  const needle = q.trim().toLowerCase();
  const shown = rows.filter((c) => !needle || c.code.toLowerCase().includes(needle) || c.description.toLowerCase().includes(needle));
  const live = rows.filter(isLive).length;
  const totalRedemptions = rows.reduce((a, c) => a + c.usedCount, 0);

  return (
    <div>
      <div className="stats">
        <StatCard icon={<Tag size={20} />} color={{ bg: "#faf2dc", fg: "#b8923a" }} n={rows.length}
                  label="Coupons" sub={`${live} live right now`} />
        <StatCard icon={<TrendingUp size={20} />} color={{ bg: "#e8f6ee", fg: "#1f8a4c" }} n={totalRedemptions}
                  label="Times redeemed" sub="paid orders only" />
      </div>

      <div className="banner">
        <AlertCircle size={17} />
        A code is only spent when a payment actually verifies — an abandoned checkout never burns a use.
      </div>

      <div className="sec-head">
        <div>
          <h2>{shown.length} coupon{shown.length !== 1 ? "s" : ""}</h2>
          <div className="note">Students apply these at checkout; the discount is computed server-side</div>
        </div>
        <div style={{ display: "flex", gap: 8, alignItems: "center", flexWrap: "wrap" }}>
          <div className="search"><Search size={15} /><input placeholder="Search codes…" value={q} onChange={(e) => setQ(e.target.value)} /></div>
          <button className="btn btn-primary" onClick={() => setEditing({
            code: "", description: "", discountType: "percent", discountValue: 10,
            maxDiscount: "", minOrder: "", planCodes: [], maxUses: "", maxUsesPerUser: 1,
            validUntil: "", isActive: true,
          })}><Plus size={16} />New coupon</button>
        </div>
      </div>

      {rows.length === 0 ? (
        <div className="panel"><Empty icon={<Tag size={26} />} title="No coupons yet"
          text="Create a code and students can apply it on the payment screen. The public site already tells them coupons exist." /></div>
      ) : shown.length === 0 ? (
        <div className="panel"><Empty icon={<Search size={26} />} title="No match" text={'Nothing matches "' + q + '".'} /></div>
      ) : (
        <div className="tbl-wrap">
          <table className="tbl">
            <thead><tr>
              <th>Code</th><th>Discount</th><th>Applies to</th><th>Used</th><th>Valid until</th>
              <th>Status</th><th style={{ textAlign: "right" }}>Actions</th>
            </tr></thead>
            <tbody>
              {shown.map((c) => {
                const expired = c.validUntil && new Date(c.validUntil).getTime() <= now;
                const exhausted = c.maxUses !== "" && c.maxUses != null && c.usedCount >= c.maxUses;
                return (
                  <tr key={c.id}>
                    <td>
                      <div style={{ fontWeight: 800, letterSpacing: ".06em", color: "var(--ink)" }}>{c.code}</div>
                      {c.description && <div className="q-sub">{c.description}</div>}
                    </td>
                    <td style={{ fontWeight: 700 }}>
                      {c.discountType === "percent" ? `${c.discountValue}%` : fmtINR(c.discountValue)}
                      {c.discountType === "percent" && c.maxDiscount !== "" && (
                        <div className="q-sub">max {fmtINR(c.maxDiscount)}</div>
                      )}
                    </td>
                    <td style={{ color: "var(--muted)", fontSize: 13 }}>
                      {c.planCodes.length === 0
                        ? "All bundles"
                        : c.planCodes.map((pc) => bundles.find((b) => b.code === pc)?.name || pc).join(", ")}
                    </td>
                    <td>
                      <button className="btn btn-ghost btn-sm" style={{ width: "auto" }}
                              onClick={() => setViewing(c)} disabled={c.usedCount === 0}>
                        {c.usedCount}{c.maxUses !== "" && c.maxUses != null ? ` / ${c.maxUses}` : ""}
                      </button>
                    </td>
                    <td style={{ color: expired ? "var(--red)" : "var(--muted)", fontSize: 13 }}>
                      {c.validUntil ? fmtLongDate(c.validUntil) : "No expiry"}
                    </td>
                    <td>
                      <button className="dot-pub" onClick={() => toggleActive(c)} title="Click to toggle">
                        <span className="dot" style={{ background: isLive(c) ? "var(--green)" : "#d2c6a8" }} />
                        <span style={{ color: isLive(c) ? "var(--green)" : "var(--muted)" }}>
                          {!c.isActive ? "Off" : expired ? "Expired" : exhausted ? "Used up" : "Live"}
                        </span>
                      </button>
                    </td>
                    <td><div className="row-actions">
                      <button className="btn-icon" title="Edit" onClick={() => setEditing(c)}><Pencil size={15} /></button>
                      <button className="btn-icon danger" title="Delete" onClick={() => remove(c)}><Trash2 size={15} /></button>
                    </div></td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}

      {editing && (
        <CouponForm initial={editing.id ? editing : null} value={editing} bundles={bundles}
                    onSave={save} onClose={() => setEditing(null)} />
      )}
    </div>
  );
}

function CouponForm({ initial, value, bundles, onSave, onClose }) {
  const [f, setF] = useState(() => ({ ...value }));
  const [err, setErr] = useState("");
  const set = (k, v) => setF((p) => ({ ...p, [k]: v }));
  const isNew = !initial;

  const togglePlan = (code) => {
    const next = f.planCodes.includes(code)
      ? f.planCodes.filter((c) => c !== code)
      : [...f.planCodes, code];
    set("planCodes", next);
  };

  const submit = () => {
    const code = String(f.code || "").trim().toUpperCase();
    if (!code) return setErr("A code is required — this is what students type.");
    if (!/^[A-Z0-9_-]{3,32}$/.test(code)) return setErr("Use 3–32 characters: letters, numbers, hyphen or underscore.");
    const v = Number(f.discountValue);
    if (!Number.isFinite(v) || v <= 0) return setErr("Enter a discount greater than zero.");
    if (f.discountType === "percent" && v > 100) return setErr("A percentage discount can't exceed 100%.");
    if (Number(f.maxUsesPerUser || 1) < 1) return setErr("Each student must be allowed at least one use.");
    setErr("");
    onSave({ ...f, code, discountValue: v });
  };

  return (
    <Modal
      title={isNew ? "New coupon" : `Edit ${f.code}`}
      onClose={onClose}
      wide
      footer={<>
        <button className="btn btn-ghost" onClick={onClose}>Cancel</button>
        <button className="btn btn-primary" onClick={submit}><Save size={16} />Save coupon</button>
      </>}
    >
      {err && <div className="form-err"><AlertCircle size={17} />{err}</div>}

      <div className="field-row">
        <Field label="Code" req hint="Students type this at checkout. Case doesn't matter to them.">
          <input className="inp" value={f.code} placeholder="WELCOME10"
                 style={{ textTransform: "uppercase", letterSpacing: ".06em", fontWeight: 700 }}
                 onChange={(e) => set("code", e.target.value.toUpperCase())} />
        </Field>
        <Field label="Internal note" hint="Only you see this.">
          <input className="inp" value={f.description} placeholder="Diwali campaign"
                 onChange={(e) => set("description", e.target.value)} />
        </Field>
      </div>

      <div className="field-row">
        <Field label="Discount type" req>
          <div className="seg">
            <button type="button" className={f.discountType === "percent" ? "on" : ""}
                    onClick={() => set("discountType", "percent")}>Percentage</button>
            <button type="button" className={f.discountType === "flat" ? "on" : ""}
                    onClick={() => set("discountType", "flat")}>Flat ₹</button>
          </div>
        </Field>
        <Field label={f.discountType === "percent" ? "Percent off" : "Rupees off"} req>
          <input className="inp" type="number" min="1" value={f.discountValue}
                 onChange={(e) => set("discountValue", e.target.value)} />
        </Field>
      </div>

      {f.discountType === "percent" && (
        <Field label="Cap the discount (₹)"
               hint="Optional. 25% off with a ₹100 cap never takes more than ₹100, whatever the bundle costs.">
          <input className="inp" type="number" min="0" value={f.maxDiscount}
                 onChange={(e) => set("maxDiscount", e.target.value)} />
        </Field>
      )}

      <Field label="Applies to" hint="Leave all unticked for every bundle.">
        <div className="chip-pick">
          {bundles.length === 0 && <span className="hint">No bundles yet.</span>}
          {bundles.map((b) => (
            <button type="button" key={b.code}
                    className={"chip-opt" + (f.planCodes.includes(b.code) ? " on" : "")}
                    onClick={() => togglePlan(b.code)}>
              {f.planCodes.includes(b.code) && <Check size={13} />}{b.name}
            </button>
          ))}
        </div>
      </Field>

      <div className="field-row">
        <Field label="Total uses" hint="Blank = unlimited.">
          <input className="inp" type="number" min="1" value={f.maxUses}
                 onChange={(e) => set("maxUses", e.target.value)} />
        </Field>
        <Field label="Uses per student" hint="Usually 1.">
          <input className="inp" type="number" min="1" value={f.maxUsesPerUser}
                 onChange={(e) => set("maxUsesPerUser", e.target.value)} />
        </Field>
      </div>

      <div className="field-row">
        <Field label="Minimum order (₹)" hint="Blank or 0 = no minimum.">
          <input className="inp" type="number" min="0" value={f.minOrder}
                 onChange={(e) => set("minOrder", e.target.value)} />
        </Field>
        <Field label="Valid until" hint="Blank = never expires.">
          <input className="inp" type="date"
                 value={f.validUntil ? String(f.validUntil).slice(0, 10) : ""}
                 onChange={(e) => set("validUntil", e.target.value)} />
        </Field>
      </div>

      <Field label="Status">
        <div className="seg">
          <button type="button" className={f.isActive !== false ? "on" : ""} onClick={() => set("isActive", true)}>Live</button>
          <button type="button" className={f.isActive === false ? "on" : ""} onClick={() => set("isActive", false)}>Off</button>
        </div>
      </Field>
    </Modal>
  );
}

function CouponRedemptions({ coupon, onBack }) {
  const [rows, setRows] = useState(null);
  const [err, setErr] = useState("");

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const r = await DB.couponRedemptions(coupon.id);
        if (alive) { setErr(""); setRows(r); }
      } catch (e) {
        console.error(e);
        if (alive) { setErr(e?.message || "Couldn't load redemptions."); setRows([]); }
      }
    })();
    return () => { alive = false; };
  }, [coupon.id]);

  const total = (rows ?? []).reduce((a, r) => a + r.discount, 0);

  return (
    <div>
      <button className="btn btn-ghost btn-sm" onClick={onBack} style={{ marginBottom: 16 }}>
        <ArrowLeft size={15} />Back to coupons
      </button>

      <div className="sec-head">
        <div>
          <h2>{coupon.code}</h2>
          <div className="note">
            {coupon.usedCount} redemption{coupon.usedCount === 1 ? "" : "s"}
            {rows ? ` · ${fmtINR(total)} given away` : ""}
          </div>
        </div>
      </div>

      {err ? <div className="panel"><ErrorState message={err} /></div>
        : rows === null ? <SkeletonCards count={2} height={90} />
        : rows.length === 0 ? (
          <div className="panel"><Empty icon={<Tag size={26} />} title="Not used yet"
            text="Redemptions appear here once a student pays with this code." /></div>
        ) : (
          <div className="tbl-wrap">
            <table className="tbl">
              <thead><tr><th>Student</th><th>Discount</th><th>When</th></tr></thead>
              <tbody>
                {rows.map((r) => (
                  <tr key={r.id}>
                    <td><div style={{ fontWeight: 700, color: "var(--ink)" }}>{r.name}</div><div className="q-sub">{r.email}</div></td>
                    <td style={{ fontWeight: 800, color: "var(--green)" }}>−{fmtINR(r.discount)}</td>
                    <td style={{ color: "var(--muted)", fontSize: 13 }}>{fmtLongDate(r.at)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
    </div>
  );
}

/* ============================================================
   VIEW: STUDENTS  —  real registered learners
   ============================================================ */
function Students({ toast }) {
  const [rows, setRows] = useState(null);
  const [err, setErr] = useState("");
  const [q, setQ] = useState("");
  const [filter, setFilter] = useState("all"); // all | enrolled | free

  const load = useCallback(async () => {
    setErr("");
    try { setRows(await DB.adminStudents()); }
    catch (e) { console.error(e); setErr(e?.message || "Could not load students."); }
  }, []);
  useEffect(() => { load(); }, [load]);

  if (err) return <div className="panel"><ErrorState message={err} onRetry={load} /></div>;
  if (!rows) return <SkeletonCards count={3} height={120} />;

  const needle = q.trim().toLowerCase();
  const shown = rows.filter((r) => {
    if (filter === "enrolled" && !r.enrolled) return false;
    if (filter === "free" && r.enrolled) return false;
    if (!needle) return true;
    return r.name.toLowerCase().includes(needle)
      || r.email.toLowerCase().includes(needle)
      || (r.phone || "").includes(needle);
  });

  const enrolled = rows.filter((r) => r.enrolled).length;
  const active = rows.filter((r) => r.attempts > 0).length;

  const exportCsv = () => {
    const head = ["Name", "Email", "Phone", "Target", "Enrolled", "Tests attempted", "Avg %", "Joined"];
    const body = shown.map((r) => [r.name, r.email, r.phone, r.target, r.enrolled ? "Yes" : "No", r.attempts, r.avg, fmtLongDate(r.joined)]);
    downloadCsv("junoonias-students.csv", [head, ...body]);
    toast?.(shown.length + " student" + (shown.length === 1 ? "" : "s") + " exported");
  };

  return (
    <div>
      <div className="stats">
        <StatCard icon={<Users size={20} />} color={{ bg: "#faf2dc", fg: "#b8923a" }} n={rows.length} label="Registered" sub="total accounts" />
        <StatCard icon={<GraduationCap size={20} />} color={{ bg: "#e8f6ee", fg: "#1f8a4c" }} n={enrolled} label="Paid & active"
                  sub={rows.length ? Math.round((enrolled / rows.length) * 100) + "% conversion" : "—"} />
        <StatCard icon={<TrendingUp size={20} />} color={{ bg: "#fcf3df", fg: "#d4a64a" }} n={active} label="Have attempted a test" sub="engaged learners" />
      </div>

      <div className="sec-head">
        <div><h2>{shown.length} student{shown.length !== 1 ? "s" : ""}</h2><div className="note">Everyone who has created an account</div></div>
        <div style={{ display: "flex", gap: 8, alignItems: "center", flexWrap: "wrap" }}>
          <div className="search"><Search size={15} /><input placeholder="Name, email or phone…" value={q} onChange={(e) => setQ(e.target.value)} /></div>
          <select className="sel" value={filter} onChange={(e) => setFilter(e.target.value)}>
            <option value="all">All students</option>
            <option value="enrolled">Paid only</option>
            <option value="free">Not yet paid</option>
          </select>
          <button className="btn btn-ghost btn-sm" onClick={exportCsv} disabled={shown.length === 0}><Download size={15} />Export CSV</button>
        </div>
      </div>

      {rows.length === 0 ? (
        <div className="panel"><Empty icon={<Users size={26} />} title="No students yet"
             text="Accounts appear here the moment your first aspirant signs up." /></div>
      ) : shown.length === 0 ? (
        <div className="panel"><Empty icon={<Search size={26} />} title="No match" text={'Nothing matches "' + q + '".'} /></div>
      ) : (
        <div className="tbl-wrap">
          <table className="tbl">
            <thead><tr><th>Student</th><th>Contact</th><th>Access</th><th>Tests</th><th>Avg. score</th><th>Joined</th></tr></thead>
            <tbody>
              {shown.map((s) => (
                <tr key={s.id}>
                  <td><div style={{ display: "flex", alignItems: "center", gap: 10 }}>
                    <span style={{ width: 32, height: 32, borderRadius: 8, background: "#b8923a", color: "#fff", display: "grid", placeItems: "center", fontSize: 12, fontWeight: 800, flex: "0 0 auto" }}>{initials(s.name)}</span>
                    <div style={{ minWidth: 0 }}>
                      <div style={{ fontWeight: 700, color: "var(--ink)" }}>{s.name}</div>
                      <div className="q-sub">{s.target}</div>
                    </div>
                  </div></td>
                  <td style={{ color: "var(--muted)", fontSize: 13 }}>{s.email}{s.phone ? <div>{s.phone}</div> : null}</td>
                  <td>
                    <Badge color={s.enrolled ? { bg: "#e8f6ee", fg: "#1f8a4c" } : { bg: "#fdf6e3", fg: "#a89474" }}>
                      {s.enrolled ? "Enrolled" : "Free"}
                    </Badge>
                  </td>
                  <td>{s.attempts}</td>
                  <td>{s.attempts === 0
                    ? <span style={{ color: "var(--muted)" }}>—</span>
                    : <span style={{ fontWeight: 800, color: s.avg >= 70 ? "var(--green)" : s.avg >= 50 ? "var(--amber)" : "var(--red)" }}>{s.avg}%</span>}</td>
                  <td style={{ color: "var(--muted)", fontSize: 13 }}>{fmtLongDate(s.joined)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

/* ============================================================
   VIEW: SALES  —  verified Razorpay transactions
   ============================================================ */
function Feedback({ toast }) {
  const [rows, setRows] = useState(null);
  const [err, setErr] = useState("");
  const [filter, setFilter] = useState("open");
  const [open, setOpen] = useState(null);
  const [reply, setReply] = useState("");
  const [status, setStatus] = useState("seen");
  const [saving, setSaving] = useState(false);

  const load = useCallback(async () => {
    setErr("");
    try { setRows(await DB.adminFeedback()); }
    catch (e) { console.error(e); setErr(e?.message || "Could not load feedback."); }
  }, []);
  useEffect(() => { load(); }, [load]);

  if (err) return <div className="panel"><ErrorState message={err} onRetry={load} /></div>;
  if (!rows) return <SkeletonCards count={3} height={110} />;

  const OPEN = ["new", "seen", "in_progress"];
  const shown = filter === "all" ? rows
    : filter === "open" ? rows.filter((r) => OPEN.includes(r.status))
    : rows.filter((r) => r.status === filter);

  const counts = {
    all: rows.length,
    open: rows.filter((r) => OPEN.includes(r.status)).length,
    resolved: rows.filter((r) => r.status === "resolved").length,
  };
  const rated = rows.filter((r) => r.rating);
  const avg = rated.length ? (rated.reduce((a, r) => a + r.rating, 0) / rated.length) : 0;

  const kindColor = {
    bug: { bg: "#fbeaea", fg: "#c0392b" },
    content: { bg: "#faf2dc", fg: "#b8923a" },
    test: { bg: "#f6ecd2", fg: "#7a1f1f" },
    payment: { bg: "#e8f6ee", fg: "#1f8a4c" },
    suggestion: { bg: "#eef2fb", fg: "#3a5ba0" },
    general: { bg: "#fdf6e3", fg: "#a89474" },
  };
  const statusColor = {
    new: { bg: "#fbeaea", fg: "#c0392b" },
    seen: { bg: "#fdf6e3", fg: "#a89474" },
    in_progress: { bg: "#faf2dc", fg: "#b8923a" },
    resolved: { bg: "#e8f6ee", fg: "#1f8a4c" },
    wont_fix: { bg: "#f4efe4", fg: "#8a7a6c" },
  };

  const startReply = (r) => { setOpen(r); setReply(r.reply || ""); setStatus(r.status === "new" ? "seen" : r.status); };

  const save = async () => {
    if (!open) return;
    setSaving(true);
    try {
      await DB.updateFeedback(open.id, { status, reply: reply.trim() || null });
      toast?.("Reply saved — the student sees it on their Feedback screen");
      setOpen(null);
      await load();
    } catch (e) {
      console.error(e);
      toast?.("Could not save that reply", "err");
    } finally { setSaving(false); }
  };

  return (
    <div>
      <div className="stats">
        <StatCard icon={<MessageSquare size={20} />} color={{ bg: "#fbeaea", fg: "#c0392b" }}
                  n={counts.open} label="Waiting on you" sub="new, read or in progress" />
        <StatCard icon={<CheckCircle2 size={20} />} color={{ bg: "#e8f6ee", fg: "#1f8a4c" }}
                  n={counts.resolved} label="Resolved" sub="closed with a reply" />
        <StatCard icon={<Star size={20} />} color={{ bg: "#faf2dc", fg: "#b8923a" }}
                  n={avg ? avg.toFixed(1) : "—"} label="Average rating"
                  sub={rated.length + " rated"} />
      </div>

      <div className="sec-head">
        <div><h2>Student feedback</h2><div className="note">Oldest open items first deserve your attention</div></div>
        <div className="tabs">
          {[["open", "Open"], ["resolved", "Resolved"], ["all", "All"]].map(([k, label]) => (
            <button key={k} className={"tab" + (filter === k ? " active" : "")} onClick={() => setFilter(k)}>
              {label} ({counts[k] ?? 0})
            </button>
          ))}
        </div>
      </div>

      {shown.length === 0 ? (
        <div className="panel">
          <Empty icon={<MessageSquare size={26} />} title="Nothing here"
                 text="When a student sends feedback from their dashboard it lands in this queue." />
        </div>
      ) : shown.map((r) => (
        <div className="panel panel-pad" key={r.id} style={{ marginBottom: 12 }}>
          <div style={{ display: "flex", alignItems: "center", gap: 9, flexWrap: "wrap", marginBottom: 9 }}>
            <Badge color={statusColor[r.status] || statusColor.new}>{r.status.replace(/_/g, " ")}</Badge>
            <Badge color={kindColor[r.kind] || kindColor.general}>{r.kind}</Badge>
            {r.rating ? (
              <span style={{ fontSize: 12.5, color: "#b8923a", fontWeight: 700 }}>{"★".repeat(r.rating)}</span>
            ) : null}
            <span style={{ fontSize: 12.5, color: "var(--muted)", marginLeft: "auto" }}>{fmtLongDate(r.at)}</span>
          </div>

          <p style={{ margin: "0 0 10px", fontSize: 14, lineHeight: 1.65, color: "var(--ink)" }}>{r.message}</p>

          <div style={{ display: "flex", alignItems: "center", gap: 10, flexWrap: "wrap" }}>
            <span style={{ fontSize: 12.5, color: "var(--muted)" }}>
              {r.name} · {r.email}{r.page ? " · " + r.page : ""}
            </span>
            <button className="btn btn-ghost btn-sm" style={{ marginLeft: "auto" }} onClick={() => startReply(r)}>
              {r.reply ? "Edit reply" : "Reply"}
            </button>
          </div>

          {r.reply && (
            <div style={{ marginTop: 11, padding: "11px 13px", borderRadius: 10, background: "#f3f8f4",
                          border: "1px solid #d8eadd", fontSize: 13, lineHeight: 1.6, color: "#1f5c39" }}>
              <b style={{ display: "block", fontSize: 11.5, letterSpacing: ".06em", textTransform: "uppercase",
                          color: "#2f9e58", marginBottom: 4 }}>Your reply</b>
              {r.reply}
            </div>
          )}
        </div>
      ))}

      {open && (
        <Modal title="Reply to this student" onClose={() => setOpen(null)}
               footer={
                 <>
                   <button className="btn btn-ghost" onClick={() => setOpen(null)}>Cancel</button>
                   <button className="btn btn-primary" onClick={save} disabled={saving}>
                     {saving ? "Saving…" : "Save reply"}
                   </button>
                 </>
               }>
          <p style={{ margin: "0 0 14px", fontSize: 13.5, lineHeight: 1.65, color: "var(--muted)" }}>
            {open.message}
          </p>
          <Field label="Status">
            <select className="sel" value={status} onChange={(e) => setStatus(e.target.value)}>
              <option value="seen">Read</option>
              <option value="in_progress">Being fixed</option>
              <option value="resolved">Resolved</option>
              <option value="wont_fix">Closed — not changing this</option>
            </select>
          </Field>
          <Field label="Reply" hint="The student sees this on their own Feedback screen">
            <textarea className="inp" rows={4} value={reply} onChange={(e) => setReply(e.target.value)}
                      placeholder="What you did about it, or why not." />
          </Field>
        </Modal>
      )}
    </div>
  );
}

function Referrals() {
  const [rows, setRows] = useState(null);
  const [err, setErr] = useState("");
  const [q, setQ] = useState("");

  const load = useCallback(async () => {
    setErr("");
    try { setRows(await DB.adminReferrals()); }
    catch (e) { console.error(e); setErr(e?.message || "Could not load referrals."); }
  }, []);
  useEffect(() => { load(); }, [load]);

  if (err) return <div className="panel"><ErrorState message={err} onRetry={load} /></div>;
  if (!rows) return <SkeletonCards count={3} height={120} />;

  const needle = q.trim().toLowerCase();
  const shown = !needle ? rows : rows.filter((r) =>
    r.referrer.toLowerCase().includes(needle) || r.referrerEmail.toLowerCase().includes(needle)
    || r.referred.toLowerCase().includes(needle) || r.referredEmail.toLowerCase().includes(needle)
    || r.code.toLowerCase().includes(needle));

  const converted = rows.filter((r) => r.paid).length;
  const rate = rows.length ? Math.round((converted / rows.length) * 100) : 0;

  // Who is actually driving signups. Worth watching for the same name topping
  // the list with nobody ever converting — that pattern is what fake-account
  // farming looks like from here.
  const byReferrer = new Map();
  rows.forEach((r) => {
    const cur = byReferrer.get(r.referrerEmail) || { name: r.referrer, n: 0, paid: 0 };
    cur.n += 1;
    if (r.paid) cur.paid += 1;
    byReferrer.set(r.referrerEmail, cur);
  });
  const top = [...byReferrer.entries()].sort((a, b) => b[1].n - a[1].n).slice(0, 5);

  const exportCsv = () => {
    const head = ["Date", "Referrer", "Referrer email", "Invitee", "Invitee email", "Code", "Paid", "Bonus status"];
    const body = shown.map((r) => [fmtLongDate(r.at), r.referrer, r.referrerEmail, r.referred, r.referredEmail, r.code, r.paid ? "yes" : "no", r.status]);
    downloadCsv("junoonias-referrals.csv", [head, ...body]);
  };

  return (
    <div>
      <div className="stats">
        <StatCard icon={<Gift size={20} />} color={{ bg: "#f6ecd2", fg: "#7a1f1f" }} n={rows.length} label="Referral signups" sub="accounts bound to a link" />
        <StatCard icon={<CheckCircle2 size={20} />} color={{ bg: "#e8f6ee", fg: "#1f8a4c" }} n={converted} label="Converted to paid" sub="the ones that earn a bonus" />
        <StatCard icon={<TrendingUp size={20} />} color={{ bg: "#faf2dc", fg: "#b8923a" }} n={rate + "%"} label="Conversion rate" sub="invitee signup to purchase" />
      </div>

      {top.length > 0 && (
        <div className="panel panel-pad" style={{ marginBottom: 16 }}>
          <div className="note" style={{ marginBottom: 10 }}>Top referrers</div>
          {top.map(([email, v]) => (
            <div key={email} style={{ display: "flex", alignItems: "center", gap: 12, padding: "9px 0", borderBottom: "1px solid var(--line)" }}>
              <div style={{ flex: 1, minWidth: 0 }}>
                <div style={{ fontWeight: 700, color: "var(--ink)" }}>{v.name}</div>
                <div className="q-sub">{email}</div>
              </div>
              <div style={{ fontSize: 13, color: "var(--muted)" }}>{v.n} invited</div>
              <Badge color={v.paid > 0 ? { bg: "#e8f6ee", fg: "#1f8a4c" } : { bg: "#fdf6e3", fg: "#a89474" }}>{v.paid} paid</Badge>
            </div>
          ))}
        </div>
      )}

      <div className="sec-head">
        <div><h2>All referrals</h2><div className="note">Bound once at signup from the invite link, and never editable afterwards</div></div>
        <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
          <div className="lb-search" style={{ minWidth: 210 }}><Search size={15} /><input placeholder="Name, email or code…" value={q} onChange={(e) => setQ(e.target.value)} /></div>
          <button className="btn btn-ghost btn-sm" onClick={exportCsv} disabled={shown.length === 0}><Download size={15} />Export CSV</button>
        </div>
      </div>

      {shown.length === 0 ? (
        <div className="panel">
          <Empty icon={<Gift size={26} />} title={rows.length === 0 ? "No referrals yet" : "Nothing matches that search"}
                 text={rows.length === 0
                   ? "Students each get an invite link on their dashboard. Anyone who signs up through one appears here, bound to the referrer permanently."
                   : "Try a different name, email or code."} />
        </div>
      ) : (
        <div className="tbl-wrap">
          <table className="tbl">
            <thead><tr><th>Referrer</th><th>Invitee</th><th>Code</th><th>Bought</th><th>Bonus</th><th>Joined</th></tr></thead>
            <tbody>
              {shown.map((r) => (
                <tr key={r.id}>
                  <td><div style={{ fontWeight: 700, color: "var(--ink)" }}>{r.referrer}</div><div className="q-sub">{r.referrerEmail}</div></td>
                  <td><div style={{ fontWeight: 700, color: "var(--ink)" }}>{r.referred}</div><div className="q-sub">{r.referredEmail}</div></td>
                  <td style={{ fontFamily: "ui-monospace,monospace", fontSize: 13, letterSpacing: ".05em" }}>{r.code}</td>
                  <td>{r.paid
                    ? <Badge color={{ bg: "#e8f6ee", fg: "#1f8a4c" }}>Yes</Badge>
                    : <Badge color={{ bg: "#fdf6e3", fg: "#a89474" }}>Not yet</Badge>}</td>
                  <td style={{ color: "var(--muted)", fontSize: 13, textTransform: "capitalize" }}>{r.status}</td>
                  <td style={{ color: "var(--muted)", fontSize: 13 }}>{fmtLongDate(r.at)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

function Sales({ toast }) {
  const [rows, setRows] = useState(null);
  const [err, setErr] = useState("");
  const [range, setRange] = useState("all"); // all | 30d | 7d

  const load = useCallback(async () => {
    setErr("");
    try { setRows(await DB.adminPayments()); }
    catch (e) { console.error(e); setErr(e?.message || "Could not load transactions."); }
  }, []);
  useEffect(() => { load(); }, [load]);

  if (err) return <div className="panel"><ErrorState message={err} onRetry={load} /></div>;
  if (!rows) return <SkeletonCards count={3} height={120} />;

  const cutoff = range === "7d" ? Date.now() - 7 * 86400000 : range === "30d" ? Date.now() - 30 * 86400000 : 0;
  const shown = rows.filter((r) => new Date(r.date).getTime() >= cutoff);
  const paid = shown.filter((p) => p.status === "paid");
  const revenue = paid.reduce((s, p) => s + p.amount, 0);
  const failed = shown.filter((p) => p.status === "failed").length;
  const successRate = shown.length ? Math.round((paid.length / shown.length) * 100) : 0;

  const byDay = {};
  paid.forEach((p) => {
    const k = String(p.date).slice(0, 10);
    byDay[k] = (byDay[k] || 0) + p.amount;
  });
  const trend = Object.entries(byDay).sort().slice(-30).map(([d, v]) => ({ name: d.slice(5), value: v }));

  const exportCsv = () => {
    const head = ["Date", "Student", "Email", "Plan", "Amount", "Status", "Method", "Payment ID"];
    const body = shown.map((p) => [fmtLongDate(p.date), p.name, p.email, p.item, p.amount, p.status, p.method, p.ref]);
    downloadCsv("junoonias-transactions.csv", [head, ...body]);
    toast?.(shown.length + " transaction" + (shown.length === 1 ? "" : "s") + " exported");
  };

  const statusColor = {
    paid: { bg: "#e8f6ee", fg: "#1f8a4c" },
    failed: { bg: "#fbeaea", fg: "#c0392b" },
    created: { bg: "#fdf6e3", fg: "#a89474" },
    refunded: { bg: "#f6ecd2", fg: "#7a1f1f" },
  };

  return (
    <div>
      <div className="stats">
        <StatCard icon={<IndianRupee size={20} />} color={{ bg: "#e8f6ee", fg: "#1f8a4c" }} n={fmtINR(revenue)} label="Revenue"
                  sub={paid.length + " successful payment" + (paid.length === 1 ? "" : "s")} />
        <StatCard icon={<TrendingUp size={20} />} color={{ bg: "#faf2dc", fg: "#b8923a" }} n={successRate + "%"} label="Success rate"
                  sub={failed + " failed attempt" + (failed === 1 ? "" : "s")} />
        <StatCard icon={<Users size={20} />} color={{ bg: "#fcf3df", fg: "#d4a64a" }} n={new Set(paid.map((p) => p.email)).size} label="Paying students" sub="unique buyers" />
      </div>

      <div className="sec-head">
        <div><h2>Transactions</h2><div className="note">Every Razorpay order, verified server-side</div></div>
        <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
          <select className="sel" value={range} onChange={(e) => setRange(e.target.value)}>
            <option value="all">All time</option>
            <option value="30d">Last 30 days</option>
            <option value="7d">Last 7 days</option>
          </select>
          <button className="btn btn-ghost btn-sm" onClick={exportCsv} disabled={shown.length === 0}><Download size={15} />Export CSV</button>
        </div>
      </div>

      {trend.length > 1 && (
        <div className="panel panel-pad" style={{ marginBottom: 16 }}>
          <div className="note" style={{ marginBottom: 10 }}>Daily revenue</div>
          <div style={{ height: 190 }}>
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={trend} margin={{ top: 8, right: 8, left: -14, bottom: 0 }}>
                <defs>
                  <linearGradient id="adRev" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stopColor="#1f8a4c" stopOpacity={0.28} />
                    <stop offset="100%" stopColor="#1f8a4c" stopOpacity={0} />
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f3e8d0" />
                <XAxis dataKey="name" tick={{ fontSize: 11, fill: "var(--muted)" }} axisLine={false} tickLine={false} />
                <YAxis tick={{ fontSize: 11, fill: "#bcae94" }} axisLine={false} tickLine={false} />
                <Tooltip formatter={(v) => [fmtINR(v), "Revenue"]} contentStyle={{ borderRadius: 10, border: "1px solid var(--line)", fontSize: 13 }} />
                <Area dataKey="value" stroke="#1f8a4c" strokeWidth={2.5} fill="url(#adRev)" />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>
      )}

      {shown.length === 0 ? (
        <div className="panel">
          <Empty icon={<IndianRupee size={26} />} title="No transactions yet"
                 text="Payments appear here as soon as your first student joins. Every row is written by the Razorpay webhook — never by the browser." />
        </div>
      ) : (
        <div className="tbl-wrap">
          <table className="tbl">
            <thead><tr><th>Student</th><th>Plan</th><th>Amount</th><th>Status</th><th>Method</th><th>Date</th></tr></thead>
            <tbody>
              {shown.map((p) => (
                <tr key={p.id}>
                  <td><div style={{ fontWeight: 700, color: "var(--ink)" }}>{p.name}</div><div className="q-sub">{p.email}</div></td>
                  <td style={{ color: "var(--muted)" }}>{p.item}</td>
                  <td style={{ fontWeight: 800 }}>{fmtINR(p.amount)}</td>
                  <td><Badge color={statusColor[p.status] || statusColor.created}>{p.status}</Badge></td>
                  <td style={{ color: "var(--muted)", fontSize: 13, textTransform: "capitalize" }}>{p.method}</td>
                  <td style={{ color: "var(--muted)", fontSize: 13 }}>{fmtLongDate(p.date)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

/* Client-side CSV export — no server round trip, no library. */
function downloadCsv(filename, rows) {
  const esc = (v) => {
    const s = String(v ?? "");
    return /[",\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
  };
  const csv = rows.map((r) => r.map(esc).join(",")).join("\n");
  // The BOM makes Excel read UTF-8 (₹ and Devanagari names) correctly.
  const blob = new Blob(["﻿" + csv], { type: "text/csv;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url; a.download = filename;
  document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}


return App;
})();

export default AdminApp;
