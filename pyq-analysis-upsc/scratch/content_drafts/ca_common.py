# -*- coding: utf-8 -*-
"""Shared tools for the current-affairs papers (ca_tN_*.py), on the 2026 shape of the real paper.

The 2026 GS paper went back to combination answer codes ('1 and 2 only', '1, 2 and 3') for most multi-statement
items, kept only a handful of 'How many ... ?' counts, brought back List-I/List-II matching with codes, and used
negative items ('NOT correctly matched'). These helpers let a module write its statements once, with their truth,
and choose the answer format per item:

  FORMAT = {cg: ("combo", truth, pos)}     truth like (1, 1, 0): which statements are correct; pos 0-3 is where the
                                           correct combination goes. Distractors are near misses (one statement
                                           flipped first), and no statement may sit in all four options or in none,
                                           so no statement is given away by the options alone.
  MX(...)                                  List-I (A-D) matched with List-II (1-4), options as codes ('A-3, B-1, ...').
  finish(name, FORMAT, window, update)     converts the planned items, tags question_data.ca_window, and writes the
                                           INSERT (or, with update=True, the in-place UPDATE) through draft_common.

A converted item keeps its statements and explanation; finish() checks that the planned truth matches both the
original count key and the explanation's opening sentence, so a plan cannot silently change an answer."""
import itertools, re
import draft_common as d
from bilingual import options_json, CLOSING_HI
from polity_common import C3, C4, T2, HOW_MANY, WHICH

CODE = "Select the correct answer using the code given below:"

def _label(subset, n):
    s = [str(i + 1) for i in sorted(subset)]
    if len(s) == 1:
        return f"{s[0]} only"
    body = ", ".join(s[:-1]) + " and " + s[-1]
    return body if len(s) == n else body + " only"

def combo(truth, pos):
    """Four combination options with the true set at pos; near-miss distractors that give nothing away."""
    n, key = len(truth), frozenset(i for i, t in enumerate(truth) if t)
    assert key, "a combination code needs at least one correct statement (use a count ladder for 'None')"
    cands = [frozenset(c) for r in range(1, n + 1) for c in itertools.combinations(range(n), r) if frozenset(c) != key]
    best = None
    for trio in itertools.combinations(cands, 3):
        opts = (key,) + trio
        if any(all(i in o for o in opts) or not any(i in o for o in opts) for i in range(n)):
            continue
        score = (sum(len(o ^ key) for o in trio), sorted(sorted(o) for o in trio))
        if best is None or score < best[0]:
            best = (score, trio)
    assert best, f"no combination set for truth {truth}"
    trio = sorted(best[1], key=lambda o: (len(o), sorted(o)))
    trio.insert(pos, key)
    return [_label(o, n) for o in trio]

COUNT_OF = {"Only one": 1, "Only two": 2, "Only three": 3, "All three": 3, "All four": 4, "None": 0,
            "1 only": None, "2 only": None, "Both 1 and 2": None, "Neither 1 nor 2": None}
_WORDS = {"one": 1, "two": 2, "three": 3, "four": 4}

def _truth_from_expl(expl, n):
    """Read the explanation's opening claim: 'Statements 1 and 3 are correct', 'Only statement 2 is correct',
    'All three statements are correct', 'Both statements are correct', 'None of the statements is correct'."""
    head = expl.split(".")[0]
    if re.match(r"(All (three|four)|Both) statements are correct", head):
        return tuple([1] * n)
    if head.startswith("None of the statements"):
        return tuple([0] * n)
    m = re.match(r"(?:Only )?[Ss]tatements? ([\d, and]+) (?:is|are) correct", head)
    if m:
        nums = {int(x) for x in re.findall(r"\d", m.group(1))}
        return tuple(1 if i + 1 in nums else 0 for i in range(n))
    return None

def MX(topic, diff, body, body_hi, l1, l1_hi, l2, l2_hi, match, pos, expl, expl_hi, cite, cg, craft):
    """Match List-I (A-D) with List-II (1-4); match[i] is the List-II number (1-4) for List-I item i.
    The three distractor codes each swap one pair of the true code, chosen so that every List-I item
    changes in at least one option."""
    assert sorted(match) == [1, 2, 3, 4] and len(l1) == len(l2) == 4
    d._craft_ok(craft, cg)
    key = list(match)
    swaps = [(0, 1), (2, 3), (0, 2)]
    alts = []
    for a, b in swaps:
        m = list(key); m[a], m[b] = m[b], m[a]; alts.append(m)
    alts.sort()
    alts.insert(pos, key)
    code = lambda m: ", ".join(f"{'ABCD'[i]}-{m[i]}" for i in range(4))
    opts = [code(m) for m in alts]
    qd = {"list_1": [f"{'ABCD'[i]}. {x}" for i, x in enumerate(l1)], "list_1_hi": [f"{'ABCD'[i]}. {x}" for i, x in enumerate(l1_hi)],
          "list_2": [f"{i + 1}. {x}" for i, x in enumerate(l2)], "list_2_hi": [f"{i + 1}. {x}" for i, x in enumerate(l2_hi)],
          "closing": CODE, "closing_hi": CLOSING_HI[CODE], "fixed_option_order": True, "craft": craft}
    d._add(topic, "match_the_following", diff, body, body_hi, qd, options_json(opts, pos, opts), expl, expl_hi, cite, cg,
           f"match-code: {'abcd'[pos]}")

