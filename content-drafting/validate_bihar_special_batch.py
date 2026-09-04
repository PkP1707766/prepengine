# -*- coding: utf-8 -*-
"""
Validator for Bihar Special content-drafting JSON files (bs<paper>- refs,
multi-word topics like "History & Culture"). Adapted from validate_batch.py:
same mechanical/flag checks, plus cell-key parsing that handles topics with
spaces and "&", plus an option-craft self-audit (length bias, absolutist
wording, answer-position spread) the History batches didn't need.

Usage: python validate_bihar_special_batch.py <path-to-batch.json>
Exit 0 on all-clean, non-zero on any issue.
"""
import json, re, sys, os
from collections import Counter

DIFFS = ["easy", "medium", "hard"]
TYPES = ["match_the_following", "statement_based", "mcq"]  # longest-suffix-first

def parse_cell_key(key):
    # "Bihar_<Topic...>_<difficulty>_<type>" -> (topic, difficulty, type)
    assert key.startswith("Bihar_")
    rest = key[len("Bihar_"):]
    for t in TYPES:
        suffix = "_" + t
        if rest.endswith(suffix):
            rest2 = rest[: -len(suffix)]
            for d in DIFFS:
                dsuffix = "_" + d
                if rest2.endswith(dsuffix):
                    topic = rest2[: -len(dsuffix)]
                    return topic, d, t
    raise ValueError(f"could not parse cell key: {key}")

TAG_WORDS = {"modern", "medieval", "ancient", "easy", "medium", "hard"}
ABSOLUTIST = {"always", "never", "only", "none"}

