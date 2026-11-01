// Cell targets (difficulty x type x sub-topic) for the Level-4 GS Paper I simulators (100 questions each).
// A simulator mirrors one recent paper's shape, as the Level-4 CSAT simulators do (subject mix from the tagged papers in
// upsc_gs1_combined_2015-2026.csv):
//   Layout A, the 2023/24 shape: Polity 16, History 11, Environment 15, Geography 15, Economy 15, S&T 10, current affairs 18
//   Layout B, the 2025 shape:    Polity 13, History 17, Environment 10, Geography 6, Economy 16, S&T 14, current affairs 24
//   Layout C, the 2026 shape:    Polity 12, History 22, Environment 9, Geography 9, Economy 19, S&T 15, current affairs 14
// Rotation A B C A B C A B C C, so the last simulator is the latest shape. The static part is drafted now; the current-
// affairs part nearer the paper's date (April-May 2027), as for Level 3. Within each subject the sub-topic and type cells
// are that subject's sectional mix at that size (the engine's buildCells); then difficulty and type are re-weighted to the
// shape's year: the papers grew harder (easy 29 -> 19 -> ~8 -> 5 of 100, hard 23 -> 20 -> ~39 -> 41) and changed format
// (Statement-I/II about 12 in 2023-25 and 3 in 2026; List-I/II codes about 10 in 2026).
// Run from the repo root: node pyq-analysis-upsc/scratch/upsc_l4_gs_cell_targets.mjs [sim no]   (one JSON line per sim)
import { readFileSync } from "node:fs";
import { buildCells } from "../../src/lib/generate.js";

const cfg = JSON.parse(readFileSync(new URL("../../live_upsc_config.json", import.meta.url), "utf8"));
const STATIC = ["Polity", "History", "Environment & Ecology", "Geography", "Economy", "Science & Technology"];
const LAYOUTS = {
  A: { mix: [16, 11, 15, 15, 15, 10], ca: 18, easy: 0.20, hard: 0.22, ar: 10, match: 7 },
  B: { mix: [13, 17, 10, 6, 16, 14], ca: 24, easy: 0.09, hard: 0.36, ar: 9, match: 7 },
  C: { mix: [12, 22, 9, 9, 19, 15], ca: 14, easy: 0.06, hard: 0.40, ar: 3, match: 9 },
};
const ROTATION = ["A", "B", "C", "A", "B", "C", "A", "B", "C", "C"];

const sectional = (subject, n) => buildCells({ blueprint: { examCategory: "upsc", patternType: "sectional", questionCount: n,
  subjectScope: { subject } }, config: cfg, pool: [] }).filter((c) => c.n > 0);

// Move units from one label to another, one at a time, always from the subject that holds most of the source label,
// so each subject keeps its share of the shift. Deterministic (stable sort on subject, sub-topic).
function shift(units, field, from, to, k, also = () => true) {
  for (let i = 0; i < k; i++) {
    const pool = units.filter((u) => u[field] === from && also(u));
    if (!pool.length) return;
    const per = {};
    for (const u of pool) per[u.subject] = (per[u.subject] || 0) + 1;
    const subj = Object.keys(per).sort((a, b) => per[b] - per[a] || a.localeCompare(b))[0];
    const u = pool.filter((x) => x.subject === subj).sort((a, b) => a.subTopic.localeCompare(b.subTopic))[0];
    u[field] = to;
  }
}
const count = (units, field, v) => units.filter((u) => u[field] === v).length;

const want = process.argv[2] ? Number(process.argv[2]) : null;
ROTATION.forEach((shape, idx) => {
  const no = idx + 1;
  if (want && want !== no) return;
  const L = LAYOUTS[shape];
  const units = [];
  STATIC.forEach((s, i) => {
    for (const c of sectional(s, L.mix[i])) for (let k = 0; k < c.n; k++)
      units.push({ subject: s, subTopic: c.subTopic, questionType: c.questionType, difficulty: c.difficulty });
  });
  const n = units.length;
  const E = Math.round(L.easy * n), H = Math.round(L.hard * n);
  // difficulty: easy down (or up) to E, then hard up to H, through medium
  if (count(units, "difficulty", "easy") > E) shift(units, "difficulty", "easy", "medium", count(units, "difficulty", "easy") - E);
  else shift(units, "difficulty", "medium", "easy", E - count(units, "difficulty", "easy"));
  if (count(units, "difficulty", "hard") < H) shift(units, "difficulty", "medium", "hard", H - count(units, "difficulty", "hard"));
  else shift(units, "difficulty", "hard", "medium", count(units, "difficulty", "hard") - H);
  // type: Statement-I/II and matching to the shape's counts, through statement-based items
  const ar = count(units, "questionType", "assertion_reason"), mt = count(units, "questionType", "match_the_following");
  if (ar > L.ar) shift(units, "questionType", "assertion_reason", "statement_based", ar - L.ar);
  else shift(units, "questionType", "statement_based", "assertion_reason", L.ar - ar);
  if (mt > L.match) shift(units, "questionType", "match_the_following", "statement_based", mt - L.match);
  else shift(units, "questionType", "statement_based", "match_the_following", L.match - mt);
  const cells = {};
  for (const u of units) {
    const key = [u.difficulty, u.questionType, u.subTopic, u.subject].join("|");
    cells[key] = (cells[key] || 0) + 1;
  }
  const roll = (k) => { const m = {}; for (const u of units) m[u[k]] = (m[u[k]] || 0) + 1; return m; };
  console.log(JSON.stringify({ no, shape, static: n, currentAffairs: L.ca,
    bySubject: Object.fromEntries(STATIC.map((s, i) => [s, L.mix[i]])), bySubTopic: roll("subTopic"),
    byType: roll("questionType"), byDifficulty: roll("difficulty"),
    cells: Object.entries(cells).map(([k, v]) => { const [d, t, st, s] = k.split("|"); return [d, t, st, v, s]; }) }));
});
