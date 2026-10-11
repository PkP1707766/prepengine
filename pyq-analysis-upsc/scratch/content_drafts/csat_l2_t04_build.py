# -*- coding: utf-8 -*-
"""Build CSAT Level 2 · Test 4 (80 items) from its three sections and write one INSERT (status 'draft').

  PYTHONIOENCODING=utf-8 python csat_l2_t04_build.py

Every Quant and Reasoning key is re-derived in code while the sections load (csat_common.N/T/S2/SC/DS
take check=...), so a build that finishes is a build whose computed keys all agree. The rows carry
question_data.csat_set = 'csat-l2-t04' and csat_order 1-80 in the same layout as Tests 1-3, so the
test can be assembled in that order with question shuffling off."""
import csat_common as c
c.SET = "csat-l2-t04"
import csat_l2_t04_qa, csat_l2_t04_lr, csat_l2_t04_rc  # noqa: E402,F401  (loading them builds the rows)

c.interleave("Q")   # both modules are written topic by topic; spread each topic through the paper
c.interleave("L")
# The Quant and Reasoning modules were written easy to hard within each topic, which left hard items
# bunched in parts of the paper. PLACE (chosen by a small search, 2026-10-11) orders each topic's items
# within the positions they already hold: about three hard items in every ten positions, no three hard
# items in a row, and no answer letter more than three times running.
PLACE = {
    "Q": [
        ["qa-nt-primes-from-50-to-100", "qa-nt-test-for-eleven", "qa-nt-x-divides-x-squared-plus-12", "qa-nt-100th-digit-of-one-seventh", "qa-nt-5a3b-divisible-by-36", "qa-nt-product-from-sum-and-squares", "qa-nt-least-number-to-add", "qa-nt-remainder-two-and-multiple-of-7"],
        ["qa-rm-shares-in-5-2-4-3", "qa-rm-family-average-before-a-birth", "qa-rm-ratio-after-taking-9-from-each", "qa-rm-men-length-and-days", "qa-rm-salaries-after-a-rise-and-a-fall"],
        ["qa-sdt-trains-with-staggered-start", "qa-sdt-faster-by-15-an-hour-less", "qa-sdt-times-from-speed-ratio", "qa-sdt-clock-hands-meet-after-four"],
        ["qa-ph-passengers-counted-backwards", "qa-ph-strikes-of-a-clock-in-a-day", "qa-ph-frog-in-a-well", "qa-ph-nine-coins-two-weighings"],
        ["qa-pp-profit-on-price-and-on-cost", "qa-pp-car-bought-cheaper-sold-dearer", "qa-pp-ci-less-si-over-three-years"],
        ["qa-ss-each-n-appears-n-times", "qa-ss-terms-needed-for-a-sum"],
        ["qa-pc-three-digit-numbers-from-0-to-4", "qa-pc-girls-kept-apart"],
        ["qa-gm-path-inside-a-field", "qa-gm-cylinder-wider-and-shorter"],
        ["qa-tw-twice-as-efficient", "qa-tw-man-hours"],
    ],
    "L": [
        ["lr-sc-later-start-comparison-group", "lr-sc-correlation-read-as-cause", "lr-sc-library-notice-on-bags"],
        ["lr-sa-round-table-some-face-out", "lr-sa-three-friends-cities-and-jobs", "lr-sa-square-table-corners-and-sides"],
        ["lr-br-count-the-men", "lr-br-grandfather-through-a-son"],
        ["lr-dd-legs-that-cancel", "lr-dd-two-walkers-opposite-ways"],
        ["lr-cd-product-written-backwards", "lr-cd-each-letter-one-place-further"],
    ],
}
order = c.place(c.assemble(), PLACE)
c.report(order)
c.write("csat_l2_t04.sql", order)
