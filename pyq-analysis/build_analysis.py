# -*- coding: utf-8 -*-
"""
Combines the 6 tagged papers into one dataset and produces every summary table
requested in the analysis prompt (bpsc-pyq-analysis-prompt.md, "Output format" 1-8).

Papers included (in chronological order): 67th_re, 68th, 69th, 70th, 70th_re, 71st.
66th and 67th-1st are excluded (see memory: mismatched key / annulled exam).
"""
import csv, os
from collections import defaultdict, Counter

DIR = os.path.dirname(__file__)
PAPERS = ["67th_re", "68th", "69th", "70th", "70th_re", "71st"]
YEAR_LABEL = {  # display label -> matches the 'year' column already in each CSV
    "67th_re": "67th-reexam", "68th": "68th", "69th": "69th",
    "70th": "70th", "70th_re": "70th-reexam", "71st": "71st",
}
YEAR_ORDER = ["67th-reexam", "68th", "69th", "70th", "70th-reexam", "71st"]

SUBJECTS = ["History","Geography","Polity","Economy","Science & Technology",
            "Environment & Ecology","Current Affairs","Bihar-Specific","Reasoning & Aptitude"]
QTYPES = ["simple_mcq","statement_based","match_the_following","assertion_reason","reasoning_aptitude"]

# Linear recency weights, oldest->newest, matching YEAR_ORDER. Sum = 21.
RECENCY_WEIGHTS = {y: i+1 for i, y in enumerate(YEAR_ORDER)}

# 70th-family questions whose PROVISIONAL key contradicts well-established fact
# (identified during tagging; final keys not yet published for either paper).
# User instruction: flag for SME recheck, exclude from any downstream "item bank"
# ingestion until verified -- do NOT silently trust these correct_option values.
SME_RECHECK = [
    ("70th",       104, "Answer key says (A) Bus Driver; she is widely reported as Bihar's first transgender Sub-Inspector (Police), not Bus Driver."),
    ("70th",       117, "RBI headline inflation forecast figure in key does not match publicly reported RBI projections for the period."),
    ("70th",       129, "Key's 'major cause of air pollution' answer (disposal of plastics) is inconsistent with standard science; vehicular/industrial emissions are the conventionally cited major cause."),
    ("70th",       135, "Key names a Union Textiles Minister that does not match the publicly reported holder of that post after the 18th Lok Sabha."),
    ("70th",       139, "Key says 108th Amendment abolished Anglo-Indian reserved seats; this was actually the 104th Constitutional Amendment Act, 2019."),
    ("70th",       141, "Key's RBI net-worth criterion for SFB-to-Universal-Bank conversion does not match RBI's publicly stated threshold."),
    ("70th",       150, "Key's constituency for Odisha CM Mohan Charan Majhi does not match his publicly reported constituency (Keonjhar)."),
    ("70th-reexam", 41, "Key says Abul Kalam Azad became INC President after Bose resigned in 1939; Rajendra Prasad is the widely reported successor."),
    ("70th-reexam", 61, "Key attributes vinegar's sour taste to citric acid; acetic acid is the standard textbook answer."),
    ("70th-reexam", 64, "Key attributes 'Tarikh-i-Firuz Shahi' to Minhaj Siraj; this work is standardly attributed to Ziauddin Barani (Minhaj-us-Siraj wrote Tabaqat-i-Nasiri, a different text)."),
    ("70th-reexam", 68, "Key names Barauni as India's highest-capacity oil refinery; publicly reported capacity rankings place other refineries (e.g. Jamnagar) well above it."),
    ("70th-reexam", 78, "Key says the Son river is 'Sorrow of Bihar'; this epithet is conventionally applied to the Kosi river."),
]

def load_all():
    rows = []
    for p in PAPERS:
        with open(os.path.join(DIR, f"{p}.csv"), encoding="utf-8") as f:
            for r in csv.DictReader(f):
                rows.append(r)
    return rows

def pct(n, d):
    return round(100.0 * n / d, 1) if d else 0.0

