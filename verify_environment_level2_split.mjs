// Pre-check for Environment's Level-2 split (build-out v2, task 2): for each of the three
// sub-topic-scoped blueprints, run the real buildCells() apportionment and compare every
// cell with the live bank, before anything is generated.
//
// Run: node verify_environment_level2_split.mjs <environment_bank.json>
//   bank = select json_agg(t) from (select difficulty, type, topic, count(*)::int n from questions
//          where exam_category='upsc' and subject='Environment & Ecology' group by 1,2,3) t;
//
// Grouping follows the blueprint's three Environment tests. Pollution sits with climate, as
// ruled on 2026-09-27. Disaster Management has no share yet (it waits on Geography's re-tag),
// so test 2 is titled for what it holds: climate change and pollution. Sizes 46 / 48 / 26 =
// the sectional's 120.
import { readFileSync } from "node:fs";
import { buildCells } from "./src/lib/generate.js";

const SUBJECT = "Environment & Ecology";
export const ENVIRONMENT_L2 = [
  { title: "Environment L2 · 1 — Ecology & Biodiversity", subs: ["Fauna & Animal Behaviour", "Flora, Fungi & Forests", "Ecosystems & Ecological Processes"] },
  { title: "Environment L2 · 2 — Climate Change & Pollution", subs: ["Climate Science & Mitigation", "Climate Agreements & Carbon Markets", "Pollution, Waste & Resources"] },
  { title: "Environment L2 · 3 — Policies & Conservation", subs: ["Protected Areas & Wildlife Protection", "International Conventions & Organisations", "Indian Environmental Laws & Bodies"] },
];

const cfg = JSON.parse(readFileSync(new URL("./live_upsc_config.json", import.meta.url), "utf8"));
const bank = JSON.parse(readFileSync(process.argv[2], "utf8"));
const key = (d, t, s) => `${d}|${t}|${s}`;
const have = new Map(bank.map((r) => [key(r.difficulty, r.type, r.topic), r.n]));

// Each test's size = its sub-topics' share of the 120-question sectional.
const sectional = buildCells({ blueprint: { examCategory: "upsc", patternType: "sectional", questionCount: 120, subjectScope: { subject: SUBJECT } }, config: cfg, pool: [] });
const bySub = {};
for (const c of sectional) bySub[c.subTopic] = (bySub[c.subTopic] || 0) + c.n;

const allSubs = ENVIRONMENT_L2.flatMap((t) => t.subs);
const configured = Object.keys(cfg.subTopicWeights[SUBJECT]);
const missing = configured.filter((s) => !allSubs.includes(s));
const dup = allSubs.filter((s, i) => allSubs.indexOf(s) !== i);
console.log(`sub-topics covered: ${allSubs.length}/${configured.length}   missing: ${missing.length ? missing.join(", ") : "none"}   duplicated: ${dup.length ? dup.join(", ") : "none"}`);

let total = 0, bankTotal = bank.reduce((s, r) => s + r.n, 0), shortCells = 0;
for (const t of ENVIRONMENT_L2) {
  const n = t.subs.reduce((s, x) => s + (bySub[x] || 0), 0);
  total += n;
  const cells = buildCells({ blueprint: { examCategory: "upsc", patternType: "sectional", questionCount: n, subjectScope: { subject: SUBJECT, sub_topics: t.subs } }, config: cfg, pool: [] });
  const pool = bank.filter((r) => t.subs.includes(r.topic)).reduce((s, r) => s + r.n, 0);
  const short = cells.filter((c) => (have.get(key(c.difficulty, c.questionType, c.subTopic)) || 0) < c.n);
  shortCells += short.length;
  const roll = (k) => Object.entries(cells.reduce((m, c) => ((m[c[k]] = (m[c[k]] || 0) + c.n), m), {})).map(([a, b]) => `${b} ${a}`).join(", ");
  console.log(`\n${t.title}\n  target ${n}  cells ${cells.length} (sum ${cells.reduce((s, c) => s + c.n, 0)})  pool ${pool}`);
  console.log(`  by difficulty: ${roll("difficulty")}\n  by type:       ${roll("questionType")}\n  by sub-topic:  ${roll("subTopic")}`);
  console.log(`  cells short of an exact match: ${short.length ? short.map((c) => `${c.difficulty}/${c.questionType}/${c.subTopic} need ${c.n} have ${have.get(key(c.difficulty, c.questionType, c.subTopic)) || 0}`).join("; ") : "none"}`);
}
console.log(`\nsplit total ${total} (sectional 120)   bank ${bankTotal}   left out of every test: ${bankTotal - total}   cells short: ${shortCells}`);
