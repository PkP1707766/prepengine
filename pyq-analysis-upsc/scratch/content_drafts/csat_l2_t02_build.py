# -*- coding: utf-8 -*-
"""Build CSAT Level 2 · Test 2 (80 items) from its three sections and write one INSERT (status 'draft').

  PYTHONIOENCODING=utf-8 python csat_l2_t02_build.py

Every Quant and Reasoning key is re-derived in code while the sections load (csat_common.N/T/S2/SC/DS
take check=...), so a build that finishes is a build whose computed keys all agree. The rows carry
question_data.csat_set = 'csat-l2-t02' and csat_order 1-80 in the same layout as Test 1, so the test can
be assembled in that order with question shuffling off."""
import csat_common as c
c.SET = "csat-l2-t02"
import csat_l2_t02_qa, csat_l2_t02_lr, csat_l2_t02_rc  # noqa: E402,F401  (loading them builds the rows)

c.interleave("Q")   # the Quant module is written topic by topic; spread each topic through the paper
# The Quant and Reasoning modules were written easy to hard within each topic, which left hard items
# bunched in parts of the paper. PLACE (chosen by a small search, 2026-10-11) orders each topic's items
# within the positions they already hold: about three hard items in every ten positions, no three hard
# items in a row, and no answer letter more than three times running.
PLACE = {
    "Q": [
        ["qa-nt-same-remainder-largest-divisor", "qa-nt-neither-square-nor-cube", "qa-nt-units-digit-7-95-3-58", "qa-nt-three-consecutive-odd", "qa-nt-trailing-zeros-100-factorial", "qa-nt-hcf-12-sum-60", "qa-nt-smallest-with-ten-divisors", "qa-nt-remainders-5-and-7"],
        ["qa-rm-father-son-ratio", "qa-rm-chained-fraction-shares", "qa-rm-rice-alligation-profit", "qa-rm-overlapping-averages", "qa-rm-equal-volumes-mixture"],
        ["qa-sdt-late-and-early", "qa-sdt-race-head-start", "qa-sdt-half-and-half-average", "qa-sdt-two-trains-cross"],
        ["qa-ph-weights-both-pans-1-to-40", "qa-ph-26-january-to-15-august", "qa-ph-coins-by-ratio", "qa-ph-tea-coffee-exactly-one"],
        ["qa-pp-buy-below-sell-above-list", "qa-pp-same-price-profit-loss", "qa-pp-election-voters-on-list"],
        ["qa-ss-n-times-n-plus-1-series", "qa-ss-ap-sum-20-terms"],
        ["qa-pc-committee-at-least-one-woman", "qa-pc-two-dice-prime-sum"],
        ["qa-gm-diagonals-12-gon", "qa-gm-square-wire-to-circle"],
        ["qa-tw-outlet-rate", "qa-tw-workers-join-midway"],
    ],
    "L": [
        ["lr-sc-onion-price-cause-effect", "lr-sc-late-entry-contrapositive", "lr-sc-tobacco-age-assumptions"],
        ["lr-sa-row-facing-south", "lr-sa-rank-swap-row-length", "lr-sa-five-floors"],
        ["lr-br-family-gender-unknown", "lr-br-son-of-mothers-brother"],
        ["lr-dd-pythagoras-north-west", "lr-dd-turned-clock-hour-hand"],
        ["lr-cd-word-code-red", "lr-cd-sum-times-length-rule"],
    ],
}
order = c.place(c.assemble(), PLACE)
c.report(order)
c.write("csat_l2_t02.sql", order)
