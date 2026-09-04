import json, sys, glob

files = [
    "history_batch_01.json",
    "history_batch_02.json",
    "history_batch_03_single.json",
    "bihar_special_batch_01_history_culture.json",
    "bihar_special_batch_02_geography.json",
    "bihar_special_batch_03_economy.json",
    "bihar_special_batch_04_polity.json",
    "bihar_special_batch_05_recent_developments.json",
]

total = 0
with open("existing_300_summary.txt", "w", encoding="utf-8") as out:
    for f in files:
        data = json.load(open(f, encoding="utf-8"))
        qs = data["questions"]
        out.write(f"=== {f} ({len(qs)} questions) ===\n")
        for q in qs:
            body = q["body"].replace("\n", " ")[:110]
            cid = q.get("concept_group_id", "MISSING")
            out.write(f"[{q.get('subject','?')}/{q.get('topic','?')}/{q.get('difficulty','?')}/{q.get('type','?')}] {cid} :: {body}\n")
        total += len(qs)
        out.write("\n")
    out.write(f"TOTAL = {total}\n")

print(f"Wrote existing_300_summary.txt, total questions = {total}")
