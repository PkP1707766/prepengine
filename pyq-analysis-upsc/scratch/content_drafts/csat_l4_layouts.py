# -*- coding: utf-8 -*-
"""The three 80-item layouts of the Level 4 CSAT simulators, one for each recent shape of the real paper
(subject counts from the high-confidence coaching consensus in scratch/build_csat_distribution.py):

  A -- 2023/2024: Quant 38, Reasoning 15, RC 27 on 9 passages of 3 items.          Simulators 1, 4, 7
  B -- 2025:      Quant 34, Reasoning 17, RC 29 on 10 passages (9 x 3, 1 x 2).      Simulators 2, 5, 8
  C -- 2026:      Quant 37, Reasoning 20, RC 23 on 10 passages (3 x 3, 7 x 2).      Simulators 3, 6, 9

Every layout keeps the 2026 five-item data-sufficiency block (2 Quant + 3 Reasoning, so the Q and L slots hold the
rest), passes the passages evenly through the paper, and puts the block a little past the middle. Slot names are those
of csat_common.assemble(): Q, L, R<n> (a passage with n items), DQ, DL."""

def make(nq, nl, passages, ds_after):
    """nq Quant and nl Reasoning slots in an even mix, the passages spread evenly between them, and the data-sufficiency
    block after the ds_after-th Quant-or-Reasoning slot."""
    n = nq + nl
    mix, ql = [], 0
    for i in range(n):                       # Bresenham: an L wherever the running share of L falls behind
        if (ql + 1) * n <= (i + 1) * nl:
            mix.append("L"); ql += 1
        else:
            mix.append("Q")
    at = [round((k + 1) * n / (len(passages) + 1)) for k in range(len(passages))]
    out = []
    for i, s in enumerate(mix, 1):
        out.append(s)
        for k, a in enumerate(at):
            if a == i:
                out.append(f"R{passages[k]}")
        if i == ds_after:
            out += ["DQ", "DQ", "DL", "DL", "DL"]
    assert out.count("Q") == nq and out.count("L") == nl and out.count("DQ") == 2 and out.count("DL") == 3
    assert sum(int(s[1]) for s in out if s.startswith("R")) == sum(passages)
    assert len(out) - len(passages) + sum(passages) == 80, out
    assert out[0] in ("Q", "L") and out[1] in ("Q", "L")
    return out

LAYOUT_A = make(36, 12, [3] * 9, 30)
LAYOUT_B = make(32, 14, [3, 3, 3, 3, 2, 3, 3, 3, 3, 3], 28)
LAYOUT_C = make(35, 17, [2, 3, 2, 2, 3, 2, 2, 3, 2, 2], 31)

if __name__ == "__main__":
    for name, lay in (("A", LAYOUT_A), ("B", LAYOUT_B), ("C", LAYOUT_C)):
        print(name, " ".join(lay))
