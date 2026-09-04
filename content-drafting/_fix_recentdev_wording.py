# -*- coding: utf-8 -*-
import json

data = json.load(open('bihar_special_batch_05_recent_developments.json', encoding='utf-8'))
by_ref = {q['batch_ref']: q for q in data['questions']}

fixes = [
  ("bs1-129", "20% vertical reservation, restricted to Class-I posts only",
              "20% vertical reservation, restricted specifically to Class-I posts"),
  ("bs1-129", "50% reservation, but only within the police and judicial services",
              "50% reservation, but restricted specifically to the police and judicial services"),

  ("bs1-131", "A rural-only cashless ration-card digitisation drive",
              "A cashless ration-card digitisation drive aimed specifically at rural areas"),
  ("bs1-131", "A programme converting village ponds into fish-farming cooperatives exclusively",
              "A programme converting village ponds into fish-farming cooperatives, with no other stated purpose"),

  ("bs1-132", "Municipal bond financing available only to Patna and Gaya",
              "Municipal bond financing made available specifically to Patna and Gaya"),

  ("bs1-135", "Support limited strictly to the year of a girl's birth only",
              "Support limited strictly to the single year of a girl's birth"),
  ("bs1-135", "Support beginning only once a girl reaches Class 10",
              "Support that begins specifically once a girl reaches Class 10"),
  ("bs1-135", "A one-time payment made only at the time of marriage",
              "A one-time payment made specifically at the time of marriage"),

  ("bs1-136", "Students pursuing only engineering and medical courses",
              "Students pursuing engineering and medical courses specifically"),
  ("bs1-136", "Only students already employed part-time while studying",
              "Students who are already employed part-time while studying, and no one else"),

  ("bs1-139", "Only students who subsequently enrol in a government-run ITI",
              "Students who subsequently enrol in a government-run ITI, and no one else"),

  ("bs1-141", "It became the first Indian state to complete rural electrification using only solar micro-grids",
              "It became the first Indian state to complete rural electrification using solar micro-grids exclusively"),
  ("bs1-141", "It became the only state to achieve this without any central government funding support",
              "It became the sole state to achieve this without any central government funding support"),

  ("bs1-142", "It covers urban households only, with rural coverage handled by a separate later scheme",
              "It covers urban households specifically, with rural coverage handled by a separate later scheme"),

  ("bs1-143", "Only families in which the bride holds a postgraduate degree",
              "Families in which the bride holds a postgraduate degree, and no others"),
  ("bs1-143", "Only families residing in officially notified urban slum areas",
              "Families residing specifically in officially notified urban slum areas"),

  ("bs1-144", "Free vocational-college seats reserved for women applicants only",
              "Free vocational-college seats reserved specifically for women applicants"),

  ("bs1-148", "A statewide toll-free highway network for freight vehicles only",
              "A statewide toll-free highway network built specifically for freight vehicles"),

  ("bs1-150", "A short-term emergency response programme created specifically for post-pandemic recovery only",
              "A short-term emergency response programme created specifically for post-pandemic recovery"),

  ("bs1-151", "Both schemes target exactly the same population of liquor-ban-affected families, differing only in payment frequency",
              "Both schemes target exactly the same population of liquor-ban-affected families, differing solely in how often payments are made"),
]

applied = 0
missing = []
for ref, old, new in fixes:
    q = by_ref[ref]
    found = False
    for o in q['options']:
        if o['body'] == old:
            o['body'] = new
            found = True
            applied += 1
            break
    if not found:
        missing.append((ref, old))

print(f"applied {applied}/{len(fixes)}")
if missing:
    print("MISSING:")
    for ref, old in missing:
        print(f"  {ref}: {old[:70]}")

json.dump(data, open('bihar_special_batch_05_recent_developments.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
