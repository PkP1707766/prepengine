# -*- coding: utf-8 -*-
"""Generic post-draft fixer: apply named option-body rewrites, then reassign
correct-answer position for an even spread (cycle 0,1,2,3 in file order).
Usage: python _fix_batch.py <path.json> <rewrites.json>
rewrites.json: {"batch_ref": ["new opt0", "new opt1", "new opt2", "new opt3"], ...}
(rewrites are matched to CURRENT option order, applied before the position shuffle)
"""
import json, sys

path = sys.argv[1]
rewrites_path = sys.argv[2]
data = json.load(open(path, encoding="utf-8"))
rewrites = json.load(open(rewrites_path, encoding="utf-8"))
qs = {q["batch_ref"]: q for q in data["questions"]}

for ref, new_bodies in rewrites.items():
    q = qs[ref]
    old_opts = q["options"]
    assert len(old_opts) == len(new_bodies) == 4, ref
    for i, body in enumerate(new_bodies):
        if body is not None:
            old_opts[i]["body"] = body

# reassign correct-answer position for even spread (cycle 0,1,2,3), mcq only
order = [q["batch_ref"] for q in data["questions"] if q["type"] == "mcq"]
target_positions = [i % 4 for i in range(len(order))]
qs_by_ref = {q["batch_ref"]: q for q in data["questions"]}

for ref, target_idx in zip(order, target_positions):
    q = qs_by_ref[ref]
    opts = q["options"]
    correct_idx = next(i for i, o in enumerate(opts) if o["isCorrect"])
    if correct_idx == target_idx:
        continue
    opts[correct_idx], opts[target_idx] = opts[target_idx], opts[correct_idx]

json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done")
