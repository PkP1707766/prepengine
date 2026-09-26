// Checks that buildCells() hits every intended total, not just the grand total:
// per subject, and per subject x difficulty / question-type / sub-topic, each must
// equal the largest-remainder rounding of its own weighted share. Targets are
// recomputed here independently of generate.js. Compares against the previous
// generate.js (git HEAD, extracted by the runner to src/lib/_generate_prev.tmp.js).
// Run: git show HEAD:src/lib/generate.js > src/lib/_generate_prev.tmp.js && node verify_apportion_marginals.mjs
import { readFileSync } from "node:fs";
import { buildCells } from "./src/lib/generate.js";
const { buildCells: prevBuildCells } = await import("./src/lib/_generate_prev.tmp.js");

const load = (f) => JSON.parse(readFileSync(new URL(f, import.meta.url), "utf8"));
const upsc = load("./live_upsc_config.json");
const bpsc = load("./live_bpsc_config.json");

// --- independent reference targets ---------------------------------------
// Same fallbacks as the generator: no weights -> a single "*" bucket (or equal thirds for difficulty).
const norm = (o, fallback = ["*"]) => {
  const e = Object.entries(o || {}).filter(([, v]) => typeof v === "number" && v > 0);
  if (!e.length) return fallback.map((k) => [k, 1 / fallback.length]);
  const s = e.reduce((a, [, v]) => a + v, 0); return e.map(([k, v]) => [k, v / s]);
};
const lr = (entries, total) => {
  const rows = entries.map(([k, v], i) => ({ k, i, n: Math.floor(total * v), rem: total * v - Math.floor(total * v) }));
  let left = total - rows.reduce((s, r) => s + r.n, 0);
  [...rows].sort((a, b) => (Math.abs(b.rem - a.rem) > 1e-9 ? b.rem - a.rem : a.i - b.i)).forEach((r) => { if (left-- > 0) r.n++; });
  return Object.fromEntries(rows.map((r) => [r.k, r.n]));
};
const diffFor = (cfg, s) => (cfg.difficultyWeights?.[s] && typeof cfg.difficultyWeights[s] === "object") ? cfg.difficultyWeights[s] : cfg.difficultyWeights;
const typeFor = (cfg, s) => { const tw = cfg.questionTypeWeights || {}; const f = Object.values(tw)[0]; return f && typeof f === "object" ? (tw[s] || {}) : tw; };

function expected(cfg, bp) {
  const subjects = bp.patternType === "full_length" ? norm(cfg.subjectWeights) : [[bp.subjectScope.subject, 1]];
  const seats = lr(subjects, bp.questionCount);
  const out = {};
  for (const [s] of subjects) {
    out[s] = { total: seats[s], difficulty: lr(norm(diffFor(cfg, s), ["easy", "medium", "hard"]), seats[s]), questionType: lr(norm(typeFor(cfg, s)), seats[s]) };
    if (bp.patternType === "sectional") out[s].subTopic = lr(norm(cfg.subTopicWeights?.[s]), seats[s]);
  }
  return out;
}
const actual = (cells, dim) => { const m = {}; for (const c of cells) { m[c.subject] ??= {}; m[c.subject][c[dim]] = (m[c.subject][c[dim]] || 0) + c.n; } return m; };
const nz = (o) => Object.fromEntries(Object.entries(o || {}).filter(([, v]) => v > 0));
const same = (a, b) => JSON.stringify(Object.entries(nz(a)).sort()) === JSON.stringify(Object.entries(nz(b)).sort());

let fail = 0;
const scenarios = [
  ["UPSC Polity sectional 120", upsc, { patternType: "sectional", questionCount: 120, subjectScope: { subject: "Polity" } }],
  ["UPSC History sectional 120", upsc, { patternType: "sectional", questionCount: 120, subjectScope: { subject: "History" } }],
  ["UPSC full-length 100", upsc, { patternType: "full_length", questionCount: 100, subjectScope: {} }],
  ["BPSC History sectional 150", bpsc, { patternType: "sectional", questionCount: 150, subjectScope: { subject: "History" } }],
  ["BPSC full-length 150", bpsc, { patternType: "full_length", questionCount: 150, subjectScope: {} }],
];
for (const [label, cfg, bp0] of scenarios) {
  const bp = { examCategory: "x", ...bp0 };
  const pool = Object.keys(cfg.subjectWeights).map((s) => ({ subject: s }));
  const now = buildCells({ blueprint: bp, config: cfg, pool });
  const prev = prevBuildCells({ blueprint: bp, config: cfg, pool });
  const exp = expected(cfg, bp);
  const dims = bp.patternType === "sectional" ? ["difficulty", "questionType", "subTopic"] : ["difficulty", "questionType"];
  const total = now.reduce((s, c) => s + c.n, 0);
  const problems = [];
  if (total !== bp.questionCount) problems.push(`total ${total}`);
  const subjTot = {}; now.forEach((c) => (subjTot[c.subject] = (subjTot[c.subject] || 0) + c.n));
  for (const s of Object.keys(exp)) if ((subjTot[s] || 0) !== exp[s].total) problems.push(`${s} total ${subjTot[s]} != ${exp[s].total}`);
  let prevOff = 0;
  for (const d of dims) {
    const a = actual(now, d), p = actual(prev, d);
    for (const s of Object.keys(exp)) {
      if (!same(a[s], exp[s][d])) problems.push(`${s}.${d} ${JSON.stringify(nz(a[s]))} != ${JSON.stringify(nz(exp[s][d]))}`);
      for (const k of new Set([...Object.keys(exp[s][d]), ...Object.keys(p[s] || {})])) prevOff += Math.abs((p[s]?.[k] || 0) - (exp[s][d][k] || 0));
    }
  }
  const ok = problems.length === 0;
  if (!ok) fail++;
  console.log(`${ok ? "PASS" : "FAIL"}  ${label}: ${now.length} cells, total ${total}; every margin matches its target` +
    `  (previous generate.js was off by ${prevOff} seats across margins)`);
  if (bp.patternType === "sectional") {
    const s = bp.subjectScope.subject;
    console.log(`        difficulty now ${JSON.stringify(nz(actual(now, "difficulty")[s]))}  was ${JSON.stringify(nz(actual(prev, "difficulty")[s]))}  target ${JSON.stringify(nz(exp[s].difficulty))}`);
  }
  problems.slice(0, 6).forEach((p) => console.log("        " + p));
}
console.log(fail ? `\n${fail} FAILED` : "\nALL PASS");
process.exit(fail ? 1 : 0);
