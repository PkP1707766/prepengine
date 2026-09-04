import json

data = json.load(open('bihar_special_batch_02_geography.json', encoding='utf-8'))
qs = data['questions']

to_reserve = {'bs1-097', 'bs1-100', 'bs1-092', 'bs1-087', 'bs1-096', 'bs1-099'}

reserved = [q for q in qs if q['batch_ref'] in to_reserve]
kept = [q for q in qs if q['batch_ref'] not in to_reserve]

assert len(reserved) == 6, len(reserved)
assert len(kept) == 41, len(kept)

data['questions'] = kept
data['meta']['total_questions'] = 41
json.dump(data, open('bihar_special_batch_02_geography.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

reserve_doc = {
    "meta": {
        "purpose": "6 validated, drafted-but-unused Geography questions from Batch 02's drafting pass, set aside because Paper I's target_cells only needed 41 -- reserved for Paper II/III's Geography allocation so this work isn't redrafted from scratch.",
        "generated_at": "2026-09-03",
        "source_citation": "Perfection IAS (Dhananjay IAS), Bihar Special Orange Book",
        "note": "bs1-092 was removed from Paper I specifically because it duplicated a fact already covered inside bs1-094's match_the_following (Sheohar = smallest district) -- not just a volume trim, a real de-dup fix. The other 5 are volume trims only, no quality/dup issue.",
    },
    "questions": reserved
}
json.dump(reserve_doc, open('bihar_special_geography_reserve_for_paper2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

from collections import Counter
cells = Counter((q['difficulty'], q['type']) for q in kept)
print('kept cells:', dict(sorted(cells.items())))
print('reserved:', [q['batch_ref'] for q in reserved])
