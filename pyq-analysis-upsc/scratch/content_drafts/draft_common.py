# -*- coding: utf-8 -*-
"""Builders for NEW bilingual UPSC rows (the insert counterpart of rewrite_common.py).

Same API as rewrite_common: S (statement ladder), M (MCQ), P (how many pairs),
A (Statement-I/II, or I/II/III with s3), C (chronology). Every builder refuses a row
that lacks Hindi for any visible part, an MCQ whose correct option is the longest, and
a duplicate concept_group_id inside the batch. write(name) saves one INSERT to run with
  supabase db query --linked --project-ref <ref> -f <file>
and prints the cell tally (difficulty/type/sub-topic) and the answer spread per format,
so the batch can be checked against its gap report before it goes in.

Rows go in as status 'draft' with marks 2 / 0.66 (GS Paper I)."""
import json, os
from bilingual import options_json, CLOSING_HI, sql_q
from polity_common import C3, C4, T2, P4, P3, HOW_MANY, WHICH, PAIRS, SI, SI3, SI_CLOSING

SUBJECT = None           # set by the batch, e.g. "Environment & Ecology"
ROWS, CELLS, SPREAD, CGS = [], {}, {}, set()
CODE = "Select the correct answer using the code given below:"
ORDER = "Select the correct order using the code given below:"
CONSIDER = "Consider the following statements:"
CONSIDER_HI = "निम्नलिखित कथनों पर विचार कीजिए:"

def _add(topic, typ, diff, body, body_hi, qd, options, expl, expl_hi, cite, cg, spread_key):
    assert SUBJECT, "set draft_common.SUBJECT first"
    assert cg not in CGS, f"duplicate concept group {cg}"
    CGS.add(cg)
    for k in ("statements", "list_1", "list_2"):
        if k in qd:
            assert len(qd[k]) == len(qd[k + "_hi"]), f"{cg}: {k} vs {k}_hi"
    for k in ("assertion", "reason", "reason_2", "closing"):
        if k in qd:
            assert qd.get(k + "_hi"), f"{cg}: {k} has no Hindi"
    assert all(o.get("body_hi") for o in options) and body_hi and expl_hi and cite, f"{cg}: missing Hindi, explanation or citation"
    ROWS.append({"topic": topic, "type": typ, "difficulty": diff, "body": body, "body_hi": body_hi, "question_data": qd,
                 "options": options, "explanation": expl, "explanation_hi": expl_hi, "source_citation": cite, "concept_group_id": cg})
    ck = f"{diff}|{typ}|{topic}"
    CELLS[ck] = CELLS.get(ck, 0) + 1
    SPREAD[spread_key] = SPREAD.get(spread_key, 0) + 1

def S(topic, diff, body, body_hi, st, st_hi, ladder, ans, expl, expl_hi, cite, cg, roman=False, opts=None, opts_hi=None, closing=None, closing_hi=None):
    """ladder C3 / C4 / T2, or None with opts for a combination ladder ('1 and 2 only' ...).
    closing: CODE for a list of items, or a custom 'How many of the above ...' line (give closing_hi)."""
    if closing is None:
        closing = HOW_MANY if ladder in (C3, C4) else WHICH
        closing_hi = CLOSING_HI[closing]
    elif closing in CLOSING_HI:
        closing_hi = CLOSING_HI[closing]
    else:
        assert closing.startswith("How many") and closing_hi, "a custom closing is a count and needs closing_hi"
    qd = {"statements": st, "statements_hi": st_hi, "closing": closing, "closing_hi": closing_hi, "fixed_option_order": True}
    if roman:
        qd["numbering"] = "roman"
    bodies = ladder if ladder is not None else opts
    fmt = f"{len(st)}-stmt " + ("count" if ladder in (C3, C4) else ("T2" if ladder is T2 else "combo"))
    _add(topic, "statement_based", diff, body, body_hi, qd, options_json(bodies, ans, opts_hi), expl, expl_hi, cite, cg, f"{fmt}: {bodies[ans]}")

MCQ_SLOTS = [2, 0, 3, 1]   # where the key goes, in turn, so a batch's answer letters stay balanced
_mcq_n = [0]

