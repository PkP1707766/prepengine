# -*- coding: utf-8 -*-
"""Two Test 9 rows rewritten in place after a cross-check against the whole bank:
- the Bergmann row also tested Allen's rule, which env-arctic-fox-allens-rule (same test)
  already cues; its third statement is now about polar blubber;
- the fruit-bat row repeated the WPA-2022 vermin fact of env-wpa-2022-schedules and leant on
  echolocation (env-echolocation); it now tests the Nipah link and true flight.
The UPDATE is generated from env_l2_t9_fauna.py, so the source file stays the truth."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import env_l2_t9_fauna  # noqa: F401  (building the module fills draft_common.ROWS)
from draft_common import ROWS
from bilingual import sql_q

RENAMED = {"env-bergmann-rule-adaptations": "env-bergmann-allen-rules", "env-fruit-bats-nipah": "env-fruit-bats-vermin"}
out = []
for r in ROWS:
    if r["concept_group_id"] in RENAMED:
        out.append("update public.questions set "
                   f"body = {sql_q(r['body'])}, body_hi = {sql_q(r['body_hi'])}, "
                   f"question_data = {sql_q(json.dumps(r['question_data'], ensure_ascii=False))}::jsonb, "
                   f"options = {sql_q(json.dumps(r['options'], ensure_ascii=False))}::jsonb, "
                   f"explanation = {sql_q(r['explanation'])}, explanation_hi = {sql_q(r['explanation_hi'])}, "
                   f"source_citation = {sql_q(r['source_citation'])}, concept_group_id = {sql_q(r['concept_group_id'])}, updated_at = now() "
                   f"where exam_category = 'upsc' and status = 'draft' and concept_group_id = {sql_q(RENAMED[r['concept_group_id']])};")
assert len(out) == 2
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "env_l2_t9_crosscue_fix.sql"), "w", encoding="utf-8").write(
    "begin;\n" + "\n".join(out) + "\ncommit;\nselect concept_group_id, status from public.questions where concept_group_id in "
    "('env-bergmann-rule-adaptations','env-fruit-bats-nipah','env-bergmann-allen-rules','env-fruit-bats-vermin');\n")
print("2 updates written")
