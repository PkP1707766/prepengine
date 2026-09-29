# -*- coding: utf-8 -*-
"""Content-based re-tag of the 95 UPSC GS1 Science & Technology PYQs (2015-2026).

The decoder filed 86 of 95 S&T questions under one catch-all, 'Tech & Innovation', so the live
config's Tech & Innovation 0.85 was not a content fact (the same problem Polity's 'Governance',
Environment's 'Biodiversity', Geography's 'Physical/Human' and Economy's 'Macroeconomics' had).
Each question is tagged from its stem (decoder_<year>_text.txt; 2023-26 from
science_technology_qs_2023_2026.txt), one primary bucket per question.

The eight buckets roll up into the two Level-2 tests the blueprint names for S&T:
  Test 19  General Science                      -> PH, CH, BI, AS
  Test 20  Applied S&T & Agriculture            -> ST, IT, EN, DF
Astronomy and earth science (stars, light-years, gravitational-wave detectors, solar storms,
forecasting systems) sit with General Science; satellites, navigation and missions with Applied
S&T. No S&T PYQ of 2015-26 is primarily about farming; the farm-technology questions the decoder
filed under Economy (biochar, fertigation, zero tillage) are tagged in Economy's agriculture bucket,
so Test 20's agriculture content is drafted inside the applied buckets (solar pumps, aquaculture
biofilters, drones, crop biotechnology) rather than as a weighted bucket of its own.

Also derives S&T's own question-type and difficulty weights from the 2023-26 questions (49), counted
from each question's option set; the 2025 entries are two-column OCR and were read one by one.
No 2023-26 S&T question is in the pairs format. Writes science_technology_subtopic_retag.csv and
prints everything needed for the live config.
"""
import csv, collections, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "upsc_gs1_combined_2015-2026.csv")
TXT = os.path.join(HERE, "science_technology_qs_2023_2026.txt")

PH = "Physics & Everyday Science"                   # pressure cookers, lamps, displays, sensors, radar, Nobel physics
CH = "Chemistry & Materials"                         # plastics, carbon materials, hydrogels, activated carbon, cloud seeding
BI = "Biology, Health & Biotechnology"               # DNA tools, metagenomics, Wolbachia, antibodies, viruses, genome projects
AS = "Astronomy & Earth Science"                     # stars, light-years, neutrino and gravitational-wave observatories, solar storms
ST = "Space Technology & Missions"                   # remote sensing, navigation satellites, Mangalyaan, RTGs, private space
IT = "IT, Communication & Emerging Technologies"     # AI, blockchain, Web3, quantum, chips, payments tech, wireless
EN = "Energy & Environmental Technology"             # fuel cells, green hydrogen, storage, nuclear fuel, DAC, EVs, water treatment
DF = "Defence, Aerospace & Security Technology"      # fighters, UAVs and swarms, stealth, explosives, flight recorders

L2 = {
    "Test 19 General Science": [PH, CH, BI, AS],
    "Test 20 Applied S&T & Agriculture": [ST, IT, EN, DF],
}

