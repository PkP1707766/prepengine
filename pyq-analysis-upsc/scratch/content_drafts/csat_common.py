# -*- coding: utf-8 -*-
"""Builders for the UPSC CSAT (Paper II) bank -- the CSAT counterpart of draft_common.py.

A CSAT paper is 80 items in 2 hours at +2.5 / -0.83 (docs/upsc-test-series-plan.md). The mix follows
pyq-analysis-upsc/upsc_csat_distribution_config.json and the playbook (Parts B, J, K):
34 Quantitative Aptitude, 18 Logical Reasoning, 28 Reading Comprehension in 10 short passages
(eight with three items, two with two), with a five-item data-sufficiency block (2 Quant + 3 Reasoning).

How the app holds CSAT (checked against src/ on 2026-10-06):
  - subject is one of the three CSAT subjects in AdminApp's SUBJECTS_BY_EXAM.upsc, topic one of its
    sub-topics (SUBTOPICS_BY_SUBJECT.upsc);
  - type is 'mcq' or 'statement_based' only: both render and score everywhere, while the
    reading_comprehension / data_sufficiency types have no exam-screen label yet;
  - the app has no passage object, so a passage travels in the body of each of its items, under
    UPSC's own directions line. The exam shows one item per screen, so every item stays answerable on
    its own, as in any computer-based test. Every row has its own concept_group_id (the generator never
    puts two rows of one concept group in a paper) and carries question_data.csat_set / csat_order /
    passage_group, so the paper can be assembled in its UPSC order with question shuffling off.

Every Quant and Reasoning key is checked in code before the row is accepted: a builder takes `check`,
a function that works the answer out by brute force or direct computation and must return the
option text marked correct. A row also refuses missing Hindi, and a text MCQ whose key is the longest
option."""
import json, os
from bilingual import combo_hi, sql_q, CLOSING_HI

QA, LR, RC = "Quantitative Aptitude", "Logical Reasoning", "Reading Comprehension"
TOPICS = {
    QA: ["Number Theory", "Speed-Distance-Time", "Percentage & Profit-Loss", "Ratio, Mixtures & Alligation", "Time & Work",
         "Permutation & Combination", "Geometry & Mensuration", "Sequences & Series", "Data Sufficiency", "Puzzle Hybrid"],
    LR: ["Statement-Conclusion/Assumption", "Seating Arrangement", "Blood Relation", "Direction & Distance", "Coding-Decoding",
         "Cube Painting", "Data Sufficiency", "Syllogism", "Truth-Liar"],
    RC: ["Main Idea", "Inference", "Assumption", "Author's Tone", "Specific Detail", "Best Summary"],
}
SET = None                      # e.g. "csat-l2-t01": the paper's prefix, set by the build script
ROWS, CGS = [], set()
SPREAD = {}
CODE = "Select the correct answer using the code given below:"
CODE_HI = CLOSING_HI[CODE]

T2 = ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"]
T2R = ["I only", "II only", "Both I and II", "Neither I nor II"]

RC_DIR = "Read the following passage and answer the item that follows. Your answer should be based solely on the passage."
RC_DIR_HI = "निम्नलिखित परिच्छेद को पढ़िए और उसके बाद दिए गए प्रश्नांश का उत्तर दीजिए। आपका उत्तर केवल परिच्छेद पर आधारित होना चाहिए।"

DS_INTRO = ("The item below contains a question followed by two statements. Decide whether the data in the statements "
            "are sufficient to answer the question.")
DS_INTRO_HI = "नीचे दिए गए प्रश्नांश में एक प्रश्न और उसके बाद दो कथन हैं। तय कीजिए कि कथनों में दिए गए आँकड़े प्रश्न का उत्तर देने के लिए पर्याप्त हैं या नहीं।"
DS_OPTS = ["The question can be answered using one of the statements alone, but not using the other statement alone",
           "The question can be answered using either statement alone",
           "The question can be answered using both the statements together, but not using either statement alone",
           "The question cannot be answered even using both the statements together"]
DS_OPTS_HI = ["प्रश्न का उत्तर किसी एक कथन के आधार पर अकेले दिया जा सकता है, पर दूसरे कथन के आधार पर अकेले नहीं",
              "प्रश्न का उत्तर किसी भी एक कथन के आधार पर अकेले दिया जा सकता है",
              "प्रश्न का उत्तर दोनों कथनों को साथ लेकर दिया जा सकता है, पर किसी भी एक कथन के आधार पर अकेले नहीं",
              "दोनों कथनों को साथ लेकर भी प्रश्न का उत्तर नहीं दिया जा सकता"]

