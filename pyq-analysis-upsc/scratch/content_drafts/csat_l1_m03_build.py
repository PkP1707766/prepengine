# -*- coding: utf-8 -*-
"""Build CSAT Level 1 · Mini 3 (a 40-item, one-hour half paper) from its three sections and write one INSERT
(status 'draft').

  PYTHONIOENCODING=utf-8 python csat_l1_m03_build.py

Same plan as Minis 1-2, except that this mini's Reasoning share includes two data-sufficiency items: its layout is
csat_common.LAYOUT_MINI with a second 'DL' slot in the data-sufficiency block and one fewer 'L' slot (the one after the
fifth passage), so the paper still has 40 items. The rows carry question_data.csat_set = 'csat-l1-m03' and
csat_order 1-40."""
import csat_common as c
c.SET = "csat-l1-m03"
import csat_l1_m03_qa, csat_l1_m03_lr, csat_l1_m03_rc  # noqa: E402,F401  (loading them builds the rows)

layout = list(c.LAYOUT_MINI)
layout.insert(layout.index("DL") + 1, "DL")
last_r = max(i for i, s in enumerate(layout) if s.startswith("R"))
assert layout[last_r + 1] == "L"
del layout[last_r + 1]
order = c.assemble(layout)
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
c.write("csat_l1_m03.sql", order)
