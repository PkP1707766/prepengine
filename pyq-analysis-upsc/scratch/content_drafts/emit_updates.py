# -*- coding: utf-8 -*-
"""Emit UPDATE statements (question_data, options, explanation, body) for chosen concept_group_ids,
from the records JSON that each batch script writes. Usage: python emit_updates.py out.sql cg1 cg2 ..."""
import json, sys, glob
from polity_common import q
recs = {}
for f in glob.glob("polity_batch*_insert_records.json"):
    for r in json.load(open(f, encoding="utf-8")):
        recs[r["cg"]] = r
out, cgs = sys.argv[1], sys.argv[2:]
parts = []
for cg in cgs:
    r = recs[cg]
    parts.append("update public.questions set body=" + q(r["body"]) + ", question_data=" + q(json.dumps(r["question_data"], ensure_ascii=False))
                 + "::jsonb, options=" + q(json.dumps(r["options"], ensure_ascii=False)) + "::jsonb, explanation=" + q(r["explanation"])
                 + " where exam_category='upsc' and subject='Polity' and concept_group_id=" + q(cg) + " returning concept_group_id")
sql = "with " + ", ".join(f"u{i} as ({p})" for i, p in enumerate(parts)) + "\nselect count(*) as updated from (" + " union all ".join(f"select * from u{i}" for i in range(len(parts))) + ") x;\n"
open(out, "w", encoding="utf-8").write(sql)
print(f"wrote {out}: {len(parts)} updates, {len(sql)} chars")
