# -*- coding: utf-8 -*-
"""Content-based re-tag of the 91 UPSC GS1 Geography PYQs (2015-2026).

The decoder filed 81 of 91 Geography questions under one catch-all, 'Physical/Human', so the
live config's Physical 0.50 / Human 0.445 split was that bucket halved, not a content fact (the
same problem Polity's 'Governance' and Environment's 'Biodiversity' had). Each question is tagged
from its actual stem (decoder_<year>_text.txt; 2023-26 from geography_qs_2023_2026.txt, whose
2025 entries are the paper's own text), one primary bucket per question.

The eight buckets roll up into the three Level-2 tests the blueprint names for Geography:
  World Physical     -> GM, CL, OC, WR
  Indian Physical    -> IR, IP
  Human & Economic   -> EM, HT

Disaster Management check (asked for by the 2026-09-27 Environment review): the script lists
every GS1 PYQ whose title names a hazard or disaster institution. In Geography those are hazard
*processes* (cyclone zones, jet streams and cyclones, seismic waves, volcanic products), tagged
with climatology or geomorphology; no GS1 question in 2015-26 tests disaster management itself.

Also derives Geography's own question-type and difficulty weights from the 2023-26 questions
(the playbook's per-subject corpus, 45 questions), counted from each question's option set.
The playbook's Part E table says Statement-I/II appears only in 2024; the option sets show it
in 2023 (Q63, Q64) and 2025 (Q26; Q27 and Q28 are the three-statement form, confirmed against
published 2025 papers). The direct count is used here and the discrepancy is flagged.
Writes geography_subtopic_retag.csv and prints everything needed for the live config.
"""
import csv, collections, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "upsc_gs1_combined_2015-2026.csv")
TXT = os.path.join(HERE, "geography_qs_2023_2026.txt")

GM = "Geomorphology & Earth's Interior"        # earth motions, interior, plates, volcanoes, quakes, rocks, weathering, landforms
CL = "Climatology & Biomes"                    # atmosphere, insolation, winds, clouds, isotherms, climate types, cyclones, biomes
OC = "Oceanography & Hydrosphere"              # currents, tides, IOD, ocean temperature, water distribution
WR = "World Regions, Water Bodies & Places"    # world mapping: seas, straits, lakes, basins, borders, regions, ranges
IR = "Indian Rivers, Lakes & Wetlands"         # tributaries, river mouths, sequences, lakes, reservoirs, waterfalls, wetlands
IP = "Indian Physiography, Climate & Regions"  # hills, ranges, peninsular block, coasts, islands, states/borders, soils, regional climate
EM = "Resources: Minerals, Energy & Agriculture"  # minerals/ores, shale gas, crop producers, agricultural comparisons
HT = "Transport, Ports & Human Geography"     # ports, corridors, bridges, inland waterways, cultural landscapes

L2 = {
    "World Physical": [GM, CL, OC, WR],
    "Indian Physical": [IR, IP],
    "Human & Economic": [EM, HT],
}

TAG = {
 # 2015
 ("2015",5):CL, ("2015",6):IP, ("2015",14):OC, ("2015",15):IP, ("2015",36):IR, ("2015",66):CL, ("2015",69):HT,
 ("2015",70):OC, ("2015",77):WR, ("2015",80):CL,
 # 2016
 ("2016",28):IR, ("2016",74):EM, ("2016",85):IR, ("2016",94):IP, ("2016",96):HT,
 # 2017
 ("2017",19):IP, ("2017",30):IR, ("2017",49):IP, ("2017",54):WR, ("2017",58):IP, ("2017",66):OC, ("2017",98):IP,
 # 2020
 ("2020",68):IR, ("2020",92):EM, ("2020",93):OC, ("2020",96):IP, ("2020",99):CL,
 # 2021
 ("2021",53):IR, ("2021",54):IR, ("2021",55):IR, ("2021",58):CL, ("2021",60):CL, ("2021",61):CL, ("2021",62):OC,
 ("2021",64):IP,
 # 2022
 ("2022",23):WR, ("2022",24):IP, ("2022",25):IP, ("2022",26):WR, ("2022",27):WR, ("2022",28):EM, ("2022",29):GM,
 ("2022",30):IR, ("2022",70):IR, ("2022",81):CL, ("2022",88):WR,
 # 2023
 ("2023",1):IR, ("2023",2):HT, ("2023",4):EM, ("2023",5):IP, ("2023",6):EM, ("2023",7):EM, ("2023",8):WR,
 ("2023",9):IP, ("2023",10):HT, ("2023",61):WR, ("2023",62):CL, ("2023",63):CL, ("2023",64):CL, ("2023",65):GM,
 # 2024
 ("2024",1):CL, ("2024",2):CL, ("2024",3):GM, ("2024",4):CL, ("2024",5):EM, ("2024",6):IR, ("2024",7):GM,
 ("2024",8):WR, ("2024",9):IR, ("2024",10):GM, ("2024",12):CL, ("2024",13):CL, ("2024",14):CL, ("2024",15):GM,
 ("2024",79):WR, ("2024",89):WR,
 # 2025 (paper text in geography_qs_2023_2026.txt)
 ("2025",22):WR, ("2025",23):WR, ("2025",25):GM, ("2025",26):CL, ("2025",27):CL, ("2025",28):GM,
 # 2026
 ("2026",24):HT, ("2026",25):IR, ("2026",26):IP, ("2026",30):WR, ("2026",31):WR, ("2026",33):IP, ("2026",34):IP,
 ("2026",39):WR, ("2026",61):HT,
}

