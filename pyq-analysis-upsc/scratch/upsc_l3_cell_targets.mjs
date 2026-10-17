// Cell targets (difficulty x type x sub-topic) for the Level-3 "Integration & Precision" GS papers (100 questions each).
// A Level-3 paper is a full GS Paper I on the engine's full-length mix at the exam's own difficulty (the live config):
// 84 static questions -- Polity 15, History 16, Environment 15, Geography 10, Economy 17, Science & Technology 11 --
// and 16 current-affairs questions. As with Level 2's Test 21, the static 84 are drafted now and the 16 current-affairs
// questions nearer the paper's date (late March to April 2027), so that they are current when the paper runs.
// Within each subject the cells are that subject's sectional mix at that size, as for Level 1's revision paper.
// Run from the repo root: node pyq-analysis-upsc/scratch/upsc_l3_cell_targets.mjs [test no]   (one JSON line per test)
import { readFileSync } from "node:fs";
import { buildCells } from "../../src/lib/generate.js";

const cfg = JSON.parse(readFileSync(new URL("../../live_upsc_config.json", import.meta.url), "utf8"));
const STATIC = ["Polity", "History", "Environment & Ecology", "Geography", "Economy", "Science & Technology"];
const TESTS = [1, 2, 3, 4, 5, 6];

const full = buildCells({ blueprint: { examCategory: "upsc", patternType: "full_length", questionCount: 100, subjectScope: {} },
  config: cfg, pool: [] }).filter((c) => c.n > 0);
const parts = {};
for (const c of full) parts[c.subject] = (parts[c.subject] || 0) + c.n;
const sectional = (subject, n) => buildCells({ blueprint: { examCategory: "upsc", patternType: "sectional", questionCount: n,
  subjectScope: { subject } }, config: cfg, pool: [] }).filter((c) => c.n > 0);

const want = process.argv[2] ? Number(process.argv[2]) : null;
for (const no of TESTS.filter((x) => !want || x === want)) {
  const cells = STATIC.flatMap((s) => sectional(s, parts[s] || 0).map((c) => ({ ...c, subject: s })));
  const roll = (k) => { const m = {}; for (const c of cells) m[c[k]] = (m[c[k]] || 0) + c.n; return m; };
  console.log(JSON.stringify({ no, static: cells.reduce((a, c) => a + c.n, 0), currentAffairs: parts["Current Affairs"] || 0,
    bySubject: Object.fromEntries(STATIC.map((s) => [s, parts[s] || 0])), bySubTopic: roll("subTopic"),
    byType: roll("questionType"), byDifficulty: roll("difficulty"),
    cells: cells.map((c) => [c.difficulty, c.questionType, c.subTopic, c.n]) }));
}