CITE_Q = "Original item in the UPSC CSAT Paper II pattern (2023-26 papers); the key is verified by direct calculation."
CITE_L = "Original item in the UPSC CSAT Paper II pattern (2023-26 papers); the key is verified by checking every case."
CITE_R = "Original passage and item written for this series in the UPSC CSAT Paper II pattern (2023-26 papers)."

def _opts(bodies, ans, bodies_hi):
    assert len(bodies) == 4 and len(bodies_hi) == 4 and 0 <= ans < 4
    assert all(bodies_hi), "every option needs Hindi"
    return [{"id": "abcd"[k], "body": b, "body_hi": h, "isCorrect": k == ans} for k, (b, h) in enumerate(zip(bodies, bodies_hi))]

def _add(subj, topic, typ, diff, body, body_hi, qd, options, expl, expl_hi, cite, cg, slot, spread_key, group=None):
    assert SET, "set csat_common.SET first"
    assert subj in TOPICS and topic in TOPICS[subj], f"{cg}: {topic!r} is not a sub-topic of {subj}"
    assert diff in ("easy", "medium", "hard"), cg
    cg = f"{SET}-{cg}"
    assert cg not in CGS, f"duplicate concept group {cg}"
    CGS.add(cg)
    for k in ("statements",):
        if k in qd:
            assert len(qd[k]) == len(qd[k + "_hi"]), f"{cg}: {k} vs {k}_hi"
    if "closing" in qd:
        assert qd.get("closing_hi"), f"{cg}: closing has no Hindi"
    assert body_hi and expl and expl_hi, f"{cg}: missing Hindi or explanation"
    qd = dict(qd, csat_set=SET)
    if group:
        qd["passage_group"] = f"{SET}-{group}"
    ROWS.append({"subject": subj, "topic": topic, "type": typ, "difficulty": diff, "body": body, "body_hi": body_hi,
                 "question_data": qd, "options": options, "explanation": expl, "explanation_hi": expl_hi,
                 "source_citation": cite, "concept_group_id": cg, "slot": slot, "group": group})
    SPREAD[spread_key] = SPREAD.get(spread_key, 0) + 1

def _verify(cg, check, want):
    if check is None:
        return
    got = check()
    assert got == want, f"{cg}: check() gives {got!r} but the key is {want!r}"

def N(subj, topic, diff, body, body_hi, opts, key, expl, expl_hi, cg, check, opts_hi=None, craft="application", slot=None):
    """A direct-answer item: four options in a fixed order (ascending numbers, days in week order ...);
    `key` is the index of the correct one, and check() must return exactly that option's text."""
    _verify(cg, check, opts[key])
    opts_hi = opts_hi or list(opts)
    qd = {"fixed_option_order": True, "craft": craft}
    _add(subj, topic, "mcq", diff, body, body_hi, qd, _opts(opts, key, opts_hi), expl, expl_hi,
         CITE_Q if subj == QA else CITE_L, cg, slot or ("Q" if subj == QA else "L"), f"{subj[:2]} fixed: {'abcd'[key]}")

TEXT_SLOTS = [3, 1, 0, 2]   # where the key of each text MCQ goes, in turn
_tn = [0]

def T(subj, topic, diff, body, body_hi, opts, opts_hi, ans, expl, expl_hi, cg, craft="inference", pos=None, check=None,
      slot=None, group=None):
    """A text MCQ: the key is written at opts[ans] and moved to the next slot (or to pos), distractors
    keeping their order. The key must not be the longest option."""
    lens = [len(x) for x in opts]
    assert lens[ans] <= max(l for i, l in enumerate(lens) if i != ans), f"{cg}: the correct option is the longest"
    _verify(cg, check, opts[ans])
    if pos is None:
        pos = TEXT_SLOTS[_tn[0] % 4]
        _tn[0] += 1
    order = [i for i in range(4) if i != ans]
    order.insert(pos, ans)
    opts, opts_hi = [opts[i] for i in order], [opts_hi[i] for i in order]
    qd = {"craft": craft}
    cite = {QA: CITE_Q, LR: CITE_L, RC: CITE_R}[subj]
    _add(subj, topic, "mcq", diff, body, body_hi, qd, _opts(opts, pos, opts_hi), expl, expl_hi, cite, cg,
         slot or {QA: "Q", LR: "L", RC: "R"}[subj], f"{subj[:2]} text: {'abcd'[pos]}", group)

