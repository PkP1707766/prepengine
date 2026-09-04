"""Shared schema for the BPSC PYQ dataset. Imported by each tag_<paper>.py.

Conventions (confirmed with user):
- Tag from the ENGLISH version (BPSC's official standard).
- correct_option comes from the official answer key, matched by the paper's Series/Set.
  Values: A/B/C/D (/E for 5-option papers), or "Deleted" if BPSC dropped the question.
- difficulty_guess is a JUDGMENT CALL, not an official rating.
- ambiguous_subject=TRUE when a question straddles subjects: pick best primary + note the other.
- is_all_or_none_correct: FUNCTIONAL — TRUE when the correct answer means ALL listed items
  or NONE of them (includes coded combos like "1, 2 and 3" when all items are right).
- all_none_literal_phrasing: TRUE only when the correct option's literal text is
  "All of the above" / "None of the above" (NOT functional-all combos).
"""
import csv

COLUMNS = [
    "year", "exam_date", "paper_variant", "booklet_series", "question_number",
    "subject", "sub_topic", "question_type", "option_count", "statement_count",
    "list_item_count", "option_combination_pattern",
    "is_all_or_none_correct", "all_none_literal_phrasing",
    "correct_option", "key_status", "difficulty_guess",
    "ambiguous_subject", "ambiguous_note", "ca_recency_months",
    "source_type_guess", "question_text_en",
]

def write_rows(rows, out_path):
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    return len(rows)
