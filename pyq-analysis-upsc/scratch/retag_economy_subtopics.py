# -*- coding: utf-8 -*-
"""Content-based re-tag of the 176 UPSC GS1 Economy PYQs (2015-2026).

The decoder filed 126 of 176 Economy questions under one catch-all, 'Macroeconomics', and 32 more
under 'Agriculture', so the live config's Macroeconomics 0.66 / Five-Year Plans 0.18 split was not a
content fact (the same problem Polity's 'Governance', Environment's 'Biodiversity' and Geography's
'Physical/Human' had). Each question is tagged from its stem (decoder_<year>_text.txt; 2023-26 from
economy_qs_2023_2026.txt), one primary bucket per question.

The ten buckets roll up into the four Level-2 tests the blueprint names for Economy:
  Test 15  Basic Concepts, Money & Banking            -> MC, MB, FM
  Test 16  Growth, Development & External Sector      -> EX, GD
  Test 17  Fiscal Policy, Budget & Economic Survey    -> FB, FT
  Test 18  Sectors of the Economy & Inclusive Growth  -> AG, IN, IG

Farm-practice questions the decoder filed as Economy (biochar, fertigation, zero tillage, SRI,
permaculture) stay in Economy's agriculture bucket: they are asked alongside MSP, procurement and
credit, and S&T's own agriculture share is set when S&T is re-tagged.

Also derives Economy's own question-type and difficulty weights from the 2023-26 questions (65), counted
from each question's option set. The 2025 entries in economy_qs_2023_2026.txt are two-column OCR in which
neighbouring questions' option blocks run together; their formats were read question by question and
checked against the published paper (e.g. the Statement-I/II/III options printed beside 2025-Q10 belong to
Q9, and 2025-Q2's option codes are printed under Q5). Writes economy_subtopic_retag.csv and prints
everything needed for the live config.
"""
import csv, collections, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "upsc_gs1_combined_2015-2026.csv")
TXT = os.path.join(HERE, "economy_qs_2023_2026.txt")

MC = "Macro Concepts, National Income & Inflation"    # GDP, price indices, inflation types, demand, capital, sectors
MB = "Money, Banking & Monetary Policy"               # RBI tools, MPC, money supply/multiplier, banks and their regulation
FM = "Financial Markets, Instruments & Fintech"       # bonds, equity, InvITs, AIFs, insurance, payments, CBDC, tokenisation
EX = "External Sector & International Institutions"  # BoP, forex, exchange rates, FDI, WTO, IMF, World Bank, trade
GD = "Growth, Development, Poverty & Planning"        # liberalisation, growth theory, poverty measures, policy committees
FB = "Budget, Deficits & Public Debt"                 # deficits, capital budget, receipts, borrowing, crowding out
FT = "Taxation & Fiscal Federalism"                   # GST, tax ratios, BEPS, black money, Finance Commissions
AG = "Agriculture & Food Economy"                     # MSP, procurement, credit, markets, inputs, farm practices, crops
IN = "Industry, Infrastructure, Energy & Services"    # core industries, MSMEs, PLI, infra finance, minerals, energy, e-commerce
IG = "Inclusive Growth, Welfare & Demography"         # SHGs, financial-inclusion index, fertility, demography

L2 = {
    "Test 15 Basic Concepts, Money & Banking": [MC, MB, FM],
    "Test 16 Growth, Development & External Sector": [EX, GD],
    "Test 17 Fiscal Policy, Budget & Economic Survey": [FB, FT],
    "Test 18 Sectors of the Economy & Inclusive Growth": [AG, IN, IG],
}

