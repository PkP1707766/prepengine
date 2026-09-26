# -*- coding: utf-8 -*-
"""Content-based re-tag of the 148 UPSC GS1 Polity PYQs (2015-2026).

The source decoder labelled almost every Polity question 'Governance' (135/148), so the
config's 86% Governance weight was a labelling artifact, not a content fact. Each question
below was tagged from its actual stem (decoder_<year>_text.txt; 2025 from its descriptive
title), one primary bucket per question. Writes the per-question tags to
polity_subtopic_retag.csv and prints the weight split three ways.
"""
import csv, collections, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "upsc_gs1_combined_2015-2026.csv")

CF = "Constitutional Framework"             # Preamble, philosophy & political theory, salient features, amendment, schedules/parts, citizenship
FR = "Fundamental Rights, DPSP & Duties"    # incl. writs (Art 32/226 remedies)
PL = "Parliament & State Legislature"       # bills, budget procedure, sessions, presiding officers, committees, anti-defection
EX = "Union & State Executive"              # President, Governor, PM/CoM, ordinances, pardon
JU = "Judiciary"                            # courts, judicial review, contempt, judges
FD = "Federalism & Special Provisions"      # Centre-State, 7th Sch, emergency/President's Rule, 5th/6th Sch, SC/ST special provisions
BO = "Constitutional & Statutory Bodies"    # FC, CAG, AG/SG, NITI, NEC, Lokpal, councils
EL = "Elections"                            # ECI, RPA, delimitation, franchise, seat reservation
PR = "Panchayati Raj & Local Governance"
SL = "Statutory-Laws"                       # question turns on a named Act's provisions
JV = "Judicial-Verdicts"                    # answer turns on a landmark judgment
GV = "Governance"                           # non-constitutional administration, agencies, schemes, ethics

TAG = {
 # 2015
 ("2015",7):FR, ("2015",27):PL, ("2015",37):PL, ("2015",42):BO, ("2015",44):EX, ("2015",59):FD, ("2015",60):PL,
 ("2015",61):JU, ("2015",82):PL, ("2015",83):FR, ("2015",85):PR, ("2015",89):FR, ("2015",91):CF,
 # 2016
 ("2016",1):PL, ("2016",25):GV, ("2016",40):SL, ("2016",95):FD, ("2016",100):PR,
 # 2017
 ("2017",1):PL, ("2017",5):CF, ("2017",7):FR, ("2017",8):CF, ("2017",16):PR, ("2017",17):FR, ("2017",36):FR,
 ("2017",38):CF, ("2017",42):CF, ("2017",46):CF, ("2017",47):CF, ("2017",48):CF, ("2017",50):PL, ("2017",57):EL,
 ("2017",76):EL, ("2017",86):EL, ("2017",90):EL, ("2017",92):JU, ("2017",96):FD, ("2017",97):FR, ("2017",99):CF,
 ("2017",100):FD,
 # 2020
 ("2020",1):JV, ("2020",2):PL, ("2020",3):GV, ("2020",4):FR, ("2020",5):FR, ("2020",6):SL, ("2020",7):CF,
 ("2020",8):CF, ("2020",9):SL, ("2020",11):CF, ("2020",12):FR, ("2020",13):JV, ("2020",14):CF, ("2020",15):GV,
 ("2020",16):CF, ("2020",18):FR, ("2020",19):EX, ("2020",20):PL,
 # 2021
 ("2021",1):GV, ("2021",2):SL, ("2021",77):CF, ("2021",78):GV, ("2021",79):JV, ("2021",80):EL, ("2021",81):PR,
 ("2021",82):SL, ("2021",83):SL, ("2021",84):SL, ("2021",85):JV, ("2021",86):FD, ("2021",87):CF, ("2021",88):JU,
 ("2021",89):CF, ("2021",90):CF, ("2021",91):FR, ("2021",92):FR, ("2021",93):CF, ("2021",94):CF,
 # 2022
 ("2022",11):JU, ("2022",12):SL, ("2022",13):CF, ("2022",14):EX, ("2022",15):PL, ("2022",16):PL, ("2022",17):BO,
 ("2022",18):FR, ("2022",20):PL, ("2022",71):GV, ("2022",72):GV, ("2022",73):FD, ("2022",74):GV, ("2022",75):SL,
 # 2023
 ("2023",29):BO, ("2023",31):FR, ("2023",32):FD, ("2023",33):CF, ("2023",34):CF, ("2023",35):BO, ("2023",36):EX,
 ("2023",37):PL, ("2023",39):FD, ("2023",40):JV, ("2023",75):FD, ("2023",77):FD, ("2023",80):EX, ("2023",91):SL,
 ("2023",92):SL,
 # 2024
 ("2024",66):CF, ("2024",68):PL, ("2024",70):BO, ("2024",71):EL, ("2024",72):CF, ("2024",74):CF, ("2024",75):FD,
 ("2024",76):JV, ("2024",80):PL, ("2024",81):EL, ("2024",83):FR, ("2024",84):FD, ("2024",85):PL, ("2024",93):PL,
 ("2024",94):PL, ("2024",95):PL,
 # 2025 (tagged from the descriptive titles in the CSV)
 ("2025",3):GV, ("2025",51):EX, ("2025",53):BO, ("2025",54):EX, ("2025",55):FR, ("2025",56):FD, ("2025",58):CF,
 ("2025",59):EX, ("2025",86):EX, ("2025",87):PL, ("2025",88):PL, ("2025",91):PR, ("2025",98):BO,
 # 2026
 ("2026",51):GV, ("2026",52):GV, ("2026",53):GV, ("2026",54):FR, ("2026",55):CF, ("2026",56):SL, ("2026",57):FD,
 ("2026",58):PL, ("2026",59):PL, ("2026",62):SL, ("2026",63):GV, ("2026",74):PR,
}