TAG = {
 # 2015
 ("2015",23):BI, ("2015",30):AS, ("2015",32):IT, ("2015",45):AS, ("2015",71):ST, ("2015",73):AS, ("2015",93):EN,
 ("2015",95):EN,
 # 2016
 ("2016",5):IT, ("2016",35):IT, ("2016",36):EN, ("2016",47):DF, ("2016",66):IT, ("2016",78):EN, ("2016",79):EN,
 ("2016",84):IT, ("2016",87):ST, ("2016",91):ST,
 # 2017
 ("2017",43):IT, ("2017",44):AS, ("2017",73):CH, ("2017",74):PH, ("2017",85):IT, ("2017",87):AS,
 # 2020
 ("2020",38):IT, ("2020",39):IT, ("2020",40):IT, ("2020",41):CH, ("2020",42):DF, ("2020",43):AS, ("2020",46):IT,
 ("2020",88):EN,
 # 2021
 ("2021",68):PH, ("2021",71):CH, ("2021",72):PH, ("2021",74):CH, ("2021",76):AS,
 # 2022
 ("2022",31):IT, ("2022",32):IT, ("2022",33):IT, ("2022",35):IT, ("2022",36):IT, ("2022",40):AS, ("2022",46):CH,
 ("2022",69):IT, ("2022",84):EN,
 # 2023
 ("2023",11):EN, ("2023",53):CH, ("2023",54):PH, ("2023",55):EN, ("2023",56):AS, ("2023",57):ST, ("2023",60):EN,
 ("2023",67):BI, ("2023",69):BI, ("2023",70):BI, ("2023",99):EN,
 # 2024
 ("2024",31):ST, ("2024",32):AS, ("2024",34):PH, ("2024",35):DF, ("2024",36):CH, ("2024",37):EN, ("2024",38):EN,
 ("2024",39):EN, ("2024",48):IT,
 # 2025
 ("2025",33):AS, ("2025",36):EN, ("2025",41):EN, ("2025",42):DF, ("2025",43):EN, ("2025",45):CH, ("2025",46):DF,
 ("2025",47):IT, ("2025",48):BI, ("2025",49):BI, ("2025",50):CH, ("2025",81):CH, ("2025",85):CH, ("2025",94):ST,
 # 2026
 ("2026",41):BI, ("2026",42):IT, ("2026",43):DF, ("2026",44):DF, ("2026",45):EN, ("2026",46):ST, ("2026",47):DF,
 ("2026",48):BI, ("2026",49):IT, ("2026",50):AS, ("2026",65):IT, ("2026",79):IT, ("2026",80):DF, ("2026",81):PH,
 ("2026",84):AS,
}

# Question format of each 2023-26 question, read from its option set:
#   mcq = single answer; statement_based = 2-statement, "How many" counts, or combination codes;
#   assertion_reason = Statement-I/II (2023-Q11; 2024-Q32; 2025-Q81) or the Statement-I/II/III form
#   (2025-Q33, Q50). No 2023-26 S&T question uses the pairs format.
M, S, A, P = "mcq", "statement_based", "assertion_reason", "match_the_following"
TYPE = {
 ("2023",11):A, ("2023",53):S, ("2023",54):S, ("2023",55):S, ("2023",56):S, ("2023",57):M, ("2023",60):S,
 ("2023",67):M, ("2023",69):M, ("2023",70):M, ("2023",99):S,
 ("2024",31):S, ("2024",32):A, ("2024",34):S, ("2024",35):S, ("2024",36):S, ("2024",37):M, ("2024",38):M,
 ("2024",39):M, ("2024",48):M,
 ("2025",33):A, ("2025",36):S, ("2025",41):S, ("2025",42):S, ("2025",43):S, ("2025",45):S, ("2025",46):M,
 ("2025",47):S, ("2025",48):S, ("2025",49):S, ("2025",50):A, ("2025",81):A, ("2025",85):M, ("2025",94):S,
 ("2026",41):S, ("2026",42):S, ("2026",43):S, ("2026",44):S, ("2026",45):S, ("2026",46):S, ("2026",47):S,
 ("2026",48):S, ("2026",49):S, ("2026",50):S, ("2026",65):S, ("2026",79):S, ("2026",80):S, ("2026",81):M,
 ("2026",84):S,
}
AR_3STATEMENT = {("2025",33), ("2025",50)}

BAND = {"easy": "easy", "med": "medium", "medium": "medium", "hard": "hard",
        "easy-medium": "easy", "medium-hard": "medium"}


