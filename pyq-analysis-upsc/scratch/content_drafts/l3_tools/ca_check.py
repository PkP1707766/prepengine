# Current-affairs test check (100 rows in parts a-h): subjects, difficulty, formats, key letters, crafts, the
# longest-key lint in English and Hindi, and the cue scan between rows of the paper.
# Usage: python ca_check.py <module-prefix> <concept-prefix>     e.g. python ca_check.py ca_t1 ca-t1-
import contextlib, importlib, io, json, os, re, sys
from collections import Counter
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.dirname(os.path.abspath(__file__)) + "/"
sys.path.insert(0, D); os.chdir(D)
import draft_common as d
d.write = lambda name: None
rows = []
for x in "abcdefgh":
    m = f"{sys.argv[1]}_{x}"
    if not os.path.exists(f"{D}/{m}.py"): continue
    d.ROWS.clear(); d.CGS.clear(); d._mcq_n[0] = 0
    with contextlib.redirect_stdout(io.StringIO()):
        importlib.import_module(m)
    for r in d.ROWS: r["mod"], r["subject"] = x, d.SUBJECT
    rows += list(d.ROWS)
key = lambda r: "abcd"[[o["isCorrect"] for o in r["options"]].index(True)]
print("rows", len(rows), "| subjects", dict(Counter(r["subject"] for r in rows)))
print("difficulty", dict(Counter(r["difficulty"] for r in rows)), "| types", dict(Counter(r["type"] for r in rows)))
print("keys", dict(sorted(Counter(key(r) for r in rows).items())), "| mcq keys", dict(sorted(Counter(key(r) for r in rows if r["type"] == "mcq").items())))
print("crafts", dict(Counter(r["question_data"].get("craft") for r in rows)))
def fmt(r):
    ob = [o["body"] for o in r["options"]]
    if r["type"] == "assertion_reason":
        return "SI3" if r["question_data"].get("reason_2") else "SI"
    if r["type"] == "match_the_following":
        return "match-code" if re.match(r"A-\d", ob[0]) else "pairs-count"
    if r["type"] == "mcq":
        return "chronology" if r["question_data"].get("statements") else ("mcq-negative" if " NOT " in r["body"] else "mcq")
    if len(r["question_data"].get("statements", [])) == 2:
        return "two-stmt"
    return "count" if ob[0] == "Only one" else "combo"
# The 2026 GS paper: combination codes in most multi-statement items, about six counts, about ten List-I/List-II
# matches, about five negative items and three statement-relationship items.
print("formats", dict(Counter(fmt(r) for r in rows)))
print("ladder answers", dict(Counter(r["options"][[o["isCorrect"] for o in r["options"]].index(True)]["body"] for r in rows if r["type"] != "mcq")))
seq = "".join(key(r) for r in rows)
print("longest run of one key in module order:", max(len(m.group(0)) for m in re.finditer(r"(.)\1*", seq)))
for r in rows:
    if r["type"] == "mcq" and not r["question_data"].get("statements"):
        for lang, f in (("en", "body"), ("hi", "body_hi")):
            L = [len(o.get(f) or "") for o in r["options"]]; k = [o["isCorrect"] for o in r["options"]].index(True)
            if max(L) > 12 and L[k] > max(l for i, l in enumerate(L) if i != k): print("  LONGEST KEY", lang, r["concept_group_id"])
if os.path.exists(f"{D}/{sys.argv[1]}_format.py"):
    plan = importlib.import_module(f"{sys.argv[1]}_format")
    stray = (set(plan.FORMAT) | set(plan.POS)) - {r["concept_group_id"] for r in rows}
    assert not stray, f"format plan names rows that do not exist: {sorted(stray)}"
print("distinct cgs", len({r["concept_group_id"] for r in rows}), f"| all {sys.argv[2]}:", all(r["concept_group_id"].startswith(sys.argv[2]) for r in rows))
print("ca_window", dict(Counter(r["question_data"].get("ca_window") for r in rows)))
from polity_common import C3, C4, T2, P4, P3, SI, SI3
LAD = set(C3 + C4 + T2 + P4 + P3 + SI + SI3)
CODEISH = re.compile(r"[\d, ]+(and \d+)?( only)?|[A-D]-\d(, [A-D]-\d)*|\d(-\d)+")
def vis(r):
    qd = r["question_data"]; parts = [r["body"]]
    for k in ("statements", "list_1", "list_2"): parts += qd.get(k) or []
    parts += [qd.get(k) or "" for k in ("assertion", "reason", "reason_2")]
    parts += [o["body"] for o in r["options"] if o["body"] not in LAD and not CODEISH.fullmatch(o["body"])]
    return parts
STOP = set("the a an of to in on and or for by with as at from is are was were be its it this that which not no only all any following statements consider correct above how many pairs india indian 2025 2026 under".split())
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
            print(f"{shs[i][0]} <> {shs[j][0]} [{len(common)}] '{k}'")
print("cue pairs flagged:", n)
# PYQ scan: rows sharing several rare two-word phrases with a 2024-2026 PYQ (its options, notes and linkages included)
import glob
blocks = []
for f in glob.glob(os.path.join(D, "..", "*_qs_2023_2026.txt")):
    for b in re.split(r"\n=====\s", io.open(f, encoding="utf-8").read()):
        m = re.match(r"(\d{4}) Q(\d+)[^\n]*?\]\s*([^\n=]*)", b)
        if m and m.group(1) in ("2024", "2025", "2026"):
            blocks.append((f"{m.group(1)} Q{m.group(2)} {m.group(3).strip()[:40]}", b.lower()))
PSTOP = STOP | set("has have their per cent central government state governments".split())
def ph(t):
    w = [x for x in re.findall(r"[a-z0-9']+", t.lower()) if x not in PSTOP and len(x) > 2]
    return {" ".join(w[i:i + 2]) for i in range(len(w) - 1)}
df = Counter(p for _, b in blocks for p in ph(b))
hits = 0
for r in rows:
    ps = {p for p in ph(" ".join(vis(r))) if df[p] <= 3}
    best = sorted(((len([p for p in ps if p in b]), name) for name, b in blocks), reverse=True)[:1]
    if best and best[0][0] >= 4:
        hits += 1
        print(f"  PYQ? {r['concept_group_id']} ~ {best[0][1]} ({best[0][0]} phrases) -- read both")
print("PYQ look-alikes flagged:", hits)
json.dump(rows, io.open(S + f"_data/{sys.argv[1]}_rows.json", "w", encoding="utf-8"), ensure_ascii=False)
