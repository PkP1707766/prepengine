import json

data = json.load(open("bihar_special2_batch_01_economy.json", encoding="utf-8"))
for q in data["questions"]:
    opts = q["options"]
    lens = [len(o["body"]) for o in opts]
    correct_idx = next(i for i, o in enumerate(opts) if o["isCorrect"])
    is_strict_longest = lens[correct_idx] == max(lens) and lens.count(max(lens)) == 1
    print(f"{q['batch_ref']}: lens={lens} correct_idx={correct_idx} STRICT_LONGEST={is_strict_longest}")
