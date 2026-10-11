// Cell targets (difficulty x type x sub-topic) for Level-2 GS Tests 1-20, from the app's own
// buildCells() against the live config -- the mix a 100-question sectional paper should have.
// Run from the repo root: node pyq-analysis-upsc/scratch/upsc_l2_cell_targets.mjs > targets.json
import { readFileSync } from "node:fs";
import { buildCells } from "../../src/lib/generate.js";
import { LEVEL2, PAPER } from "../../upsc_level2_targets.mjs";

const cfg = JSON.parse(readFileSync(new URL("../../live_upsc_config.json", import.meta.url), "utf8"));
const out = {};
for (const t of LEVEL2.filter((x) => x.subs)) {
  const cells = buildCells({ blueprint: { examCategory: "upsc", patternType: "sectional", questionCount: PAPER,
    subjectScope: { subject: t.subject, sub_topics: t.subs } }, config: cfg, pool: [] });
  out[t.no] = cells.filter((c) => c.n > 0).map((c) => ({ difficulty: c.difficulty, type: c.questionType, topic: c.subTopic, n: c.n }));
}
console.log(JSON.stringify(out));