def _render(nums, joiner):
    nums = sorted(nums)
    return str(nums[0]) if len(nums) == 1 else ", ".join(map(str, nums[:-1])) + joiner + str(nums[-1])

def renumber(text, newnum, hindi=False):
    """Rewrite statement numbers ('Statements 1 and 3', 'कथन 2') after the statements are reordered."""
    if hindi:
        rx, joiner = re.compile(r"कथन ((?:\d+)(?:(?:, | और )\d+)*)"), " और "
        return rx.sub(lambda m: "कथन " + _render([newnum[int(x)] for x in re.findall(r"\d+", m.group(1))], joiner), text)
    rx, joiner = re.compile(r"\b([Ss]tatements?) ((?:\d+)(?:(?:, | and )\d+)*)"), " and "
    return rx.sub(lambda m: m.group(1) + " " + _render([newnum[int(x)] for x in re.findall(r"\d+", m.group(2))], joiner), text)

def _reorder(r, perm):
    """perm[i] = the old position (0-based) of the statement that goes to position i."""
    qd = r["question_data"]
    n = len(qd["statements"])
    assert sorted(perm) == list(range(n)), perm
    newnum = {perm[i] + 1: i + 1 for i in range(n)}
    for k in ("statements", "statements_hi"):
        qd[k] = [qd[k][p] for p in perm]
    r["explanation"] = renumber(r["explanation"], newnum)
    r["explanation_hi"] = renumber(r["explanation_hi"], newnum, hindi=True)

def finish(name, plan, window, update=False, replaces=None):
    """plan[cg] = ("combo", truth, pos[, perm]) -- truth in the authored order; perm reorders the statements so the
    correct ones do not cluster at the top -- or ("perm", perm) to reorder a two-statement or count item only."""
    for r in d.ROWS:
        cg = r["concept_group_id"]
        r["question_data"]["ca_window"] = window
        if cg not in plan:
            continue
        spec = plan[cg]
        st = r["question_data"].get("statements") or []
        if spec[0] == "perm":
            perm = spec[1]
            said = _truth_from_expl(r["explanation"], len(st))
            _reorder(r, perm)
            if said is not None:
                truth = tuple(said[p] for p in perm)
                assert _truth_from_expl(r["explanation"], len(st)) == truth, f"{cg}: renumbered explanation disagrees"
                if len(st) == 2:                               # the T2 key follows the statements
                    k = {(1, 0): 0, (0, 1): 1, (1, 1): 2, (0, 0): 3}[truth]
                    r["options"] = options_json(T2, k)
            continue
        fmt, truth, pos = spec[:3]
        perm = spec[3] if len(spec) > 3 else tuple(range(len(st)))
        assert fmt == "combo" and r["type"] == "statement_based", cg
        assert len(truth) == len(st), f"{cg}: truth has {len(truth)} values for {len(st)} statements"
        old = next(o["body"] for o in r["options"] if o["isCorrect"])
        if COUNT_OF.get(old) is not None:
            assert sum(truth) == COUNT_OF[old], f"{cg}: plan truth {truth} disagrees with the count key '{old}'"
        said = _truth_from_expl(r["explanation"], len(st))
        assert said is None or said == tuple(truth), f"{cg}: plan truth {truth} disagrees with the explanation {said}"
        _reorder(r, perm)
        truth = tuple(truth[p] for p in perm)
        said = _truth_from_expl(r["explanation"], len(st))
        assert said is None or said == truth, f"{cg}: renumbered explanation {said} disagrees with {truth}"
        opts = combo(truth, pos)
        r["options"] = options_json(opts, pos)
        r["question_data"].update({"closing": WHICH, "closing_hi": CLOSING_HI[WHICH]})
    d.write(name)                      # the INSERT stays the paper's full build
    if update:                         # rows already in the bank: rewrite them in place, keeping their ids
        upd = name.replace(".sql", "_upd.sql")  # published rows too: a CA paper is revised only before anyone sits it
        d.write_updates(upd, replaces=replaces or {}, statuses=("draft", "published"))
        if replaces:                   # usages record the concept id; keep them in step with a renamed row
            import os
            path = os.path.join(os.path.dirname(os.path.abspath(d.__file__)), upd)
            s = open(path, encoding="utf-8").read().rstrip("\n")
            assert s.endswith("commit;")
            extra = "".join(f"update public.question_usages set concept_group_id = '{new}' where concept_group_id = '{old}';\n"
                            for new, old in replaces.items())
            open(path, "w", encoding="utf-8", newline="\n").write(s[:-len("commit;")] + extra + "commit;\n")
