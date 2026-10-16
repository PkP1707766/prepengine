# -*- coding: utf-8 -*-
"""Build CSAT Level 1 · Mini 1 (a 40-item, one-hour half paper) from its three sections and write one INSERT
(status 'draft').

  PYTHONIOENCODING=utf-8 python csat_l1_m01_build.py

The half paper keeps Level 2's CSAT mix at half the length -- 17 Quant (one in the data-sufficiency block), 9 Reasoning
(one in the block) and 14 Reading Comprehension items on five passages -- at the foundation level (12 easy / 22 medium /
6 hard). Every Quant and Reasoning key is re-derived in code while the sections load. The modules are written in the
order the items take on the paper (csat_common.LAYOUT_MINI), so no interleaving is needed; the rows carry
question_data.csat_set = 'csat-l1-m01' and csat_order 1-40, and the test is assembled in that order with question
shuffling off."""
import csat_common as c
c.SET = "csat-l1-m01"
import csat_l1_m01_qa, csat_l1_m01_lr, csat_l1_m01_rc  # noqa: E402,F401  (loading them builds the rows)

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
c.write("csat_l1_m01.sql", order)