def main(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    issues = []
    qs = data.get("questions", [])
    by_ref = {q["batch_ref"]: q for q in qs}

    # ---- flagged_for_extra_review cross-check ----
    flags = data.get("meta", {}).get("flagged_for_extra_review", [])
    for entry in flags:
        m = re.match(r"^(bs\d-\d{3})", entry)
        if not m:
            issues.append(f"[FLAG PARSE] no batch_ref at start of: {entry[:80]}")
            continue
        ref = m.group(1)
        q = by_ref.get(ref)
        if not q:
            issues.append(f"[FLAG MISSING REF] {ref} in flag list but not in questions[]: {entry[:80]}")
            continue
        entry_l = entry.lower()
        actual_diff = q["difficulty"].lower()
        for label in ["easy", "medium", "hard"]:
            if re.search(rf"\b{label}\b", entry_l) and label != actual_diff:
                issues.append(f"[FLAG DIFFICULTY MISMATCH] {ref}: entry mentions '{label}' but actual difficulty is '{actual_diff}'")
        head_and_body = (q["body"] + " " + q["explanation"]).lower()
        stopwords = set("the a an of in on to for and or by is was are were be been being with this that these those which what if smart sme entry claim actual test rewrite kept per its it as at from but not only into over under about above below given most from".split())
        entry_tail = re.sub(r"^bs\d-\d{3}[^\w]*", "", entry).lower()
        entry_tokens = [t for t in re.findall(r"[a-z]{4,}", entry_tail) if t not in stopwords and t not in TAG_WORDS]
        distinctive = [t for t in entry_tokens if len(t) >= 5]
        if distinctive:
            hits = [t for t in distinctive if t in head_and_body]
            if not hits:
                issues.append(f"[FLAG CONTENT MISMATCH] {ref}: none of the entry's distinctive words {distinctive[:6]} appear in the referenced question's body/explanation")

    skipped = data.get("meta", {}).get("skipped_topics_worth_considering_for_future_batches", [])
    for entry in skipped:
        for ref_cited in re.findall(r"bs\d-\d{3}", entry):
            if ref_cited not in by_ref:
                issues.append(f"[SKIPPED CITES MISSING REF] '{ref_cited}' cited in skipped-topics entry but not in questions[]: {entry[:80]}")

    # ---- mechanical checks ----
    if len(qs) != data.get("meta", {}).get("total_questions"):
        issues.append(f"[META COUNT] meta.total_questions={data['meta']['total_questions']} but questions[] has {len(qs)}")

    target = data.get("meta", {}).get("target_cells", {})
    cells = Counter((q["topic"], q["difficulty"], q["type"]) for q in qs)
    for cell_key, want in target.items():
        topic, diff, qtype = parse_cell_key(cell_key)
        got = cells.get((topic, diff, qtype), 0)
        if got != want:
            issues.append(f"[CELL COUNT] {cell_key}: target {want}, actual {got}")
    # also flag any drafted cell NOT present in target_cells at all
    target_keys_parsed = {parse_cell_key(k) for k in target}
    for (topic, diff, qtype), n in cells.items():
        if (topic, diff, qtype) not in target_keys_parsed:
            issues.append(f"[UNPLANNED CELL] ({topic}, {diff}, {qtype}) has {n} rows but is not in target_cells")

    slugs = Counter(q["concept_group_id"] for q in qs)
    for s, n in slugs.items():
        if n > 1:
            issues.append(f"[DUPLICATE SLUG] '{s}' used {n} times")
    refs = Counter(q["batch_ref"] for q in qs)
    for r, n in refs.items():
        if n > 1:
            issues.append(f"[DUPLICATE BATCH_REF] '{r}' used {n} times")

    for q in qs:
        r = q["batch_ref"]
        if q.get("status") != "draft":
            issues.append(f"[STATUS] {r}: status is not 'draft'")
        if not q.get("explanation"):
            issues.append(f"[EMPTY EXPLANATION] {r}")
        if not q.get("source_citation"):
            issues.append(f"[EMPTY SOURCE] {r}")
        if q.get("marks_correct") != 1 or q.get("marks_wrong") != 0.33:
            issues.append(f"[MARKS SCALE] {r}: expected 1/0.33, got {q.get('marks_correct')}/{q.get('marks_wrong')}")
        opts = q.get("options", [])
        if len(opts) != 4:
            issues.append(f"[OPTIONS COUNT] {r}: expected 4, got {len(opts)}")
        n_correct = sum(1 for o in opts if o.get("isCorrect"))
        if n_correct != 1:
            issues.append(f"[CORRECT COUNT] {r}: expected exactly 1 correct (all Bihar-Special types here are single-correct), got {n_correct}")
        if q["type"] in ("statement_based", "match_the_following") and "question_data" not in q:
            issues.append(f"[MISSING question_data] {r}: type={q['type']} requires question_data.statements/closing or list_1/list_2")

    # ---- option-craft self-audit (length bias, absolutist wording, position spread) ----
    n = len(qs)
    longest_correct = 0
    shortest_correct = 0
    position_counts = Counter()
    absolutist_hits = []
    for q in qs:
        opts = q["options"]
        lens = [(len(o["body"]), i) for i, o in enumerate(opts)]
        correct_idx = next(i for i, o in enumerate(opts) if o["isCorrect"])
        position_counts[correct_idx] += 1
        sorted_by_len = sorted(lens, reverse=True)
        if sorted_by_len[0][1] == correct_idx and sorted_by_len[0][0] > sorted_by_len[1][0]:
            longest_correct += 1
        sorted_by_len_asc = sorted(lens)
        if sorted_by_len_asc[0][1] == correct_idx and sorted_by_len_asc[0][0] < sorted_by_len_asc[1][0]:
            shortest_correct += 1
        for i, o in enumerate(opts):
            words = set(re.findall(r"[a-z']+", o["body"].lower()))
            hit = words & ABSOLUTIST
            if hit:
                absolutist_hits.append((q["batch_ref"], "abcd"[i], o["isCorrect"], sorted(hit)))

    print(f"\n=== OPTION-CRAFT SELF-AUDIT ({n} questions) ===")
    print(f"Correct answer is the STRICTLY longest option: {longest_correct}/{n} ({longest_correct/n*100:.1f}%)")
    print(f"Correct answer is the STRICTLY shortest option: {shortest_correct}/{n} ({shortest_correct/n*100:.1f}%)")
    print(f"Answer-position distribution (0=a,1=b,2=c,3=d): {dict(sorted(position_counts.items()))}")
    print(f"Absolutist-wording occurrences (always/never/only/none) in ANY option: {len(absolutist_hits)}")
    for ref, pos, is_correct, words in absolutist_hits:
        print(f"  - {ref} option {pos} (correct={is_correct}): {words}")

    if not issues:
        print(f"\nOK — {os.path.basename(path)}: all mechanical/flag checks pass ({len(qs)} questions, {len(flags)} flag entries verified)")
        return 0
    print(f"\nFAIL — {len(issues)} issues in {os.path.basename(path)}:")
    for i in issues:
        print(f"  - {i}")
    return 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python validate_bihar_special_batch.py <batch.json>")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
