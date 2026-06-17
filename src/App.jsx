import React, { useState, useEffect, useRef, useMemo } from "react";
import {
  LayoutDashboard, ListChecks, FileText, GraduationCap, FolderOpen, Users,
  IndianRupee, Plus, Search, Pencil, Trash2, X, Upload, Check, ChevronRight,
  Menu, AlertCircle, CheckCircle2, BookOpen, Clock, Layers, Eye, EyeOff, Save,
  ArrowLeft, Filter, TrendingUp, Home, BarChart3, Trophy, User, Flame, Target,
  Award, Play, RotateCcw, Lock, Calendar, Bell, Star, Zap, ArrowUp, ArrowDown,
  Medal, Sparkles, LogOut, Mail, Phone, ArrowRight, ShieldCheck,
} from "lucide-react";
import {
  AreaChart, Area, LineChart, Line, RadarChart, PolarGrid, PolarAngleAxis,
  PolarRadiusAxis, Radar, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip,
  ResponsiveContainer, Cell, LabelList,
} from "recharts";

const ExamApp = (() => {
/* ============================================================
   EXAM DATA  (seed content — replace from your question bank / DB)
   type: 'mcq' | 'multiple' | 'numerical'
   ============================================================ */
const EXAM = {
  title: "BPSC / UPSC Prelims — Full Mock Test 01",
  durationSec: 20 * 60, // 20 minutes
  sections: [
    {
      name: "General Studies",
      questions: [
        { id: "A1", topic: "Polity", type: "mcq", marks: 2, negative: 0.66,
          text: "Which Article of the Indian Constitution is described by Dr. B. R. Ambedkar as the 'heart and soul' of the Constitution?",
          options: ["Article 14", "Article 19", "Article 32", "Article 21"], correct: 2,
          explanation: "Article 32 (Right to Constitutional Remedies) lets citizens move the Supreme Court directly for enforcement of Fundamental Rights. Ambedkar called it the heart and soul of the Constitution because rights are meaningless without a remedy to enforce them." },
        { id: "A2", topic: "Modern History", type: "mcq", marks: 2, negative: 0.66,
          text: "The Non-Cooperation Movement was formally launched by Mahatma Gandhi in which year?",
          options: ["1919", "1920", "1922", "1930"], correct: 1,
          explanation: "The Non-Cooperation Movement was launched in 1920 (Nagpur session, December 1920). It was withdrawn in February 1922 after the Chauri Chaura incident." },
        { id: "A3", topic: "Geography", type: "mcq", marks: 2, negative: 0.66,
          text: "Which is the longest river of Peninsular India?",
          options: ["Krishna", "Godavari", "Cauvery", "Narmada"], correct: 1,
          explanation: "The Godavari (~1465 km) is the longest river of Peninsular India, earning the name 'Dakshina Ganga'. It rises near Trimbak in Maharashtra and drains into the Bay of Bengal." },
        { id: "A4", topic: "Polity", type: "mcq", marks: 2, negative: 0.66,
          text: "How many Fundamental Duties are presently enumerated in the Constitution of India?",
          options: ["10", "11", "12", "9"], correct: 1,
          explanation: "Originally 10 Fundamental Duties were added by the 42nd Amendment (1976). The 11th (education of children aged 6–14) was added by the 86th Amendment (2002). Total = 11, listed under Article 51A." },
        { id: "A5", topic: "Economy", type: "multiple", marks: 2, negative: 0.66,
          text: "Which of the following are DIRECT taxes? (Select all that apply)",
          options: ["Income Tax", "Goods and Services Tax (GST)", "Corporate Tax", "Customs Duty"], correct: [0, 2],
          explanation: "Direct taxes are paid directly by the entity on which they are levied — Income Tax and Corporate Tax. GST and Customs Duty are indirect taxes (the burden is passed on to the consumer). Full marks only if exactly Income Tax + Corporate Tax are selected." },
        { id: "A6", topic: "Environment", type: "mcq", marks: 2, negative: 0.66,
          text: "In which year was 'Project Tiger' launched in India?",
          options: ["1972", "1973", "1985", "1991"], correct: 1,
          explanation: "Project Tiger was launched in 1973 from Jim Corbett National Park to protect Bengal tigers through a network of tiger reserves managed under the NTCA (formed 2006)." },
        { id: "A7", topic: "Modern History", type: "mcq", marks: 2, negative: 0.66,
          text: "Who founded the Arya Samaj in 1875?",
          options: ["Raja Ram Mohan Roy", "Swami Vivekananda", "Swami Dayananda Saraswati", "Keshab Chandra Sen"], correct: 2,
          explanation: "Swami Dayananda Saraswati founded the Arya Samaj in Bombay in 1875, giving the call 'Back to the Vedas' and opposing idol worship, caste rigidity, and child marriage." },
        { id: "A8", topic: "Geography", type: "mcq", marks: 2, negative: 0.66,
          text: "The Tropic of Cancer passes through how many Indian states?",
          options: ["6", "7", "8", "9"], correct: 2,
          explanation: "The Tropic of Cancer passes through 8 states: Gujarat, Rajasthan, Madhya Pradesh, Chhattisgarh, Jharkhand, West Bengal, Tripura, and Mizoram." },
      ],
    },
    {
      name: "CSAT (Aptitude)",
      questions: [
        { id: "B1", topic: "Number System", type: "mcq", marks: 2.5, negative: 0.83,
          text: "What is the unit (last) digit of 7^105?",
          options: ["1", "3", "7", "9"], correct: 2,
          explanation: "The unit digit of powers of 7 cycles every 4: 7, 9, 3, 1. Since 105 ÷ 4 leaves remainder 1, the unit digit matches 7^1 = 7." },
        { id: "B2", topic: "Reasoning", type: "mcq", marks: 2.5, negative: 0.83,
          text: "Find the next number in the series: 2, 6, 12, 20, 30, ?",
          options: ["36", "40", "42", "44"], correct: 2,
          explanation: "The pattern is n² + n: 1·2=2, 2·3=6, 3·4=12, 4·5=20, 5·6=30, 6·7=42. Differences (4,6,8,10,12) also confirm the next term is 42." },
        { id: "B3", topic: "Reading Comprehension", type: "mcq", marks: 2.5, negative: 0.83,
          text: "Passage: 'Economic growth without equitable distribution often deepens social fault lines. A nation may post impressive GDP figures while its poorest citizens see little change. True development must therefore be measured not by aggregate output alone, but by how widely its benefits are shared.'\n\nWhat does the passage most strongly imply?",
          options: [
            "GDP growth should be the primary goal of every nation",
            "Development should be judged by how widely benefits are distributed, not output alone",
            "Poor citizens are responsible for slow economic growth",
            "Social fault lines are unrelated to economic policy",
          ], correct: 1,
          explanation: "The passage's central inference is that real development is about distribution and shared benefit, not just headline GDP. Option B captures this; the others contradict or overstate the text." },
        { id: "B4", topic: "Quantitative Aptitude", type: "numerical", marks: 2.5, negative: 0, tolerance: 0.01,
          text: "A train 150 metres long crosses a stationary pole in 15 seconds. What is the speed of the train in km/h? (Enter a number)",
          correct: 36,
          explanation: "Speed = distance ÷ time = 150 m ÷ 15 s = 10 m/s. Convert: 10 × (18/5) = 36 km/h. (No negative marking on numerical questions in this set.)" },
        { id: "B5", topic: "Number System", type: "mcq", marks: 2.5, negative: 0.83,
          text: "What is the HCF (GCD) of 36 and 48?",
          options: ["6", "12", "18", "24"], correct: 1,
          explanation: "36 = 2²·3², 48 = 2⁴·3. Common factors: 2²·3 = 12. So HCF(36, 48) = 12." },
        { id: "B6", topic: "Reasoning", type: "mcq", marks: 2.5, negative: 0.83,
          text: "If in a code 'FACE' is written as 'GBDF', how is 'HEAD' written in the same code?",
          options: ["IFBE", "IFBD", "GFBE", "IEBF"], correct: 0,
          explanation: "Each letter is shifted +1: F→G, A→B, C→D, E→F. Applying +1 to HEAD: H→I, E→F, A→B, D→E = 'IFBE'." },
        { id: "B7", topic: "Quantitative Aptitude", type: "mcq", marks: 2.5, negative: 0.83,
          text: "An article bought for ₹400 is sold for ₹500. What is the profit percentage?",
          options: ["20%", "25%", "30%", "15%"], correct: 1,
          explanation: "Profit = 500 − 400 = ₹100. Profit % = (100 / 400) × 100 = 25%. (Profit % is always calculated on cost price.)" },
        { id: "B8", topic: "Reading Comprehension", type: "mcq", marks: 2.5, negative: 0.83,
          text: "Passage: 'Technology promises to democratise education, yet access to devices and connectivity remains deeply unequal. Without addressing this digital divide, online learning may widen the very gaps it claims to bridge.'\n\nWhich conclusion is best supported?",
          options: [
            "Technology has already made education fully equal",
            "Online learning can deepen inequality if the digital divide is ignored",
            "Devices and connectivity are now universally available",
            "Traditional classrooms are superior to online learning",
          ], correct: 1,
          explanation: "The passage warns that ignoring unequal access (the digital divide) can make online learning widen existing gaps. Option B is the supported inference; the others are unsupported or contradicted." },
      ],
    },
  ],
};

/* ============================================================
   HELPERS
   ============================================================ */
const fmt = (s) => {
  s = Math.max(0, Math.round(s));
  const h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), sec = s % 60;
  const pad = (n) => String(n).padStart(2, "0");
  return h > 0 ? `${pad(h)}:${pad(m)}:${pad(sec)}` : `${pad(m)}:${pad(sec)}`;
};
const arraysEqual = (a, b) => {
  if (!Array.isArray(a) || !Array.isArray(b) || a.length !== b.length) return false;
  const x = [...a].sort(), y = [...b].sort();
  return x.every((v, i) => v === y[i]);
};
const hasAnswer = (a) => {
  if (a === undefined || a === null) return false;
  if (Array.isArray(a)) return a.length > 0;
  if (typeof a === "string") return a.trim() !== "";
  return true;
};
const evaluate = (q, ans) => {
  const attempted = hasAnswer(ans);
  let correct = false;
  if (attempted) {
    if (q.type === "mcq") correct = ans === q.correct;
    else if (q.type === "multiple") correct = arraysEqual(ans, q.correct);
    else if (q.type === "numerical") correct = Math.abs(parseFloat(ans) - q.correct) <= (q.tolerance || 0.01);
  }
  const awarded = !attempted ? 0 : correct ? q.marks : -q.negative;
  return { attempted, correct, awarded };
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
  if (p >= 55) return { g: "B", c: "#ec5a52" };
  if (p >= 40) return { g: "C", c: "#cc7a00" };
  return { g: "D", c: "#cf4040" };
};
const SEM = { strong: "#1f8a4c", average: "#cc8a00", weak: "#cf4040" };
const bandFor = (acc) => (acc >= 75 ? "strong" : acc >= 50 ? "average" : "weak");

/* ============================================================
   STYLES (self-contained design system)
   ============================================================ */
const CSS = `
:root{
  --navy:#0e8fa8; --navy-2:#0a6173; --gold:#ec5a52;
  --bg:#eefbfd; --card:#ffffff; --ink:#0e3540; --muted:#5e7d86; --line:#dcecf0;
  --green:#1f8a4c; --amber:#cc8a00; --red:#cf4040;
  --grn-bg:#e8f6ee; --amb-bg:#fff1ec; --red-bg:#fbeaea;
}
*{box-sizing:border-box}
.ee-root{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--ink);
  font-variant-numeric:tabular-nums;line-height:1.5;background:var(--bg);min-height:100%;}
.ee-root button{font-family:inherit;cursor:pointer;border:none;background:none}
.ee-wrap{max-width:1180px;margin:0 auto;padding:0 16px}

/* ---------- INSTRUCTIONS ---------- */
.inst{max-width:860px;margin:0 auto;padding:28px 16px 60px}
.inst-card{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:0 1px 3px rgba(20,120,140,.06)}
.inst-head{background:linear-gradient(135deg,#27bdd6,#0e94ad);color:#fff;padding:22px 26px}
.inst-eyebrow{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:#d4f3f9;font-weight:700}
.inst-title{font-size:22px;font-weight:800;margin:6px 0 0;letter-spacing:-.01em}
.inst-meta{display:flex;flex-wrap:wrap;gap:8px 24px;margin-top:14px;font-size:13px;color:#d6f1f7}
.inst-meta b{color:#fff}
.inst-body{padding:24px 26px}
.inst-h{font-size:13px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;color:var(--navy);margin:22px 0 10px}
.inst-h:first-child{margin-top:0}
.inst-list{margin:0;padding-left:18px;font-size:14.5px;color:#2a4750}
.inst-list li{margin:7px 0}
.legend-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:10px;margin-top:6px}
.legend-row{display:flex;align-items:center;gap:10px;font-size:13.5px;color:#33495d}
.consent{display:flex;gap:12px;align-items:flex-start;margin-top:26px;padding:16px;background:#f3f7fb;border:1px solid #d8e4ef;border-radius:10px}
.consent input{width:18px;height:18px;margin-top:2px;accent-color:var(--navy);cursor:pointer;flex:0 0 auto}
.consent label{font-size:14px;color:#2a4750;cursor:pointer}
.begin-row{margin-top:22px}
.begin-btn{background:var(--green);color:#fff;font-weight:700;font-size:15px;padding:13px 28px;border-radius:10px;transition:.15s}
.begin-btn:disabled{background:#aebfce;cursor:not-allowed}
.begin-btn:not(:disabled):hover{background:#1a7a42}

/* ---------- EXAM SHELL ---------- */
.exam-head{background:linear-gradient(110deg,#159aab,#0d6f80);color:#fff;position:sticky;top:0;z-index:20}
.exam-head-in{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:10px 18px;max-width:1280px;margin:0 auto}
.cand{display:flex;align-items:center;gap:12px;min-width:0}
.cand-av{width:38px;height:38px;border-radius:8px;background:#0c6e82;display:grid;place-items:center;font-weight:800;font-size:15px;flex:0 0 auto}
.cand-name{font-weight:700;font-size:14.5px;line-height:1.15;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cand-sub{font-size:11.5px;color:#d4f3f9}
.timer-box{display:flex;align-items:center;gap:10px;background:#0a6173;border:1px solid #0c6e82;padding:7px 14px;border-radius:10px}
.timer-box.danger{background:#7a1f1f;border-color:#a13030;animation:pulse 1s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.72}}
.timer-label{font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:#eafdff}
.timer-box.danger .timer-label{color:#f3c9c9}
.timer-val{font-size:19px;font-weight:800;font-variant-numeric:tabular-nums;letter-spacing:.02em}

.sec-tabs{background:#0a6173;border-top:1px solid #0c6e82}
.sec-tabs-in{display:flex;gap:0;max-width:1280px;margin:0 auto;padding:0 10px;overflow-x:auto}
.sec-tab{padding:11px 20px;color:#d4f3f9;font-size:13.5px;font-weight:700;border-bottom:3px solid transparent;white-space:nowrap;transition:.15s}
.sec-tab.active{color:#fff;border-bottom-color:var(--gold);background:rgba(255,255,255,.04)}
.sec-tab:hover:not(.active){color:#d6f1f7}

.exam-body{display:grid;grid-template-columns:1fr 296px;gap:18px;max-width:1280px;margin:0 auto;padding:18px;align-items:start}
@media(max-width:900px){.exam-body{grid-template-columns:1fr}}

.q-card{background:var(--card);border:1px solid var(--line);border-radius:12px;box-shadow:0 1px 3px rgba(20,120,140,.05);overflow:hidden}
.q-top{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:13px 20px;border-bottom:1px solid var(--line);background:#f6fdfe}
.q-no{font-weight:800;font-size:15px}
.q-tags{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.tag{font-size:11px;font-weight:700;padding:3px 9px;border-radius:20px}
.tag-type{background:#e7eef5;color:#0e7d92}
.tag-pos{background:var(--grn-bg);color:#1a6b3c}
.tag-neg{background:var(--red-bg);color:#a83232}
.tag-topic{background:#e3f3f7;color:#2a8fb0}
.q-text{padding:20px 20px 6px;font-size:16px;line-height:1.62;color:#103a44;white-space:pre-wrap}
.opts{padding:6px 20px 20px;display:flex;flex-direction:column;gap:10px}
.opt{display:flex;align-items:flex-start;gap:12px;padding:13px 15px;border:1.5px solid #dbe3ec;border-radius:10px;transition:.12s;background:#fff}
.opt:hover{border-color:#a8d4de;background:#f7fafd}
.opt.sel{border-color:var(--navy);background:#e6f6fa;box-shadow:inset 0 0 0 1px var(--navy)}
.opt-mark{width:22px;height:22px;border-radius:50%;border:2px solid #b6cdd4;flex:0 0 auto;display:grid;place-items:center;margin-top:1px;font-size:12px;font-weight:800;color:#fff}
.opt.sel .opt-mark{background:var(--navy);border-color:var(--navy)}
.opt-mark.sq{border-radius:6px}
.opt-key{font-weight:800;color:#5e7d86;margin-right:2px}
.opt.sel .opt-key{color:var(--navy)}
.opt-txt{font-size:15px;color:#243a4d;padding-top:1px}
.num-in{margin:6px 20px 22px;display:flex;flex-direction:column;gap:8px;max-width:320px}
.num-in label{font-size:12.5px;color:var(--muted);font-weight:600}
.num-in input{padding:12px 14px;border:1.5px solid #cfe3e9;border-radius:9px;font-size:16px;font-weight:600;color:var(--ink);outline:none;width:100%}
.num-in input:focus{border-color:var(--navy);box-shadow:0 0 0 3px rgba(20,150,180,.1)}

.q-actions{display:flex;flex-wrap:wrap;gap:10px;padding:16px 20px;border-top:1px solid var(--line);background:#f6fdfe}
.btn{font-size:13.5px;font-weight:700;padding:11px 18px;border-radius:9px;transition:.14s;border:1.5px solid transparent}
.btn-ghost{background:#fff;border-color:#cfe3e9;color:#43585f}
.btn-ghost:hover{border-color:#a8d4de;background:#f1f6fb}
.btn-mark{background:#fff;border-color:#c3b2e0;color:#2a8fb0}
.btn-mark:hover{background:#f5f1fc}
.btn-save{background:var(--green);color:#fff;margin-left:auto}
.btn-save:hover{background:#1a7a42}
@media(max-width:520px){.btn-save{margin-left:0;width:100%}}

/* ---------- PALETTE ---------- */
.palette{background:var(--card);border:1px solid var(--line);border-radius:12px;box-shadow:0 1px 3px rgba(20,120,140,.05);overflow:hidden;position:sticky;top:118px}
.pal-user{padding:14px 16px;border-bottom:1px solid var(--line);display:flex;align-items:center;gap:11px;background:#f6fdfe}
.pal-av{width:34px;height:34px;border-radius:7px;background:var(--navy);color:#fff;display:grid;place-items:center;font-weight:800;font-size:13px}
.pal-legend{padding:14px 16px;border-bottom:1px solid var(--line);display:grid;grid-template-columns:1fr 1fr;gap:9px 10px}
.lg{display:flex;align-items:center;gap:8px;font-size:11.5px;color:#4a6168}
.lg-box{width:22px;height:22px;border-radius:6px;display:grid;place-items:center;font-size:11px;font-weight:800;color:#fff;flex:0 0 auto;position:relative}
.pal-sec{padding:12px 16px}
.pal-sec-name{font-size:11.5px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);margin-bottom:10px}
.pal-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:8px}
.pal-btn{aspect-ratio:1;border-radius:7px;font-size:13px;font-weight:800;color:#fff;display:grid;place-items:center;position:relative;border:2px solid transparent;transition:.12s}
.pal-btn:hover{transform:translateY(-1px)}
.pal-btn.cur{outline:2px solid var(--navy);outline-offset:2px}
.dot{position:absolute;bottom:2px;right:2px;width:8px;height:8px;border-radius:50%;background:var(--green);border:1.5px solid #fff}
.pal-foot{padding:14px 16px;border-top:1px solid var(--line);background:#f6fdfe}
.submit-btn{width:100%;background:var(--navy);color:#fff;font-weight:800;font-size:15px;padding:13px;border-radius:10px;transition:.15s}
.submit-btn:hover{background:var(--navy-2)}

/* ---------- MODAL ---------- */
.overlay{position:fixed;inset:0;background:rgba(13,27,42,.55);display:grid;place-items:center;z-index:50;padding:18px;backdrop-filter:blur(2px)}
.modal{background:#fff;border-radius:16px;max-width:480px;width:100%;overflow:hidden;box-shadow:0 24px 60px rgba(0,0,0,.3)}
.modal-head{padding:20px 24px;border-bottom:1px solid var(--line)}
.modal-head h3{margin:0;font-size:18px;font-weight:800}
.modal-head p{margin:5px 0 0;font-size:13.5px;color:var(--muted)}
.modal-stats{padding:18px 24px;display:grid;grid-template-columns:repeat(2,1fr);gap:12px}
.mstat{border:1px solid var(--line);border-radius:10px;padding:13px 15px}
.mstat .n{font-size:24px;font-weight:800;line-height:1}
.mstat .l{font-size:11.5px;color:var(--muted);margin-top:5px;font-weight:600}
.modal-foot{padding:16px 24px;display:flex;gap:12px;border-top:1px solid var(--line);background:#f6fdfe}
.modal-foot .btn{flex:1;text-align:center;padding:13px}
.btn-danger{background:var(--green);color:#fff}
.btn-danger:hover{background:#1a7a42}

/* ---------- RESULTS ---------- */
.res{padding:26px 16px 70px;max-width:1180px;margin:0 auto}
.res-hero{background:url("data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20viewBox%3D%270%200%201200%20360%27%3E%3Cg%20fill%3D%27none%27%20stroke%3D%27%230a4f5e%27%20stroke-width%3D%273.2%27%20stroke-linecap%3D%27round%27%3E%3Cpath%20d%3D%27M120%2095%20q22%20-20%2044%200%20q22%20-20%2044%200%27%20opacity%3D%270.20%27%2F%3E%3Cpath%20d%3D%27M300%2062%20q16%20-14%2032%200%20q16%20-14%2032%200%27%20opacity%3D%270.16%27%2F%3E%3Cpath%20d%3D%27M520%20102%20q20%20-18%2040%200%20q20%20-18%2040%200%27%20opacity%3D%270.18%27%2F%3E%3Cpath%20d%3D%27M720%2056%20q14%20-12%2028%200%20q14%20-12%2028%200%27%20opacity%3D%270.14%27%2F%3E%3Cpath%20d%3D%27M900%2098%20q24%20-22%2048%200%20q24%20-22%2048%200%27%20opacity%3D%270.20%27%2F%3E%3Cpath%20d%3D%27M1050%2066%20q16%20-14%2032%200%20q16%20-14%2032%200%27%20opacity%3D%270.16%27%2F%3E%3Cpath%20d%3D%27M430%20152%20q12%20-10%2024%200%20q12%20-10%2024%200%27%20opacity%3D%270.12%27%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat center 16px / 88% auto,radial-gradient(ellipse 55% 50% at 16% 4%, rgba(255,255,255,.55), transparent 72%),radial-gradient(ellipse 46% 42% at 83% 2%, rgba(255,255,255,.40), transparent 72%),url("data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20viewBox%3D%270%200%201200%20220%27%3E%3Cdefs%3E%3ClinearGradient%20id%3D%27bk0%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%23b5714f%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%23b5714f%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk1%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%23ad8c48%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%23ad8c48%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk2%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%235d8576%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%235d8576%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk3%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%236f6398%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%236f6398%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk4%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%233f7a88%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%233f7a88%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk5%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%239a564c%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%239a564c%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk6%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%237e8a4e%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%237e8a4e%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk7%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%2348688f%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%2348688f%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3C%2Fdefs%3E%3Cg%20opacity%3D%270.42%27%3E%3Crect%20x%3D%270%27%20y%3D%270%27%20width%3D%2723%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%2724%27%20y%3D%270%27%20width%3D%2732%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%2757%27%20y%3D%270%27%20width%3D%2741%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%2799%27%20y%3D%270%27%20width%3D%2716%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27116%27%20y%3D%270%27%20width%3D%2725%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27142%27%20y%3D%270%27%20width%3D%2734%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27177%27%20y%3D%270%27%20width%3D%2743%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%27221%27%20y%3D%270%27%20width%3D%2718%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%27240%27%20y%3D%270%27%20width%3D%2727%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%27268%27%20y%3D%270%27%20width%3D%2736%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%27305%27%20y%3D%270%27%20width%3D%2745%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%27351%27%20y%3D%270%27%20width%3D%2720%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27372%27%20y%3D%270%27%20width%3D%2729%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27402%27%20y%3D%270%27%20width%3D%2738%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27441%27%20y%3D%270%27%20width%3D%2747%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%27489%27%20y%3D%270%27%20width%3D%2722%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%27512%27%20y%3D%270%27%20width%3D%2731%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%27544%27%20y%3D%270%27%20width%3D%2740%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%27585%27%20y%3D%270%27%20width%3D%2749%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%27635%27%20y%3D%270%27%20width%3D%2724%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27660%27%20y%3D%270%27%20width%3D%2733%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27694%27%20y%3D%270%27%20width%3D%2742%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27737%27%20y%3D%270%27%20width%3D%2717%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%27755%27%20y%3D%270%27%20width%3D%2726%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%27782%27%20y%3D%270%27%20width%3D%2735%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%27818%27%20y%3D%270%27%20width%3D%2744%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%27863%27%20y%3D%270%27%20width%3D%2719%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%27883%27%20y%3D%270%27%20width%3D%2728%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27912%27%20y%3D%270%27%20width%3D%2737%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27950%27%20y%3D%270%27%20width%3D%2746%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27997%27%20y%3D%270%27%20width%3D%2721%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%271019%27%20y%3D%270%27%20width%3D%2730%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%271050%27%20y%3D%270%27%20width%3D%2739%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%271090%27%20y%3D%270%27%20width%3D%2748%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%271139%27%20y%3D%270%27%20width%3D%2723%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%271163%27%20y%3D%270%27%20width%3D%2732%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%271196%27%20y%3D%270%27%20width%3D%2741%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom / 100% 42%,linear-gradient(135deg,#2cc4db 0%,#159fbd 100%);border-radius:18px;color:#fff;padding:30px;display:grid;grid-template-columns:auto 1fr;gap:30px;align-items:center;box-shadow:0 16px 40px rgba(18,140,170,.26);overflow:hidden}
@media(max-width:760px){.res-hero{grid-template-columns:1fr;text-align:center;gap:22px}}
.ring-wrap{position:relative;width:172px;height:172px;margin:0 auto}
.ring-center{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.ring-score{font-size:38px;font-weight:800;line-height:1;letter-spacing:-.02em}
.ring-max{font-size:13px;color:#d4f3f9;margin-top:3px}
.ring-grade{margin-top:7px;font-size:13px;font-weight:800;padding:2px 12px;border-radius:20px;background:rgba(255,255,255,.14)}
.hero-eyebrow{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:#9bbdd9;font-weight:700}
.hero-title{font-size:23px;font-weight:800;margin:5px 0 3px;letter-spacing:-.01em;text-shadow:0 1px 12px rgba(8,70,84,.30)}
.hero-sub{font-size:13.5px;color:#eafdff;text-shadow:0 1px 9px rgba(8,70,84,.34)}
.hero-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(96px,1fr));gap:14px;margin-top:20px}
.hs{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);border-radius:11px;padding:13px}
.hs .n{font-size:21px;font-weight:800;line-height:1}
.hs .l{font-size:11px;color:#d4f3f9;margin-top:5px;font-weight:600;letter-spacing:.02em}
.pct-badge{display:inline-flex;align-items:center;gap:8px;margin-top:18px;background:var(--gold);color:#fff;font-weight:800;font-size:14px;padding:9px 16px;border-radius:30px}

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
.track{height:11px;background:#eefbfd;border-radius:8px;overflow:hidden}
.fill{height:100%;border-radius:8px;transition:width .8s ease}
.secbar-meta{font-size:11.5px;color:var(--muted);margin-top:5px}

.topic-list{display:flex;flex-direction:column;gap:11px;margin-top:4px}
.topic-row{display:flex;align-items:center;gap:12px}
.topic-name{font-size:13.5px;font-weight:600;width:150px;flex:0 0 auto;color:#2a4750}
.topic-track{flex:1;height:9px;background:#eefbfd;border-radius:6px;overflow:hidden}
.topic-fill{height:100%;border-radius:6px}
.band{font-size:10.5px;font-weight:800;padding:3px 9px;border-radius:20px;flex:0 0 auto;text-transform:uppercase;letter-spacing:.03em}

.plan-list{display:flex;flex-direction:column;gap:13px}
.plan-item{display:flex;gap:13px;padding:14px 16px;border-radius:11px;border:1px solid var(--line)}
.plan-item.weak{background:var(--red-bg);border-color:#f1cfcf}
.plan-item.avg{background:var(--amb-bg);border-color:#f0dfba}
.plan-item.good{background:var(--grn-bg);border-color:#c9e8d5}
.plan-ic{width:30px;height:30px;border-radius:8px;flex:0 0 auto;display:grid;place-items:center;font-weight:800;font-size:14px;color:#fff}
.plan-txt h5{margin:0 0 3px;font-size:14px;font-weight:800}
.plan-txt p{margin:0;font-size:13px;color:#3a5258;line-height:1.5}

/* ---------- REVIEW ---------- */
.rev-filters{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px}
.rev-f{font-size:12.5px;font-weight:700;padding:8px 15px;border-radius:20px;border:1.5px solid #d6dfe8;color:#4a6168;background:#fff;transition:.13s}
.rev-f.active{background:var(--navy);border-color:var(--navy);color:#fff}
.rev-f:hover:not(.active){border-color:#a8d4de}
.rev-item{border:1px solid var(--line);border-radius:12px;margin-bottom:12px;overflow:hidden}
.rev-bar{display:flex;align-items:center;gap:12px;padding:14px 16px;cursor:pointer;background:#fff;transition:.13s}
.rev-bar:hover{background:#f6fdfe}
.rev-idx{width:34px;height:34px;border-radius:8px;display:grid;place-items:center;font-weight:800;font-size:13px;color:#fff;flex:0 0 auto}
.rev-q{flex:1;min-width:0;font-size:14px;color:#2a4750;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.rev-meta{display:flex;align-items:center;gap:14px;flex:0 0 auto}
.rev-marks{font-size:13px;font-weight:800}
.rev-time{font-size:11.5px;color:var(--muted);display:flex;align-items:center;gap:4px}
.rev-chev{color:#9bb4bc;font-size:13px;transition:.2s}
.rev-chev.open{transform:rotate(90deg)}
.rev-body{padding:0 16px 18px;border-top:1px solid var(--line);background:#fbfcfd}
.rev-qfull{font-size:14.5px;color:#103a44;line-height:1.6;white-space:pre-wrap;padding:16px 0 14px}
.rev-opts{display:flex;flex-direction:column;gap:8px;margin-bottom:14px}
.rev-opt{display:flex;align-items:flex-start;gap:10px;padding:10px 13px;border-radius:9px;font-size:14px;border:1.5px solid transparent}
.rev-opt.correct{background:var(--grn-bg);border-color:#bfe3cd;color:#176437}
.rev-opt.wrong{background:var(--red-bg);border-color:#f1cccc;color:#a13232}
.rev-opt.neutral{background:#f4f7fa;color:#43585f}
.rev-opt-key{font-weight:800;flex:0 0 auto}
.rev-flag{margin-left:auto;font-size:11px;font-weight:800;padding:2px 9px;border-radius:20px;flex:0 0 auto}
.flag-c{background:#cdeedb;color:#176437}
.flag-w{background:#f6d6d6;color:#a13232}
.expl{background:#fff;border:1px solid #dbe6f0;border-left:3px solid var(--navy);border-radius:8px;padding:13px 15px;font-size:13.5px;color:#2a4750;line-height:1.6}
.expl b{color:var(--navy)}

.res-foot{display:flex;justify-content:center;gap:12px;margin-top:26px}
.foot-btn{font-size:14px;font-weight:700;padding:13px 26px;border-radius:10px;border:1.5px solid var(--navy);color:var(--navy);background:#fff;transition:.14s}
.foot-btn:hover{background:#e6f6fa}
.foot-btn.primary{background:var(--navy);color:#fff}
.foot-btn.primary:hover{background:var(--navy-2)}
`;

/* palette status colors */
const STATUS = {
  notVisited: { bg: "#ffffff", bd: "#cfe3e9", fg: "#4a6168" },
  notAnswered: { bg: "#cf4040", bd: "#cf4040", fg: "#fff" },
  answered: { bg: "#1f8a4c", bd: "#1f8a4c", fg: "#fff" },
  marked: { bg: "#3a9bbf", bd: "#3a9bbf", fg: "#fff" },
  ansMarked: { bg: "#3a9bbf", bd: "#3a9bbf", fg: "#fff" },
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
  const [agree, setAgree] = useState(false);
  const totalQ = EXAM.sections.reduce((s, x) => s + x.questions.length, 0);
  const maxMarks = EXAM.sections.reduce((s, x) => s + x.questions.reduce((a, q) => a + q.marks, 0), 0);
  return (
    <div className="inst">
      <div className="inst-card">
        <div className="inst-head">
          <div className="inst-eyebrow">Online Examination</div>
          <h1 className="inst-title">{EXAM.title}</h1>
          <div className="inst-meta">
            <span>Duration: <b>{EXAM.durationSec / 60} min</b></span>
            <span>Questions: <b>{totalQ}</b></span>
            <span>Max Marks: <b>{maxMarks}</b></span>
            <span>Sections: <b>{EXAM.sections.length}</b></span>
          </div>
        </div>
        <div className="inst-body">
          <div className="inst-h">General Instructions</div>
          <ol className="inst-list">
            <li>The countdown timer at the top right shows the time remaining. When it reaches zero, the test is <b>submitted automatically</b>.</li>
            <li>The timer turns <b style={{ color: "var(--red)" }}>red in the last 60 seconds</b> as a final warning.</li>
            <li>The question palette on the right shows the status of every question using the colour codes below.</li>
            <li>You may move between sections and questions freely using the palette or the navigation buttons.</li>
            <li>Use <b>Save &amp; Next</b> to save your answer, <b>Mark for Review &amp; Next</b> to flag a question, and <b>Clear Response</b> to remove your selection.</li>
            <li>Question order is randomised per candidate to maintain exam integrity.</li>
          </ol>

          <div className="inst-h">Marking Scheme</div>
          <ul className="inst-list">
            <li><b>General Studies:</b> +2 for each correct answer, −0.66 for each wrong answer.</li>
            <li><b>CSAT (Aptitude):</b> +2.5 for each correct answer, −0.83 for each wrong answer.</li>
            <li><b>Numerical answer type:</b> No negative marking.</li>
            <li><b>Multiple-correct:</b> Full marks only if all correct options (and no wrong ones) are selected.</li>
          </ul>

          <div className="inst-h">Question Palette Legend</div>
          <div className="legend-grid">
            <div className="legend-row"><span className="lg-box" style={{ background: STATUS.answered.bg }}>1</span> Answered</div>
            <div className="legend-row"><span className="lg-box" style={{ background: STATUS.notAnswered.bg }}>2</span> Not Answered</div>
            <div className="legend-row"><span className="lg-box" style={{ background: STATUS.notVisited.bg, color: STATUS.notVisited.fg, border: "1.5px solid " + STATUS.notVisited.bd }}>3</span> Not Visited</div>
            <div className="legend-row"><span className="lg-box" style={{ background: STATUS.marked.bg }}>4</span> Marked for Review</div>
            <div className="legend-row"><span className="lg-box" style={{ background: STATUS.ansMarked.bg }}>5<span className="dot" /></span> Answered &amp; Marked</div>
          </div>

          <div className="consent">
            <input id="agree" type="checkbox" checked={agree} onChange={(e) => setAgree(e.target.checked)} />
            <label htmlFor="agree">I have read and understood all the instructions. I declare that I am not in possession of any prohibited material and I agree to abide by the examination rules.</label>
          </div>

          <div className="begin-row">
            <button className="begin-btn" disabled={!agree} onClick={onStart}>I am ready to begin →</button>
            <button onClick={onExit} style={{ marginLeft: 12, padding: "13px 22px", background: "#fff", border: "1.5px solid #cfe3e9", borderRadius: 10, color: "#43585f", fontWeight: 700, fontSize: 15, cursor: "pointer" }}>← Dashboard</button>
          </div>
        </div>
      </div>
    </div>
  );
}

/* ============================================================
   EXAM SCREEN
   ============================================================ */
function ExamScreen({ state, actions }) {
  const { secIdx, qIdx, answers, visited, marked, timeLeft } = state;
  const sec = EXAM.sections[secIdx];
  const q = sec.questions[qIdx];
  const danger = timeLeft <= 60;
  const candidate = "Priyadarshee Kumar";
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
              <div className="cand-sub">Roll No: BPSC2026-04417</div>
            </div>
          </div>
          <div className={"timer-box" + (danger ? " danger" : "")}>
            <div>
              <div className="timer-label">Time Left</div>
              <div className="timer-val">{fmt(timeLeft)}</div>
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
            <span className="q-no">Question {qIdx + 1}</span>
            <div className="q-tags">
              <span className="tag tag-topic">{q.topic}</span>
              <span className="tag tag-type">{q.type === "mcq" ? "Single Correct" : q.type === "multiple" ? "Multiple Correct" : "Numerical"}</span>
              <span className="tag tag-pos">+{q.marks}</span>
              {q.negative > 0 && <span className="tag tag-neg">−{q.negative}</span>}
            </div>
          </div>

          <div className="q-text">{q.text}</div>

          {q.type === "numerical" ? (
            <div className="num-in">
              <label>Enter your answer</label>
              <input type="number" inputMode="decimal" value={answers[q.id] ?? ""} placeholder="Type a number…"
                onChange={(e) => actions.setNumerical(q.id, e.target.value)} />
            </div>
          ) : (
            <div className="opts">
              {q.options.map((opt, i) => {
                const selected = q.type === "multiple"
                  ? Array.isArray(answers[q.id]) && answers[q.id].includes(i)
                  : answers[q.id] === i;
                return (
                  <button key={i} className={"opt" + (selected ? " sel" : "")}
                    onClick={() => q.type === "multiple" ? actions.toggleMulti(q.id, i) : actions.selectMcq(q.id, i)}>
                    <span className={"opt-mark" + (q.type === "multiple" ? " sq" : "")}>{selected ? "✓" : ""}</span>
                    <span className="opt-txt"><span className="opt-key">{optLetter(i)}.</span> {opt}</span>
                  </button>
                );
              })}
            </div>
          )}

          <div className="q-actions">
            <button className="btn btn-ghost" onClick={actions.prev}>← Previous</button>
            <button className="btn btn-ghost" onClick={() => actions.clear(q.id)}>Clear Response</button>
            <button className="btn btn-mark" onClick={() => actions.markNext(q.id)}>Mark for Review &amp; Next</button>
            <button className="btn btn-save" onClick={actions.saveNext}>Save &amp; Next</button>
          </div>
        </div>

        {/* PALETTE */}
        <div className="palette">
          <div className="pal-user">
            <div className="pal-av">{initials}</div>
            <div>
              <div style={{ fontWeight: 700, fontSize: 13.5 }}>{candidate}</div>
              <div style={{ fontSize: 11.5, color: "var(--muted)" }}>Attempt in progress</div>
            </div>
          </div>
          <div className="pal-legend">
            <div className="lg"><span className="lg-box" style={{ background: STATUS.answered.bg }} /> Answered</div>
            <div className="lg"><span className="lg-box" style={{ background: STATUS.notAnswered.bg }} /> Not Answered</div>
            <div className="lg"><span className="lg-box" style={{ background: STATUS.notVisited.bg, border: "1.5px solid " + STATUS.notVisited.bd }} /> Not Visited</div>
            <div className="lg"><span className="lg-box" style={{ background: STATUS.marked.bg }} /> Marked</div>
            <div className="lg" style={{ gridColumn: "1/-1" }}><span className="lg-box" style={{ background: STATUS.ansMarked.bg }}><span className="dot" /></span> Answered &amp; Marked for Review</div>
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
            <button className="submit-btn" onClick={actions.openSubmit}>Submit Test</button>
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
  return (
    <div className="overlay" onClick={onCancel}>
      <div className="modal" onClick={(e) => e.stopPropagation()}>
        <div className="modal-head">
          <h3>Submit your test?</h3>
          <p>Once submitted, you cannot change your answers. Please review the summary below.</p>
        </div>
        <div className="modal-stats">
          <div className="mstat"><div className="n" style={{ color: "var(--green)" }}>{counts.answered}</div><div className="l">Answered</div></div>
          <div className="mstat"><div className="n" style={{ color: "var(--red)" }}>{counts.unanswered}</div><div className="l">Unanswered</div></div>
          <div className="mstat"><div className="n" style={{ color: "#3a9bbf" }}>{counts.marked}</div><div className="l">Marked for Review</div></div>
          <div className="mstat"><div className="n" style={{ color: "var(--muted)" }}>{counts.notVisited}</div><div className="l">Not Visited</div></div>
        </div>
        <div className="modal-foot">
          <button className="btn btn-ghost" onClick={onCancel}>Resume Test</button>
          <button className="btn btn-danger" onClick={onConfirm}>Submit Now</button>
        </div>
      </div>
    </div>
  );
}

/* ============================================================
   RESULTS SCREEN
   ============================================================ */
function Results({ data, onRetake, onExit }) {
  const [filter, setFilter] = useState("all");
  const [open, setOpen] = useState(null);

  const grade = gradeFor(data.scorePct);
  const pctile = estPercentile(data.scorePct);

  const filtered = data.review.filter((r) =>
    filter === "all" ? true :
    filter === "correct" ? r.correct :
    filter === "wrong" ? (r.attempted && !r.correct) :
    !r.attempted
  );

  const cmpData = [
    { name: "You", value: +data.scorePct.toFixed(1), fill: grade.c },
    { name: "Avg. Student", value: 48, fill: "#94a8bc" },
    { name: "Topper", value: 91, fill: "#ec5a52" },
  ];
  const radarData = data.topics.map((t) => ({ topic: t.name, You: Math.round(t.acc) }));
  const timeData = data.review.map((r) => ({ q: r.id, time: Math.round(r.time), slow: r.slow }));

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
          <div className="pct-badge">★ Estimated Percentile: {pctile.toFixed(1)}</div>
          <div className="hero-stats">
            <div className="hs"><div className="n" style={{ color: "#7fe0a3" }}>{data.correct}</div><div className="l">Correct</div></div>
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
          <div className="panel-title">Section-wise Performance</div>
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
          <div className="panel-title">You vs Average vs Topper</div>
          <p className="panel-note">Your score % against typical and top performers.</p>
          <div style={{ height: 230 }}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={cmpData} margin={{ top: 16, right: 8, left: -18, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#eefbfd" />
                <XAxis dataKey="name" tick={{ fontSize: 12, fill: "#5e7d86" }} axisLine={false} tickLine={false} />
                <YAxis domain={[0, 100]} tick={{ fontSize: 11, fill: "#9bb4bc" }} axisLine={false} tickLine={false} unit="%" />
                <Tooltip cursor={{ fill: "rgba(20,150,180,.04)" }} formatter={(v) => [v + "%", "Score"]}
                  contentStyle={{ borderRadius: 10, border: "1px solid #dcecf0", fontSize: 13 }} />
                <Bar dataKey="value" radius={[7, 7, 0, 0]} maxBarSize={66}>
                  {cmpData.map((e, i) => <Cell key={i} fill={e.fill} />)}
                  <LabelList dataKey="value" position="top" formatter={(v) => v + "%"} style={{ fontSize: 12, fontWeight: 800, fill: "#33495d" }} />
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* TOPIC RADAR */}
        <div className="panel">
          <div className="panel-eyebrow">Diagnosis</div>
          <div className="panel-title">Topic Strength Map</div>
          <p className="panel-note">Accuracy across every topic tested.</p>
          <div style={{ height: 250 }}>
            <ResponsiveContainer width="100%" height="100%">
              <RadarChart data={radarData} outerRadius="72%">
                <PolarGrid stroke="#dde5ee" />
                <PolarAngleAxis dataKey="topic" tick={{ fontSize: 11, fill: "#5e7d86" }} />
                <PolarRadiusAxis domain={[0, 100]} tick={{ fontSize: 9, fill: "#b6cdd4" }} axisLine={false} />
                <Radar dataKey="You" stroke="#0e8fa8" fill="#0e8fa8" fillOpacity={0.28} strokeWidth={2} />
                <Tooltip formatter={(v) => [v + "%", "Accuracy"]} contentStyle={{ borderRadius: 10, border: "1px solid #dcecf0", fontSize: 13 }} />
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
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#eefbfd" />
                <XAxis dataKey="q" tick={{ fontSize: 11, fill: "#5e7d86" }} axisLine={false} tickLine={false} />
                <YAxis tick={{ fontSize: 11, fill: "#9bb4bc" }} axisLine={false} tickLine={false} unit="s" />
                <Tooltip cursor={{ fill: "rgba(20,150,180,.04)" }} formatter={(v) => [v + "s", "Time"]}
                  contentStyle={{ borderRadius: 10, border: "1px solid #dcecf0", fontSize: 13 }} />
                <Bar dataKey="time" radius={[5, 5, 0, 0]} maxBarSize={40}>
                  {timeData.map((e, i) => <Cell key={i} fill={e.slow ? "#cf4040" : "#149cba"} />)}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* AI IMPROVEMENT PLAN */}
        <div className="panel full">
          <div className="panel-eyebrow">Action Plan</div>
          <div className="panel-title">Your Personalised Improvement Plan</div>
          <p className="panel-note">Generated from this attempt. (In production this is enriched by the Claude API for deeper, topic-specific guidance.)</p>
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
                <div className="plan-ic" style={{ background: "#149cba" }}>⏱</div>
                <div className="plan-txt">
                  <h5>Speed — Manage your time better</h5>
                  <p>You spent too long on <b>{slowQ.length}</b> question{slowQ.length > 1 ? "s" : ""} ({slowQ.map((r) => r.id).join(", ")}). Practise a time cap per question and learn to flag-and-move instead of getting stuck.</p>
                </div>
              </div>
            )}
            {data.unattempted > 0 && (
              <div className="plan-item avg">
                <div className="plan-ic" style={{ background: "#3a9bbf" }}>○</div>
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
          <div className="panel-title">Question-by-Question Analysis</div>
          <p className="panel-note">Your answer, the correct answer, marks awarded, time spent, and a full explanation for every question.</p>
          <div className="rev-filters">
            {[["all", "All"], ["correct", "Correct"], ["wrong", "Wrong"], ["skipped", "Skipped"]].map(([k, label]) => (
              <button key={k} className={"rev-f" + (filter === k ? " active" : "")} onClick={() => setFilter(k)}>
                {label} ({k === "all" ? data.review.length : k === "correct" ? data.correct : k === "wrong" ? data.wrong : data.unattempted})
              </button>
            ))}
          </div>

          {filtered.map((r) => {
            const col = !r.attempted ? "#94a8bc" : r.correct ? SEM.strong : SEM.weak;
            const isOpen = open === r.id;
            return (
              <div className="rev-item" key={r.id}>
                <div className="rev-bar" onClick={() => setOpen(isOpen ? null : r.id)}>
                  <div className="rev-idx" style={{ background: col }}>{r.id}</div>
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
                        <div className={"rev-opt correct"}><span className="rev-opt-key">✓</span><span>Correct answer: {r.correctVal}</span></div>
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
        <button className="foot-btn primary" onClick={onExit}>Back to dashboard →</button>
      </div>
    </div>
  );
}

/* ============================================================
   APP (state machine + scoring)
   ============================================================ */
function App({ onExit }) {
  const [screen, setScreen] = useState("instructions"); // instructions | exam | result
  const [secIdx, setSecIdx] = useState(0);
  const [qIdx, setQIdx] = useState(0);
  const [answers, setAnswers] = useState({});
  const [visited, setVisited] = useState(new Set());
  const [marked, setMarked] = useState(new Set());
  const [timeLeft, setTimeLeft] = useState(EXAM.durationSec);
  const [showSubmit, setShowSubmit] = useState(false);
  const [results, setResults] = useState(null);

  const timeSpent = useRef({});
  const enteredAt = useRef(0);

  // flat order for navigation
  const order = useMemo(() => {
    const o = [];
    EXAM.sections.forEach((s, si) => s.questions.forEach((q, qi) => o.push({ si, qi, id: q.id })));
    return o;
  }, []);

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
    selectMcq: (qid, i) => { setAnswers((a) => ({ ...a, [qid]: i })); setVisited((v) => new Set(v).add(qid)); },
    toggleMulti: (qid, i) => setAnswers((a) => {
      const cur = Array.isArray(a[qid]) ? a[qid] : [];
      const next = cur.includes(i) ? cur.filter((x) => x !== i) : [...cur, i];
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

  const doSubmit = () => {
    flush(curId());
    // build review + aggregates
    const review = [];
    const sectionAgg = {};
    const topicAgg = {};
    let score = 0, maxScore = 0, attempted = 0, correctN = 0, wrongN = 0;

    const times = order.map(({ id }) => timeSpent.current[id] || 0);
    const avgTime = times.reduce((a, b) => a + b, 0) / (times.length || 1);
    const slowThreshold = Math.max(avgTime * 1.6, 25);

    EXAM.sections.forEach((s) => {
      sectionAgg[s.name] = { name: s.name, score: 0, max: 0, correct: 0, wrong: 0, unattempted: 0 };
      s.questions.forEach((q) => {
        const ans = answers[q.id];
        const ev = evaluate(q, ans);
        const t = timeSpent.current[q.id] || 0;
        maxScore += q.marks;
        score += ev.awarded;
        sectionAgg[s.name].max += q.marks;
        sectionAgg[s.name].score += ev.awarded;

        if (!topicAgg[q.topic]) topicAgg[q.topic] = { name: q.topic, correct: 0, total: 0 };
        topicAgg[q.topic].total += 1;

        if (ev.attempted) {
          attempted++;
          if (ev.correct) { correctN++; sectionAgg[s.name].correct++; topicAgg[q.topic].correct++; }
          else { wrongN++; sectionAgg[s.name].wrong++; }
        } else {
          sectionAgg[s.name].unattempted++;
        }

        review.push({
          id: q.id, text: q.text, type: q.type, options: q.options || [],
          topic: q.topic, explanation: q.explanation,
          yourVal: q.type === "numerical" ? (ev.attempted ? ans : null) : ans,
          correctVal: q.correct,
          attempted: ev.attempted, correct: ev.correct, awarded: ev.awarded,
          time: t, slow: t >= slowThreshold && t > 0,
        });
      });
    });

    const total = order.length;
    const unattempted = total - attempted;
    const accuracy = attempted > 0 ? (correctN / attempted) * 100 : 0;
    const scorePct = maxScore > 0 ? (Math.max(0, score) / maxScore) * 100 : 0;

    const topics = Object.values(topicAgg).map((t) => {
      const acc = t.total > 0 ? (t.correct / t.total) * 100 : 0;
      return { name: t.name, acc, band: bandFor(acc) };
    });

    setResults({
      score: +score.toFixed(2), maxScore, scorePct, attempted, total, unattempted,
      correct: correctN, wrong: wrongN, accuracy,
      timeUsed: EXAM.durationSec - timeLeft,
      sections: Object.values(sectionAgg),
      topics, review,
    });
    setShowSubmit(false);
    setScreen("result");
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
      {screen === "exam" && <ExamScreen state={{ secIdx, qIdx, answers, visited, marked, timeLeft }} actions={actions} />}
      {screen === "result" && results && <Results data={results} onRetake={retake} onExit={onExit} />}
      {showSubmit && <SubmitModal counts={counts} onCancel={() => setShowSubmit(false)} onConfirm={doSubmit} />}
    </div>
  );
}

return App;
})();

const AdminApp = (() => {
/* ============================================================
   HELPERS + PERSISTENCE (browser storage; falls back to memory)
   ============================================================ */
const uid = () =>
  (window.crypto && crypto.randomUUID ? crypto.randomUUID() : "id-" + Date.now() + "-" + Math.random().toString(36).slice(2, 8));

async function loadKey(key, fallback) {
  try {
    if (!window.storage) return fallback;
    const r = await window.storage.get(key, false);
    return r && r.value ? JSON.parse(r.value) : fallback;
  } catch { return fallback; }
}
async function saveKey(key, val) {
  try { if (!window.storage) return; await window.storage.set(key, JSON.stringify(val), false); } catch (e) { /* memory only */ }
}

const TYPE_LABEL = { mcq: "Single Correct", multiple: "Multiple Correct", numerical: "Numerical" };
const TYPE_COLOR = { mcq: { bg: "#e7eef5", fg: "#0e7d92" }, multiple: { bg: "#e3f3f7", fg: "#2a8fb0" }, numerical: { bg: "#e6f4ef", fg: "#1a6b3c" } };
const DIFF_COLOR = { easy: { bg: "#e8f6ee", fg: "#1f8a4c" }, medium: { bg: "#fff1ec", fg: "#ec5a52" }, hard: { bg: "#fbeaea", fg: "#cf4040" } };
const SUBJECTS = ["Polity", "Modern History", "Ancient History", "Medieval History", "Geography", "Economy", "Environment", "Science & Tech", "Current Affairs", "Number System", "Reasoning", "Reading Comprehension", "Quantitative Aptitude", "Data Interpretation"];
const fmtINR = (n) => "₹" + Number(n).toLocaleString("en-IN");

/* ============================================================
   SEED DATA  (first run only; then your edits persist)
   ============================================================ */
const SEED = {
  questions: [
    { id: uid(), subject: "Polity", topic: "Fundamental Rights", type: "mcq", difficulty: "medium",
      body: "Which Article of the Indian Constitution is described by Dr. B. R. Ambedkar as the 'heart and soul' of the Constitution?",
      options: [{ id: uid(), body: "Article 14", isCorrect: false }, { id: uid(), body: "Article 19", isCorrect: false }, { id: uid(), body: "Article 32", isCorrect: true }, { id: uid(), body: "Article 21", isCorrect: false }],
      numericAnswer: null, numericTolerance: 0.01, marksCorrect: 2, marksWrong: 0.66,
      explanation: "Article 32 (Right to Constitutional Remedies) lets citizens move the Supreme Court directly to enforce Fundamental Rights." },
    { id: uid(), subject: "Modern History", topic: "National Movement", type: "mcq", difficulty: "easy",
      body: "The Non-Cooperation Movement was formally launched by Mahatma Gandhi in which year?",
      options: [{ id: uid(), body: "1919", isCorrect: false }, { id: uid(), body: "1920", isCorrect: true }, { id: uid(), body: "1922", isCorrect: false }, { id: uid(), body: "1930", isCorrect: false }],
      numericAnswer: null, numericTolerance: 0.01, marksCorrect: 2, marksWrong: 0.66,
      explanation: "Launched in 1920 (Nagpur session) and withdrawn in February 1922 after Chauri Chaura." },
    { id: uid(), subject: "Geography", topic: "Drainage", type: "mcq", difficulty: "medium",
      body: "Which is the longest river of Peninsular India?",
      options: [{ id: uid(), body: "Krishna", isCorrect: false }, { id: uid(), body: "Godavari", isCorrect: true }, { id: uid(), body: "Cauvery", isCorrect: false }, { id: uid(), body: "Narmada", isCorrect: false }],
      numericAnswer: null, numericTolerance: 0.01, marksCorrect: 2, marksWrong: 0.66,
      explanation: "The Godavari (~1465 km) is the longest peninsular river, called 'Dakshina Ganga'." },
    { id: uid(), subject: "Economy", topic: "Taxation", type: "multiple", difficulty: "medium",
      body: "Which of the following are DIRECT taxes? (Select all that apply)",
      options: [{ id: uid(), body: "Income Tax", isCorrect: true }, { id: uid(), body: "GST", isCorrect: false }, { id: uid(), body: "Corporate Tax", isCorrect: true }, { id: uid(), body: "Customs Duty", isCorrect: false }],
      numericAnswer: null, numericTolerance: 0.01, marksCorrect: 2, marksWrong: 0.66,
      explanation: "Income Tax and Corporate Tax are direct taxes; GST and Customs are indirect." },
    { id: uid(), subject: "Environment", topic: "Conservation", type: "mcq", difficulty: "easy",
      body: "In which year was 'Project Tiger' launched in India?",
      options: [{ id: uid(), body: "1972", isCorrect: false }, { id: uid(), body: "1973", isCorrect: true }, { id: uid(), body: "1985", isCorrect: false }, { id: uid(), body: "1991", isCorrect: false }],
      numericAnswer: null, numericTolerance: 0.01, marksCorrect: 2, marksWrong: 0.66,
      explanation: "Project Tiger was launched in 1973 from Jim Corbett National Park." },
    { id: uid(), subject: "Number System", topic: "Unit Digit", type: "mcq", difficulty: "medium",
      body: "What is the unit (last) digit of 7^105?",
      options: [{ id: uid(), body: "1", isCorrect: false }, { id: uid(), body: "3", isCorrect: false }, { id: uid(), body: "7", isCorrect: true }, { id: uid(), body: "9", isCorrect: false }],
      numericAnswer: null, numericTolerance: 0.01, marksCorrect: 2.5, marksWrong: 0.83,
      explanation: "Unit digit of 7 cycles 7,9,3,1 (period 4). 105 mod 4 = 1 → 7." },
    { id: uid(), subject: "Quantitative Aptitude", topic: "Speed Distance Time", type: "numerical", difficulty: "medium",
      body: "A train 150 m long crosses a pole in 15 seconds. What is its speed in km/h?",
      options: [], numericAnswer: 36, numericTolerance: 0.01, marksCorrect: 2.5, marksWrong: 0,
      explanation: "150/15 = 10 m/s = 10 × 18/5 = 36 km/h." },
    { id: uid(), subject: "Reading Comprehension", topic: "Inference", type: "mcq", difficulty: "hard",
      body: "Passage: 'Economic growth without equitable distribution deepens social fault lines...' What does it most strongly imply?",
      options: [{ id: uid(), body: "GDP growth should be every nation's primary goal", isCorrect: false }, { id: uid(), body: "Development should be judged by how widely benefits are shared", isCorrect: true }, { id: uid(), body: "The poor cause slow growth", isCorrect: false }, { id: uid(), body: "Social fault lines are unrelated to economics", isCorrect: false }],
      numericAnswer: null, numericTolerance: 0.01, marksCorrect: 2.5, marksWrong: 0.83,
      explanation: "The inference is that real development is about distribution, not aggregate output alone." },
  ],
  courses: [],
  batches: [],
  tests: [],
  materials: [],
};

/* build courses/batches/tests/materials referencing seed question ids */
(() => {
  const c1 = uid(), c2 = uid();
  SEED.courses = [
    { id: c1, title: "BPSC Prelims 2026 — Foundation", examTarget: "BPSC Prelims 2026", description: "Complete GS + CSAT coverage with weekly mocks.", isPublished: true, createdAt: Date.now() },
    { id: c2, title: "UPSC CSAT Crash Course", examTarget: "UPSC Prelims 2026", description: "Aptitude, reasoning & comprehension sprint.", isPublished: false, createdAt: Date.now() },
  ];
  const b1 = uid(), b2 = uid(), b3 = uid();
  SEED.batches = [
    { id: b1, courseId: c1, name: "Foundation Batch — Jan 2026", price: 999, seatLimit: 200, startDate: "2026-01-15", endDate: "2026-06-30", isActive: true },
    { id: b2, courseId: c1, name: "Lifetime Founding Batch", price: 1499, seatLimit: 100, startDate: "2026-01-01", endDate: "", isActive: true },
    { id: b3, courseId: c2, name: "CSAT Sprint — Feb", price: 499, seatLimit: 150, startDate: "2026-02-01", endDate: "2026-04-30", isActive: true },
  ];
  const gs = SEED.questions.filter((q) => ["Polity", "Modern History", "Geography", "Economy", "Environment"].includes(q.subject)).map((q) => q.id);
  const csat = SEED.questions.filter((q) => ["Number System", "Quantitative Aptitude", "Reading Comprehension"].includes(q.subject)).map((q) => q.id);
  SEED.tests = [
    { id: uid(), title: "BPSC Full Mock 01", seriesTitle: "BPSC Prelims Test Series 2026", durationMin: 20, shuffleQuestions: true, shuffleOptions: true, isPublished: true,
      sections: [{ id: uid(), name: "General Studies", questionIds: gs }, { id: uid(), name: "CSAT (Aptitude)", questionIds: csat }] },
  ];
  SEED.materials = [
    { id: uid(), title: "Polity NCERT Quick Notes", type: "pdf", url: "https://example.com/polity-notes.pdf", isFree: true, batchId: b1 },
    { id: uid(), title: "Modern History — Crash Revision", type: "video", url: "https://youtube.com/watch?v=demo", isFree: true, batchId: b1 },
  ];
})();

const SAMPLE_STUDENTS = [
  { name: "Rahul Verma", email: "rahul.v@gmail.com", batch: "Foundation Batch — Jan 2026", attempts: 12, avg: 64 },
  { name: "Sneha Kumari", email: "sneha.k@gmail.com", batch: "Lifetime Founding Batch", attempts: 18, avg: 78 },
  { name: "Amit Raj", email: "amit.raj@gmail.com", batch: "Foundation Batch — Jan 2026", attempts: 7, avg: 52 },
  { name: "Pooja Singh", email: "pooja.s@gmail.com", batch: "CSAT Sprint — Feb", attempts: 9, avg: 71 },
  { name: "Vikash Anand", email: "vikash.a@gmail.com", batch: "Lifetime Founding Batch", attempts: 21, avg: 83 },
];
const SAMPLE_PAYMENTS = [
  { name: "Vikash Anand", item: "Lifetime Founding Batch", amount: 1499, status: "paid", date: "2026-06-12" },
  { name: "Sneha Kumari", item: "Lifetime Founding Batch", amount: 1499, status: "paid", date: "2026-06-11" },
  { name: "Pooja Singh", item: "CSAT Sprint — Feb", amount: 499, status: "paid", date: "2026-06-10" },
  { name: "Rahul Verma", item: "Foundation Batch — Jan 2026", amount: 999, status: "paid", date: "2026-06-09" },
  { name: "Amit Raj", item: "Foundation Batch — Jan 2026", amount: 999, status: "failed", date: "2026-06-08" },
];

/* ============================================================
   STYLES
   ============================================================ */
const CSS = `
:root{
  --navy:#0e8fa8; --navy-2:#0a6173; --navy-3:#084e5c; --gold:#f76b6b; --gold-2:#ec5a52;
  --bg:#eefbfd; --card:#ffffff; --ink:#0e3540; --muted:#5e7d86; --line:#dcecf0;
  --green:#1f8a4c; --amber:#ec5a52; --red:#cf4040; --blue:#149cba;
  --grn-bg:#e8f6ee; --amb-bg:#fff1ec; --red-bg:#fbeaea;
}
*{box-sizing:border-box}
.ad-root{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--ink);
  font-variant-numeric:tabular-nums;line-height:1.5;background:var(--bg);min-height:100vh;display:flex}
.ad-root button{font-family:inherit;cursor:pointer;border:none;background:none}
.ad-root input,.ad-root textarea,.ad-root select{font-family:inherit}

/* SIDEBAR */
.sb{width:248px;background:linear-gradient(180deg,#0e6273,#0b4f5e);color:#cfeaf0;flex:0 0 auto;display:flex;flex-direction:column;position:sticky;top:0;height:100vh;z-index:40}
.sb-brand{padding:20px 20px 16px;border-bottom:1px solid rgba(255,255,255,.08)}
.sb-logo{display:flex;align-items:center;gap:11px}
.sb-logo-mark{width:36px;height:36px;border-radius:9px;background:linear-gradient(135deg,var(--gold) 0%,var(--gold-2) 100%);display:grid;place-items:center;color:#fff;font-weight:800;font-size:16px;flex:0 0 auto}
.sb-name{font-weight:800;font-size:15px;color:#fff;line-height:1.15}
.sb-tag{font-size:11px;color:#bfe6ee}
.sb-nav{flex:1;padding:12px 12px;overflow-y:auto}
.sb-group{font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:#8fb8c4;font-weight:700;margin:16px 10px 8px}
.sb-item{display:flex;align-items:center;gap:11px;padding:10px 12px;border-radius:9px;font-size:14px;font-weight:600;color:#bdcfe2;width:100%;text-align:left;transition:.13s;margin-bottom:2px;position:relative}
.sb-item:hover{background:rgba(255,255,255,.06);color:#fff}
.sb-item.active{background:rgba(255,255,255,.1);color:#fff}
.sb-item.active::before{content:"";position:absolute;left:0;top:8px;bottom:8px;width:3px;border-radius:3px;background:var(--gold)}
.sb-badge{margin-left:auto;background:rgba(255,255,255,.14);font-size:11px;font-weight:700;padding:1px 8px;border-radius:20px}
.sb-foot{padding:14px 16px;border-top:1px solid rgba(255,255,255,.08);font-size:11.5px;color:#bfe6ee}

/* MAIN */
.main{flex:1;min-width:0;display:flex;flex-direction:column}
.topbar{background:#fff;border-bottom:1px solid var(--line);padding:14px 26px;display:flex;align-items:center;justify-content:space-between;gap:14px;position:sticky;top:0;z-index:30}
.topbar h1{margin:0;font-size:19px;font-weight:800;letter-spacing:-.01em}
.topbar .sub{font-size:12.5px;color:var(--muted);margin-top:1px}
.tb-right{display:flex;align-items:center;gap:12px}
.tb-admin{display:flex;align-items:center;gap:10px}
.tb-av{width:36px;height:36px;border-radius:9px;background:var(--navy);color:#fff;display:grid;place-items:center;font-weight:800;font-size:13px}
.tb-admin-name{font-size:13.5px;font-weight:700;line-height:1.1}
.tb-admin-role{font-size:11px;color:var(--muted)}
.hamburger{display:none;width:38px;height:38px;border-radius:9px;border:1px solid var(--line);align-items:center;justify-content:center}
.content{padding:26px;max-width:1240px;width:100%;margin:0 auto}

/* BUTTONS */
.btn{display:inline-flex;align-items:center;gap:7px;font-size:13.5px;font-weight:700;padding:10px 16px;border-radius:9px;transition:.14s;border:1.5px solid transparent;white-space:nowrap}
.btn-primary{background:linear-gradient(135deg,#1bb6d2,#0e9bb5);color:#fff;box-shadow:0 5px 16px rgba(20,150,180,.38)}
.btn-primary:hover{background:linear-gradient(135deg,#16a8c4,#0c8aa3);box-shadow:0 8px 22px rgba(20,150,180,.48)}
.btn-gold{background:var(--gold-2);color:#fff}
.btn-gold:hover{filter:brightness(.94)}
.btn-ghost{background:#fff;border-color:#cfe3e9;color:#43585f}
.btn-ghost:hover{border-color:#a8d4de;background:#f1fafc}
.btn-danger{background:var(--red);color:#fff}
.btn-danger:hover{filter:brightness(.94)}
.btn-sm{padding:7px 12px;font-size:12.5px}
.btn-icon{width:34px;height:34px;padding:0;justify-content:center;border-radius:8px;border:1.5px solid var(--line);background:#fff;color:#5e7d86}
.btn-icon:hover{border-color:#a8d4de;color:var(--navy);background:#f1fafc}
.btn-icon.danger:hover{border-color:#e8b4b4;color:var(--red);background:var(--red-bg)}

/* CARDS / SECTIONS */
.panel{background:var(--card);border:1px solid var(--line);border-radius:14px;box-shadow:0 1px 3px rgba(20,120,140,.05)}
.panel-pad{padding:22px}
.sec-head{display:flex;align-items:center;justify-content:space-between;gap:14px;margin-bottom:18px;flex-wrap:wrap}
.sec-head h2{margin:0;font-size:16px;font-weight:800}
.sec-head .note{font-size:12.5px;color:var(--muted);margin-top:2px}

/* STAT CARDS */
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(168px,1fr));gap:16px;margin-bottom:22px}
.stat{background:#fff;border:1px solid var(--line);border-radius:13px;padding:18px;box-shadow:0 1px 3px rgba(20,120,140,.05)}
.stat-ic{width:40px;height:40px;border-radius:10px;display:grid;place-items:center;margin-bottom:13px}
.stat-n{font-size:27px;font-weight:800;line-height:1;letter-spacing:-.02em}
.stat-l{font-size:12.5px;color:var(--muted);margin-top:6px;font-weight:600}
.stat-sub{font-size:11.5px;color:#90a3b6;margin-top:3px}

/* TWO-COL */
.cols{display:grid;grid-template-columns:1fr 1fr;gap:18px}
@media(max-width:900px){.cols{grid-template-columns:1fr}}

/* TOOLBAR (filters) */
.toolbar{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:18px}
.search{flex:1;min-width:200px;display:flex;align-items:center;gap:9px;background:#fff;border:1.5px solid var(--line);border-radius:9px;padding:9px 13px}
.search input{border:none;outline:none;flex:1;font-size:14px;background:transparent;color:var(--ink)}
.search svg{color:#9bb4bc;flex:0 0 auto}
.sel{background:#fff;border:1.5px solid var(--line);border-radius:9px;padding:9px 12px;font-size:13.5px;color:#43585f;outline:none;cursor:pointer}
.sel:focus{border-color:var(--navy)}

/* TABLE */
.tbl-wrap{overflow-x:auto;border:1px solid var(--line);border-radius:13px;background:#fff}
table.tbl{width:100%;border-collapse:collapse;min-width:640px}
.tbl thead th{text-align:left;font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);font-weight:700;padding:13px 16px;border-bottom:1px solid var(--line);background:#f6fdfe;white-space:nowrap}
.tbl tbody td{padding:14px 16px;border-bottom:1px solid #eefbfd;font-size:13.5px;vertical-align:middle}
.tbl tbody tr:last-child td{border-bottom:none}
.tbl tbody tr:hover{background:#f9fbfd}
.q-cell{max-width:440px}
.q-body{font-weight:600;color:#103a44;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.q-sub{font-size:11.5px;color:var(--muted);margin-top:4px}
.row-actions{display:flex;gap:8px;justify-content:flex-end}

/* BADGES */
.badge{display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:700;padding:3px 9px;border-radius:20px;white-space:nowrap}
.badge-topic{background:#e3f3f7;color:#2a8fb0}
.marks{font-weight:800;font-size:13px}
.marks .pos{color:var(--green)}
.marks .neg{color:var(--red)}
.dot-pub{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:700}
.dot{width:8px;height:8px;border-radius:50%}

/* EMPTY */
.empty{text-align:center;padding:48px 20px;color:var(--muted)}
.empty-ic{width:56px;height:56px;border-radius:14px;background:#eefbfd;display:grid;place-items:center;margin:0 auto 14px;color:#9bb4bc}
.empty h3{margin:0 0 5px;font-size:16px;color:var(--ink);font-weight:700}
.empty p{margin:0 0 16px;font-size:13.5px}

/* MODAL */
.overlay{position:fixed;inset:0;background:rgba(13,27,42,.55);display:flex;align-items:flex-start;justify-content:center;z-index:60;padding:30px 18px;overflow-y:auto;backdrop-filter:blur(2px)}
.modal{background:#fff;border-radius:16px;width:100%;max-width:600px;box-shadow:0 24px 60px rgba(0,0,0,.3);margin:auto}
.modal.wide{max-width:820px}
.modal-head{display:flex;align-items:center;justify-content:space-between;padding:20px 24px;border-bottom:1px solid var(--line);position:sticky;top:0;background:#fff;border-radius:16px 16px 0 0;z-index:2}
.modal-head h3{margin:0;font-size:17px;font-weight:800}
.modal-head .x{width:34px;height:34px;border-radius:8px;display:grid;place-items:center;color:#7e93a8}
.modal-head .x:hover{background:#f1f5f9;color:var(--ink)}
.modal-body{padding:22px 24px}
.modal-foot{padding:16px 24px;display:flex;gap:11px;justify-content:flex-end;border-top:1px solid var(--line);background:#f6fdfe;border-radius:0 0 16px 16px;position:sticky;bottom:0}

/* FORM */
.field{margin-bottom:16px}
.field-row{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:560px){.field-row{grid-template-columns:1fr}}
.field label{display:block;font-size:12.5px;font-weight:700;color:#3a5258;margin-bottom:6px}
.field .req{color:var(--red)}
.inp{width:100%;padding:11px 13px;border:1.5px solid #cfe3e9;border-radius:9px;font-size:14px;color:var(--ink);outline:none;transition:.13s;background:#fff}
.inp:focus{border-color:var(--navy);box-shadow:0 0 0 3px rgba(20,150,180,.1)}
textarea.inp{resize:vertical;min-height:74px;line-height:1.55}
.hint{font-size:11.5px;color:var(--muted);margin-top:5px}
.seg{display:flex;gap:8px;flex-wrap:wrap}
.seg button{flex:1;min-width:90px;padding:10px;border:1.5px solid #cfe3e9;border-radius:9px;font-size:13px;font-weight:700;color:#5e7d86;background:#fff;transition:.13s}
.seg button.on{border-color:var(--navy);background:#e6f6fa;color:var(--navy)}
.opt-edit{display:flex;align-items:center;gap:10px;margin-bottom:9px}
.opt-edit .pick{width:36px;height:36px;border-radius:8px;border:1.5px solid #cfe3e9;display:grid;place-items:center;flex:0 0 auto;color:#fff;background:#fff;transition:.13s}
.opt-edit .pick.on{background:var(--green);border-color:var(--green)}
.opt-edit .inp{flex:1}
.opt-edit .rm{width:34px;height:34px;border-radius:8px;display:grid;place-items:center;color:#a9b8c6;flex:0 0 auto}
.opt-edit .rm:hover{color:var(--red);background:var(--red-bg)}
.add-opt{font-size:13px;font-weight:700;color:var(--navy);display:inline-flex;align-items:center;gap:6px;padding:7px 0}
.form-err{display:flex;align-items:center;gap:8px;background:var(--red-bg);border:1px solid #f1cccc;color:#a13232;font-size:13px;font-weight:600;padding:11px 14px;border-radius:9px;margin-bottom:16px}

/* TEST BUILDER */
.tb-section{border:1px solid var(--line);border-radius:12px;margin-bottom:14px;overflow:hidden}
.tb-section-head{display:flex;align-items:center;gap:12px;padding:13px 16px;background:#f6fdfe;border-bottom:1px solid var(--line)}
.tb-section-head .inp{max-width:280px}
.tb-section-body{padding:14px 16px}
.picked-q{display:flex;align-items:center;gap:11px;padding:10px 12px;border:1px solid #eefbfd;border-radius:9px;margin-bottom:8px;background:#fff}
.picked-q .n{width:26px;height:26px;border-radius:7px;background:var(--navy);color:#fff;display:grid;place-items:center;font-size:12px;font-weight:800;flex:0 0 auto}
.picked-q .t{flex:1;min-width:0;font-size:13px;color:#2a4750;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.picker-item{display:flex;align-items:flex-start;gap:11px;padding:11px 13px;border:1.5px solid #eefbfd;border-radius:9px;margin-bottom:8px;cursor:pointer;transition:.12s}
.picker-item:hover{border-color:#bcd0e4;background:#f6fdfe}
.picker-item.on{border-color:var(--navy);background:#e6f6fa}
.picker-check{width:22px;height:22px;border-radius:6px;border:2px solid #b6cdd4;display:grid;place-items:center;flex:0 0 auto;margin-top:1px;color:#fff}
.picker-item.on .picker-check{background:var(--navy);border-color:var(--navy)}

/* BANNER */
.banner{display:flex;align-items:center;gap:11px;background:#e6f6fa;border:1px solid #cfe0f3;color:#0e8fa8;font-size:13px;padding:12px 16px;border-radius:11px;margin-bottom:20px}
.banner.sample{background:var(--amb-bg);border-color:#f0dfba;color:#8a6a14}

/* BREAKDOWN LIST */
.bd-row{display:flex;align-items:center;gap:12px;margin-bottom:11px}
.bd-name{font-size:13px;font-weight:600;width:160px;flex:0 0 auto;color:#2a4750;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bd-track{flex:1;height:9px;background:#eefbfd;border-radius:6px;overflow:hidden}
.bd-fill{height:100%;border-radius:6px;background:var(--navy)}
.bd-val{font-size:12.5px;font-weight:700;color:var(--muted);width:30px;text-align:right;flex:0 0 auto}

/* TOAST */
.toasts{position:fixed;bottom:22px;right:22px;display:flex;flex-direction:column;gap:10px;z-index:90}
.toast{display:flex;align-items:center;gap:10px;background:var(--ink);color:#fff;font-size:13.5px;font-weight:600;padding:12px 16px;border-radius:11px;box-shadow:0 10px 30px rgba(0,0,0,.25);animation:slideIn .25s ease}
.toast svg{color:#7fe0a3;flex:0 0 auto}
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
function QuestionForm({ initial, onSave, onClose }) {
  const blank = {
    id: null, subject: "", topic: "", type: "mcq", difficulty: "medium", body: "",
    options: [{ id: uid(), body: "", isCorrect: true }, { id: uid(), body: "", isCorrect: false }, { id: uid(), body: "", isCorrect: false }, { id: uid(), body: "", isCorrect: false }],
    numericAnswer: "", numericTolerance: 0.01, marksCorrect: 2, marksWrong: 0.66, explanation: "",
  };
  const [f, setF] = useState(() => initial ? JSON.parse(JSON.stringify(initial)) : blank);
  const [err, setErr] = useState("");
  const set = (k, v) => setF((p) => ({ ...p, [k]: v }));

  const setType = (t) => {
    setF((p) => {
      let opts = p.options;
      if (t === "mcq") {
        // keep only first correct
        let seen = false;
        opts = p.options.map((o) => {
          if (o.isCorrect && !seen) { seen = true; return o; }
          return { ...o, isCorrect: false };
        });
        if (!seen && opts[0]) opts = opts.map((o, i) => i === 0 ? { ...o, isCorrect: true } : o);
      }
      return { ...p, type: t, options: opts };
    });
  };
  const setOpt = (id, body) => set("options", f.options.map((o) => o.id === id ? { ...o, body } : o));
  const toggleCorrect = (id) => set("options", f.options.map((o) => {
    if (f.type === "mcq") return { ...o, isCorrect: o.id === id };
    return o.id === id ? { ...o, isCorrect: !o.isCorrect } : o;
  }));
  const addOpt = () => set("options", [...f.options, { id: uid(), body: "", isCorrect: false }]);
  const rmOpt = (id) => { if (f.options.length <= 2) return; set("options", f.options.filter((o) => o.id !== id)); };

  const submit = () => {
    if (!f.body.trim()) return setErr("Question text is required.");
    if (f.type === "numerical") {
      if (f.numericAnswer === "" || isNaN(parseFloat(f.numericAnswer))) return setErr("Enter a valid numerical answer.");
    } else {
      const filled = f.options.filter((o) => o.body.trim());
      if (filled.length < 2) return setErr("Add at least 2 options with text.");
      const correct = f.options.filter((o) => o.isCorrect && o.body.trim());
      if (f.type === "mcq" && correct.length !== 1) return setErr("Mark exactly one correct option.");
      if (f.type === "multiple" && correct.length < 1) return setErr("Mark at least one correct option.");
    }
    const clean = {
      ...f,
      id: f.id || uid(),
      subject: f.subject.trim() || "General",
      topic: f.topic.trim(),
      marksCorrect: parseFloat(f.marksCorrect) || 0,
      marksWrong: parseFloat(f.marksWrong) || 0,
      numericAnswer: f.type === "numerical" ? parseFloat(f.numericAnswer) : null,
      numericTolerance: parseFloat(f.numericTolerance) || 0.01,
      options: f.type === "numerical" ? [] : f.options.filter((o) => o.body.trim()),
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
        <Field label="Topic"><input className="inp" value={f.topic} placeholder="e.g. Fundamental Rights" onChange={(e) => set("topic", e.target.value)} /></Field>
      </div>

      <Field label="Question type" req>
        <div className="seg">
          {["mcq", "multiple", "numerical"].map((t) => (
            <button key={t} className={f.type === t ? "on" : ""} onClick={() => setType(t)}>{TYPE_LABEL[t]}</button>
          ))}
        </div>
      </Field>

      <Field label="Question text" req>
        <textarea className="inp" rows={3} value={f.body} placeholder="Type the full question…" onChange={(e) => set("body", e.target.value)} />
      </Field>

      {f.type === "numerical" ? (
        <div className="field-row">
          <Field label="Correct numerical answer" req><input className="inp" type="number" value={f.numericAnswer} placeholder="e.g. 36" onChange={(e) => set("numericAnswer", e.target.value)} /></Field>
          <Field label="Tolerance (±)" hint="How much deviation counts as correct"><input className="inp" type="number" value={f.numericTolerance} onChange={(e) => set("numericTolerance", e.target.value)} /></Field>
        </div>
      ) : (
        <Field label={f.type === "mcq" ? "Options (tap the box to mark the correct one)" : "Options (tap boxes to mark all correct ones)"} req>
          {f.options.map((o, i) => (
            <div className="opt-edit" key={o.id}>
              <button className={"pick" + (o.isCorrect ? " on" : "")} onClick={() => toggleCorrect(o.id)} title="Mark correct">
                {o.isCorrect && <Check size={16} />}
              </button>
              <input className="inp" value={o.body} placeholder={"Option " + String.fromCharCode(65 + i)} onChange={(e) => setOpt(o.id, e.target.value)} />
              <button className="rm" onClick={() => rmOpt(o.id)} title="Remove"><Trash2 size={16} /></button>
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
      </Field>
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
    "subject": "Quantitative Aptitude",
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
        <pre style={{ margin: 0, background: "#0a6173", color: "#d6f1f7", padding: 16, borderRadius: 10, fontSize: 12, overflowX: "auto", lineHeight: 1.5 }}>{IMPORT_EXAMPLE}</pre>
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
            <div style={{ fontSize: 13.5, fontWeight: 600, color: "#103a44" }}>{x.body}</div>
            <div style={{ display: "flex", gap: 7, marginTop: 6, flexWrap: "wrap" }}>
              <Badge color={{ bg: "#eefbfd", fg: "#5e7d86" }}>{x.subject}</Badge>
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
function TestEditor({ initial, bank, onSave, onCancel, toast }) {
  const blank = { id: null, title: "", seriesTitle: "", durationMin: 20, shuffleQuestions: true, shuffleOptions: true, isPublished: false, sections: [{ id: uid(), name: "Section 1", questionIds: [] }] };
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
    onSave({ ...t, id: t.id || uid(), title: t.title.trim(), durationMin: parseInt(t.durationMin) || 20, isPublished: publish ?? t.isPublished });
  };

  const pickerSection = t.sections.find((s) => s.id === picker);

  return (
    <div>
      <button className="btn btn-ghost btn-sm" onClick={onCancel} style={{ marginBottom: 16 }}><ArrowLeft size={15} />Back to tests</button>

      {err && <div className="form-err"><AlertCircle size={17} />{err}</div>}

      <div className="panel panel-pad" style={{ marginBottom: 18 }}>
        <div className="field-row">
          <Field label="Test title" req><input className="inp" value={t.title} placeholder="e.g. BPSC Full Mock 02" onChange={(e) => set("title", e.target.value)} /></Field>
          <Field label="Test series"><input className="inp" value={t.seriesTitle} placeholder="e.g. BPSC Prelims Test Series 2026" onChange={(e) => set("seriesTitle", e.target.value)} /></Field>
        </div>
        <div className="field-row">
          <Field label="Duration (minutes)" req><input className="inp" type="number" value={t.durationMin} onChange={(e) => set("durationMin", e.target.value)} /></Field>
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

      {t.sections.map((s, si) => (
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
                  <button className="rm" onClick={() => rmQ(s.id, qid)} style={{ width: 30, height: 30, borderRadius: 7, display: "grid", placeItems: "center", color: "#a9b8c6" }}><X size={16} /></button>
                </div>
              );
            })}
          </div>
        </div>
      ))}

      <button className="btn btn-ghost" onClick={addSection} style={{ marginBottom: 22 }}><Plus size={15} />Add section</button>

      <div style={{ display: "flex", gap: 11, justifyContent: "flex-end", flexWrap: "wrap" }}>
        <button className="btn btn-ghost" onClick={() => submit(false)}><Save size={16} />Save as draft</button>
        <button className="btn btn-gold" onClick={() => submit(true)}><Eye size={16} />Save &amp; publish</button>
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
  const [f, setF] = useState(initial || { id: null, title: "", type: "pdf", url: "", isFree: true, batchId: batches[0]?.id || "" });
  const [err, setErr] = useState("");
  const set = (k, v) => setF((p) => ({ ...p, [k]: v }));
  const submit = () => {
    if (!f.title.trim()) return setErr("Title is required.");
    onSave({ ...f, id: f.id || uid(), title: f.title.trim() });
  };
  return (
    <Modal title={initial ? "Edit material" : "Add material"} onClose={onClose}
      footer={<><button className="btn btn-ghost" onClick={onClose}>Cancel</button><button className="btn btn-primary" onClick={submit}><Save size={16} />Save</button></>}>
      {err && <div className="form-err"><AlertCircle size={17} />{err}</div>}
      <div className="banner"><AlertCircle size={17} />In production, files upload to Supabase Storage. Here, paste a URL (PDF link / YouTube / Drive).</div>
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
      <Field label="URL"><input className="inp" value={f.url} placeholder="https://…" onChange={(e) => set("url", e.target.value)} /></Field>
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
      <p style={{ margin: 0, fontSize: 14.5, color: "#2a4750" }}>{message}</p>
    </Modal>
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
    { id: "courses", label: "Courses & Batches", icon: GraduationCap },
    { id: "materials", label: "Free Materials", icon: FolderOpen },
  ]},
  { group: "People & Revenue", items: [
    { id: "students", label: "Students", icon: Users },
    { id: "sales", label: "Sales", icon: IndianRupee },
  ]},
];
const PAGE_META = {
  overview: { title: "Dashboard", sub: "Your platform at a glance" },
  questions: { title: "Question Bank", sub: "Create and manage all questions" },
  tests: { title: "Tests & Series", sub: "Build tests from your question bank" },
  courses: { title: "Courses & Batches", sub: "Organise your offerings and pricing" },
  materials: { title: "Free Materials", sub: "PDFs, notes and videos for students" },
  students: { title: "Students", sub: "Enrolled learners and their activity" },
  sales: { title: "Sales", sub: "Revenue and transactions" },
};

function App({ onLogout }) {
  const [view, setView] = useState("overview");
  const [loading, setLoading] = useState(true);
  const [sbOpen, setSbOpen] = useState(false);
  const loaded = useRef(false);

  const [questions, setQuestions] = useState([]);
  const [courses, setCourses] = useState([]);
  const [batches, setBatches] = useState([]);
  const [tests, setTests] = useState([]);
  const [materials, setMaterials] = useState([]);

  const [toasts, setToasts] = useState([]);
  const [confirm, setConfirm] = useState(null);

  const toast = (msg) => {
    const id = uid();
    setToasts((t) => [...t, { id, msg }]);
    setTimeout(() => setToasts((t) => t.filter((x) => x.id !== id)), 2600);
  };
  const askDelete = (message, onYes) => setConfirm({ message, onYes });

  /* load once */
  useEffect(() => {
    (async () => {
      let seeded = false;
      try { if (window.storage) { const r = await window.storage.get("admin:seeded", false); seeded = r && r.value === "true"; } } catch {}
      if (seeded) {
        setQuestions(await loadKey("admin:questions", SEED.questions));
        setCourses(await loadKey("admin:courses", SEED.courses));
        setBatches(await loadKey("admin:batches", SEED.batches));
        setTests(await loadKey("admin:tests", SEED.tests));
        setMaterials(await loadKey("admin:materials", SEED.materials));
      } else {
        setQuestions(SEED.questions); setCourses(SEED.courses); setBatches(SEED.batches); setTests(SEED.tests); setMaterials(SEED.materials);
        saveKey("admin:questions", SEED.questions); saveKey("admin:courses", SEED.courses); saveKey("admin:batches", SEED.batches);
        saveKey("admin:tests", SEED.tests); saveKey("admin:materials", SEED.materials);
        try { if (window.storage) await window.storage.set("admin:seeded", "true", false); } catch {}
      }
      loaded.current = true;
      setLoading(false);
    })();
  }, []);

  /* auto-save on change */
  useEffect(() => { if (loaded.current) saveKey("admin:questions", questions); }, [questions]);
  useEffect(() => { if (loaded.current) saveKey("admin:courses", courses); }, [courses]);
  useEffect(() => { if (loaded.current) saveKey("admin:batches", batches); }, [batches]);
  useEffect(() => { if (loaded.current) saveKey("admin:tests", tests); }, [tests]);
  useEffect(() => { if (loaded.current) saveKey("admin:materials", materials); }, [materials]);

  if (loading) return <div className="ad-root"><style>{CSS}</style><div className="loader">Loading your admin panel…</div></div>;

  const go = (v) => { setView(v); setSbOpen(false); };

  return (
    <div className="ad-root">
      <style>{CSS}</style>

      {/* SIDEBAR */}
      {sbOpen && <div className="scrim" onClick={() => setSbOpen(false)} />}
      <aside className={"sb" + (sbOpen ? " open" : "")}>
        <div className="sb-brand">
          <div className="sb-logo">
            <div className="sb-logo-mark">P</div>
            <div>
              <div className="sb-name">PrepEngine</div>
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
        <div className="sb-foot">Data saved in your browser.<br />Connects to Supabase in production.</div>
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
            <div className="tb-admin">
              <button className="btn-icon" title="Log out" onClick={onLogout} style={{ width: 40, height: 40, marginRight: 4 }}><LogOut size={18} /></button>
              <div className="tb-av">PK</div>
              <div>
                <div className="tb-admin-name">Priyadarshee</div>
                <div className="tb-admin-role">Administrator</div>
              </div>
            </div>
          </div>
        </header>

        <main className="content">
          {view === "overview" && <Overview {...{ questions, tests, courses, batches, materials, go }} />}
          {view === "questions" && <QuestionBank {...{ questions, setQuestions, toast, askDelete }} />}
          {view === "tests" && <Tests {...{ tests, setTests, questions, toast, askDelete }} />}
          {view === "courses" && <Courses {...{ courses, setCourses, batches, setBatches, toast, askDelete }} />}
          {view === "materials" && <Materials {...{ materials, setMaterials, batches, toast, askDelete }} />}
          {view === "students" && <Students />}
          {view === "sales" && <Sales />}
        </main>
      </div>

      {/* TOASTS + CONFIRM */}
      <div className="toasts">
        {toasts.map((t) => <div className="toast" key={t.id}><CheckCircle2 size={18} />{t.msg}</div>)}
      </div>
      {confirm && <Confirm message={confirm.message} onYes={confirm.onYes} onClose={() => setConfirm(null)} />}
    </div>
  );
}

/* ============================================================
   VIEW: OVERVIEW
   ============================================================ */
function Overview({ questions, tests, courses, batches, materials, go }) {
  const published = tests.filter((t) => t.isPublished).length;
  const bySubject = useMemo(() => {
    const m = {};
    questions.forEach((q) => { m[q.subject] = (m[q.subject] || 0) + 1; });
    return Object.entries(m).sort((a, b) => b[1] - a[1]);
  }, [questions]);
  const maxSub = bySubject.length ? bySubject[0][1] : 1;
  const revenue = SAMPLE_PAYMENTS.filter((p) => p.status === "paid").reduce((s, p) => s + p.amount, 0);
  const recent = questions.slice(-5).reverse();

  return (
    <div>
      <div className="banner"><CheckCircle2 size={17} />Welcome back! Everything you create here is saved automatically. Start by adding questions, then build a test.</div>

      <div className="stats">
        <StatCard icon={<ListChecks size={20} />} color={{ bg: "#e6f6fa", fg: "#0e8fa8" }} n={questions.length} label="Questions" sub="in your bank" />
        <StatCard icon={<FileText size={20} />} color={{ bg: "#e3f3f7", fg: "#2a8fb0" }} n={tests.length} label="Tests" sub={`${published} published`} />
        <StatCard icon={<GraduationCap size={20} />} color={{ bg: "#e6f4ef", fg: "#1a6b3c" }} n={courses.length} label="Courses" sub={`${batches.length} batches`} />
        <StatCard icon={<Users size={20} />} color={{ bg: "#fff1ec", fg: "#ec5a52" }} n={SAMPLE_STUDENTS.length} label="Students" sub="sample data" />
        <StatCard icon={<IndianRupee size={20} />} color={{ bg: "#e8f6ee", fg: "#1f8a4c" }} n={fmtINR(revenue)} label="Revenue" sub="sample data" />
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
              <div key={q.id} style={{ padding: "11px 0", borderBottom: "1px solid #eefbfd" }}>
                <div style={{ fontSize: 13.5, fontWeight: 600, color: "#103a44", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>{q.body}</div>
                <div style={{ display: "flex", gap: 7, marginTop: 6 }}>
                  <Badge color={{ bg: "#eefbfd", fg: "#5e7d86" }}>{q.subject}</Badge>
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
function QuestionBank({ questions, setQuestions, toast, askDelete }) {
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

  const save = (item) => {
    setQuestions((prev) => prev.some((x) => x.id === item.id) ? prev.map((x) => x.id === item.id ? item : x) : [...prev, item]);
    setEditing(null);
    toast(item.id && questions.some((x) => x.id === item.id) ? "Question updated" : "Question saved");
  };
  const importQs = (arr) => { setQuestions((prev) => [...prev, ...arr]); setBulk(false); toast(`${arr.length} questions imported`); };
  const del = (item) => askDelete(`Delete this question? "${item.body.slice(0, 60)}…" This cannot be undone.`, () => { setQuestions((p) => p.filter((x) => x.id !== item.id)); toast("Question deleted"); });

  return (
    <div>
      <div className="toolbar">
        <div className="search"><Search size={17} /><input value={q} placeholder="Search by question or topic…" onChange={(e) => setQ(e.target.value)} /></div>
        <select className="sel" value={subj} onChange={(e) => setSubj(e.target.value)}>{subjects.map((s) => <option key={s} value={s}>{s === "all" ? "All subjects" : s}</option>)}</select>
        <select className="sel" value={type} onChange={(e) => setType(e.target.value)}>
          <option value="all">All types</option><option value="mcq">Single Correct</option><option value="multiple">Multiple Correct</option><option value="numerical">Numerical</option>
        </select>
        <button className="btn btn-ghost" onClick={() => setBulk(true)}><Upload size={16} />Bulk import</button>
        <button className="btn btn-primary" onClick={() => setEditing({})}><Plus size={16} />Add question</button>
      </div>

      {filtered.length === 0 ? (
        <div className="panel"><Empty icon={<ListChecks size={26} />} title={questions.length === 0 ? "No questions yet" : "No matches"}
          text={questions.length === 0 ? "Add your first question or bulk-import a set." : "Try a different search or filter."}
          action={questions.length === 0 ? <button className="btn btn-primary" onClick={() => setEditing({})}><Plus size={16} />Add question</button> : null} />
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
                  <td><Badge color={{ bg: "#eefbfd", fg: "#5e7d86" }}>{x.subject}</Badge></td>
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
function Tests({ tests, setTests, questions, toast, askDelete }) {
  const [editor, setEditor] = useState(null); // null=list, {}=new, test=edit

  const save = (t) => {
    setTests((prev) => prev.some((x) => x.id === t.id) ? prev.map((x) => x.id === t.id ? t : x) : [...prev, t]);
    setEditor(null);
    toast(t.isPublished ? "Test published" : "Test saved as draft");
  };
  const del = (t) => askDelete(`Delete the test "${t.title}"? This cannot be undone.`, () => { setTests((p) => p.filter((x) => x.id !== t.id)); toast("Test deleted"); });
  const togglePublish = (t) => { setTests((p) => p.map((x) => x.id === t.id ? { ...x, isPublished: !x.isPublished } : x)); toast(t.isPublished ? "Unpublished" : "Published"); };

  if (editor !== null) {
    return <TestEditor initial={editor.id ? editor : null} bank={questions} onSave={save} onCancel={() => setEditor(null)} toast={toast} />;
  }

  const qCount = (t) => t.sections.reduce((s, sec) => s + sec.questionIds.length, 0);

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
                  <td><div style={{ fontWeight: 700, color: "#103a44" }}>{t.title}</div>{t.seriesTitle && <div className="q-sub">{t.seriesTitle}</div>}</td>
                  <td>{t.sections.length}</td>
                  <td>{qCount(t)}</td>
                  <td><Clock size={13} style={{ verticalAlign: -2, marginRight: 4, color: "#9bb4bc" }} />{t.durationMin} min</td>
                  <td>
                    <button className="dot-pub" onClick={() => togglePublish(t)} title="Click to toggle">
                      <span className="dot" style={{ background: t.isPublished ? "var(--green)" : "#c0ccd8" }} />
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
function Courses({ courses, setCourses, batches, setBatches, toast, askDelete }) {
  const [courseForm, setCourseForm] = useState(null);
  const [batchForm, setBatchForm] = useState(null); // {courseId, batch?}

  const saveCourse = (c) => { setCourses((p) => p.some((x) => x.id === c.id) ? p.map((x) => x.id === c.id ? c : x) : [...p, c]); setCourseForm(null); toast("Course saved"); };
  const delCourse = (c) => askDelete(`Delete "${c.title}" and all its batches?`, () => { setCourses((p) => p.filter((x) => x.id !== c.id)); setBatches((p) => p.filter((b) => b.courseId !== c.id)); toast("Course deleted"); });
  const saveBatch = (b) => { setBatches((p) => p.some((x) => x.id === b.id) ? p.map((x) => x.id === b.id ? b : x) : [...p, b]); setBatchForm(null); toast("Batch saved"); };
  const delBatch = (b) => askDelete(`Delete batch "${b.name}"?`, () => { setBatches((p) => p.filter((x) => x.id !== b.id)); toast("Batch deleted"); });

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
                  <span className="dot-pub"><span className="dot" style={{ background: c.isPublished ? "var(--green)" : "#c0ccd8" }} /><span style={{ color: c.isPublished ? "var(--green)" : "var(--muted)", fontSize: 12 }}>{c.isPublished ? "Published" : "Draft"}</span></span>
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
                        <td style={{ fontWeight: 700, color: "#103a44" }}>{b.name}</td>
                        <td>{b.price > 0 ? fmtINR(b.price) : <span style={{ color: "var(--green)", fontWeight: 700 }}>Free</span>}</td>
                        <td>{b.seatLimit ?? "∞"}</td>
                        <td style={{ fontSize: 12.5, color: "var(--muted)" }}>{b.startDate || "—"}{b.endDate ? " → " + b.endDate : ""}</td>
                        <td><span className="dot-pub"><span className="dot" style={{ background: b.isActive ? "var(--green)" : "#c0ccd8" }} /><span style={{ fontSize: 12, color: b.isActive ? "var(--green)" : "var(--muted)" }}>{b.isActive ? "Active" : "Inactive"}</span></span></td>
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

      {courseForm && <CourseForm initial={courseForm.id ? courseForm : null} onSave={saveCourse} onClose={() => setCourseForm(null)} />}
      {batchForm && <BatchForm initial={batchForm.batch || null} courseId={batchForm.courseId} onSave={saveBatch} onClose={() => setBatchForm(null)} />}
    </div>
  );
}

/* ============================================================
   VIEW: MATERIALS
   ============================================================ */
function Materials({ materials, setMaterials, batches, toast, askDelete }) {
  const [form, setForm] = useState(null);
  const save = (m) => { setMaterials((p) => p.some((x) => x.id === m.id) ? p.map((x) => x.id === m.id ? m : x) : [...p, m]); setForm(null); toast("Material saved"); };
  const del = (m) => askDelete(`Delete "${m.title}"?`, () => { setMaterials((p) => p.filter((x) => x.id !== m.id)); toast("Material deleted"); });
  const batchName = (id) => batches.find((b) => b.id === id)?.name || "Public";
  const typeColor = { pdf: { bg: "#fbeaea", fg: "#cf4040" }, note: { bg: "#e6f6fa", fg: "#0e8fa8" }, video: { bg: "#e3f3f7", fg: "#2a8fb0" }, link: { bg: "#e6f4ef", fg: "#1a6b3c" } };

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
                  <td style={{ fontWeight: 700, color: "#103a44" }}>{m.title}</td>
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
   VIEW: STUDENTS (sample)
   ============================================================ */
function Students() {
  return (
    <div>
      <div className="banner sample"><AlertCircle size={17} />Sample data. In production this lists real enrolled students from your <code style={{ margin: "0 4px" }}>enrollments</code> table.</div>
      <div className="tbl-wrap">
        <table className="tbl">
          <thead><tr><th>Student</th><th>Email</th><th>Batch</th><th>Tests Attempted</th><th>Avg. Score</th></tr></thead>
          <tbody>
            {SAMPLE_STUDENTS.map((s, i) => (
              <tr key={i}>
                <td><div style={{ display: "flex", alignItems: "center", gap: 10 }}>
                  <span style={{ width: 32, height: 32, borderRadius: 8, background: "#0e8fa8", color: "#fff", display: "grid", placeItems: "center", fontSize: 12, fontWeight: 800 }}>{s.name.split(" ").map((w) => w[0]).slice(0, 2).join("")}</span>
                  <span style={{ fontWeight: 700, color: "#103a44" }}>{s.name}</span>
                </div></td>
                <td style={{ color: "var(--muted)" }}>{s.email}</td>
                <td>{s.batch}</td>
                <td>{s.attempts}</td>
                <td><span style={{ fontWeight: 800, color: s.avg >= 70 ? "var(--green)" : s.avg >= 50 ? "var(--amber)" : "var(--red)" }}>{s.avg}%</span></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

/* ============================================================
   VIEW: SALES (sample)
   ============================================================ */
function Sales() {
  const paid = SAMPLE_PAYMENTS.filter((p) => p.status === "paid");
  const revenue = paid.reduce((s, p) => s + p.amount, 0);
  return (
    <div>
      <div className="banner sample"><AlertCircle size={17} />Sample data. In production this reads verified Razorpay transactions from your <code style={{ margin: "0 4px" }}>payments</code> table.</div>
      <div className="stats">
        <StatCard icon={<IndianRupee size={20} />} color={{ bg: "#e8f6ee", fg: "#1f8a4c" }} n={fmtINR(revenue)} label="Total Revenue" sub={`${paid.length} successful payments`} />
        <StatCard icon={<TrendingUp size={20} />} color={{ bg: "#e6f6fa", fg: "#0e8fa8" }} n={SAMPLE_PAYMENTS.length} label="Transactions" sub="all attempts" />
        <StatCard icon={<Users size={20} />} color={{ bg: "#fff1ec", fg: "#ec5a52" }} n={new Set(paid.map((p) => p.name)).size} label="Paying Students" sub="unique buyers" />
      </div>
      <div className="tbl-wrap">
        <table className="tbl">
          <thead><tr><th>Student</th><th>Item</th><th>Amount</th><th>Status</th><th>Date</th></tr></thead>
          <tbody>
            {SAMPLE_PAYMENTS.map((p, i) => (
              <tr key={i}>
                <td style={{ fontWeight: 700, color: "#103a44" }}>{p.name}</td>
                <td style={{ color: "var(--muted)" }}>{p.item}</td>
                <td style={{ fontWeight: 800 }}>{fmtINR(p.amount)}</td>
                <td><Badge color={p.status === "paid" ? { bg: "#e8f6ee", fg: "#1f8a4c" } : { bg: "#fbeaea", fg: "#cf4040" }}>{p.status === "paid" ? "Paid" : "Failed"}</Badge></td>
                <td style={{ color: "var(--muted)", fontSize: 13 }}>{p.date}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

return App;
})();

const StudentApp = (() => {
/* ============================================================
   HELPERS
   ============================================================ */
const uid = () => (window.crypto && crypto.randomUUID ? crypto.randomUUID() : "id-" + Date.now() + "-" + Math.random().toString(36).slice(2, 8));
const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
const fmtDate = (s) => { const d = new Date(s); return d.getDate() + " " + MONTHS[d.getMonth()]; };
const fmtINR = (n) => "₹" + Number(n).toLocaleString("en-IN");
const fmtTime = (s) => { const m = Math.floor(s / 60), sec = Math.round(s % 60); return m + "m " + String(sec).padStart(2, "0") + "s"; };
const daysUntil = (target) => Math.max(0, Math.ceil((new Date(target) - new Date()) / 86400000));
const bandFor = (a) => (a >= 75 ? "strong" : a >= 50 ? "average" : "weak");
const SEM = { strong: "#1f8a4c", average: "#ec5a52", weak: "#cf4040" };
const gradeFor = (p) => (p >= 85 ? { g: "A+", c: "#1f8a4c" } : p >= 70 ? { g: "A", c: "#2f9e58" } : p >= 55 ? { g: "B", c: "#ec5a52" } : p >= 40 ? { g: "C", c: "#cc7a00" } : { g: "D", c: "#cf4040" });

async function loadKey(k, fb) { try { if (!window.storage) return fb; const r = await window.storage.get(k, false); return r && r.value ? JSON.parse(r.value) : fb; } catch { return fb; } }
async function saveKey(k, v) { try { if (!window.storage) return; await window.storage.set(k, JSON.stringify(v), false); } catch (e) {} }

/* ============================================================
   SEED DATA  (deterministic — stable across reloads)
   ============================================================ */
function buildAttempt(id, title, series, date, score, acc, pct, rank, timeSec) {
  const maxScore = 50, totalQ = 23;
  const attempted = Math.round(totalQ * 0.92);
  const correct = Math.round(attempted * (acc / 100));
  const wrong = attempted - correct;
  const skipped = totalQ - attempted;
  const gsScore = +(score * 0.54).toFixed(1), csatScore = +(score - gsScore).toFixed(1);
  return {
    id, title, series, date, score, maxScore, accuracy: acc, percentile: pct, rank, totalStudents: 980,
    timeSec, durationMin: 60, totalQ, correct, wrong, skipped,
    sections: [
      { name: "General Studies", score: gsScore, max: 26 },
      { name: "CSAT (Aptitude)", score: csatScore, max: 24 },
    ],
  };
}
const ATTEMPTS = [
  buildAttempt(uid(), "BPSC Prelims Mock 01", "BPSC Prelims Test Series 2026", "2026-04-26", 22, 55, 42, 412, 1080),
  buildAttempt(uid(), "Polity Sectional Test", "Sectional Series", "2026-05-01", 24.5, 58, 48, 360, 1050),
  buildAttempt(uid(), "BPSC Prelims Mock 02", "BPSC Prelims Test Series 2026", "2026-05-06", 21, 52, 39, 440, 1110),
  buildAttempt(uid(), "Modern History Sectional", "Sectional Series", "2026-05-11", 27, 61, 55, 300, 1020),
  buildAttempt(uid(), "CSAT Full Mock 01", "CSAT Series", "2026-05-17", 29.5, 64, 61, 250, 990),
  buildAttempt(uid(), "BPSC Prelims Mock 03", "BPSC Prelims Test Series 2026", "2026-05-23", 28, 62, 58, 270, 1005),
  buildAttempt(uid(), "Geography + Economy Combined", "Sectional Series", "2026-05-29", 33, 69, 72, 180, 960),
  buildAttempt(uid(), "BPSC Prelims Mock 04", "BPSC Prelims Test Series 2026", "2026-06-03", 35.5, 72, 78, 130, 930),
  buildAttempt(uid(), "Full Length GS Test", "BPSC Prelims Test Series 2026", "2026-06-08", 34, 70, 75, 150, 945),
  buildAttempt(uid(), "BPSC Prelims Mock 05", "BPSC Prelims Test Series 2026", "2026-06-12", 38, 76, 85, 88, 900),
];

const NEW_TESTS = [
  { id: uid(), title: "BPSC Prelims Mock 06", series: "BPSC Prelims Test Series 2026", questions: 100, durationMin: 120, isFree: true },
  { id: uid(), title: "CSAT Full Mock 02", series: "CSAT Series", questions: 80, durationMin: 120, isFree: false },
  { id: uid(), title: "Current Affairs — June 2026", series: "Monthly CA Series", questions: 50, durationMin: 45, isFree: true },
];
const UPCOMING = [
  { id: uid(), title: "All-India Grand Test 01", series: "Grand Test Series", questions: 100, durationMin: 120, isFree: false, scheduledFor: "2026-06-18" },
  { id: uid(), title: "BPSC Prelims Mock 07", series: "BPSC Prelims Test Series 2026", questions: 100, durationMin: 120, isFree: true, scheduledFor: "2026-06-21" },
];

const SUBJECT_STRENGTH = {
  "Polity": 82, "Modern History": 75, "Geography": 61, "Economy": 47, "Environment": 70,
  "Number System": 64, "Reasoning": 62, "Reading Comprehension": 54, "Quantitative Aptitude": 49,
};

const BATCHES = [
  { id: uid(), name: "BPSC Prelims 2026 — Foundation", examTarget: "BPSC Prelims 2026", totalTests: 18, attemptedTests: 8, validTill: "2026-06-30", color: "#0e8fa8" },
  { id: uid(), name: "CSAT Sprint", examTarget: "UPSC Prelims 2026", totalTests: 8, attemptedTests: 2, validTill: "2026-07-30", color: "#2a8fb0" },
];

const MATERIALS = [
  { id: uid(), title: "Polity NCERT — Quick Revision Notes", subject: "Polity", type: "pdf", isFree: true },
  { id: uid(), title: "Modern History — One-Liner Capsule", subject: "Modern History", type: "pdf", isFree: true },
  { id: uid(), title: "Geography Mapping — Video Series", subject: "Geography", type: "video", isFree: true },
  { id: uid(), title: "Economy Survey 2026 — Key Highlights", subject: "Economy", type: "note", isFree: false },
  { id: uid(), title: "CSAT Reasoning — Shortcut Tricks", subject: "Reasoning", type: "video", isFree: true },
  { id: uid(), title: "June 2026 Current Affairs Compilation", subject: "Current Affairs", type: "pdf", isFree: true },
];

const LEADERBOARD = [
  { rank: 1, name: "Ananya Mishra", score: 46.5, tests: 11, move: 0 },
  { rank: 2, name: "Rohan Gupta", score: 45, tests: 12, move: 1 },
  { rank: 3, name: "Sneha Kumari", score: 44, tests: 10, move: -1 },
  { rank: 4, name: "Aditya Roy", score: 42.5, tests: 9, move: 2 },
  { rank: 5, name: "Kritika Sharma", score: 41, tests: 11, move: 0 },
  { rank: 6, name: "Priyadarshee", score: 38, tests: 10, move: 4, you: true },
  { rank: 7, name: "Vivek Anand", score: 37.5, tests: 8, move: -2 },
  { rank: 8, name: "Megha Jain", score: 36, tests: 9, move: 1 },
  { rank: 9, name: "Sahil Verma", score: 35, tests: 7, move: 0 },
  { rank: 10, name: "Pooja Singh", score: 34, tests: 10, move: -3 },
];

const QUOTES = [
  "Consistency beats intensity. Show up today.",
  "Every mock is a rehearsal for the real day.",
  "Small daily progress compounds into ranks.",
  "Revise what you learn, or you'll relearn what you forgot.",
  "Discipline today, designation tomorrow.",
];

/* deterministic 84-day activity heatmap */
function genActivity() {
  const days = 84, out = [], today = new Date();
  for (let i = days - 1; i >= 0; i--) {
    const d = new Date(today); d.setDate(d.getDate() - i);
    let base = (Math.sin(i * 0.7) + 1) * 1.4;
    if (d.getDay() === 0) base *= 0.4;
    const recency = ((days - i) / days) * 1.6;
    let c = Math.round(base + recency);
    if ((i * 13) % 17 === 0) c = 0;
    out.push({ date: d, count: Math.max(0, Math.min(4, c)) });
  }
  return out;
}
const ACTIVITY = genActivity();
function currentStreak() { let s = 0; for (let i = ACTIVITY.length - 1; i >= 0; i--) { if (ACTIVITY[i].count > 0) s++; else break; } return s; }

/* derived aggregates */
const DERIVED = (() => {
  const n = ATTEMPTS.length;
  const scorePcts = ATTEMPTS.map((a) => (a.score / a.maxScore) * 100);
  const avgScore = scorePcts.reduce((x, y) => x + y, 0) / n;
  const bestScore = Math.max(...scorePcts);
  const bestPct = Math.max(...ATTEMPTS.map((a) => a.percentile));
  const bestRank = Math.min(...ATTEMPTS.map((a) => a.rank));
  const avgAcc = ATTEMPTS.reduce((x, a) => x + a.accuracy, 0) / n;
  const bestAcc = Math.max(...ATTEMPTS.map((a) => a.accuracy));
  const totalTime = ATTEMPTS.reduce((x, a) => x + a.timeSec, 0);
  const streak = currentStreak();
  const activeDays = ACTIVITY.filter((d) => d.count > 0).length;
  return { n, avgScore, bestScore, bestPct, bestRank, avgAcc, bestAcc, totalTime, streak, activeDays };
})();

const ACHIEVEMENTS = [
  { key: "first", title: "First Step", desc: "Completed your first test", icon: Play, earned: DERIVED.n >= 1 },
  { key: "ten", title: "Mock Marathoner", desc: "Completed 10 tests", icon: FileText, earned: DERIVED.n >= 10 },
  { key: "score70", title: "Strong Scorer", desc: "Scored 70%+ in a test", icon: Target, earned: DERIVED.bestScore >= 70 },
  { key: "streak7", title: "On Fire", desc: "7-day study streak", icon: Flame, earned: DERIVED.streak >= 7 },
  { key: "pct80", title: "Top Percentile", desc: "Crossed 80th percentile", icon: TrendingUp, earned: DERIVED.bestPct >= 80 },
  { key: "rank100", title: "Century Rank", desc: "Ranked inside top 100", icon: Medal, earned: DERIVED.bestRank <= 100 },
  { key: "acc90", title: "Sniper", desc: "90%+ accuracy in a test", icon: Zap, earned: DERIVED.bestAcc >= 90 },
  { key: "twentyfive", title: "Quarter Century", desc: "Complete 25 tests", icon: Award, earned: DERIVED.n >= 25 },
  { key: "top10", title: "Elite Ten", desc: "Rank inside top 10", icon: Trophy, earned: DERIVED.bestRank <= 10 },
  { key: "streak30", title: "Unstoppable", desc: "30-day study streak", icon: Sparkles, earned: DERIVED.streak >= 30 },
];

/* ============================================================
   STYLES
   ============================================================ */
const CSS = `
:root{
  --navy:#0e8fa8; --navy-2:#0a6173; --gold:#f76b6b; --gold-2:#ec5a52;
  --bg:#eefbfd; --card:#fff; --ink:#0e3540; --muted:#5e7d86; --line:#dcecf0;
  --green:#1f8a4c; --amber:#ec5a52; --red:#cf4040; --blue:#149cba; --purple:#2a8fb0;
  --grn-bg:#e8f6ee; --amb-bg:#fff1ec; --red-bg:#fbeaea;
}
*{box-sizing:border-box}
.sd-root{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--ink);
  font-variant-numeric:tabular-nums;line-height:1.5;background:var(--bg);min-height:100vh;display:flex}
.sd-root button{font-family:inherit;cursor:pointer;border:none;background:none}
.sd-root input{font-family:inherit}
.sd-root a{text-decoration:none}

/* SIDEBAR */
.sb{width:244px;background:linear-gradient(180deg,#0e6273,#0b4f5e);color:#cfeaf0;flex:0 0 auto;display:flex;flex-direction:column;position:sticky;top:0;height:100vh;z-index:40}
.sb-brand{padding:20px;border-bottom:1px solid rgba(255,255,255,.08)}
.sb-logo{display:flex;align-items:center;gap:11px}
.sb-mark{width:36px;height:36px;border-radius:9px;background:linear-gradient(135deg,var(--gold),var(--gold-2));display:grid;place-items:center;color:#fff;font-weight:800;font-size:16px;flex:0 0 auto}
.sb-name{font-weight:800;font-size:15px;color:#fff;line-height:1.15}
.sb-tag{font-size:11px;color:#bfe6ee}
.sb-nav{flex:1;padding:14px 12px;overflow-y:auto}
.sb-item{display:flex;align-items:center;gap:12px;padding:11px 13px;border-radius:9px;font-size:14px;font-weight:600;color:#bdcfe2;width:100%;text-align:left;transition:.13s;margin-bottom:3px;position:relative}
.sb-item:hover{background:rgba(255,255,255,.06);color:#fff}
.sb-item.active{background:rgba(255,255,255,.1);color:#fff}
.sb-item.active::before{content:"";position:absolute;left:0;top:8px;bottom:8px;width:3px;border-radius:3px;background:var(--gold)}
.sb-streak{margin:8px 12px 0;background:rgba(247,107,107,.14);border:1px solid rgba(247,107,107,.3);border-radius:11px;padding:13px 14px}
.sb-streak-top{display:flex;align-items:center;gap:8px;color:#ffd0c0;font-weight:800;font-size:14px}
.sb-streak-sub{font-size:11.5px;color:#d4f3f9;margin-top:4px}

/* MAIN */
.main{flex:1;min-width:0;display:flex;flex-direction:column}
.topbar{background:#fff;border-bottom:1px solid var(--line);padding:13px 26px;display:flex;align-items:center;justify-content:space-between;gap:14px;position:sticky;top:0;z-index:30}
.topbar h1{margin:0;font-size:19px;font-weight:800;letter-spacing:-.01em}
.topbar .sub{font-size:12.5px;color:var(--muted);margin-top:1px}
.tb-right{display:flex;align-items:center;gap:14px}
.bell{position:relative;width:40px;height:40px;border-radius:10px;border:1px solid var(--line);display:grid;place-items:center;color:#5e7d86}
.bell:hover{background:#f1fafc;color:var(--navy)}
.bell-dot{position:absolute;top:9px;right:9px;width:8px;height:8px;border-radius:50%;background:var(--red);border:1.5px solid #fff}
.notif{position:absolute;top:52px;right:0;width:320px;background:#fff;border:1px solid var(--line);border-radius:13px;box-shadow:0 16px 40px rgba(20,120,140,.18);overflow:hidden;z-index:50}
.notif-head{padding:14px 16px;border-bottom:1px solid var(--line);font-weight:800;font-size:14px}
.notif-item{display:flex;gap:11px;padding:13px 16px;border-bottom:1px solid #eefbfd}
.notif-item:last-child{border-bottom:none}
.notif-ic{width:32px;height:32px;border-radius:8px;display:grid;place-items:center;flex:0 0 auto}
.notif-t{font-size:13px;font-weight:700;color:#103a44}
.notif-d{font-size:12px;color:var(--muted);margin-top:2px}
.tb-av{width:38px;height:38px;border-radius:10px;background:var(--navy);color:#fff;display:grid;place-items:center;font-weight:800;font-size:14px}
.hamburger{display:none;width:40px;height:40px;border-radius:10px;border:1px solid var(--line);align-items:center;justify-content:center}
.content{padding:26px;max-width:1240px;width:100%;margin:0 auto}

/* CARDS */
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;box-shadow:0 1px 3px rgba(20,120,140,.05)}
.card-pad{padding:22px}
.sec-head{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:16px;flex-wrap:wrap}
.sec-head h2{margin:0;font-size:16px;font-weight:800}
.sec-head .note{font-size:12.5px;color:var(--muted);margin-top:2px}
.eyebrow{font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-2);font-weight:800}

/* HERO */
.hero{background:url("data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20viewBox%3D%270%200%201200%20360%27%3E%3Cg%20fill%3D%27none%27%20stroke%3D%27%230a4f5e%27%20stroke-width%3D%273.2%27%20stroke-linecap%3D%27round%27%3E%3Cpath%20d%3D%27M120%2095%20q22%20-20%2044%200%20q22%20-20%2044%200%27%20opacity%3D%270.20%27%2F%3E%3Cpath%20d%3D%27M300%2062%20q16%20-14%2032%200%20q16%20-14%2032%200%27%20opacity%3D%270.16%27%2F%3E%3Cpath%20d%3D%27M520%20102%20q20%20-18%2040%200%20q20%20-18%2040%200%27%20opacity%3D%270.18%27%2F%3E%3Cpath%20d%3D%27M720%2056%20q14%20-12%2028%200%20q14%20-12%2028%200%27%20opacity%3D%270.14%27%2F%3E%3Cpath%20d%3D%27M900%2098%20q24%20-22%2048%200%20q24%20-22%2048%200%27%20opacity%3D%270.20%27%2F%3E%3Cpath%20d%3D%27M1050%2066%20q16%20-14%2032%200%20q16%20-14%2032%200%27%20opacity%3D%270.16%27%2F%3E%3Cpath%20d%3D%27M430%20152%20q12%20-10%2024%200%20q12%20-10%2024%200%27%20opacity%3D%270.12%27%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat center 16px / 88% auto,radial-gradient(ellipse 55% 50% at 16% 4%, rgba(255,255,255,.55), transparent 72%),radial-gradient(ellipse 46% 42% at 83% 2%, rgba(255,255,255,.40), transparent 72%),url("data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20viewBox%3D%270%200%201200%20220%27%3E%3Cdefs%3E%3ClinearGradient%20id%3D%27bk0%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%23b5714f%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%23b5714f%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk1%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%23ad8c48%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%23ad8c48%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk2%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%235d8576%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%235d8576%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk3%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%236f6398%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%236f6398%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk4%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%233f7a88%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%233f7a88%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk5%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%239a564c%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%239a564c%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk6%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%237e8a4e%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%237e8a4e%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk7%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%2348688f%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%2348688f%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3C%2Fdefs%3E%3Cg%20opacity%3D%270.42%27%3E%3Crect%20x%3D%270%27%20y%3D%270%27%20width%3D%2723%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%2724%27%20y%3D%270%27%20width%3D%2732%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%2757%27%20y%3D%270%27%20width%3D%2741%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%2799%27%20y%3D%270%27%20width%3D%2716%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27116%27%20y%3D%270%27%20width%3D%2725%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27142%27%20y%3D%270%27%20width%3D%2734%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27177%27%20y%3D%270%27%20width%3D%2743%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%27221%27%20y%3D%270%27%20width%3D%2718%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%27240%27%20y%3D%270%27%20width%3D%2727%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%27268%27%20y%3D%270%27%20width%3D%2736%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%27305%27%20y%3D%270%27%20width%3D%2745%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%27351%27%20y%3D%270%27%20width%3D%2720%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27372%27%20y%3D%270%27%20width%3D%2729%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27402%27%20y%3D%270%27%20width%3D%2738%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27441%27%20y%3D%270%27%20width%3D%2747%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%27489%27%20y%3D%270%27%20width%3D%2722%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%27512%27%20y%3D%270%27%20width%3D%2731%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%27544%27%20y%3D%270%27%20width%3D%2740%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%27585%27%20y%3D%270%27%20width%3D%2749%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%27635%27%20y%3D%270%27%20width%3D%2724%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27660%27%20y%3D%270%27%20width%3D%2733%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27694%27%20y%3D%270%27%20width%3D%2742%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27737%27%20y%3D%270%27%20width%3D%2717%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%27755%27%20y%3D%270%27%20width%3D%2726%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%27782%27%20y%3D%270%27%20width%3D%2735%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%27818%27%20y%3D%270%27%20width%3D%2744%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%27863%27%20y%3D%270%27%20width%3D%2719%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%27883%27%20y%3D%270%27%20width%3D%2728%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27912%27%20y%3D%270%27%20width%3D%2737%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27950%27%20y%3D%270%27%20width%3D%2746%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27997%27%20y%3D%270%27%20width%3D%2721%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%271019%27%20y%3D%270%27%20width%3D%2730%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%271050%27%20y%3D%270%27%20width%3D%2739%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%271090%27%20y%3D%270%27%20width%3D%2748%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%271139%27%20y%3D%270%27%20width%3D%2723%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%271163%27%20y%3D%270%27%20width%3D%2732%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%271196%27%20y%3D%270%27%20width%3D%2741%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom / 100% 42%,linear-gradient(135deg,#2cc4db 0%,#159fbd 100%);border-radius:18px;color:#fff;padding:26px 28px;display:grid;grid-template-columns:1fr auto;gap:24px;align-items:center;box-shadow:0 16px 40px rgba(18,140,170,.26);margin-bottom:22px;overflow:hidden}
@media(max-width:680px){.hero{grid-template-columns:1fr}}
.hero-greet{font-size:23px;font-weight:800;letter-spacing:-.01em;text-shadow:0 1px 12px rgba(8,70,84,.30)}
.hero-quote{font-size:13.5px;color:#eafdff;margin-top:6px;display:flex;align-items:center;gap:8px;text-shadow:0 1px 9px rgba(8,70,84,.34)}
.hero-cd{background:rgba(247,107,107,.16);border:1px solid rgba(247,107,107,.36);border-radius:14px;padding:16px 22px;text-align:center;min-width:150px}
.hero-cd-n{font-size:34px;font-weight:800;color:#ffd0c0;line-height:1}
.hero-cd-l{font-size:11.5px;color:#d6f1f7;margin-top:5px;font-weight:600}
.hero-cd-d{font-size:11px;color:#9bbdd9;margin-top:2px}

/* STATS */
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:16px;margin-bottom:22px}
.stat{background:#fff;border:1px solid var(--line);border-radius:13px;padding:18px;box-shadow:0 1px 3px rgba(20,120,140,.05)}
.stat-ic{width:40px;height:40px;border-radius:10px;display:grid;place-items:center;margin-bottom:13px}
.stat-n{font-size:26px;font-weight:800;line-height:1;letter-spacing:-.02em}
.stat-l{font-size:12.5px;color:var(--muted);margin-top:6px;font-weight:600}
.stat-sub{font-size:11.5px;color:#90a3b6;margin-top:3px;display:flex;align-items:center;gap:4px}

/* GRID */
.grid2{display:grid;grid-template-columns:1.4fr 1fr;gap:18px}
.grid2b{display:grid;grid-template-columns:1fr 1fr;gap:18px}
@media(max-width:900px){.grid2,.grid2b{grid-template-columns:1fr}}
.mb{margin-bottom:18px}

/* RING */
.ring-wrap{position:relative;display:grid;place-items:center}
.ring-c{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}

/* HEATMAP */
.heat{display:grid;grid-template-rows:repeat(7,1fr);grid-auto-flow:column;gap:4px}
.heat-cell{width:13px;height:13px;border-radius:3px}
.heat-legend{display:flex;align-items:center;gap:6px;font-size:11.5px;color:var(--muted);margin-top:12px;justify-content:flex-end}

/* BADGES */
.badge{display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:700;padding:3px 9px;border-radius:20px;white-space:nowrap}
.chip{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:700;padding:5px 11px;border-radius:8px}
.dot{width:8px;height:8px;border-radius:50%}

/* TEST CARDS */
.test-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px}
.test-card{background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px;box-shadow:0 1px 3px rgba(20,120,140,.05);display:flex;flex-direction:column;gap:12px;transition:.15s}
.test-card:hover{box-shadow:0 6px 20px rgba(20,120,140,.1);transform:translateY(-2px)}
.test-top{display:flex;justify-content:space-between;align-items:flex-start;gap:10px}
.test-title{font-size:15.5px;font-weight:800;color:#103a44;line-height:1.25}
.test-series{font-size:12px;color:var(--muted);margin-top:3px}
.test-meta{display:flex;gap:16px;font-size:12.5px;color:#5e7d86;font-weight:600}
.test-meta span{display:flex;align-items:center;gap:5px}
.test-score{display:flex;align-items:center;gap:14px;padding:12px;background:#f6fdfe;border-radius:10px;border:1px solid #eefbfd}
.test-score-n{font-size:22px;font-weight:800;line-height:1}
.test-score-l{font-size:11px;color:var(--muted);font-weight:600;margin-top:3px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:7px;font-size:13.5px;font-weight:700;padding:11px 16px;border-radius:9px;transition:.14s;border:1.5px solid transparent;width:100%}
.btn-primary{background:linear-gradient(135deg,#1bb6d2,#0e9bb5);color:#fff;box-shadow:0 5px 16px rgba(20,150,180,.38)}
.btn-primary:hover{background:linear-gradient(135deg,#16a8c4,#0c8aa3);box-shadow:0 8px 22px rgba(20,150,180,.48)}
.btn-gold{background:var(--gold-2);color:#fff}
.btn-gold:hover{filter:brightness(.94)}
.btn-ghost{background:#fff;border-color:#cfe3e9;color:#43585f}
.btn-ghost:hover{border-color:#a8d4de;background:#f1fafc}
.btn-sm{padding:8px 13px;font-size:12.5px;width:auto}
.tabs{display:flex;gap:8px;margin-bottom:18px;flex-wrap:wrap}
.tab{font-size:13px;font-weight:700;padding:9px 16px;border-radius:20px;border:1.5px solid #d6dfe8;color:#4a6168;background:#fff;transition:.13s}
.tab.active{background:var(--navy);border-color:var(--navy);color:#fff}
.tab:hover:not(.active){border-color:#a8d4de}

/* PERFORMANCE */
.panel-title{font-size:16px;font-weight:800;margin:5px 0 2px;letter-spacing:-.01em}
.panel-note{font-size:12.5px;color:var(--muted);margin:0 0 16px}
.topic-row{display:flex;align-items:center;gap:12px;margin-bottom:11px}
.topic-name{font-size:13px;font-weight:600;width:160px;flex:0 0 auto;color:#2a4750;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.topic-track{flex:1;height:9px;background:#eefbfd;border-radius:6px;overflow:hidden}
.topic-fill{height:100%;border-radius:6px}
.topic-band{font-size:10.5px;font-weight:800;padding:3px 9px;border-radius:20px;flex:0 0 auto;text-transform:uppercase;letter-spacing:.03em}
.sw-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:560px){.sw-grid{grid-template-columns:1fr}}
.sw-box{border-radius:12px;padding:16px;border:1px solid}
.sw-box.s{background:var(--grn-bg);border-color:#c9e8d5}
.sw-box.w{background:var(--red-bg);border-color:#f1cfcf}
.sw-box h4{margin:0 0 10px;font-size:13px;font-weight:800;display:flex;align-items:center;gap:7px}
.sw-list{display:flex;flex-direction:column;gap:7px}
.sw-item{display:flex;justify-content:space-between;font-size:13px;font-weight:600}

/* BATCH */
.batch-card{background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:0 1px 3px rgba(20,120,140,.05)}
.batch-bar{height:5px}
.batch-body{padding:20px}
.batch-name{font-size:16px;font-weight:800;color:#103a44}
.batch-exam{font-size:12.5px;color:var(--muted);margin-top:3px}
.progress{height:9px;background:#eefbfd;border-radius:6px;overflow:hidden;margin:14px 0 7px}
.progress-fill{height:100%;border-radius:6px}

/* LEADERBOARD */
.lb-you{background:radial-gradient(ellipse 55% 50% at 16% 4%, rgba(255,255,255,.55), transparent 72%),radial-gradient(ellipse 46% 42% at 83% 2%, rgba(255,255,255,.40), transparent 72%),linear-gradient(135deg,#27bdd6,#0e94ad);border-radius:16px;color:#fff;padding:22px 26px;display:grid;grid-template-columns:auto 1fr auto;gap:22px;align-items:center;box-shadow:0 14px 36px rgba(18,140,170,.24);margin-bottom:20px}
@media(max-width:600px){.lb-you{grid-template-columns:1fr;text-align:center;gap:14px}}
.lb-rank-big{font-size:40px;font-weight:800;line-height:1;color:#ffd0c0}
.lb-row{display:flex;align-items:center;gap:14px;padding:14px 18px;border-bottom:1px solid #eefbfd}
.lb-row:last-child{border-bottom:none}
.lb-row.me{background:#fff2ee}
.lb-pos{width:34px;font-weight:800;font-size:15px;text-align:center;flex:0 0 auto}
.lb-av{width:38px;height:38px;border-radius:10px;display:grid;place-items:center;font-weight:800;font-size:13px;color:#fff;flex:0 0 auto}
.lb-name{flex:1;font-weight:700;font-size:14px;color:#103a44}
.lb-move{display:flex;align-items:center;gap:3px;font-size:12px;font-weight:700}
.lb-score{font-weight:800;font-size:15px;width:60px;text-align:right;flex:0 0 auto}

/* ACHIEVEMENTS */
.ach-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:14px}
.ach{border:1px solid var(--line);border-radius:13px;padding:18px;text-align:center;background:#fff;transition:.14s}
.ach.earned{border-color:#ffd9cf;background:linear-gradient(180deg,#fff6f2,#fff)}
.ach.locked{opacity:.55}
.ach-ic{width:50px;height:50px;border-radius:14px;display:grid;place-items:center;margin:0 auto 12px}
.ach-t{font-size:14px;font-weight:800;color:#103a44}
.ach-d{font-size:11.5px;color:var(--muted);margin-top:4px;line-height:1.4}

/* MATERIALS */
.mat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px}
.mat-card{display:flex;gap:14px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:13px;padding:16px;box-shadow:0 1px 3px rgba(20,120,140,.05)}
.mat-ic{width:46px;height:46px;border-radius:11px;display:grid;place-items:center;flex:0 0 auto}
.mat-t{font-size:14px;font-weight:700;color:#103a44;line-height:1.3}
.mat-sub{font-size:12px;color:var(--muted);margin-top:3px}

/* PROFILE */
.prof-head{display:flex;align-items:center;gap:20px;flex-wrap:wrap}
.prof-av{width:78px;height:78px;border-radius:18px;background:linear-gradient(140deg,#19b1cd,#0e8fa8);color:#fff;display:grid;place-items:center;font-size:28px;font-weight:800;flex:0 0 auto}
.prof-name{font-size:22px;font-weight:800;letter-spacing:-.01em}
.prof-meta{font-size:13px;color:var(--muted);margin-top:4px}
.field{margin-bottom:16px}
.field label{display:block;font-size:12.5px;font-weight:700;color:#3a5258;margin-bottom:6px}
.inp{width:100%;padding:11px 13px;border:1.5px solid #cfe3e9;border-radius:9px;font-size:14px;color:var(--ink);outline:none}
.inp:focus{border-color:var(--navy);box-shadow:0 0 0 3px rgba(20,150,180,.1)}
.toggle-row{display:flex;align-items:center;justify-content:space-between;padding:13px 0;border-bottom:1px solid #eefbfd}
.toggle-row:last-child{border-bottom:none}
.switch{width:44px;height:25px;border-radius:20px;background:#cbd5e1;position:relative;transition:.18s;flex:0 0 auto}
.switch.on{background:var(--green)}
.switch::after{content:"";position:absolute;top:3px;left:3px;width:19px;height:19px;border-radius:50%;background:#fff;transition:.18s;box-shadow:0 1px 3px rgba(0,0,0,.2)}
.switch.on::after{left:22px}

/* MODAL */
.overlay{position:fixed;inset:0;background:rgba(13,27,42,.55);display:flex;align-items:flex-start;justify-content:center;z-index:60;padding:30px 18px;overflow-y:auto;backdrop-filter:blur(2px)}
.modal{background:#fff;border-radius:16px;width:100%;max-width:640px;box-shadow:0 24px 60px rgba(0,0,0,.3);margin:auto}
.modal-head{display:flex;align-items:center;justify-content:space-between;padding:20px 24px;border-bottom:1px solid var(--line)}
.modal-head h3{margin:0;font-size:17px;font-weight:800}
.modal-head .x{width:34px;height:34px;border-radius:8px;display:grid;place-items:center;color:#7e93a8}
.modal-head .x:hover{background:#f1f5f9;color:var(--ink)}
.modal-body{padding:22px 24px}
.modal-foot{padding:16px 24px;display:flex;gap:11px;justify-content:flex-end;border-top:1px solid var(--line);background:#f6fdfe;border-radius:0 0 16px 16px}

/* TOAST */
.toasts{position:fixed;bottom:22px;right:22px;display:flex;flex-direction:column;gap:10px;z-index:90}
.toast{display:flex;align-items:center;gap:10px;background:var(--ink);color:#fff;font-size:13.5px;font-weight:600;padding:12px 16px;border-radius:11px;box-shadow:0 10px 30px rgba(0,0,0,.25)}
.toast svg{color:#7fe0a3;flex:0 0 auto}

.empty{text-align:center;padding:44px 20px;color:var(--muted)}
.empty-ic{width:54px;height:54px;border-radius:14px;background:#eefbfd;display:grid;place-items:center;margin:0 auto 14px;color:#9bb4bc}
.loader{display:grid;place-items:center;min-height:100vh;width:100%;color:var(--muted);font-size:14px}

@media(max-width:860px){
  .sb{position:fixed;left:0;top:0;transform:translateX(-100%);transition:transform .22s;box-shadow:8px 0 30px rgba(0,0,0,.2)}
  .sb.open{transform:translateX(0)}
  .hamburger{display:flex}
  .content{padding:18px}
  .scrim{position:fixed;inset:0;background:rgba(0,0,0,.4);z-index:39}
}
`;

/* ============================================================
   SMALL COMPONENTS
   ============================================================ */
function Ring({ value, size = 150, stroke = 13, color, children, track = "#eefbfd" }) {
  const r = (size - stroke) / 2, C = 2 * Math.PI * r, off = C * (1 - Math.min(1, Math.max(0, value)));
  return (
    <div className="ring-wrap" style={{ width: size, height: size }}>
      <svg width={size} height={size} style={{ transform: "rotate(-90deg)" }}>
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke={track} strokeWidth={stroke} />
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke={color} strokeWidth={stroke} strokeLinecap="round"
          strokeDasharray={C} strokeDashoffset={off} style={{ transition: "stroke-dashoffset 1s ease" }} />
      </svg>
      <div className="ring-c">{children}</div>
    </div>
  );
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
function Badge({ color, children }) { return <span className="badge" style={{ background: color.bg, color: color.fg }}>{children}</span>; }
function Avatar({ name, bg = "#0e8fa8", cls = "lb-av" }) {
  return <span className={cls} style={{ background: bg }}>{name.split(" ").map((w) => w[0]).slice(0, 2).join("")}</span>;
}
function heatColor(c) { return ["#eefbfd", "#cfe7d8", "#86cfa0", "#3fa86a", "#1f8a4c"][c]; }
const TYPE_ICON = { pdf: { ic: <FileText size={22} />, c: { bg: "#fbeaea", fg: "#cf4040" } }, note: { ic: <BookOpen size={22} />, c: { bg: "#e6f6fa", fg: "#0e8fa8" } }, video: { ic: <Play size={22} />, c: { bg: "#e3f3f7", fg: "#2a8fb0" } } };

/* ============================================================
   ATTEMPT ANALYSIS MODAL
   ============================================================ */
function AnalysisModal({ a, onClose }) {
  const pct = (a.score / a.maxScore) * 100;
  const grade = gradeFor(pct);
  return (
    <div className="overlay" onClick={onClose}>
      <div className="modal" onClick={(e) => e.stopPropagation()}>
        <div className="modal-head"><h3>{a.title}</h3><button className="x" onClick={onClose}><X size={19} /></button></div>
        <div className="modal-body">
          <div style={{ display: "flex", gap: 22, alignItems: "center", flexWrap: "wrap", marginBottom: 20 }}>
            <Ring value={pct / 100} size={128} color={grade.c}>
              <div style={{ fontSize: 26, fontWeight: 800 }}>{a.score}</div>
              <div style={{ fontSize: 12, color: "var(--muted)" }}>of {a.maxScore}</div>
              <div style={{ fontSize: 12, fontWeight: 800, color: grade.c }}>Grade {grade.g}</div>
            </Ring>
            <div style={{ flex: 1, minWidth: 200 }}>
              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
                <Mini n={a.percentile} l="Percentile" c="var(--gold-2)" />
                <Mini n={"#" + a.rank} l={"of " + a.totalStudents} c="var(--navy)" />
                <Mini n={a.accuracy + "%"} l="Accuracy" c="var(--green)" />
                <Mini n={fmtTime(a.timeSec)} l="Time taken" c="var(--blue)" />
              </div>
            </div>
          </div>

          <div style={{ display: "flex", gap: 10, marginBottom: 18 }}>
            <SmallStat n={a.correct} l="Correct" c="var(--green)" bg="var(--grn-bg)" />
            <SmallStat n={a.wrong} l="Wrong" c="var(--red)" bg="var(--red-bg)" />
            <SmallStat n={a.skipped} l="Skipped" c="var(--muted)" bg="#f1f5f9" />
          </div>

          <div className="eyebrow" style={{ marginBottom: 10 }}>Section-wise</div>
          {a.sections.map((s) => {
            const p = (s.score / s.max) * 100;
            const col = p >= 65 ? SEM.strong : p >= 40 ? SEM.average : SEM.weak;
            return (
              <div key={s.name} style={{ marginBottom: 12 }}>
                <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 6 }}>
                  <span style={{ fontSize: 13.5, fontWeight: 700 }}>{s.name}</span>
                  <span style={{ fontSize: 13, fontWeight: 700, color: col }}>{s.score} / {s.max}</span>
                </div>
                <div className="topic-track"><div className="topic-fill" style={{ width: p + "%", background: col }} /></div>
              </div>
            );
          })}
        </div>
        <div className="modal-foot">
          <button className="btn btn-ghost btn-sm" onClick={onClose}>Close</button>
          <button className="btn btn-gold btn-sm" onClick={onClose}><RotateCcw size={15} />Re-attempt</button>
        </div>
      </div>
    </div>
  );
}
function Mini({ n, l, c }) { return <div><div style={{ fontSize: 20, fontWeight: 800, color: c, lineHeight: 1 }}>{n}</div><div style={{ fontSize: 11.5, color: "var(--muted)", marginTop: 4, fontWeight: 600 }}>{l}</div></div>; }
function SmallStat({ n, l, c, bg }) { return <div style={{ flex: 1, background: bg, borderRadius: 10, padding: "12px 14px" }}><div style={{ fontSize: 20, fontWeight: 800, color: c, lineHeight: 1 }}>{n}</div><div style={{ fontSize: 11.5, color: "var(--muted)", marginTop: 5, fontWeight: 600 }}>{l}</div></div>; }

/* ============================================================
   VIEW: HOME
   ============================================================ */
function HomeView({ profile, go, setAnalysis, onStart }) {
  const hr = new Date().getHours();
  const greet = hr < 12 ? "Good morning" : hr < 17 ? "Good afternoon" : "Good evening";
  const quote = QUOTES[new Date().getDate() % QUOTES.length];
  const days = daysUntil(profile.targetDate);
  const recent = ATTEMPTS.slice(-6);
  const trend = recent.map((a) => ({ name: fmtDate(a.date), score: +((a.score / a.maxScore) * 100).toFixed(0), pct: a.percentile }));
  const last = ATTEMPTS[ATTEMPTS.length - 1];
  const sorted = Object.entries(SUBJECT_STRENGTH).sort((a, b) => b[1] - a[1]);
  const strong = sorted.slice(0, 3), weak = sorted.slice(-3).reverse();
  const goal = { done: 18, total: 25 };

  return (
    <div>
      <div className="hero">
        <div>
          <div className="hero-greet">{greet}, {profile.name.split(" ")[0]} 👋</div>
          <div className="hero-quote"><Sparkles size={15} style={{ color: "#ffd0c0" }} />{quote}</div>
        </div>
        <div className="hero-cd">
          <div className="hero-cd-n">{days}</div>
          <div className="hero-cd-l">days to your target</div>
          <div className="hero-cd-d">{profile.target}</div>
        </div>
      </div>

      <div className="stats">
        <StatCard icon={<FileText size={20} />} color={{ bg: "#e6f6fa", fg: "#0e8fa8" }} n={DERIVED.n} label="Tests attempted" sub="keep going" />
        <StatCard icon={<Target size={20} />} color={{ bg: "#e8f6ee", fg: "#1f8a4c" }} n={DERIVED.avgScore.toFixed(0) + "%"} label="Average score" sub={<><TrendingUp size={12} /> improving</>} />
        <StatCard icon={<Award size={20} />} color={{ bg: "#fff1ec", fg: "#ec5a52" }} n={DERIVED.bestPct} label="Best percentile" sub={"in " + last.title.slice(0, 16) + "…"} />
        <StatCard icon={<Flame size={20} />} color={{ bg: "#fbeaea", fg: "#cf4040" }} n={DERIVED.streak + " days"} label="Study streak" sub={DERIVED.activeDays + " active days"} />
      </div>

      <div className="grid2 mb">
        <div className="card card-pad">
          <div className="sec-head"><div><div className="eyebrow">Your trajectory</div><div className="panel-title">Score &amp; percentile trend</div></div>
            <button className="btn btn-ghost btn-sm" onClick={() => go("performance")}>Full analytics<ChevronRight size={15} /></button></div>
          <div style={{ height: 230 }}>
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={trend} margin={{ top: 10, right: 8, left: -20, bottom: 0 }}>
                <defs>
                  <linearGradient id="gScore" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stopColor="#0e8fa8" stopOpacity={0.28} /><stop offset="100%" stopColor="#0e8fa8" stopOpacity={0} /></linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#eefbfd" />
                <XAxis dataKey="name" tick={{ fontSize: 11, fill: "#5e7d86" }} axisLine={false} tickLine={false} />
                <YAxis domain={[0, 100]} tick={{ fontSize: 11, fill: "#9bb4bc" }} axisLine={false} tickLine={false} unit="%" />
                <Tooltip contentStyle={{ borderRadius: 10, border: "1px solid #dcecf0", fontSize: 13 }} />
                <Area dataKey="score" name="Score %" stroke="#0e8fa8" strokeWidth={2.5} fill="url(#gScore)" />
                <Line dataKey="pct" name="Percentile" stroke="#f76b6b" strokeWidth={2.5} dot={{ r: 3, fill: "#f76b6b" }} />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="card card-pad">
          <div className="eyebrow">Today's goal</div>
          <div className="panel-title" style={{ marginBottom: 16 }}>Daily practice</div>
          <div style={{ display: "flex", justifyContent: "center", marginBottom: 16 }}>
            <Ring value={goal.done / goal.total} size={150} color="#1f8a4c">
              <div style={{ fontSize: 28, fontWeight: 800 }}>{goal.done}<span style={{ fontSize: 15, color: "var(--muted)" }}>/{goal.total}</span></div>
              <div style={{ fontSize: 12, color: "var(--muted)", fontWeight: 600 }}>questions</div>
            </Ring>
          </div>
          <button className="btn btn-primary" onClick={onStart}><Play size={16} />Continue practice</button>
        </div>
      </div>

      <div className="grid2 mb">
        <div className="card card-pad">
          <div className="sec-head"><div><div className="eyebrow">Pick up where you left</div><div className="panel-title">Available tests</div></div>
            <button className="btn btn-ghost btn-sm" onClick={() => go("tests")}>View all<ChevronRight size={15} /></button></div>
          {NEW_TESTS.slice(0, 3).map((t) => (
            <div key={t.id} style={{ display: "flex", alignItems: "center", gap: 12, padding: "12px 0", borderBottom: "1px solid #eefbfd" }}>
              <div style={{ width: 40, height: 40, borderRadius: 10, background: "#e6f6fa", color: "#0e8fa8", display: "grid", placeItems: "center", flex: "0 0 auto" }}><FileText size={19} /></div>
              <div style={{ flex: 1, minWidth: 0 }}>
                <div style={{ fontSize: 14, fontWeight: 700, color: "#103a44", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>{t.title}</div>
                <div style={{ fontSize: 12, color: "var(--muted)", marginTop: 2 }}>{t.questions} Qs · {t.durationMin} min · {t.isFree ? "Free" : "Paid"}</div>
              </div>
              <button className="btn btn-gold btn-sm" onClick={onStart}><Play size={14} />Start</button>
            </div>
          ))}
        </div>

        <div className="card card-pad">
          <div className="sec-head"><div><div className="eyebrow">Strengths &amp; focus</div><div className="panel-title">Where you stand</div></div></div>
          <div className="sw-grid">
            <div className="sw-box s">
              <h4><CheckCircle2 size={15} style={{ color: SEM.strong }} />Strongest</h4>
              <div className="sw-list">{strong.map(([s, v]) => <div className="sw-item" key={s}><span>{s}</span><span style={{ color: SEM.strong }}>{v}%</span></div>)}</div>
            </div>
            <div className="sw-box w">
              <h4><Target size={15} style={{ color: SEM.weak }} />Needs work</h4>
              <div className="sw-list">{weak.map(([s, v]) => <div className="sw-item" key={s}><span>{s}</span><span style={{ color: SEM.weak }}>{v}%</span></div>)}</div>
            </div>
          </div>
        </div>
      </div>

      <div className="card card-pad mb">
        <div className="sec-head"><div><div className="eyebrow">Last 12 weeks</div><div className="panel-title">Study activity</div></div>
          <span style={{ fontSize: 13, color: "var(--muted)", fontWeight: 600 }}><Flame size={14} style={{ verticalAlign: -2, color: "var(--red)" }} /> {DERIVED.streak}-day streak</span></div>
        <div style={{ overflowX: "auto" }}>
          <div className="heat">{ACTIVITY.map((d, i) => <div key={i} className="heat-cell" style={{ background: heatColor(d.count) }} title={fmtDate(d.date) + ": " + d.count + " activities"} />)}</div>
        </div>
        <div className="heat-legend">Less {[0, 1, 2, 3, 4].map((c) => <span key={c} className="heat-cell" style={{ background: heatColor(c) }} />)} More</div>
      </div>
    </div>
  );
}

/* ============================================================
   VIEW: TEST SERIES
   ============================================================ */
function TestsView({ go, setAnalysis, onStart }) {
  const [tab, setTab] = useState("available");
  const attempted = [...ATTEMPTS].reverse();

  return (
    <div>
      <div className="tabs">
        {[["available", "Available (" + NEW_TESTS.length + ")"], ["upcoming", "Upcoming (" + UPCOMING.length + ")"], ["attempted", "Attempted (" + attempted.length + ")"]].map(([k, l]) => (
          <button key={k} className={"tab" + (tab === k ? " active" : "")} onClick={() => setTab(k)}>{l}</button>
        ))}
      </div>

      {tab === "available" && (
        <div className="test-grid">
          {NEW_TESTS.map((t) => (
            <div className="test-card" key={t.id}>
              <div className="test-top">
                <div><div className="test-title">{t.title}</div><div className="test-series">{t.series}</div></div>
                <Badge color={t.isFree ? { bg: "#e8f6ee", fg: "#1f8a4c" } : { bg: "#fff1ec", fg: "#ec5a52" }}>{t.isFree ? "Free" : "Paid"}</Badge>
              </div>
              <div className="test-meta"><span><Layers size={14} />{t.questions} Qs</span><span><Clock size={14} />{t.durationMin} min</span></div>
              <button className="btn btn-primary" onClick={onStart}><Play size={16} />Start test</button>
            </div>
          ))}
        </div>
      )}

      {tab === "upcoming" && (
        <div className="test-grid">
          {UPCOMING.map((t) => (
            <div className="test-card" key={t.id}>
              <div className="test-top">
                <div><div className="test-title">{t.title}</div><div className="test-series">{t.series}</div></div>
                <Badge color={{ bg: "#e6f6fa", fg: "#0e8fa8" }}><Calendar size={11} />{fmtDate(t.scheduledFor)}</Badge>
              </div>
              <div className="test-meta"><span><Layers size={14} />{t.questions} Qs</span><span><Clock size={14} />{t.durationMin} min</span></div>
              <button className="btn btn-ghost"><Bell size={16} />Set reminder</button>
            </div>
          ))}
        </div>
      )}

      {tab === "attempted" && (
        <div className="test-grid">
          {attempted.map((a) => {
            const pct = (a.score / a.maxScore) * 100, grade = gradeFor(pct);
            return (
              <div className="test-card" key={a.id}>
                <div className="test-top">
                  <div><div className="test-title">{a.title}</div><div className="test-series">{fmtDate(a.date)} · {a.series}</div></div>
                  <Badge color={{ bg: "#eefbfd", fg: grade.c }}>Grade {grade.g}</Badge>
                </div>
                <div className="test-score">
                  <div><div className="test-score-n" style={{ color: grade.c }}>{a.score}<span style={{ fontSize: 14, color: "var(--muted)" }}>/{a.maxScore}</span></div><div className="test-score-l">Score</div></div>
                  <div style={{ width: 1, alignSelf: "stretch", background: "#dcecf0" }} />
                  <div><div className="test-score-n" style={{ color: "var(--gold-2)" }}>{a.percentile}</div><div className="test-score-l">Percentile</div></div>
                  <div style={{ width: 1, alignSelf: "stretch", background: "#dcecf0" }} />
                  <div><div className="test-score-n">#{a.rank}</div><div className="test-score-l">Rank</div></div>
                </div>
                <button className="btn btn-ghost" onClick={() => setAnalysis(a)}><Eye size={16} />View analysis</button>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

/* ============================================================
   VIEW: PERFORMANCE
   ============================================================ */
function PerformanceView() {
  const trend = ATTEMPTS.map((a) => ({ name: fmtDate(a.date), score: +((a.score / a.maxScore) * 100).toFixed(0), pct: a.percentile, acc: a.accuracy, tpq: +(a.timeSec / a.totalQ).toFixed(0) }));
  const subjects = Object.entries(SUBJECT_STRENGTH).map(([name, acc]) => ({ name, acc, band: bandFor(acc) }));
  const radar = subjects.map((s) => ({ topic: s.name.length > 12 ? s.name.slice(0, 11) + "…" : s.name, You: s.acc }));
  const sortedSub = [...subjects].sort((a, b) => b.acc - a.acc);
  const cmp = [{ name: "You", value: +DERIVED.avgScore.toFixed(0), fill: "#0e8fa8" }, { name: "Batch Avg", value: 54, fill: "#94a8bc" }, { name: "Topper", value: 91, fill: "#f76b6b" }];

  return (
    <div>
      <div className="stats">
        <StatCard icon={<FileText size={20} />} color={{ bg: "#e6f6fa", fg: "#0e8fa8" }} n={DERIVED.n} label="Tests taken" />
        <StatCard icon={<Target size={20} />} color={{ bg: "#e8f6ee", fg: "#1f8a4c" }} n={DERIVED.avgScore.toFixed(0) + "%"} label="Avg score" sub={"best " + DERIVED.bestScore.toFixed(0) + "%"} />
        <StatCard icon={<Award size={20} />} color={{ bg: "#fff1ec", fg: "#ec5a52" }} n={DERIVED.bestPct} label="Best percentile" />
        <StatCard icon={<CheckCircle2 size={20} />} color={{ bg: "#e3f3f7", fg: "#2a8fb0" }} n={DERIVED.avgAcc.toFixed(0) + "%"} label="Avg accuracy" />
        <StatCard icon={<Clock size={20} />} color={{ bg: "#fbeaea", fg: "#cf4040" }} n={Math.round(DERIVED.totalTime / 60) + "m"} label="Total time" />
      </div>

      <div className="card card-pad mb">
        <div className="eyebrow">Your trajectory</div>
        <div className="panel-title">Score &amp; percentile over time</div>
        <p className="panel-note">Every attempt since you started — the trend is what matters, not any single test.</p>
        <div style={{ height: 280 }}>
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart data={trend} margin={{ top: 10, right: 10, left: -18, bottom: 0 }}>
              <defs><linearGradient id="g2" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stopColor="#0e8fa8" stopOpacity={0.25} /><stop offset="100%" stopColor="#0e8fa8" stopOpacity={0} /></linearGradient></defs>
              <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#eefbfd" />
              <XAxis dataKey="name" tick={{ fontSize: 11, fill: "#5e7d86" }} axisLine={false} tickLine={false} />
              <YAxis domain={[0, 100]} tick={{ fontSize: 11, fill: "#9bb4bc" }} axisLine={false} tickLine={false} unit="%" />
              <Tooltip contentStyle={{ borderRadius: 10, border: "1px solid #dcecf0", fontSize: 13 }} />
              <Area dataKey="score" name="Score %" stroke="#0e8fa8" strokeWidth={2.5} fill="url(#g2)" />
              <Line dataKey="pct" name="Percentile" stroke="#f76b6b" strokeWidth={2.5} dot={{ r: 3, fill: "#f76b6b" }} />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="grid2b mb">
        <div className="card card-pad">
          <div className="eyebrow">Diagnosis</div>
          <div className="panel-title">Subject strength map</div>
          <p className="panel-note">Accuracy across subjects, averaged over all attempts.</p>
          <div style={{ height: 270 }}>
            <ResponsiveContainer width="100%" height="100%">
              <RadarChart data={radar} outerRadius="72%">
                <PolarGrid stroke="#dde5ee" />
                <PolarAngleAxis dataKey="topic" tick={{ fontSize: 10.5, fill: "#5e7d86" }} />
                <PolarRadiusAxis domain={[0, 100]} tick={{ fontSize: 9, fill: "#b6cdd4" }} axisLine={false} />
                <Radar dataKey="You" stroke="#0e8fa8" fill="#0e8fa8" fillOpacity={0.28} strokeWidth={2} />
                <Tooltip formatter={(v) => [v + "%", "Accuracy"]} contentStyle={{ borderRadius: 10, border: "1px solid #dcecf0", fontSize: 13 }} />
              </RadarChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="card card-pad">
          <div className="eyebrow">Benchmark</div>
          <div className="panel-title">You vs batch vs topper</div>
          <p className="panel-note">Average score % against your batch and the topper.</p>
          <div style={{ height: 270 }}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={cmp} margin={{ top: 16, right: 8, left: -18, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#eefbfd" />
                <XAxis dataKey="name" tick={{ fontSize: 12, fill: "#5e7d86" }} axisLine={false} tickLine={false} />
                <YAxis domain={[0, 100]} tick={{ fontSize: 11, fill: "#9bb4bc" }} axisLine={false} tickLine={false} unit="%" />
                <Tooltip cursor={{ fill: "rgba(20,150,180,.04)" }} formatter={(v) => [v + "%", "Score"]} contentStyle={{ borderRadius: 10, border: "1px solid #dcecf0", fontSize: 13 }} />
                <Bar dataKey="value" radius={[7, 7, 0, 0]} maxBarSize={64}>
                  {cmp.map((e, i) => <Cell key={i} fill={e.fill} />)}
                  <LabelList dataKey="value" position="top" formatter={(v) => v + "%"} style={{ fontSize: 12, fontWeight: 800, fill: "#33495d" }} />
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      <div className="grid2b mb">
        <div className="card card-pad">
          <div className="eyebrow">Subject-wise</div>
          <div className="panel-title">Strong / Average / Weak</div>
          <p className="panel-note" style={{ marginBottom: 18 }}>Each subject graded by your accuracy.</p>
          {sortedSub.map((s) => {
            const col = SEM[s.band], bg = s.band === "strong" ? "var(--grn-bg)" : s.band === "average" ? "var(--amb-bg)" : "var(--red-bg)";
            return (
              <div className="topic-row" key={s.name}>
                <span className="topic-name">{s.name}</span>
                <div className="topic-track"><div className="topic-fill" style={{ width: s.acc + "%", background: col }} /></div>
                <span className="topic-band" style={{ background: bg, color: col }}>{s.band}</span>
              </div>
            );
          })}
        </div>

        <div className="card card-pad">
          <div className="eyebrow">Time management</div>
          <div className="panel-title">Avg time per question</div>
          <p className="panel-note">Trending down means you're getting faster.</p>
          <div style={{ height: 250 }}>
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={trend} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#eefbfd" />
                <XAxis dataKey="name" tick={{ fontSize: 11, fill: "#5e7d86" }} axisLine={false} tickLine={false} />
                <YAxis tick={{ fontSize: 11, fill: "#9bb4bc" }} axisLine={false} tickLine={false} unit="s" />
                <Tooltip formatter={(v) => [v + "s", "Per question"]} contentStyle={{ borderRadius: 10, border: "1px solid #dcecf0", fontSize: 13 }} />
                <Line dataKey="tpq" name="Time/Q" stroke="#149cba" strokeWidth={2.5} dot={{ r: 3, fill: "#149cba" }} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      <div className="card card-pad">
        <div className="eyebrow">Action plan</div>
        <div className="panel-title">What to focus on next</div>
        <p className="panel-note">Built from your performance across all attempts.</p>
        <div className="sw-grid">
          <div className="sw-box w">
            <h4><Target size={15} style={{ color: SEM.weak }} />Priority subjects</h4>
            <p style={{ margin: 0, fontSize: 13, color: "#3a5258", lineHeight: 1.55 }}>Your weakest areas are <b>{sortedSub.filter((s) => s.band === "weak").map((s) => s.name).join(", ")}</b>. Spend the next study cycle revising concepts and drilling 25–30 PYQs each before your next mock.</p>
          </div>
          <div className="sw-box s">
            <h4><TrendingUp size={15} style={{ color: SEM.strong }} />Momentum</h4>
            <p style={{ margin: 0, fontSize: 13, color: "#3a5258", lineHeight: 1.55 }}>Your score climbed from <b>{((ATTEMPTS[0].score / 50) * 100).toFixed(0)}%</b> to <b>{DERIVED.bestScore.toFixed(0)}%</b> and you're now in the <b>{DERIVED.bestPct}th percentile</b>. Keep the test-revise-retest loop going — consistency is paying off.</p>
          </div>
        </div>
      </div>
    </div>
  );
}

/* ============================================================
   VIEW: BATCHES
   ============================================================ */
function BatchesView({ go, onStart }) {
  return (
    <div>
      <div className="sec-head"><div><h2>My batches</h2><div className="note">Courses you're enrolled in</div></div></div>
      <div className="test-grid">
        {BATCHES.map((b) => {
          const p = (b.attemptedTests / b.totalTests) * 100;
          return (
            <div className="batch-card" key={b.id}>
              <div className="batch-bar" style={{ background: b.color }} />
              <div className="batch-body">
                <div className="batch-name">{b.name}</div>
                <div className="batch-exam">{b.examTarget} · valid till {fmtDate(b.validTill)}</div>
                <div className="progress"><div className="progress-fill" style={{ width: p + "%", background: b.color }} /></div>
                <div style={{ display: "flex", justifyContent: "space-between", fontSize: 12.5, color: "var(--muted)", fontWeight: 600 }}>
                  <span>{b.attemptedTests} of {b.totalTests} tests done</span><span>{p.toFixed(0)}%</span>
                </div>
                <button className="btn btn-primary" style={{ marginTop: 16 }} onClick={onStart}><Play size={16} />Continue batch</button>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

/* ============================================================
   VIEW: MATERIALS
   ============================================================ */
function MaterialsView({ toast }) {
  const [f, setF] = useState("all");
  const types = ["all", "pdf", "note", "video"];
  const filtered = MATERIALS.filter((m) => f === "all" || m.type === f);
  return (
    <div>
      <div className="tabs">{types.map((t) => <button key={t} className={"tab" + (f === t ? " active" : "")} onClick={() => setF(t)}>{t === "all" ? "All" : t.toUpperCase()}</button>)}</div>
      <div className="mat-grid">
        {filtered.map((m) => {
          const ti = TYPE_ICON[m.type];
          return (
            <div className="mat-card" key={m.id}>
              <div className="mat-ic" style={{ background: ti.c.bg, color: ti.c.fg }}>{ti.ic}</div>
              <div style={{ flex: 1, minWidth: 0 }}>
                <div className="mat-t">{m.title}</div>
                <div className="mat-sub">{m.subject} · {m.isFree ? <span style={{ color: "var(--green)", fontWeight: 700 }}>Free</span> : <span style={{ color: "var(--amber)", fontWeight: 700 }}>Paid</span>}</div>
              </div>
              <button className="btn btn-ghost btn-sm" onClick={() => toast("Opening: " + m.title)} style={{ flex: "0 0 auto" }}>{m.type === "video" ? <Play size={14} /> : <Eye size={14} />}Open</button>
            </div>
          );
        })}
      </div>
    </div>
  );
}

/* ============================================================
   VIEW: LEADERBOARD
   ============================================================ */
function LeaderboardView() {
  const me = LEADERBOARD.find((x) => x.you);
  const colors = ["#f76b6b", "#94a8bc", "#cd7f32"];
  return (
    <div>
      <div className="lb-you">
        <div style={{ textAlign: "center" }}>
          <div className="lb-rank-big">#{me.rank}</div>
          <div style={{ fontSize: 12, color: "#eafdff", marginTop: 4 }}>this week</div>
        </div>
        <div>
          <div style={{ fontSize: 18, fontWeight: 800 }}>You're in the top 10 this week!</div>
          <div style={{ fontSize: 13.5, color: "#eafdff", marginTop: 4 }}>Overall rank <b style={{ color: "#fff" }}>#{DERIVED.bestRank}</b> of 980 · top {Math.round((DERIVED.bestRank / 980) * 100)}% · <span style={{ color: "#7fe0a3" }}><ArrowUp size={13} style={{ verticalAlign: -2 }} />{me.move} this week</span></div>
        </div>
        <div style={{ textAlign: "center" }}>
          <div style={{ fontSize: 28, fontWeight: 800, color: "#ffd0c0" }}>{me.score}</div>
          <div style={{ fontSize: 12, color: "#eafdff" }}>avg score</div>
        </div>
      </div>

      <div className="card">
        <div className="sec-head" style={{ padding: "18px 20px 0" }}><div><h2>This week's top performers</h2><div className="note">Ranked by average score across attempts</div></div></div>
        <div style={{ marginTop: 14 }}>
          {LEADERBOARD.map((r, i) => (
            <div className={"lb-row" + (r.you ? " me" : "")} key={i}>
              <div className="lb-pos" style={{ color: i < 3 ? colors[i] : "var(--muted)" }}>{i < 3 ? <Medal size={18} style={{ color: colors[i] }} /> : r.rank}</div>
              <Avatar name={r.name} bg={r.you ? "#f76b6b" : "#0e8fa8"} />
              <div className="lb-name">{r.name}{r.you && <span style={{ marginLeft: 8, fontSize: 11, color: "var(--gold-2)", fontWeight: 800 }}>YOU</span>}<div style={{ fontSize: 11.5, color: "var(--muted)", fontWeight: 500 }}>{r.tests} tests</div></div>
              <div className="lb-move" style={{ color: r.move > 0 ? "var(--green)" : r.move < 0 ? "var(--red)" : "var(--muted)" }}>
                {r.move > 0 ? <ArrowUp size={13} /> : r.move < 0 ? <ArrowDown size={13} /> : "—"}{r.move !== 0 && Math.abs(r.move)}
              </div>
              <div className="lb-score">{r.score}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

/* ============================================================
   VIEW: PROFILE
   ============================================================ */
function ProfileView({ profile, setProfile, toast }) {
  const [form, setForm] = useState(profile);
  const [notif, setNotif] = useState({ email: true, sms: false, whatsapp: true });
  const earned = ACHIEVEMENTS.filter((a) => a.earned).length;
  const save = () => { setProfile(form); saveKey("dash:profile", form); toast("Profile updated"); };

  return (
    <div>
      <div className="card card-pad mb">
        <div className="prof-head">
          <div className="prof-av">{profile.name.split(" ").map((w) => w[0]).slice(0, 2).join("")}</div>
          <div style={{ flex: 1 }}>
            <div className="prof-name">{profile.name}</div>
            <div className="prof-meta">{profile.target} · Member since {fmtDate(profile.memberSince)}</div>
            <div style={{ display: "flex", gap: 8, marginTop: 10, flexWrap: "wrap" }}>
              <span className="chip" style={{ background: "#fff1ec", color: "#ec5a52" }}><Trophy size={13} />{earned}/{ACHIEVEMENTS.length} badges</span>
              <span className="chip" style={{ background: "#fbeaea", color: "#cf4040" }}><Flame size={13} />{DERIVED.streak}-day streak</span>
              <span className="chip" style={{ background: "#e8f6ee", color: "#1f8a4c" }}><Medal size={13} />Rank #{DERIVED.bestRank}</span>
            </div>
          </div>
        </div>
      </div>

      <div className="grid2b mb">
        <div className="card card-pad">
          <div className="eyebrow">Settings</div>
          <div className="panel-title" style={{ marginBottom: 16 }}>Exam target</div>
          <div className="field"><label>Full name</label><input className="inp" value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} /></div>
          <div className="field"><label>Target exam</label><input className="inp" value={form.target} onChange={(e) => setForm({ ...form, target: e.target.value })} /></div>
          <div className="field"><label>Target exam date</label><input className="inp" type="date" value={form.targetDate} onChange={(e) => setForm({ ...form, targetDate: e.target.value })} /></div>
          <button className="btn btn-primary" style={{ width: "auto" }} onClick={save}><Save size={16} />Save changes</button>
        </div>

        <div className="card card-pad">
          <div className="eyebrow">Notifications</div>
          <div className="panel-title" style={{ marginBottom: 8 }}>Reminders &amp; alerts</div>
          <div className="toggle-row"><div><div style={{ fontWeight: 700, fontSize: 14 }}>Email</div><div style={{ fontSize: 12.5, color: "var(--muted)" }}>Test reminders &amp; results</div></div>
            <button className={"switch" + (notif.email ? " on" : "")} onClick={() => setNotif({ ...notif, email: !notif.email })} /></div>
          <div className="toggle-row"><div><div style={{ fontWeight: 700, fontSize: 14 }}>SMS</div><div style={{ fontSize: 12.5, color: "var(--muted)" }}>Important updates only</div></div>
            <button className={"switch" + (notif.sms ? " on" : "")} onClick={() => setNotif({ ...notif, sms: !notif.sms })} /></div>
          <div className="toggle-row"><div><div style={{ fontWeight: 700, fontSize: 14 }}>WhatsApp</div><div style={{ fontSize: 12.5, color: "var(--muted)" }}>Daily practice nudges</div></div>
            <button className={"switch" + (notif.whatsapp ? " on" : "")} onClick={() => setNotif({ ...notif, whatsapp: !notif.whatsapp })} /></div>
        </div>
      </div>

      <div className="card card-pad">
        <div className="sec-head"><div><div className="eyebrow">Milestones</div><div className="panel-title">Achievements</div></div>
          <span style={{ fontSize: 13, fontWeight: 700, color: "var(--gold-2)" }}>{earned} of {ACHIEVEMENTS.length} unlocked</span></div>
        <div className="ach-grid">
          {ACHIEVEMENTS.map((a) => {
            const Icon = a.icon;
            return (
              <div className={"ach " + (a.earned ? "earned" : "locked")} key={a.key}>
                <div className="ach-ic" style={{ background: a.earned ? "linear-gradient(135deg,#ffb3a0,#f76b6b)" : "#eefbfd", color: a.earned ? "#fff" : "#9bb4bc" }}>
                  {a.earned ? <Icon size={24} /> : <Lock size={22} />}
                </div>
                <div className="ach-t">{a.title}</div>
                <div className="ach-d">{a.desc}</div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

/* ============================================================
   APP
   ============================================================ */
const NAV = [
  { id: "home", label: "Home", icon: Home },
  { id: "tests", label: "Test Series", icon: FileText },
  { id: "performance", label: "My Performance", icon: BarChart3 },
  { id: "batches", label: "My Batches", icon: GraduationCap },
  { id: "materials", label: "Study Material", icon: FolderOpen },
  { id: "leaderboard", label: "Leaderboard", icon: Trophy },
  { id: "profile", label: "Profile", icon: User },
];
const META = {
  home: { t: "Home", s: "Your preparation command centre" },
  tests: { t: "Test Series", s: "Attempt mocks and review past tests" },
  performance: { t: "My Performance", s: "Deep analytics across every attempt" },
  batches: { t: "My Batches", s: "Courses you're enrolled in" },
  materials: { t: "Study Material", s: "PDFs, notes and videos" },
  leaderboard: { t: "Leaderboard", s: "See where you rank" },
  profile: { t: "Profile", s: "Your account and achievements" },
};
const NOTIFS = [
  { ic: <Calendar size={16} />, c: { bg: "#e6f6fa", fg: "#0e8fa8" }, t: "All-India Grand Test 01", d: "Scheduled for 18 Jun · set a reminder" },
  { ic: <CheckCircle2 size={16} />, c: { bg: "#e8f6ee", fg: "#1f8a4c" }, t: "Result published", d: "BPSC Prelims Mock 05 · you scored 85th percentile" },
  { ic: <FolderOpen size={16} />, c: { bg: "#e3f3f7", fg: "#2a8fb0" }, t: "New material added", d: "June 2026 Current Affairs Compilation" },
];

function App({ onLaunchExam, onLogout }) {
  const [view, setView] = useState("home");
  const [loading, setLoading] = useState(true);
  const [sbOpen, setSbOpen] = useState(false);
  const [bellOpen, setBellOpen] = useState(false);
  const [analysis, setAnalysis] = useState(null);
  const [toasts, setToasts] = useState([]);
  const [profile, setProfile] = useState({ name: "Priyadarshee Kumar", target: "BPSC Prelims 2026", targetDate: "2026-09-20", memberSince: "2026-03-01", email: "priyadarshee@example.com" });

  const toast = (msg) => { const id = uid(); setToasts((t) => [...t, { id, msg }]); setTimeout(() => setToasts((t) => t.filter((x) => x.id !== id)), 2600); };

  useEffect(() => {
    (async () => {
      const saved = await loadKey("dash:profile", null);
      if (saved) setProfile((p) => ({ ...p, ...saved }));
      setLoading(false);
    })();
  }, []);

  if (loading) return <div className="sd-root"><style>{CSS}</style><div className="loader">Loading your dashboard…</div></div>;

  const go = (v) => { setView(v); setSbOpen(false); };

  return (
    <div className="sd-root" onClick={() => bellOpen && setBellOpen(false)}>
      <style>{CSS}</style>

      {sbOpen && <div className="scrim" onClick={() => setSbOpen(false)} />}
      <aside className={"sb" + (sbOpen ? " open" : "")}>
        <div className="sb-brand">
          <div className="sb-logo">
            <div className="sb-mark">P</div>
            <div><div className="sb-name">PrepEngine</div><div className="sb-tag">Student</div></div>
          </div>
        </div>
        <nav className="sb-nav">
          {NAV.map((it) => { const Icon = it.icon; return (
            <button key={it.id} className={"sb-item" + (view === it.id ? " active" : "")} onClick={() => go(it.id)}><Icon size={18} />{it.label}</button>
          ); })}
          <div className="sb-streak">
            <div className="sb-streak-top"><Flame size={17} />{DERIVED.streak}-day streak</div>
            <div className="sb-streak-sub">Don't break the chain — practise today!</div>
          </div>
        </nav>
        <div style={{ padding: "14px 16px", borderTop: "1px solid rgba(255,255,255,.08)", fontSize: 11.5, color: "#bfe6ee" }}>
          {daysUntil(profile.targetDate)} days to {profile.target}
        </div>
      </aside>

      <div className="main">
        <header className="topbar">
          <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
            <button className="hamburger" onClick={() => setSbOpen(true)}><Menu size={20} /></button>
            <div><h1>{META[view].t}</h1><div className="sub">{META[view].s}</div></div>
          </div>
          <div className="tb-right">
            <div style={{ position: "relative" }} onClick={(e) => e.stopPropagation()}>
              <button className="bell" onClick={() => setBellOpen(!bellOpen)}><Bell size={19} /><span className="bell-dot" /></button>
              {bellOpen && (
                <div className="notif">
                  <div className="notif-head">Notifications</div>
                  {NOTIFS.map((n, i) => (
                    <div className="notif-item" key={i}>
                      <div className="notif-ic" style={{ background: n.c.bg, color: n.c.fg }}>{n.ic}</div>
                      <div><div className="notif-t">{n.t}</div><div className="notif-d">{n.d}</div></div>
                    </div>
                  ))}
                </div>
              )}
            </div>
            <button className="bell" title="Log out" onClick={onLogout} style={{ marginRight: 2 }}><LogOut size={19} /></button>
            <div className="tb-av">{profile.name.split(" ").map((w) => w[0]).slice(0, 2).join("")}</div>
          </div>
        </header>

        <main className="content">
          {view === "home" && <HomeView profile={profile} go={go} setAnalysis={setAnalysis} onStart={onLaunchExam} />}
          {view === "tests" && <TestsView go={go} setAnalysis={setAnalysis} onStart={onLaunchExam} />}
          {view === "performance" && <PerformanceView />}
          {view === "batches" && <BatchesView go={go} onStart={onLaunchExam} />}
          {view === "materials" && <MaterialsView toast={toast} />}
          {view === "leaderboard" && <LeaderboardView />}
          {view === "profile" && <ProfileView profile={profile} setProfile={setProfile} toast={toast} />}
        </main>
      </div>

      <div className="toasts">{toasts.map((t) => <div className="toast" key={t.id}><CheckCircle2 size={18} />{t.msg}</div>)}</div>
      {analysis && <AnalysisModal a={analysis} onClose={() => setAnalysis(null)} />}
    </div>
  );
}

return App;
})();

/* ============================================================
   LOGIN SCREEN
   ============================================================ */
const LOGIN_CSS = `
.login-root{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  min-height:100vh;background:url("data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20viewBox%3D%270%200%201200%20360%27%3E%3Cg%20fill%3D%27none%27%20stroke%3D%27%230a4f5e%27%20stroke-width%3D%273.2%27%20stroke-linecap%3D%27round%27%3E%3Cpath%20d%3D%27M120%2095%20q22%20-20%2044%200%20q22%20-20%2044%200%27%20opacity%3D%270.20%27%2F%3E%3Cpath%20d%3D%27M300%2062%20q16%20-14%2032%200%20q16%20-14%2032%200%27%20opacity%3D%270.16%27%2F%3E%3Cpath%20d%3D%27M520%20102%20q20%20-18%2040%200%20q20%20-18%2040%200%27%20opacity%3D%270.18%27%2F%3E%3Cpath%20d%3D%27M720%2056%20q14%20-12%2028%200%20q14%20-12%2028%200%27%20opacity%3D%270.14%27%2F%3E%3Cpath%20d%3D%27M900%2098%20q24%20-22%2048%200%20q24%20-22%2048%200%27%20opacity%3D%270.20%27%2F%3E%3Cpath%20d%3D%27M1050%2066%20q16%20-14%2032%200%20q16%20-14%2032%200%27%20opacity%3D%270.16%27%2F%3E%3Cpath%20d%3D%27M430%20152%20q12%20-10%2024%200%20q12%20-10%2024%200%27%20opacity%3D%270.12%27%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat center 16px / 88% auto,radial-gradient(ellipse 55% 50% at 16% 4%, rgba(255,255,255,.55), transparent 72%),radial-gradient(ellipse 46% 42% at 83% 2%, rgba(255,255,255,.40), transparent 72%),url("data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20viewBox%3D%270%200%201200%20220%27%3E%3Cdefs%3E%3ClinearGradient%20id%3D%27bk0%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%23b5714f%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%23b5714f%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk1%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%23ad8c48%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%23ad8c48%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk2%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%235d8576%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%235d8576%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk3%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%236f6398%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%236f6398%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk4%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%233f7a88%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%233f7a88%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk5%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%239a564c%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%239a564c%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk6%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%237e8a4e%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%237e8a4e%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk7%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%2348688f%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%2348688f%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3C%2Fdefs%3E%3Cg%20opacity%3D%270.42%27%3E%3Crect%20x%3D%270%27%20y%3D%270%27%20width%3D%2723%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%2724%27%20y%3D%270%27%20width%3D%2732%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%2757%27%20y%3D%270%27%20width%3D%2741%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%2799%27%20y%3D%270%27%20width%3D%2716%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27116%27%20y%3D%270%27%20width%3D%2725%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27142%27%20y%3D%270%27%20width%3D%2734%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27177%27%20y%3D%270%27%20width%3D%2743%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%27221%27%20y%3D%270%27%20width%3D%2718%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%27240%27%20y%3D%270%27%20width%3D%2727%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%27268%27%20y%3D%270%27%20width%3D%2736%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%27305%27%20y%3D%270%27%20width%3D%2745%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%27351%27%20y%3D%270%27%20width%3D%2720%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27372%27%20y%3D%270%27%20width%3D%2729%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27402%27%20y%3D%270%27%20width%3D%2738%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27441%27%20y%3D%270%27%20width%3D%2747%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%27489%27%20y%3D%270%27%20width%3D%2722%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%27512%27%20y%3D%270%27%20width%3D%2731%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%27544%27%20y%3D%270%27%20width%3D%2740%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%27585%27%20y%3D%270%27%20width%3D%2749%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%27635%27%20y%3D%270%27%20width%3D%2724%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27660%27%20y%3D%270%27%20width%3D%2733%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27694%27%20y%3D%270%27%20width%3D%2742%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27737%27%20y%3D%270%27%20width%3D%2717%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%27755%27%20y%3D%270%27%20width%3D%2726%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%27782%27%20y%3D%270%27%20width%3D%2735%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%27818%27%20y%3D%270%27%20width%3D%2744%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%27863%27%20y%3D%270%27%20width%3D%2719%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%27883%27%20y%3D%270%27%20width%3D%2728%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27912%27%20y%3D%270%27%20width%3D%2737%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27950%27%20y%3D%270%27%20width%3D%2746%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27997%27%20y%3D%270%27%20width%3D%2721%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%271019%27%20y%3D%270%27%20width%3D%2730%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%271050%27%20y%3D%270%27%20width%3D%2739%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%271090%27%20y%3D%270%27%20width%3D%2748%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%271139%27%20y%3D%270%27%20width%3D%2723%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%271163%27%20y%3D%270%27%20width%3D%2732%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%271196%27%20y%3D%270%27%20width%3D%2741%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom / 100% 30%,linear-gradient(135deg,#32c7de 0%,#179fbe 58%,#0e8fa8 100%);
  display:grid;place-items:center;padding:24px;color:#0e3540}
.login-root *{box-sizing:border-box}
.login-root button{font-family:inherit;cursor:pointer;border:none}
.login-card{display:grid;grid-template-columns:1fr 1fr;max-width:880px;width:100%;background:#fff;
  border-radius:22px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.4)}
@media(max-width:760px){.login-card{grid-template-columns:1fr;max-width:430px}.login-brand{display:none}}
.login-brand{background:radial-gradient(ellipse 60% 55% at 20% 0%, rgba(255,255,255,.28), transparent 75%),linear-gradient(150deg,#0f93a8,#0a6173);color:#fff;padding:40px 34px;display:flex;flex-direction:column}
.lb-mark{width:52px;height:52px;border-radius:14px;background:linear-gradient(135deg,#ff9a86,#f25b54);
  display:grid;place-items:center;font-weight:800;font-size:24px;color:#fff;margin-bottom:22px}
.lb-title{font-size:26px;font-weight:800;letter-spacing:-.02em;text-shadow:0 1px 12px rgba(8,70,84,.30)}
.lb-sub{font-size:14px;color:#eafdff;margin-top:8px;line-height:1.5}
.lb-points{list-style:none;padding:0;margin:30px 0 0;display:flex;flex-direction:column;gap:14px}
.lb-points li{display:flex;align-items:center;gap:11px;font-size:14px;color:#d6f1f7;font-weight:500}
.lb-points li svg{color:#7fe0a3;flex:0 0 auto}
.lb-foot{margin-top:auto;padding-top:30px;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#8fb8c4;font-weight:700}
.login-form{padding:40px 36px;display:flex;flex-direction:column}
.login-form h2{margin:0;font-size:23px;font-weight:800;letter-spacing:-.01em}
.lf-sub{margin:6px 0 22px;font-size:13.5px;color:#5e7d86}
.lf-tabs{display:flex;gap:8px;margin-bottom:20px}
.lf-tabs button{flex:1;display:flex;align-items:center;justify-content:center;gap:7px;padding:10px;border-radius:9px;
  border:1.5px solid #cfe3e9;background:#fff;font-size:13.5px;font-weight:700;color:#5e7d86;transition:.13s}
.lf-tabs button.on{border-color:#0e8fa8;background:#e6f6fa;color:#0e8fa8}
.lf-field{margin-bottom:14px}
.lf-field label{display:block;font-size:12.5px;font-weight:700;color:#3a5258;margin-bottom:6px}
.lf-field input{width:100%;padding:11px 13px;border:1.5px solid #cfe3e9;border-radius:9px;font-size:14px;outline:none;color:#0e3540}
.lf-field input:focus{border-color:#0e8fa8;box-shadow:0 0 0 3px rgba(20,150,180,.1)}
.lf-primary{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;background:linear-gradient(135deg,#1bb6d2,#0e9bb5);box-shadow:0 8px 22px rgba(20,150,180,.40);color:#fff;
  font-weight:700;font-size:15px;padding:13px;border-radius:10px;margin-top:6px;transition:.14s}
.lf-primary:hover{background:#0a6173}
.lf-divider{display:flex;align-items:center;gap:12px;margin:18px 0;color:#9bb4bc;font-size:12px}
.lf-divider::before,.lf-divider::after{content:"";flex:1;height:1px;background:#dcecf0}
.lf-google{display:flex;align-items:center;justify-content:center;gap:10px;width:100%;background:#fff;border:1.5px solid #cfe3e9;
  font-weight:700;font-size:14px;padding:12px;border-radius:10px;color:#43585f;transition:.13s}
.lf-google:hover{background:#f1fafc;border-color:#a8d4de}
.lf-gicon{width:18px;height:18px;border-radius:50%;background:#fff;display:grid;place-items:center;font-weight:800;font-size:13px;color:#4285F4;border:1px solid #dcecf0}
.lf-admin{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;margin-top:12px;background:#fff2ee;
  border:1.5px solid #ffd2c6;color:#c24a42;font-weight:700;font-size:13.5px;padding:12px;border-radius:10px;transition:.13s}
.lf-admin:hover{background:#ffe6df}
.lf-note{margin-top:18px;font-size:12px;color:#90a3b6;text-align:center;line-height:1.5}
`;

function LoginScreen({ onStudent, onAdmin }) {
  const [method, setMethod] = useState("email");
  return (
    <div className="login-root">
      <style>{LOGIN_CSS}</style>
      <div className="login-card">
        <div className="login-brand">
          <div className="lb-mark">P</div>
          <div className="lb-title">PrepEngine</div>
          <div className="lb-sub">Your all-in-one exam preparation platform for civil services aspirants.</div>
          <ul className="lb-points">
            <li><CheckCircle2 size={17} /> Real exam-style mock tests</li>
            <li><CheckCircle2 size={17} /> Deep performance analytics</li>
            <li><CheckCircle2 size={17} /> Rank, percentile &amp; leaderboard</li>
          </ul>
          <div className="lb-foot">BPSC &middot; UPSC &middot; State PSC</div>
        </div>
        <div className="login-form">
          <h2>Welcome back</h2>
          <div className="lf-sub">Sign in to continue your preparation</div>
          <div className="lf-tabs">
            <button className={method === "email" ? "on" : ""} onClick={() => setMethod("email")}><Mail size={15} /> Email</button>
            <button className={method === "phone" ? "on" : ""} onClick={() => setMethod("phone")}><Phone size={15} /> Phone</button>
          </div>
          {method === "email" ? (
            <>
              <div className="lf-field"><label>Email address</label><input placeholder="you@example.com" /></div>
              <div className="lf-field"><label>Password</label><input type="password" placeholder="\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022" /></div>
            </>
          ) : (
            <>
              <div className="lf-field"><label>Phone number</label><input placeholder="+91 90000 00000" /></div>
              <div className="lf-field"><label>OTP</label><input placeholder="6-digit code" /></div>
            </>
          )}
          <button className="lf-primary" onClick={onStudent}>Sign in <ArrowRight size={17} /></button>
          <div className="lf-divider">or</div>
          <button className="lf-google" onClick={onStudent}><span className="lf-gicon">G</span> Continue with Google</button>
          <button className="lf-admin" onClick={onAdmin}><ShieldCheck size={16} /> Enter admin console</button>
          <div className="lf-note">Demo mode &mdash; choose how you'd like to explore. No real account needed yet.</div>
        </div>
      </div>
    </div>
  );
}

/* ============================================================
   ROOT ROUTER
   ============================================================ */
export default function App() {
  const [route, setRoute] = useState("login");
useEffect(() => {
    import("@supabase/supabase-js").then(({ createClient }) => {
      const sb = createClient(
        import.meta.env.VITE_SUPABASE_URL,
        import.meta.env.VITE_SUPABASE_ANON_KEY
      );
      sb.auth.getSession().then(({ data }) => {
        if (data.session) setRoute("student");
      });
    });
  }, []);
  if (route === "login") return <LoginScreen onStudent={() => setRoute("student")} onAdmin={() => setRoute("admin")} />;
  if (route === "student") return <StudentApp onLaunchExam={() => setRoute("exam")} onLogout={() => setRoute("login")} />;
  if (route === "exam") return <ExamApp onExit={() => setRoute("student")} />;
  if (route === "admin") return <AdminApp onLogout={() => setRoute("login")} />;
  return null;
}