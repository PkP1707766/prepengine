import React, { useState, useEffect, useRef, useMemo, useCallback } from "react";
import { FileText, GraduationCap, FolderOpen, Search, X, Check, ChevronRight, Menu, CheckCircle2, BookOpen, Clock, Layers, Eye, Save, TrendingUp, Home, BarChart3, Trophy, User, Flame, Target, Award, Play, RotateCcw, Lock, Calendar, Bell, Zap, ArrowUp, ArrowDown, Medal, Sparkles, LogOut, Share2, Camera, Gift, Copy, Users, UserPlus, Wallet, IndianRupee, MessageSquare, Star, Send } from "lucide-react";
import { AreaChart, Area, LineChart, Line, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell, LabelList } from "recharts";
import { DiyaLogo } from "../ui/Brand.jsx";
import { ChromeControls } from "../lib/i18n.jsx";
import { useLang } from "../lib/contexts.js";
import { EmptyState, ErrorState } from "../ui/Feedback.jsx";

import * as DB from "../lib/db.js";
import { fmtDate, fmtDuration, daysUntil, uid, initials, gradeFor, SEM } from "../lib/format.js";
import Pattern from "../ui/Pattern.jsx";
import { ReviewCard, ReviewStyles } from "../ui/Review.jsx";

const StudentApp = (() => {
/* ============================================================
   LIVE DATA
   Everything on the student side used to come from hardcoded
   arrays — attempts, tests, batches, materials, the leaderboard,
   the activity heatmap. All of it now comes from the database
   through one context, loaded once and shared by every view.
   ============================================================ */
const DataCtx = React.createContext(null);
const useData = () => React.useContext(DataCtx);

const QUOTES = ["sd_q1", "sd_q2", "sd_q3", "sd_q4", "sd_q5"];

/** Aggregates the dashboard needs, derived from real attempts. */
function derive(attempts, activity) {
  const n = attempts.length;
  if (n === 0) {
    return { n: 0, avgScore: 0, bestScore: 0, bestPct: null, bestRank: null,
             avgAcc: 0, bestAcc: 0, totalTime: 0, streak: DB.streakFrom(activity),
             activeDays: activity.filter((d) => d.count > 0).length, lastDelta: null };
  }
  const scorePcts = attempts.map((a) => a.scorePct);
  const percentiles = attempts.map((a) => a.percentile).filter((p) => typeof p === "number");
  const ranks = attempts.map((a) => a.rank).filter((r) => typeof r === "number");
  const avgScore = scorePcts.reduce((x, y) => x + y, 0) / n;
  const lastTwo = scorePcts.slice(-2);
  return {
    n,
    avgScore,
    bestScore: Math.max(...scorePcts),
    bestPct: percentiles.length ? Math.max(...percentiles) : null,
    bestRank: ranks.length ? Math.min(...ranks) : null,
    avgAcc: attempts.reduce((x, a) => x + a.accuracy, 0) / n,
    bestAcc: Math.max(...attempts.map((a) => a.accuracy)),
    totalTime: attempts.reduce((x, a) => x + a.timeSec, 0),
    streak: DB.streakFrom(activity),
    activeDays: activity.filter((d) => d.count > 0).length,
    lastDelta: lastTwo.length === 2 ? lastTwo[1] - lastTwo[0] : null,
  };
}

/** Badges a student has genuinely earned — no participation trophies.
 *  Titles and blurbs are dictionary keys, not text: hardcoded here they stayed
 *  English on a Hindi profile. */
function achievementsFor(d) {
  return [
    { key: "first", tKey: "ach_first_t", dKey: "ach_first_d", icon: Play, earned: d.n >= 1 },
    { key: "ten", tKey: "ach_ten_t", dKey: "ach_ten_d", icon: FileText, earned: d.n >= 10 },
    { key: "score70", tKey: "ach_score_t", dKey: "ach_score_d", icon: Target, earned: d.bestScore >= 70 },
    { key: "streak7", tKey: "ach_fire_t", dKey: "ach_fire_d", icon: Flame, earned: d.streak >= 7 },
    { key: "pct80", tKey: "ach_pct_t", dKey: "ach_pct_d", icon: TrendingUp, earned: (d.bestPct ?? 0) >= 80 },
    { key: "rank100", tKey: "ach_rank_t", dKey: "ach_rank_d", icon: Medal, earned: d.bestRank != null && d.bestRank <= 100 },
    { key: "acc90", tKey: "ach_acc_t", dKey: "ach_acc_d", icon: Zap, earned: d.bestAcc >= 90 },
    { key: "twentyfive", tKey: "ach_25_t", dKey: "ach_25_d", icon: Award, earned: d.n >= 25 },
    { key: "top10", tKey: "ach_top10_t", dKey: "ach_top10_d", icon: Trophy, earned: d.bestRank != null && d.bestRank <= 10 },
    { key: "streak30", tKey: "ach_un_t", dKey: "ach_un_d", icon: Sparkles, earned: d.streak >= 30 },
  ];
}


const CSS = `
:root{
  --navy:#b8923a; --navy-2:#5b1414; --gold:#dca84a; --gold-2:#d4a64a;
  --bg:#fdf6e3; --card:#ffffff; --ink:#2a1810; --muted:#7a6450; --line:#e8dcc0;
  --green:#1f8a4c; --amber:#d4a64a; --red:#c0392b; --blue:#c39d44; --purple:#7a1f1f;
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
.sd-root{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--ink);
  font-variant-numeric:tabular-nums;line-height:1.5;background:var(--bg);min-height:100vh;display:flex}
.sd-root :where(button){font-family:inherit;cursor:pointer;border:none;background:none}
.sd-root input{font-family:inherit}
.sd-root a{text-decoration:none}

/* SIDEBAR */
.sb{width:244px;background:linear-gradient(180deg,#7c5e16,#5e4610);color:#ecdcb6;flex:0 0 auto;display:flex;flex-direction:column;position:sticky;top:0;height:100vh;z-index:40}
.sb-brand{padding:20px;border-bottom:1px solid rgba(255,255,255,.08)}
.sb-logo{display:flex;align-items:center;gap:11px}
.sb-mark{width:36px;height:36px;border-radius:9px;background:linear-gradient(135deg,var(--gold),var(--gold-2));display:grid;place-items:center;color:#ffffff;font-weight:800;font-size:16px;flex:0 0 auto}
.sb-name{font-weight:800;font-size:15px;color:#ffffff;line-height:1.15}
.sb-tag{font-size:11px;color:#e8d8b0}
.sb-nav{flex:1;padding:14px 12px;overflow-y:auto}
.sb-item{display:flex;align-items:center;gap:12px;padding:11px 13px;border-radius:9px;font-size:14px;font-weight:600;color:#d8cba6;width:100%;text-align:left;transition:.13s;margin-bottom:3px;position:relative}
.sb-item:hover{background:rgba(255,255,255,.06);color:#ffffff}
.sb-item.active{background:rgba(255,255,255,.1);color:#ffffff}
.sb-item.active::before{content:"";position:absolute;left:0;top:8px;bottom:8px;width:3px;border-radius:3px;background:var(--gold)}
.sb-streak{margin:8px 12px 0;background:rgba(247,107,107,.14);border:1px solid rgba(247,107,107,.3);border-radius:11px;padding:13px 14px}
.sb-streak-top{display:flex;align-items:center;gap:8px;color:#f2dcae;font-weight:800;font-size:14px}
.sb-streak-sub{font-size:11.5px;color:#f1e4c4;margin-top:4px}

/* MAIN */
.main{flex:1;min-width:0;display:flex;flex-direction:column}
.topbar{background:#ffffff;border-bottom:1px solid var(--line);padding:13px 26px;display:flex;align-items:center;justify-content:space-between;gap:14px;position:sticky;top:0;z-index:30}
.topbar h1{margin:0;font-size:19px;font-weight:800;letter-spacing:-.01em}
.topbar .sub{font-size:12.5px;color:var(--muted);margin-top:1px}
.tb-right{display:flex;align-items:center;gap:14px}
.bell{position:relative;width:40px;height:40px;border-radius:10px;border:1px solid var(--line);display:grid;place-items:center;color:#7a6450}
.bell:hover{background:#fdf6e3;color:var(--navy)}
.bell-dot{position:absolute;top:9px;right:9px;width:8px;height:8px;border-radius:50%;background:var(--red);border:1.5px solid #ffffff}
.notif{position:absolute;top:52px;right:0;width:320px;background:#ffffff;border:1px solid var(--line);border-radius:13px;box-shadow:0 16px 40px rgba(20,120,140,.18);overflow:hidden;z-index:50}
.notif-head{padding:14px 16px;border-bottom:1px solid var(--line);font-weight:800;font-size:14px}
.notif-item{display:flex;gap:11px;padding:13px 16px;border-bottom:1px solid #fdf6e3}
.notif-item:last-child{border-bottom:none}
.notif-ic{width:32px;height:32px;border-radius:8px;display:grid;place-items:center;flex:0 0 auto}
.notif-t{font-size:13px;font-weight:700;color:#2e1c12}
.notif-d{font-size:12px;color:var(--muted);margin-top:2px}
.tb-av{width:38px;height:38px;border-radius:10px;background:var(--navy);color:#ffffff;display:grid;place-items:center;font-weight:800;font-size:14px;border:0;cursor:pointer;padding:0;font-family:inherit;transition:transform .16s ease,box-shadow .16s ease}
.tb-av:hover{transform:translateY(-1px);box-shadow:0 6px 16px rgba(90,40,10,.22)}
.hamburger{display:none;width:40px;height:40px;border-radius:10px;border:1px solid var(--line);align-items:center;justify-content:center}
.content{padding:26px;max-width:1240px;width:100%;margin:0 auto}
.sd-foot{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;
  padding:20px 26px 26px;max-width:1240px;margin:0 auto;width:100%;
  border-top:1px solid var(--line);font-size:12.5px;color:var(--muted)}
.sd-foot a,.sd-foot button.flink{color:var(--navy);text-decoration:none;font-weight:600;
  background:none;border:0;font-family:inherit;font-size:inherit;cursor:pointer;padding:0}
.sd-foot a:hover,.sd-foot button.flink:hover{text-decoration:underline}

/* CARDS */
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;box-shadow:0 1px 3px rgba(20,120,140,.05)}
.card-pad{padding:22px}
.sec-head{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:16px;flex-wrap:wrap}
.sec-head h2{margin:0;font-size:16px;font-weight:800}
.sec-head .note{font-size:12.5px;color:var(--muted);margin-top:2px}
.eyebrow{font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-2);font-weight:800}

/* HERO */
.hero{background:url("data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20viewBox%3D%270%200%201200%20360%27%3E%3Cg%20fill%3D%27none%27%20stroke%3D%27%230a4f5e%27%20stroke-width%3D%273.2%27%20stroke-linecap%3D%27round%27%3E%3Cpath%20d%3D%27M120%2095%20q22%20-20%2044%200%20q22%20-20%2044%200%27%20opacity%3D%270.20%27%2F%3E%3Cpath%20d%3D%27M300%2062%20q16%20-14%2032%200%20q16%20-14%2032%200%27%20opacity%3D%270.16%27%2F%3E%3Cpath%20d%3D%27M520%20102%20q20%20-18%2040%200%20q20%20-18%2040%200%27%20opacity%3D%270.18%27%2F%3E%3Cpath%20d%3D%27M720%2056%20q14%20-12%2028%200%20q14%20-12%2028%200%27%20opacity%3D%270.14%27%2F%3E%3Cpath%20d%3D%27M900%2098%20q24%20-22%2048%200%20q24%20-22%2048%200%27%20opacity%3D%270.20%27%2F%3E%3Cpath%20d%3D%27M1050%2066%20q16%20-14%2032%200%20q16%20-14%2032%200%27%20opacity%3D%270.16%27%2F%3E%3Cpath%20d%3D%27M430%20152%20q12%20-10%2024%200%20q12%20-10%2024%200%27%20opacity%3D%270.12%27%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat center 16px / 88% auto,radial-gradient(ellipse 55% 50% at 16% 4%, rgba(255,255,255,.55), transparent 72%),radial-gradient(ellipse 46% 42% at 83% 2%, rgba(255,255,255,.40), transparent 72%),url("data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20viewBox%3D%270%200%201200%20220%27%3E%3Cdefs%3E%3ClinearGradient%20id%3D%27bk0%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%23b5714f%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%23b5714f%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk1%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%23ad8c48%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%23ad8c48%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk2%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%235d8576%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%235d8576%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk3%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%236f6398%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%236f6398%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk4%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%233f7a88%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%233f7a88%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk5%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%239a564c%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%239a564c%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk6%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%237e8a4e%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%237e8a4e%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3ClinearGradient%20id%3D%27bk7%27%20x1%3D%270%27%20y1%3D%270%27%20x2%3D%270%27%20y2%3D%271%27%3E%3Cstop%20offset%3D%270.04%27%20stop-color%3D%27%2348688f%27%20stop-opacity%3D%270%27%2F%3E%3Cstop%20offset%3D%271%27%20stop-color%3D%27%2348688f%27%20stop-opacity%3D%270.62%27%2F%3E%3C%2FlinearGradient%3E%3C%2Fdefs%3E%3Cg%20opacity%3D%270.42%27%3E%3Crect%20x%3D%270%27%20y%3D%270%27%20width%3D%2723%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%2724%27%20y%3D%270%27%20width%3D%2732%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%2757%27%20y%3D%270%27%20width%3D%2741%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%2799%27%20y%3D%270%27%20width%3D%2716%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27116%27%20y%3D%270%27%20width%3D%2725%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27142%27%20y%3D%270%27%20width%3D%2734%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27177%27%20y%3D%270%27%20width%3D%2743%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%27221%27%20y%3D%270%27%20width%3D%2718%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%27240%27%20y%3D%270%27%20width%3D%2727%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%27268%27%20y%3D%270%27%20width%3D%2736%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%27305%27%20y%3D%270%27%20width%3D%2745%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%27351%27%20y%3D%270%27%20width%3D%2720%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27372%27%20y%3D%270%27%20width%3D%2729%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27402%27%20y%3D%270%27%20width%3D%2738%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27441%27%20y%3D%270%27%20width%3D%2747%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%27489%27%20y%3D%270%27%20width%3D%2722%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%27512%27%20y%3D%270%27%20width%3D%2731%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%27544%27%20y%3D%270%27%20width%3D%2740%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%27585%27%20y%3D%270%27%20width%3D%2749%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%27635%27%20y%3D%270%27%20width%3D%2724%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27660%27%20y%3D%270%27%20width%3D%2733%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27694%27%20y%3D%270%27%20width%3D%2742%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27737%27%20y%3D%270%27%20width%3D%2717%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%27755%27%20y%3D%270%27%20width%3D%2726%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%27782%27%20y%3D%270%27%20width%3D%2735%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%27818%27%20y%3D%270%27%20width%3D%2744%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%27863%27%20y%3D%270%27%20width%3D%2719%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%27883%27%20y%3D%270%27%20width%3D%2728%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%27912%27%20y%3D%270%27%20width%3D%2737%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3Crect%20x%3D%27950%27%20y%3D%270%27%20width%3D%2746%27%20height%3D%27220%27%20fill%3D%27url%28%23bk5%29%27%2F%3E%3Crect%20x%3D%27997%27%20y%3D%270%27%20width%3D%2721%27%20height%3D%27220%27%20fill%3D%27url%28%23bk6%29%27%2F%3E%3Crect%20x%3D%271019%27%20y%3D%270%27%20width%3D%2730%27%20height%3D%27220%27%20fill%3D%27url%28%23bk7%29%27%2F%3E%3Crect%20x%3D%271050%27%20y%3D%270%27%20width%3D%2739%27%20height%3D%27220%27%20fill%3D%27url%28%23bk0%29%27%2F%3E%3Crect%20x%3D%271090%27%20y%3D%270%27%20width%3D%2748%27%20height%3D%27220%27%20fill%3D%27url%28%23bk1%29%27%2F%3E%3Crect%20x%3D%271139%27%20y%3D%270%27%20width%3D%2723%27%20height%3D%27220%27%20fill%3D%27url%28%23bk2%29%27%2F%3E%3Crect%20x%3D%271163%27%20y%3D%270%27%20width%3D%2732%27%20height%3D%27220%27%20fill%3D%27url%28%23bk3%29%27%2F%3E%3Crect%20x%3D%271196%27%20y%3D%270%27%20width%3D%2741%27%20height%3D%27220%27%20fill%3D%27url%28%23bk4%29%27%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom / 100% 42%,linear-gradient(135deg,#9a2a2a 0%,#c39d44 100%);border-radius:18px;color:#ffffff;padding:26px 28px;display:grid;grid-template-columns:1fr auto;gap:24px;align-items:center;box-shadow:0 16px 40px rgba(18,140,170,.26);margin-bottom:22px;overflow:hidden}
@media(max-width:680px){.hero{grid-template-columns:1fr}}
.hero-greet{font-size:23px;font-weight:800;letter-spacing:-.01em;text-shadow:0 1px 12px rgba(8,70,84,.30)}
.hero-quote{font-size:13.5px;color:#fffaef;margin-top:6px;display:flex;align-items:center;gap:8px;text-shadow:0 1px 9px rgba(8,70,84,.34)}
.hero-cd{background:rgba(247,107,107,.16);border:1px solid rgba(247,107,107,.36);border-radius:14px;padding:16px 22px;text-align:center;min-width:150px}
.hero-cd-n{font-size:34px;font-weight:800;color:#f2dcae;line-height:1}
.hero-cd-l{font-size:11.5px;color:#f1e4c4;margin-top:5px;font-weight:600}
.hero-cd-d{font-size:11px;color:#cbb98e;margin-top:2px}

/* STATS */
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:16px;margin-bottom:22px}
.stat{background:#ffffff;border:1px solid var(--line);border-radius:13px;padding:18px;box-shadow:0 1px 3px rgba(20,120,140,.05)}
.stat-ic{width:40px;height:40px;border-radius:10px;display:grid;place-items:center;margin-bottom:13px}
.stat-n{font-size:26px;font-weight:800;line-height:1;letter-spacing:-.02em}
.stat-l{font-size:12.5px;color:var(--muted);margin-top:6px;font-weight:600}
.stat-sub{font-size:11.5px;color:#aa9a7a;margin-top:3px;display:flex;align-items:center;gap:4px}

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
.test-card{background:#ffffff;border:1px solid var(--line);border-radius:14px;padding:18px;box-shadow:0 1px 3px rgba(20,120,140,.05);display:flex;flex-direction:column;gap:12px;transition:.15s}
.test-card:hover{box-shadow:0 6px 20px rgba(20,120,140,.1);transform:translateY(-2px)}
.test-top{display:flex;justify-content:space-between;align-items:flex-start;gap:10px}
.test-title{font-size:15.5px;font-weight:800;color:#2e1c12;line-height:1.25}
.test-series{font-size:12px;color:var(--muted);margin-top:3px}
.test-meta{display:flex;gap:16px;font-size:12.5px;color:#7a6450;font-weight:600}
.test-meta span{display:flex;align-items:center;gap:5px}
.test-score{display:flex;align-items:center;gap:14px;padding:12px;background:#fffaef;border-radius:10px;border:1px solid #fdf6e3}
.test-score-n{font-size:22px;font-weight:800;line-height:1}
.test-score-l{font-size:11px;color:var(--muted);font-weight:600;margin-top:3px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:7px;font-size:13.5px;font-weight:700;padding:11px 16px;border-radius:9px;transition:.14s;border:1.5px solid transparent;width:100%}
.btn-primary{background:linear-gradient(135deg,#8a2222,#6b1a1a);color:#ffffff;box-shadow:0 5px 16px rgba(20,150,180,.38)}
.btn-primary:hover{background:linear-gradient(135deg,#c8a24a,#a8842f);box-shadow:0 8px 22px rgba(20,150,180,.48)}
.btn-gold{background:var(--gold-2);color:#ffffff}
.btn-gold:hover{filter:brightness(.94)}
.btn-ghost{background:#ffffff;border-color:#e6d6b2;color:#5c4636}
.btn-ghost:hover{border-color:#d8c79c;background:#fdf6e3}
.btn-sm{padding:8px 13px;font-size:12.5px;width:auto}
.tabs{display:flex;gap:8px;margin-bottom:18px;flex-wrap:wrap}
.tab{font-size:13px;font-weight:700;padding:9px 16px;border-radius:20px;border:1.5px solid #e6dcc4;color:#5c4636;background:#ffffff;transition:.13s}
.tab.active{background:var(--navy);border-color:var(--navy);color:#ffffff}
.tab:hover:not(.active){border-color:#d8c79c}

/* PERFORMANCE */
.panel-title{font-size:16px;font-weight:800;margin:5px 0 2px;letter-spacing:-.01em}
.panel-note{font-size:12.5px;color:var(--muted);margin:0 0 16px}
.topic-row{display:flex;align-items:center;gap:12px;margin-bottom:11px}
.topic-name{font-size:13px;font-weight:600;width:160px;flex:0 0 auto;color:#4a3322;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.topic-track{flex:1;height:9px;background:#fdf6e3;border-radius:6px;overflow:hidden}
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
.batch-card{background:#ffffff;border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:0 1px 3px rgba(20,120,140,.05);transition:.18s}
.batch-card:hover{transform:translateY(-3px);box-shadow:0 12px 28px rgba(58,14,14,.1);border-color:#e8d6ae}
.batch-card.expired{opacity:.75}
.batch-bar{height:5px}
.batch-body{padding:20px}
.batch-name{font-size:16px;font-weight:800;color:#2e1c12}
.batch-exam{font-size:12.5px;color:var(--muted);margin-top:3px}
.batch-tag{font-size:11px;font-weight:800;padding:4px 9px;border-radius:7px;white-space:nowrap;flex:0 0 auto;text-transform:uppercase;letter-spacing:.03em}
.batch-tag.expired{background:#f1e6d8;color:#8a7860}
.batch-tag.urgent{background:#fbeaea;color:#c0392b}
.progress{height:9px;background:#fdf6e3;border-radius:6px;overflow:hidden;margin:14px 0 7px}
.progress-fill{height:100%;border-radius:6px}

/* LEADERBOARD */
.lb-you{background:radial-gradient(ellipse 55% 50% at 16% 4%, rgba(255,255,255,.55), transparent 72%),radial-gradient(ellipse 46% 42% at 83% 2%, rgba(255,255,255,.40), transparent 72%),linear-gradient(135deg,#8a2222,#b8923a);border-radius:16px;color:#ffffff;padding:22px 26px;display:grid;grid-template-columns:auto 1fr auto auto;gap:22px;align-items:center;box-shadow:0 14px 36px rgba(18,140,170,.24);margin-bottom:20px}
@media(max-width:700px){.lb-you{grid-template-columns:1fr;text-align:center;gap:14px}}
.lb-share{display:flex;align-items:center;gap:7px;background:rgba(255,255,255,.16);border:1.5px solid rgba(255,255,255,.35);
  color:#fff;font-weight:700;font-size:13px;padding:10px 16px;border-radius:10px;transition:.15s;backdrop-filter:blur(4px)}
.lb-share:hover{background:rgba(255,255,255,.26);transform:translateY(-1px)}
.lb-search{display:flex;align-items:center;gap:8px;background:#fdf6e3;border:1.5px solid #eee0c0;border-radius:10px;
  padding:8px 12px;color:#bcae94;min-width:200px}
.sort-select{background:#fdf6e3;border:1.5px solid #eee0c0;border-radius:10px;padding:9px 12px;font-size:13px;font-weight:600;color:#5c4636;cursor:pointer;font-family:inherit}
.lb-search input{border:none;background:none;outline:none;font-size:13px;color:#4a3322;width:100%;font-family:inherit}
.lb-row.top3{background:linear-gradient(90deg, rgba(220,168,74,.08), transparent)}
.lb-row.top3 .lb-av,.lb-row.top3 .prof-av{box-shadow:0 0 0 2px #f4cf86}
.lb-rank-big{font-size:40px;font-weight:800;line-height:1;color:#f2dcae}
.lb-row{display:flex;align-items:center;gap:14px;padding:14px 18px;border-bottom:1px solid #fdf6e3}
.lb-row:last-child{border-bottom:none}
.lb-row.me{background:#fcf3df}
.lb-pos{width:34px;font-weight:800;font-size:15px;text-align:center;flex:0 0 auto}
.lb-av{width:38px;height:38px;border-radius:10px;display:grid;place-items:center;font-weight:800;font-size:13px;color:#ffffff;flex:0 0 auto}
.lb-name{flex:1;font-weight:700;font-size:14px;color:#2e1c12}
.lb-move{display:flex;align-items:center;gap:3px;font-size:12px;font-weight:700}
.lb-score{font-weight:800;font-size:15px;width:60px;text-align:right;flex:0 0 auto}

/* ACHIEVEMENTS */
.ach-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:14px}
.ach{border:1px solid var(--line);border-radius:13px;padding:18px;text-align:center;background:#ffffff;transition:.14s}
.ach.earned{border-color:#f4e0b8;background:linear-gradient(180deg,#fdf6e8,#ffffff)}
.ach.locked{opacity:.55}
.ach-ic{width:50px;height:50px;border-radius:14px;display:grid;place-items:center;margin:0 auto 12px}
.ach-t{font-size:14px;font-weight:800;color:#2e1c12}
.ach-d{font-size:11.5px;color:var(--muted);margin-top:4px;line-height:1.4}

/* MATERIALS */
.mat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px}
.mat-card{display:flex;gap:14px;align-items:center;background:#ffffff;border:1px solid var(--line);border-radius:13px;padding:16px;box-shadow:0 1px 3px rgba(20,120,140,.05);transition:.16s}
.mat-card:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(58,14,14,.1);border-color:#e8d6ae}
.mat-ic{width:46px;height:46px;border-radius:11px;display:grid;place-items:center;flex:0 0 auto}
.mat-t{font-size:14px;font-weight:700;color:#2e1c12;line-height:1.3}
.mat-sub{font-size:12px;color:var(--muted);margin-top:3px}
.mat-subj-tag{font-weight:600}
.btn-locked{background:#f6ecd2;color:#8a6a2a;border:1.5px solid #e8d29a}
.btn-locked:hover{background:#efe0b8}

/* PROFILE */
.prof-head{display:flex;align-items:center;gap:20px;flex-wrap:wrap}
.prof-av{width:78px;height:78px;border-radius:18px;background:linear-gradient(140deg,#cda74f,#b8923a);color:#ffffff;display:grid;place-items:center;font-size:28px;font-weight:800;flex:0 0 auto}
.prof-av-wrap{position:relative;flex:0 0 auto}
.prof-av-edit{position:absolute;bottom:-6px;right:-6px;width:28px;height:28px;border-radius:50%;background:#5b1414;color:#fff;
  display:grid;place-items:center;box-shadow:0 3px 10px rgba(58,14,14,.35);border:2px solid #fff;transition:.15s}
.prof-av-edit:hover{background:#8a2222;transform:scale(1.08)}
.prof-av-remove{background:none;border:none;padding:0;font-size:12px;font-weight:700;color:#c0392b;margin-top:6px;cursor:pointer;text-decoration:underline}
.prof-name{font-size:22px;font-weight:800;letter-spacing:-.01em}
.prof-meta{font-size:13px;color:var(--muted);margin-top:4px}
.field{margin-bottom:16px}
.field label{display:block;font-size:12.5px;font-weight:700;color:#4a3322;margin-bottom:6px}
/* background and font-family must be stated. Without them a <textarea> keeps
   the browser's own form-control defaults — monospace, and a dark canvas under
   a dark colour-scheme — which put dark text on a near-black box while every
   input beside it stayed cream. */
.inp{width:100%;padding:11px 13px;border:1.5px solid #e6d6b2;border-radius:9px;font-size:14px;
  color:var(--ink);outline:none;background:var(--card);font-family:inherit;line-height:1.55}
.inp::placeholder{color:var(--muted);opacity:1}
textarea.inp{resize:vertical;min-height:88px}
.inp:focus{border-color:var(--navy);box-shadow:0 0 0 3px rgba(20,150,180,.1)}
.toggle-row{display:flex;align-items:center;justify-content:space-between;padding:13px 0;border-bottom:1px solid #fdf6e3}
.toggle-row:last-child{border-bottom:none}
.switch{width:44px;height:25px;border-radius:20px;background:#d6cbb0;position:relative;transition:.18s;flex:0 0 auto}
.switch.on{background:var(--green)}
.switch::after{content:"";position:absolute;top:3px;left:3px;width:19px;height:19px;border-radius:50%;background:#ffffff;transition:.18s;box-shadow:0 1px 3px rgba(0,0,0,.2)}
.switch.on::after{left:22px}

/* MODAL */
.overlay{position:fixed;inset:0;background:rgba(13,27,42,.55);display:flex;align-items:flex-start;justify-content:center;z-index:60;padding:30px 18px;overflow-y:auto;backdrop-filter:blur(2px)}
.modal{background:#ffffff;border-radius:16px;width:100%;max-width:640px;box-shadow:0 24px 60px rgba(0,0,0,.3);margin:auto}
.modal-head{display:flex;align-items:center;justify-content:space-between;padding:20px 24px;border-bottom:1px solid var(--line)}
.modal-head h3{margin:0;font-size:17px;font-weight:800}
.modal-head .x{width:34px;height:34px;border-radius:8px;display:grid;place-items:center;color:#9c8c70}
.modal-head .x:hover{background:#f7efdd;color:var(--ink)}
.modal-body{padding:22px 24px}
.modal-foot{padding:16px 24px;display:flex;gap:11px;justify-content:flex-end;border-top:1px solid var(--line);background:#fffaef;border-radius:0 0 16px 16px}

/* TOAST */
.toasts{position:fixed;bottom:22px;right:22px;display:flex;flex-direction:column;gap:10px;z-index:90}
.toast{display:flex;align-items:center;gap:10px;background:var(--ink);color:#ffffff;font-size:13.5px;font-weight:600;padding:12px 16px;border-radius:11px;box-shadow:0 10px 30px rgba(0,0,0,.25)}
.toast svg{color:#7fe0a3;flex:0 0 auto}

.empty{text-align:center;padding:44px 20px;color:var(--muted)}
.empty-ic{width:54px;height:54px;border-radius:14px;background:#fdf6e3;display:grid;place-items:center;margin:0 auto 14px;color:#bcae94}
.loader{display:grid;place-items:center;min-height:100vh;width:100%;color:var(--muted);font-size:14px}

.rf-wallet{display:grid;grid-template-columns:1.1fr 1fr;gap:0;border:1px solid var(--line);
  border-radius:16px;overflow:hidden;background:var(--card);margin-bottom:20px}
.rf-wal-main{padding:24px;background:linear-gradient(140deg,#fdf8ec,#faf2dc)}
[data-theme="dark"] .rf-wal-main{background:linear-gradient(140deg,#241a12,#1c150f)}
.rf-wal-label{font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:800}
.rf-wal-amt{font-size:38px;font-weight:800;color:var(--ink);line-height:1.05;margin:7px 0 3px;
  display:flex;align-items:baseline;gap:3px}
.rf-wal-amt small{font-size:20px;font-weight:700}
.rf-wal-sub{font-size:12.5px;color:var(--muted)}
.rf-wal-side{padding:24px;display:flex;flex-direction:column;justify-content:center;gap:14px}
.rf-gate{display:flex;align-items:flex-start;gap:9px;font-size:12.5px;line-height:1.5}
.rf-gate .tick{width:18px;height:18px;border-radius:50%;flex:0 0 auto;display:grid;place-items:center;
  font-size:11px;font-weight:800;margin-top:1px}
.rf-gate.ok .tick{background:#e8f6ee;color:#1f8a4c}
.rf-gate.no .tick{background:#f6ecd2;color:#8a6a2a}
.rf-ledger-row{display:flex;align-items:center;gap:12px;padding:12px 0;border-bottom:1px solid var(--line)}
.rf-ledger-row:last-child{border-bottom:0}
.rf-ledger-row .amt{font-weight:800;font-size:14.5px;margin-left:auto;white-space:nowrap}
.rf-ledger-row .amt.rev{color:var(--muted);text-decoration:line-through}

/* FEEDBACK */
.fb-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:20px;align-items:start}
.fb-kinds{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:4px}
.fb-kind{padding:9px 15px;border-radius:100px;border:1.5px solid var(--line);background:var(--card);
  font:inherit;font-size:13px;font-weight:700;color:var(--muted);cursor:pointer;transition:.16s}
.fb-kind:hover{border-color:var(--gold-2,#b8923a)}
.fb-kind.on{background:#7a1f1f;border-color:#7a1f1f;color:#fff}
.fb-stars{display:flex;gap:5px}
.fb-star{background:none;border:0;padding:4px;cursor:pointer;color:#dccfae;transition:transform .14s,color .14s;
  line-height:0}
.fb-star:hover{transform:scale(1.14)}
.fb-star.on{color:#e0a92a}
.fb-note{font-size:12px;color:var(--muted);margin-top:6px;line-height:1.55}
.fb-item{border:1px solid var(--line);border-radius:13px;padding:15px 16px;margin-bottom:11px;
  background:var(--card)}
.fb-item-head{display:flex;align-items:center;gap:9px;margin-bottom:8px;flex-wrap:wrap}
.fb-msg{font-size:13.5px;line-height:1.6;color:var(--ink);margin:0}
.fb-reply{margin-top:11px;padding:11px 13px;border-radius:10px;background:#f3f8f4;border:1px solid #d8eadd;
  font-size:13px;line-height:1.6;color:#1f5c39}
.fb-reply b{display:block;font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;
  color:#2f9e58;margin-bottom:4px}
@media(max-width:860px){
  .fb-grid{grid-template-columns:1fr}
}

/* REFER & EARN */
.rf-hero{background:linear-gradient(150deg,#7a1f1f,#4e1114);color:#fdf6e3;border-radius:16px;
  padding:26px;position:relative;overflow:hidden}
.rf-hero::after{content:"";position:absolute;right:-50px;top:-50px;width:220px;height:220px;border-radius:50%;
  background:radial-gradient(circle,rgba(201,162,39,.34),transparent 70%);pointer-events:none}
.rf-hero-in{position:relative;z-index:2}
.rf-hero h3{margin:0 0 7px;font-size:19px;font-weight:800;display:flex;align-items:center;gap:9px}
.rf-hero p{margin:0;font-size:13.5px;color:#e6d8be;line-height:1.62;max-width:54ch}
.rf-code{display:inline-flex;align-items:center;gap:11px;margin:18px 0 13px;
  background:rgba(255,255,255,.1);border:1px dashed rgba(255,255,255,.42);border-radius:12px;
  padding:9px 17px;font-size:21px;font-weight:800;letter-spacing:.17em}
.rf-linkrow{display:flex;gap:9px;flex-wrap:wrap}
.rf-linkbox{flex:1 1 250px;min-width:0;background:rgba(255,255,255,.95);color:#4a3524;border:0;
  border-radius:10px;padding:0 14px;height:42px;font:inherit;font-size:13px;font-weight:600;
  text-overflow:ellipsis;overflow:hidden;white-space:nowrap}
.rf-act{display:inline-flex;align-items:center;justify-content:center;gap:7px;height:42px;padding:0 16px;
  border-radius:10px;font:inherit;font-size:13px;font-weight:700;border:0;cursor:pointer;transition:.15s;flex:0 0 auto}
.rf-act-gold{background:var(--gold-2,#b8923a);color:#fff}
.rf-act-gold:hover{filter:brightness(1.08)}
.rf-act-line{background:rgba(255,255,255,.12);color:#fdf6e3;border:1.5px solid rgba(255,255,255,.34)}
.rf-act-line:hover{background:rgba(255,255,255,.2)}
.rf-fine{margin-top:16px;font-size:11.5px;line-height:1.6;color:#cbb99c;max-width:62ch;position:relative;z-index:2}
.rf-steps{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:20px 0}
.rf-step{background:var(--card);border:1px solid var(--line);border-radius:13px;padding:17px}
.rf-step .n{width:26px;height:26px;border-radius:8px;background:#faf2dc;color:#8a6a2a;font-size:12.5px;
  font-weight:800;display:grid;place-items:center;margin-bottom:9px}
.rf-step b{display:block;font-size:13.5px;margin-bottom:4px}
.rf-step span{font-size:12.5px;color:var(--muted);line-height:1.55}
.rf-row{display:flex;align-items:center;gap:12px;padding:13px 0;border-bottom:1px solid var(--line)}
.rf-row:last-child{border-bottom:0}
.rf-row .who{flex:1;min-width:0}
.rf-row .who b{display:block;font-size:13.5px}
.rf-row .who span{font-size:12px;color:var(--muted)}

@media(max-width:860px){
  .sb{position:fixed;left:0;top:0;transform:translateX(-100%);transition:transform .22s;box-shadow:8px 0 30px rgba(0,0,0,.2)}
  .sb.open{transform:translateX(0)}
  .hamburger{display:flex}
  .content{padding:18px}
  .scrim{position:fixed;inset:0;background:rgba(0,0,0,.4);z-index:39}
  .rf-steps{grid-template-columns:1fr}
  .rf-wallet{grid-template-columns:1fr}
  .rf-wal-main,.rf-wal-side{padding:20px}
  .rf-hero{padding:20px}
  .rf-code{font-size:18px;letter-spacing:.13em}
  .rf-act{flex:1 1 auto}
}

/* ---------- MOBILE ----------
   The stat cards fell to a single column on a phone and four numbers then
   took 720px of scrolling. The cause was arithmetic, not intent:
   minmax(170px,1fr) with a 16px gap needs 356px and the container is 323px,
   so auto-fit dropped to one track by two pixels a side. Stated as two
   columns explicitly, with the padding brought in to match. */
@media(max-width:560px){
  .stats{grid-template-columns:1fr 1fr;gap:11px;margin-bottom:16px}
  .stats > *{padding:14px 13px}
  .stat-n,.stats .n{font-size:26px}
  .card-pad{padding:17px}
  .sec-head{margin-bottom:13px}
  .sec-head h2{font-size:15px}
}
`;

/* ============================================================
   SMALL COMPONENTS
   ============================================================ */
function Ring({ value, size = 150, stroke = 13, color, children, track = "#fdf6e3" }) {
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
function StatCard({ icon, color, n, label, sub, subColor }) {
  return (
    <div className="stat">
      <div className="stat-ic" style={{ background: color.bg, color: color.fg }}>{icon}</div>
      <div className="stat-n">{n}</div>
      <div className="stat-l">{label}</div>
      {sub && <div className="stat-sub" style={subColor ? { color: subColor, fontWeight: 700 } : undefined}>{sub}</div>}
    </div>
  );
}
function Badge({ color, children }) { return <span className="badge" style={{ background: color.bg, color: color.fg }}>{children}</span>; }
function Avatar({ name, bg = "#b8923a", cls = "lb-av" }) {
  return <span className={cls} style={{ background: bg }}>{name.split(" ").map((w) => w[0]).slice(0, 2).join("")}</span>;
}
function heatColor(c) { return ["#fdf6e3", "#cfe7d8", "#86cfa0", "#3fa86a", "#1f8a4c"][c]; }
const TYPE_ICON = { pdf: { ic: <FileText size={22} />, c: { bg: "#fbeaea", fg: "#c0392b" } }, note: { ic: <BookOpen size={22} />, c: { bg: "#faf2dc", fg: "#b8923a" } }, video: { ic: <Play size={22} />, c: { bg: "#f6ecd2", fg: "#7a1f1f" } } };

/* ============================================================
   ATTEMPT ANALYSIS MODAL
   ============================================================ */
/**
 * The per-question solutions for one past attempt (§7: the review is reachable
 * later, not only right after submitting). Renders the shared ReviewCard from
 * the attempt's stored review rows, so it matches the post-test result screen.
 */
function SolutionsSection({ review }) {
  const { t } = useLang();
  const [show, setShow] = useState(false);
  if (!Array.isArray(review) || review.length === 0) return null;
  return (
    <div style={{ marginTop: 16 }}>
      <button className="btn btn-ghost btn-sm" onClick={() => setShow((s) => !s)}>
        <Eye size={15} />{show ? t("sd_hide_sol") : t("sd_view_sol")}
      </button>
      {show && (
        <div style={{ marginTop: 12 }}>
          <ReviewStyles />
          {review.map((r, i) => <ReviewCard key={r.id ?? i} r={r} />)}
        </div>
      )}
    </div>
  );
}

/**
 * My-Performance drill-down (§7): every question the student got wrong in one
 * subject, across all attempts, in the same ReviewCard the result screen uses —
 * filtered instead of scoped to one test. Data comes from the my_review RPC.
 */
function SubjectDrilldown({ subject, onClose }) {
  const { t } = useLang();
  const [rows, setRows] = useState(null);
  const [err, setErr] = useState("");
  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const r = await DB.myReview(subject, { wrongOnly: true });
        if (alive) setRows(r);
      } catch (e) { if (alive) setErr(e?.message || "Could not load your review."); }
    })();
    return () => { alive = false; };
  }, [subject]);

  return (
    <div className="overlay" onClick={onClose}>
      <div className="modal" onClick={(e) => e.stopPropagation()} style={{ maxWidth: 720 }}>
        <div className="modal-head"><h3>{subject} — {t("sd_mistakes")}</h3><button className="x" onClick={onClose}><X size={19} /></button></div>
        <div className="modal-body">
          <ReviewStyles />
          {err && <div style={{ color: "var(--red)", fontSize: 13, marginBottom: 10 }}>{err}</div>}
          {rows === null && !err && <p style={{ fontSize: 13, color: "var(--muted)" }}>{t("sd_loading")}</p>}
          {rows !== null && rows.length === 0 && (
            <EmptyState compact icon={<CheckCircle2 size={24} />} title={t("sd_no_mistakes")} text={t("sd_no_mistakes_sub")} />
          )}
          {rows && rows.map((r, i) => <ReviewCard key={r.responseId ?? i} r={r} defaultOpen={rows.length <= 3} />)}
        </div>
        <div className="modal-foot"><button className="btn btn-ghost btn-sm" onClick={onClose}>{t("sd_close")}</button></div>
      </div>
    </div>
  );
}

