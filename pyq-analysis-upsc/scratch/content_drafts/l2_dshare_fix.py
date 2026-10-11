# -*- coding: utf-8 -*-
"""Fix the under-use of answer (d) in the Level-2 GS papers (owner's go-ahead, 2026-10-11).

The fixed UPSC ladders put "None" / "Neither" / "All four" at (d), and the bank had drifted to
"Only one" / "Only two" keys, so a paper had only 8-20 (d) answers -- a pattern a candidate could exploit.
Two kinds of change, both recorded in l2_dshare_fix.sql:
  1. MCQ reorders (l2_dshare_reorders.py): where option order carries no meaning, the key moves to (d)
     and the distractors keep their order; MCQ (d) share per paper is capped at about 36 %.
  2. Content re-keys (l2_dshare_edits_*.py): the one true statement of an "Only one" item becomes a precise
     near-miss, so the answer is "None"; the explanation's opening is rewritten and the rest kept.
Run: PYTHONIOENCODING=utf-8 python l2_dshare_fix.py <rows.json> -- rows.json is an export of the papers'
rows (id, concept_group_id as cg, options, question_data as qd, explanation, explanation_hi)."""
import glob, importlib, io, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

def q(s): return "'" + str(s).replace("'", "''") + "'"
def j(o): return q(json.dumps(o, ensure_ascii=False)) + "::jsonb"

def main():
    raw = io.open(sys.argv[1], encoding="utf-8").read()
    rows = {r["cg"]: r for r in json.loads(raw[raw.index("{"):raw.rindex("}") + 1])["rows"]}
    from l2_dshare_reorders import REORDERS as reorders
    edits = []
    for f in sorted(glob.glob(os.path.join(HERE, "l2_dshare_edits_*.py"))):
        edits += importlib.import_module(os.path.basename(f)[:-3]).EDITS
    sql, done = ["begin;"], set()
    for cg, key_was in reorders.items():
        r = rows[cg]
        o = r["options"] if isinstance(r["options"], list) else json.loads(r["options"])
        ki = [x["isCorrect"] for x in o].index(True)
        assert "abcd"[ki] == key_was, cg
        order = [i for i in range(4) if i != ki] + [ki]
        new = [{"id": "abcd"[n], "body": o[i]["body"], "body_hi": o[i].get("body_hi"), "isCorrect": i == ki} for n, i in enumerate(order)]
        sql.append(f"update public.questions set options = {j(new)}, updated_at = now() where concept_group_id = {q(cg)} returning concept_group_id;")
        done.add(cg)
    for cg, n, en, hi, head_en, head_hi in edits:
        assert cg not in done, f"{cg} edited twice"
        r = rows[cg]
        qd = r["qd"] if isinstance(r["qd"], dict) else json.loads(r["qd"])
        o = r["options"] if isinstance(r["options"], list) else json.loads(r["options"])
        assert [x["body"] for x in o][3] in ("None", "Neither 1 nor 2", "Neither I nor II"), cg
        ki = [x["isCorrect"] for x in o].index(True)
        assert ki in (0, 1), f"{cg}: expected an 'Only one' / '1 only' / '2 only' key"
        if head_en.startswith("FULL:"):          # explanation that names no other statement: replaced whole
            assert head_hi.startswith("FULL:") and r["explanation"].startswith(f"Only statement {n} is correct"), cg
        else:
            m_en = re.match(r"^(Only statement (\d) is correct.*?)\s+(?=Statements? \d)", r["explanation"], re.S)
            m_hi = re.match(r"^(केवल कथन (\d) सही है.*?)\s+(?=कथन \d)", r["explanation_hi"], re.S)
            assert m_en and m_hi and int(m_en.group(2)) == n == int(m_hi.group(2)), f"{cg}: explanation opening not found for statement {n}"
        qd = dict(qd)
        st, st_hi = list(qd["statements"]), list(qd["statements_hi"])
        st[n - 1], st_hi[n - 1] = en, hi
        qd["statements"], qd["statements_hi"] = st, st_hi
        new_o = [dict(x, isCorrect=(k == 3)) for k, x in enumerate(o)]
        if head_en.startswith("FULL:"):
            expl, expl_hi = head_en[5:], head_hi[5:]
        else:
            expl = head_en + " " + r["explanation"][m_en.end():]
            expl_hi = head_hi + " " + r["explanation_hi"][m_hi.end():]
        sql.append(f"update public.questions set question_data = {j(qd)}, options = {j(new_o)}, explanation = {q(expl)}, explanation_hi = {q(expl_hi)}, "
                   f"updated_at = now() where concept_group_id = {q(cg)} returning concept_group_id;")
        done.add(cg)
    sql.append("commit;")
    sql.append(f"select count(*) as rows_touched from public.questions where concept_group_id = any(array[{', '.join(q(c) for c in sorted(done))}]);")
    io.open(os.path.join(HERE, "l2_dshare_fix.sql"), "w", encoding="utf-8", newline="\n").write("\n".join(sql) + "\n")
    print(f"l2_dshare_fix.sql: {len(reorders)} reorders, {len(edits)} re-keys")

if __name__ == "__main__":
    main()