def write_csv(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            w.writerow(r)

def main():
    rows = load_all()
    assert len(rows) == 900, f"expected 900 rows, got {len(rows)}"

    # ---------- Output 1: combined dataset (+ SME recheck flag) ----------
    recheck_map = {(y, q): reason for y, q, reason in SME_RECHECK}
    header = list(rows[0].keys()) + ["needs_sme_recheck", "sme_recheck_reason"]
    out_rows = []
    for r in rows:
        key = (r["year"], int(r["question_number"]))
        reason = recheck_map.get(key, "")
        vals = [r[h] for h in header[:-2]] + [("TRUE" if reason else "FALSE"), reason]
        out_rows.append(vals)
    write_csv(os.path.join(DIR, "combined_dataset.csv"), header, out_rows)
    n_flagged = sum(1 for v in out_rows if v[-2] == "TRUE")
    assert n_flagged == len(SME_RECHECK), f"expected {len(SME_RECHECK)} recheck rows, matched {n_flagged}"

    # ---------- standalone SME recheck handoff file ----------
    recheck_rows = []
    by_key = {(r["year"], int(r["question_number"])): r for r in rows}
    for y, q, reason in SME_RECHECK:
        r = by_key[(y, q)]
        recheck_rows.append([y, q, r["subject"], r["question_text_en"], r["correct_option"],
                              r["key_status"], reason])
    write_csv(os.path.join(DIR, "sme_recheck_70th_family.csv"),
              ["year","question_number","subject","question_text_en","key_correct_option",
               "key_status","recheck_reason"], recheck_rows)

    # ---------- Output 2: subject % by year + averaged ----------
    by_year = defaultdict(list)
    for r in rows:
        by_year[r["year"]].append(r)

    subj_table = []
    for subj in SUBJECTS:
        row = [subj]
        pcts = []
        for y in YEAR_ORDER:
            yrows = by_year[y]
            n = sum(1 for r in yrows if r["subject"] == subj)
            p = pct(n, len(yrows))
            pcts.append(p)
            row.append(f"{p}% ({n})")
        row.append(f"{round(sum(pcts)/len(pcts),1)}%")
        subj_table.append(row)
    write_csv(os.path.join(DIR, "summary_2_subject_by_year.csv"),
              ["subject"] + YEAR_ORDER + ["average"], subj_table)

    # ---------- Output 3: sub-topic % within each subject, pooled across years ----------
    # Pooled (not per-year-averaged): per-year subject x subtopic cells are frequently
    # single digits, so an unweighted average of tiny-sample percentages would be noisy.
    # Pooling sums counts across all 900 rows first, then takes %, which is the
    # count-weighted average across years -- documented explicitly per output #8.
    subtopic_table = []
    for subj in SUBJECTS:
        srows = [r for r in rows if r["subject"] == subj]
        sub_counts = Counter(r["sub_topic"] for r in srows)
        for sub, n in sub_counts.most_common():
            subtopic_table.append([subj, sub, n, f"{pct(n, len(srows))}%"])
        subtopic_table.append([subj, "— TOTAL —", len(srows), "100.0%"])
    write_csv(os.path.join(DIR, "summary_3_subtopic_within_subject.csv"),
              ["subject", "sub_topic", "count", "pct_of_subject"], subtopic_table)

    # ---------- Output 4: question_type % overall + per-subject ----------
    overall_type = Counter(r["question_type"] for r in rows)
    overall_rows = [[t, overall_type.get(t,0), f"{pct(overall_type.get(t,0), len(rows))}%"] for t in QTYPES]
    write_csv(os.path.join(DIR, "summary_4a_type_overall.csv"),
              ["question_type","count","pct"], overall_rows)

    type_by_subj = []
    for subj in SUBJECTS:
        srows = [r for r in rows if r["subject"] == subj]
        tcount = Counter(r["question_type"] for r in srows)
        row = [subj, len(srows)]
        for t in QTYPES:
            row.append(f"{pct(tcount.get(t,0), len(srows))}%")
        type_by_subj.append(row)
    write_csv(os.path.join(DIR, "summary_4b_type_by_subject.csv"),
              ["subject","n"] + QTYPES, type_by_subj)

    # ---------- Output 5: statement_based deep-dive ----------
    st_rows = [r for r in rows if r["question_type"] == "statement_based"]
    sc_dist = Counter(r["statement_count"] for r in st_rows if r["statement_count"])
    sc_table = [[k, v, f"{pct(v,len(st_rows))}%"] for k,v in sorted(sc_dist.items(), key=lambda x:-x[1])]
    write_csv(os.path.join(DIR, "summary_5a_statement_count_distribution.csv"),
              ["statement_count","n","pct_of_statement_based"], sc_table)

    pattern_dist = Counter(r["option_combination_pattern"] for r in st_rows if r["option_combination_pattern"])
    pattern_table = [[k, v, f"{pct(v,len(st_rows))}%"] for k,v in sorted(pattern_dist.items(), key=lambda x:-x[1])]
    write_csv(os.path.join(DIR, "summary_5b_option_combination_pattern.csv"),
              ["option_combination_pattern","n","pct_of_statement_based"], pattern_table)

    # All/None correctness rate -- functional vs literal, across the WHOLE dataset
    # (all_none_literal_phrasing/is_all_or_none_correct apply to any question_type,
    # not just statement_based -- match_the_following and simple_mcq can carry
    # "All of the above"/"None of the above" as a plain option too).
    total_n = len(rows)
    func_true = sum(1 for r in rows if r["is_all_or_none_correct"] == "TRUE")
    lit_true  = sum(1 for r in rows if r["all_none_literal_phrasing"] == "TRUE")
    allnone_table = [
        ["is_all_or_none_correct (functional -- incl. coded combos like '1,2 and 3' meaning ALL)",
         func_true, f"{pct(func_true, total_n)}%"],
        ["all_none_literal_phrasing (literal 'All/None of the above' text only)",
         lit_true, f"{pct(lit_true, total_n)}%"],
        ["denominator", total_n, "100.0%"],
    ]
    write_csv(os.path.join(DIR, "summary_5c_all_none_correct_rate.csv"),
              ["metric","n","pct_of_all_900"], allnone_table)

    # ---------- Output 6: match_the_following list_item_count distribution ----------
    mt_rows = [r for r in rows if r["question_type"] == "match_the_following"]
    li_dist = Counter(r["list_item_count"] for r in mt_rows if r["list_item_count"])
    li_table = [[k, v, f"{pct(v,len(mt_rows))}%"] for k,v in sorted(li_dist.items())]
    write_csv(os.path.join(DIR, "summary_6_match_list_item_count.csv"),
              ["list_item_count","n","pct_of_match_the_following"], li_table)

    # ---------- Output 7: ambiguous-subject flagged questions ----------
    amb = [r for r in rows if r["ambiguous_subject"] == "TRUE"]
    amb_table = [[r["year"], r["question_number"], r["subject"], r["sub_topic"],
                  r["ambiguous_note"], r["question_text_en"]] for r in amb]
    write_csv(os.path.join(DIR, "summary_7_ambiguous_subject_flagged.csv"),
              ["year","question_number","primary_subject","sub_topic","ambiguous_note","question_text_en"],
              amb_table)

    # ---------- Output 8: sample-size / low-confidence cells ----------
    low_conf = []
    for subj in SUBJECTS:
        srows = [r for r in rows if r["subject"] == subj]
        tcount = Counter(r["question_type"] for r in srows)
        for t in QTYPES:
            n = tcount.get(t, 0)
            if 0 < n < 10:
                low_conf.append([subj, t, n, "LOW CONFIDENCE (<10 across all 6 papers combined)"])
    for subj in SUBJECTS:
        srows = [r for r in rows if r["subject"] == subj]
        sc = Counter(r["sub_topic"] for r in srows)
        for sub, n in sc.items():
            if n < 10:
                low_conf.append([f"{subj} > {sub}", "(sub_topic)", n, "LOW CONFIDENCE (<10 across all 6 papers combined)"])
    write_csv(os.path.join(DIR, "summary_8_low_confidence_cells.csv"),
              ["cell","dimension","n","flag"], low_conf)

    # ---------- Output 9 (config recommendations, per user instruction): ----------
    # 9a. Bihar-Specific: recency-weighted average (linear weights 1..6, oldest->newest)
    #     instead of a flat average, because the flat 15.7% hides a real swing between
    #     the 5-option era (~21%) and the 4-option era (~10-15%).
    bihar_by_year = {y: sum(1 for r in by_year[y] if r["subject"]=="Bihar-Specific") for y in YEAR_ORDER}
    bihar_pct_by_year = {y: pct(bihar_by_year[y], len(by_year[y])) for y in YEAR_ORDER}
    w_sum = sum(RECENCY_WEIGHTS.values())
    bihar_weighted = sum(bihar_pct_by_year[y]*RECENCY_WEIGHTS[y] for y in YEAR_ORDER) / w_sum
    bihar_flat = sum(bihar_pct_by_year.values()) / len(YEAR_ORDER)
    bihar_table = [[y, RECENCY_WEIGHTS[y], f"{bihar_pct_by_year[y]}%", f"{bihar_by_year[y]}"] for y in YEAR_ORDER]
    bihar_table.append(["FLAT AVERAGE", "-", f"{round(bihar_flat,1)}%", "-"])
    bihar_table.append(["RECENCY-WEIGHTED AVERAGE (linear, oldest=1..newest=6)", "-", f"{round(bihar_weighted,1)}%", "-"])
    write_csv(os.path.join(DIR, "summary_9a_bihar_specific_recency_weighted.csv"),
              ["year","recency_weight","pct_of_paper","raw_count"], bihar_table)

    # 9b. statement_based baseline excluding the 69th (confirmed outlier)
    non_69th_years = [y for y in YEAR_ORDER if y != "69th"]
    st_baseline_rows = [r for r in rows if r["year"] in non_69th_years]
    st_baseline_n = sum(1 for r in st_baseline_rows if r["question_type"]=="statement_based")
    st_baseline_pct = pct(st_baseline_n, len(st_baseline_rows))
    st_69th_n = sum(1 for r in rows if r["year"]=="69th" and r["question_type"]=="statement_based")
    st_69th_pct = pct(st_69th_n, 150)
    st_all6_pct = pct(len(st_rows), 900)
    write_csv(os.path.join(DIR, "summary_9b_statement_based_baseline_excl_69th.csv"),
              ["metric","n","denominator","pct"], [
        ["baseline (5 cycles, 69th excluded)", st_baseline_n, len(st_baseline_rows), f"{st_baseline_pct}%"],
        ["69th only (outlier, excluded from baseline)", st_69th_n, 150, f"{st_69th_pct}%"],
        ["all 6 cycles pooled (for reference only -- do not use as target)", len(st_rows), 900, f"{st_all6_pct}%"],
    ])

    # 9c. reasoning_aptitude as a FIXED COUNT per paper, not a percentage weight
    ra_table = [[y, sum(1 for r in by_year[y] if r["question_type"]=="reasoning_aptitude")] for y in YEAR_ORDER]
    ra_counts = [c for _, c in ra_table]
    write_csv(os.path.join(DIR, "summary_9c_reasoning_aptitude_fixed_count.csv"),
              ["year","reasoning_aptitude_count_of_150"], ra_table +
              [["MIN", min(ra_counts)], ["MODE", Counter(ra_counts).most_common(1)[0][0]], ["MAX", max(ra_counts)]])

    # ---------- console summary for sanity ----------
    print("Combined:", len(rows), "rows across", len(PAPERS), "papers")
    print("\nSubject totals (pooled):")
    for subj in SUBJECTS:
        n = sum(1 for r in rows if r["subject"] == subj)
        print(f"  {subj:24s} {n:4d}  {pct(n,900)}%")
    print("\nQuestion type totals (pooled):")
    for t in QTYPES:
        print(f"  {t:22s} {overall_type.get(t,0):4d}  {pct(overall_type.get(t,0),900)}%")
    print(f"\nstatement_based n={len(st_rows)}  match_the_following n={len(mt_rows)}")
    print(f"ambiguous flagged: {len(amb)} / 900 ({pct(len(amb),900)}%)")
    print(f"low-confidence cells flagged: {len(low_conf)}")
    print(f"functional all/none correct: {func_true} ({pct(func_true,900)}%)  |  literal phrasing: {lit_true} ({pct(lit_true,900)}%)")
    print(f"\nBihar-Specific: flat avg={round(bihar_flat,1)}%  recency-weighted avg={round(bihar_weighted,1)}%")
    print(f"statement_based baseline (excl. 69th) = {st_baseline_pct}%  (69th alone = {st_69th_pct}%, all-6-pooled = {st_all6_pct}%)")
    print(f"reasoning_aptitude per paper: {ra_counts}  (min={min(ra_counts)} mode={Counter(ra_counts).most_common(1)[0][0]} max={max(ra_counts)})")
    print(f"SME recheck flagged: {n_flagged} rows -> sme_recheck_70th_family.csv")

if __name__ == "__main__":
    main()