TAG = {
 # 2015
 ("2015",2):FT, ("2015",4):FT, ("2015",8):IN, ("2015",11):AG, ("2015",13):AG, ("2015",22):MB, ("2015",24):AG,
 ("2015",29):MC, ("2015",34):EX, ("2015",58):EX, ("2015",62):AG, ("2015",65):MB, ("2015",81):MC, ("2015",86):MB,
 ("2015",87):MC, ("2015",90):GD, ("2015",94):EX, ("2015",97):AG, ("2015",98):FB, ("2015",99):EX, ("2015",100):IN,
 # 2016
 ("2016",3):FB, ("2016",4):MB, ("2016",8):FM, ("2016",12):FB, ("2016",18):EX, ("2016",24):AG, ("2016",29):MB,
 ("2016",37):IN, ("2016",43):MB, ("2016",56):MB, ("2016",60):FT, ("2016",61):IN, ("2016",62):IN, ("2016",71):FM,
 ("2016",83):AG,
 # 2017
 ("2017",11):MB, ("2017",20):FT, ("2017",27):EX, ("2017",33):AG, ("2017",40):MB, ("2017",55):IN, ("2017",64):MB,
 ("2017",71):AG, ("2017",77):GD, ("2017",79):FM, ("2017",81):FT, ("2017",94):FB,
 # 2020
 ("2020",17):EX, ("2020",49):EX, ("2020",50):MB, ("2020",51):EX, ("2020",52):EX, ("2020",53):IN, ("2020",54):FM,
 ("2020",56):EX, ("2020",57):MB, ("2020",58):GD, ("2020",59):MB, ("2020",60):FM, ("2020",61):AG, ("2020",62):FM,
 ("2020",63):AG, ("2020",66):AG, ("2020",67):MC, ("2020",69):AG, ("2020",70):FM, ("2020",80):AG, ("2020",83):AG,
 ("2020",84):IN, ("2020",86):AG, ("2020",87):AG, ("2020",89):AG, ("2020",90):AG, ("2020",91):AG, ("2020",94):AG,
 # 2021
 ("2021",3):MC, ("2021",4):MC, ("2021",5):MB, ("2021",6):FM, ("2021",7):EX, ("2021",8):EX, ("2021",9):FT,
 ("2021",10):FB, ("2021",11):MB, ("2021",12):MC, ("2021",13):FM, ("2021",15):MB, ("2021",51):AG, ("2021",52):AG,
 ("2021",57):AG, ("2021",59):AG, ("2021",63):AG,
 # 2022
 ("2022",1):EX, ("2022",2):EX, ("2022",3):MB, ("2022",4):EX, ("2022",5):FM, ("2022",6):IN, ("2022",7):MC,
 ("2022",8):FT, ("2022",9):FB, ("2022",10):FM, ("2022",22):AG, ("2022",61):EX, ("2022",62):AG, ("2022",63):FM,
 ("2022",64):MB, ("2022",65):FM, ("2022",68):MB, ("2022",79):AG,
 # 2023
 ("2023",21):FM, ("2023",22):MB, ("2023",23):FM, ("2023",24):MB, ("2023",25):FM, ("2023",26):AG, ("2023",27):AG,
 ("2023",28):MC, ("2023",66):IN, ("2023",71):IN, ("2023",72):FM, ("2023",73):FM, ("2023",74):IG, ("2023",88):IN,
 # 2024
 ("2024",27):IN, ("2024",40):FM, ("2024",41):IG, ("2024",42):FM, ("2024",43):FM, ("2024",44):FM, ("2024",45):MC,
 ("2024",46):IN, ("2024",47):MC, ("2024",49):MB, ("2024",50):IN, ("2024",51):EX, ("2024",52):FM, ("2024",53):FM,
 ("2024",67):IG, ("2024",92):EX,
 # 2025
 ("2025",1):FM, ("2025",2):MB, ("2025",4):IN, ("2025",5):FT, ("2025",7):FM, ("2025",8):FM, ("2025",10):FB,
 ("2025",24):AG, ("2025",60):IN, ("2025",61):FB, ("2025",63):IN, ("2025",65):FB, ("2025",66):FT, ("2025",67):EX,
 ("2025",68):FM, ("2025",89):IN,
 # 2026
 ("2026",28):AG, ("2026",29):IN, ("2026",35):IN, ("2026",83):IN, ("2026",86):FM, ("2026",87):IN, ("2026",88):IG,
 ("2026",89):IN, ("2026",90):FM, ("2026",91):FM, ("2026",92):FM, ("2026",93):FM, ("2026",94):FB, ("2026",95):IN,
 ("2026",96):FM, ("2026",97):FM, ("2026",98):GD, ("2026",99):MB, ("2026",100):GD,
}

# Question format of each 2023-26 question, read from its option set:
#   mcq = single answer (incl. 2024-Q47's fixed/working-capital classification and 2025-Q65's numerical);
#   statement_based = 2-statement, "How many" counts, or combination codes ("1 and 3", "I, II and III");
#   assertion_reason = Statement-I/II (2023-Q21, Q22, Q23, Q88; 2024-Q51, Q52; 2025-Q5, Q7, Q63, Q89);
#   match_the_following = pairs (2026-Q83 'NOT correctly matched', 2026-Q98 committee pairs).
M, S, A, P = "mcq", "statement_based", "assertion_reason", "match_the_following"
TYPE = {
 ("2023",21):A, ("2023",22):A, ("2023",23):A, ("2023",24):M, ("2023",25):S, ("2023",26):M, ("2023",27):S,
 ("2023",28):S, ("2023",66):S, ("2023",71):S, ("2023",72):S, ("2023",73):M, ("2023",74):S, ("2023",88):A,
 ("2024",27):S, ("2024",40):M, ("2024",41):M, ("2024",42):S, ("2024",43):S, ("2024",44):S, ("2024",45):S,
 ("2024",46):S, ("2024",47):M, ("2024",49):S, ("2024",50):S, ("2024",51):A, ("2024",52):A, ("2024",53):S,
 ("2024",67):S, ("2024",92):S,
 ("2025",1):S, ("2025",2):S, ("2025",4):S, ("2025",5):A, ("2025",7):A, ("2025",8):S, ("2025",10):S,
 ("2025",24):S, ("2025",60):S, ("2025",61):S, ("2025",63):A, ("2025",65):M, ("2025",66):S, ("2025",67):S,
 ("2025",68):S, ("2025",89):A,
 ("2026",28):S, ("2026",29):S, ("2026",35):S, ("2026",83):P, ("2026",86):S, ("2026",87):M, ("2026",88):M,
 ("2026",89):M, ("2026",90):M, ("2026",91):S, ("2026",92):M, ("2026",93):S, ("2026",94):M, ("2026",95):S,
 ("2026",96):S, ("2026",97):S, ("2026",98):P, ("2026",99):S, ("2026",100):S,
}