function AnalysisModal({ a, onClose, onRetake }) {
  const { t } = useLang();
  const pct = a.scorePct ?? (a.maxScore > 0 ? (a.score / a.maxScore) * 100 : 0);
  const grade = gradeFor(pct);
  const weak = (a.topics || []).filter((t) => t.band === "weak");
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
                <Mini n={a.percentile != null ? a.percentile : "—"} l="Percentile" c="var(--gold-2)" />
                <Mini n={a.rank != null ? "#" + a.rank : "—"} l={a.totalStudents ? "of " + a.totalStudents : "not ranked yet"} c="var(--navy)" />
                <Mini n={a.accuracy.toFixed(0) + "%"} l="Accuracy" c="var(--green)" />
                <Mini n={fmtDuration(a.timeSec)} l="Time taken" c="var(--blue)" />
              </div>
            </div>
          </div>

          <div style={{ display: "flex", gap: 10, marginBottom: 18 }}>
            <SmallStat n={a.correct} l="Correct" c="var(--green)" bg="var(--grn-bg)" />
            <SmallStat n={a.wrong} l="Wrong" c="var(--red)" bg="var(--red-bg)" />
            <SmallStat n={a.skipped} l="Skipped" c="var(--muted)" bg="#f7efdd" />
          </div>

          <div className="eyebrow" style={{ marginBottom: 10 }}>{t("sd_secwise")}</div>
          {(a.sections || []).length === 0 && (
            <div style={{ fontSize: 13, color: "var(--muted)" }}>{t("sd_nosec")}</div>
          )}
          {(a.sections || []).map((s) => {
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

          {weak.length > 0 && (
            <div className="sw-box w" style={{ marginTop: 16 }}>
              <h4><Target size={15} style={{ color: SEM.weak }} />{t("sd_revise_first")}</h4>
              <p style={{ margin: 0, fontSize: 13, color: "var(--ink)", lineHeight: 1.55 }}>
                You lost the most marks in <b>{weak.map((t) => t.name).join(", ")}</b>. Go through those topics before your next attempt.
              </p>
            </div>
          )}

          <SolutionsSection review={a.review} />
        </div>
        <div className="modal-foot">
          <button className="btn btn-ghost btn-sm" onClick={onClose}>Close</button>
          {a.testId && onRetake && (
            <button className="btn btn-gold btn-sm" onClick={() => onRetake(a.testId)}><RotateCcw size={15} />{t("sd_reattempt")}</button>
          )}
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
function HomeView({ go, setAnalysis, onStart }) {
  const { t } = useLang();
  const { profile, attempts, tests, subjects, activity, derived, enrollments } = useData();
  const hr = new Date().getHours();
  const greet = t(hr < 12 ? "sd_morning" : hr < 17 ? "sd_afternoon" : "sd_evening");
  const quote = QUOTES[new Date().getDate() % QUOTES.length];
  const days = daysUntil(profile.targetDate);

  const recent = attempts.slice(-6);
  const trend = recent.map((a) => ({
    name: fmtDate(a.date),
    score: +a.scorePct.toFixed(0),
    pct: typeof a.percentile === "number" ? a.percentile : null,
  }));
  const last = attempts[attempts.length - 1];
  const strong = subjects.slice(0, 3);
  const weak = [...subjects].slice(-3).reverse();
  const available = tests.filter((t) => !t.attemptedByMe && !t.isUpcoming);
  const firstRun = attempts.length === 0;

  return (
    <div>
      <div className="hero">
        <div>
          <div className="hero-greet">{greet}, {(profile.name || t("sd_aspirant")).split(" ")[0]} 👋</div>
          <div className="hero-quote"><Sparkles size={15} style={{ color: "#f2dcae" }} />{t(quote)}</div>
        </div>
        {profile.targetDate && (
          <div className="hero-cd">
            <div className="hero-cd-n">{days}</div>
            <div className="hero-cd-l">{t("sd_days_target")}</div>
            <div className="hero-cd-d">{profile.target}</div>
          </div>
        )}
      </div>

      {firstRun ? (
        <div className="card card-pad mb" style={{ textAlign: "center", padding: "44px 24px" }}>
          <div style={{ width: 62, height: 62, borderRadius: 18, margin: "0 auto 16px", display: "grid", placeItems: "center", background: "linear-gradient(135deg,#ecca88,#dca84a)", color: "#fff" }}>
            <Play size={28} />
          </div>
          <div style={{ fontFamily: "var(--font-display)", fontSize: 21, color: "var(--ink)" }}>{t("sd_first_mock")}</div>
          <p style={{ fontSize: 14, color: "var(--muted)", maxWidth: 440, margin: "10px auto 20px", lineHeight: 1.7 }}>
            Everything on this dashboard — your trend line, subject map, rank and streak — is built from real attempts.
            Take one test and it all comes alive.
          </p>
          {available.length > 0 ? (
            <button className="btn btn-primary" style={{ width: "auto", display: "inline-flex" }} onClick={() => onStart(available[0].id)}>
              <Play size={16} />Start "{available[0].title}"
            </button>
          ) : (
            <div style={{ fontSize: 13.5, color: "var(--muted)" }}>
              No tests have been published yet. They'll appear here the moment your mentor adds one.
            </div>
          )}
        </div>
      ) : (
        <div className="stats">
          <StatCard icon={<FileText size={20} />} color={{ bg: "#faf2dc", fg: "#b8923a" }} n={derived.n} label={t("sd_tests_att")}
                    sub={t(derived.n === 1 ? "sd_just_start" : "sd_keep_going")} />
          <StatCard icon={<Target size={20} />} color={{ bg: "#e8f6ee", fg: "#1f8a4c" }} n={derived.avgScore.toFixed(0) + "%"} label={t("sd_avg_score")}
                    sub={derived.lastDelta === null ? t("sd_across_all")
                      : <>{derived.lastDelta >= 0 ? <ArrowUp size={12} /> : <ArrowDown size={12} />} {Math.abs(derived.lastDelta).toFixed(0)}% {t("sd_vs_last")}</>}
                    subColor={derived.lastDelta === null ? undefined : derived.lastDelta >= 0 ? "#1f8a4c" : "#c0392b"} />
          <StatCard icon={<Award size={20} />} color={{ bg: "#fcf3df", fg: "#d4a64a" }}
                    n={derived.bestPct != null ? derived.bestPct : "—"} label={t("sd_best_pct")}
                    sub={derived.bestPct != null && last ? t("sd_in_test").replace("{x}", last.title.slice(0, 18)) : t("sd_ranked_once")} />
          <StatCard icon={<Flame size={20} />} color={{ bg: "#fbeaea", fg: "#c0392b" }} n={derived.streak + " " + t(derived.streak === 1 ? "sd_day" : "sd_days")} label={t("sd_streak_l")}
                    sub={derived.streak === 0 ? t("sd_practise_today") : derived.activeDays + " " + t("sd_active_days")} />
        </div>
      )}

      {!firstRun && (
        <div className="grid2 mb">
          <div className="card card-pad">
            <div className="sec-head"><div><div className="eyebrow">{t("sd_trajectory")}</div><div className="panel-title">{t("sd_trend_l")}</div></div>
              <button className="btn btn-ghost btn-sm" onClick={() => go("performance")}>{t("sd_full_analytics")}<ChevronRight size={15} /></button></div>
            <div style={{ height: 230 }}>
              <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={trend} margin={{ top: 10, right: 8, left: -20, bottom: 0 }}>
                  <defs>
                    <linearGradient id="gScore" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stopColor="#b8923a" stopOpacity={0.28} /><stop offset="100%" stopColor="#b8923a" stopOpacity={0} /></linearGradient>
                  </defs>
                  <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="var(--line)" />
                  <XAxis dataKey="name" tick={{ fontSize: 11, fill: "var(--muted)" }} axisLine={false} tickLine={false} />
                  <YAxis domain={[0, 100]} tick={{ fontSize: 11, fill: "#bcae94" }} axisLine={false} tickLine={false} unit="%" />
                  <Tooltip contentStyle={{ borderRadius: 10, border: "1px solid var(--line)", fontSize: 13 }} />
                  <Area dataKey="score" name="Score %" stroke="#b8923a" strokeWidth={2.5} fill="url(#gScore)" />
                  <Line dataKey="pct" name="Percentile" stroke="#dca84a" strokeWidth={2.5} dot={{ r: 3, fill: "#dca84a" }} connectNulls />
                </AreaChart>
              </ResponsiveContainer>
            </div>
          </div>

          <div className="card card-pad">
            <div className="eyebrow">{t("sd_last_attempt")}</div>
            <div className="panel-title" style={{ marginBottom: 16 }}>{last ? last.title : "—"}</div>
            <div style={{ display: "flex", justifyContent: "center", marginBottom: 16 }}>
              <Ring value={last ? last.scorePct / 100 : 0} size={150} color={last ? gradeFor(last.scorePct).c : "#b8923a"}>
                <div style={{ fontSize: 28, fontWeight: 800 }}>{last ? last.score : 0}<span style={{ fontSize: 15, color: "var(--muted)" }}>/{last ? last.maxScore : 0}</span></div>
                <div style={{ fontSize: 12, color: "var(--muted)", fontWeight: 600 }}>{last ? t("sd_accuracy_of").replace("{n}", last.accuracy.toFixed(0)) : ""}</div>
              </Ring>
            </div>
            {last && <button className="btn btn-primary" onClick={() => setAnalysis(last)}><Eye size={16} />{t("sd_view_full")}</button>}
          </div>
        </div>
      )}

      <div className="grid2 mb">
        <div className="card card-pad">
          <div className="sec-head"><div><div className="eyebrow">{t("sd_pickup")}</div><div className="panel-title">{t("sd_available")}</div></div>
            <button className="btn btn-ghost btn-sm" onClick={() => go("tests")}>{t("sd_view_all")}<ChevronRight size={15} /></button></div>
          {available.length === 0 ? (
            <div style={{ padding: "26px 0", textAlign: "center", color: "var(--muted)", fontSize: 13.5 }}>
              {t(tests.length === 0 ? "sd_no_tests_yet" : "sd_all_attempted")}
            </div>
          ) : available.slice(0, 3).map((t) => (
            <div key={t.id} style={{ display: "flex", alignItems: "center", gap: 12, padding: "12px 0", borderBottom: "1px solid var(--line)" }}>
              <div style={{ width: 40, height: 40, borderRadius: 10, background: "#faf2dc", color: "#b8923a", display: "grid", placeItems: "center", flex: "0 0 auto" }}><FileText size={19} /></div>
              <div style={{ flex: 1, minWidth: 0 }}>
                <div style={{ fontSize: 14, fontWeight: 700, color: "var(--ink)", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>{t.title}</div>
                <div style={{ fontSize: 12, color: "var(--muted)", marginTop: 2 }}>{t.totalQuestions} Qs · {t.durationMin} min · {t.isFree ? "Free" : "Included"}</div>
              </div>
              <button className="btn btn-gold btn-sm" onClick={() => onStart(t.id)}><Play size={14} />Start</button>
            </div>
          ))}
        </div>

        <div className="card card-pad">
          <div className="sec-head"><div><div className="eyebrow">{t("sd_str_focus")}</div><div className="panel-title">{t("sd_where_stand")}</div></div></div>
          {subjects.length === 0 ? (
            <div style={{ padding: "26px 0", textAlign: "center", color: "var(--muted)", fontSize: 13.5 }}>
              Attempt a test and your subject-wise strengths appear here.
            </div>
          ) : (
            <div className="sw-grid">
              <div className="sw-box s">
                <h4><CheckCircle2 size={15} style={{ color: SEM.strong }} />{t("sd_strongest")}</h4>
                <div className="sw-list">{strong.map((s) => <div className="sw-item" key={s.name}><span>{s.name}</span><span style={{ color: SEM.strong }}>{s.acc}%</span></div>)}</div>
              </div>
              <div className="sw-box w">
                <h4><Target size={15} style={{ color: SEM.weak }} />{t("sd_needs_work")}</h4>
                <div className="sw-list">{weak.map((s) => <div className="sw-item" key={s.name}><span>{s.name}</span><span style={{ color: SEM.weak }}>{s.acc}%</span></div>)}</div>
              </div>
            </div>
          )}
        </div>
      </div>

      <div className="card card-pad mb">
        <div className="sec-head"><div><div className="eyebrow">{t("sd_last12")}</div><div className="panel-title">{t("sd_activity")}</div></div>
          <span style={{ fontSize: 13, color: "var(--muted)", fontWeight: 600 }}><Flame size={14} style={{ verticalAlign: -2, color: "var(--red)" }} /> {derived.streak} {t("sd_pf_streak")}</span></div>
        <div style={{ overflowX: "auto" }}>
          <div className="heat">{activity.map((d, i) => (
            <div key={i} className="heat-cell" style={{ background: heatColor(d.count) }}
                 title={fmtDate(d.date) + ": " + (d.count === 0 ? t("sd_no_activity") : t("sd_n_tests").replace("{n}", d.count))} />
          ))}</div>
        </div>
        <div className="heat-legend">{t("sd_less")} {[0, 1, 2, 3, 4].map((c) => <span key={c} className="heat-cell" style={{ background: heatColor(c) }} />)} {t("sd_more")}</div>
      </div>

      {enrollments.length > 0 && (
        <div className="card card-pad">
          <div className="eyebrow">{t("sd_your_access")}</div>
          <div className="panel-title" style={{ marginBottom: 10 }}>{t("sd_active_enrol")}</div>
          {enrollments.map((e) => (
            <div key={e.id} style={{ display: "flex", justifyContent: "space-between", alignItems: "center", padding: "10px 0", borderBottom: "1px solid var(--line)", flexWrap: "wrap", gap: 8 }}>
              <div>
                <div style={{ fontWeight: 700, color: "var(--ink)", fontSize: 14 }}>{e.batches?.name || e.plan_code || "Full access"}</div>
                <div style={{ fontSize: 12.5, color: "var(--muted)" }}>{t("sd_since").replace("{d}", fmtDate(e.enrolled_at))}</div>
              </div>
              <Badge color={{ bg: "#e8f6ee", fg: "#1f8a4c" }}>
                {e.expires_at ? t("sd_valid_till").replace("{d}", fmtDate(e.expires_at)) : t("sd_lifetime")}
              </Badge>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

/* ============================================================
   VIEW: TEST SERIES
   ============================================================ */
function TestsView({ setAnalysis, onStart, toast }) {
  const { t } = useLang();
  /* The rows below bind each test to a variable called t, which shadows the
     translate function; tr is the same function under a name they cannot hide. */
  const tr = t;
  const { tests, attempts, reminders, setReminders, profile } = useData();
  const [tab, setTab] = useState("available");
  const [q, setQ] = useState("");
  const [sort, setSort] = useState("date");

  const available = tests.filter((t) => !t.isUpcoming);
  const upcoming = tests.filter((t) => t.isUpcoming);
  const attempted = [...attempts].reverse();

  const needle = q.trim().toLowerCase();
  const matches = (t) => !needle || t.title.toLowerCase().includes(needle) || (t.seriesTitle || "").toLowerCase().includes(needle);
  const availableFiltered = available.filter(matches);
  const upcomingFiltered = upcoming.filter(matches);

  const sortedAttempted = [...attempted].sort((a, b) => {
    if (sort === "score") return b.scorePct - a.scorePct;
    if (sort === "rank") return (a.rank ?? 1e9) - (b.rank ?? 1e9);
    return new Date(b.date) - new Date(a.date);
  });

  const toggleReminder = async (t) => {
    const on = !reminders.has(t.id);
    const next = new Set(reminders);
    on ? next.add(t.id) : next.delete(t.id);
    setReminders(next);
    try {
      await DB.toggleReminder(profile.id, t.id, on);
      toast(on ? "🔔 We'll remind you before " + t.title : "Reminder removed");
    } catch (e) {
      console.error(e);
      setReminders(reminders); // roll back to what the server still believes
      toast("Couldn't save that reminder — try again");
    }
  };

  return (
    <div>
      <div className="sec-head" style={{ marginBottom: 4 }}>
        <div className="tabs">
          {[["available", tr("sd_tab_avail").replace("{n}", available.length)],
            ["upcoming", tr("sd_tab_upcoming").replace("{n}", upcoming.length)],
            ["attempted", tr("sd_tab_attempted").replace("{n}", attempted.length)]].map(([k, l]) => (
            <button key={k} className={"tab" + (tab === k ? " active" : "")} onClick={() => setTab(k)}>{l}</button>
          ))}
        </div>
        {tab !== "attempted" && <div className="lb-search" style={{ minWidth: 220 }}><Search size={15} /><input placeholder={t("sd_search_tests")} value={q} onChange={(e) => setQ(e.target.value)} /></div>}
        {tab === "attempted" && attempted.length > 1 && (
          <select className="sort-select" value={sort} onChange={(e) => setSort(e.target.value)}>
            <option value="date">{t("sd_sort_recent")}</option>
            <option value="score">{t("sd_sort_score")}</option>
            <option value="rank">{t("sd_sort_rank")}</option>
          </select>
        )}
      </div>

      {tab === "available" && (
        <div className="test-grid">
          {availableFiltered.length === 0 && (
            <div className="card card-pad" style={{ gridColumn: "1/-1", textAlign: "center", color: "var(--muted)", padding: "40px 20px" }}>
              {available.length === 0
                ? "No tests have been published yet. They will appear here as soon as your mentor adds one."
                : `No test matches "${q}".`}
            </div>
          )}
          {availableFiltered.map((t) => (
            <div className="test-card" key={t.id}>
              <div className="test-top">
                <div><div className="test-title">{t.title}</div><div className="test-series">{t.seriesTitle || tr("sd_standalone")}</div></div>
                <Badge color={t.attemptedByMe ? { bg: "#e8f6ee", fg: "#1f8a4c" } : t.isFree ? { bg: "#faf2dc", fg: "#b8923a" } : { bg: "#fcf3df", fg: "#d4a64a" }}>
                  {t.attemptedByMe ? tr("sd_done") : t.isFree ? tr("sd_free") : tr("sd_included")}
                </Badge>
              </div>
              <div className="test-meta"><span><Layers size={14} />{t.totalQuestions} Qs</span><span><Clock size={14} />{t.durationMin} min</span></div>
              <button className={"btn " + (t.attemptedByMe ? "btn-ghost" : "btn-primary")} onClick={() => onStart(t.id)}>
                {t.attemptedByMe ? <><RotateCcw size={16} />{tr("sd_reattempt")}</> : <><Play size={16} />{tr("sd_start_test")}</>}
              </button>
            </div>
          ))}
        </div>
      )}

      {tab === "upcoming" && (
        <div className="test-grid">
          {upcomingFiltered.length === 0 && (
            <div className="card card-pad" style={{ gridColumn: "1/-1", textAlign: "center", color: "var(--muted)", padding: "40px 20px" }}>
              {upcoming.length === 0 ? "Nothing scheduled right now." : `No test matches "${q}".`}
            </div>
          )}
          {upcomingFiltered.map((t) => (
            <div className="test-card" key={t.id}>
              <div className="test-top">
                <div><div className="test-title">{t.title}</div><div className="test-series">{t.seriesTitle || tr("sd_standalone")}</div></div>
                <Badge color={{ bg: "#faf2dc", fg: "#b8923a" }}><Calendar size={11} />{fmtDate(t.scheduledFor)}</Badge>
              </div>
              <div className="test-meta"><span><Layers size={14} />{t.totalQuestions} Qs</span><span><Clock size={14} />{t.durationMin} min</span></div>
              <button className={"btn btn-sm " + (reminders.has(t.id) ? "btn-primary" : "btn-ghost")} onClick={() => toggleReminder(t)}>
                {reminders.has(t.id) ? <><Check size={16} />{t("sd_rem_set")}</> : <><Bell size={16} />{t("sd_set_rem")}</>}
              </button>
            </div>
          ))}
        </div>
      )}

      {tab === "attempted" && (
        <div className="test-grid">
          {sortedAttempted.length === 0 && (
            <div className="card card-pad" style={{ gridColumn: "1/-1", textAlign: "center", color: "var(--muted)", padding: "40px 20px" }}>
              You haven't attempted a test yet. Your reports will collect here.
            </div>
          )}
          {sortedAttempted.map((a) => {
            const grade = gradeFor(a.scorePct);
            return (
              <div className="test-card" key={a.id}>
                <div className="test-top">
                  <div><div className="test-title">{a.title}</div><div className="test-series">{fmtDate(a.date)}{a.series ? " · " + a.series : ""}</div></div>
                  <Badge color={{ bg: "#fdf6e3", fg: grade.c }}>Grade {grade.g}</Badge>
                </div>
                <div className="test-score">
                  <div><div className="test-score-n" style={{ color: grade.c }}>{a.score}<span style={{ fontSize: 14, color: "var(--muted)" }}>/{a.maxScore}</span></div><div className="test-score-l">Score</div></div>
                  <div style={{ width: 1, alignSelf: "stretch", background: "var(--line)" }} />
                  <div><div className="test-score-n" style={{ color: "var(--gold-2)" }}>{a.accuracy.toFixed(0)}%</div><div className="test-score-l">Accuracy</div></div>
                  <div style={{ width: 1, alignSelf: "stretch", background: "var(--line)" }} />
                  <div><div className="test-score-n">{a.rank ? "#" + a.rank : "—"}</div><div className="test-score-l">Rank</div></div>
                </div>
                <button className="btn btn-ghost" onClick={() => setAnalysis(a)}><Eye size={16} />{t("sd_view_anal")}</button>
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
function PerformanceView({ go }) {
  const { t } = useLang();
  const { attempts, subjects, derived, peer } = useData();
  const [drill, setDrill] = useState(null);

  if (attempts.length === 0) {
    return (
      <div className="card card-pad">
        <EmptyState
          icon={<BarChart3 size={26} />}
          title={t("sd_no_anal")}
          text="Analytics are built entirely from your own attempts — nothing here is simulated. Take a test and this page fills in."
          action={<button className="btn btn-primary" style={{ width: "auto", display: "inline-flex" }} onClick={() => go("tests")}><Play size={16} />Browse tests</button>}
        />
      </div>
    );
  }

  const trend = attempts.map((a) => ({
    name: fmtDate(a.date),
    score: +a.scorePct.toFixed(0),
    pct: typeof a.percentile === "number" ? a.percentile : null,
    acc: +a.accuracy.toFixed(0),
    tpq: a.totalQ > 0 ? +(a.timeSec / a.totalQ).toFixed(0) : 0,
  }));
  const radar = subjects.map((s) => ({ topic: s.name.length > 12 ? s.name.slice(0, 11) + "…" : s.name, You: s.acc }));
  const weakest = subjects.filter((s) => s.band === "weak").map((s) => s.name);
  const first = attempts[0];

  const cmp = peer
    ? [{ name: "You", value: +derived.avgScore.toFixed(0), fill: "#b8923a" },
       { name: t("sd_batch_avg"), value: Math.round(peer.avgPct), fill: "#b0a080" },
       { name: t("sd_topper"), value: Math.round(peer.bestPct), fill: "#dca84a" }]
    : null;

  return (
    <div>
      <div className="stats">
        <StatCard icon={<FileText size={20} />} color={{ bg: "#faf2dc", fg: "#b8923a" }} n={derived.n} label={t("sd_tests_taken")} />
        <StatCard icon={<Target size={20} />} color={{ bg: "#e8f6ee", fg: "#1f8a4c" }} n={derived.avgScore.toFixed(0) + "%"} label={t("sd_avg_score_s")}
                  sub={derived.lastDelta === null ? t("sd_best_n") + " " + derived.bestScore.toFixed(0) + "%" : (derived.lastDelta >= 0 ? "↑ " : "↓ ") + Math.abs(derived.lastDelta).toFixed(0) + "% " + t("sd_vs_last")}
                  subColor={derived.lastDelta !== null ? (derived.lastDelta >= 0 ? "#1f8a4c" : "#c0392b") : undefined} />
        <StatCard icon={<Award size={20} />} color={{ bg: "#fcf3df", fg: "#d4a64a" }} n={derived.bestPct ?? "—"} label={t("sd_best_pct")} />
        <StatCard icon={<CheckCircle2 size={20} />} color={{ bg: "#f6ecd2", fg: "#7a1f1f" }} n={derived.avgAcc.toFixed(0) + "%"} label={t("sd_avg_acc")} />
        <StatCard icon={<Clock size={20} />} color={{ bg: "#fbeaea", fg: "#c0392b" }} n={fmtDuration(derived.totalTime)} label={t("sd_total_time")} />
      </div>

      <div className="card card-pad mb">
        <div className="eyebrow">{t("sd_trajectory")}</div>
        <div className="panel-title">{t("sd_trend_time")}</div>
        <p className="panel-note">{t("sd_every_attempt")}</p>
        <div style={{ height: 280 }}>
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart data={trend} margin={{ top: 10, right: 10, left: -18, bottom: 0 }}>
              <defs><linearGradient id="g2" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stopColor="#b8923a" stopOpacity={0.25} /><stop offset="100%" stopColor="#b8923a" stopOpacity={0} /></linearGradient></defs>
              <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="var(--line)" />
              <XAxis dataKey="name" tick={{ fontSize: 11, fill: "var(--muted)" }} axisLine={false} tickLine={false} />
              <YAxis domain={[0, 100]} tick={{ fontSize: 11, fill: "#bcae94" }} axisLine={false} tickLine={false} unit="%" />
              <Tooltip contentStyle={{ borderRadius: 10, border: "1px solid var(--line)", fontSize: 13 }} />
              <Area dataKey="score" name="Score %" stroke="#b8923a" strokeWidth={2.5} fill="url(#g2)" />
              <Line dataKey="pct" name="Percentile" stroke="#dca84a" strokeWidth={2.5} dot={{ r: 3, fill: "#dca84a" }} connectNulls />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="grid2b mb">
        <div className="card card-pad">
          <div className="eyebrow">{t("sd_diagnosis")}</div>
          <div className="panel-title">{t("sd_subj_map")}</div>
          <p className="panel-note">{t("sd_subj_sub")}</p>
          {subjects.length < 3 ? (
            <EmptyState compact icon={<Target size={24} />} title={t("sd_not_enough")}
                        text="Attempt a full-length test covering several subjects to see this map." />
          ) : (
            <div style={{ height: 270 }}>
              <ResponsiveContainer width="100%" height="100%">
                <RadarChart data={radar} outerRadius="72%">
                  <PolarGrid stroke="#eae0c8" />
                  <PolarAngleAxis dataKey="topic" tick={{ fontSize: 10.5, fill: "var(--muted)" }} />
                  <PolarRadiusAxis domain={[0, 100]} tick={{ fontSize: 9, fill: "#cfc3a4" }} axisLine={false} />
                  <Radar dataKey="You" stroke="#b8923a" fill="#b8923a" fillOpacity={0.28} strokeWidth={2} />
                  <Tooltip formatter={(v) => [v + "%", "Accuracy"]} contentStyle={{ borderRadius: 10, border: "1px solid var(--line)", fontSize: 13 }} />
                </RadarChart>
              </ResponsiveContainer>
            </div>
          )}
        </div>

        <div className="card card-pad">
          <div className="eyebrow">{t("sd_benchmark")}</div>
          <div className="panel-title">{t("sd_vs")}</div>
          <p className="panel-note">
            {t(cmp ? "sd_avg_vs_all" : "sd_cmp_locked")}
          </p>
          {!cmp ? (
            <EmptyState compact icon={<Trophy size={24} />} title={t("sd_ahead")}
                        text={t("sd_ahead_d")} />
          ) : (
            <div style={{ height: 270 }}>
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={cmp} margin={{ top: 16, right: 8, left: -18, bottom: 0 }}>
                  <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="var(--line)" />
                  <XAxis dataKey="name" tick={{ fontSize: 12, fill: "var(--muted)" }} axisLine={false} tickLine={false} />
                  <YAxis domain={[0, 100]} tick={{ fontSize: 11, fill: "#bcae94" }} axisLine={false} tickLine={false} unit="%" />
                  <Tooltip cursor={{ fill: "rgba(20,150,180,.04)" }} formatter={(v) => [v + "%", "Score"]} contentStyle={{ borderRadius: 10, border: "1px solid var(--line)", fontSize: 13 }} />
                  <Bar dataKey="value" radius={[7, 7, 0, 0]} maxBarSize={64}>
                    {cmp.map((e, i) => <Cell key={i} fill={e.fill} />)}
                    <LabelList dataKey="value" position="top" formatter={(v) => v + "%"} style={{ fontSize: 12, fontWeight: 800, fill: "#4a3322" }} />
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            </div>
          )}
        </div>
      </div>

      <div className="grid2b mb">
        <div className="card card-pad">
          <div className="eyebrow">{t("sd_subjwise")}</div>
          <div className="panel-title">{t("sd_bands")}</div>
          <p className="panel-note" style={{ marginBottom: 18 }}>{t("sd_bands_sub")} {t("sd_tap_subject")}</p>
          {subjects.length === 0 ? (
            <EmptyState compact icon={<Layers size={24} />} title={t("sd_no_subj")} text="It appears after your first attempt." />
          ) : subjects.map((s) => {
            const col = SEM[s.band], bg = s.band === "strong" ? "var(--grn-bg)" : s.band === "average" ? "var(--amb-bg)" : "var(--red-bg)";
            return (
              <div className="topic-row drill" key={s.name} onClick={() => setDrill(s.name)} title={t("sd_view_sol")} style={{ cursor: "pointer" }}>
                <span className="topic-name">{s.name}</span>
                <div className="topic-track"><div className="topic-fill" style={{ width: s.acc + "%", background: col }} /></div>
                <span className="topic-band" style={{ background: bg, color: col }}>{t("ex_band_" + s.band)}</span>
                <ChevronRight size={15} style={{ color: "var(--muted)", flex: "0 0 auto" }} />
              </div>
            );
          })}
        </div>

        <div className="card card-pad">
          <div className="eyebrow">{t("sd_timemgmt")}</div>
          <div className="panel-title">{t("sd_avg_time_q")}</div>
          <p className="panel-note">{t("sd_trend_down")}</p>
          <div style={{ height: 250 }}>
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={trend} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="var(--line)" />
                <XAxis dataKey="name" tick={{ fontSize: 11, fill: "var(--muted)" }} axisLine={false} tickLine={false} />
                <YAxis tick={{ fontSize: 11, fill: "#bcae94" }} axisLine={false} tickLine={false} unit="s" />
                <Tooltip formatter={(v) => [v + "s", "Per question"]} contentStyle={{ borderRadius: 10, border: "1px solid var(--line)", fontSize: 13 }} />
                <Line dataKey="tpq" name="Time/Q" stroke="#c39d44" strokeWidth={2.5} dot={{ r: 3, fill: "#c39d44" }} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      <div className="card card-pad">
        <div className="eyebrow">{t("sd_action_plan")}</div>
        <div className="panel-title">{t("sd_focus_next")}</div>
        <p className="panel-note">{t("sd_plan_sub")}</p>
        <div className="sw-grid">
          <div className="sw-box w">
            <h4><Target size={15} style={{ color: SEM.weak }} />{t("sd_prio_subj")}</h4>
            <p style={{ margin: 0, fontSize: 13, color: "var(--ink)", lineHeight: 1.55 }}>
              {weakest.length === 0
                ? t("sd_no_weak")
                : <Pattern text={t("sd_weakest_d")} x={weakest.join(", ")} />}
            </p>
          </div>
          <div className="sw-box s">
            <h4><TrendingUp size={15} style={{ color: SEM.strong }} />{t("sd_momentum")}</h4>
            <p style={{ margin: 0, fontSize: 13, color: "var(--ink)", lineHeight: 1.55 }}>
              {attempts.length < 2
                ? <Pattern text={t("sd_one_point_d")} x={derived.bestScore.toFixed(0) + "%"} />
                : <Pattern text={t("sd_moved_d").replace("{p}", derived.bestPct != null ? t("sd_best_pct_is").replace("{p}", derived.bestPct) : "")}
                           x={first.scorePct.toFixed(0) + "%"} y={derived.bestScore.toFixed(0) + "%"} />}
            </p>
          </div>
        </div>
      </div>
      {drill && <SubjectDrilldown subject={drill} onClose={() => setDrill(null)} />}
    </div>
  );
}

/* ============================================================
   VIEW: BATCHES
   ============================================================ */
function BatchesView({ go, onStart, toast }) {
  const { t } = useLang();
  const { enrollments, tests, attempts } = useData();
  const now = new Date();
  const palette = ["#b8923a", "#7a1f1f", "#1a6b3c", "#a07c2a"];

  if (enrollments.length === 0) {
    return (
      <div className="card card-pad">
        <EmptyState
          icon={<GraduationCap size={26} />}
          title={t("sd_no_batch")}
          text="When you join a course or batch, it shows up here with its validity and how far through the test plan you are."
          action={<button className="btn btn-primary" style={{ width: "auto", display: "inline-flex" }} onClick={() => go("tests")}><FileText size={16} />{t("sd_see_avail")}</button>}
        />
      </div>
    );
  }

  const attemptedIds = new Set(attempts.map((a) => a.testId));

  return (
    <div className="test-grid">
      {enrollments.map((e, i) => {
        const name = e.batches?.name || (e.plan_code ? e.plan_code.replace(/-/g, " ") : "Full access");
        const exam = e.batches?.courses?.exam_target || e.batches?.courses?.title || t("sd_all_exams");
        const validTill = e.expires_at || e.batches?.end_date || null;
        const daysLeft = validTill ? Math.ceil((new Date(validTill) - now) / 86400000) : null;
        const expired = daysLeft !== null && daysLeft < 0;
        const urgent = daysLeft !== null && !expired && daysLeft <= 7;

        // Today a single plan unlocks the whole catalogue, so progress is
        // measured against every published test. When per-batch test scoping
        // lands, filter `tests` by `e.batch_id` here.
        const scope = tests;
        const total = scope.length;
        const done = scope.filter((t) => attemptedIds.has(t.id)).length;
        const p = total > 0 ? (done / total) * 100 : 0;
        const color = palette[i % palette.length];
        const next = scope.find((t) => !attemptedIds.has(t.id) && !t.isUpcoming);

        return (
          <div className={"batch-card" + (expired ? " expired" : "")} key={e.id}>
            <div className="batch-bar" style={{ background: expired ? "#b0a596" : color }} />
            <div className="batch-body">
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", gap: 8 }}>
                <div className="batch-name" style={{ textTransform: "capitalize" }}>{name}</div>
                {expired ? <span className="batch-tag expired">{t("sd_expired")}</span>
                  : urgent ? <span className="batch-tag urgent">{t("sd_days_left").replace("{n}", daysLeft)}</span> : null}
              </div>
              <div className="batch-exam">{exam} · {validTill ? t("sd_valid_till_l").replace("{d}", fmtDate(validTill)) : t("sd_lifetime_l")}</div>
              <div className="progress"><div className="progress-fill" style={{ width: p + "%", background: expired ? "#b0a596" : color }} /></div>
              <div style={{ display: "flex", justifyContent: "space-between", fontSize: 12.5, color: "var(--muted)", fontWeight: 600 }}>
                <span>{t("sd_tests_done").replace("{a}", done).replace("{b}", total)}</span><span>{p.toFixed(0)}%</span>
              </div>
              {expired ? (
                <button className="btn btn-locked" style={{ marginTop: 16 }} onClick={() => toast(t("sd_renew_msg"))}><Lock size={16} />{t("sd_renew")}</button>
              ) : next ? (
                <button className="btn btn-primary" style={{ marginTop: 16 }} onClick={() => onStart(next.id)}><Play size={16} />{t("sd_continue")} — {next.title.slice(0, 22)}</button>
              ) : (
                <button className="btn btn-ghost" style={{ marginTop: 16 }} onClick={() => go("performance")}><BarChart3 size={16} />{t("sd_all_done")}</button>
              )}
            </div>
          </div>
        );
      })}
    </div>
  );
}

/* ============================================================
   VIEW: STUDY MATERIAL
   ============================================================ */
function MaterialsView({ toast }) {
  const { t } = useLang();
  /* The filter tabs bind each type to a variable called t, shadowing the
     translate function; tr is the same function under a name they cannot hide. */
  const tr = t;
  const { materials } = useData();
  const [f, setF] = useState("all");
  const [q, setQ] = useState("");
  const types = ["all", "pdf", "note", "video", "link"];

  const needle = q.trim().toLowerCase();
  const filtered = materials.filter((m) =>
    (f === "all" || m.type === f)
    && (!needle || m.title.toLowerCase().includes(needle) || (m.subject || "").toLowerCase().includes(needle)));

  const openItem = (m) => {
    if (!m.url) { toast("This item has no file attached yet — we've told your mentor"); return; }
    // Row-level security already decides what a student can see; anything that
    // reaches this list is genuinely theirs to open.
    window.open(m.url, "_blank", "noopener,noreferrer");
  };

  return (
    <div>
      <div className="sec-head" style={{ marginBottom: 16 }}>
        <div className="tabs">{types.map((t) => (
          <button key={t} className={"tab" + (f === t ? " active" : "")} onClick={() => setF(t)}>{t === "all" ? tr("sd_mat_all") : tr("sd_type_" + t)}</button>
        ))}</div>
        <div className="lb-search" style={{ minWidth: 220 }}><Search size={15} /><input placeholder={t("sd_search_mat")} value={q} onChange={(e) => setQ(e.target.value)} /></div>
      </div>

      {materials.length === 0 ? (
        <div className="card card-pad">
          <EmptyState icon={<FolderOpen size={26} />} title={t("sd_no_mat")}
                      text="PDFs, notes and video links your mentor uploads will appear here." />
        </div>
      ) : filtered.length === 0 ? (
        <div className="card card-pad" style={{ textAlign: "center", color: "var(--muted)", fontSize: 13.5, padding: "40px 20px" }}>
          {q ? t("sd_no_mat_q").replace("{q}", q) : t("sd_no_mat_f").replace("{f}", t("sd_type_" + f))}
        </div>
      ) : (
        <div className="mat-grid">
          {filtered.map((m) => {
            const ti = TYPE_ICON[m.type] || TYPE_ICON.note;
            return (
              <div className="mat-card" key={m.id}>
                <div className="mat-ic" style={{ background: ti.c.bg, color: ti.c.fg }}>{ti.ic}</div>
                <div style={{ flex: 1, minWidth: 0 }}>
                  <div className="mat-t">{m.title}</div>
                  <div className="mat-sub">
                    {m.subject ? <><span className="mat-subj-tag">{m.subject}</span> · </> : null}
                    {m.isFree ? <span style={{ color: "var(--green)", fontWeight: 700 }}>{t("sd_free")}</span>
                              : <span style={{ color: "var(--gold-2)", fontWeight: 700 }}>{t("sd_included")}</span>}
                  </div>
                </div>
                <button className="btn btn-sm btn-ghost" onClick={() => openItem(m)} style={{ flex: "0 0 auto" }}>
                  {m.type === "video" ? <Play size={14} /> : <Eye size={14} />}{t("sd_open")}
                </button>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

/* ============================================================
   VIEW: LEADERBOARD
   ============================================================ */
function LeaderboardView({ toast }) {
  const { t } = useLang();
  const { profile, leaderboard, derived } = useData();
  const [q, setQ] = useState("");
  const colors = ["#dca84a", "#b0a080", "#b8923a"];

  const rows = leaderboard.map((r) => ({ ...r, you: r.student_id === profile.id }));
  const me = rows.find((r) => r.you);
  const needle = q.trim().toLowerCase();
  const filtered = needle ? rows.filter((r) => r.name.toLowerCase().includes(needle)) : rows;

  const share = async () => {
    if (!me) return;
    const text = `I'm ranked #${me.rank} of ${rows.length} on JUNOONIAS, preparing for ${profile.target}. 🪔`;
    try {
      if (navigator.share) await navigator.share({ text, title: "My JUNOONIAS rank" });
      else { await navigator.clipboard.writeText(text); toast("Rank copied — share it!"); }
    } catch { /* the user dismissed the share sheet */ }
  };

  if (rows.length === 0) {
    return (
      <div className="card card-pad">
        <EmptyState icon={<Trophy size={26} />} title={t("sd_board_empty")}
                    text="Rankings are computed from real attempts across all aspirants. Take a test and you'll be the first name on it." />
      </div>
    );
  }

  return (
    <div>
      {me ? (
        <div className="lb-you">
          <div style={{ textAlign: "center" }}>
            <div className="lb-rank-big">#{me.rank}</div>
            <div style={{ fontSize: 12, color: "#fffaef", marginTop: 4 }}>{t("sd_overall")}</div>
          </div>
          <div>
            <div style={{ fontSize: 18, fontWeight: 800 }}>
              {t(me.rank <= 3 ? "sd_podium" : me.rank <= 10 ? "sd_top10" : "sd_keep_climb")}
            </div>
            <div style={{ fontSize: 13.5, color: "#fffaef", marginTop: 4 }}>
              {t("sd_rank_line").replace("{r}", me.rank).replace("{n}", rows.length).replace("{p}", Math.max(1, Math.round((me.rank / rows.length) * 100))).replace("{c}", me.tests_taken)}
            </div>
          </div>
          <div style={{ textAlign: "center" }}>
            <div style={{ fontSize: 28, fontWeight: 800, color: "#f2dcae" }}>{Number(me.avg_pct).toFixed(0)}%</div>
            <div style={{ fontSize: 12, color: "#fffaef" }}>{t("sd_avg_score_l")}</div>
          </div>
          <button className="lb-share" onClick={share} title={t("sd_share_rank")}><Share2 size={15} />{t("sd_share")}</button>
        </div>
      ) : (
        <div className="card card-pad mb" style={{ textAlign: "center", color: "var(--muted)", fontSize: 13.5 }}>
          You're not on the board yet — attempt a test to be ranked. {derived.n > 0 ? "Your first result is still being scored." : ""}
        </div>
      )}

      <div className="card">
        <div className="sec-head" style={{ padding: "18px 20px 0" }}>
          <div><h2>{t("sd_top_perf")}</h2><div className="note">{t("sd_ranked_by")}</div></div>
          <div className="lb-search"><Search size={15} /><input placeholder={t("sd_find_asp")} value={q} onChange={(e) => setQ(e.target.value)} /></div>
        </div>
        <div style={{ marginTop: 14 }}>
          {filtered.length === 0 && <div style={{ padding: "30px 20px", textAlign: "center", color: "var(--muted)", fontSize: 13.5 }}>No aspirant matches "{q}"</div>}
          {filtered.map((r) => {
            const podium = !needle && r.rank <= 3;
            return (
              <div className={"lb-row" + (r.you ? " me" : "") + (podium ? " top3" : "")} key={r.student_id}>
                <div className="lb-pos" style={{ color: podium ? colors[r.rank - 1] : "var(--muted)" }}>
                  {podium ? <Medal size={18} style={{ color: colors[r.rank - 1] }} /> : r.rank}
                </div>
                {r.avatar_url
                  ? <span className="lb-av" style={{ backgroundImage: `url(${r.avatar_url})`, backgroundSize: "cover", backgroundPosition: "center" }} />
                  : <Avatar name={r.name} bg={r.you ? "#dca84a" : "#b8923a"} />}
                <div className="lb-name">
                  {r.name}{r.you && <span style={{ marginLeft: 8, fontSize: 11, color: "var(--gold-2)", fontWeight: 800 }}>YOU</span>}
                  <div style={{ fontSize: 11.5, color: "var(--muted)", fontWeight: 500 }}>{t("sd_tests_acc").replace("{n}", r.tests_taken).replace("{a}", Number(r.avg_accuracy ?? 0).toFixed(0))}</div>
                </div>
                <div className="lb-score">{Number(r.avg_pct).toFixed(0)}%</div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

/* ============================================================
   VIEW: PROFILE
   ============================================================ */
function ProfileView({ toast }) {
  const { t } = useLang();
  const { profile, setProfile, derived } = useData();
  const [form, setForm] = useState(profile);
  const [saving, setSaving] = useState(false);
  const [avatarErr, setAvatarErr] = useState("");
  const [uploadingPhoto, setUploadingPhoto] = useState(false);
  const fileRef = useRef(null);

  const achievements = achievementsFor(derived);
  const earned = achievements.filter((a) => a.earned).length;
  const notif = form.prefs?.notif || { email: true, sms: false, whatsapp: true };

  /* Every profile change is written to the database, not just to this tab. */
  const persist = async (patch, successMsg) => {
    const next = { ...form, ...patch };
    setForm(next);
    setProfile(next);
    try {
      await DB.updateProfile(profile.id, {
        full_name: next.name,
        target_exam: next.target,
        target_date: next.targetDate || null,
        city: next.city || null,
        avatar_url: next.avatarUrl || null,
        prefs: next.prefs || {},
      });
      if (successMsg) toast(successMsg);
      return true;
    } catch (e) {
      console.error(e);
      toast(t("sd_pf_savefail"));
      return false;
    }
  };

  const save = async () => {
    if (!form.name?.trim()) { toast(t("sd_pf_needname")); return; }
    setSaving(true);
    await persist({}, t("sd_pf_saved"));
    setSaving(false);
  };

  const toggleNotif = (key) => {
    const nextNotif = { ...notif, [key]: !notif[key] };
    persist({ prefs: { ...(form.prefs || {}), notif: nextNotif } });
  };

  /* The photo goes to storage and only its URL is stored on the profile row.
     It used to be inlined as a base-64 data URL, which meant every profile read
     dragged the whole image along with it. */
  const onPhoto = async (e) => {
    const file = e.target.files?.[0];
    e.target.value = ""; // let the same file be picked again after an error
    if (!file) return;
    setAvatarErr("");
    setUploadingPhoto(true);
    try {
      const url = await DB.uploadAvatar(profile.id, file);
      await persist({ avatarUrl: url }, t("sd_pf_photodone"));
    } catch (ex) {
      console.error(ex);
      setAvatarErr(ex?.message || t("sd_pf_photofail"));
    }
    setUploadingPhoto(false);
  };

  return (
    <div>
      <div className="card card-pad mb">
        <div className="prof-head">
          <div className="prof-av-wrap">
            <div className="prof-av" style={form.avatarUrl ? { backgroundImage: `url(${form.avatarUrl})`, backgroundSize: "cover", backgroundPosition: "center" } : undefined}>
              {!form.avatarUrl && initials(form.name)}
            </div>
            <button className="prof-av-edit" onClick={() => fileRef.current?.click()} disabled={uploadingPhoto}
                    title={t("sd_pf_photo")} aria-label={t("sd_pf_photo")}><Camera size={15} /></button>
            <input ref={fileRef} type="file" accept="image/*" style={{ display: "none" }} onChange={onPhoto} />
          </div>
          <div style={{ flex: 1 }}>
            <div className="prof-name">{form.name}</div>
            <div className="prof-meta">{form.target}{form.memberSince ? " · " + t("sd_pf_member").replace("{d}", fmtDate(form.memberSince)) : ""}</div>
            {uploadingPhoto && <div style={{ fontSize: 12, color: "var(--muted)", marginTop: 4, fontWeight: 600 }}>{t("sd_pf_photoup")}</div>}
            {avatarErr && <div style={{ fontSize: 12, color: "#c0392b", marginTop: 4, fontWeight: 600 }}>{avatarErr}</div>}
            {form.avatarUrl && <button className="prof-av-remove" onClick={() => persist({ avatarUrl: null }, t("sd_pf_photormd"))}>{t("sd_pf_photorm")}</button>}
            <div style={{ display: "flex", gap: 8, marginTop: 10, flexWrap: "wrap" }}>
              <span className="chip" style={{ background: "#fcf3df", color: "#d4a64a" }}><Trophy size={13} />{earned}/{achievements.length} {t("sd_pf_badges")}</span>
              <span className="chip" style={{ background: "#fbeaea", color: "#c0392b" }}><Flame size={13} />{derived.streak} {t("sd_pf_streak")}</span>
              {derived.bestRank != null && <span className="chip" style={{ background: "#e8f6ee", color: "#1f8a4c" }}><Medal size={13} />{t("sd_pf_bestrank")} #{derived.bestRank}</span>}
            </div>
          </div>
        </div>
      </div>

      <div className="grid2b mb">
        <div className="card card-pad">
          <div className="eyebrow">{t("sd_pf_settings")}</div>
          <div className="panel-title" style={{ marginBottom: 16 }}>{t("sd_pf_details")}</div>
          <div className="field"><label htmlFor="pf-name">{t("sd_pf_name")}</label>
            <input id="pf-name" className="inp" value={form.name || ""} onChange={(e) => setForm({ ...form, name: e.target.value })} /></div>
          <div className="field"><label htmlFor="pf-target">{t("sd_pf_target")}</label>
            <input id="pf-target" className="inp" value={form.target || ""} onChange={(e) => setForm({ ...form, target: e.target.value })} placeholder="UPSC Prelims 2026" /></div>
          <div className="field"><label htmlFor="pf-date">{t("sd_pf_tdate")}</label>
            <input id="pf-date" className="inp" type="date" value={form.targetDate || ""} onChange={(e) => setForm({ ...form, targetDate: e.target.value })} /></div>
          <div className="field"><label htmlFor="pf-city">{t("sd_pf_city")}</label>
            <input id="pf-city" className="inp" value={form.city || ""} onChange={(e) => setForm({ ...form, city: e.target.value })} placeholder="Patna" /></div>
          <div className="field"><label>{t("sd_pf_email")}</label>
            <input className="inp" value={form.email || ""} disabled style={{ opacity: .65, cursor: "not-allowed" }} />
            <div style={{ fontSize: 11.5, color: "var(--muted)", marginTop: 5 }}>{t("sd_pf_emailnote")}</div></div>
          <button className="btn btn-primary" style={{ width: "auto" }} onClick={save} disabled={saving}>
            <Save size={16} />{saving ? t("sd_pf_saving") : t("sd_pf_save")}
          </button>
        </div>

        <div className="card card-pad">
          <div className="eyebrow">{t("sd_pf_notif")}</div>
          <div className="panel-title" style={{ marginBottom: 8 }}>{t("sd_pf_reminders")}</div>
          {[["email", "Email", t("sd_pf_n_email")],
            ["sms", "SMS", t("sd_pf_n_sms")],
            ["whatsapp", "WhatsApp", t("sd_pf_n_wa")]].map(([key, label, desc]) => (
            <div className="toggle-row" key={key}>
              <div><div style={{ fontWeight: 700, fontSize: 14 }}>{label}</div><div style={{ fontSize: 12.5, color: "var(--muted)" }}>{desc}</div></div>
              <button className={"switch" + (notif[key] ? " on" : "")} onClick={() => toggleNotif(key)}
                      role="switch" aria-checked={!!notif[key]} aria-label={label + " notifications"} />
            </div>
          ))}
        </div>
      </div>

      <div className="card card-pad">
        <div className="sec-head"><div><div className="eyebrow">{t("sd_ach_eyebrow")}</div><div className="panel-title">{t("sd_ach_h")}</div></div>
          <span style={{ fontSize: 13, fontWeight: 700, color: "var(--gold-2)" }}>{t("sd_ach_count").replace("{a}", earned).replace("{b}", achievements.length)}</span></div>
        <div className="ach-grid">
          {achievements.map((a) => {
            const Icon = a.icon;
            return (
              <div className={"ach " + (a.earned ? "earned" : "locked")} key={a.key}>
                <div className="ach-ic" style={{ background: a.earned ? "linear-gradient(135deg,#ecca88,#dca84a)" : "#fdf6e3", color: a.earned ? "#ffffff" : "#bcae94" }}>
                  {a.earned ? <Icon size={24} /> : <Lock size={22} />}
                </div>
                <div className="ach-t">{t(a.tKey)}</div>
                <div className="ach-d">{t(a.dKey)}</div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

/* ============================================================
   APP SHELL
   ============================================================ */
/* ============================================================
   REFER & EARN

   The link is the only way in. There is deliberately no "enter a
   referral code" field: a typed box invites students to trade
   codes in comment sections, which is precisely the abuse the
   link-only rule exists to stop. The code rides in ?ref= and is
   bound automatically, once, on the invitee's first sign-in.
   ============================================================ */
const LEDGER_KEY = {
  referral_bonus: "sd_wallet_bonus",
  withdrawal: "sd_wallet_wd",
  adjustment: "sd_wallet_adj",
  reversal: "sd_wallet_rev",
};

function ReferView({ toast }) {
  const { t } = useLang();
  const [stats, setStats] = useState(null);
  const [list, setList] = useState([]);
  const [wallet, setWallet] = useState(null);
  const [ledger, setLedger] = useState([]);
  const [err, setErr] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const [s, l, w, tx] = await Promise.all([
          DB.myReferralStats(), DB.myReferrals(), DB.myWallet(), DB.myWalletTransactions(),
        ]);
        if (!alive) return;
        setStats(s);
        setList(l);
        setWallet(w);
        setLedger(tx);
      } catch (e) {
        if (alive) setErr(e?.message || "Could not load your referral details");
      }
      if (alive) setLoading(false);
    })();
    return () => { alive = false; };
  }, []);

  const link = stats ? DB.referralLink(stats.code) : "";
  const pitch = `I'm preparing on JUNOONIAS — full-length mocks with real rank and a proper analysis after every test. Join with my link: ${link}`;

  const copy = async () => {
    try {
      await navigator.clipboard.writeText(link);
      toast(t("sd_ref_copied"));
    } catch {
      // The Clipboard API needs a secure context and a user gesture; on older
      // Android browsers neither is guaranteed. Fall back to a selection.
      try {
        const el = document.createElement("textarea");
        el.value = link;
        el.style.position = "fixed";
        el.style.opacity = "0";
        document.body.appendChild(el);
        el.select();
        document.execCommand("copy");
        document.body.removeChild(el);
        toast(t("sd_ref_copied"));
      } catch {
        toast("Couldn't copy — long-press the link to copy it manually");
      }
    }
  };

  const share = async () => {
    if (navigator.share) {
      try {
        await navigator.share({ title: "JUNOONIAS", text: pitch, url: link });
        return;
      } catch { /* the user dismissed the sheet — not an error */ }
    }
    window.open(`https://wa.me/?text=${encodeURIComponent(pitch)}`, "_blank", "noopener,noreferrer");
  };

  if (loading) return <div className="card card-pad" style={{ textAlign: "center", color: "var(--muted)" }}>{t("sd_ref_loading")}</div>;
  if (err) return <ErrorState message={err} onRetry={() => window.location.reload()} />;
  if (!stats) return <ErrorState message="Your referral code hasn't been generated yet. Reload the page." onRetry={() => window.location.reload()} />;

  return (
    <div>
      {wallet && (
        <div className="rf-wallet">
          <div className="rf-wal-main">
            <div className="rf-wal-label">{t("sd_wallet_bal")}</div>
            <div className="rf-wal-amt"><small>₹</small>{wallet.balance}</div>
            <div className="rf-wal-sub">
              ₹{wallet.lifetime} {t("sd_earned_from")} {stats.paid} {stats.paid === 1 ? t("sd_paid_ref_one") : t("sd_paid_refs")}
            </div>
          </div>
          <div className="rf-wal-side">
            <div className="rf-wal-label" style={{ marginBottom: -4 }}>{t("sd_wallet_unlock")}</div>
            <div className={"rf-gate " + (wallet.balance >= wallet.minWithdraw ? "ok" : "no")}>
              <span className="tick">{wallet.balance >= wallet.minWithdraw ? "✓" : "1"}</span>
              <span>₹{wallet.minWithdraw} — {t("sd_you_have")} ₹{wallet.balance}</span>
            </div>
            <div className={"rf-gate " + (wallet.hasActiveCourse ? "ok" : "no")}>
              <span className="tick">{wallet.hasActiveCourse ? "✓" : "2"}</span>
              <span>
                {t("sd_one_active")}
                {wallet.hasActiveCourse ? "" : ` — ${t("sd_buy_unlock")}`}
              </span>
            </div>
            <div style={{ fontSize: 11.5, color: "var(--muted)", lineHeight: 1.5 }}>
              {t("sd_wallet_payouts")}
            </div>
          </div>
        </div>
      )}

      <div className="rf-hero">
        <div className="rf-hero-in">
          <h3><Gift size={20} /> {t("sd_ref_invite")} ₹{stats.bonus}</h3>
          <p>
            {t("sd_ref_lede")}
          </p>

          <div className="rf-code"><span>{stats.code}</span></div>

          <div className="rf-linkrow">
            <input className="rf-linkbox" readOnly value={link} onFocus={(e) => e.target.select()} aria-label={t("sd_your_link")} />
            <button className="rf-act rf-act-gold" onClick={copy}><Copy size={15} /> {t("sd_ref_copy")}</button>
            <button className="rf-act rf-act-line" onClick={share}><Share2 size={15} /> {t("sd_ref_share")}</button>
          </div>

          <p className="rf-fine">
            {t("sd_ref_fine")}
          </p>
        </div>
      </div>

      <div className="stats" style={{ marginTop: 22 }}>
        <StatCard icon={<Users size={19} />} color="#7a1f1f" n={stats.total} label={t("sd_ref_joined")} sub={t("sd_ref_joined_s")} />
        <StatCard icon={<CheckCircle2 size={19} />} color="#1f8a4c" n={stats.paid} label={t("sd_ref_bought")} sub={t("sd_ref_bought_s")} />
        <StatCard icon={<IndianRupee size={19} />} color="#b8923a" n={`₹${wallet ? wallet.lifetime : 0}`} label={t("sd_ref_lifetime")} sub={t("sd_ref_lifetime_s")} />
      </div>

      <div className="rf-steps">
        <div className="rf-step">
          <div className="n">1</div>
          <b>{t("sd_ref_s1_t")}</b>
          <span>{t("sd_ref_s1_d")}</span>
        </div>
        <div className="rf-step">
          <div className="n">2</div>
          <b>{t("sd_ref_s2_t")}</b>
          <span>{t("sd_ref_s2_d")}</span>
        </div>
        <div className="rf-step">
          <div className="n">3</div>
          <b>{t("sd_ref_s3_t")}</b>
          <span>{t("sd_ref_s3_d")}</span>
        </div>
      </div>

      <div className="card card-pad">
        <div className="sec-head">
          <div>
            <h2>{t("sd_ref_people")}</h2>
            <div className="note">{t("sd_ref_masked")}</div>
          </div>
        </div>
        {list.length === 0 ? (
          <div className="empty">
            <div className="empty-ic"><UserPlus size={24} /></div>
            {t("sd_ref_none")}
          </div>
        ) : list.map((r, i) => (
          <div className="rf-row" key={i}>
            <Avatar name={r.name} />
            <div className="who">
              <b>{r.name}</b>
              <span>{t("sd_joined_on").replace("{d}", fmtDate(r.joined))}</span>
            </div>
            {r.paid
              ? <Badge color={{ bg: "#e8f6ee", fg: "#1f8a4c" }}>{t("sd_ref_bought")}</Badge>
              : <Badge color={{ bg: "#fdf6e3", fg: "#a89474" }}>{t("sd_ref_browsing")}</Badge>}
          </div>
        ))}
      </div>

      {ledger.length > 0 && (
        <div className="card card-pad" style={{ marginTop: 18 }}>
          <div className="sec-head">
            <div>
              <h2>{t("sd_wallet_hist")}</h2>
              <div className="note">{t("sd_wallet_hist_s")}</div>
            </div>
          </div>
          {ledger.map((tx) => (
            <div className="rf-ledger-row" key={tx.id}>
              <div style={{
                width: 34, height: 34, borderRadius: 10, flex: "0 0 auto", display: "grid",
                placeItems: "center",
                background: tx.status === "reversed" ? "#f4efe4" : "#e8f6ee",
                color: tx.status === "reversed" ? "#a89474" : "#1f8a4c",
              }}>
                <Wallet size={16} />
              </div>
              <div style={{ minWidth: 0 }}>
                <div style={{ fontSize: 13.5, fontWeight: 700 }}>
                  {LEDGER_KEY[tx.type] ? t(LEDGER_KEY[tx.type]) : tx.type.replace(/_/g, " ")}
                  {tx.status === "reversed" && (
                    <span style={{ fontWeight: 600, color: "var(--muted)" }}> · {t("sd_wallet_revd")}</span>
                  )}
                </div>
                <div style={{ fontSize: 12, color: "var(--muted)" }}>{fmtDate(tx.at)}</div>
              </div>
              <div className={"amt" + (tx.status === "reversed" ? " rev" : "")}>
                {tx.amount > 0 ? "+" : "−"}₹{Math.abs(tx.amount)}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

/* Labels are dictionary keys, not text: these are module constants, so they
   cannot call t() themselves — the sidebar and the page header resolve them
   at render time. */

/* ============================================================
   FEEDBACK

   A place to say something went wrong, and to see that a person
   read it. The reply is the point: feedback that vanishes into a
   form teaches students not to bother a second time.
   ============================================================ */
const FB_KINDS = ["bug", "content", "test", "payment", "suggestion", "general"];
const FB_STATUS_COLOR = {
  new:         { bg: "#fdf6e3", fg: "#a89474" },
  seen:        { bg: "#f6ecd2", fg: "#8a6a2a" },
  in_progress: { bg: "#faf2dc", fg: "#b8923a" },
  resolved:    { bg: "#e8f6ee", fg: "#1f8a4c" },
  wont_fix:    { bg: "#f4efe4", fg: "#8a7a6c" },
};

function FeedbackView({ toast }) {
  const { t } = useLang();
  const [kind, setKind] = useState("bug");
  const [rating, setRating] = useState(0);
  const [message, setMessage] = useState("");
  const [busy, setBusy] = useState(false);
  const [mine, setMine] = useState([]);
  const [err, setErr] = useState("");

  const load = useCallback(async () => {
    try { setMine(await DB.myFeedback()); }
    catch (e) { console.error(e); }
  }, []);
  useEffect(() => { load(); }, [load]);

  const send = async (e) => {
    e.preventDefault();
    const text = message.trim();
    if (text.length < 5) { setErr(t("fb_too_short")); return; }
    setErr("");
    setBusy(true);
    try {
      await DB.submitFeedback({ kind, rating: rating || null, message: text, page: "/dashboard" });
      setMessage(""); setRating(0);
      toast(t("fb_sent"));
      await load();
    } catch (e2) {
      console.error("feedback failed", e2);
      setErr(t("fb_failed"));
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="fb-grid">
      <div className="card card-pad">
        <div className="sec-head">
          <div>
            <h2>{t("fb_h")}</h2>
            <div className="note">{t("fb_sub")}</div>
          </div>
        </div>

        <form onSubmit={send}>
          <label className="lbl">{t("fb_what")}</label>
          <div className="fb-kinds">
            {FB_KINDS.map((k) => (
              <button type="button" key={k} className={"fb-kind" + (kind === k ? " on" : "")}
                      onClick={() => setKind(k)}>{t("fb_k_" + k)}</button>
            ))}
          </div>

          <label className="lbl" style={{ marginTop: 16 }}>{t("fb_rate")}</label>
          <div className="fb-stars">
            {[1, 2, 3, 4, 5].map((n) => (
              <button type="button" key={n} className={"fb-star" + (n <= rating ? " on" : "")}
                      onClick={() => setRating(n === rating ? 0 : n)}
                      aria-label={`${n} / 5`}>
                <Star size={24} fill={n <= rating ? "currentColor" : "none"} />
              </button>
            ))}
          </div>

          <label className="lbl" style={{ marginTop: 16 }}>{t("fb_msg")}</label>
          <textarea className="inp" rows={5} value={message} maxLength={2000}
                    placeholder={t("fb_ph")}
                    onChange={(e) => { setMessage(e.target.value); setErr(""); }} />
          <div className="fb-note">{t("fb_tip")}</div>

          {err && <div className="fb-note" style={{ color: "var(--red,#c0392b)" }}>{err}</div>}

          <button className="btn btn-primary" type="submit" disabled={busy} style={{ marginTop: 14 }}>
            <Send size={15} />{busy ? t("fb_sending") : t("fb_send")}
          </button>
        </form>
      </div>

      <div className="card card-pad">
        <div className="sec-head">
          <div>
            <h2>{t("fb_mine")}</h2>
            <div className="note">{t("fb_mine_sub")}</div>
          </div>
        </div>

        {mine.length === 0 ? (
          <div className="empty">
            <div className="empty-ic"><MessageSquare size={24} /></div>
            {t("fb_none")}
          </div>
        ) : mine.map((f) => (
          <div className="fb-item" key={f.id}>
            <div className="fb-item-head">
              <Badge color={FB_STATUS_COLOR[f.status] || FB_STATUS_COLOR.new}>{t("fb_s_" + f.status)}</Badge>
              <span style={{ fontSize: 12, color: "var(--muted)" }}>{t("fb_k_" + f.kind)}</span>
              <span style={{ fontSize: 12, color: "var(--muted)", marginLeft: "auto" }}>{fmtDate(f.at)}</span>
            </div>
            <p className="fb-msg">{f.message}</p>
            {f.reply && (
              <div className="fb-reply">
                <b>{t("fb_reply")}</b>
                {f.reply}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

const NAV = [
  { id: "home", key: "sd_home", icon: Home },
  { id: "tests", key: "sd_tests", icon: FileText },
  { id: "performance", key: "sd_perf", icon: BarChart3 },
  { id: "batches", key: "sd_batches", icon: GraduationCap },
  { id: "materials", key: "sd_materials", icon: FolderOpen },
  { id: "leaderboard", key: "sd_leaderboard", icon: Trophy },
  { id: "refer", key: "sd_refer", icon: Gift },
  { id: "feedback", key: "sd_feedback", icon: MessageSquare },
  { id: "profile", key: "sd_profile", icon: User },
];
const META_KEY = {
  home: "sd_home", tests: "sd_tests", performance: "sd_perf", batches: "sd_batches",
  materials: "sd_materials", leaderboard: "sd_leaderboard", refer: "sd_refer",
  feedback: "sd_feedback", profile: "sd_profile",
};

const NOTIF_ICON = {
  success: { ic: <CheckCircle2 size={16} />, c: { bg: "#e8f6ee", fg: "#1f8a4c" } },
  test: { ic: <Calendar size={16} />, c: { bg: "#faf2dc", fg: "#b8923a" } },
  material: { ic: <FolderOpen size={16} />, c: { bg: "#f6ecd2", fg: "#7a1f1f" } },
  info: { ic: <Bell size={16} />, c: { bg: "#fdf6e3", fg: "#a89474" } },
};

function App({ onLaunchExam, onLogout, onBrowse }) {
  const { t } = useLang();
  const [view, setView] = useState("home");
  const [loading, setLoading] = useState(true);
  const [loadError, setLoadError] = useState("");
  const [sbOpen, setSbOpen] = useState(false);
  const [bellOpen, setBellOpen] = useState(false);
  const [analysis, setAnalysis] = useState(null);
  const [toasts, setToasts] = useState([]);

  const [profile, setProfile] = useState(null);
  const [attempts, setAttempts] = useState([]);
  const [tests, setTests] = useState([]);
  const [materials, setMaterials] = useState([]);
  const [enrollments, setEnrollments] = useState([]);
  const [activity, setActivity] = useState([]);
  const [board, setBoard] = useState([]);
  const [notifs, setNotifs] = useState([]);
  const [reminders, setReminders] = useState(new Set());
  const [peer, setPeer] = useState(null);

  const toast = useCallback((msg) => {
    const id = uid();
    setToasts((t) => [...t, { id, msg }]);
    setTimeout(() => setToasts((t) => t.filter((x) => x.id !== id)), 3000);
  }, []);

  const load = useCallback(async () => {
    setLoadError("");
    try {
      const user = await DB.currentUser();
      if (!user) { setLoadError("Your session has expired. Please sign in again."); setLoading(false); return; }
      const prof = await DB.ensureProfile(user);

      const [att, allTests, mats, enr, act, lb, nts, rem] = await Promise.all([
        DB.listAttempts(user.id),
        DB.listTests({ publishedOnly: true }),
        DB.materials.list(),
        DB.listEnrollments(user.id),
        DB.studyActivity(user.id),
        DB.leaderboard(),
        DB.listNotifications(user.id),
        DB.listReminders(user.id),
      ]);

      const attemptedIds = new Set(att.map((a) => a.testId));
      const now = Date.now();
      const decorated = allTests.map((t) => ({
        ...t,
        attemptedByMe: attemptedIds.has(t.id),
        isUpcoming: t.scheduledFor ? new Date(t.scheduledFor).getTime() > now : false,
      }));

      setProfile({
        id: user.id,
        name: (prof.full_name || "").trim() || user.email?.split("@")[0] || "Aspirant",
        email: prof.email || user.email || "",
        target: prof.target_exam || "UPSC Prelims 2026",
        targetDate: prof.target_date || "",
        city: prof.city || "",
        avatarUrl: prof.avatar_url || null,
        prefs: prof.prefs || {},
        memberSince: prof.created_at ? prof.created_at.slice(0, 10) : null,
      });
      setAttempts(att);
      setTests(decorated);
      setMaterials(mats.filter((m) => m.isPublished !== false));
      setEnrollments(enr);
      setActivity(act);
      setBoard(lb);
      setNotifs(nts);
      setReminders(rem);

      // Peer benchmark for the performance page — averaged over the tests this
      // student has actually taken, so the comparison is like-for-like.
      if (att.length > 0) {
        const stats = await Promise.all(att.map((a) => DB.testStats(a.testId).catch(() => null)));
        const real = stats.filter((s) => s && s.takers > 1);
        if (real.length > 0) {
          setPeer({
            avgPct: real.reduce((x, s) => x + s.avgPct, 0) / real.length,
            bestPct: Math.max(...real.map((s) => s.bestPct)),
          });
        }
      }
    } catch (e) {
      console.error("dashboard load failed", e);
      setLoadError(e?.message || "We couldn't reach the server.");
    }
    setLoading(false);
  }, []);

  useEffect(() => { load(); }, [load]);

  const derived = useMemo(() => derive(attempts, activity), [attempts, activity]);
  const subjects = useMemo(() => DB.subjectStrength(attempts), [attempts]);
  const unread = notifs.filter((n) => !n.read_at).length;

  const openBell = async () => {
    const next = !bellOpen;
    setBellOpen(next);
    if (next && unread > 0 && profile) {
      try {
        await DB.markNotificationsRead(profile.id);
        setNotifs((ns) => ns.map((n) => ({ ...n, read_at: n.read_at || new Date().toISOString() })));
      } catch { /* the badge simply stays until the next load */ }
    }
  };

  if (loading) {
    return (
      <div className="sd-root">
        <style>{CSS}</style>
        <div className="loader"><DiyaLogo size={40} ring /> {t("sd_loading_dash")}</div>
      </div>
    );
  }

  if (loadError || !profile) {
    return (
      <div className="sd-root">
        <style>{CSS}</style>
        <div style={{ minHeight: "100vh", display: "grid", placeItems: "center", padding: 24 }}>
          <div style={{ maxWidth: 440, width: "100%" }}>
            <ErrorState message={loadError} onRetry={() => { setLoading(true); load(); }} />
            <button className="btn btn-ghost" style={{ marginTop: 8 }} onClick={onLogout}><LogOut size={16} />{t("sd_signout")}</button>
          </div>
        </div>
      </div>
    );
  }

  const go = (v) => { setView(v); setSbOpen(false); };
  const ctx = { profile, setProfile, attempts, tests, materials, enrollments,
                activity, derived, subjects, leaderboard: board, reminders, setReminders, peer, reload: load };

  return (
    <DataCtx.Provider value={ctx}>
      <div className="sd-root" onClick={() => bellOpen && setBellOpen(false)}>
        <style>{CSS}</style>

        {sbOpen && <div className="scrim" onClick={() => setSbOpen(false)} />}
        <aside className={"sb" + (sbOpen ? " open" : "")}>
          <div className="sb-brand">
            <div className="sb-logo">
              <DiyaLogo size={36} boxed radius={9} />
              <div><div className="sb-name" style={{ fontFamily: "var(--font-display)", letterSpacing: ".02em" }}>JUNOONIAS</div><div className="sb-tag">{t("sd_student")}</div></div>
            </div>
          </div>
          <nav className="sb-nav">
            {NAV.map((it) => { const Icon = it.icon; return (
              <button key={it.id} className={"sb-item" + (view === it.id ? " active" : "")} onClick={() => go(it.id)}
                      aria-current={view === it.id ? "page" : undefined}><Icon size={18} />{t(it.key)}</button>
            ); })}
            <div className="sb-streak">
              <div className="sb-streak-top"><Flame size={17} />{t("sd_streak_days").replace("{n}", derived.streak)}</div>
              <div className="sb-streak-sub">
                {t(derived.streak === 0 ? "sd_start_chain" : "sd_keep_chain")}
              </div>
            </div>
          </nav>
          {profile.targetDate && (
            <div style={{ padding: "14px 16px", borderTop: "1px solid rgba(255,255,255,.08)", fontSize: 11.5, color: "#e8d8b0" }}>
              {t("sd_days_to").replace("{n}", daysUntil(profile.targetDate)).replace("{x}", profile.target)}
            </div>
          )}
        </aside>

        <div className="main">
          <header className="topbar">
            <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
              <button className="hamburger" onClick={() => setSbOpen(true)} aria-label={t("sd_open_menu")}><Menu size={20} /></button>
              <div><h1>{t(META_KEY[view])}</h1><div className="sub">{t(META_KEY[view] + "_s")}</div></div>
            </div>
            <div className="tb-right">
              <div style={{ position: "relative" }} onClick={(e) => e.stopPropagation()}>
                <button className="bell" onClick={openBell} aria-label={`Notifications${unread ? ", " + unread + " unread" : ""}`}>
                  <Bell size={19} />{unread > 0 && <span className="bell-dot" />}
                </button>
                {bellOpen && (
                  <div className="notif">
                    <div className="notif-head">Notifications</div>
                    {notifs.length === 0 ? (
                      <div style={{ padding: "22px 16px", fontSize: 13, color: "var(--muted)", textAlign: "center" }}>Nothing new right now.</div>
                    ) : notifs.map((n) => {
                      const ic = NOTIF_ICON[n.kind] || NOTIF_ICON.info;
                      return (
                        <div className="notif-item" key={n.id}>
                          <div className="notif-ic" style={{ background: ic.c.bg, color: ic.c.fg }}>{ic.ic}</div>
                          <div><div className="notif-t">{n.title}</div><div className="notif-d">{n.body}</div></div>
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
              <ChromeControls />
              <button className="bell" title="Log out" aria-label="Log out" onClick={onLogout} style={{ marginRight: 2 }}><LogOut size={19} /></button>
              <button className="tb-av" onClick={() => go("profile")} aria-label={t("sd_open_profile")}
                      style={profile.avatarUrl ? { backgroundImage: `url(${profile.avatarUrl})`, backgroundSize: "cover", backgroundPosition: "center" } : undefined}>
                {!profile.avatarUrl && initials(profile.name)}
              </button>
            </div>
          </header>

          <main className="content">
            {view === "home" && <HomeView go={go} setAnalysis={setAnalysis} onStart={onLaunchExam} />}
            {view === "tests" && <TestsView setAnalysis={setAnalysis} onStart={onLaunchExam} toast={toast} />}
            {view === "performance" && <PerformanceView go={go} />}
            {view === "batches" && <BatchesView go={go} onStart={onLaunchExam} toast={toast} />}
            {view === "materials" && <MaterialsView toast={toast} />}
            {view === "leaderboard" && <LeaderboardView toast={toast} />}
            {view === "refer" && <ReferView toast={toast} />}
            {view === "feedback" && <FeedbackView toast={toast} />}
            {view === "profile" && <ProfileView toast={toast} />}
          </main>

          <footer className="sd-foot">
            <span>© {new Date().getFullYear()} JUNOONIAS · An Academy of Inner Fire</span>
            <span>
              {onBrowse && <><button className="flink" onClick={onBrowse}>All test series</button> · </>}
              <a href="mailto:junoonias123@gmail.com">junoonias123@gmail.com</a>
            </span>
          </footer>
        </div>

        <div className="toasts">{toasts.map((t) => <div className="toast" key={t.id} role="status"><CheckCircle2 size={18} />{t.msg}</div>)}</div>
        {analysis && <AnalysisModal a={analysis} onClose={() => setAnalysis(null)} onRetake={(id) => { setAnalysis(null); onLaunchExam(id); }} />}
      </div>
    </DataCtx.Provider>
  );
}


return App;
})();

export default StudentApp;
