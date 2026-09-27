// Checks the sub-topic-scoped blueprint extension in generate.js (subjectScope.sub_topics):
//  1. regression -- every blueprint WITHOUT sub_topics produces byte-identical cells to the
//     previous generate.js (git HEAD, extracted by the runner to src/lib/_generate_prev.tmp.js);
//  2. a scoped paper's cells use only its own sub-topics, and every margin (difficulty, type,
//     sub-topic) equals the largest-remainder rounding of its renormalised weights;
//  3. the pool, backfill included, never crosses the sub-topic boundary;
//  4. listed sub-topics without config weights split evenly.
// Run: git show HEAD:src/lib/generate.js > src/lib/_generate_prev.tmp.js && node verify_subtopic_scoped_blueprints.mjs
import { readFileSync } from "node:fs";
import { buildCells, generateTest } from "./src/lib/generate.js";
const { buildCells: prevBuildCells } = await import("./src/lib/_generate_prev.tmp.js");

const load = (f) => JSON.parse(readFileSync(new URL(f, import.meta.url), "utf8"));
const upsc = load("./live_upsc_config.json");
const bpsc = load("./live_bpsc_config.json");
let fail = 0;
const check = (label, ok, detail = "") => { console.log(`${ok ? "PASS" : "FAIL"}  ${label}${detail ? "  " + detail : ""}`); if (!ok) fail++; };
const key = (cells) => cells.map((c) => `${c.subject}|${c.difficulty}|${c.questionType}|${c.subTopic}|${c.n}`).sort().join("\n");
const roll = (cells, dim) => { const m = {}; for (const c of cells) m[c[dim]] = (m[c[dim]] || 0) + c.n; return m; };
const lr = (weights, total) => {
  const e = Object.entries(weights).filter(([, v]) => v > 0); const s = e.reduce((a, [, v]) => a + v, 0);
  const rows = e.map(([k, v], i) => { const x = total * v / s; return { k, i, n: Math.floor(x), rem: x - Math.floor(x) }; });
  let left = total - rows.reduce((a, r) => a + r.n, 0);
  [...rows].sort((a, b) => (Math.abs(b.rem - a.rem) > 1e-9 ? b.rem - a.rem : a.i - b.i)).forEach((r) => { if (left-- > 0) r.n++; });
  return Object.fromEntries(rows.filter((r) => r.n > 0).map((r) => [r.k, r.n]));
};
const same = (a, b) => JSON.stringify(Object.entries(a).sort()) === JSON.stringify(Object.entries(b).sort());

// ---- 1. regression: no sub_topics -> identical to the previous generator ----
const scenarios = [
  ["UPSC Polity sectional 120", upsc, { patternType: "sectional", questionCount: 120, subjectScope: { subject: "Polity" } }],
  ["UPSC History sectional 120", upsc, { patternType: "sectional", questionCount: 120, subjectScope: { subject: "History" } }],
  ["UPSC full-length 100", upsc, { patternType: "full_length", questionCount: 100, subjectScope: {} }],
  ["BPSC History sectional 150", bpsc, { patternType: "sectional", questionCount: 150, subjectScope: { subject: "History" } }],
  ["BPSC full-length 150", bpsc, { patternType: "full_length", questionCount: 150, subjectScope: {} }],
  ["UPSC History with empty sub_topics []", upsc, { patternType: "sectional", questionCount: 120, subjectScope: { subject: "History", sub_topics: [] } }],
];
for (const [label, cfg, bp0] of scenarios) {
  const bp = { examCategory: "x", ...bp0 };
  const pool = Object.keys(cfg.subjectWeights).map((s) => ({ subject: s }));
  check(`unchanged without sub_topics: ${label}`, key(buildCells({ blueprint: bp, config: cfg, pool })) === key(prevBuildCells({ blueprint: bp, config: cfg, pool })));
}