def main():
    allrows = list(csv.DictReader(open(SRC, encoding="utf-8")))
    rows = [r for r in allrows if r["subject"] == "Science & Technology"]
    keys = {(r["year"], int(r["question_number"])) for r in rows}
    assert keys == set(TAG), ("untagged:", sorted(keys - set(TAG)), "extra:", sorted(set(TAG) - keys))
    assert len(rows) == 95

    with open(os.path.join(HERE, "science_technology_subtopic_retag.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["year", "question_number", "title", "old_sub_topic", "new_sub_topic"])
        for r in sorted(rows, key=lambda r: (int(r["year"]), int(r["question_number"]))):
            w.writerow([r["year"], r["question_number"], r["title"], r["sub_topic"], TAG[(r["year"], int(r["question_number"]))]])

    tag = lambda r: TAG[(r["year"], int(r["question_number"]))]
    print(f"Science & Technology rows: {len(rows)}")
    print("old decoder sub-topics:", dict(collections.Counter(r["sub_topic"] for r in rows).most_common()))

    labels = [PH, CH, BI, AS, ST, IT, EN, DF]
    years = sorted({r["year"] for r in rows}, key=int)
    wmap = {y: i + 1 for i, y in enumerate(years)}  # same linear recency weights as build_config.py
    pooled = collections.Counter(tag(r) for r in rows)
    recent = collections.Counter(tag(r) for r in rows if int(r["year"]) >= 2023)
    n_recent = sum(recent.values())
    acc = collections.Counter(); tw = 0
    for y in years:
        ry = [r for r in rows if r["year"] == y]
        cy = collections.Counter(tag(r) for r in ry)
        for k in labels: acc[k] += wmap[y] * cy[k] / len(ry)
        tw += wmap[y]
    rec = {k: acc[k] / tw for k in labels}

    print(f"\n{'sub-topic':46} {'count':>5} {'pooled%':>8} {'recency%':>9} {'2023-26%':>9}")
    for k in sorted(labels, key=lambda k: -rec[k]):
        print(f"{k:46} {pooled[k]:5} {100*pooled[k]/len(rows):7.1f}% {100*rec[k]:8.1f}% {100*recent[k]/n_recent:8.1f}%")
    print(f"{'TOTAL':46} {sum(pooled.values()):5}")

    print("\nLevel-2 roll-up (recency-weighted):")
    for test, subs in L2.items():
        print(f"  {test:40} {100*sum(rec[k] for k in subs):5.1f}%")

    r4 = {k: round(rec[k], 4) for k in labels}
    drift = round(1 - sum(r4.values()), 4)
    top = max(r4, key=r4.get); r4[top] = round(r4[top] + drift, 4)
    print("\nsub_topic_weights (recency, rounded, sum=1):")
    print(r4, "sum =", round(sum(r4.values()), 4))

    text = open(TXT, encoding="utf-8").read()
    heads = re.findall(r"^===== (\d{4}) Q(\d+) \[[^,\]]+, ([^\]]+)\]", text, re.M)
    corpus = [(y, int(q), d.strip().lower()) for y, q, d in heads]
    assert len(corpus) == 49
    assert {(y, q) for y, q, _ in corpus} == set(TYPE), "type map must cover exactly the 2023-26 rows"
    n = len(corpus)
    tcount = collections.Counter(TYPE[(y, q)] for y, q, _ in corpus)
    dcount = collections.Counter(BAND[d] for _, _, d in corpus)
    print(f"\n2023-26 corpus: {n} questions")
    print("question types:", dict(tcount), f"(assertion_reason includes {len(AR_3STATEMENT)} Statement-I/II/III)")
    print("difficulty:    ", dict(dcount))
    t4 = {k: round(v / n, 4) for k, v in tcount.items()}
    d4 = {k: round(v / n, 4) for k, v in dcount.items()}
    for m in (t4, d4):
        drift = round(1 - sum(m.values()), 4); top = max(m, key=m.get); m[top] = round(m[top] + drift, 4)
    print("question_type_weights[Science & Technology] =", t4, "sum =", round(sum(t4.values()), 4))
    print("difficulty_weights[Science & Technology]    =", d4, "sum =", round(sum(d4.values()), 4))
    print("\nper year (type):")
    for y in ["2023", "2024", "2025", "2026"]:
        print(" ", y, dict(collections.Counter(TYPE[(yy, q)] for yy, q, _ in corpus if yy == y)))
    print("per year (difficulty):")
    for y in ["2023", "2024", "2025", "2026"]:
        print(" ", y, dict(collections.Counter(BAND[d] for yy, q, d in corpus if yy == y)))


if __name__ == "__main__":
    main()
