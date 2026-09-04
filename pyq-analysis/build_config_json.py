# -*- coding: utf-8 -*-
"""
Builds the exact distribution_config JSON to push into the live Supabase table,
per user's explicit instructions:
  - subject_weights: Bihar-Specific = 14.3% (recency-weighted), others = pooled flat %
  - reasoning_aptitude: fixed-count equivalent (10/150), not proportional to the pool
  - question_type_weights: nested per-subject (statement_based baseline excl. 69th)
  - sub_topic_weights: nested per-subject, pooled
  - difficulty_weights: pooled across all 6 cycles
  - The 12 SME-recheck-flagged rows (sme_recheck_70th_family.csv) are EXCLUDED from
    every computation below, per explicit instruction -- their tagging has zero
    influence on the pushed config, not just their unverified answers.
"""
import csv, json, os
from collections import Counter, defaultdict

DIR = os.path.dirname(__file__)
YEAR_ORDER = ["67th-reexam", "68th", "69th", "70th", "70th-reexam", "71st"]
RECENCY_WEIGHTS = {y: i + 1 for i, y in enumerate(YEAR_ORDER)}
SUBJECTS = ["History","Geography","Polity","Economy","Science & Technology",
            "Environment & Ecology","Current Affairs","Bihar-Specific","Reasoning & Aptitude"]
QTYPES = ["simple_mcq","statement_based","match_the_following","assertion_reason","reasoning_aptitude"]

with open(os.path.join(DIR, "combined_dataset.csv"), encoding="utf-8") as f:
    all_rows = list(csv.DictReader(f))

excluded = [r for r in all_rows if r["needs_sme_recheck"] == "TRUE"]
rows = [r for r in all_rows if r["needs_sme_recheck"] != "TRUE"]
print(f"Base dataset: {len(all_rows)} rows. Excluded (SME recheck): {len(excluded)}. Used for config: {len(rows)}.")

by_year = defaultdict(list)
for r in rows:
    by_year[r["year"]].append(r)

def pct(n, d):
    return 100.0 * n / d if d else 0.0

# ---------- subject_weights ----------
subject_weights = {}
for subj in SUBJECTS:
    if subj == "Bihar-Specific":
        w_sum = sum(RECENCY_WEIGHTS.values())
        weighted = 0.0
        for y in YEAR_ORDER:
            yr = by_year[y]
            n = sum(1 for r in yr if r["subject"] == subj)
            weighted += pct(n, len(yr)) * RECENCY_WEIGHTS[y]
        subject_weights[subj] = round(weighted / w_sum / 100.0, 4)
    elif subj == "Reasoning & Aptitude":
        subject_weights[subj] = round(10 / 150, 4)  # fixed-count equivalent
    else:
        n = sum(1 for r in rows if r["subject"] == subj)
        subject_weights[subj] = round(pct(n, len(rows)) / 100.0, 4)

print("\nsubject_weights (before normalization -- generate.js normWeights() renormalizes to 1.0 automatically):")
for k, v in subject_weights.items():
    print(f"  {k:24s} {v}")
print(f"  SUM = {round(sum(subject_weights.values()),4)}  (normWeights() will rescale this to exactly 1.0)")

# ---------- difficulty_weights ----------
diff_counts = Counter(r["difficulty_guess"] for r in rows)
diff_total = sum(diff_counts.values())
difficulty_weights = {k: round(v/diff_total, 4) for k, v in diff_counts.items()}
print("\ndifficulty_weights:", difficulty_weights)

# ---------- question_type_weights (nested per subject) ----------
# 69th excluded from ALL subjects here (not just History) -- it was confirmed as
# an outlier CYCLE for question-type mix overall (23.3% statement_based vs a 4.0%
# baseline in every other cycle), so the type-mix baseline is computed uniformly
# from the other 5 cycles. subject_weights/difficulty_weights/sub_topic_weights
# are NOT affected -- the user's exclusion instruction was specifically scoped to
# "statement_based ke global average", i.e. question_type only.
question_type_weights = {}
for subj in SUBJECTS:
    if subj == "Reasoning & Aptitude":
        question_type_weights[subj] = {"reasoning_aptitude": 1.0}
        continue
    base_rows = [r for r in rows if r["subject"] == subj and r["year"] != "69th"]
    if not base_rows:
        continue
    tcount = Counter(r["question_type"] for r in base_rows)
    total = len(base_rows)
    tw = {t: round(tcount[t]/total, 4) for t in QTYPES if tcount.get(t, 0) > 0}
    question_type_weights[subj] = tw

print("\nquestion_type_weights (per subject):")
print(json.dumps(question_type_weights, indent=2))

# ---------- sub_topic_weights (nested per subject, pooled) ----------
sub_topic_weights = {}
for subj in SUBJECTS:
    srows = [r for r in rows if r["subject"] == subj]
    if not srows:
        continue
    sc = Counter(r["sub_topic"] for r in srows if r["sub_topic"])
    total = sum(sc.values())
    if total == 0:
        continue
    sub_topic_weights[subj] = {k: round(v/total, 4) for k, v in sc.items()}

print("\nsub_topic_weights (per subject, pooled):")
print(json.dumps(sub_topic_weights, indent=2))

# ---------- write the final config JSON to a file for the SQL insert ----------
config = {
    "name": "BPSC Full Length — PYQ-derived (67th-re–71st, SME-pending excl.)",
    "subject_weights": subject_weights,
    "difficulty_weights": difficulty_weights,
    "question_type_weights": question_type_weights,
    "sub_topic_weights": sub_topic_weights,
}
out_path = os.path.join(DIR, "distribution_config_payload.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2, ensure_ascii=False)
print(f"\nWrote {out_path}")

# statement_based baseline sanity check (pooled across subjects, 69th excluded,
# should read ~4.3%, matching summary_9b -- not the 69th-inflated 7.4% pooled figure)
base5 = [r for r in rows if r["year"] != "69th"]
sb_check = pct(sum(1 for r in base5 if r["question_type"]=="statement_based"), len(base5))
print(f"\nSanity check -- statement_based baseline (69th excl., SME-recheck excl.) = {round(sb_check,1)}%")
