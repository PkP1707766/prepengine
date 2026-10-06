# -*- coding: utf-8 -*-
"""Build CSAT Level 2 · Test 7 (80 items) from its three sections and write one INSERT (status 'draft').

  PYTHONIOENCODING=utf-8 python csat_l2_t07_build.py

Every Quant and Reasoning key is re-derived in code while the sections load (csat_common.N/T/S2/SC/DS
take check=...), so a build that finishes is a build whose computed keys all agree. The rows carry
question_data.csat_set = 'csat-l2-t07' and csat_order 1-80 in the same layout as Tests 1-6, so the
test can be assembled in that order with question shuffling off."""
import csat_common as c
c.SET = "csat-l2-t07"
import csat_l2_t07_qa, csat_l2_t07_lr, csat_l2_t07_rc  # noqa: E402,F401  (loading them builds the rows)

# The Quant and Reasoning modules were written easy to hard within each topic, and interleave() keeps a
# topic's written order, which would leave most hard items in the last fifth of the paper. PLACE gives each
# topic's items in the order they should reach the paper: about three hard items in every ten positions
# (with the passages' own hard items), never three hard items in a row, and no answer letter more than
# three times running.
PLACE = {
    "Q": [["qa-nt-the-number-that-is-not-a-square", "qa-nt-three-surds-compared", "qa-nt-the-smallest-four-digit-multiple-of-12-15-18",
           "qa-nt-three-consecutive-squares-sum-365", "qa-nt-cube-of-x-plus-one-over-x", "qa-nt-a-repeating-decimal-as-a-fraction",
           "qa-nt-multiples-of-7-but-not-of-5", "qa-nt-the-least-a-with-a-squared-divisible-by-18"],
          ["qa-sdt-the-return-speed-that-makes-an-average", "qa-sdt-two-walkers-in-the-same-direction",
           "qa-sdt-buses-that-overtake-and-meet-a-walker", "qa-sdt-equal-times-at-two-speeds"],
          ["qa-rm-a-ratio-and-a-sum-of-squares", "qa-rm-a-diamond-worth-the-square-of-its-weight", "qa-rm-percentages-that-cancel",
           "qa-rm-pure-alcohol-added-to-a-solution", "qa-rm-water-in-milk-of-a-given-price"],
          ["qa-pp-simple-interest-from-two-amounts", "qa-pp-half-yearly-compounding-against-simple-interest", "qa-pp-two-successive-discounts"],
          ["qa-ss-a-series-that-alternates-two-operations", "qa-ss-a-series-whose-partial-sums-are-given"],
          ["qa-pc-a-card-that-is-red-or-a-king", "qa-pc-ten-people-split-into-two-teams"],
          ["qa-gm-fencing-a-semicircular-plot", "qa-gm-the-curved-surface-of-a-cone"],
          ["qa-tw-a-worker-25-per-cent-less-efficient", "qa-tw-a-job-that-is-behind-schedule"],
          ["qa-ph-three-people-on-a-library-rota", "qa-ph-climbing-stairs-one-or-two-at-a-time", "qa-ph-a-knockout-draw",
           "qa-ph-cutting-a-pizza-with-four-straight-cuts"]],
    "L": [["lr-sc-a-necessary-condition-taken-as-enough", "lr-sc-an-average-that-rises-when-a-member-leaves",
           "lr-sc-a-few-large-incomes-carry-the-average"],
          ["lr-sa-seven-parking-slots-one-empty", "lr-sa-a-queue-counted-from-both-ends", "lr-sa-a-row-facing-two-ways"],
          ["lr-br-my-son-s-father-s-brother-s-sister", "lr-br-a-maternal-uncle-s-wife"],
          ["lr-dd-a-spiral-walk", "lr-dd-a-walk-with-right-and-left-turns"],
          ["lr-cd-the-next-letter-of-its-own-kind", "lr-cd-a-coded-inequality-strict-and-weak"]],
}
for slot, topics in PLACE.items():
    for names in topics:
        idx = [i for i, r in enumerate(c.ROWS) if r["slot"] == slot and r["concept_group_id"][len(c.SET) + 1:] in names]
        rows = {c.ROWS[i]["concept_group_id"][len(c.SET) + 1:]: c.ROWS[i] for i in idx}
        assert len(rows) == len(names) and len({r["topic"] for r in rows.values()}) == 1, names
        assert len(names) == sum(r["slot"] == slot and r["topic"] == rows[names[0]]["topic"] for r in c.ROWS), names
        for i, n in zip(idx, names):
            c.ROWS[i] = rows[n]

c.interleave("Q")   # both modules are written topic by topic; spread each topic through the paper
c.interleave("L")
order = c.assemble()
c.report(order)
c.write("csat_l2_t07.sql", order)
