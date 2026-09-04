import json, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
files = [
    "history_batch_01.json","history_batch_02.json","history_batch_03_single.json",
    "bihar_special_batch_01_history_culture.json","bihar_special_batch_02_geography.json",
    "bihar_special_batch_03_economy.json","bihar_special_batch_04_polity.json",
    "bihar_special_batch_05_recent_developments.json",
    "bihar_special2_batch_01_economy.json","bihar_special2_batch_02_polity.json",
    "bihar_special2_batch_03_recent_dev.json","bihar_special2_batch_04_geography.json",
]
seen = {}
dupes = []
total = 0
for f in files:
    data = json.load(open(f, encoding="utf-8"))
    for q in data["questions"]:
        total += 1
        cid = q["concept_group_id"]
        if cid in seen:
            dupes.append((cid, seen[cid], f))
        seen[cid] = f
print(f"Total questions checked: {total}")
print(f"Unique concept_group_ids: {len(seen)}")
print(f"Duplicates: {dupes}")
