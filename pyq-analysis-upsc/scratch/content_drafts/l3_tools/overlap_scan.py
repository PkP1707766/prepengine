# Overlap scan for a Level 3 paper against the whole UPSC bank (bank_dump.json, explanations included).
# For each new row, take its distinctive 2-3 word phrases (from stem, statements, pairs and options), drop phrases
# common across the bank, and list bank rows that share several of them.
# Usage: python overlap_scan.py <N> <module-prefix> [min_shared]
# First refresh the dump: run bank_dump.sql with the Supabase CLI (-o json) and save its rows to _data/bank_dump.json.
import contextlib, importlib, io, json, os, re, sys
from collections import Counter, defaultdict
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D); os.chdir(D)
import draft_common as d
d.write = lambda name: None
rows = []
for x in "abcdefgh":
    m = f"{sys.argv[2]}_{x}"
    if not os.path.exists(f"{D}/{m}.py"): continue
    d.ROWS.clear(); d.CGS.clear(); d._mcq_n[0] = 0
    with contextlib.redirect_stdout(io.StringIO()):
        importlib.import_module(m)
    rows += list(d.ROWS)
bank = json.load(io.open(os.path.join(S, "_data", "bank_dump.json"), encoding="utf-8"))
btxt = [(b["cg"], b["txt"].lower()) for b in bank]
STOP = set("""a an the of to in on and or for by with as at from is are was were be been it its this that these those which who whom
whose not no only all any each both one two three four five than then there their they them he she his her i we our you your
under over into after before about between above below during more most less least such other another same can may must
should would could will shall has have had do does did following statements statement consider correct given above code select
using pairs pair how many matched what which one india india's indian government""".split())
def phrases(text):
    w = re.findall(r"[A-Za-z][A-Za-z\-']+|\d[\d.,]*", text)
    out = set()
    for n in (2, 3):
        for i in range(len(w) - n + 1):
            g = w[i:i + n]
            if sum(1 for t in g if t.lower() in STOP) > n - 2: continue
            if any(len(t) < 3 and not t[0].isdigit() for t in g): continue
            out.add(" ".join(g).lower())
    return out
doc_freq = Counter()
cache = {}
allp = set()
for r in rows:
    qd = r["question_data"]
    t = " ".join([r["body"]] + [str(x) for x in qd.get("statements", [])] + [qd.get(k, "") for k in ("assertion", "reason", "reason_2")]
                 + [str(x) for x in qd.get("list_1", []) + qd.get("list_2", [])] + [o["body"] for o in r["options"]])
    cache[r["concept_group_id"]] = phrases(t)
    allp |= cache[r["concept_group_id"]]
for p in allp:
    doc_freq[p] = sum(1 for _, bt in btxt if p in bt)
minshared = int(sys.argv[3]) if len(sys.argv) > 3 else 3
flag = 0
for cg, ps in cache.items():
    rare = {p for p in ps if 0 < doc_freq[p] <= 25}
    hits = defaultdict(set)
    for p in rare:
        for bcg, bt in btxt:
            if bcg != cg and p in bt: hits[bcg].add(p)
    top = sorted(((len(v), k, v) for k, v in hits.items() if len(v) >= minshared), reverse=True)[:3]
    if top:
        flag += 1
        print(f"\n{cg}")
        for n, k, v in top: print(f"   {n:2d} {k}: {sorted(v)[:8]}")
print(f"\nrows {len(rows)} | flagged {flag}")
