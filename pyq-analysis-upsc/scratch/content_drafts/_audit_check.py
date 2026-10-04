# Depth-audit check. Usage (from content_drafts): python _audit_check.py <tN_rows.txt> <tN_pool.json> <tN_pool_kept.json> mod1 [mod2 ...]
# The last module must define TAGS for the kept rows.
import sys, re, json, io, contextlib, importlib
sys.path.insert(0, ".")
import draft_common as d
d.ROWS.clear(); d.CGS.clear()
mods = []
with contextlib.redirect_stdout(io.StringIO()):
    for name in sys.argv[4:]:
        mods.append(importlib.import_module(name))
rows = list(d.ROWS); TAGS = mods[-1].TAGS
TY = {"AR": "assertion_reason", "MCQ": "mcq", "stmt": "statement_based", "MTF": "match_the_following"}
hdr, tagged = {}, {}
for line in open(sys.argv[1], encoding="utf-8"):
    mm = re.match(r"## (\S+) \| (\w+) (\w+) \| ([^|]+) \|[^|]*(?:\| craft=(\w+))?", line)
    if mm:
        hdr[mm.group(1)] = (mm.group(2), TY[mm.group(3)], mm.group(4).strip())
        if mm.group(5): tagged[mm.group(1)] = mm.group(5)
bad = [(r["concept_group_id"], hdr.get(r["concept_group_id"]), (r["difficulty"], r["type"], r["topic"])) for r in rows if hdr.get(r["concept_group_id"]) != (r["difficulty"], r["type"], r["topic"])]
new = {r["concept_group_id"]: r["question_data"]["craft"] for r in rows}
print("rows", len(rows), "cell mismatches", bad)
allc = {**tagged, **TAGS, **new}
print("covered", len(allc), "of", len(hdr), "missing", sorted(set(hdr) - set(allc)), "extra", sorted(set(allc) - set(hdr)),
      "overlap", sorted(set(TAGS) & set(new)), sorted(set(tagged) & set(new)), sorted(set(tagged) & set(TAGS)))
def bands(mp):
    b = {}
    for c in mp.values():
        k = "analytic" if c in ("application", "inference", "linkage", "multi") else c
        b[k] = b.get(k, 0) + 1
    return b
print("bands after", bands(allc))
p = json.load(open(sys.argv[2], encoding="utf-8"))
p["rows"] = [r for r in p["rows"] if r["cg"] not in new]
json.dump(p, open(sys.argv[3], "w", encoding="utf-8"), ensure_ascii=False)
print("kept pool", len(p["rows"]))
