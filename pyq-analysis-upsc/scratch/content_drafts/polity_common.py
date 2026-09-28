# -*- coding: utf-8 -*-
"""Shared row builders for the UPSC GS1 drafting batches (Polity batch 3 onward;
Environment from its batch 1).

Every row: exam_category 'upsc', marks 2 / 0.66, status 'draft', source_type
'original_pattern_matched', a primary-source citation. Ladder rows (count, T2,
pairs, Statement-I/II) carry fixed_option_order so the exam screen never shuffles
an ordered answer ladder. A batch for another subject sets
`polity_common.SUBJECT` before adding rows (Polity batches leave the default).
"""
import json, os

SUBJECT = "Polity"

def q(s):
    return "'" + s.replace("'", "''") + "'"

def opts(bodies, i):
    assert 0 <= i < len(bodies) == 4
    return json.dumps([{"id": "abcd"[k], "body": b, "isCorrect": k == i} for k, b in enumerate(bodies)])

C3 = ["Only one", "Only two", "All three", "None"]
C4 = ["Only one", "Only two", "Only three", "All four"]
T2 = ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"]
P4 = ["Only one pair", "Only two pairs", "Only three pairs", "All four pairs"]
P3 = ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"]
# Verbatim UPSC Statement-I/Statement-II option text (playbook D.6).
SI = ["Both Statement-I and Statement-II are correct and Statement-II is the correct explanation for Statement-I",
      "Both Statement-I and Statement-II are correct and Statement-II is not the correct explanation for Statement-I",
      "Statement-I is correct but Statement-II is incorrect",
      "Statement-I is incorrect but Statement-II is correct"]
# Verbatim UPSC 2025 three-statement key: Statements II and III as explanations of I.
SI3 = ["Both Statement II and Statement III are correct and both of them explain Statement I",
       "Both Statement II and Statement III are correct but only one of them explains Statement I",
       "Only one of the Statements II and III is correct and that explains Statement I",
       "Neither Statement II nor Statement III is correct"]
HOW_MANY = "How many of the above statements are correct?"
WHICH = "Which of the statements given above is/are correct?"
PAIRS = "How many of the pairs given above are correctly matched?"
SI_CLOSING = "Which one of the following is correct in respect of the above statements?"
LAX = "M. Laxmikanth, Indian Polity"

LADDER_NAME = {id(C3): "C3", id(C4): "C4", id(T2): "T2", id(P4): "P4", id(P3): "P3", id(SI): "SI", id(SI3): "SI3"}

rows, tally, cells, records = [], {}, {}, []
letters = {"a": 0, "b": 0, "c": 0, "d": 0}  # correct-option letter, across every row type

def pg_jsonb_text(v):
    """Render a value exactly as Postgres prints jsonb::text (keys ordered by length, then bytes)."""
    if isinstance(v, dict):
        ks = sorted(v, key=lambda k: (len(k.encode("utf-8")), k.encode("utf-8")))
        return "{" + ", ".join(json.dumps(k, ensure_ascii=False) + ": " + pg_jsonb_text(v[k]) for k in ks) + "}"
    if isinstance(v, list):
        return "[" + ", ".join(pg_jsonb_text(x) for x in v) + "]"
    return json.dumps(v, ensure_ascii=False)

def _row(topic, typ, diff, body, qdata, bodies, ans, expl, cg, cite, ladder=None):
    letters["abcd"[ans]] += 1
    rows.append("('upsc'," + q(SUBJECT) + "," + q(topic) + "," + q(typ) + "," + q(diff) + "," + q(body) + "," + q(json.dumps(qdata, ensure_ascii=False)) + "::jsonb,"
                + q(opts(bodies, ans)) + "::jsonb,2,0.66," + q(expl) + "," + q(cg) + ",'original_pattern_matched'," + q(cite) + ",'draft')")
    records.append({"cg": cg, "topic": topic, "type": typ, "difficulty": diff, "body": body, "question_data": qdata,
                    "options": json.loads(opts(bodies, ans)), "explanation": expl, "citation": cite})
    key = f"{typ}:{LADDER_NAME[id(ladder)]}:{bodies[ans]}" if ladder is not None else f"{typ}:letter-{'abcd'[ans]}"
    tally[key] = tally.get(key, 0) + 1
    ck = (diff, typ, topic)
    cells[ck] = cells.get(ck, 0) + 1