def M(topic, diff, body, body_hi, opts, opts_hi, ans, expl, expl_hi, cite, cg, pos=None):
    """Write the key at opts[ans]; it is moved to the next slot of MCQ_SLOTS (or to pos) with the
    distractors kept in their order. Pass pos for sets whose order means something."""
    lens = [len(x) for x in opts]
    assert lens[ans] <= max(l for i, l in enumerate(lens) if i != ans), f"{cg}: the correct option is the longest"
    if pos is None:
        pos = MCQ_SLOTS[_mcq_n[0] % 4]
        _mcq_n[0] += 1
    order = [i for i in range(4) if i != ans]
    order.insert(pos, ans)
    opts, opts_hi = [opts[i] for i in order], [opts_hi[i] for i in order]
    _add(topic, "mcq", diff, body, body_hi, {}, options_json(opts, pos, opts_hi), expl, expl_hi, cite, cg, f"mcq: {'abcd'[pos]}")

def P(topic, diff, body, body_hi, pairs_en, pairs_hi, ans, expl, expl_hi, cite, cg):
    ladder = P4 if len(pairs_en) == 4 else P3
    sp = lambda xs: [tuple(y.strip() for y in x.split(" : ")) for x in xs]
    en, hi = sp(pairs_en), sp(pairs_hi)
    assert len(en) == len(hi) and all(len(t) == 2 for t in en + hi), f"{cg}: every pair needs one ' : '"
    qd = {"list_1": [f"{i + 1}. {a}" for i, (a, _) in enumerate(en)], "list_1_hi": [f"{i + 1}. {a}" for i, (a, _) in enumerate(hi)],
          "list_2": [b for _, b in en], "list_2_hi": [b for _, b in hi], "closing": PAIRS, "closing_hi": CLOSING_HI[PAIRS], "fixed_option_order": True}
    _add(topic, "match_the_following", diff, body, body_hi, qd, options_json(ladder, ans), expl, expl_hi, cite, cg, f"pairs-{len(en)}: {ladder[ans]}")

def A(topic, diff, s1, s1_hi, s2, s2_hi, ans, expl, expl_hi, cite, cg, s3=None, s3_hi=None):
    qd = {"assertion": s1, "assertion_hi": s1_hi, "reason": s2, "reason_hi": s2_hi, "ar_labels": "statement",
          "closing": SI_CLOSING, "closing_hi": CLOSING_HI[SI_CLOSING], "fixed_option_order": True}
    ladder = SI
    if s3 is not None:
        qd["reason_2"], qd["reason_2_hi"], ladder = s3, s3_hi, SI3
    _add(topic, "assertion_reason", diff, CONSIDER, CONSIDER_HI, qd, options_json(ladder, ans), expl, expl_hi, cite, cg,
         f"{'SI3' if s3 else 'SI'}: {'abcd'[ans]}")

def C(topic, diff, body, body_hi, items, items_hi, opts, ans, expl, expl_hi, cite, cg):
    qd = {"statements": items, "statements_hi": items_hi, "closing": ORDER, "closing_hi": CLOSING_HI[ORDER]}
    _add(topic, "mcq", diff, body, body_hi, qd, options_json(opts, ans, list(opts)), expl, expl_hi, cite, cg, "chronology")

def write(name):
    here = os.path.dirname(os.path.abspath(__file__))
    vals = []
    for r in ROWS:
        vals.append("('upsc'," + ",".join(sql_q(x) for x in (SUBJECT, r["topic"], r["type"], r["difficulty"], r["body"], r["body_hi"]))
                    + "," + sql_q(json.dumps(r["question_data"], ensure_ascii=False)) + "::jsonb,"
                    + sql_q(json.dumps(r["options"], ensure_ascii=False)) + "::jsonb,2,0.66,"
                    + ",".join(sql_q(r[k]) for k in ("explanation", "explanation_hi", "concept_group_id")) + ",'original_pattern_matched',"
                    + sql_q(r["source_citation"]) + ",'draft')")
    sql = ("insert into public.questions (exam_category, subject, topic, type, difficulty, body, body_hi, question_data, options, "
           "marks_correct, marks_wrong, explanation, explanation_hi, concept_group_id, source_type, source_citation, status)\nvalues\n"
           + ",\n".join(vals) + "\nreturning concept_group_id;\n")
    open(os.path.join(here, name), "w", encoding="utf-8").write(sql)
    json.dump([r["concept_group_id"] for r in ROWS], open(os.path.join(here, name.replace(".sql", "_cgs.json")), "w"))
    print(f"{name}: {len(ROWS)} rows")
    print("cells:", json.dumps(dict(sorted(CELLS.items())), ensure_ascii=False))
    print("answer spread:", json.dumps(dict(sorted(SPREAD.items())), ensure_ascii=False))
