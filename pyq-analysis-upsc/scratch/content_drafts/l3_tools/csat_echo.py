# -*- coding: utf-8 -*-
"""Echo check for a new CSAT paper against every earlier CSAT paper's INSERT file.

  python l3_tools/csat_echo.py csat_l3_t01.sql            (from content_drafts/)

An echo is an old item reappearing in a new form: the same numbers in a Quant or Reasoning stem (Level 2 Test 7
reused Test 5's 28 handshakes and ran Test 2's 30 / 60 -> 40 km/h average backwards), or the same run of seven words
in a stem or a passage once the fixed frames (directions, closings, the data-sufficiency instructions) are stripped.
It reads the rows straight from the SQL (15 quoted fields per row, as csat_common.write() prints them). A Quant or
Reasoning pair is flagged when the two share a sub-topic and two or more numbers of two digits or more, or any
seven-word run; across sub-topics, when they share three such numbers or two seven-word runs (stock phrasing such as
'which one of the following, if true' otherwise floods the report). A passage is flagged on any shared seven-word run.
Each flag needs reading."""
import glob, io, json, os, re, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIT = re.compile(r"'((?:[^']|'')*)'")
FRAMES = ["Read the following passage and answer the item that follows. Your answer should be based solely on the passage.",
          "The item below contains a question followed by two statements. Decide whether the data in the statements are sufficient to answer the question.",
          "Select the correct answer using the code given below:", "Which of the following conclusions follow(s) from the statements?",
          "Which one of the following statements best reflects the crux of the passage?",
          "Which one of the following statements best reflects the most logical and rational message conveyed by the passage?",
          "On the basis of the passage, which of the following conclusions is/are valid?",
          "Which of the following assumptions has/have been made in the passage?"]

def rows(path):
    out = []
    text = io.open(path, encoding="utf-8").read()
    lits = [x.replace("''", "'") for x in LIT.findall(text.split("\nvalues\n", 1)[1])]
    for i in range(0, len(lits), 15):        # 15 quoted fields per row, from 'upsc' to the status
        f = lits[i:i + 15]
        assert f[0] == "upsc" and f[14] in ("draft", "published"), (path, i)
        qd = json.loads(f[7])
        stem = f[5]
        for fr in FRAMES:
            stem = stem.replace(fr, " ")
        passage = ""
        if "\n\nPassage\n" in f[5]:
            passage = f[5].split("\n\nPassage\n", 1)[1].rsplit("\n\n", 1)[0]
            stem = f[5].rsplit("\n\n", 1)[1]
        text = stem + " " + " ".join(qd.get("statements") or [])
        out.append({"cg": f[11], "subject": f[1], "topic": f[2], "text": text, "passage": passage})
    return out

def nums(t):
    return {n.replace(",", "") for n in re.findall(r"\d[\d,]*\.?\d*", t) if len(n.replace(",", "").rstrip(".")) >= 2}

def shingles(t, k=7):
    w = re.findall(r"[a-z0-9']+", t.lower())
    return {" ".join(w[i:i + k]) for i in range(len(w) - k + 1)}

def main():
    new_path = sys.argv[1]
    new = rows(os.path.join(HERE, new_path))
    old = []
    for p in sorted(glob.glob(os.path.join(HERE, "csat_l*.sql"))):
        if os.path.basename(p) != os.path.basename(new_path) and not re.search(r"_fix|_update", p):
            old += rows(p)
    print(len(new), "new rows against", len(old), "earlier rows")
    seen_passages = {}
    flags = 0
    for r in new:
        if r["passage"]:
            sp = shingles(r["passage"])
            for o in old:
                if o["passage"] and o["passage"] not in seen_passages.get(r["cg"], set()):
                    common = sp & shingles(o["passage"])
                    if common:
                        flags += 1
                        print(f"PASSAGE {r['cg']} ~ {o['cg']}: {sorted(common)[0]!r}")
                        seen_passages.setdefault(r["cg"], set()).add(o["passage"])
        else:
            nr, sr = nums(r["text"]), shingles(r["text"])
            for o in old:
                if o["passage"]:
                    continue
                shared = nr & nums(o["text"])
                common = sr & shingles(o["text"])
                same = o["topic"] == r["topic"]
                if (same and (len(shared) >= 2 or common)) or len(shared) >= 3 or len(common) >= 2:
                    flags += 1
                    print(f"{r['cg']} ~ {o['cg']}: numbers {sorted(shared)} words {sorted(common)[:1]}")
    print("flags:", flags)

if __name__ == "__main__":
    main()
