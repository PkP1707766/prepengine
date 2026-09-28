# -*- coding: utf-8 -*-
"""Hindi for the UPSC bank: the fixed answer ladders and closings, and row builders
that carry Hindi alongside English.

House style for the Hindi (docs/upsc-hindi-style.md):
- The frame of a question (stem opener, closing line, answer ladder) uses the
  wording of UPSC's own Hindi paper, which Hindi-medium students already know.
- The content is plain, standard Hindi as in the NCERT Hindi textbooks: short
  sentences, common words, no heavy Sanskritisation. A technical term a student
  meets in English first gets the English in brackets on first use, e.g.
  "जैव-आवर्धन (biomagnification)".
- Numerals stay Western (1, 2, 3; अनुच्छेद 324), as on the UPSC paper.

Where this module stores Hindi (the app already renders every one of these):
  body_hi, explanation_hi                       -- columns
  question_data.statements_hi / list_1_hi / list_2_hi / assertion_hi /
  reason_hi / reason_2_hi / closing_hi         -- parallel keys
  options[i].body_hi                            -- inside each option object
"""
import json, re, hashlib

# ---- answer ladders (fixed-order options) -------------------------------------------
LADDER_HI = {
    "Only one": "केवल एक", "Only two": "केवल दो", "Only three": "केवल तीन",
    "All three": "सभी तीन", "All four": "सभी चार", "None": "कोई नहीं",
    "Only one pair": "केवल एक युग्म", "Only two pairs": "केवल दो युग्म", "Only three pairs": "केवल तीन युग्म",
    "All three pairs": "सभी तीन युग्म", "All four pairs": "सभी चार युग्म", "None of the pairs": "कोई भी युग्म नहीं",
    "Both 1 and 2": "1 और 2 दोनों", "Neither 1 nor 2": "न तो 1, न ही 2",
    "Both I and II": "I और II दोनों", "Neither I nor II": "न तो I, न ही II",
    # Verbatim UPSC Statement-I / Statement-II key, in the Hindi paper's wording.
    "Both Statement-I and Statement-II are correct and Statement-II is the correct explanation for Statement-I":
        "कथन-I और कथन-II दोनों सही हैं और कथन-II, कथन-I की सही व्याख्या है",
    "Both Statement-I and Statement-II are correct and Statement-II is not the correct explanation for Statement-I":
        "कथन-I और कथन-II दोनों सही हैं, किंतु कथन-II, कथन-I की सही व्याख्या नहीं है",
    "Statement-I is correct but Statement-II is incorrect": "कथन-I सही है, किंतु कथन-II गलत है",
    "Statement-I is incorrect but Statement-II is correct": "कथन-I गलत है, किंतु कथन-II सही है",
    # UPSC 2025 three-statement key.
    "Both Statement II and Statement III are correct and both of them explain Statement I":
        "कथन-II और कथन-III दोनों सही हैं और ये दोनों कथन-I की व्याख्या करते हैं",
    "Both Statement II and Statement III are correct but only one of them explains Statement I":
        "कथन-II और कथन-III दोनों सही हैं, किंतु इनमें से केवल एक ही कथन-I की व्याख्या करता है",
    "Only one of the Statements II and III is correct and that explains Statement I":
        "कथन-II और कथन-III में से केवल एक सही है और वही कथन-I की व्याख्या करता है",
    "Neither Statement II nor Statement III is correct": "न तो कथन-II सही है, न ही कथन-III",
}

_NUM = r"(?:\d+|I{1,3}|IV)"

def combo_hi(en):
    """'1 and 2 only' -> 'केवल 1 और 2'; '1, 2 and 3' -> '1, 2 और 3'; '3 only' -> 'केवल 3'."""
    if en in LADDER_HI:
        return LADDER_HI[en]
    m = re.fullmatch(rf"((?:{_NUM}, )*{_NUM})(?: and ({_NUM}))?( only)?", en)
    if not m:
        raise KeyError(f"no Hindi rule for option {en!r}")
    head, last, only = m.groups()
    s = head + (f" और {last}" if last else "")
    return ("केवल " + s) if only else s

# ---- closings and stem openers ------------------------------------------------------
CLOSING_HI = {
    "How many of the above statements are correct?": "उपर्युक्त में से कितने कथन सही हैं?",
    "Which of the statements given above is/are correct?": "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
    "How many of the pairs given above are correctly matched?": "उपर्युक्त में से कितने युग्म सही सुमेलित हैं?",
    "Which one of the following is correct in respect of the above statements?":
        "उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-सा एक सही है?",
    "Select the correct answer using the code given below:": "नीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
    "Select the correct answer using the codes given below:": "नीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
    "Which of the pairs given above is/are correctly matched?": "उपर्युक्त युग्मों में से कौन-सा/से सही सुमेलित है/हैं?",
    "Select the correct order using the code given below:": "नीचे दिए गए कूट का प्रयोग कर सही क्रम चुनिए:",
}
CONSIDER_HI = "निम्नलिखित कथनों पर विचार कीजिए:"

def sql_q(s):
    return "'" + s.replace("'", "''") + "'"