def _stmt_data(statements, closing, roman):
    qd = {"statements": statements, "closing": closing, "fixed_option_order": True}
    if roman:
        qd["numbering"] = "roman"  # UPSC 2025 style: statements I, II, III
    return qd

def stmt(topic, diff, body, statements, ladder, ans, expl, cg, cite, roman=False):
    assert ladder in (C3, C4, T2) and len(statements) == {id(C3): 3, id(C4): 4, id(T2): 2}[id(ladder)]
    assert not (roman and ladder is T2), "T2 options name statements 1 and 2; write a stmt_opts row for Roman"
    closing = WHICH if ladder is T2 else HOW_MANY
    _row(topic, "statement_based", diff, body, _stmt_data(statements, closing, roman),
         ladder, ans, expl, cg, cite, ladder)

def stmt_opts(topic, diff, body, statements, options, ans, expl, cg, cite, roman=False):
    """A statement question with its own combination options ("1 and 2 only", or the 2026-style
    "1 only / 1 and 2 / 2 and 3 / 3 only"). Kept in the printed order, as on the paper. With
    roman=True the options must name the statements I, II, III."""
    assert len(options) == 4 and len(statements) in (2, 3, 4)
    names_roman = any(" I" in f" {o}" or o.startswith("I") for o in options)
    assert roman == names_roman or not any(ch.isdigit() for o in options for ch in o), "numbering and option labels disagree"
    _row(topic, "statement_based", diff, body, _stmt_data(statements, WHICH, roman),
         options, ans, expl, cg, cite)

def mcq(topic, diff, body, options, ans, expl, cg, cite):
    _row(topic, "mcq", diff, body, {}, options, ans, expl, cg, cite)

def ar(topic, diff, s1, s2, ans, expl, cg, cite):
    _row(topic, "assertion_reason", diff, "Consider the following statements:",
         {"assertion": s1, "reason": s2, "ar_labels": "statement", "closing": SI_CLOSING, "fixed_option_order": True},
         SI, ans, expl, cg, cite, SI)

def ar3(topic, diff, s1, s2, s3, ans, expl, cg, cite):
    """UPSC 2025's three-statement form; renders as Statement-I/II/III (question_data.reason_2)."""
    _row(topic, "assertion_reason", diff, "Consider the following statements:",
         {"assertion": s1, "reason": s2, "reason_2": s3, "ar_labels": "statement", "closing": SI_CLOSING, "fixed_option_order": True},
         SI3, ans, expl, cg, cite, SI3)

def pairs(topic, diff, body, list_1, list_2, ans, expl, cg, cite):
    ladder = P4 if len(list_1) == 4 else P3
    assert len(list_1) == len(list_2) and len(list_1) in (3, 4)
    _row(topic, "match_the_following", diff, body,
         {"list_1": [f"{i + 1}. {x}" for i, x in enumerate(list_1)], "list_2": list_2, "closing": PAIRS, "fixed_option_order": True},
         ladder, ans, expl, cg, cite, ladder)

def write_sql(here, name):
    sql = ("insert into public.questions\n(exam_category, subject, topic, type, difficulty, body, question_data, options, marks_correct, marks_wrong, explanation, concept_group_id, source_type, source_citation, status)\nvalues\n"
           + ",\n".join(rows) + "\nreturning topic, type, difficulty, concept_group_id;\n")
    out = os.path.join(here, name)
    open(out, "w", encoding="utf-8").write(sql)
    print(f"wrote {name}: {len(rows)} rows, {len(sql)} chars")
    print("cells:", {f"{d}/{t}/{s}": n for (d, t, s), n in sorted(cells.items())})
    print("answer tally:", dict(sorted(tally.items())))
    print("correct letter:", letters)
    # Checksum manifest: md5 of each row as the DB will print it, for a read-back comparison.
    import hashlib
    man = {r["cg"]: hashlib.md5("|".join([r["body"], pg_jsonb_text(r["question_data"]), pg_jsonb_text(r["options"]), r["explanation"],
                                          r["citation"], r["topic"], r["type"], r["difficulty"]]).encode("utf-8")).hexdigest() for r in records}
    assert len(man) == len(records), "duplicate concept_group_id inside the batch"
    json.dump(man, open(out.replace(".sql", "_md5.json"), "w"), indent=0, sort_keys=True)
    json.dump(records, open(out.replace(".sql", "_records.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("checksum manifest:", out.replace(".sql", "_md5.json"))
