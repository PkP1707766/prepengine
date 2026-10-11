# -*- coding: utf-8 -*-
"""Build CSAT Level 2 · Test 6 (80 items) from its three sections and write one INSERT (status 'draft').

  PYTHONIOENCODING=utf-8 python csat_l2_t06_build.py

Every Quant and Reasoning key is re-derived in code while the sections load (csat_common.N/T/S2/SC/DS
take check=...), so a build that finishes is a build whose computed keys all agree. The rows carry
question_data.csat_set = 'csat-l2-t06' and csat_order 1-80 in the same layout as Tests 1-5, so the
test can be assembled in that order with question shuffling off."""
import csat_common as c
c.SET = "csat-l2-t06"
import csat_l2_t06_qa, csat_l2_t06_lr, csat_l2_t06_rc  # noqa: E402,F401  (loading them builds the rows)

c.interleave("Q")   # both modules are written topic by topic; spread each topic through the paper
c.interleave("L")
# The Quant and Reasoning modules were written easy to hard within each topic, which left hard items
# bunched in parts of the paper. PLACE (chosen by a small search, 2026-10-11) orders each topic's items
# within the positions they already hold: about three hard items in every ten positions, no three hard
# items in a row, and no answer letter more than three times running.
PLACE = {
    "Q": [
        ["qa-nt-two-primes-with-sum-99", "qa-nt-divisible-by-none-of-4-6-10", "qa-nt-exactly-three-divisors", "qa-nt-ratio-and-lcm-largest-number", "qa-nt-exponent-equation", "qa-nt-multiplier-for-a-perfect-cube", "qa-nt-terminating-decimal", "qa-nt-last-two-digits-of-7-to-2025"],
        ["qa-rm-provisions-for-a-fort", "qa-rm-working-partner-and-sleeping-partner", "qa-rm-drawn-off-and-refilled-with-the-second-liquid", "qa-rm-hostel-ratio-from-percentages", "qa-rm-three-vessels-emptied-together"],
        ["qa-sdt-runners-same-direction-on-a-track", "qa-sdt-trains-at-right-angles", "qa-sdt-counting-telegraph-posts", "qa-sdt-late-at-three-quarters-speed"],
        ["qa-ph-three-and-five-litre-jugs", "qa-ph-bat-and-ball", "qa-ph-cutting-a-log-into-pieces", "qa-ph-squares-on-a-chessboard"],
        ["qa-pp-compound-interest-doubling-to-eight-times", "qa-pp-slab-tax-and-income", "qa-pp-fresh-and-dried-grapes"],
        ["qa-ss-twice-the-last-term-less-one", "qa-ss-differences-that-double"],
        ["qa-pc-circular-table-two-seated-together", "qa-pc-arrangements-of-banana"],
        ["qa-gm-altitude-of-a-13-14-15-triangle", "qa-gm-sphere-dropped-into-a-cylinder"],
        ["qa-tw-two-workers-leave-before-the-end", "qa-tw-machines-and-articles"],
    ],
    "L": [
        ["lr-sc-failures-in-mathematics-course-of-action", "lr-sc-share-up-number-up", "lr-sc-trees-along-the-main-road"],
        ["lr-sa-order-of-speakers", "lr-sa-a-committee-under-four-conditions", "lr-sa-three-by-three-block-of-seats"],
        ["lr-br-the-only-daughter-in-law-of-a-grandfather", "lr-br-father-s-sister-s-daughter"],
        ["lr-dd-a-diagonal-that-makes-the-direction-exact", "lr-dd-two-diagonals-that-make-a-due-south"],
        ["lr-cd-the-ends-exchanged-the-middle-moved-on", "lr-cd-a-rule-that-depends-on-the-length-of-the-word"],
    ],
}
order = c.place(c.assemble(), PLACE)
c.report(order)
c.write("csat_l2_t06.sql", order)