def ladder_sql():
    """One statement that gives every fixed-order ladder option its Hindi, and every standard
    closing its closing_hi, across the UPSC bank. Idempotent."""
    vals = ",\n  ".join(f"({sql_q(k)}, {sql_q(v)})" for k, v in LADDER_HI.items())
    combos = ["1 only", "2 only", "3 only", "1 and 2", "2 and 3", "1 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only",
              "1, 2 and 3", "I only", "II only", "III only", "I and II only", "II and III only", "I and III only", "I, II and III"]
    vals += ",\n  " + ",\n  ".join(f"({sql_q(c)}, {sql_q(combo_hi(c))})" for c in combos)
    cl = ",\n  ".join(f"({sql_q(k)}, {sql_q(v)})" for k, v in CLOSING_HI.items())
    # Two statements, not two CTEs: a single statement may modify a row only once, so a
    # second data-modifying CTE on the same rows would silently lose one of the updates.
    return f"""with m(en, hi) as (values
  {vals}
)
update public.questions q set options = (
    select jsonb_agg(case when m.hi is not null then o.v || jsonb_build_object('body_hi', m.hi) else o.v end order by o.ord)
    from jsonb_array_elements(q.options) with ordinality o(v, ord) left join m on m.en = o.v->>'body'),
  updated_at = now()
where q.exam_category = 'upsc' and coalesce((q.question_data->>'fixed_option_order')::boolean, false);

with c(en, hi) as (values
  {cl}
)
update public.questions q set question_data = q.question_data || jsonb_build_object('closing_hi', c.hi), updated_at = now()
from c where q.exam_category = 'upsc' and q.question_data->>'closing' = c.en;
"""

# ---- per-row Hindi for rows that are kept --------------------------------------------
QD_HI_KEYS = ("statements_hi", "list_1_hi", "list_2_hi", "assertion_hi", "reason_hi", "reason_2_hi", "closing_hi", "series_hi")

def hindi_update(full_id, body_hi, explanation_hi, qd_hi=None, options_hi=None, n_statements=None, n_pairs=None):
    """UPDATE that adds Hindi to one kept row without touching its English.
    qd_hi: parallel keys for question_data. options_hi: {'a': ..., 'b': ...} for non-ladder options.
    The WHERE clause re-checks the statement / pair count so a Hindi list can never be
    attached to a row it does not fit."""
    qd_hi = qd_hi or {}
    assert set(qd_hi) <= set(QD_HI_KEYS), set(qd_hi) - set(QD_HI_KEYS)
    sets = [f"body_hi = {sql_q(body_hi)}", f"explanation_hi = {sql_q(explanation_hi)}", "updated_at = now()"]
    if qd_hi:
        sets.append(f"question_data = question_data || {sql_q(json.dumps(qd_hi, ensure_ascii=False))}::jsonb")
    if options_hi:
        sets.append("options = (select jsonb_agg(case when h.hi ? (o.v->>'id') then o.v || jsonb_build_object('body_hi', h.hi->>(o.v->>'id')) else o.v end order by o.ord) "
                    f"from jsonb_array_elements(options) with ordinality o(v, ord), (select {sql_q(json.dumps(options_hi, ensure_ascii=False))}::jsonb as hi) h)")
    guard = ""
    if n_statements is not None:
        assert len(qd_hi.get("statements_hi", [])) == n_statements
        guard += f" and jsonb_array_length(question_data->'statements') = {n_statements}"
    if n_pairs is not None:
        assert len(qd_hi.get("list_1_hi", [])) == n_pairs == len(qd_hi.get("list_2_hi", []))
        guard += f" and jsonb_array_length(question_data->'list_1') = {n_pairs}"
    return f"update public.questions set {', '.join(sets)} where id = '{full_id}' and exam_category = 'upsc'{guard} returning id;"

# ---- full rewrites of a row (English and Hindi together) ------------------------------
def options_json(bodies, ans, bodies_hi=None):
    assert len(bodies) == 4 and 0 <= ans < 4
    bodies_hi = bodies_hi or [combo_hi(b) for b in bodies]
    return [{"id": "abcd"[k], "body": b, "body_hi": h, "isCorrect": k == ans} for k, (b, h) in enumerate(zip(bodies, bodies_hi))]

def rewrite_sql(full_id, *, topic, typ, diff, body, body_hi, qd, options, explanation, explanation_hi, citation, cg):
    """Replace a row's content in place (same id). Used where the audit found a giveaway,
    an outdated format or a stale fact. Only unpublished-test rows are rewritten."""
    for k in ("statements", "list_1", "list_2"):
        if k in qd:
            assert len(qd[k]) == len(qd[k + "_hi"]), f"{full_id}: {k} and {k}_hi differ in length"
    for k in ("assertion", "reason", "reason_2", "closing"):
        if k in qd:
            assert qd.get(k + "_hi"), f"{full_id}: {k} has no Hindi"
    assert all(o.get("body_hi") for o in options), f"{full_id}: an option has no Hindi"
    return ("update public.questions set "
            f"topic = {sql_q(topic)}, type = {sql_q(typ)}, difficulty = {sql_q(diff)}, body = {sql_q(body)}, body_hi = {sql_q(body_hi)}, "
            f"question_data = {sql_q(json.dumps(qd, ensure_ascii=False))}::jsonb, options = {sql_q(json.dumps(options, ensure_ascii=False))}::jsonb, "
            f"explanation = {sql_q(explanation)}, explanation_hi = {sql_q(explanation_hi)}, source_citation = {sql_q(citation)}, "
            f"concept_group_id = {sql_q(cg)}, updated_at = now() "
            f"where id = '{full_id}' and exam_category = 'upsc' returning id;")

if __name__ == "__main__":
    for s in ["1 only", "1 and 2 only", "1, 2 and 3", "I and III only", "2 and 3", "3 only", "I, II and III", "Both 1 and 2"]:
        print(s, "->", combo_hi(s))
