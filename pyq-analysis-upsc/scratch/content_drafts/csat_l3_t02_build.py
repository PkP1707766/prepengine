# -*- coding: utf-8 -*-
"""Build CSAT Level 3 · Test 2 (80 items) from its three sections and write one INSERT (status 'draft').

  PYTHONIOENCODING=utf-8 python csat_l3_t02_build.py

Level 3 is the harder CSAT tier (difficulty 6 easy / 41 medium / 33 hard against Level 2's 10 / 44 / 26), on the same
80-slot layout as Level 2. Every Quant and Reasoning key is re-derived in code while the sections load
(csat_common.N/T/S2/SC/DS take check=...), so a build that finishes is a build whose computed keys all agree. The rows
carry question_data.csat_set = 'csat-l3-t02' and csat_order 1-80, so the test can be assembled in that order with
question shuffling off.

spread() swaps Quant items
with Quant items and Reasoning items with Reasoning items (passages and the data-sufficiency block stay where they
are) until no three hard items run together, every ten positions hold two to six hard items (three to five wherever the
fixed passages and data-sufficiency block allow), the first two items are not hard, no answer letter appears four
times running, and no sub-topic comes twice within four positions. Test 1
could swap only within a sub-topic; here the sub-topics placed late in the paper had no hard items to move, so the
swaps run across sub-topics with the spacing rule in their place. The search is seeded, so the build is repeatable."""
import random
import csat_common as c
c.SET = "csat-l3-t02"
import csat_l3_t02_qa, csat_l3_t02_lr, csat_l3_t02_rc  # noqa: E402,F401  (loading them builds the rows)

def key(r):
    return [o["isCorrect"] for o in r["options"]].index(True)

def cost(order):
    """(rule breaks, soft distance): the rules must all hold; the soft part asks for 3-5 hard items in every ten."""
    d = [r["difficulty"] == "hard" for r in order]
    k = [key(r) for r in order]
    t = [(r["slot"], r["topic"]) if r["slot"] in ("Q", "L") else None for r in order]
    win = [sum(d[i:i + 10]) for i in range(0, len(d) - 9)]
    rules = (d[0] + d[1]
             + sum(1 for h in win if not 2 <= h <= 6)
             + sum(1 for i in range(len(d) - 2) if d[i] and d[i + 1] and d[i + 2])
             + sum(1 for i in range(len(k) - 3) if k[i] == k[i + 1] == k[i + 2] == k[i + 3])
             + sum(1 for i in range(len(t)) for j in range(i + 1, min(i + 4, len(t))) if t[i] and t[i] == t[j]))
    soft = sum(1 for h in win if not 3 <= h <= 5)
    return rules, soft

def spread(order, seed=1):
    rng = random.Random(seed)
    groups = {}
    for i, r in enumerate(order):
        if r["slot"] in ("Q", "L"):
            groups.setdefault(r["slot"], []).append(i)
    pairs = [g for g in groups.values() if len(g) > 1]
    best = cost(order)
    for _ in range(40000):
        g = rng.choice(pairs)
        i, j = rng.sample(g, 2)
        order[i], order[j] = order[j], order[i]
        new = cost(order)
        if new <= best:
            best = new
        else:
            order[i], order[j] = order[j], order[i]
    for n, r in enumerate(order, 1):
        r["question_data"]["csat_order"] = n
    return order, best

c.interleave("Q")   # both modules are written topic by topic; spread each topic through the paper
c.interleave("L")
best = None
for seed in range(1, 21):                      # keep the seed with the fewest soft misses among those meeting every rule
    order, (rules, soft) = spread(c.assemble(), seed)
    if rules == 0 and (best is None or soft < best[1]):
        best = (seed, soft, [r["concept_group_id"] for r in order])
    if best and best[1] == 0:
        break
assert best, "spread() could not meet every rule"
seed, soft, ids = best
order, _ = spread(c.assemble(), seed)
assert [r["concept_group_id"] for r in order] == ids
print("spread() seed", seed, "| ten-item windows outside 3-5 hard:", soft)
diff = "".join(r["difficulty"][0] for r in order)
print("difficulty by position:", diff)
print("hard per ten:", [diff[i:i + 10].count("h") for i in range(0, 80, 10)])
c.report(order)
c.write("csat_l3_t02.sql", order)
