# -*- coding: utf-8 -*-
"""
Broader pass than validate_bihar_special_batch.py's narrow 4-word check.
Scans every option in every question for a wider set of absolutist/extreme
words, and prints full context for EVERY hit so a human can triage genuine
guessability tells vs innocuous uses (e.g. "all three sectors" is fine;
"banned every factory from exporting any goods" is not).
"""
import json, re, sys

WIDE_WORDS = {"always","never","only","none","every","any","all","entirely",
              "exclusively","permanently","purely","strictly","wholly","solely",
              "completely","absolutely","guaranteed","alone","whole","ever"}

files = sys.argv[1:]
for path in files:
    data = json.load(open(path, encoding='utf-8'))
    qs = data['questions']
    hits = []
    for q in qs:
        for i, o in enumerate(q['options']):
            words = set(re.findall(r"[a-z']+", o['body'].lower()))
            matched = words & WIDE_WORDS
            if matched:
                hits.append((q['batch_ref'], "abcd"[i], o['isCorrect'], sorted(matched), o['body']))
    print(f"\n=== {path}: {len(qs)} questions, {len(hits)} wide-word hits ===")
    for ref, pos, correct, words, body in hits:
        tag = "CORRECT" if correct else "  wrong"
        print(f"  {ref} ({pos}) [{tag}] {words}: {body}")
