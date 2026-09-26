// Proves the per-subject difficulty override in generate.js changes only the subject
// that has one. Run: node verify_per_subject_difficulty.mjs
import { readFileSync } from "node:fs";
import { buildCells } from "./src/lib/generate.js";

const base = JSON.parse(readFileSync(new URL("./live_upsc_config.json", import.meta.url), "utf8"));
const POLITY_DIFF = { easy: 0.0536, medium: 0.6071, hard: 0.3393 };
const withOverride = { ...base, difficultyWeights: { ...base.difficultyWeights, Polity: POLITY_DIFF } };

const sectional = (subject, n) => ({ examCategory: "upsc", patternType: "sectional", questionCount: n, subjectScope: { subject } });
const key = (cells) => cells.map((c) => `${c.subject}|${c.difficulty}|${c.questionType}|${c.subTopic}|${c.n}`).sort().join("\n");
const byDiff = (cells) => { const m = { easy: 0, medium: 0, hard: 0 }; cells.forEach((c) => (m[c.difficulty] += c.n)); return m; };
let fail = 0;
const check = (label, ok, detail = "") => { console.log(`${ok ? "PASS" : "FAIL"}  ${label}${detail ? "  " + detail : ""}`); if (!ok) fail++; };

// 1. History sectional: identical cells with and without a Polity override.
const hBefore = buildCells({ blueprint: sectional("History", 120), config: base, pool: [] });
const hAfter = buildCells({ blueprint: sectional("History", 120), config: withOverride, pool: [] });
check("History 120Q cells unchanged by a Polity override", key(hBefore) === key(hAfter), JSON.stringify(byDiff(hAfter)));

// 2. Configs WITHOUT an override produce byte-identical cells to the previous
//    generate.js (git HEAD, extracted to src/lib/_generate_prev.tmp.js).
const { buildCells: prevBuildCells } = await import("./src/lib/_generate_prev.tmp.js");
const flat = { ...base, difficultyWeights: { easy: 0.3, medium: 0.5, hard: 0.2 } };
const fullLen = { examCategory: "upsc", patternType: "full_length", questionCount: 100, subjectScope: {} };
const pool0 = Object.keys(base.subjectWeights).map((s) => ({ subject: s }));
for (const [label, cfg, bp, pl] of [
  ["live config, History sectional", base, sectional("History", 120), []],
  ["live config, Polity sectional (no override)", base, sectional("Polity", 120), []],
  ["flat BPSC-shape config, History sectional", flat, sectional("History", 120), []],
  ["live config, full-length 100Q", base, fullLen, pool0],
  ["empty difficulty config", { ...base, difficultyWeights: {} }, sectional("History", 120), []],
  ["missing difficulty config", { ...base, difficultyWeights: undefined }, sectional("History", 120), []],
]) {
  const now = buildCells({ blueprint: bp, config: cfg, pool: pl });
  const prev = prevBuildCells({ blueprint: bp, config: cfg, pool: pl });
  check(`identical to previous generate.js: ${label}`, key(now) === key(prev), `${now.length} cells`);
}

// 3. Polity sectional uses its own mix.
const p = buildCells({ blueprint: sectional("Polity", 120), config: withOverride, pool: [] });
const pd = byDiff(p);
check("Polity 120Q uses its override (~6 easy / ~73 medium / ~41 hard)", pd.easy <= 8 && pd.hard >= 38, JSON.stringify(pd));
check("Polity 120Q totals 120", p.reduce((s, c) => s + c.n, 0) === 120);

// 5. Full-length: only Polity's slice shifts; every other subject's difficulty split is unchanged.
const fl = { examCategory: "upsc", patternType: "full_length", questionCount: 100, subjectScope: {} };
const pool = Object.keys(base.subjectWeights).map((s) => ({ subject: s }));
const a = buildCells({ blueprint: fl, config: base, pool });
const b = buildCells({ blueprint: fl, config: withOverride, pool });
const perSubj = (cells) => { const m = {}; cells.forEach((c) => { m[c.subject] ??= { easy: 0, medium: 0, hard: 0 }; m[c.subject][c.difficulty] += c.n; }); return m; };
const A = perSubj(a), B = perSubj(b);
const others = Object.keys(A).filter((s) => s !== "Polity");
const subjTotals = (m) => Object.fromEntries(Object.entries(m).map(([s, d]) => [s, d.easy + d.medium + d.hard]));
check("full-length: every subject keeps its question count", JSON.stringify(subjTotals(A)) === JSON.stringify(subjTotals(B)), JSON.stringify(subjTotals(B)));
const drift = others.map((s) => Math.abs(A[s].hard - B[s].hard) + Math.abs(A[s].easy - B[s].easy)).reduce((x, y) => x + y, 0);
check("full-length: non-Polity difficulty splits shift by at most rounding (<=2 total)", drift <= 2, `drift=${drift}`);
check("full-length: Polity slice gets harder", B.Polity.hard > A.Polity.hard && B.Polity.easy < A.Polity.easy, `before ${JSON.stringify(A.Polity)} after ${JSON.stringify(B.Polity)}`);

console.log(fail ? `\n${fail} FAILED` : "\nALL PASS");
process.exit(fail ? 1 : 0);
