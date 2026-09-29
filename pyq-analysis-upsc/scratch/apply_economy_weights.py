# -*- coding: utf-8 -*-
"""Write Economy's content-derived weights (retag_economy_subtopics.py, 2026-09-29) into the
reference config and emit the SQL that applies the same values to the live distribution_config
row e6f68e99 (live_upsc_config.json is then re-pulled from that row, as the gap report expects).
Mirrors how Environment's and Geography's re-tags were recorded: reconciled sub-topic weights with a
_method note and the superseded mapping kept, plus live overrides for type and difficulty.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
GS1 = os.path.join(HERE, "..", "upsc_gs1_distribution_config.json")
OUT_SQL = os.path.join(HERE, "economy_weights_update.sql")

SUB = {"Financial Markets, Instruments & Fintech": 0.2627, "Industry, Infrastructure, Energy & Services": 0.1777,
       "Agriculture & Food Economy": 0.1323, "Money, Banking & Monetary Policy": 0.115,
       "External Sector & International Institutions": 0.0868, "Budget, Deficits & Public Debt": 0.0619,
       "Macro Concepts, National Income & Inflation": 0.0546, "Taxation & Fiscal Federalism": 0.0451,
       "Inclusive Growth, Welfare & Demography": 0.0368, "Growth, Development, Poverty & Planning": 0.0271}
TYPE = {"statement_based": 0.6154, "mcq": 0.2, "assertion_reason": 0.1538, "match_the_following": 0.0308}
DIFF = {"easy": 0.2, "medium": 0.6, "hard": 0.2}
assert round(sum(SUB.values()), 4) == 1 and round(sum(TYPE.values()), 4) == 1 and round(sum(DIFF.values()), 4) == 1

SUB_METHOD = ("Content re-tag of all 176 Economy PYQs 2015-2026 from their actual stems "
              "(scratch/retag_economy_subtopics.py -> scratch/economy_subtopic_retag.csv, output in "
              "scratch/economy_retag_output.txt). The decoder filed 126 of 176 under one catch-all 'Macroeconomics' "
              "and 32 under 'Agriculture'; the earlier reconciliation mapped Agriculture to 'Five-Year Plans & Policy' and "
              "carved Fintech and Critical Minerals from named 2026 examples. Recency-weighted with the same linear year "
              "weights as build_config.py. Level-2 roll-up: Test 15 Basic Concepts, Money & Banking (MC+MB+FM) 43.2%, "
              "Test 16 Growth, Development & External Sector (EX+GD) 11.4%, Test 17 Fiscal Policy & Budget (FB+FT) 10.7%, "
              "Test 18 Sectors & Inclusive Growth (AG+IN+IG) 34.7%. Farm-practice questions filed as Economy (biochar, "
              "fertigation, zero tillage, SRI) stay in Agriculture & Food Economy.")
TYPE_METHOD = ("Read from each 2023-26 question's option set (n=65): 40 statement (2-statement, 'how many' counts, "
               "combination codes), 13 single-answer MCQ (incl. 2024-Q47 classification and 2025-Q65 numerical), "
               "10 Statement-I/II (2023-Q21, Q22, Q23, Q88; 2024-Q51, Q52; 2025-Q5, Q7, Q63, Q89), 2 pairs (2026-Q83, Q98). "
               "The 2025 text is two-column OCR in which option blocks of neighbouring questions run together; each 2025 "
               "format was read question by question against the published paper.")
DIFF_METHOD = ("2023-26 pooled (n=65: 13 easy / 39 medium / 13 hard). A hyphenated 2025 label takes the lower band "
               "(the Polity/Environment/Geography rule); it affects 2025-Q4, Q5, Q7 ('easy-medium' -> easy) and Q63, Q66, "
               "Q89 ('medium-hard' -> medium). 2026 is the hardest year (8 of 19 hard).")


def main():
    g = json.load(open(GS1, encoding="utf-8"))
    rec = g["sub_topic_weights_reconciled"]
    rec["Economy_superseded_reconciled_mapping"] = rec["Economy"]
    rec["Economy"] = {**SUB, "_method": SUB_METHOD}
    g["difficulty_weights_live_override"]["Economy"] = {**DIFF, "_method": DIFF_METHOD}
    g["question_type_weights_live_override"]["Economy"] = {**TYPE, "_method": TYPE_METHOD}
    json.dump(g, open(GS1, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    j = lambda d: json.dumps(d, ensure_ascii=False).replace("'", "''")
    sql = ("update public.distribution_config set\n"
           f"  sub_topic_weights = jsonb_set(sub_topic_weights, '{{Economy}}', '{j(SUB)}'::jsonb),\n"
           f"  question_type_weights = jsonb_set(question_type_weights, '{{Economy}}', '{j(TYPE)}'::jsonb),\n"
           f"  difficulty_weights = jsonb_set(difficulty_weights, '{{Economy}}', '{j(DIFF)}'::jsonb),\n"
           "  updated_at = now()\n"
           "where id = 'e6f68e99-3cc7-45de-8b7e-9de24273ff89' and exam_category = 'upsc'\n"
           "returning sub_topic_weights->'Economy' as sub, question_type_weights->'Economy' as type, difficulty_weights->'Economy' as diff;\n")
    open(OUT_SQL, "w", encoding="utf-8").write(sql)
    print("updated", GS1, "-- apply the SQL, then re-pull live_upsc_config.json from the DB")
    print(sql)


if __name__ == "__main__":
    main()
