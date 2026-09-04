# -*- coding: utf-8 -*-
import json

path = "bihar_special2_batch_01_economy.json"
data = json.load(open(path, encoding="utf-8"))
qs = {q["batch_ref"]: q for q in data["questions"]}

# --- Step 1: length-rebalance the 7 flagged questions (rewrite option bodies) ---
rewrites = {
    "bs2-203": ["Pulses (chana, masur)", "Jute, as in the Kosi belt", "Litchi orchards", "Tea plantations"],
    "bs2-207": ["Anand pattern (three-tier)", "Producer-company model", "Rochdale cooperative principles", "State-run procurement model"],
    "bs2-208": ["Renewable energy & rural electrification", "Coal-based thermal power generation", "Canal and irrigation-network upkeep", "Industrial land allotment for factories"],
    "bs2-210": ["Leather footwear manufacturing", "Handloom Tussar silk weaving", "Cane sugar refining and milling", "Makhana processing and export"],
    "bs2-216": ["Bihar State Power (Generation) Holding Company", "Bihar State Hydroelectric Power Corporation", "Bihar Industrial Area Development Authority (BIADA)", "the undivided Bihar State Electricity Board"],
    "bs2-217": ["Hindustan Urvarak & Rasayan Ltd. (HURL)", "Bharat Heavy Electricals Ltd. (BHEL) unit", "Steel Authority of India Ltd. (SAIL) plant", "Hindustan Aeronautics Ltd. (HAL) aircraft-component unit"],
    "bs2-218": ["Banks lend little locally relative to deposits collected", "Deposits collected fall short of loans disbursed", "Loan interest rates run below the national average", "Public-sector banks hold a distinctly smaller branch network than private banks statewide"],
}

for ref, new_bodies in rewrites.items():
    q = qs[ref]
    old_opts = q["options"]
    assert len(old_opts) == len(new_bodies) == 4, ref
    # option 0 was always correct pre-fix; preserve isCorrect flags positionally (all correct=idx0 still)
    for i, body in enumerate(new_bodies):
        old_opts[i]["body"] = body

# --- Step 2: reassign correct-answer position for even spread (cycle 0,1,2,3) ---
order = [q["batch_ref"] for q in data["questions"]]  # preserves file order
target_positions = [i % 4 for i in range(len(order))]

for ref, target_idx in zip(order, target_positions):
    q = qs[ref]
    opts = q["options"]
    correct_idx = next(i for i, o in enumerate(opts) if o["isCorrect"])
    if correct_idx == target_idx:
        continue
    # swap correct option into target_idx, shifting the displaced one into correct_idx
    opts[correct_idx], opts[target_idx] = opts[target_idx], opts[correct_idx]

json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done")
