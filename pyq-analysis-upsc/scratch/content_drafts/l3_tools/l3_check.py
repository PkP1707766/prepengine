# Level 3 Test N (static 84): combined cell tally vs targets, key letters, crafts, and the cue scan (new vs new only).
import contextlib, importlib, io, json, os, sys
from collections import Counter
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.dirname(os.path.abspath(__file__)) + "/"   # l3_targets.jsonl lives here; the bank dump in _data/
sys.path.insert(0, D); os.chdir(D)
import draft_common as d
d.write = lambda name: None
rows = []
for m in [f"{sys.argv[2]}_{x}" for x in "abcdef" if os.path.exists(f"{D}/{sys.argv[2]}_{x}.py")]:
    d.ROWS.clear(); d.CGS.clear(); d._mcq_n[0] = 0
    with contextlib.redirect_stdout(io.StringIO()):
        importlib.import_module(m)
    for r in d.ROWS: r["mod"] = m[-1]
    rows += list(d.ROWS)
tgt = None
for line in io.open(S + "l3_targets.jsonl", encoding="utf-8"):
    t = json.loads(line)
    if t["no"] == int(sys.argv[1]): tgt = Counter({(c[0], c[1], c[2]): c[3] for c in t["cells"]})
have = Counter((r["difficulty"], r["type"], r["topic"]) for r in rows)
print("rows", len(rows), "| cells match targets:", have == tgt)
for k in sorted(set(have) | set(tgt)):
    if have[k] != tgt[k]: print("  CELL", k, "have", have[k], "want", tgt[k])
keys = Counter("abcd"[[o["isCorrect"] for o in r["options"]].index(True)] for r in rows)
print("keys", dict(sorted(keys.items())), "| crafts", dict(Counter(r["question_data"].get("craft") for r in rows)))
mk = Counter("abcd"[[o["isCorrect"] for o in r["options"]].index(True)] for r in rows if r["type"] == "mcq")
print("mcq keys", dict(sorted(mk.items())), "| types", dict(Counter(r["type"] for r in rows)), "| diff", dict(Counter(r["difficulty"] for r in rows)))
for r in rows:
    if r["type"] == "mcq":
        for lang, f in (("en", "body"), ("hi", "body_hi")):
            L = [len(o.get(f) or "") for o in r["options"]]; k = [o["isCorrect"] for o in r["options"]].index(True)
            if L[k] > max(l for i, l in enumerate(L) if i != k): print("  LONGEST KEY", lang, r["concept_group_id"])
print("distinct cgs", len({r["concept_group_id"] for r in rows}), f"| all {sys.argv[3]}:", all(r["concept_group_id"].startswith(sys.argv[3]) for r in rows))
# cue scan: shared distinctive 3-word shingles between new rows (visible text only)
import re
from polity_common import C3, C4, T2, P4, P3, SI, SI3
LAD = set(C3 + C4 + T2 + P4 + P3 + SI + SI3 + ["Only two", "Only three", "Only four", "All five"])
def vis(r):
    qd = r["question_data"]; parts = [r["body"]]
    for k in ("statements", "list_1", "list_2"): parts += qd.get(k) or []
    parts += [o["body"] for o in r["options"] if o["body"] not in LAD]
    return parts
STOP = set("the a an of and or to in on for by with as is are was were be its it this that which from at their his her any all not no only can may has have had been also following statements consider about pairs above correct how many india indian century centuries period".split())
def sh(texts):
    out = {}
    for t in texts:
        w = [x for x in re.findall(r"[a-z0-9']+", t.lower()) if x not in STOP]
        for i in range(len(w) - 2): out.setdefault(" ".join(w[i:i + 3]), t)
    return out
shs = [(r["concept_group_id"], sh(vis(r))) for r in rows]
n = 0
for i in range(len(shs)):
    for j in range(i + 1, len(shs)):
        common = set(shs[i][1]) & set(shs[j][1])
        if common:
            k = sorted(common)[0]; n += 1
            print(f"{shs[i][0]} <> {shs[j][0]} [{len(common)}] '{k}'\n    A: {shs[i][1][k][:140]}\n    B: {shs[j][1][k][:140]}")
print("pairs flagged:", n)
json.dump(rows, io.open(S + f"_data/l3_t{sys.argv[1]}_rows.json", "w", encoding="utf-8"), ensure_ascii=False)