def S2(subj, topic, diff, body, body_hi, st, st_hi, key, expl, expl_hi, cg, roman=False, craft="inference", check=None,
       slot=None, group=None):
    """Two statements or conclusions with the code '1 only / 2 only / Both / Neither' (or I / II)."""
    assert len(st) == 2
    lad = T2R if roman else T2
    _verify(cg, check, lad[key])
    qd = {"statements": st, "statements_hi": st_hi, "closing": CODE, "closing_hi": CODE_HI, "fixed_option_order": True, "craft": craft}
    if roman:
        qd["numbering"] = "roman"
    cite = {QA: CITE_Q, LR: CITE_L, RC: CITE_R}[subj]
    _add(subj, topic, "statement_based", diff, body, body_hi, qd, _opts(lad, key, [combo_hi(x) for x in lad]), expl, expl_hi,
         cite, cg, slot or {QA: "Q", LR: "L", RC: "R"}[subj], f"two-statement: {lad[key]}", group)

def SC(subj, topic, diff, body, body_hi, st, st_hi, opts, key, expl, expl_hi, cg, opts_hi=None, roman=False, craft="inference",
       check=None, slot=None, group=None):
    """Three or four statements with combination options ('1 and 2 only', '1, 2 and 3', 'None of the above' ...),
    in the fixed order given."""
    assert 3 <= len(st) <= 4
    _verify(cg, check, opts[key])
    if opts_hi is None:
        opts_hi = ["उपर्युक्त में से कोई नहीं" if o == "None of the above" else combo_hi(o) for o in opts]
    qd = {"statements": st, "statements_hi": st_hi, "closing": CODE, "closing_hi": CODE_HI, "fixed_option_order": True, "craft": craft}
    if roman:
        qd["numbering"] = "roman"
    cite = {QA: CITE_Q, LR: CITE_L, RC: CITE_R}[subj]
    _add(subj, topic, "statement_based", diff, body, body_hi, qd, _opts(opts, key, opts_hi), expl, expl_hi, cite, cg,
         slot or {QA: "Q", LR: "L", RC: "R"}[subj], f"combo-{len(st)}: {'abcd'[key]}", group)

def DS(subj, diff, question, question_hi, s1, s1_hi, s2, s2_hi, key, expl, expl_hi, cg, check=None):
    """A data-sufficiency item with UPSC's four fixed instructions as its options. check() returns the
    key letter worked out by testing each statement alone and both together."""
    _verify(cg, check, "abcd"[key])
    qd = {"statements": [s1, s2], "statements_hi": [s1_hi, s2_hi], "numbering": "roman", "fixed_option_order": True, "craft": "inference"}
    body = DS_INTRO + "\n\nQuestion: " + question
    body_hi = DS_INTRO_HI + "\n\nप्रश्न: " + question_hi
    _add(subj, "Data Sufficiency", "mcq", diff, body, body_hi, qd, _opts(DS_OPTS, key, DS_OPTS_HI), expl, expl_hi,
         CITE_Q if subj == QA else CITE_L, cg, "DQ" if subj == QA else "DL", f"DS: {'abcd'[key]}")

PASSAGES = {}

def passage(pid, text, text_hi):
    """Register a passage; its items are added with RQ (in the order they appear on the paper)."""
    assert pid not in PASSAGES
    words = len(text.split())
    assert 70 <= words <= 260, f"{pid}: {words} words"
    PASSAGES[pid] = {"text": text, "text_hi": text_hi, "items": 0}
    return pid

def RQ(pid, topic, diff, form, stem, stem_hi, expl, expl_hi, cg_tail, **kw):
    """One item on passage pid. form: 'mcq' (kw opts, opts_hi, ans), 's2' (kw st, st_hi, key) or 'sc'
    (kw st, st_hi, opts, key)."""
    p = PASSAGES[pid]
    p["items"] += 1
    body = RC_DIR + "\n\nPassage\n" + p["text"] + "\n\n" + stem
    body_hi = RC_DIR_HI + "\n\nपरिच्छेद\n" + p["text_hi"] + "\n\n" + stem_hi
    cg = f"rc-{pid}-{cg_tail}"
    craft = "precision" if topic == "Specific Detail" else "inference"
    if form == "mcq":
        T(RC, topic, diff, body, body_hi, kw["opts"], kw["opts_hi"], kw["ans"], expl, expl_hi, cg, craft=craft, pos=kw.get("pos"), group=pid)
    elif form == "s2":
        S2(RC, topic, diff, body, body_hi, kw["st"], kw["st_hi"], kw["key"], expl, expl_hi, cg, craft=craft, group=pid)
    elif form == "sc":
        SC(RC, topic, diff, body, body_hi, kw["st"], kw["st_hi"], kw["opts"], kw["key"], expl, expl_hi, cg,
           opts_hi=kw.get("opts_hi"), craft=craft, group=pid)
    else:
        raise ValueError(form)

