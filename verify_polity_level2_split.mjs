// Pre-check for Polity's Level-2 split (build-out v2, task 1): for each of the four
// sub-topic-scoped blueprints, run the real buildCells() apportionment and compare
// every cell with the live bank, before anything is generated.
//
// Run: node verify_polity_level2_split.mjs <polity_bank.json>
//   bank = select json_agg(t) from (select difficulty, type, topic, count(*)::int n
//          from questions where exam_category='upsc' and subject='Polity' group by 1,2,3) t;
//
// Grouping: the blueprint's four suggested groups cover 10 of Polity's 12 sub-topics.
// Judicial-Verdicts (4) goes with Judiciary, and Statutory-Laws (12, questions that turn
// on a named Act) with the other law-and-institutions test, which also balances the
// sizes: 29 / 30 / 29 / 32 = the sectional's 120.
import { readFileSync } from "node:fs";
import { buildCells } from "./src/lib/generate.js";

export const POLITY_L2 = [
  { title: "Polity L2 · 1 — Constitutional Framework & Rights", subs: ["Constitutional Framework", "Fundamental Rights, DPSP & Duties"] },
  { title: "Polity L2 · 2 — Parliament & Executive", subs: ["Parliament & State Legislature", "Union & State Executive"] },
  { title: "Polity L2 · 3 — Judiciary, Bodies, Elections & Laws", subs: ["Judiciary", "Judicial-Verdicts", "Constitutional & Statutory Bodies", "Elections", "Statutory-Laws"] },
  { title: "Polity L2 · 4 — Federalism, Local Government & Governance", subs: ["Federalism & Special Provisions", "Panchayati Raj & Local Governance", "Governance"] },
];

const cfg = JSON.parse(readFileSync(new URL("./live_upsc_config.json", import.meta.url), "utf8"));
const bank = JSON.parse(readFileSync(process.argv[2], "utf8"));
const key = (d, t, s) => `${d}|${t}|${s}`;
const have = new Map(bank.map((r) => [key(r.difficulty, r.type, r.topic), r.n]));

// Each test's size = its sub-topics' share of the 120-question sectional.
const sectional = buildCells({ blueprint: { examCategory: "upsc", patternType: "sectional", questionCount: 120, subjectScope: { subject: "Polity" } }, config: cfg, pool: [] });
const bySub = {};
for (const c of sectional) bySub[c.subTopic] = (bySub[c.subTopic] || 0) + c.n;

const allSubs = POLITY_L2.flatMap((t) => t.subs);
const missing = Object.keys(cfg.subTopicWeights.Polity).filter((s) => !allSubs.includes(s));
const dup = allSubs.filter((s, i) => allSubs.indexOf(s) !== i);
console.log(`sub-topics covered: ${allSubs.length}/12   missing: ${missing.length ? missing.join(", ") : "none"}   duplicated: ${dup.length ? dup.join(", ") : "none"}`);

let total = 0, bankTotal = bank.reduce((s, r) => s + r.n, 0), shortCells = 0;
for (const t of POLITY_L2) {
  const n = t.subs.reduce((s, x) => s + (bySub[x] || 0), 0);
  total += n;
  const cells = buildCells({ blueprint: { examCategory: "upsc", patternType: "sectional", questionCount: n, subjectScope: { subject: "Polity", sub_topics: t.subs } }, config: cfg, pool: [] });
  const pool = bank.filter((r) => t.subs.includes(r.topic)).reduce((s, r) => s + r.n, 0);
  const short = cells.filter((c) => (have.get(key(c.difficulty, c.questionType, c.subTopic)) || 0) < c.n);
  shortCells += short.length;
  const roll = (k) => Object.entries(cells.reduce((m, c) => ((m[c[k]] = (m[c[k]] || 0) + c.n), m), {})).map(([a, b]) => `${b} ${a}`).join(", ");
  console.log(`\n${t.title}\n  target ${n}  cells ${cells.length} (sum ${cells.reduce((s, c) => s + c.n, 0)})  pool ${pool}`);
  console.log(`  by difficulty: ${roll("difficulty")}\n  by type:       ${roll("questionType")}\n  by sub-topic:  ${roll("subTopic")}`);
  console.log(`  cells short of an exact match: ${short.length ? short.map((c) => `${c.difficulty}/${c.questionType}/${c.subTopic} need ${c.n} have ${have.get(key(c.difficulty, c.questionType, c.subTopic)) || 0}`).join("; ") : "none"}`);
}
console.log(`\nsplit total ${total} (sectional 120)   bank ${bankTotal}   left out of every test: ${bankTotal - total}   cells short: ${shortCells}`);
