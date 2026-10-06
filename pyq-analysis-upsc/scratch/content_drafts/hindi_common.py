# -*- coding: utf-8 -*-
"""Hindi for rows the audit kept unchanged. One H() call per row; write() turns a batch
into guarded UPDATEs (bilingual.hindi_update), checked against the English export
(_kept_en_rows.json) so that every statement, list item, Statement-I/II line and
non-ladder option of a row gets its Hindi and nothing extra.

Style: docs/upsc-hindi-style.md -- UPSC Hindi-paper wording for the frame, plain
NCERT-style Hindi for the content, English in brackets for a technical term on first
use, Western numerals."""
import json, os
from bilingual import hindi_update, CONSIDER_HI

HERE = os.path.dirname(os.path.abspath(__file__))
EN = {r["id"]: r for r in json.load(open(os.path.join(HERE, "_kept_en_rows.json"), encoding="utf-8"))}
OUT, SEEN = [], set()
# MCQs whose options were rewritten with Hindi in env_polity_audit_fixes.py (length cues).
OPTS_DONE = {"3455fdee-f876-4d56-a20e-86a8d7341c7b", "a4daa638-19d0-40c9-a038-371e37cdfec6", "5029fc61-903b-469b-af34-9746d4dfeabf",
             "01c1b03b-f1d5-4d02-b5f8-068eedcb8b50", "29c1f42a-a126-4516-961d-a2b6b9dce538", "7cfc9d0e-4a34-4673-ae45-8a687db8126e",
             "4649a5a5-3d76-48be-bfda-0e6441461d3b", "946bb8a0-1499-4592-a13d-8f1b07de751a", "46f7e342-7b01-418d-92f8-0bb15a962f71",
             "ec96412e-d646-4c45-810b-8ade62d1f0e6", "f70e6048-ed4d-470f-ba52-839437106c17", "ee38ee90-2f3a-41f8-97c1-601e572d781e",
             "4415dc51-5698-44cd-8e86-652d80d3395e"}

def H(fid, body_hi, expl_hi, st=None, l1=None, l2=None, a=None, r=None, r2=None, o=None, closing=None):
    en = EN[fid]
    qd = en["qd"] or {}
    assert fid not in SEEN, f"{fid} twice"
    SEEN.add(fid)
    hi = {}
    if "statements" in qd:
        assert st and len(st) == len(qd["statements"]), f"{fid}: statements {len(qd['statements'])} vs Hindi {len(st or [])}"
        hi["statements_hi"] = st
    if "list_1" in qd:
        assert l1 and l2 and len(l1) == len(qd["list_1"]) and len(l2) == len(qd["list_2"]), f"{fid}: list lengths"
        # list_1 items carry their '1. ' numbering in English; keep it identical in Hindi.
        hi["list_1_hi"] = [f"{i + 1}. {x}" for i, x in enumerate(l1)]
        hi["list_2_hi"] = l2
    for k, v in (("assertion", a), ("reason", r), ("reason_2", r2)):
        if k in qd:
            assert v, f"{fid}: {k} needs Hindi"
            hi[k + "_hi"] = v
    if closing is not None:
        hi["closing_hi"] = closing
    if fid in OPTS_DONE:
        assert o is None, f"{fid}: options already carry Hindi"
    elif en["opts"]:
        assert o and set(o) == set(en["opts"]), f"{fid}: options {sorted(en['opts'])} vs Hindi {sorted(o or {})}"
    else:
        assert o is None, f"{fid}: ladder options already have Hindi"
    OUT.append(hindi_update(fid, body_hi, expl_hi, qd_hi=hi, options_hi=o,
                            n_statements=len(st) if st else None, n_pairs=len(l1) if l1 else None))

def write(name, subject=None):
    left = [i for i, r in EN.items() if (subject is None or r["subject"] == subject) and i not in SEEN]
    open(os.path.join(HERE, name), "w", encoding="utf-8", newline="\n").write("\n".join(OUT) + "\n")
    print(f"{name}: {len(OUT)} rows; still without Hindi in this subject: {len(left)}")
