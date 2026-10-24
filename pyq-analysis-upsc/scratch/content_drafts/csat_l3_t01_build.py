# -*- coding: utf-8 -*-
"""Build CSAT Level 3 · Test 1 (80 items) from its three sections and write one INSERT (status 'draft').

  PYTHONIOENCODING=utf-8 python csat_l3_t01_build.py

Level 3 is the harder CSAT tier (difficulty 6 easy / 42 medium / 32 hard against Level 2's 10 / 44 / 26), on the same
80-slot layout as Level 2. Every Quant and Reasoning key is re-derived in code while the sections load
(csat_common.N/T/S2/SC/DS take check=...), so a build that finishes is a build whose computed keys all agree. The rows
carry question_data.csat_set = 'csat-l3-t01' and csat_order 1-80, so the test can be assembled in that order with
question shuffling off.

With 40 per cent of the items hard, interleave() alone left five hard items in a row near the start. spread() swaps
items only within the same slot and sub-topic (so every topic keeps its places on the paper, and passages and the
data-sufficiency block stay where they are) until no three hard items run together, every ten positions hold three to
five hard items, the first two items are not hard, and no answer letter appears four times running. The search is
seeded, so the build is repeatable."""
import random
import csat_common as c
c.SET = "csat-l3-t01"
import csat_l3_t01_qa, csat_l3_t01_lr, csat_l3_t01_rc  # noqa: E402,F401  (loading them builds the rows)

def key(r):
    return [o["isCorrect"] for o in r["options"]].index(True)

def cost(order):
    d = [r["difficulty"] == "hard" for r in order]
    k = [key(r) for r in order]
    s = 30 * (d[0] + d[1])
    s += sum(max(0, abs(sum(d[i:i + 10]) - 4) - 1) ** 2 * 5 for i in range(0, len(d) - 9))
    s += sum(40 for i in range(len(d) - 2) if d[i] and d[i + 1] and d[i + 2])
    s += sum(60 for i in range(len(k) - 3) if k[i] == k[i + 1] == k[i + 2] == k[i + 3])
    return s

def spread(order, seed=1):
    rng = random.Random(seed)
    groups = {}
    for i, r in enumerate(order):
        if r["slot"] in ("Q", "L"):
            groups.setdefault((r["slot"], r["topic"]), []).append(i)
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
for seed in range(1, 51):                      # the first seed whose search meets every rule
    order, left = spread(c.assemble(), seed)
    if left == 0:
        break
assert left == 0, f"spread() could not meet every rule (cost {left})"
print("spread() seed", seed)
diff = "".join(r["difficulty"][0] for r in order)
print("difficulty by position:", diff)
print("hard per ten:", [diff[i:i + 10].count("h") for i in range(0, 80, 10)])
c.report(order)
c.write("csat_l3_t01.sql", order)
