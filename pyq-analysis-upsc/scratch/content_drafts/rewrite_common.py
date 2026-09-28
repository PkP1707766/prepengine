# -*- coding: utf-8 -*-
"""Builders for in-place rewrites of audited UPSC rows (English and Hindi together).

S = statement question on a fixed ladder, M = single-answer MCQ (options shuffle on the
exam screen), P = "how many pairs are correctly matched", C = chronology / sequence MCQ
whose items are listed as numbered statements. Every builder refuses a row that is
missing Hindi for any visible part. write(name) saves the batch as one SQL file to run
in a single transaction:
  supabase db query --linked --project-ref <ref> -f <file>
"""
import os
from bilingual import options_json, rewrite_sql, CLOSING_HI
from polity_common import C3, C4, T2, P4, P3, HOW_MANY, WHICH, PAIRS, SI, SI3, SI_CLOSING

OUT, TALLY = [], {}
ORDER = "Select the correct order using the code given below:"

def _t(key):
    TALLY[key] = TALLY.get(key, 0) + 1

CODE = "Select the correct answer using the code given below:"

def S(fid, topic, diff, body, body_hi, st, st_hi, ladder, ans, expl, expl_hi, cite, cg, roman=False, opts=None, opts_hi=None, closing=None):
    """ladder: C3/C4/T2, or None with opts (+ opts_hi optional) for a combination ladder.
    closing: CODE for a list of items that are not statements ("In which of the following
    places ...?" with the '1 and 2 only' ladder), as UPSC sets them."""
    assert closing in (None, CODE)
    closing = closing or (HOW_MANY if ladder in (C3, C4) else WHICH)
    qd = {"statements": st, "statements_hi": st_hi, "closing": closing, "closing_hi": CLOSING_HI[closing], "fixed_option_order": True}
    if roman:
        qd["numbering"] = "roman"
    bodies = ladder if ladder is not None else opts
    OUT.append(rewrite_sql(fid, topic=topic, typ="statement_based", diff=diff, body=body, body_hi=body_hi, qd=qd,
                           options=options_json(bodies, ans, opts_hi), explanation=expl, explanation_hi=expl_hi, citation=cite, cg=cg))
    _t(f"stmt:{len(st)}:{bodies[ans]}")

def M(fid, topic, diff, body, body_hi, opts, opts_hi, ans, expl, expl_hi, cite, cg):
    OUT.append(rewrite_sql(fid, topic=topic, typ="mcq", diff=diff, body=body, body_hi=body_hi, qd={},
                           options=options_json(opts, ans, opts_hi), explanation=expl, explanation_hi=expl_hi, citation=cite, cg=cg))
    _t("mcq")

def C(fid, topic, diff, body, body_hi, items, items_hi, opts, ans, expl, expl_hi, cite, cg):
    """Chronology: the items are numbered like statements; the options are sequences such
    as '2-4-3-1'. The options may shuffle, since each one is self-describing."""
    assert len(items) == len(items_hi)
    qd = {"statements": items, "statements_hi": items_hi, "closing": ORDER, "closing_hi": CLOSING_HI[ORDER]}
    OUT.append(rewrite_sql(fid, topic=topic, typ="mcq", diff=diff, body=body, body_hi=body_hi, qd=qd,
                           options=options_json(opts, ans, list(opts)), explanation=expl, explanation_hi=expl_hi, citation=cite, cg=cg))
    _t("chronology")

def P(fid, topic, diff, body, body_hi, pairs_en, pairs_hi, ans, expl, expl_hi, cite, cg):
    """pairs_en / pairs_hi: 'left : right' strings, split into the List-I and List-II columns."""
    ladder = P4 if len(pairs_en) == 4 else P3
    assert len(pairs_en) == len(pairs_hi) and len(pairs_en) in (3, 4)
    sp = lambda xs: [tuple(y.strip() for y in x.split(" : ")) for x in xs]
    en, hi = sp(pairs_en), sp(pairs_hi)
    assert all(len(t) == 2 for t in en + hi), "every pair needs exactly one ' : '"
    qd = {"list_1": [f"{i + 1}. {a}" for i, (a, _) in enumerate(en)], "list_1_hi": [f"{i + 1}. {a}" for i, (a, _) in enumerate(hi)],
          "list_2": [b for _, b in en], "list_2_hi": [b for _, b in hi], "closing": PAIRS, "closing_hi": CLOSING_HI[PAIRS], "fixed_option_order": True}
    OUT.append(rewrite_sql(fid, topic=topic, typ="match_the_following", diff=diff, body=body, body_hi=body_hi, qd=qd,
                           options=options_json(ladder, ans), explanation=expl, explanation_hi=expl_hi, citation=cite, cg=cg))
    _t(f"pairs:{ladder[ans]}")

def A(fid, topic, diff, s1, s1_hi, s2, s2_hi, ans, expl, expl_hi, cite, cg, s3=None, s3_hi=None):
    """Statement-I / Statement-II (and the 2025 three-statement form when s3 is given)."""
    qd = {"assertion": s1, "assertion_hi": s1_hi, "reason": s2, "reason_hi": s2_hi, "ar_labels": "statement",
          "closing": SI_CLOSING, "closing_hi": CLOSING_HI[SI_CLOSING], "fixed_option_order": True}
    ladder = SI
    if s3 is not None:
        qd["reason_2"], qd["reason_2_hi"], ladder = s3, s3_hi, SI3
    OUT.append(rewrite_sql(fid, topic=topic, typ="assertion_reason", diff=diff, body="Consider the following statements:",
                           body_hi="निम्नलिखित कथनों पर विचार कीजिए:", qd=qd, options=options_json(ladder, ans),
                           explanation=expl, explanation_hi=expl_hi, citation=cite, cg=cg))
    _t(f"{'SI3' if s3 else 'SI'}:{'abcd'[ans]}")

def O(fid, opts, opts_hi, ans):
    """Replace only the options of a kept MCQ (English and Hindi), e.g. to remove a
    length cue: the correct option must not be the one that stands out as longest or most
    qualified. The stem and explanation are untouched."""
    import json
    from bilingual import sql_q
    lens = [len(x) for x in opts]
    assert lens[ans] <= max(l for i, l in enumerate(lens) if i != ans), f"{fid}: the correct option is still the longest"
    OUT.append(f"update public.questions set options = {sql_q(json.dumps(options_json(opts, ans, opts_hi), ensure_ascii=False))}::jsonb, "
               f"updated_at = now() where id = '{fid}' and exam_category = 'upsc' and type = 'mcq' returning id;")
    _t("options-rebalanced")

def write(name):
    here = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(here, name), "w", encoding="utf-8").write("\n".join(OUT) + "\n")
    print(f"{name}: {len(OUT)} rows;", dict(sorted(TALLY.items())))
