// Real per-cell drafting targets for any UPSC sectional blueprint, computed with the
// actual buildCells() apportionment from generate.js against the live
// distribution_config (pulled from the DB at run time and saved to live_upsc_config.json).
//
// Run: node generate_subject_gap_report.mjs <Subject> <questionCount> <bankCountsJson?>
//   e.g. node generate_subject_gap_report.mjs Polity 120
import { readFileSync } from "node:fs";
import { buildCells } from "./src/lib/generate.js";

const subject = process.argv[2];
const questionCount = Number(process.argv[3]);
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
const sorted = [...cells].sort((a, b) => b.n - a.n);
console.log("row |   n | difficulty | type                 | sub-topic");
console.log("-".repeat(70));
sorted.forEach((c, i) => console.log(`${String(i + 1).padStart(3)} | ${String(c.n).padStart(3)} | ${c.difficulty.padEnd(10)} | ${String(c.questionType).padEnd(20)} | ${c.subTopic}`));
const total = cells.reduce((s, c) => s + c.n, 0);
console.log("-".repeat(70));
console.log(`cells: ${cells.length}   TOTAL: ${total} (blueprint target ${questionCount})`);
const roll = (key) => { const m = {}; for (const c of cells) m[c[key]] = (m[c[key]] || 0) + c.n; return Object.entries(m).sort((a, b) => b[1] - a[1]).map(([k, v]) => `${v} ${k}`).join("  |  "); };
console.log(`\nby sub-topic:  ${roll("subTopic")}`);
console.log(`by type:       ${roll("questionType")}`);
console.log(`by difficulty: ${roll("difficulty")}`);
