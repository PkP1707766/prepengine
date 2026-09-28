# -*- coding: utf-8 -*-
"""Write Geography's content-derived weights (retag_geography_subtopics.py, 2026-09-28) into the
reference config and emit the SQL that applies the same values to the live distribution_config
row e6f68e99 (live_upsc_config.json is then re-pulled from that row, as the gap report expects). Mirrors how Environment's re-tag was recorded: reconciled sub-topic weights with a
_method note and the superseded decoder mapping kept, plus live overrides for type and
difficulty.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
GS1 = os.path.join(HERE, "..", "upsc_gs1_distribution_config.json")
OUT_SQL = os.path.join(HERE, "geography_weights_update.sql")

SUB = {"World Regions, Water Bodies & Places": 0.2099, "Climatology & Biomes": 0.2004,
       "Indian Physiography, Climate & Regions": 0.1666, "Indian Rivers, Lakes & Wetlands": 0.1401,
       "Geomorphology & Earth's Interior": 0.1099, "Resources: Minerals, Energy & Agriculture": 0.0681,
       "Transport, Ports & Human Geography": 0.0677, "Oceanography & Hydrosphere": 0.0373}
TYPE = {"statement_based": 0.5111, "mcq": 0.2444, "assertion_reason": 0.1778, "match_the_following": 0.0667}
DIFF = {"easy": 0.1778, "medium": 0.6, "hard": 0.2222}
assert round(sum(SUB.values()), 4) == 1 and round(sum(TYPE.values()), 4) == 1 and round(sum(DIFF.values()), 4) == 1

SUB_METHOD = ("Content re-tag of all 91 Geography PYQs 2015-2026 from their actual stems "
              "(scratch/retag_geography_subtopics.py -> scratch/geography_subtopic_retag.csv, output in "
              "scratch/geography_retag_output.txt). The decoder filed 81 of 91 under one catch-all 'Physical/Human', "
              "which the earlier reconciliation split 50/50 as an estimate. Recency-weighted with the same linear year "
              "weights as build_config.py. Level-2 roll-up: World Physical (GM+CL+OC+WR) 55.8%, Indian Physical (IR+IP) "
              "30.7%, Human & Economic (EM+HT) 13.6%. No GS1 PYQ 2015-26 tests disaster management; the four hazard "
              "questions (2015-Q5, 2020-Q99, 2023-Q65, 2024-Q3) are physical processes tagged CL/GM.")
TYPE_METHOD = ("Read from each 2023-26 question's option set (n=45): 23 statement (2-statement, 'how many' counts, "
               "combination codes), 11 single-answer MCQ (incl. 2024-Q6 sequence and 2026-Q25 identify-the-river), "
               "8 Statement-I/II (2023-Q63, Q64; 2024-Q1, Q2, Q7; 2025-Q26, Q27, Q28 -- 2024-Q7, 2025-Q27 and Q28 in the "
               "Statement-I/II/III form), 3 pairs (2023-Q2, 2024-Q9, Q10). The playbook's Part E table (T1 14 / T2 9 / "
               "T3 13 / T4 5 / T5 3 / T6 1) counts Statement-I/II only in 2024 and files 2025's three as direct factual; "
               "the 2025 formats were confirmed against published papers. Direct count used, discrepancy flagged.")
DIFF_METHOD = ("2023-26 pooled, the playbook's own evidence window (n=45: 8 easy / 27 medium / 10 hard). A hyphenated "
               "2025 label takes the lower band (the Polity/Environment rule); it affects 2025-Q26 and Q27 "
               "('medium-hard' -> medium). The playbook's E.3 prose rounds the same corpus to about 20/55/25.")


def main():
    g = json.load(open(GS1, encoding="utf-8"))
    rec = g["sub_topic_weights_reconciled"]
    rec["Geography_superseded_decoder_mapping"] = rec["Geography"]
    rec["Geography"] = {**SUB, "_method": SUB_METHOD}
    g["difficulty_weights_live_override"]["Geography"] = {**DIFF, "_method": DIFF_METHOD}
    g["question_type_weights_live_override"]["Geography"] = {**TYPE, "_method": TYPE_METHOD}
    json.dump(g, open(GS1, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


    j = lambda d: json.dumps(d, ensure_ascii=False).replace("'", "''")
    sql = ("update public.distribution_config set\n"
           f"  sub_topic_weights = jsonb_set(sub_topic_weights, '{{Geography}}', '{j(SUB)}'::jsonb),\n"
           f"  question_type_weights = jsonb_set(question_type_weights, '{{Geography}}', '{j(TYPE)}'::jsonb),\n"
           f"  difficulty_weights = jsonb_set(difficulty_weights, '{{Geography}}', '{j(DIFF)}'::jsonb),\n"
           "  updated_at = now()\n"
           "where id = 'e6f68e99-3cc7-45de-8b7e-9de24273ff89' and exam_category = 'upsc'\n"
           "returning sub_topic_weights->'Geography' as sub, question_type_weights->'Geography' as type, difficulty_weights->'Geography' as diff;\n")
    open(OUT_SQL, "w", encoding="utf-8").write(sql)
    print("updated", GS1, "-- apply the SQL, then re-pull live_upsc_config.json from the DB")
    print(sql)


if __name__ == "__main__":
    main()
