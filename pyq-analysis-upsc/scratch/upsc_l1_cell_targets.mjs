// Cell targets (difficulty x type x sub-topic) for the Level-1 NCERT Foundation GS papers (100 questions each).
// Tests 1-6 are subject papers: sub-topic and question-type shares come from the live PYQ-derived config, as
// for Level 2; difficulty uses a foundation mix (30 / 55 / 15) instead of the subject's exam mix, because
// Level 1 builds the base before the exam-level sectionals.
// Test 7, the GS Foundation Revision, is a full-syllabus paper. Its subject shares are the engine's full-length
// GS mix with the current-affairs slots (Level 1 has none; it is NCERT-based) shared out among the six static
// subjects in proportion; within each subject, the cells are that subject's sectional mix at that size.
// Run from the repo root: node pyq-analysis-upsc/scratch/upsc_l1_cell_targets.mjs [test no]
import { readFileSync } from "node:fs";
import { buildCells } from "../../src/lib/generate.js";

export const LEVEL1 = [
  { no: 1, subject: "Polity" }, { no: 2, subject: "History" }, { no: 3, subject: "Environment & Ecology" },
  { no: 4, subject: "Geography" }, { no: 5, subject: "Economy" }, { no: 6, subject: "Science & Technology" },
];
export const FOUNDATION = { easy: 0.30, medium: 0.55, hard: 0.15 };
const STATIC = LEVEL1.map((t) => t.subject);

const cfg = JSON.parse(readFileSync(new URL("../../live_upsc_config.json", import.meta.url), "utf8"));
const foundation = (subjects) => {
  const dw = { ...cfg.difficultyWeights };
  for (const s of subjects) dw[s] = FOUNDATION;
  return { ...cfg, difficultyWeights: dw };
};
const sectional = (subject, n) => buildCells({ blueprint: { examCategory: "upsc", patternType: "sectional", questionCount: n,
  subjectScope: { subject } }, config: foundation([subject]), pool: [] }).filter((c) => c.n > 0);

// Test 7: the full-length subject shares without current affairs, scaled to 100 by largest remainder.
function revisionShares() {
  const full = buildCells({ blueprint: { examCategory: "upsc", patternType: "full_length", questionCount: 100, subjectScope: {} },
    config: foundation(STATIC), pool: [] }).filter((c) => c.n > 0);
  const raw = {}; for (const c of full) if (STATIC.includes(c.subject)) raw[c.subject] = (raw[c.subject] || 0) + c.n;
  const total = Object.values(raw).reduce((a, b) => a + b, 0);
  const exact = STATIC.map((s) => [s, (raw[s] || 0) * 100 / total]);
  const share = Object.fromEntries(exact.map(([s, x]) => [s, Math.floor(x)]));
  let left = 100 - Object.values(share).reduce((a, b) => a + b, 0);
  for (const [s] of exact.sort((a, b) => (b[1] % 1) - (a[1] % 1))) { if (left-- <= 0) break; share[s] += 1; }
  return share;
}

const want = process.argv[2] ? Number(process.argv[2]) : null;
const papers = [...LEVEL1.map((t) => ({ ...t, parts: { [t.subject]: 100 } })),
                { no: 7, subject: "GS Foundation Revision", parts: revisionShares() }];
for (const t of papers.filter((x) => !want || x.no === want)) {
  const cells = Object.entries(t.parts).flatMap(([s, n]) => sectional(s, n).map((c) => ({ ...c, subject: s })));
  const roll = (k) => { const m = {}; for (const c of cells) m[c[k]] = (m[c[k]] || 0) + c.n; return m; };
  console.log(JSON.stringify({ no: t.no, subject: t.subject, ...(t.no === 7 ? { bySubject: t.parts } : {}),
    bySubTopic: roll("subTopic"), byType: roll("questionType"), byDifficulty: roll("difficulty"),
    cells: cells.map((c) => [c.difficulty, c.questionType, c.subTopic, c.n]) }));
}
