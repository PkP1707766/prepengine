# -*- coding: utf-8 -*-
"""List every text-MCQ lint failure in a CSAT paper's modules at once (csat_common.T stops at the first one).

  python l3_tools/csat_lint_all.py csat-l3-t01 csat_l3_t01_qa csat_l3_t01_lr csat_l3_t01_rc     (from content_drafts/)

Reports each item whose key is the longest option in English or Hindi, and any other assertion T() raises."""
import os, sys, importlib
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import csat_common as c
c.SET = sys.argv[1]
orig = c.T
bad = []
def T(subj, topic, diff, body, body_hi, opts, opts_hi, ans, expl, expl_hi, cg, **kw):
    lens = [len(x) for x in opts]; lh = [len(x) for x in opts_hi]
    if lens[ans] > max(l for i, l in enumerate(lens) if i != ans):
        bad.append((cg, "en", lens[ans], max(l for i, l in enumerate(lens) if i != ans)))
    if max(lens + lh) > 12 and lh[ans] > max(l for i, l in enumerate(lh) if i != ans):
        bad.append((cg, "hi", lh[ans], max(l for i, l in enumerate(lh) if i != ans)))
    try:
        orig(subj, topic, diff, body, body_hi, opts, opts_hi, ans, expl, expl_hi, cg, **kw)
    except AssertionError as e:
        if "longest" not in str(e):
            bad.append((cg, "other", str(e), ""))
c.T = T
for m in sys.argv[2:]:
    try:
        importlib.import_module(m)
    except AssertionError as e:
        print("STOPPED in", m, ":", e)
for b in bad:
    print(*b)
print(len(bad), "problems")
