// Per-test drafting targets for one Level-2 UPSC test at the real 100-question format:
// runs the real buildCells() apportionment for the test's sub-topic scope against the
// live config, and compares every (difficulty, type, sub-topic) cell with the live bank.
// Run: node upsc_test_gap_report.mjs <test no> <bank_cells.json>
// bank_cells.json: a fresh export of the live bank, every UPSC subject, e.g. with the signed-in CLI:
//   select subject, topic, type, difficulty, count(*)::int as n from public.questions
//   where exam_category='upsc' and status in ('draft','published') group by 1,2,3,4;
// (rows of the other subjects are ignored). Export again before each drafting round.
import { readFileSync } from "node:fs";
import { buildCells } from "./src/lib/generate.js";
import { LEVEL2, PAPER } from "./upsc_level2_targets.mjs";

const no = Number(process.argv[2]);
const t = LEVEL2.find((x) => x.no === no);
if (!t || !t.subs) { console.error("unknown test or no sub-topic scope yet"); process.exit(1); }
const cfg = JSON.parse(readFileSync(new URL("./live_upsc_config.json", import.meta.url), "utf8"));
const bank = JSON.parse(readFileSync(process.argv[3], "utf8")).filter((r) => (!r.subject || r.subject === t.subject) && t.subs.includes(r.topic));
const cells = buildCells({ blueprint: { examCategory: "upsc", patternType: "sectional", questionCount: PAPER, subjectScope: { subject: t.subject, sub_topics: t.subs } }, config: cfg, pool: [] });
const key = (d, ty, s) => `${d}|${ty}|${s}`;
const have = new Map(bank.map((r) => [key(r.difficulty, r.type, r.topic), r.n]));
console.log(`=== Level 2 · Test ${t.no} -- ${t.title} (${PAPER} Q) ===`);
console.log(`row |   n | have | gap | difficulty | type                 | sub-topic`);
let gap = 0;
[...cells].sort((a, b) => b.n - a.n).forEach((c, i) => {
  const h = have.get(key(c.difficulty, c.questionType, c.subTopic)) || 0;
  gap += Math.max(0, c.n - h);
  console.log(`${String(i + 1).padStart(3)} | ${String(c.n).padStart(3)} | ${String(h).padStart(4)} | ${String(Math.max(0, c.n - h)).padStart(3)} | ${c.difficulty.padEnd(10)} | ${c.questionType.padEnd(20)} | ${c.subTopic}`);
});
const inCell = new Set(cells.map((c) => key(c.difficulty, c.questionType, c.subTopic)));
const surplus = cells.reduce((s, c) => s + Math.max(0, (have.get(key(c.difficulty, c.questionType, c.subTopic)) || 0) - c.n), 0);
const off = bank.filter((r) => !inCell.has(key(r.difficulty, r.type, r.topic)));
console.log(`\nquestions still to draft: ${gap}   spare in the bank: ${surplus} above cell targets + ${off.reduce((s, r) => s + r.n, 0)} in no cell` + (off.length ? ` (${off.map((r) => `${r.n} ${r.difficulty}/${r.type}/${r.topic}`).join("; ")})` : ""));
const roll = (k) => { const m = {}; for (const c of cells) m[c[k]] = (m[c[k]] || 0) + c.n; return Object.entries(m).map(([a, b]) => `${b} ${a}`).join(" | "); };
console.log(`by sub-topic: ${roll("subTopic")}\nby type: ${roll("questionType")}\nby difficulty: ${roll("difficulty")}`);
