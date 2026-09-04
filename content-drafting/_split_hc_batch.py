# -*- coding: utf-8 -*-
import json

path = "bihar_special2_batch_05_history_culture.json"
data = json.load(open(path, encoding="utf-8"))
qs = data["questions"]

cut_refs = {
    "bs2-601","bs2-602","bs2-603","bs2-604","bs2-605","bs2-607","bs2-608","bs2-609","bs2-610",
    "bs2-611","bs2-612","bs2-614","bs2-615","bs2-621","bs2-624","bs2-628","bs2-629","bs2-632",
    "bs2-634","bs2-638","bs2-639","bs2-641","bs2-649","bs2-650","bs2-654","bs2-655","bs2-658",
    "bs2-659","bs2-661","bs2-663",
}
assert len(cut_refs) == 30, len(cut_refs)

keep = [q for q in qs if q["batch_ref"] not in cut_refs]
cut = [q for q in qs if q["batch_ref"] in cut_refs]
assert len(keep) == 63, len(keep)
assert len(cut) == 30, len(cut)

# recompute target_cells from the kept 63
from collections import Counter
cells = Counter()
for q in keep:
    topic = q["topic"]
    key = f"Bihar_{topic}_{q['difficulty']}_{q['type']}"
    cells[key] += 1

data["meta"]["total_questions"] = 63
data["meta"]["target_cells"] = dict(sorted(cells.items()))
data["questions"] = keep
# remove references in flagged/skipped lists to cut batch_refs' facts that no longer apply
# (bs2-601 and bs2-621 were flagged/cut -- drop their flag entries, keep others)
data["meta"]["flagged_for_extra_review"] = [
    e for e in data["meta"]["flagged_for_extra_review"]
    if not e.startswith("bs2-601") and not e.startswith("bs2-621")
]
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

reserve = {
    "meta": {
        "purpose": "30 validated, drafted-but-unused History & Culture questions from Batch 05's drafting pass -- Orange Book source material for Ancient Bihar turned out far richer than the 63-question target needed, so these were set aside rather than discarded. Reserved for Paper III's History & Culture allocation so this work isn't redrafted from scratch.",
        "generated_at": "2026-09-04",
        "source_citation": "Perfection IAS (Dhananjay IAS), Bihar Special Orange Book",
        "note": "All 30 are fully-formed, validated questions (same option-craft/absolutist/length-bias standard as the live 63) -- none were cut for quality reasons, purely for volume. Re-run validate_bihar_special_batch.py after merging into a future batch, since concept_group_id/batch_ref collisions against Paper III's own live content will need a fresh check at that time."
    },
    "questions": cut
}
json.dump(reserve, open("bihar_special2_history_culture_reserve_for_paper3.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"done: kept {len(keep)}, reserved {len(cut)}")
print("target_cells:", dict(sorted(cells.items())))
