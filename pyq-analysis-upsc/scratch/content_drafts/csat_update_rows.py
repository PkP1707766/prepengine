# -*- coding: utf-8 -*-
"""Re-sync chosen CSAT rows in the database with their source after a correction.

  PYTHONIOENCODING=utf-8 python csat_update_rows.py <NN> <out.sql> <concept_group_id> [...]

Runs csat_l2_tNN_build.py exactly as the build does (without writing its INSERT), then writes one UPDATE per
named row for its text fields -- body, body_hi, question_data, options, explanation, explanation_hi. Only
rows still in 'draft' are touched; a published row is left alone and the UPDATE returns nothing for it."""
import sys, json, runpy
import csat_common as c
from bilingual import sql_q

t, out, cgs = sys.argv[1], sys.argv[2], sys.argv[3:]
got = {}
c.write = lambda name, order: got.setdefault("order", order)
c.report = lambda order: None
runpy.run_path(f"csat_l2_t{t}_build.py")
rows = {r["concept_group_id"]: r for r in got["order"]}
missing = [g for g in cgs if g not in rows]
assert not missing, f"not in Test {t}: {missing}"
sql = []
for g in cgs:
    r = rows[g]
    sql.append("update public.questions set "
               f"body = {sql_q(r['body'])}, body_hi = {sql_q(r['body_hi'])}, "
               f"question_data = {sql_q(json.dumps(r['question_data'], ensure_ascii=False))}::jsonb, "
               f"options = {sql_q(json.dumps(r['options'], ensure_ascii=False))}::jsonb, "
               f"explanation = {sql_q(r['explanation'])}, explanation_hi = {sql_q(r['explanation_hi'])} "
               f"where concept_group_id = {sql_q(g)} and status = 'draft' returning concept_group_id;")
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(sql) + "\n")
print(f"{out}: {len(sql)} updates")