# Question format of each 2023-26 question, read from its option set:
#   mcq = single answer (incl. 2024-Q6's one-answer sequence and 2026-Q25's identify-the-river);
#   statement_based = 2-statement, "How many" counts, or combination codes ("1 and 3", "3 only");
#   assertion_reason = Statement-I/II (2024-Q7, 2025-Q27, 2025-Q28 are the three-statement form);
#   match_the_following = "how many pairs/rows are correctly matched".
M, S, A, P = "mcq", "statement_based", "assertion_reason", "match_the_following"
TYPE = {
 ("2023",1):S, ("2023",2):P, ("2023",4):S, ("2023",5):M, ("2023",6):M, ("2023",7):M, ("2023",8):M,
 ("2023",9):S, ("2023",10):S, ("2023",61):S, ("2023",62):M, ("2023",63):A, ("2023",64):A, ("2023",65):S,
 ("2024",1):A, ("2024",2):A, ("2024",3):S, ("2024",4):S, ("2024",5):M, ("2024",6):M, ("2024",7):A,
 ("2024",8):S, ("2024",9):P, ("2024",10):P, ("2024",12):S, ("2024",13):M, ("2024",14):S, ("2024",15):S,
 ("2024",79):M, ("2024",89):S,
 ("2025",22):S, ("2025",23):S, ("2025",25):S, ("2025",26):A, ("2025",27):A, ("2025",28):A,
 ("2026",24):S, ("2026",25):M, ("2026",26):S, ("2026",30):S, ("2026",31):M, ("2026",33):S, ("2026",34):S,
 ("2026",39):S, ("2026",61):S,
}
AR_3STATEMENT = {("2024",7), ("2025",27), ("2025",28)}

# Difficulty: the header label of each 2023-26 question; a hyphenated label takes the lower
# band (the rule used for Polity and Environment).
BAND = {"easy": "easy", "med": "medium", "medium": "medium", "hard": "hard",
        "easy-medium": "easy", "medium-hard": "medium"}

HAZARD = re.compile(r"disaster|cyclone|earthquake|seismic|tsunami|flood|landslide|drought|volcan|NDMA|Sendai|P & S Waves", re.I)


def main():
    allrows = list(csv.DictReader(open(SRC, encoding="utf-8")))
    rows = [r for r in allrows if r["subject"] == "Geography"]
    keys = {(r["year"], int(r["question_number"])) for r in rows}
    assert keys == set(TAG), ("untagged:", sorted(keys - set(TAG)), "extra:", sorted(set(TAG) - keys))
    assert len(rows) == 91

    with open(os.path.join(HERE, "geography_subtopic_retag.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["year", "question_number", "title", "old_sub_topic", "new_sub_topic"])
        for r in rows:
            w.writerow([r["year"], r["question_number"], r["title"], r["sub_topic"], TAG[(r["year"], int(r["question_number"]))]])

    tag = lambda r: TAG[(r["year"], int(r["question_number"]))]
    print(f"Geography rows: {len(rows)}")
    print("old decoder sub-topics:", dict(collections.Counter(r["sub_topic"] for r in rows).most_common()))

    labels = [GM, CL, OC, WR, IR, IP, EM, HT]
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

    print(f"\n{'sub-topic':44} {'count':>5} {'pooled%':>8} {'recency%':>9} {'2023-26%':>9}")
    for k in sorted(labels, key=lambda k: -rec[k]):
        print(f"{k:44} {pooled[k]:5} {100*pooled[k]/len(rows):7.1f}% {100*rec[k]:8.1f}% {100*recent[k]/n_recent:8.1f}%")
    print(f"{'TOTAL':44} {sum(pooled.values()):5}")

    print("\nLevel-2 roll-up (recency-weighted):")
    for test, subs in L2.items():
        print(f"  {test:20} {100*sum(rec[k] for k in subs):5.1f}%   ({', '.join(subs)})")

    r4 = {k: round(rec[k], 4) for k in labels}
    drift = round(1 - sum(r4.values()), 4)
    top = max(r4, key=r4.get); r4[top] = round(r4[top] + drift, 4)
    print("\nsub_topic_weights (recency, rounded, sum=1):")
    print(r4, "sum =", round(sum(r4.values()), 4))

    # ---- Disaster Management evidence across all of GS1 ---------------------------------
    print("\nHazard / disaster titles across all GS1 PYQs 2015-26:")
    for r in allrows:
        if HAZARD.search(r["title"]):
            t = tag(r) if r["subject"] == "Geography" else "-"
            print(f"  {r['year']}-Q{r['question_number']:>3} [{r['subject']}] {r['title']}  -> {t}")

    # ---- type + difficulty from the 2023-26 corpus -------------------------------------
    text = open(TXT, encoding="utf-8").read()
    heads = re.findall(r"^===== (\d{4}) Q(\d+) \[[^,\]]+, ([^\]]+)\]", text, re.M)
    corpus = [(y, int(q), d.strip().lower()) for y, q, d in heads]
    assert len(corpus) == 45
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
    print("question_type_weights[Geography] =", t4, "sum =", round(sum(t4.values()), 4))
    print("difficulty_weights[Geography]    =", d4, "sum =", round(sum(d4.values()), 4))
    print("\nper year (type):")
    for y in ["2023", "2024", "2025", "2026"]:
        print(" ", y, dict(collections.Counter(TYPE[(yy, q)] for yy, q, _ in corpus if yy == y)))
    print("\nStatement-I/II per year (playbook Part E says 2024 only):",
          dict(collections.Counter(y for y, q, _ in corpus if TYPE[(y, q)] == A)))


if __name__ == "__main__":
    main()
