# -*- coding: utf-8 -*-
"""Build CSAT Level 2 · Test 3 (80 items) from its three sections and write one INSERT (status 'draft').

  PYTHONIOENCODING=utf-8 python csat_l2_t03_build.py

Every Quant and Reasoning key is re-derived in code while the sections load (csat_common.N/T/S2/SC/DS
take check=...), so a build that finishes is a build whose computed keys all agree. The rows carry
question_data.csat_set = 'csat-l2-t03' and csat_order 1-80 in the same layout as Tests 1 and 2, so the
test can be assembled in that order with question shuffling off."""
import csat_common as c
c.SET = "csat-l2-t03"
import csat_l2_t03_qa, csat_l2_t03_lr, csat_l2_t03_rc  # noqa: E402,F401  (loading them builds the rows)

c.interleave("Q")   # both modules are written topic by topic; spread each topic through the paper
c.interleave("L")
# The Quant and Reasoning modules were written easy to hard within each topic, which left hard items
# bunched in parts of the paper. PLACE (chosen by a small search, 2026-10-11) orders each topic's items
# within the positions they already hold: about three hard items in every ten positions, no three hard
# items in a row, and no answer letter more than three times running.
PLACE = {
    "Q": [
        ["qa-nt-remainders-two-short", "qa-nt-largest-of-four-powers", "qa-nt-factorial-sum-mod-12", "qa-nt-odd-number-of-divisors", "qa-nt-difference-of-squares-45", "qa-nt-remainder-136-then-17", "qa-nt-digits-reversed-27", "qa-nt-sum-of-odd-divisors-360"],
        ["qa-rm-water-to-reverse-ratio", "qa-rm-two-vessels-to-two-to-one", "qa-rm-incomes-and-expenditures", "qa-rm-twice-thrice-four-times", "qa-rm-batting-average-up-by-2"],
        ["qa-sdt-pole-and-platform", "qa-sdt-bus-stoppage-minutes", "qa-sdt-bird-between-cyclists", "qa-sdt-escalator-steps"],
        ["qa-ph-pens-and-pencils", "qa-ph-two-black-socks-in-the-dark", "qa-ph-class-size-not-given", "qa-ph-twice-as-old-as-b-was"],
        ["qa-pp-price-up-consumption-down", "qa-pp-savings-unchanged", "qa-pp-chain-of-two-sales"],
        ["qa-ss-gp-from-third-and-sixth", "qa-ss-wrong-term-rising-multipliers"],
        ["qa-pc-prizes-with-repeats", "qa-pc-grid-routes-4-by-3"],
        ["qa-gm-incircle-7-24-25", "qa-gm-ladder-slides-down"],
        ["qa-tw-men-and-women-equivalence", "qa-tw-alternate-days"],
    ],
    "L": [
        ["lr-sc-metro-rival-cause", "lr-sc-pass-overlap-bounds", "lr-sc-dengue-course-of-action"],
        ["lr-sa-two-rows-facing", "lr-sa-second-lightest-box", "lr-sa-week-of-lectures"],
        ["lr-br-only-son-of-d", "lr-br-chain-folds-back"],
        ["lr-dd-turns-by-angles", "lr-dd-towns-without-distances"],
        ["lr-cd-swapped-operators", "lr-cd-forward-and-back-in-turn"],
    ],
}
order = c.place(c.assemble(), PLACE)
c.report(order)
c.write("csat_l2_t03.sql", order)