# ---------------------------------------------------------------- assembly
# One layout for an 80-item paper, modelled on the 2026 paper's flow: Quant and Reasoning items between
# ten passages, and the data-sufficiency block in the second half. Q = Quant, L = Reasoning, R3 / R2 = a
# passage with three or two items, DQ / DL = the data-sufficiency block's Quant / Reasoning items.
LAYOUT = ("Q Q L Q Q R3 Q L Q R3 Q Q L Q R3 L Q Q L R2 Q Q L Q R3 Q L Q Q R3 L Q Q L Q R3 Q L Q Q R2 "
          "DQ DQ DL DL DL R3 Q L Q Q L R3 Q Q L Q Q L Q L Q").split()

def assemble():
    """Give every row its position on the paper (question_data.csat_order) by filling the layout's slots
    in the order the rows were built, keeping each passage's items together and in order."""
    pool = {k: [r for r in ROWS if r["slot"] == k] for k in ("Q", "L", "DQ", "DL")}
    groups = []
    for r in ROWS:
        if r["slot"] == "R" and r["group"] not in groups:
            groups.append(r["group"])
    take = {k: iter(v) for k, v in pool.items()}
    gi = iter(groups)
    order = []
    for s in LAYOUT:
        if s.startswith("R"):
            g = next(gi)
            items = [r for r in ROWS if r["group"] == g]
            assert len(items) == int(s[1]), f"passage {g} has {len(items)} items but its slot holds {s[1]}"
            order.extend(items)
        else:
            order.append(next(take[s]))
    for k, it in take.items():
        assert next(it, None) is None, f"rows left over for slot {k}"
    assert next(gi, None) is None, "passages left over"
    assert len(order) == len(ROWS) == 80, (len(order), len(ROWS))
    for n, r in enumerate(order, 1):
        r["question_data"]["csat_order"] = n
    return order

def report(order):
    by = {}
    for r in order:
        by.setdefault(r["subject"], {}).setdefault(r["topic"], 0)
        by[r["subject"]][r["topic"]] += 1
    print("subjects:", {s: sum(t.values()) for s, t in by.items()})
    for s, t in by.items():
        print(" ", s, dict(t))
    diff = {}
    for r in order:
        diff[(r["subject"][:2], r["difficulty"])] = diff.get((r["subject"][:2], r["difficulty"]), 0) + 1
    print("difficulty:", dict(sorted(diff.items())))
    letters = {}
    for r in order:
        k = "abcd"[[o["isCorrect"] for o in r["options"]].index(True)]
        letters[k] = letters.get(k, 0) + 1
    print("key letters over the paper:", dict(sorted(letters.items())))
    print("spread by format:", json.dumps(dict(sorted(SPREAD.items())), ensure_ascii=False))
    print("passages:", {p: v["items"] for p, v in PASSAGES.items()})

def write(name, order):
    here = os.path.dirname(os.path.abspath(__file__))
    vals = []
    for r in order:
        vals.append("('upsc'," + ",".join(sql_q(x) for x in (r["subject"], r["topic"], r["type"], r["difficulty"], r["body"], r["body_hi"]))
                    + "," + sql_q(json.dumps(r["question_data"], ensure_ascii=False)) + "::jsonb,"
                    + sql_q(json.dumps(r["options"], ensure_ascii=False)) + "::jsonb,2.5,0.83,"
                    + ",".join(sql_q(r[k]) for k in ("explanation", "explanation_hi", "concept_group_id")) + ",'original_pattern_matched',"
                    + sql_q(r["source_citation"]) + ",'draft')")
    sql = ("insert into public.questions (exam_category, subject, topic, type, difficulty, body, body_hi, question_data, options, "
           "marks_correct, marks_wrong, explanation, explanation_hi, concept_group_id, source_type, source_citation, status)\nvalues\n"
           + ",\n".join(vals) + "\nreturning concept_group_id;\n")
    open(os.path.join(here, name), "w", encoding="utf-8").write(sql)
    json.dump([r["concept_group_id"] for r in order], open(os.path.join(here, name.replace(".sql", "_cgs.json")), "w"))
    print(f"{name}: {len(order)} rows")
