import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = sys.argv[1]
refs = set(sys.argv[2:])
data = json.load(open(path, encoding="utf-8"))
for q in data["questions"]:
    if q["batch_ref"] not in refs or q["type"] != "mcq":
        continue
    print(f"=== {q['batch_ref']} ===")
    for i, o in enumerate(q["options"]):
        print(f"  [{i}] len={len(o['body'])} correct={o['isCorrect']} :: {o['body']}")
