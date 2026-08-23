import React, { useState, useEffect, useRef, useMemo } from "react";
import { AlertCircle, Trophy } from "lucide-react";
import { RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell, LabelList } from "recharts";
import { DiyaLogo } from "../ui/Brand.jsx";
import { ChromeControls } from "../lib/i18n.jsx";
import { useLang } from "../lib/contexts.js";
import { loadExamTest, submitAttempt, currentUser, getProfile } from "../lib/db.js";


const ExamApp = (() => {
/* ============================================================
   THE PAPER
   The exam is no longer a hardcoded constant. `ExamApp` loads the
   real test (and its questions) from the question bank and puts it
   on this context, so every screen below reads the same paper.
   ============================================================ */
const ExamCtx = React.createContext(null);
const useExam = () => React.useContext(ExamCtx);

/* ============================================================
   HELPERS
   ============================================================ */
const fmt = (s) => {
  s = Math.max(0, Math.round(s));
  const h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), sec = s % 60;
  const pad = (n) => String(n).padStart(2, "0");
  return h > 0 ? `${pad(h)}:${pad(m)}:${pad(sec)}` : `${pad(m)}:${pad(sec)}`;
};
const hasAnswer = (a) => {
  if (a === undefined || a === null) return false;
  if (Array.isArray(a)) return a.length > 0;
  if (typeof a === "string") return a.trim() !== "";
  return true;
};
const estPercentile = (p) => {
  const pts = [[0, 1], [20, 16], [35, 36], [50, 56], [60, 71], [72, 84], [82, 92], [90, 97], [100, 99.6]];
  for (let i = 0; i < pts.length - 1; i++) {
    if (p >= pts[i][0] && p <= pts[i + 1][0]) {
      const [x0, y0] = pts[i], [x1, y1] = pts[i + 1];
      return y0 + ((y1 - y0) * (p - x0)) / (x1 - x0);
    }
  }
  return p <= 0 ? 1 : 99.6;
};
const gradeFor = (p) => {
  if (p >= 85) return { g: "A+", c: "#1f8a4c" };
  if (p >= 70) return { g: "A", c: "#2f9e58" };
  if (p >= 55) return { g: "B", c: "#d4a64a" };
  if (p >= 40) return { g: "C", c: "#a8842f" };
  return { g: "D", c: "#c0392b" };
};
const SEM = { strong: "#1f8a4c", average: "#b8923a", weak: "#c0392b" };
// bandFor moved to the server with the rest of the scoring.

/* ============================================================
   STYLES (self-contained design system)
   ============================================================ */
const CSS = `
:root{
  --navy:#b8923a; --navy-2:#5b1414; --gold:#d4a64a;
  --bg:#fdf6e3; --card:#ffffff; --ink:#2a1810; --muted:#7a6450; --line:#e8dcc0;
  --green:#1f8a4c; --amber:#b8923a; --red:#c0392b;
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
.ee-root{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--ink);
  font-variant-numeric:tabular-nums;line-height:1.5;background:var(--bg);min-height:100%;}
.ee-root :where(button){font-family:inherit;cursor:pointer;border:none;background:none}
.ee-wrap{max-width:1180px;margin:0 auto;padding:0 16px}

/* ---------- INSTRUCTIONS ---------- */
.inst{max-width:860px;margin:0 auto;padding:28px 16px 60px}
.inst-card{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:0 1px 3px rgba(20,120,140,.06)}
.inst-head{background:linear-gradient(135deg,#8a2222,#b8923a);color:#ffffff;padding:22px 26px}
.inst-eyebrow{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:#f1e4c4;font-weight:700}
.inst-title{font-size:22px;font-weight:800;margin:6px 0 0;letter-spacing:-.01em}
.inst-meta{display:flex;flex-wrap:wrap;gap:8px 24px;margin-top:14px;font-size:13px;color:#f1e4c4}
.inst-meta b{color:#ffffff}
.inst-body{padding:24px 26px}
.inst-h{font-size:13px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;color:var(--navy);margin:22px 0 10px}
.inst-h:first-child{margin-top:0}
.inst-list{margin:0;padding-left:18px;font-size:14.5px;color:#4a3322}
.inst-list li{margin:7px 0}
.legend-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:10px;margin-top:6px}
.legend-row{display:flex;align-items:center;gap:10px;font-size:13.5px;color:#4a3322}
.consent{display:flex;gap:12px;align-items:flex-start;margin-top:26px;padding:16px;background:#f7efdd;border:1px solid #ece2cc;border-radius:10px}
.consent input{width:18px;height:18px;margin-top:2px;accent-color:var(--navy);cursor:pointer;flex:0 0 auto}
.consent label{font-size:14px;color:#4a3322;cursor:pointer}
.begin-row{margin-top:22px}
.begin-btn{background:var(--green);color:#ffffff;font-weight:700;font-size:15px;padding:13px 28px;border-radius:10px;transition:.15s}
.begin-btn:disabled{background:#c6b896;cursor:not-allowed}
.begin-btn:not(:disabled):hover{background:#1a7a42}

.ee-blocker{position:fixed;inset:0;z-index:120;display:grid;place-items:center;
  background:rgba(28,18,10,.55);backdrop-filter:blur(3px);padding:20px}
.ee-blocker-card{background:var(--card,#fff);border-radius:16px;padding:26px 28px;max-width:400px;
  display:flex;flex-direction:column;gap:7px;text-align:center;align-items:center;
  box-shadow:0 20px 60px rgba(0,0,0,.3);font-size:13.5px;line-height:1.55}
.ee-blocker-card b{font-size:16px}
.ee-spin{width:30px;height:30px;border-radius:50%;border:3px solid #e8d9b8;border-top-color:#8a2222;
  animation:ee-rot .8s linear infinite;margin-bottom:6px}
@keyframes ee-rot{to{transform:rotate(360deg)}}

/* ---------- EXAM SHELL ---------- */
.exam-head{background:linear-gradient(110deg,#c39d44,#8a6a14);color:#ffffff;position:sticky;top:0;z-index:20}
.exam-head-in{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:10px 18px;max-width:1280px;margin:0 auto}
.cand{display:flex;align-items:center;gap:12px;min-width:0}
.cand-av{width:38px;height:38px;border-radius:8px;background:#8a6a14;display:grid;place-items:center;font-weight:800;font-size:15px;flex:0 0 auto}
.cand-name{font-weight:700;font-size:14.5px;line-height:1.15;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cand-sub{font-size:11.5px;color:#f1e4c4}
.timer-box{display:flex;align-items:center;gap:10px;background:#5b1414;border:1px solid #8a6a14;padding:7px 14px;border-radius:10px}
.timer-box.danger{background:#7a1f1f;border-color:#a32f24;animation:pulse 1s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.72}}
.timer-label{font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:#fffaef}
.timer-box.danger .timer-label{color:#f3c9c9}
.timer-val{font-size:19px;font-weight:800;font-variant-numeric:tabular-nums;letter-spacing:.02em}

.sec-tabs{background:#5b1414;border-top:1px solid #8a6a14}
.sec-tabs-in{display:flex;gap:0;max-width:1280px;margin:0 auto;padding:0 10px;overflow-x:auto}
.sec-tab{padding:11px 20px;color:#f1e4c4;font-size:13.5px;font-weight:700;border-bottom:3px solid transparent;white-space:nowrap;transition:.15s}
.sec-tab.active{color:#ffffff;border-bottom-color:var(--gold);background:rgba(255,255,255,.04)}
.sec-tab:hover:not(.active){color:#f1e4c4}

.exam-body{display:grid;grid-template-columns:1fr 296px;gap:18px;max-width:1280px;margin:0 auto;padding:18px;align-items:start}
@media(max-width:900px){.exam-body{grid-template-columns:1fr}}

.q-card{background:var(--card);border:1px solid var(--line);border-radius:12px;box-shadow:0 1px 3px rgba(20,120,140,.05);overflow:hidden}
.q-top{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:13px 20px;border-bottom:1px solid var(--line);background:#fffaef}
.q-no{font-weight:800;font-size:15px}
.q-tags{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.tag{font-size:11px;font-weight:700;padding:3px 9px;border-radius:20px}
.tag-type{background:#f2e9d4;color:#a07c2a}
.tag-pos{background:var(--grn-bg);color:#1a6b3c}
.tag-neg{background:var(--red-bg);color:#a32f24}
.tag-topic{background:#f6ecd2;color:#7a1f1f}
.q-text{padding:20px 20px 6px;font-size:16px;line-height:1.62;color:#2e1c12;white-space:pre-wrap}
.opts{padding:6px 20px 20px;display:flex;flex-direction:column;gap:10px}
.opt{display:flex;align-items:flex-start;gap:12px;padding:13px 15px;border:1.5px solid #ece2cc;border-radius:10px;transition:.12s;background:#ffffff}
.opt:hover{border-color:#d8c79c;background:#fbf5e7}
.opt.sel{border-color:var(--navy);background:#faf2dc;box-shadow:inset 0 0 0 1px var(--navy)}
.opt-mark{width:22px;height:22px;border-radius:50%;border:2px solid #cfc3a4;flex:0 0 auto;display:grid;place-items:center;margin-top:1px;font-size:12px;font-weight:800;color:#ffffff}
.opt.sel .opt-mark{background:var(--navy);border-color:var(--navy)}
.opt-mark.sq{border-radius:6px}
.opt-key{font-weight:800;color:#7a6450;margin-right:2px}
.opt.sel .opt-key{color:var(--navy)}
.opt-txt{font-size:15px;color:#3a2418;padding-top:1px}
.num-in{margin:6px 20px 22px;display:flex;flex-direction:column;gap:8px;max-width:320px}
.num-in label{font-size:12.5px;color:var(--muted);font-weight:600}
.num-in input{padding:12px 14px;border:1.5px solid #e6d6b2;border-radius:9px;font-size:16px;font-weight:600;color:var(--ink);outline:none;width:100%}
.num-in input:focus{border-color:var(--navy);box-shadow:0 0 0 3px rgba(20,150,180,.1)}

.q-actions{display:flex;flex-wrap:wrap;gap:10px;padding:16px 20px;border-top:1px solid var(--line);background:#fffaef}
.btn{font-size:13.5px;font-weight:700;padding:11px 18px;border-radius:9px;transition:.14s;border:1.5px solid transparent}
.btn-ghost{background:#ffffff;border-color:#e6d6b2;color:#5c4636}
.btn-ghost:hover{border-color:#d8c79c;background:#f7efdd}
.btn-mark{background:#ffffff;border-color:#c8a24a;color:#7a1f1f}
.btn-mark:hover{background:#fbf3df}
.btn-save{background:var(--green);color:#ffffff;margin-left:auto}
.btn-save:hover{background:#1a7a42}
@media(max-width:520px){.btn-save{margin-left:0;width:100%}}

/* ---------- PALETTE ---------- */
.palette{background:var(--card);border:1px solid var(--line);border-radius:12px;box-shadow:0 1px 3px rgba(20,120,140,.05);overflow:hidden;position:sticky;top:118px}
.pal-user{padding:14px 16px;border-bottom:1px solid var(--line);display:flex;align-items:center;gap:11px;background:#fffaef}
.pal-av{width:34px;height:34px;border-radius:7px;background:var(--navy);color:#ffffff;display:grid;place-items:center;font-weight:800;font-size:13px}
.pal-legend{padding:14px 16px;border-bottom:1px solid var(--line);display:grid;grid-template-columns:1fr 1fr;gap:9px 10px}
.lg{display:flex;align-items:center;gap:8px;font-size:11.5px;color:#5c4636}
.lg-box{width:22px;height:22px;border-radius:6px;display:grid;place-items:center;font-size:11px;font-weight:800;color:#ffffff;flex:0 0 auto;position:relative}
.pal-sec{padding:12px 16px}
.pal-sec-name{font-size:11.5px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);margin-bottom:10px}
.pal-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:8px}
.pal-btn{aspect-ratio:1;border-radius:7px;font-size:13px;font-weight:800;color:#ffffff;display:grid;place-items:center;position:relative;border:2px solid transparent;transition:.12s}
.pal-btn:hover{transform:translateY(-1px)}
.pal-btn.cur{outline:2px solid var(--navy);outline-offset:2px}
.dot{position:absolute;bottom:2px;right:2px;width:8px;height:8px;border-radius:50%;background:var(--green);border:1.5px solid #ffffff}
.pal-foot{padding:14px 16px;border-top:1px solid var(--line);background:#fffaef}
.submit-btn{width:100%;background:var(--navy);color:#ffffff;font-weight:800;font-size:15px;padding:13px;border-radius:10px;transition:.15s}
.submit-btn:hover{background:var(--navy-2)}

/* ---------- MODAL ---------- */
.overlay{position:fixed;inset:0;background:rgba(13,27,42,.55);display:grid;place-items:center;z-index:50;padding:18px;backdrop-filter:blur(2px)}
.modal{background:#ffffff;border-radius:16px;max-width:480px;width:100%;overflow:hidden;box-shadow:0 24px 60px rgba(0,0,0,.3)}
.modal-head{padding:20px 24px;border-bottom:1px solid var(--line)}
.modal-head h3{margin:0;font-size:18px;font-weight:800}
.modal-head p{margin:5px 0 0;font-size:13.5px;color:var(--muted)}
.modal-stats{padding:18px 24px;display:grid;grid-template-columns:repeat(2,1fr);gap:12px}
.mstat{border:1px solid var(--line);border-radius:10px;padding:13px 15px}
.mstat .n{font-size:24px;font-weight:800;line-height:1}
.mstat .l{font-size:11.5px;color:var(--muted);margin-top:5px;font-weight:600}
.modal-foot{padding:16px 24px;display:flex;gap:12px;border-top:1px solid var(--line);background:#fffaef}
.modal-foot .btn{flex:1;text-align:center;padding:13px}
.btn-danger{background:var(--green);color:#ffffff}
.btn-danger:hover{background:#1a7a42}

/* ---------- RESULTS ---------- */
.res{padding:26px 16px 70px;max-width:1180px;margin:0 auto}
.res-hero{background:url("data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20viewBox%3D%270%200%201200%20360%27%3E%3Cg%20fill%3D%27none%27%20stroke%3D%27%230a4f5e%27%20stroke-width%3D%273.2%27%20stroke-linecap%3D%27round%27%3E%3Cpath%20d%3D%27M120%2095%20q22%20-20%2044%200%20q22%20-20%2044%200%27%20opacity%3D%270.20%27%2F%3E%3Cpath%20d%3D%27M300%2062%20q16%20-14%2032%200%20q16%20-14%2032%200%27%20opacity%3D%270.16%27%2F%3E%3Cpath%20d%3D%27M520%20102%20q20%20-18%2040%200%20q20%20-18%2040%200%27%20opacity%3D%270.18%27%2F%3E%3Cpath%20d%3D%27M720%2056%20q14%20-12%2028%200%20q14%20-12%2028%200%27%20opacity%3D%270.14%27%2F%3E%3Cpath%20d%3D%27M900%2098%20q24%20-22%2048%200%20q24%20-22%2048%200%27%20opacity%3D%270.20%27%2F%3E%3Cpath%20d%3D%27M1050%2066%20q16%20-14%2032%200%20q16%20-14%2032%200%27%20opacity%3D%270.16%27%2F%3E%3Cpath%20d%3D%27M430%20152%20q12%20-10%2024%200%20q12%20-10%2024%200%27%20opacity%3D%270.12%27%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat center 16px / 88% auto,radial-gradient(ellipse 55% 50% at 16% 4%, rgba(255,255,255,.55), transparent 72%),radial-gradient(ellipse 46% 42% at 83% 2%, rgba(255,255,255,.40), transparent 72%),url("data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20viewBox%3D%270%200%201200%20220%27%3E%3Cdefs%3E%3ClinearGradient%20id%3D%27bk0%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%23b5714f%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%23b5714f%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk1%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%23ad8c48%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%23ad8c48%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk2%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%235d8576%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%235d8576%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk3%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%236f6398%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%236f6398%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk4%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%233f7a88%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%233f7a88%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk5%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%239a564c%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%239a564c%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk6%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%237e8a4e%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%237e8a4e%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk7%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%2348688f%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%2348688f%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3C%2Fdefs%3E%3Cg%20opacity%3D%270.42%27%3E%3Crect%20x%3D%270%27%20y%3D%270%27%20width%3D%2723%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%2724%27%20y%3D%270%27%20width%3D%2732%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%2757%27%20y%3D%270%27%20width%3D%2741%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%2799%27%20y%3D%270%27%20width%3D%2716%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27116%27%20y%3D%270%27%20width%3D%2725%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27142%27%20y%3D%270%27%20width%3D%2734%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27177%27%20y%3D%270%27%20width%3D%2743%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%27221%27%20y%3D%270%27%20width%3D%2718%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%27240%27%20y%3D%270%27%20width%3D%2727%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%27268%27%20y%3D%270%27%20width%3D%2736%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%27305%27%20y%3D%270%27%20width%3D%2745%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%27351%27%20y%3D%270%27%20width%3D%2720%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27372%27%20y%3D%270%27%20width%3D%2729%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27402%27%20y%3D%270%27%20width%3D%2738%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27441%27%20y%3D%270%27%20width%3D%2747%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%27489%27%20y%3D%270%27%20width%3D%2722%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%27512%27%20y%3D%270%27%20width%3D%2731%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%27544%27%20y%3D%270%27%20width%3D%2740%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%27585%27%20y%3D%270%27%20width%3D%2749%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%27635%27%20y%3D%270%27%20width%3D%2724%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27660%27%20y%3D%270%27%20width%3D%2733%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27694%27%20y%3D%270%27%20width%3D%2742%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27737%27%20y%3D%270%27%20width%3D%2717%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%27755%27%20y%3D%270%27%20width%3D%2726%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%27782%27%20y%3D%270%27%20width%3D%2735%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%27818%27%20y%3D%270%27%20width%3D%2744%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%27863%27%20y%3D%270%27%20width%3D%2719%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%27883%27%20y%3D%270%27%20width%3D%2728%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27912%27%20y%3D%270%27%20width%3D%2737%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27950%27%20y%3D%270%27%20width%3D%2746%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27997%27%20y%3D%270%27%20width%3D%2721%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%271019%27%20y%3D%270%27%20width%3D%2730%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%271050%27%20y%3D%270%27%20width%3D%2739%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%271090%27%20y%3D%270%27%20width%3D%2748%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%271139%27%20y%3D%270%27%20width%3D%2723%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%271163%27%20y%3D%270%27%20width%3D%2732%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%271196%27%20y%3D%270%27%20width%3D%2741%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom / 100% 42%,linear-gradient(135deg,#9a2a2a 0%,#c39d44 100%);border-radius:18px;color:#ffffff;padding:30px;display:grid;grid-template-columns:auto 1fr;gap:30px;align-items:center;box-shadow:0 16px 40px rgba(18,140,170,.26);overflow:hidden}
@media(max-width:760px){.res-hero{grid-template-columns:1fr;text-align:center;gap:22px}}
.ring-wrap{position:relative;width:172px;height:172px;margin:0 auto}
.ring-center{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.ring-score{font-size:38px;font-weight:800;line-height:1;letter-spacing:-.02em}
.ring-max{font-size:13px;color:#f1e4c4;margin-top:3px}
.ring-grade{margin-top:7px;font-size:13px;font-weight:800;padding:2px 12px;border-radius:20px;background:rgba(255,255,255,.14)}
.hero-eyebrow{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:#cbb98e;font-weight:700}
.hero-title{font-size:23px;font-weight:800;margin:5px 0 3px;letter-spacing:-.01em;text-shadow:0 1px 12px rgba(8,70,84,.30)}
.hero-sub{font-size:13.5px;color:#fffaef;text-shadow:0 1px 9px rgba(8,70,84,.34)}
.hero-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(96px,1fr));gap:14px;margin-top:20px}
.hs{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);border-radius:11px;padding:13px}
.hs .n{font-size:21px;font-weight:800;line-height:1}
.hs .l{font-size:11px;color:#f1e4c4;margin-top:5px;font-weight:600;letter-spacing:.02em}
.pct-badge{display:inline-flex;align-items:center;gap:8px;margin-top:18px;background:var(--gold);color:#ffffff;font-weight:800;font-size:14px;padding:9px 16px;border-radius:30px}

.res-grid{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:18px}
@media(max-width:820px){.res-grid{grid-template-columns:1fr}}
.panel{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px;box-shadow:0 1px 3px rgba(20,120,140,.05)}
.panel.full{grid-column:1/-1}
.panel-eyebrow{font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);font-weight:800}
.panel-title{font-size:17px;font-weight:800;margin:5px 0 2px;letter-spacing:-.01em}
.panel-note{font-size:12.5px;color:var(--muted);margin:0 0 16px}

.secbar{margin-bottom:16px}
.secbar:last-child{margin-bottom:0}
.secbar-top{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:7px}
.secbar-name{font-size:14px;font-weight:700;color:var(--ink)}
.secbar-val{font-size:13px;font-weight:700}
.track{height:11px;background:#fdf6e3;border-radius:8px;overflow:hidden}
.fill{height:100%;border-radius:8px;transition:width .8s ease}
.secbar-meta{font-size:11.5px;color:var(--muted);margin-top:5px}

.topic-list{display:flex;flex-direction:column;gap:11px;margin-top:4px}
.topic-row{display:flex;align-items:center;gap:12px}
.topic-name{font-size:13.5px;font-weight:600;width:150px;flex:0 0 auto;color:#4a3322}
.topic-track{flex:1;height:9px;background:#fdf6e3;border-radius:6px;overflow:hidden}
.topic-fill{height:100%;border-radius:6px}
.band{font-size:10.5px;font-weight:800;padding:3px 9px;border-radius:20px;flex:0 0 auto;text-transform:uppercase;letter-spacing:.03em}

.plan-list{display:flex;flex-direction:column;gap:13px}
.plan-item{display:flex;gap:13px;padding:14px 16px;border-radius:11px;border:1px solid var(--line)}
.plan-item.weak{background:var(--red-bg);border-color:#f1cfcf}
.plan-item.avg{background:var(--amb-bg);border-color:#efdfba}
.plan-item.good{background:var(--grn-bg);border-color:#c9e8d5}
.plan-ic{width:30px;height:30px;border-radius:8px;flex:0 0 auto;display:grid;place-items:center;font-weight:800;font-size:14px;color:#ffffff}
.plan-txt h5{margin:0 0 3px;font-size:14px;font-weight:800}
.plan-txt p{margin:0;font-size:13px;color:#4a3322;line-height:1.5}

/* ---------- REVIEW ---------- */
.rev-filters{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px}
.rev-f{font-size:12.5px;font-weight:700;padding:8px 15px;border-radius:20px;border:1.5px solid #e6dcc4;color:#5c4636;background:#ffffff;transition:.13s}
.rev-f.active{background:var(--navy);border-color:var(--navy);color:#ffffff}
.rev-f:hover:not(.active){border-color:#d8c79c}
.rev-item{border:1px solid var(--line);border-radius:12px;margin-bottom:12px;overflow:hidden}
.rev-bar{display:flex;align-items:center;gap:12px;padding:14px 16px;cursor:pointer;background:#ffffff;transition:.13s}
.rev-bar:hover{background:#fffaef}
.rev-idx{width:34px;height:34px;border-radius:8px;display:grid;place-items:center;font-weight:800;font-size:13px;color:#ffffff;flex:0 0 auto}
.rev-q{flex:1;min-width:0;font-size:14px;color:#4a3322;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.rev-meta{display:flex;align-items:center;gap:14px;flex:0 0 auto}
.rev-marks{font-size:13px;font-weight:800}
.rev-time{font-size:11.5px;color:var(--muted);display:flex;align-items:center;gap:4px}
.rev-chev{color:#bcae94;font-size:13px;transition:.2s}
.rev-chev.open{transform:rotate(90deg)}
.rev-body{padding:0 16px 18px;border-top:1px solid var(--line);background:#fdfaf0}
.rev-qfull{font-size:14.5px;color:#2e1c12;line-height:1.6;white-space:pre-wrap;padding:16px 0 14px}
.rev-opts{display:flex;flex-direction:column;gap:8px;margin-bottom:14px}
.rev-opt{display:flex;align-items:flex-start;gap:10px;padding:10px 13px;border-radius:9px;font-size:14px;border:1.5px solid transparent}
.rev-opt.correct{background:var(--grn-bg);border-color:#bfe3cd;color:#176437}
.rev-opt.wrong{background:var(--red-bg);border-color:#f1cccc;color:#a32f24}
.rev-opt.neutral{background:#f7efdd;color:#5c4636}
.rev-opt-key{font-weight:800;flex:0 0 auto}
.rev-flag{margin-left:auto;font-size:11px;font-weight:800;padding:2px 9px;border-radius:20px;flex:0 0 auto}
.flag-c{background:#cdeedb;color:#176437}
.flag-w{background:#f6d6d6;color:#a32f24}
.expl{background:#ffffff;border:1px solid #ece2cc;border-left:3px solid var(--navy);border-radius:8px;padding:13px 15px;font-size:13.5px;color:#4a3322;line-height:1.6}
.expl b{color:var(--navy)}

.res-foot{display:flex;justify-content:center;gap:12px;margin-top:26px}
.foot-btn{font-size:14px;font-weight:700;padding:13px 26px;border-radius:10px;border:1.5px solid var(--navy);color:var(--navy);background:#ffffff;transition:.14s}
.foot-btn:hover{background:#faf2dc}
.foot-btn.primary{background:var(--navy);color:#ffffff}
.foot-btn.primary:hover{background:var(--navy-2)}
`;

/* palette status colors */
const STATUS = {
  notVisited: { bg: "#ffffff", bd: "#e6d6b2", fg: "#5c4636" },
  notAnswered: { bg: "#c0392b", bd: "#c0392b", fg: "#ffffff" },
  answered: { bg: "#1f8a4c", bd: "#1f8a4c", fg: "#ffffff" },
  marked: { bg: "#8a2727", bd: "#8a2727", fg: "#ffffff" },
  ansMarked: { bg: "#8a2727", bd: "#8a2727", fg: "#ffffff" },
};

/* ============================================================
   SCORE RING
   ============================================================ */
function ScoreRing({ score, max, grade }) {
  const pct = max > 0 ? Math.max(0, score) / max : 0;
  const R = 76, C = 2 * Math.PI * R;
  const off = C * (1 - Math.min(1, pct));
  return (
    <div className="ring-wrap">
      <svg width="172" height="172" viewBox="0 0 172 172" style={{ transform: "rotate(-90deg)" }}>
        <circle cx="86" cy="86" r={R} fill="none" stroke="rgba(255,255,255,.14)" strokeWidth="13" />
        <circle cx="86" cy="86" r={R} fill="none" stroke={grade.c} strokeWidth="13" strokeLinecap="round"
          strokeDasharray={C} strokeDashoffset={off} style={{ transition: "stroke-dashoffset 1s ease" }} />
      </svg>
      <div className="ring-center">
        <div className="ring-score">{score.toFixed(score % 1 === 0 ? 0 : 2)}</div>
        <div className="ring-max">out of {max}</div>
        <div className="ring-grade" style={{ color: grade.c }}>Grade {grade.g}</div>
      </div>
    </div>
  );
}

/* ============================================================
   INSTRUCTIONS SCREEN
   ============================================================ */
function Instructions({ onStart, onExit }) {
  const EXAM = useExam();
  const { t } = useLang();
  const [agree, setAgree] = useState(false);
  const totalQ = EXAM.sections.reduce((s, x) => s + x.questions.length, 0);
  const maxMarks = EXAM.sections.reduce((s, x) => s + x.questions.reduce((a, q) => a + q.marks, 0), 0);

  /* The marking scheme is read off the actual paper — it used to be hardcoded
     to one specific GS/CSAT split and was wrong for every other test. */
  const marking = EXAM.sections.map((sec) => {
    const plus = [...new Set(sec.questions.map((q) => q.marks))].sort((a, b) => a - b);
    const minus = [...new Set(sec.questions.map((q) => q.negative).filter(Boolean))].sort((a, b) => a - b);
    return { section: sec.name, plus: "+" + plus.join(" / +"), minus: minus.length ? minus.join(" / ") : null };
  });
  const shuffled = EXAM.shuffleQuestions || EXAM.shuffleOptions;
  return (
    <div className="inst">
      <div className="inst-card">
        <div className="inst-head">
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", gap: 12 }}>
            <div className="inst-eyebrow">{t("ex_online")}</div>
            <ChromeControls />
          </div>
          <h1 className="inst-title">{EXAM.title}</h1>
          <div className="inst-meta">
            <span>{t("ex_duration")} <b>{Math.round(EXAM.durationSec / 60)} {t("ex_min")}</b></span>
            <span>{t("ex_questions")} <b>{totalQ}</b></span>
            <span>{t("ex_maxmarks")} <b>{maxMarks}</b></span>
            <span>{t("ex_sections")} <b>{EXAM.sections.length}</b></span>
          </div>
        </div>
        <div className="inst-body">
          <div className="inst-h">{t("ex_gen_inst")}</div>
          <ol className="inst-list">
            <li>{t("ex_i1a")}<b>{t("ex_i1b")}</b>.</li>
            <li>{t("ex_i2a")}<b style={{ color: "var(--red)" }}>{t("ex_i2b")}</b>{t("ex_i2c")}</li>
            <li>{t("ex_i3")}</li>
            <li>{t("ex_i4")}</li>
            <li>{t("ex_i5a")}<b>{t("ex_save_next")}</b>{t("ex_i5b")}<b>{t("ex_mark_next")}</b>{t("ex_i5c")}<b>{t("ex_clear")}</b>{t("ex_i5d")}</li>
            {shuffled && <li>{t("ex_i6")}</li>}
          </ol>

          <div className="inst-h">{t("ex_marking")}</div>
          <ul className="inst-list">
            {marking.map((m) => (
              <li key={m.section}>
                <b>{m.section}:</b> {m.plus} {t("ex_for_correct")}
                {m.minus ? <>, −{m.minus} {t("ex_for_wrong")}</> : <>, {t("ex_no_negative")}</>}.
              </li>
            ))}
            <li><b>{t("ex_multi_t")}</b> {t("ex_multi_d")}</li>
          </ul>

          <div className="inst-h">{t("ex_legend")}</div>
          <div className="legend-grid">
            <div className="legend-row"><span className="lg-box" style={{ background: STATUS.answered.bg }}>1</span> {t("ex_answered")}</div>
            <div className="legend-row"><span className="lg-box" style={{ background: STATUS.notAnswered.bg }}>2</span> {t("ex_notanswered")}</div>
            <div className="legend-row"><span className="lg-box" style={{ background: STATUS.notVisited.bg, color: STATUS.notVisited.fg, border: "1.5px solid " + STATUS.notVisited.bd }}>3</span> {t("ex_notvisited")}</div>
            <div className="legend-row"><span className="lg-box" style={{ background: STATUS.marked.bg }}>4</span> {t("ex_marked")}</div>
            <div className="legend-row"><span className="lg-box" style={{ background: STATUS.ansMarked.bg }}>5<span className="dot" /></span> {t("ex_ansmarked")}</div>
          </div>

          <div className="consent">
            <input id="agree" type="checkbox" checked={agree} onChange={(e) => setAgree(e.target.checked)} />
            <label htmlFor="agree">{t("ex_consent")}</label>
          </div>

          <div className="begin-row">
            <button className="begin-btn" disabled={!agree} onClick={onStart}>{t("ex_begin")} →</button>
            <button onClick={onExit} style={{ marginLeft: 12, padding: "13px 22px", background: "var(--card)", border: "1.5px solid #e6d6b2", borderRadius: 10, color: "var(--muted)", fontWeight: 700, fontSize: 15, cursor: "pointer" }}>← {t("ex_dashboard")}</button>
          </div>
        </div>
      </div>
    </div>
  );
}

/* ============================================================
   EXAM SCREEN
   ============================================================ */
function ExamScreen({ state, actions, candidateName, candidateId }) {
  const { t } = useLang();
  const EXAM = useExam();
  const { secIdx, qIdx, answers, visited, marked, timeLeft } = state;
  const sec = EXAM.sections[secIdx];
  const q = sec.questions[qIdx];
  const danger = timeLeft <= 60;
  const candidate = candidateName || t("ex_candidate");
  const initials = candidate.split(" ").map((w) => w[0]).slice(0, 2).join("");

  const getStatus = (qid) => {
    if (!visited.has(qid)) return "notVisited";
    const ans = hasAnswer(answers[qid]);
    const mk = marked.has(qid);
    if (mk && ans) return "ansMarked";
    if (mk) return "marked";
    if (ans) return "answered";
    return "notAnswered";
  };

  const optLetter = (i) => String.fromCharCode(65 + i);

  return (
    <div>
      {/* HEADER */}
      <div className="exam-head">
        <div className="exam-head-in">
          <div className="cand">
            <div className="cand-av">{initials}</div>
            <div style={{ minWidth: 0 }}>
              <div className="cand-name">{candidate}</div>
              <div className="cand-sub">{candidateId ? `${t("ex_candidate_id")}: ${candidateId}` : ""}</div>
            </div>
          </div>
          {/* A student who starts the paper in English and finds they cannot
              follow it must be able to switch mid-attempt — this used to exist
              only on the instructions page, so they were stuck for the whole
              two hours. Changing language re-renders; it does not remount the
              runner, so answers and the clock survive. */}
          <div style={{ display: "flex", alignItems: "center", gap: 12, marginLeft: "auto" }}>
            <ChromeControls />
            <div className={"timer-box" + (danger ? " danger" : "")}>
              <div>
                <div className="timer-label">{t("ex_time_left")}</div>
                <div className="timer-val">{fmt(timeLeft)}</div>
              </div>
            </div>
          </div>
        </div>
        <div className="sec-tabs">
          <div className="sec-tabs-in">
            {EXAM.sections.map((s, i) => (
              <button key={s.name} className={"sec-tab" + (i === secIdx ? " active" : "")}
                onClick={() => actions.goTo(i, 0)}>{s.name}</button>
            ))}
          </div>
        </div>
      </div>

      {/* BODY */}
      <div className="exam-body">
        {/* QUESTION */}
        <div className="q-card">
          <div className="q-top">
            <span className="q-no">{t("ex_question_n")} {qIdx + 1}</span>
            <div className="q-tags">
              <span className="tag tag-topic">{q.topic}</span>
              <span className="tag tag-type">{q.type === "mcq" ? t("ex_single") : q.type === "multiple" ? t("ex_multiple") : t("ex_numerical")}</span>
              <span className="tag tag-pos">+{q.marks}</span>
              {q.negative > 0 && <span className="tag tag-neg">−{q.negative}</span>}
            </div>
          </div>

          <div className="q-text">{q.text}</div>

          {q.type === "numerical" ? (
            <div className="num-in">
              <label>{t("ex_enter_ans")}</label>
              <input type="number" inputMode="decimal" value={answers[q.id] ?? ""} placeholder={t("ex_type_number")}
                onChange={(e) => actions.setNumerical(q.id, e.target.value)} />
            </div>
          ) : (
            <div className="opts">
              {q.options.map((opt, i) => {
                // The answer is stored as the option's own id, not its
                // position, so shuffling cannot change what was chosen.
                const selected = q.type === "multiple"
                  ? Array.isArray(answers[q.id]) && answers[q.id].includes(opt.id)
                  : answers[q.id] === opt.id;
                return (
                  <button key={opt.id} className={"opt" + (selected ? " sel" : "")}
                    onClick={() => q.type === "multiple" ? actions.toggleMulti(q.id, opt.id) : actions.selectMcq(q.id, opt.id)}>
                    <span className={"opt-mark" + (q.type === "multiple" ? " sq" : "")}>{selected ? "✓" : ""}</span>
                    <span className="opt-txt"><span className="opt-key">{optLetter(i)}.</span> {opt.body}</span>
                  </button>
                );
              })}
            </div>
          )}

          <div className="q-actions">
            <button className="btn btn-ghost" onClick={actions.prev}>← {t("ex_previous")}</button>
            <button className="btn btn-ghost" onClick={() => actions.clear(q.id)}>{t("ex_clear")}</button>
            <button className="btn btn-mark" onClick={() => actions.markNext(q.id)}>{t("ex_mark_next")}</button>
            <button className="btn btn-save" onClick={actions.saveNext}>{t("ex_save_next")}</button>
          </div>
        </div>

        {/* PALETTE */}
        <div className="palette">
          <div className="pal-user">
            <div className="pal-av">{initials}</div>
            <div>
              <div style={{ fontWeight: 700, fontSize: 13.5 }}>{candidate}</div>
              <div style={{ fontSize: 11.5, color: "var(--muted)" }}>{t("ex_in_progress")}</div>
            </div>
          </div>
          <div className="pal-legend">
            <div className="lg"><span className="lg-box" style={{ background: STATUS.answered.bg }} /> {t("ex_answered")}</div>
            <div className="lg"><span className="lg-box" style={{ background: STATUS.notAnswered.bg }} /> {t("ex_notanswered")}</div>
            <div className="lg"><span className="lg-box" style={{ background: STATUS.notVisited.bg, border: "1.5px solid " + STATUS.notVisited.bd }} /> {t("ex_notvisited")}</div>
            <div className="lg"><span className="lg-box" style={{ background: STATUS.marked.bg }} /> {t("ex_marked")}</div>
            <div className="lg" style={{ gridColumn: "1/-1" }}><span className="lg-box" style={{ background: STATUS.ansMarked.bg }}><span className="dot" /></span> {t("ex_ansmarked_l")}</div>
          </div>

          {EXAM.sections.map((s, si) => (
            <div className="pal-sec" key={s.name}>
              <div className="pal-sec-name">{s.name}</div>
              <div className="pal-grid">
                {s.questions.map((qq, qi) => {
                  const st = getStatus(qq.id);
                  const c = STATUS[st];
                  const isCur = si === secIdx && qi === qIdx;
                  return (
                    <button key={qq.id} className={"pal-btn" + (isCur ? " cur" : "")}
                      style={{ background: c.bg, color: c.fg, border: "2px solid " + c.bd }}
                      onClick={() => actions.goTo(si, qi)}>
                      {qi + 1}
                      {st === "ansMarked" && <span className="dot" />}
                    </button>
                  );
                })}
              </div>
            </div>
          ))}

          <div className="pal-foot">
            <button className="submit-btn" onClick={actions.openSubmit}>{t("ex_submit_test")}</button>
          </div>
        </div>
      </div>
    </div>
  );
}

/* ============================================================
   SUBMIT MODAL
   ============================================================ */
function SubmitModal({ counts, onCancel, onConfirm }) {
  const { t } = useLang();
  return (
    <div className="overlay" onClick={onCancel}>
      <div className="modal" onClick={(e) => e.stopPropagation()}>
        <div className="modal-head">
          <h3>{t("ex_submit_q")}</h3>
          <p>{t("ex_submit_warn")}</p>
        </div>
        <div className="modal-stats">
          <div className="mstat"><div className="n" style={{ color: "var(--green)" }}>{counts.answered}</div><div className="l">{t("ex_answered")}</div></div>
          <div className="mstat"><div className="n" style={{ color: "var(--red)" }}>{counts.unanswered}</div><div className="l">{t("ex_notanswered")}</div></div>
          <div className="mstat"><div className="n" style={{ color: "#8a2727" }}>{counts.marked}</div><div className="l">{t("ex_marked")}</div></div>
          <div className="mstat"><div className="n" style={{ color: "var(--muted)" }}>{counts.notVisited}</div><div className="l">{t("ex_notvisited")}</div></div>
        </div>
        <div className="modal-foot">
          <button className="btn btn-ghost" onClick={onCancel}>{t("ex_resume")}</button>
          <button className="btn btn-danger" onClick={onConfirm}>{t("ex_submit_now")}</button>
        </div>
      </div>
    </div>
  );
}

/* ============================================================
   RESULTS SCREEN
   ============================================================ */
function Results({ data, onRetake, onExit }) {
  const EXAM = useExam();
  const { t } = useLang();
  const [filter, setFilter] = useState("all");
  const [open, setOpen] = useState(null);

  const grade = gradeFor(data.scorePct);
  // A real percentile arrives once the attempt is scored against everyone who
  // has taken this paper. Until then we show a clearly-labelled estimate
  // rather than passing a curve off as a rank.
  const hasRealStanding = typeof data.percentile === "number" && data.totalStudents > 1;
  const pctile = hasRealStanding ? data.percentile : estPercentile(data.scorePct);

  const filtered = data.review.filter((r) =>
    filter === "all" ? true :
    filter === "correct" ? r.correct :
    filter === "wrong" ? (r.attempted && !r.correct) :
    !r.attempted
  );

  // Peer figures come from everyone else's attempts on this same paper. With
  // no peers yet, the comparison is hidden instead of invented.
  const hasPeers = typeof data.peerAvg === "number" && data.totalStudents > 1;
  const cmpData = hasPeers ? [
    { name: "You", value: +data.scorePct.toFixed(1), fill: grade.c },
    { name: "Batch avg.", value: +Number(data.peerAvg).toFixed(1), fill: "#b0a080" },
    { name: "Topper", value: +Number(data.peerBest ?? data.peerAvg).toFixed(1), fill: "#d4a64a" },
  ] : null;
  const radarData = data.topics.map((t) => ({ topic: t.name, You: Math.round(t.acc) }));
  const timeData = data.review.map((r) => ({ q: "Q" + (r.num ?? "?"), time: Math.round(r.time), slow: r.slow }));

  const weak = data.topics.filter((t) => t.band === "weak");
  const avg = data.topics.filter((t) => t.band === "average");
  const strong = data.topics.filter((t) => t.band === "strong");
  const slowQ = data.review.filter((r) => r.slow);

  return (
    <div className="res">
      {/* HERO SCORECARD */}
      <div className="res-hero">
        <ScoreRing score={data.score} max={data.maxScore} grade={grade} />
        <div>
          <div className="hero-eyebrow">Performance Report</div>
          <div className="hero-title">{EXAM.title}</div>
          <div className="hero-sub">Attempted {data.attempted} of {data.total} questions in {fmt(data.timeUsed)}</div>
          <div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginTop: 10 }}>
            <div className="pct-badge" style={{ margin: 0 }}>
              ★ {hasRealStanding ? "Percentile" : "Estimated percentile"}: {pctile.toFixed(1)}
            </div>
            {hasRealStanding && (
              <div className="pct-badge" style={{ margin: 0 }}>
                Rank #{data.rank} of {data.totalStudents}
              </div>
            )}
          </div>
          {data.saveFailed && (
            <div style={{ marginTop: 10, fontSize: 12.5, color: "#f29b9b", display: "flex", alignItems: "center", gap: 6 }}>
              <AlertCircle size={14} /> We couldn't save this attempt to your account — the report below is still accurate.
            </div>
          )}
          <div className="hero-stats">
            <div className="hs"><div className="n" style={{ color: "#7fe0a3" }}>{data.correct}</div><div className="l">{t("ex_correct")}</div></div>
            <div className="hs"><div className="n" style={{ color: "#f29b9b" }}>{data.wrong}</div><div className="l">Wrong</div></div>
            <div className="hs"><div className="n">{data.unattempted}</div><div className="l">Skipped</div></div>
            <div className="hs"><div className="n">{data.accuracy.toFixed(0)}%</div><div className="l">Accuracy</div></div>
          </div>
        </div>
      </div>

      <div className="res-grid">
        {/* SECTION-WISE */}
        <div className="panel">
          <div className="panel-eyebrow">Breakdown</div>
          <div className="panel-title">{t("ex_sec_perf")}</div>
          <p className="panel-note">Score in each section as a share of its maximum.</p>
          {data.sections.map((s) => {
            const pct = s.max > 0 ? (Math.max(0, s.score) / s.max) * 100 : 0;
            const col = pct >= 65 ? SEM.strong : pct >= 40 ? SEM.average : SEM.weak;
            return (
              <div className="secbar" key={s.name}>
                <div className="secbar-top">
                  <span className="secbar-name">{s.name}</span>
                  <span className="secbar-val" style={{ color: col }}>{s.score.toFixed(2)} / {s.max}</span>
                </div>
                <div className="track"><div className="fill" style={{ width: pct + "%", background: col }} /></div>
                <div className="secbar-meta">{s.correct} correct · {s.wrong} wrong · {s.unattempted} skipped · {pct.toFixed(0)}%</div>
              </div>
            );
          })}
        </div>

        {/* COMPARISON */}
        <div className="panel">
          <div className="panel-eyebrow">Benchmark</div>
          <div className="panel-title">You vs Batch vs Topper</div>
          <p className="panel-note">
            {hasPeers
              ? `Your score % against the ${data.totalStudents} aspirants who have taken this paper.`
              : "Nobody else has taken this paper yet — you're the first."}
          </p>
          {!hasPeers ? (
            <div style={{ height: 230, display: "grid", placeItems: "center", textAlign: "center",
                          color: "var(--muted)", fontSize: 13.5, lineHeight: 1.7, padding: "0 20px" }}>
              <div>
                <Trophy size={30} style={{ color: "#d4a64a", marginBottom: 10 }} />
                <div>You set the benchmark on this test.<br />Come back after others attempt it to see where you stand.</div>
              </div>
            </div>
          ) : (
          <div style={{ height: 230 }}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={cmpData} margin={{ top: 16, right: 8, left: -18, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="var(--line)" />
                <XAxis dataKey="name" tick={{ fontSize: 12, fill: "var(--muted)" }} axisLine={false} tickLine={false} />
                <YAxis domain={[0, 100]} tick={{ fontSize: 11, fill: "#bcae94" }} axisLine={false} tickLine={false} unit="%" />
                <Tooltip cursor={{ fill: "rgba(20,150,180,.04)" }} formatter={(v) => [v + "%", "Score"]}
                  contentStyle={{ borderRadius: 10, border: "1px solid var(--line)", fontSize: 13 }} />
                <Bar dataKey="value" radius={[7, 7, 0, 0]} maxBarSize={66}>
                  {cmpData.map((e, i) => <Cell key={i} fill={e.fill} />)}
                  <LabelList dataKey="value" position="top" formatter={(v) => v + "%"} style={{ fontSize: 12, fontWeight: 800, fill: "#4a3322" }} />
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
          )}
        </div>

        {/* TOPIC RADAR */}
        <div className="panel">
          <div className="panel-eyebrow">Diagnosis</div>
          <div className="panel-title">Topic Strength Map</div>
          <p className="panel-note">Accuracy across every topic tested.</p>
          <div style={{ height: 250 }}>
            <ResponsiveContainer width="100%" height="100%">
              <RadarChart data={radarData} outerRadius="72%">
                <PolarGrid stroke="#eae0c8" />
                <PolarAngleAxis dataKey="topic" tick={{ fontSize: 11, fill: "var(--muted)" }} />
                <PolarRadiusAxis domain={[0, 100]} tick={{ fontSize: 9, fill: "#cfc3a4" }} axisLine={false} />
                <Radar dataKey="You" stroke="#b8923a" fill="#b8923a" fillOpacity={0.28} strokeWidth={2} />
                <Tooltip formatter={(v) => [v + "%", "Accuracy"]} contentStyle={{ borderRadius: 10, border: "1px solid var(--line)", fontSize: 13 }} />
              </RadarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* TOPIC BANDS */}
        <div className="panel">
          <div className="panel-eyebrow">Diagnosis</div>
          <div className="panel-title">Strong / Average / Weak</div>
          <p className="panel-note">Each topic graded by your accuracy.</p>
          <div className="topic-list">
            {data.topics.slice().sort((a, b) => b.acc - a.acc).map((t) => {
              const col = SEM[t.band];
              const bg = t.band === "strong" ? "var(--grn-bg)" : t.band === "average" ? "var(--amb-bg)" : "var(--red-bg)";
              return (
                <div className="topic-row" key={t.name}>
                  <span className="topic-name">{t.name}</span>
                  <div className="topic-track"><div className="topic-fill" style={{ width: t.acc + "%", background: col }} /></div>
                  <span className="band" style={{ background: bg, color: col }}>{t.band}</span>
                </div>
              );
            })}
          </div>
        </div>

        {/* TIME PER QUESTION */}
        <div className="panel full">
          <div className="panel-eyebrow">Time Management</div>
          <div className="panel-title">Time Spent per Question</div>
          <p className="panel-note">Bars in red took noticeably longer than your average — target these for speed.</p>
          <div style={{ height: 240 }}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={timeData} margin={{ top: 16, right: 8, left: -22, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="var(--line)" />
                <XAxis dataKey="q" tick={{ fontSize: 11, fill: "var(--muted)" }} axisLine={false} tickLine={false} />
                <YAxis tick={{ fontSize: 11, fill: "#bcae94" }} axisLine={false} tickLine={false} unit="s" />
                <Tooltip cursor={{ fill: "rgba(20,150,180,.04)" }} formatter={(v) => [v + "s", "Time"]}
                  contentStyle={{ borderRadius: 10, border: "1px solid var(--line)", fontSize: 13 }} />
                <Bar dataKey="time" radius={[5, 5, 0, 0]} maxBarSize={40}>
                  {timeData.map((e, i) => <Cell key={i} fill={e.slow ? "#c0392b" : "#c39d44"} />)}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* AI IMPROVEMENT PLAN */}
        <div className="panel full">
          <div className="panel-eyebrow">Action Plan</div>
          <div className="panel-title">Your Personalised Improvement Plan</div>
          <p className="panel-note">Built from what actually happened in this attempt — your topic accuracy, the questions you spent too long on, and the ones you left blank.</p>
          <div className="plan-list">
            {weak.length > 0 && (
              <div className="plan-item weak">
                <div className="plan-ic" style={{ background: SEM.weak }}>!</div>
                <div className="plan-txt">
                  <h5>Priority — Weak areas to fix first</h5>
                  <p>You scored below 50% in <b>{weak.map((t) => t.name).join(", ")}</b>. Dedicate the next 3–4 study sessions here: revise core concepts, then drill 20–30 PYQs per topic before re-testing.</p>
                </div>
              </div>
            )}
            {avg.length > 0 && (
              <div className="plan-item avg">
                <div className="plan-ic" style={{ background: SEM.average }}>~</div>
                <div className="plan-txt">
                  <h5>Strengthen — Almost there</h5>
                  <p><b>{avg.map((t) => t.name).join(", ")}</b> {avg.length > 1 ? "are" : "is"} in the 50–75% range. You understand the basics but lose marks on tricky variants. Focus on application-level questions and previous mistakes.</p>
                </div>
              </div>
            )}
            {slowQ.length > 0 && (
              <div className="plan-item avg">
                <div className="plan-ic" style={{ background: "#c39d44" }}>⏱</div>
                <div className="plan-txt">
                  <h5>Speed — Manage your time better</h5>
                  <p>You spent too long on <b>{slowQ.length}</b> question{slowQ.length > 1 ? "s" : ""} ({slowQ.map((r) => "Q" + (r.num ?? "?")).join(", ")}). Practise a time cap per question and learn to flag-and-move instead of getting stuck.</p>
                </div>
              </div>
            )}
            {data.unattempted > 0 && (
              <div className="plan-item avg">
                <div className="plan-ic" style={{ background: "#8a2727" }}>○</div>
                <div className="plan-txt">
                  <h5>Coverage — Don't leave marks on the table</h5>
                  <p>You skipped <b>{data.unattempted}</b> question{data.unattempted > 1 ? "s" : ""}. With negative marking in mind, attempt questions where you can eliminate at least two options — calculated guessing improves expected score.</p>
                </div>
              </div>
            )}
            {strong.length > 0 && (
              <div className="plan-item good">
                <div className="plan-ic" style={{ background: SEM.strong }}>✓</div>
                <div className="plan-txt">
                  <h5>Keep it up — Your strengths</h5>
                  <p>Strong performance in <b>{strong.map((t) => t.name).join(", ")}</b>. Maintain with light weekly revision so these stay your scoring anchors on exam day.</p>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* QUESTION-BY-QUESTION REVIEW */}
        <div className="panel full">
          <div className="panel-eyebrow">Deep Review</div>
          <div className="panel-title">{t("ex_qbyq")}</div>
          <p className="panel-note">Your answer, the correct answer, marks awarded, time spent, and a full explanation for every question.</p>
          <div className="rev-filters">
            {[["all", "All"], ["correct", "Correct"], ["wrong", "Wrong"], ["skipped", "Skipped"]].map(([k, label]) => (
              <button key={k} className={"rev-f" + (filter === k ? " active" : "")} onClick={() => setFilter(k)}>
                {label} ({k === "all" ? data.review.length : k === "correct" ? data.correct : k === "wrong" ? data.wrong : data.unattempted})
              </button>
            ))}
          </div>

          {filtered.map((r) => {
            const col = !r.attempted ? "#b0a080" : r.correct ? SEM.strong : SEM.weak;
            const isOpen = open === r.id;
            return (
              <div className="rev-item" key={r.id}>
                <div className="rev-bar" onClick={() => setOpen(isOpen ? null : r.id)}>
                  <div className="rev-idx" style={{ background: col }}>{r.num ?? "?"}</div>
                  <div className="rev-q">{r.text.split("\n")[0]}</div>
                  <div className="rev-meta">
                    <span className="rev-time">⏱ {fmt(r.time)}</span>
                    <span className="rev-marks" style={{ color: r.awarded > 0 ? SEM.strong : r.awarded < 0 ? SEM.weak : "var(--muted)" }}>
                      {r.awarded > 0 ? "+" : ""}{r.awarded.toFixed(2)}
                    </span>
                    <span className={"rev-chev" + (isOpen ? " open" : "")}>▶</span>
                  </div>
                </div>
                {isOpen && (
                  <div className="rev-body">
                    <div className="rev-qfull">{r.text}</div>
                    {r.type !== "numerical" ? (
                      <div className="rev-opts">
                        {r.options.map((opt, i) => {
                          const isCorrect = r.type === "multiple" ? r.correctVal.includes(i) : r.correctVal === i;
                          const isYour = r.type === "multiple" ? (Array.isArray(r.yourVal) && r.yourVal.includes(i)) : r.yourVal === i;
                          let cls = "neutral";
                          if (isCorrect) cls = "correct";
                          else if (isYour && !isCorrect) cls = "wrong";
                          return (
                            <div key={i} className={"rev-opt " + cls}>
                              <span className="rev-opt-key">{String.fromCharCode(65 + i)}.</span>
                              <span>{opt}</span>
                              {isCorrect && <span className="rev-flag flag-c">Correct answer</span>}
                              {isYour && !isCorrect && <span className="rev-flag flag-w">Your answer</span>}
                            </div>
                          );
                        })}
                      </div>
                    ) : (
                      <div className="rev-opts">
                        <div className={"rev-opt correct"}><span className="rev-opt-key">✓</span><span>{t("ex_correct_ans")}: {r.correctVal}</span></div>
                        <div className={"rev-opt " + (r.correct ? "correct" : r.attempted ? "wrong" : "neutral")}>
                          <span className="rev-opt-key">{r.attempted ? (r.correct ? "✓" : "✗") : "—"}</span>
                          <span>Your answer: {r.attempted ? r.yourVal : "Not attempted"}</span>
                        </div>
                      </div>
                    )}
                    <div className="expl"><b>Explanation:</b> {r.explanation}</div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>

      <div className="res-foot">
        <button className="foot-btn" onClick={onRetake}>↻ Re-attempt test</button>
        <button className="foot-btn primary" onClick={onExit}>{t("ex_back_dash")} →</button>
      </div>
    </div>
  );
}

/* ============================================================
   APP (state machine + scoring)
   ============================================================ */
function ExamRunner({ onExit, candidateName, candidateId, onSubmitted }) {
  const EXAM = useExam();
  const { t } = useLang();
  const [screen, setScreen] = useState("instructions"); // instructions | exam | result
  const [secIdx, setSecIdx] = useState(0);
  const [qIdx, setQIdx] = useState(0);
  const [answers, setAnswers] = useState({});
  const [visited, setVisited] = useState(new Set());
  const [marked, setMarked] = useState(new Set());
  const [timeLeft, setTimeLeft] = useState(EXAM.durationSec);
  const [showSubmit, setShowSubmit] = useState(false);
  const [results, setResults] = useState(null);
  const [submitting, setSubmitting] = useState(false);
  const [submitErr, setSubmitErr] = useState("");
  const timeSpent = useRef({});
  const enteredAt = useRef(0);
  const startedAt = useRef(new Date().toISOString());

  // Flat navigation order. The paper is fixed for the life of this runner, so
  // the sections object is a stable dependency.
  const order = useMemo(() => {
    const o = [];
    EXAM.sections.forEach((s, si) => s.questions.forEach((q, qi) => o.push({ si, qi, id: q.id })));
    return o;
  }, [EXAM.sections]);

  // timer
  useEffect(() => {
    if (screen !== "exam") return;
    if (timeLeft <= 0) { doSubmit(); return; }
    const t = setTimeout(() => setTimeLeft((x) => x - 1), 1000);
    return () => clearTimeout(t);
    // eslint-disable-next-line
  }, [screen, timeLeft]);

  const curId = () => EXAM.sections[secIdx].questions[qIdx].id;

  const flush = (qid) => {
    if (!enteredAt.current) return;
    const dt = (Date.now() - enteredAt.current) / 1000;
    timeSpent.current[qid] = (timeSpent.current[qid] || 0) + dt;
    enteredAt.current = Date.now();
  };

  const start = () => {
    const firstId = order[0].id;
    setVisited(new Set([firstId]));
    enteredAt.current = Date.now();
    startedAt.current = new Date().toISOString();
    setScreen("exam");
  };

  const goTo = (si, qi) => {
    flush(curId());
    setSecIdx(si); setQIdx(qi);
    setVisited((v) => new Set(v).add(EXAM.sections[si].questions[qi].id));
    enteredAt.current = Date.now();
  };
  const goByOffset = (off) => {
    const pos = order.findIndex((o) => o.si === secIdx && o.qi === qIdx);
    const np = Math.min(order.length - 1, Math.max(0, pos + off));
    goTo(order[np].si, order[np].qi);
  };

  const actions = {
    goTo,
    prev: () => goByOffset(-1),
    saveNext: () => goByOffset(1),
    selectMcq: (qid, optId) => { setAnswers((a) => ({ ...a, [qid]: optId })); setVisited((v) => new Set(v).add(qid)); },
    toggleMulti: (qid, optId) => setAnswers((a) => {
      const cur = Array.isArray(a[qid]) ? a[qid] : [];
      const next = cur.includes(optId) ? cur.filter((x) => x !== optId) : [...cur, optId];
      return { ...a, [qid]: next };
    }),
    setNumerical: (qid, v) => { setAnswers((a) => ({ ...a, [qid]: v })); setVisited((vv) => new Set(vv).add(qid)); },
    clear: (qid) => setAnswers((a) => { const c = { ...a }; delete c[qid]; return c; }),
    markNext: (qid) => { setMarked((m) => new Set(m).add(qid)); goByOffset(1); },
    openSubmit: () => { flush(curId()); setShowSubmit(true); },
  };

  const counts = useMemo(() => {
    let answered = 0, marks = 0, notVisited = 0;
    order.forEach(({ id }) => {
      const ans = hasAnswer(answers[id]);
      if (!visited.has(id)) notVisited++;
      if (ans) answered++;
      if (marked.has(id)) marks++;
    });
    return { answered, unanswered: order.length - answered, marked: marks, notVisited };
  }, [answers, visited, marked, order]);

  /* Scoring happens on the server. The browser sends which option ids were
     chosen and nothing else — it no longer knows the answers, and it can no
     longer write to `attempts` at all. */
  const doSubmit = async () => {
    flush(curId());
    setShowSubmit(false);
    setSubmitErr("");
    setSubmitting(true);
    try {
      const data = await onSubmitted({
        testId: EXAM.id,
        answers,
        timeSpent: { ...timeSpent.current },
        timeUsed: EXAM.durationSec - timeLeft,
        startedAt: startedAt.current,
      });
      if (!data) throw new Error("Could not score this paper.");
      setResults(data);
      setScreen("result");
    } catch (e) {
      console.error("submit failed", e);
      // The answers stay exactly where they are — a failed submit must never
      // cost a student the paper they just sat.
      setSubmitErr(e?.message || "Could not submit. Check your connection and try again.");
    } finally {
      setSubmitting(false);
    }
  };

  const retake = () => {
    setScreen("instructions");
    setSecIdx(0); setQIdx(0); setAnswers({}); setVisited(new Set()); setMarked(new Set());
    setTimeLeft(EXAM.durationSec); setResults(null); setShowSubmit(false);
    timeSpent.current = {}; enteredAt.current = 0;
  };

  return (
    <div className="ee-root">
      <style>{CSS}</style>
      {screen === "instructions" && <Instructions onStart={start} onExit={onExit} />}
      {screen === "exam" && <ExamScreen state={{ secIdx, qIdx, answers, visited, marked, timeLeft }} actions={actions} candidateName={candidateName} candidateId={candidateId} />}
      {screen === "result" && results && <Results data={results} onRetake={retake} onExit={onExit} />}
      {showSubmit && <SubmitModal counts={counts} onCancel={() => setShowSubmit(false)} onConfirm={doSubmit} />}
      {submitting && (
        <div className="ee-blocker">
          <div className="ee-blocker-card">
            <div className="ee-spin" />
            <b>{t("ex_scoring")}</b>
            <span>{t("ex_scoring_sub")}</span>
          </div>
        </div>
      )}
      {submitErr && (
        <div className="ee-blocker">
          <div className="ee-blocker-card">
            <b>{t("ex_sub_failed")}</b>
            <span>{submitErr}</span>
            <span style={{ color: "var(--muted)" }}>{t("ex_answers_safe")}</span>
            <div style={{ display: "flex", gap: 10, marginTop: 6 }}>
              <button className="btn btn-primary" onClick={doSubmit}>{t("ex_try_again")}</button>
              <button className="btn btn-ghost" onClick={() => setSubmitErr("")}>{t("ex_back_paper")}</button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

/* ============================================================
   LOADER — resolves the real test, then hands it to the runner.
   ============================================================ */
function App({ testId, onExit }) {
  const { t } = useLang();
  const [exam, setExam] = useState(null);
  const [err, setErr] = useState("");
  const [candidateName, setCandidateName] = useState("Candidate");
  const [userId, setUserId] = useState(null);

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const user = await currentUser();
        if (!user) { if (alive) setErr("Your session has expired. Please sign in again."); return; }
        if (alive) setUserId(user.id);

        const profile = await getProfile(user.id).catch(() => null);
        const name = (profile?.full_name || "").trim()
          || (user.email ? user.email.split("@")[0] : "")
          || "Candidate";
        if (alive) setCandidateName(name);

        if (!testId) { if (alive) setErr("No test was selected. Pick one from the Test Series page."); return; }
        const paper = await loadExamTest(testId);
        if (alive) setExam(paper);
      } catch (e) {
        console.error("exam load failed", e);
        if (alive) setErr(e?.message || "This test could not be opened. Please try again.");
      }
    })();
    return () => { alive = false; };
  }, [testId]);

  /* Warn before a refresh or tab close mid-paper. */
  useEffect(() => {
    const onBeforeUnload = (e) => { e.preventDefault(); e.returnValue = ""; };
    window.addEventListener("beforeunload", onBeforeUnload);
    return () => window.removeEventListener("beforeunload", onBeforeUnload);
  }, []);

  /* Persist the attempt and return the student's real standing. */
  /* One server round trip does the whole thing: it scores the paper, writes
     the attempt, computes the rank and percentile, and returns the report.
     The failure is deliberately propagated rather than swallowed — the runner
     keeps the student's answers on screen and offers a retry, which is far
     better than showing a score that was never saved. */
  const handleSubmitted = async (raw) => {
    if (!userId) throw new Error("You appear to be signed out. Sign in again to submit.");
    return await submitAttempt(raw);
  };

  if (err) {
    return (
      <div className="ee-root">
        <style>{CSS}</style>
        <div style={{ minHeight: "100vh", display: "grid", placeItems: "center", padding: 24 }}>
          <div style={{ maxWidth: 420, textAlign: "center", background: "var(--card)", border: "1px solid #e6d6b2",
                        borderRadius: 16, padding: "32px 26px" }}>
            <DiyaLogo size={48} ring />
            <div style={{ fontFamily: "var(--font-display,serif)", fontSize: 19, margin: "14px 0 8px", color: "#5b1414" }}>
              Can't start this test
            </div>
            <div style={{ fontSize: 14, color: "var(--muted)", lineHeight: 1.6 }}>{err}</div>
            <button className="begin-btn" style={{ marginTop: 20 }} onClick={onExit}>Back to dashboard</button>
          </div>
        </div>
      </div>
    );
  }

  if (!exam) {
    return (
      <div className="ee-root">
        <style>{CSS}</style>
        <div style={{ minHeight: "100vh", display: "grid", placeItems: "center", gap: 14 }}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 14 }}>
            <div style={{ animation: "jn-breathe 2.2s ease-in-out infinite" }}><DiyaLogo size={50} ring /></div>
            <div style={{ color: "var(--muted)", fontWeight: 600 }}>{t("ex_preparing")}</div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <ExamCtx.Provider value={exam}>
      <ExamRunner onExit={onExit} candidateName={candidateName}
                  candidateId={userId ? "JN-" + userId.replace(/-/g, "").slice(0, 8).toUpperCase() : ""}
                  onSubmitted={handleSubmitted} />
    </ExamCtx.Provider>
  );
}

return App;
})();

export default ExamApp;
