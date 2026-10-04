# Flag pairs of rows in one test pool that share a distinctive phrase (>= N-word shingle,
# stop-words ignored), so each can be read for a cross-question cue.
import json, re, runpy, sys, os
sys.path.insert(0, os.getcwd())
import draft_common as d
d.write = lambda name: None
for f in sys.argv[2:]:
    d.REQUIRE_CRAFT = False   # a batch opts in for itself; do not leak it into the next file
    runpy.run_path(f, run_name="scan")
pool = json.load(open(sys.argv[1], encoding="utf-8"))["rows"]
def vis(qd, body, options):
    parts = [body or ""]
    for k in ("statements", "list_1", "list_2"):
        parts += qd.get(k) or []
    for k in ("assertion", "reason", "reason_2"):
        if qd.get(k): parts.append(qd[k])
    from polity_common import C3, C4, T2, P4, P3, SI, SI3
    ladder = set(C3 + C4 + T2 + P4 + P3 + SI + SI3)
    parts += [o["body"] for o in options if o["body"] not in ladder]
    return parts
rows = [(r["cg"], "old", vis(r["qd"] or {}, r["body"], r["options"])) for r in pool]
rows += [(r["concept_group_id"], "new", vis(r["question_data"], r["body"], r["options"])) for r in d.ROWS]
STOP = set("the a an of and or to in on for by with as is are was were be its it this that which from at under their his her any all not no only can may shall has have had been also following statements consider about regarding india indian constitution article articles supreme court held directive principles state policy fundamental rights right amendment act parliament legislature legislatures president case states union bill law laws".split())
N = 3
def shingles(texts):
    out = {}
    for t in texts:
        w = [x for x in re.findall(r"[a-z0-9()']+", t.lower()) if x not in STOP]
        for i in range(len(w) - N + 1):
            out.setdefault(" ".join(w[i:i+N]), t)
    return out
sh = [(cg, src, shingles(v)) for cg, src, v in rows]
seen = set()
for i in range(len(sh)):
    for j in range(i + 1, len(sh)):
        a, b = sh[i], sh[j]
        if a[1] == "old" and b[1] == "old":
            continue
        common = set(a[2]) & set(b[2])
        if common:
            k = sorted(common)[0]
            print(f"{a[0]} <> {b[0]}  [{len(common)}] e.g. '{k}'\n    A: {a[2][k][:150]}\n    B: {b[2][k][:150]}")