rows = [r for r in csv.DictReader(open(SRC, encoding="utf-8")) if r["subject"] == "Polity"]
keys = {(r["year"], int(r["question_number"])) for r in rows}
assert keys == set(TAG), ("untagged:", sorted(keys - set(TAG)), "extra:", sorted(set(TAG) - keys))
assert len(rows) == 148

with open(os.path.join(HERE, "polity_subtopic_retag.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["year", "question_number", "title", "old_sub_topic", "new_sub_topic"])
    for r in rows:
        w.writerow([r["year"], r["question_number"], r["title"], r["sub_topic"], TAG[(r["year"], int(r["question_number"]))]])

years = sorted({r["year"] for r in rows}, key=int)
wmap = {y: i + 1 for i, y in enumerate(years)}  # same linear recency weights as build_config.py
labels = [CF, FR, PL, EX, JU, FD, BO, EL, PR, SL, JV, GV]

pooled = collections.Counter(TAG[(r["year"], int(r["question_number"]))] for r in rows)
recent = collections.Counter(TAG[(r["year"], int(r["question_number"]))] for r in rows if int(r["year"]) >= 2023)
n_recent = sum(recent.values())
acc = collections.Counter(); tw = 0
for y in years:
    ry = [r for r in rows if r["year"] == y]
    cy = collections.Counter(TAG[(r["year"], int(r["question_number"]))] for r in ry)
    for k in labels: acc[k] += wmap[y] * cy[k] / len(ry)
    tw += wmap[y]
rec = {k: acc[k] / tw for k in labels}

print(f"{'sub-topic':36} {'count':>5} {'pooled%':>8} {'recency%':>9} {'2023-26%':>9}")
for k in sorted(labels, key=lambda k: -rec[k]):
    print(f"{k:36} {pooled[k]:5} {100*pooled[k]/len(rows):7.1f}% {100*rec[k]:8.1f}% {100*recent[k]/n_recent:8.1f}%")
print(f"{'TOTAL':36} {sum(pooled.values()):5}")
print("\nrecency weights (rounded, sum=1):")
r4 = {k: round(rec[k], 4) for k in labels}
drift = round(1 - sum(r4.values()), 4)
top = max(r4, key=r4.get); r4[top] = round(r4[top] + drift, 4)
print(r4, "sum =", round(sum(r4.values()), 4))
