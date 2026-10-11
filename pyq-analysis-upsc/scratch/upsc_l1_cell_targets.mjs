// Cell targets (difficulty x type x sub-topic) for the six Level-1 NCERT Foundation subject papers
// (100 questions each). Sub-topic and question-type shares come from the live PYQ-derived config, as
// for Level 2; difficulty uses a foundation mix (30 / 55 / 15) instead of the subject's exam mix,
// because Level 1 builds the base before the exam-level sectionals.
// Run from the repo root: node pyq-analysis-upsc/scratch/upsc_l1_cell_targets.mjs [test no]
import { readFileSync } from "node:fs";
import { buildCells } from "../../src/lib/generate.js";

export const LEVEL1 = [
  { no: 1, subject: "Polity" }, { no: 2, subject: "History" }, { no: 3, subject: "Environment & Ecology" },
  { no: 4, subject: "Geography" }, { no: 5, subject: "Economy" }, { no: 6, subject: "Science & Technology" },
];
export const FOUNDATION = { easy: 0.30, medium: 0.55, hard: 0.15 };

const cfg = JSON.parse(readFileSync(new URL("../../live_upsc_config.json", import.meta.url), "utf8"));
const want = process.argv[2] ? Number(process.argv[2]) : null;
for (const t of LEVEL1.filter((x) => !want || x.no === want)) {
  const config = { ...cfg, difficultyWeights: { ...cfg.difficultyWeights, [t.subject]: FOUNDATION } };
  const cells = buildCells({ blueprint: { examCategory: "upsc", patternType: "sectional", questionCount: 100,
    subjectScope: { subject: t.subject } }, config, pool: [] }).filter((c) => c.n > 0);
  const roll = (k) => { const m = {}; for (const c of cells) m[c[k]] = (m[c[k]] || 0) + c.n; return m; };
  console.log(JSON.stringify({ no: t.no, subject: t.subject, bySubTopic: roll("subTopic"), byType: roll("questionType"),
    byDifficulty: roll("difficulty"), cells: cells.map((c) => [c.difficulty, c.questionType, c.subTopic, c.n]) }));
}
