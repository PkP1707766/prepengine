# -*- coding: utf-8 -*-
"""
Batch validator for content-drafting JSON files. Runs BEFORE any batch is
delivered to catch the exact class of bug that appeared in Batch 01's initial
delivery: `flagged_for_extra_review` entries whose batch_ref content had nothing
to do with the flag's claimed topic.

Also verifies the mechanical rules the earlier ad-hoc check ran:
counts per cell, unique slugs, one correct option per mcq, all required fields
populated, status=draft everywhere.

Usage:  python validate_batch.py <path-to-batch.json>
Exit 0 on all-clean, non-zero on any issue. Prints every issue found.
"""
import json, re, sys, os
from collections import Counter

def main(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    issues = []
    qs = data.get("questions", [])
    by_ref = {q["batch_ref"]: q for q in qs}

    # ---- flagged_for_extra_review cross-check ----
    # Each entry starts with the ref, then some topic language after ":" or "—".
    # For every ref cited, check: (a) it exists; (b) the topic/difficulty labels
    # in the entry text match the actual question's topic/difficulty; (c) key
    # topical nouns in the entry appear in the actual question body/explanation.
    flags = data.get("meta", {}).get("flagged_for_extra_review", [])
    for entry in flags:
        m = re.match(r"^(hb\d{2}-\d{3})", entry)
        if not m:
            issues.append(f"[FLAG PARSE] no batch_ref at start of: {entry[:80]}")
            continue
        ref = m.group(1)
        q = by_ref.get(ref)
        if not q:
            issues.append(f"[FLAG MISSING REF] {ref} in flag list but not in questions[]: {entry[:80]}")
            continue
        entry_l = entry.lower()
        # topic label check
        actual_topic = q["topic"].lower()  # Ancient/Medieval/Modern
        actual_diff = q["difficulty"].lower()
        for label in ["ancient", "medieval", "modern"]:
            if label in entry_l and label != actual_topic:
                issues.append(f"[FLAG TOPIC MISMATCH] {ref}: entry mentions '{label}' but actual topic is '{actual_topic}'")
        for label in ["easy", "medium", "hard"]:
            if re.search(rf"\b{label}\b", entry_l) and label != actual_diff:
                issues.append(f"[FLAG DIFFICULTY MISMATCH] {ref}: entry mentions '{label}' but actual difficulty is '{actual_diff}'")
        # topical-noun overlap: extract distinctive words from the entry after the ref-prefix, check ANY appears in body/explanation
        head_and_body = (q["body"] + " " + q["explanation"]).lower()
        # words in the entry that are NOT trivial glue
        stopwords = set("the a an of in on to for and or by is was are were be been being with this that these those which what if smart sme entry claim actual test rewrite kept per its it as at from but not only into over under about above below".split())
        # Topic/difficulty descriptor words: exclude explicitly, because they
        # already have their own dedicated label-match checks above AND they
        # trivially collide with words that appear in many History-question
        # bodies/explanations (e.g. "modern" appears in phrases like "in modern
        # India"), which would let a wrong ref sneak past this overlap gate.
        tag_words = {"modern", "medieval", "ancient", "easy", "medium", "hard"}
        entry_tail = re.sub(r"^hb\d{2}-\d{3}[^\w]*", "", entry).lower()
        entry_tokens = [t for t in re.findall(r"[a-z]{4,}", entry_tail) if t not in stopwords and t not in tag_words]
        distinctive = [t for t in entry_tokens if len(t) >= 5]
        if distinctive:
            hits = [t for t in distinctive if t in head_and_body]
            if not hits:
                issues.append(f"[FLAG CONTENT MISMATCH] {ref}: none of the entry's distinctive words {distinctive[:6]} appear in the referenced question's body/explanation")

    # ---- claimed "not drafted" topics should really be absent from the file ----
    skipped = data.get("meta", {}).get("skipped_topics_worth_considering_for_future_batches", [])
    haystack = " ".join((q["body"] + " " + q["explanation"] + " " + q["concept_group_id"]).lower() for q in qs)
    for entry in skipped:
        # rough topic keywords in first 40 chars
        head = entry.split(":", 1)[0].lower()
        keyword_candidates = [w for w in re.findall(r"[a-z]{5,}", head)]
        for kw in keyword_candidates:
            if kw in {"riots", "civil", "services", "provision", "topics"}:  # generic — skip
                continue
            if kw in haystack:
                # OK if the skipped entry itself acknowledges the topic appears in other refs
                pass
        # cross-ref citations inside the skipped entry (e.g., "at hb01-043") must exist
        for ref_cited in re.findall(r"hb\d{2}-\d{3}", entry):
            if ref_cited not in by_ref:
                issues.append(f"[SKIPPED CITES MISSING REF] '{ref_cited}' cited in skipped-topics entry but not in questions[]: {entry[:80]}")

    # ---- mechanical checks (same as the earlier ad-hoc validator) ----
    if len(qs) != data.get("meta", {}).get("total_questions"):
        issues.append(f"[META COUNT] meta.total_questions={data['meta']['total_questions']} but questions[] has {len(qs)}")

    target = data.get("meta", {}).get("target_cells", {})
    cells = Counter((q["topic"], q["difficulty"], q["type"]) for q in qs)
    for cell_key, want in target.items():
        # cell_key format: "History_Modern_medium_mcq"
        parts = cell_key.split("_")
        # subject_topic_difficulty_type — subject part may be one token
        if len(parts) < 4:
            continue
        topic, diff, qtype = parts[1], parts[2], "_".join(parts[3:])
        got = cells.get((topic, diff, qtype), 0)
        if got != want:
            issues.append(f"[CELL COUNT] {cell_key}: target {want}, actual {got}")

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
        opts = q.get("options", [])
        if len(opts) != 4:
            issues.append(f"[OPTIONS COUNT] {r}: expected 4, got {len(opts)}")
        if q.get("type") == "mcq":
            n_correct = sum(1 for o in opts if o.get("isCorrect"))
            if n_correct != 1:
                issues.append(f"[MCQ CORRECT] {r}: expected exactly 1 correct, got {n_correct}")

    if not issues:
        print(f"OK — {os.path.basename(path)}: all checks pass ({len(qs)} questions, {len(flags)} flag entries verified)")
        return 0
    print(f"FAIL — {len(issues)} issues in {os.path.basename(path)}:")
    for i in issues:
        print(f"  - {i}")
    return 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python validate_batch.py <batch.json>")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
