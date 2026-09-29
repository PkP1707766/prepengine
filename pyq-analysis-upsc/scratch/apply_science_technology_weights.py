# -*- coding: utf-8 -*-
"""Write Science & Technology's content-derived weights (retag_science_technology_subtopics.py, 2026-09-29) into the
reference config and emit the SQL that applies the same values to the live distribution_config
row e6f68e99 (live_upsc_config.json is then re-pulled from that row, as the gap report expects).
Mirrors how the Environment, Geography and Economy re-tags were recorded: reconciled sub-topic weights with a
_method note and the superseded mapping kept, plus live overrides for type and difficulty.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
GS1 = os.path.join(HERE, "..", "upsc_gs1_distribution_config.json")
OUT_SQL = os.path.join(HERE, "science_technology_weights_update.sql")

SUB = {"IT, Communication & Emerging Technologies": 0.2203, "Energy & Environmental Technology": 0.1786,
       "Chemistry & Materials": 0.1412, "Astronomy & Earth Science": 0.1281,
       "Defence, Aerospace & Security Technology": 0.1008, "Physics & Everyday Science": 0.0853,
       "Biology, Health & Biotechnology": 0.0846, "Space Technology & Missions": 0.0611}
TYPE = {"statement_based": 0.6735, "mcq": 0.2245, "assertion_reason": 0.102}
DIFF = {"easy": 0.2041, "medium": 0.6122, "hard": 0.1837}
assert round(sum(SUB.values()), 4) == 1 and round(sum(TYPE.values()), 4) == 1 and round(sum(DIFF.values()), 4) == 1

SUB_METHOD = ("Content re-tag of all 95 S&T PYQs 2015-2026 from their actual stems "
              "(scratch/retag_science_technology_subtopics.py -> scratch/science_technology_subtopic_retag.csv, output in "
              "scratch/science_technology_retag_output.txt). The decoder filed 86 of 95 under one catch-all 'Tech & Innovation'; "
              "the earlier reconciliation left it at 0.85 and carved Space-Missions and Defence-Technology from named examples. "
              "Recency-weighted with the same linear year weights as build_config.py. Level-2 roll-up: Test 19 General Science "
              "(PH+CH+BI+AS) 43.9%, Test 20 Applied S&T & Agriculture (ST+IT+EN+DF) 56.1%. No S&T PYQ is primarily about "
              "farming, so Test 20's agriculture content is drafted inside the applied buckets.")
TYPE_METHOD = ("Read from each 2023-26 question's option set (n=49): 33 statement (2-statement, 'how many' counts, "
               "combination codes), 11 single-answer MCQ, 5 Statement-I/II (2023-Q11, 2024-Q32, 2025-Q81; 2025-Q33 and Q50 in "
               "the Statement-I/II/III form). No pairs question in 2023-26, so no match_the_following weight. The 2025 text is "
               "two-column OCR; each 2025 format was read question by question.")
DIFF_METHOD = ("2023-26 pooled (n=49: 10 easy / 30 medium / 9 hard). A hyphenated 2025 label takes the lower band "
               "(the rule used for every subject so far); it affects 2025-Q41, Q85 ('easy-medium' -> easy) and Q33, Q47 "
               "('medium-hard' -> medium). 2026 has no easy S&T question.")


def main():
    g = json.load(open(GS1, encoding="utf-8"))
    rec = g["sub_topic_weights_reconciled"]
    rec["Science & Technology_superseded_reconciled_mapping"] = rec["Science & Technology"]
    rec["Science & Technology"] = {**SUB, "_method": SUB_METHOD}
    g["difficulty_weights_live_override"]["Science & Technology"] = {**DIFF, "_method": DIFF_METHOD}
    g["question_type_weights_live_override"]["Science & Technology"] = {**TYPE, "_method": TYPE_METHOD}
    json.dump(g, open(GS1, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    j = lambda d: json.dumps(d, ensure_ascii=False).replace("'", "''")
    sql = ("update public.distribution_config set\n"
           f"  sub_topic_weights = jsonb_set(sub_topic_weights, '{{\"Science & Technology\"}}', '{j(SUB)}'::jsonb),\n"
           f"  question_type_weights = jsonb_set(question_type_weights, '{{\"Science & Technology\"}}', '{j(TYPE)}'::jsonb),\n"
           f"  difficulty_weights = jsonb_set(difficulty_weights, '{{\"Science & Technology\"}}', '{j(DIFF)}'::jsonb),\n"
           "  updated_at = now()\n"
           "where id = 'e6f68e99-3cc7-45de-8b7e-9de24273ff89' and exam_category = 'upsc'\n"
           "returning sub_topic_weights->'Science & Technology' as sub, question_type_weights->'Science & Technology' as type, difficulty_weights->'Science & Technology' as diff;\n")
    open(OUT_SQL, "w", encoding="utf-8").write(sql)
    print("updated", GS1, "-- apply the SQL, then re-pull live_upsc_config.json from the DB")
    print(sql)


if __name__ == "__main__":
    main()