# Difficulty: the header label of each 2023-26 question; a hyphenated label takes the lower
# band (the rule used for Polity, Environment and Geography).
BAND = {"easy": "easy", "med": "medium", "medium": "medium", "hard": "hard",
        "easy-medium": "easy", "medium-hard": "medium"}


def main():
    allrows = list(csv.DictReader(open(SRC, encoding="utf-8")))
    rows = [r for r in allrows if r["subject"] == "Economy"]
    keys = {(r["year"], int(r["question_number"])) for r in rows}
    assert keys == set(TAG), ("untagged:", sorted(keys - set(TAG)), "extra:", sorted(set(TAG) - keys))
    assert len(rows) == 176

    with open(os.path.join(HERE, "economy_subtopic_retag.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["year", "question_number", "title", "old_sub_topic", "new_sub_topic"])
        for r in sorted(rows, key=lambda r: (int(r["year"]), int(r["question_number"]))):
            w.writerow([r["year"], r["question_number"], r["title"], r["sub_topic"], TAG[(r["year"], int(r["question_number"]))]])

    tag = lambda r: TAG[(r["year"], int(r["question_number"]))]
    print(f"Economy rows: {len(rows)}")
    print("old decoder sub-topics:", dict(collections.Counter(r["sub_topic"] for r in rows).most_common()))

    labels = [MC, MB, FM, EX, GD, FB, FT, AG, IN, IG]
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

    print(f"\n{'sub-topic':48} {'count':>5} {'pooled%':>8} {'recency%':>9} {'2023-26%':>9}")
    for k in sorted(labels, key=lambda k: -rec[k]):
        print(f"{k:48} {pooled[k]:5} {100*pooled[k]/len(rows):7.1f}% {100*rec[k]:8.1f}% {100*recent[k]/n_recent:8.1f}%")
    print(f"{'TOTAL':48} {sum(pooled.values()):5}")

    print("\nLevel-2 roll-up (recency-weighted):")
    for test, subs in L2.items():
        print(f"  {test:52} {100*sum(rec[k] for k in subs):5.1f}%")

    r4 = {k: round(rec[k], 4) for k in labels}
    drift = round(1 - sum(r4.values()), 4)
    top = max(r4, key=r4.get); r4[top] = round(r4[top] + drift, 4)
    print("\nsub_topic_weights (recency, rounded, sum=1):")
    print(r4, "sum =", round(sum(r4.values()), 4))

    # ---- type + difficulty from the 2023-26 corpus -------------------------------------
    text = open(TXT, encoding="utf-8").read()
    heads = re.findall(r"^===== (\d{4}) Q(\d+) \[[^,\]]+, ([^\]]+)\]", text, re.M)
    corpus = [(y, int(q), d.strip().lower()) for y, q, d in heads]
    assert len(corpus) == 65
    assert {(y, q) for y, q, _ in corpus} == set(TYPE), "type map must cover exactly the 2023-26 rows"
    n = len(corpus)
    tcount = collections.Counter(TYPE[(y, q)] for y, q, _ in corpus)
    dcount = collections.Counter(BAND[d] for _, _, d in corpus)
    print(f"\n2023-26 corpus: {n} questions")
    print("question types:", dict(tcount))
    print("difficulty:    ", dict(dcount))
    t4 = {k: round(v / n, 4) for k, v in tcount.items()}
    d4 = {k: round(v / n, 4) for k, v in dcount.items()}
    for m in (t4, d4):
        drift = round(1 - sum(m.values()), 4); top = max(m, key=m.get); m[top] = round(m[top] + drift, 4)
    print("question_type_weights[Economy] =", t4, "sum =", round(sum(t4.values()), 4))
    print("difficulty_weights[Economy]    =", d4, "sum =", round(sum(d4.values()), 4))
    print("\nper year (type):")
    for y in ["2023", "2024", "2025", "2026"]:
        print(" ", y, dict(collections.Counter(TYPE[(yy, q)] for yy, q, _ in corpus if yy == y)))
    print("per year (difficulty):")
    for y in ["2023", "2024", "2025", "2026"]:
        print(" ", y, dict(collections.Counter(BAND[d] for yy, q, d in corpus if yy == y)))


if __name__ == "__main__":
    main()
