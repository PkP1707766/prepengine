"""List every MCQ in a batch whose correct option is the longest (draft_common.M refuses
these one at a time; this reports them all at once). Usage: python _mcq_len_scan.py <batch.py>"""
import sys, runpy, draft_common as d
bad, orig = [], d.M
def M(topic, diff, body, body_hi, opts, opts_hi, ans, *a, **k):
    lens = [len(x) for x in opts]
    if lens[ans] > max(l for i, l in enumerate(lens) if i != ans):
        bad.append((a[-1] if a else "?", opts[ans], [o for i, o in enumerate(opts) if i != ans]))
        return
    return orig(topic, diff, body, body_hi, opts, opts_hi, ans, *a, **k)
d.M = M
runpy.run_path(sys.argv[1], run_name="scan")
for cg, key, rest in bad:
    print(cg, "|", key, "|", rest)
print(len(bad), "longest-correct MCQs")