// ---- 2. the four Level-2 History tests: scope + exact margins ----
const hDiff = Object.fromEntries(Object.entries(upsc.difficultyWeights).filter(([, v]) => typeof v !== "object"));
const hType = upsc.questionTypeWeights.History;
const hSub = upsc.subTopicWeights.History;
const AC = ["Architecture", "Painting", "Music & Dance", "Iconography", "Culture-Other"];
const LEVEL2 = [["Ancient", ["Ancient"], 43], ["Medieval", ["Medieval"], 20], ["Modern", ["Modern"], 45], ["Art & Culture", AC, 12]];
for (const [name, subs, n] of LEVEL2) {
  const cells = buildCells({ blueprint: { examCategory: "upsc", patternType: "sectional", questionCount: n, subjectScope: { subject: "History", sub_topics: subs } }, config: upsc, pool: [] });
  const total = cells.reduce((s, c) => s + c.n, 0);
  const onlyOwn = cells.every((c) => subs.includes(c.subTopic));
  const expSub = lr(Object.fromEntries(Object.entries(hSub).filter(([k]) => subs.includes(k))), n);
  const ok = total === n && onlyOwn && same(roll(cells, "difficulty"), lr(hDiff, n)) && same(roll(cells, "questionType"), lr(hType, n)) && same(roll(cells, "subTopic"), expSub);
  check(`History ${name} (${n}Q): only its sub-topics, every margin exact`, ok,
    `${cells.length} cells | difficulty ${JSON.stringify(roll(cells, "difficulty"))} | type ${JSON.stringify(roll(cells, "questionType"))} | sub-topic ${JSON.stringify(roll(cells, "subTopic"))}`);
}

// ---- 3. pool + backfill never cross the sub-topic boundary ----
// A deliberately thin Ancient bank (2 questions) beside a rich Modern one: the Ancient
// paper must come up short with gaps, never pad itself with Modern questions.
const mk = (i, topic, difficulty, type) => ({ id: `q${i}`, examCategory: "upsc", subject: "History", topic, difficulty, type, status: "published", options: [{ id: "a", isCorrect: true }, { id: "b" }, { id: "c" }, { id: "d" }] });
const bank = [mk(1, "Ancient", "medium", "statement_based"), mk(2, "Ancient", "easy", "mcq")];
for (let i = 3; i < 60; i++) bank.push(mk(i, "Modern", ["easy", "medium", "hard"][i % 3], ["mcq", "statement_based", "match_the_following"][i % 3]));
const res = generateTest({ blueprint: { examCategory: "upsc", patternType: "sectional", questionCount: 10, subjectScope: { subject: "History", sub_topics: ["Ancient"] }, title: "Ancient" }, config: upsc, bank, options: { seed: 7 } });
const picked = res.questionIds.map((id) => bank.find((q) => q.id === id));
check("scoped pool excludes other sub-topics (backfill included)", picked.every((q) => q.topic === "Ancient") && res.report.poolSize === 2,
  `pool ${res.report.poolSize}, selected ${picked.length} (${JSON.stringify(res.report.distribution.subTopic)}), gaps reported ${res.report.gaps.reduce((s, g) => s + g.short, 0)}`);
const resAll = generateTest({ blueprint: { examCategory: "upsc", patternType: "sectional", questionCount: 10, subjectScope: { subject: "History" }, title: "All" }, config: upsc, bank, options: { seed: 7 } });
check("unscoped History paper still backfills across sub-topics as before", resAll.questionIds.length === 10, `selected ${resAll.questionIds.length}`);

// ---- 4. listed sub-topics without config weights split evenly ----
const even = buildCells({ blueprint: { examCategory: "upsc", patternType: "sectional", questionCount: 10, subjectScope: { subject: "History", sub_topics: ["Numismatics", "Epigraphy"] } }, config: upsc, pool: [] });
check("unweighted sub-topics split evenly", same(roll(even, "subTopic"), { Numismatics: 5, Epigraphy: 5 }), JSON.stringify(roll(even, "subTopic")));

console.log(fail ? `\n${fail} FAILED` : "\nALL PASS");
process.exit(fail ? 1 : 0);
