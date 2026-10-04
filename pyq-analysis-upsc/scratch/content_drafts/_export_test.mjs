// Export one Level-2 test's rows for the depth audit (docs/upsc-question-design-standard.md §6).
//   node _export_test.mjs <test no> <out dir>
// Writes <out>/t<no>_rows.txt (compact, one block per row: id, cell, craft, stem, items, options with the
// key starred, explanation head) and <out>/t<no>_pool.json (the {rows:[{cg,qd,body,options}]} shape
// _cue_scan.py reads). Uses the signed-in Supabase CLI.
import { execFileSync } from "node:child_process";
import { writeFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import { LEVEL2 } from "../../../upsc_level2_targets.mjs";

const no = Number(process.argv[2]);
const out = process.argv[3];
const t = LEVEL2.find((x) => x.no === no);
if (!t || !t.subs) throw new Error("unknown test or no sub-topic scope");
mkdirSync(out, { recursive: true });
const q = (s) => "'" + s.replace(/'/g, "''") + "'";
const sql = `select concept_group_id cg, topic, type, difficulty, status, body, question_data qd, options, explanation
  from public.questions where exam_category='upsc' and subject=${q(t.subject)} and topic in (${t.subs.map(q).join(",")})
  order by topic, type, difficulty, concept_group_id;`;
const f = join(out, `t${no}.sql`);
writeFileSync(f, sql);
const cli = join(process.env.LOCALAPPDATA, "npm-cache/_npx/aa8e5c70f9d8d161/node_modules/.bin/supabase.cmd");
const raw = execFileSync(cli, ["db", "query", "--linked", "--project-ref", "jcdlgfpaoebsapjaqzah", "-o", "json", "-f", f],
  { encoding: "utf8", maxBuffer: 1 << 28, stdio: ["ignore", "pipe", "ignore"], shell: true });
const rows = JSON.parse(raw.slice(raw.indexOf("{"))).rows;
writeFileSync(join(out, `t${no}_pool.json`), JSON.stringify({ rows: rows.map((r) => ({ cg: r.cg, qd: r.qd, body: r.body, options: r.options })) }));
const T = { statement_based: "stmt", mcq: "MCQ", match_the_following: "MTF", assertion_reason: "AR" };
const lines = [];
for (const r of rows) {
  const qd = r.qd || {};
  lines.push(`## ${r.cg} | ${r.difficulty} ${T[r.type] || r.type} | ${r.topic} | ${r.status}${qd.craft ? " | craft=" + qd.craft : ""}`);
  lines.push(`Q: ${r.body}`);
  (qd.statements || []).forEach((s, i) => lines.push(`  ${i + 1}. ${s}`));
  if (qd.list_1) qd.list_1.forEach((a, i) => lines.push(`  ${a} : ${qd.list_2[i]}`));
  if (qd.assertion) { lines.push(`  I: ${qd.assertion}`); lines.push(`  II: ${qd.reason}`); if (qd.reason_2) lines.push(`  III: ${qd.reason_2}`); }
  if (qd.closing && !/How many of the above statements|Which of the statements given above/.test(qd.closing)) lines.push(`  [${qd.closing}]`);
  const key = (r.options || []).find((o) => o.isCorrect);
  const opts = (r.options || []).map((o) => (o.isCorrect ? "*" : "") + o.body);
  lines.push(r.type === "assertion_reason" ? `  key: ${"abcd"[(r.options || []).indexOf(key)]}` : `  opts: ${opts.join(" | ")}`);
  lines.push(`  E: ${(r.explanation || "").slice(0, 260)}`);
  lines.push("");
}
writeFileSync(join(out, `t${no}_rows.txt`), lines.join("\n"));
console.log(`Test ${no}: ${rows.length} rows (${rows.filter((r) => (r.qd || {}).craft).length} already tagged) -> ${out}`);
