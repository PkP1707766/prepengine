# -*- coding: utf-8 -*-
"""Content-based re-tag of the 161 UPSC GS1 Environment & Ecology PYQs (2015-2026).

The decoder labelled 152 of 161 questions 'Biodiversity' / 'Ecology/Biodiversity', so the
config's 94.4% Biodiversity weight was a labelling artifact, not a content fact (the same
problem as Polity's 'Governance'). Each question is tagged from its actual stem
(decoder_<year>_text.txt; 2023-26 from environment_ecology_qs_2023_2026.txt; 2025 from the
paper text in that file), one primary bucket per question.

The nine buckets roll up into the three Level-2 tests the blueprint names for Environment:
  Ecology & Biodiversity                 -> FA, FL, EC
  Climate Change & Disaster Management   -> CS, CA, PW
  Policies & Conservation                -> PA, IL, IC

XS marks 22 rows that are not Environment questions at all (vaccines, genetics, cell biology,
microbiology, physiology) - the decoder filed them under 'Biodiversity'. They are left out of
every Environment weight below rather than moved to Science & Technology: moving them changes
the full-length subject weights, which is a separate decision (flagged, not made here).

Also derives Environment's own question-type and difficulty weights from the 2023-26 questions
(the playbook's per-subject corpus), excluding the one XS row in that window (2024-Q33).
Writes environment_subtopic_retag.csv and prints everything needed for the live config.
"""
import csv, collections, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "upsc_gs1_combined_2015-2026.csv")
TXT = os.path.join(HERE, "environment_ecology_qs_2023_2026.txt")

FA = "Fauna & Animal Behaviour"                  # species identification, behaviour, range, feeding
FL = "Flora, Fungi & Forests"                    # plants, trees, fungi, forest types
EC = "Ecosystems & Ecological Processes"         # food chains, cycles, symbiosis, wetland/ocean functions
CS = "Climate Science & Mitigation"              # GHGs, sinks, sequestration, emissions data, impacts
CA = "Climate Agreements & Carbon Markets"       # UNFCCC/Kyoto/Paris/INDC, REDD+, carbon funds, metrics, climate coalitions
PW = "Pollution, Waste & Resources"              # air/water/soil pollution, pollutants, waste, circular economy, groundwater use
PA = "Protected Areas & Wildlife Protection"     # NPs, TRs, reserves, WPA schedules, species conservation practice
IL = "Indian Environmental Laws & Bodies"        # GEAC, NGRBA, CGWA, BMCs, ESZ committees, national missions/platforms
IC = "International Conventions & Organisations" # IUCN, CITES, UNCCD, Montreal, Rio, TEEB, TRAFFIC, EU laws, UN bodies
XS = "XS: not Environment (S&T biotech/health)"

L2 = {
    "Ecology & Biodiversity": [FA, FL, EC],
    "Climate Change & Disaster Management": [CS, CA, PW],
    "Policies & Conservation": [PA, IL, IC],
}

