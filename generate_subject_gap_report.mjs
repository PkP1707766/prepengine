// Real per-cell drafting targets for any UPSC sectional blueprint, computed with the
// actual buildCells() apportionment from generate.js against the live
// distribution_config (pulled from the DB at run time and saved to live_upsc_config.json).
//
// Run: node generate_subject_gap_report.mjs <Subject> <questionCount> [bankCounts.json]
//   e.g. node generate_subject_gap_report.mjs Polity 120
// bankCounts.json (optional) is the live bank, straight from the DB:
//   select json_agg(t) from (select difficulty, type, topic, count(*)::int as n from questions
//   where exam_category='upsc' and subject='<Subject>' and status in ('draft','active') group by 1,2,3) t;
// With it, every cell also shows have / gap, and bank rows that fit no cell are listed as spare.
import { readFileSync } from "node:fs";
import { buildCells } from "./src/lib/generate.js";

const subject = process.argv[2];
const questionCount = Number(process.argv[3]);
const bankFile = process.argv[4];
if (!subject || !questionCount) { console.error("usage: node generate_subject_gap_report.mjs <Subject> <count>"); process.exit(1); }

const config = JSON.parse(readFileSync(new URL("./live_upsc_config.json", import.meta.url), "utf8"));
const blueprint = { examCategory: "upsc", patternType: "sectional", questionCount, subjectScope: { subject }, title: subject };
const cells = buildCells({ blueprint, config, pool: [] });

console.log(`=== ${subject} sectional (${questionCount}Q) -- real drafting targets from the live config ===`);
console.log(`config: ${config.name}`);
console.log(`type weights used:     ${JSON.stringify((config.questionTypeWeights || {})[subject] || "(none -> wildcard)")}`);
const dw = config.difficultyWeights || {};
console.log(`difficulty weights:    ${JSON.stringify(dw[subject] && typeof dw[subject] === "object" ? dw[subject] : Object.fromEntries(Object.entries(dw).filter(([, v]) => typeof v !== "object")))}  (${dw[subject] && typeof dw[subject] === "object" ? "per-subject override" : "global"})`);
console.log(`sub-topic weights:     ${JSON.stringify((config.subTopicWeights || {})[subject])}\n`);
const bank = bankFile ? JSON.parse(readFileSync(bankFile, "utf8")) : null;
const cellKey = (d, t, s) => `${d}|${t}|${s}`;
const have = new Map();
if (bank) for (const r of bank) have.set(cellKey(r.difficulty, r.type, r.topic), (have.get(cellKey(r.difficulty, r.type, r.topic)) || 0) + r.n);
const sorted = [...cells].sort((a, b) => b.n - a.n);
console.log(`row |   n |${bank ? " have | gap |" : ""} difficulty | type                 | sub-topic`);
console.log("-".repeat(bank ? 83 : 70));
sorted.forEach((c, i) => {
  const h = have.get(cellKey(c.difficulty, c.questionType, c.subTopic)) || 0;
  const cols = bank ? ` ${String(h).padStart(4)} | ${String(Math.max(0, c.n - h)).padStart(3)} |` : "";
  console.log(`${String(i + 1).padStart(3)} | ${String(c.n).padStart(3)} |${cols} ${c.difficulty.padEnd(10)} | ${String(c.questionType).padEnd(20)} | ${c.subTopic}`);
});
const total = cells.reduce((s, c) => s + c.n, 0);
console.log("-".repeat(bank ? 83 : 70));
console.log(`cells: ${cells.length}   TOTAL: ${total} (blueprint target ${questionCount})`);
if (bank) {
  const inCell = new Set(cells.map((c) => cellKey(c.difficulty, c.questionType, c.subTopic)));
  const gap = cells.reduce((s, c) => s + Math.max(0, c.n - (have.get(cellKey(c.difficulty, c.questionType, c.subTopic)) || 0)), 0);
  const filledCells = cells.filter((c) => (have.get(cellKey(c.difficulty, c.questionType, c.subTopic)) || 0) >= c.n).length;
  const bankTotal = bank.reduce((s, r) => s + r.n, 0);
  const surplus = cells.reduce((s, c) => s + Math.max(0, (have.get(cellKey(c.difficulty, c.questionType, c.subTopic)) || 0) - c.n), 0);
  const offGrid = bank.filter((r) => !inCell.has(cellKey(r.difficulty, r.type, r.topic)));
  console.log(`bank: ${bankTotal} rows   cells filled: ${filledCells}/${cells.length}   questions still to draft: ${gap}`);
  console.log(`spare rows: ${surplus} above target in a cell + ${offGrid.reduce((s, r) => s + r.n, 0)} in no cell` +
    (offGrid.length ? `  (${offGrid.map((r) => `${r.n} ${r.difficulty}/${r.type}/${r.topic}`).join("; ")})` : ""));
}
const roll = (key) => { const m = {}; for (const c of cells) m[c[key]] = (m[c[key]] || 0) + c.n; return Object.entries(m).sort((a, b) => b[1] - a[1]).map(([k, v]) => `${v} ${k}`).join("  |  "); };
console.log(`\nby sub-topic:  ${roll("subTopic")}`);
console.log(`by type:       ${roll("questionType")}`);
console.log(`by difficulty: ${roll("difficulty")}`);
