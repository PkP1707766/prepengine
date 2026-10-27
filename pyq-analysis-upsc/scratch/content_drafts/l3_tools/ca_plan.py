# Make the answer-format plan for a current-affairs paper (writes <prefix>_format.py; see ca_common.finish).
# Usage: python ca_plan.py ca_t1 [seed]
# - Builds the parts with an empty plan, reads each statement item's truth from its explanation.
# - Multi-statement items take combination codes; items with no correct statement, and those named in KEEP_COUNT
#   inside the existing plan file, keep the 'How many' count; two-statement items keep 1 only / 2 only / Both / Neither.
# - Statements are reordered so that, across the paper, each position is true about equally often (authors tend to
#   put the true statement first), and about half the two-statement '1 only' items become '2 only'.
# - Key positions of combination codes are then chosen so the paper's letters come to 25 each; the MCQ and matching
#   positions (POS) are kept as they are in the existing plan file.
import contextlib, importlib, io, itertools, os, random, sys, types
from collections import Counter
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, D); os.chdir(D)
prefix, seed = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 2026
old = importlib.import_module(f"{prefix}_format")
KEEP_COUNT, POS = set(getattr(old, "KEEP_COUNT", ())), dict(old.POS)
sys.modules[f"{prefix}_format"] = types.SimpleNamespace(FORMAT={}, POS=POS, KEEP_COUNT=KEEP_COUNT)
import draft_common as d, ca_common as c
d.write = lambda name: None
rows = []
for x in "abcdefgh":
    m = f"{prefix}_{x}"
    if not os.path.exists(f"{D}/{m}.py"): continue
    d.ROWS.clear(); d.CGS.clear(); d._mcq_n[0] = 0
    with contextlib.redirect_stdout(io.StringIO()):
        importlib.import_module(m)
    rows += list(d.ROWS)
rng = random.Random(seed)
key = lambda r: "abcd"[[o["isCorrect"] for o in r["options"]].index(True)]
tally = Counter()                  # (n, position) -> how often the statement there is true
plan, fixed = {}, Counter()
two = [r for r in rows if r["type"] == "statement_based" and len(r["question_data"]["statements"]) == 2]
ones = [r for r in two if key(r) == "a"]
swap = set(r["concept_group_id"] for r in rng.sample(ones, len(ones) // 2))
combos = []
for r in rows:
    cg = r["concept_group_id"]
    if cg in POS:
        continue
    if r["type"] != "statement_based":
        fixed[key(r)] += 1
        continue
    st = r["question_data"]["statements"]
    t = c._truth_from_expl(r["explanation"], len(st))
    assert t is not None, f"{cg}: cannot read the truth from the explanation"
    if len(st) == 2:
        if cg in swap:
            plan[cg] = ("perm", (1, 0))
            fixed["b"] += 1
        else:
            fixed[key(r)] += 1
        continue
    if sum(t) == 0 or cg in KEEP_COUNT:
        fixed[key(r)] += 1
        continue
    perms = list(itertools.permutations(range(len(st))))
    rng.shuffle(perms)
    best = min(perms, key=lambda p: sum((tally[(len(st), i)] + t[p[i]]) ** 2 for i in range(len(st))))
    for i in range(len(st)):
        tally[(len(st), i)] += t[best[i]]
    combos.append((cg, t, best))
mk = Counter("abcd"[p] for p in POS.values())
need = {L: 25 * len(rows) // 100 - fixed[L] - mk[L] for L in "abcd"}
assert sum(need.values()) == len(combos) and min(need.values()) >= 0, (need, len(combos))
pool = [L for L in "abcd" for _ in range(need[L])]
for _ in range(1000):
    rng.shuffle(pool)
    if all(not (pool[i] == pool[i + 1] == pool[i + 2]) for i in range(len(pool) - 2)):
        break
for (cg, t, p), L in zip(combos, pool):
    plan[cg] = ("combo", t, "abcd".index(L), p)
print("fixed", dict(fixed), "| mcq+match", dict(mk), "| combos", len(combos), "| need", need)
print("true-by-position", {k: v for k, v in sorted(tally.items())})
out = [
    "# -*- coding: utf-8 -*-",
    f'"""Answer-format plan for {prefix} (made by l3_tools/ca_plan.py; see ca_common.finish), on the 2026 shape of the',
    "real paper: combination codes for most multi-statement items (truth in the authored order, the position of the",
    "correct code, and the order the statements are shown in), a few 'How many' counts, two-statement items with",
    "their order set, and the key positions of the MCQ and matching items. Keys come to 25 per letter.\"\"\"",
    f"KEEP_COUNT = {sorted(KEEP_COUNT)!r}",
    "FORMAT = {"]
out += [f'    "{cg}": {spec!r},' for cg, spec in plan.items()]
out += ["}", "POS = {"] + [f'    "{cg}": {p},' for cg, p in POS.items()] + ["}"]
io.open(f"{D}/{prefix}_format.py", "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
print(f"{prefix}_format.py: {len(plan)} planned items")