TAG = {
 # 2015
 ("2015",9):PA, ("2015",12):IC, ("2015",18):PW, ("2015",19):FA, ("2015",25):FA, ("2015",38):FL, ("2015",40):IC,
 ("2015",43):IC, ("2015",52):PA, ("2015",56):CA, ("2015",63):IL, ("2015",72):FL, ("2015",74):CA, ("2015",76):IC,
 ("2015",78):FL, ("2015",84):EC, ("2015",92):XS,
 # 2016
 ("2016",6):CA, ("2016",13):IC, ("2016",22):FA, ("2016",23):IL, ("2016",30):CA, ("2016",31):XS, ("2016",33):IL,
 ("2016",44):FA, ("2016",45):FL, ("2016",52):IC, ("2016",53):FL, ("2016",54):CA, ("2016",55):CA, ("2016",57):IC,
 ("2016",59):XS, ("2016",68):IL, ("2016",86):PW, ("2016",90):FA, ("2016",97):CA,
 # 2017
 ("2017",4):PA, ("2017",6):IC, ("2017",14):PW, ("2017",21):EC, ("2017",22):CS, ("2017",25):CS, ("2017",31):XS,
 ("2017",35):PA, ("2017",45):XS, ("2017",59):PW, ("2017",65):CA, ("2017",67):FA, ("2017",78):XS, ("2017",80):PA,
 ("2017",91):PA, ("2017",95):PA,
 # 2020
 ("2020",37):XS, ("2020",44):XS, ("2020",45):XS, ("2020",47):XS, ("2020",48):PW, ("2020",72):FA, ("2020",73):PA,
 ("2020",74):FA, ("2020",75):PA, ("2020",76):PW, ("2020",77):PA, ("2020",78):PW, ("2020",79):PW, ("2020",81):PA,
 ("2020",85):CA, ("2020",95):PA, ("2020",98):IL, ("2020",100):PA,
 # 2021
 ("2021",16):PW, ("2021",17):PW, ("2021",18):PW, ("2021",19):CS, ("2021",20):FL, ("2021",21):FL, ("2021",22):EC,
 ("2021",23):FA, ("2021",24):CA, ("2021",25):PW, ("2021",26):FA, ("2021",27):EC, ("2021",28):EC, ("2021",29):CA,
 ("2021",30):EC, ("2021",65):XS, ("2021",66):XS, ("2021",67):XS, ("2021",69):XS, ("2021",70):XS, ("2021",73):XS,
 ("2021",75):PW,
 # 2022
 ("2022",21):CS, ("2022",37):XS, ("2022",38):XS, ("2022",39):XS, ("2022",41):CA, ("2022",42):CA, ("2022",43):EC,
 ("2022",44):PW, ("2022",45):FL, ("2022",47):FA, ("2022",48):FL, ("2022",49):PA, ("2022",50):PA, ("2022",80):CA,
 ("2022",89):PA, ("2022",90):FA, ("2022",97):XS, ("2022",98):PW, ("2022",99):XS, ("2022",100):PW,
 # 2023
 ("2023",3):FL, ("2023",12):FA, ("2023",13):IC, ("2023",14):FA, ("2023",15):FA, ("2023",16):FL, ("2023",17):FA,
 ("2023",18):EC, ("2023",19):FA, ("2023",20):CS, ("2023",38):PA, ("2023",59):PW, ("2023",68):CS, ("2023",76):PW,
 ("2023",79):IL,
 # 2024
 ("2024",16):CS, ("2024",17):PW, ("2024",18):EC, ("2024",19):FL, ("2024",20):FA, ("2024",21):FA, ("2024",22):PW,
 ("2024",23):FA, ("2024",25):PA, ("2024",28):EC, ("2024",29):FA, ("2024",30):FL, ("2024",33):XS, ("2024",90):PW,
 ("2024",96):CA,
 # 2025 (paper text in environment_ecology_qs_2023_2026.txt)
 ("2025",9):PW, ("2025",29):CS, ("2025",31):CS, ("2025",37):FA, ("2025",38):CS, ("2025",39):FL, ("2025",40):EC,
 ("2025",44):PW, ("2025",64):CS, ("2025",90):IC,
 # 2026
 ("2026",21):CA, ("2026",22):FA, ("2026",23):CS, ("2026",27):FA, ("2026",32):PA, ("2026",36):FL, ("2026",38):IC,
 ("2026",40):CA, ("2026",77):IL,
}

# Question format of each 2023-26 question, read from its option set:
#   mcq = single-answer factual; statement_based = 2-statement ("1 only/2 only/Both/Neither"),
#   "How many ..." counts, or "1 and 2 only" combinations; assertion_reason = Statement-I/II
#   (and the 2025 Statement-I/II/III variant, marked *); match_the_following = pairs.
M, S, A, P = "mcq", "statement_based", "assertion_reason", "match_the_following"
TYPE = {
 ("2023",3):S, ("2023",12):A, ("2023",13):M, ("2023",14):S, ("2023",15):M, ("2023",16):S, ("2023",17):S,
 ("2023",18):S, ("2023",19):M, ("2023",20):S, ("2023",38):S, ("2023",59):S, ("2023",68):S, ("2023",76):A,
 ("2023",79):S,
 ("2024",16):M, ("2024",17):S, ("2024",18):S, ("2024",19):S, ("2024",20):A, ("2024",21):M, ("2024",22):S,
 ("2024",23):P, ("2024",25):S, ("2024",28):S, ("2024",29):S, ("2024",30):S, ("2024",90):M, ("2024",96):S,
 ("2025",9):A, ("2025",29):S, ("2025",31):A, ("2025",37):S, ("2025",38):S, ("2025",39):P, ("2025",40):S,
 ("2025",44):S, ("2025",64):S, ("2025",90):M,
 ("2026",21):S, ("2026",22):S, ("2026",23):S, ("2026",27):S, ("2026",32):S, ("2026",36):S, ("2026",38):M,
 ("2026",40):M, ("2026",77):S,
}
AR_3STATEMENT = {("2025",9), ("2025",31)}  # "Both Statement II and Statement III ... explain Statement I"

# Difficulty: the header label of each 2023-26 question. A hyphenated label takes the lower
# band - the rule that reproduces Polity's live 3/34/19 (its 7 'medium-hard' count as medium).
BAND = {"easy": "easy", "med": "medium", "medium": "medium", "hard": "hard",
        "easy-medium": "easy", "medium-hard": "medium"}


