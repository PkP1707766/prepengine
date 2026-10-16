# -*- coding: utf-8 -*-
"""Build CSAT Level 1 · Mini 2 (a 40-item, one-hour half paper) from its three sections and write one INSERT
(status 'draft').

  PYTHONIOENCODING=utf-8 python csat_l1_m02_build.py

Same plan as Mini 1 (csat_l1_m01_build.py): 17 Quant, 9 Reasoning and 14 Reading Comprehension items on five passages,
12 easy / 22 medium / 6 hard, modules written in paper order (csat_common.LAYOUT_MINI); the rows carry
question_data.csat_set = 'csat-l1-m02' and csat_order 1-40."""
import csat_common as c
c.SET = "csat-l1-m02"
import csat_l1_m02_qa, csat_l1_m02_lr, csat_l1_m02_rc  # noqa: E402,F401  (loading them builds the rows)

order = c.assemble(c.LAYOUT_MINI)
c.report(order)
keys = "".join("abcd"[[o["isCorrect"] for o in r["options"]].index(True)] for r in order)
diff = "".join(r["difficulty"][0] for r in order)
run = best = 1
for a, b in zip(keys, keys[1:]):
    run = run + 1 if a == b else 1
    best = max(best, run)
print("keys :", keys, "| longest letter run", best)
print("diff :", diff, "| hard by quarter", [diff[i:i + 10].count("h") for i in range(0, 40, 10)])
assert best <= 3 and "hhh" not in diff and diff[0] != "h"
assert {k: keys.count(k) for k in "abcd"} == {"a": 10, "b": 10, "c": 10, "d": 10}
assert (diff.count("e"), diff.count("m"), diff.count("h")) == (12, 22, 6)
c.write("csat_l1_m02.sql", order)