def main():
    rows = [r for r in csv.DictReader(open(SRC, encoding="utf-8")) if r["subject"] == "Environment & Ecology"]
    keys = {(r["year"], int(r["question_number"])) for r in rows}
    assert keys == set(TAG), ("untagged:", sorted(keys - set(TAG)), "extra:", sorted(set(TAG) - keys))
    assert len(rows) == 161

    with open(os.path.join(HERE, "environment_subtopic_retag.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["year", "question_number", "title", "old_sub_topic", "new_sub_topic"])
        for r in rows:
            w.writerow([r["year"], r["question_number"], r["title"], r["sub_topic"], TAG[(r["year"], int(r["question_number"]))]])

    tag = lambda r: TAG[(r["year"], int(r["question_number"]))]
    env = [r for r in rows if tag(r) != XS]
    xs = [r for r in rows if tag(r) == XS]
    print(f"Environment rows: {len(rows)}   not Environment (XS): {len(xs)}   kept: {len(env)}")
    old = collections.Counter(r["sub_topic"] for r in rows)
    print("old decoder sub-topics:", dict(old.most_common()))

    labels = [FA, FL, EC, CS, CA, PW, PA, IL, IC]
    years = sorted({r["year"] for r in env}, key=int)
    wmap = {y: i + 1 for i, y in enumerate(years)}  # same linear recency weights as build_config.py
    pooled = collections.Counter(tag(r) for r in env)
    recent = collections.Counter(tag(r) for r in env if int(r["year"]) >= 2023)
    n_recent = sum(recent.values())
    acc = collections.Counter(); tw = 0
    for y in years:
        ry = [r for r in env if r["year"] == y]
        cy = collections.Counter(tag(r) for r in ry)
        for k in labels: acc[k] += wmap[y] * cy[k] / len(ry)
        tw += wmap[y]
    rec = {k: acc[k] / tw for k in labels}

    print(f"\n{'sub-topic':44} {'count':>5} {'pooled%':>8} {'recency%':>9} {'2023-26%':>9}")
    for k in sorted(labels, key=lambda k: -rec[k]):
        print(f"{k:44} {pooled[k]:5} {100*pooled[k]/len(env):7.1f}% {100*rec[k]:8.1f}% {100*recent[k]/n_recent:8.1f}%")
    print(f"{'TOTAL':44} {sum(pooled.values()):5}")

    print("\nLevel-2 roll-up (recency-weighted):")
    for test, subs in L2.items():
        print(f"  {test:40} {100*sum(rec[k] for k in subs):5.1f}%   ({', '.join(subs)})")

    r4 = {k: round(rec[k], 4) for k in labels}
    drift = round(1 - sum(r4.values()), 4)
    top = max(r4, key=r4.get); r4[top] = round(r4[top] + drift, 4)
    print("\nsub_topic_weights (recency, rounded, sum=1):")
    print(r4, "sum =", round(sum(r4.values()), 4))

    # ---- type + difficulty from the 2023-26 corpus -------------------------------------
    text = open(TXT, encoding="utf-8").read()
    heads = re.findall(r"^===== (\d{4}) Q(\d+) \[[^,\]]+, ([^\]]+)\]", text, re.M)
    corpus = [(y, int(q), d.strip().lower()) for y, q, d in heads]
    assert len(corpus) == 49
    corpus = [c for c in corpus if TAG[(c[0], c[1])] != XS]
    assert {(y, q) for y, q, _ in corpus} == set(TYPE), "type map must cover exactly the kept 2023-26 rows"
    n = len(corpus)
    tcount = collections.Counter(TYPE[(y, q)] for y, q, _ in corpus)
    dcount = collections.Counter(BAND[d] for _, _, d in corpus)
    print(f"\n2023-26 corpus: 49 questions, {49 - n} not Environment -> {n}")
    print("question types:", dict(tcount), f"(assertion_reason includes {len(AR_3STATEMENT)} Statement-I/II/III)")
    print("difficulty:    ", dict(dcount))
    t4 = {k: round(v / n, 4) for k, v in tcount.items()}
    d4 = {k: round(v / n, 4) for k, v in dcount.items()}
    for m in (t4, d4):
        drift = round(1 - sum(m.values()), 4); top = max(m, key=m.get); m[top] = round(m[top] + drift, 4)
    print("question_type_weights[Environment & Ecology] =", t4, "sum =", round(sum(t4.values()), 4))
    print("difficulty_weights[Environment & Ecology]    =", d4, "sum =", round(sum(d4.values()), 4))
    print("\nper year (type):")
    for y in ["2023", "2024", "2025", "2026"]:
        print(" ", y, dict(collections.Counter(TYPE[(yy, q)] for yy, q, _ in corpus if yy == y)))


if __name__ == "__main__":
    main()
