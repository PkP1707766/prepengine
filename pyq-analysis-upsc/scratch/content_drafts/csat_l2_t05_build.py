# -*- coding: utf-8 -*-
"""Build CSAT Level 2 · Test 5 (80 items) from its three sections and write one INSERT (status 'draft').

  PYTHONIOENCODING=utf-8 python csat_l2_t05_build.py

Every Quant and Reasoning key is re-derived in code while the sections load (csat_common.N/T/S2/SC/DS
take check=...), so a build that finishes is a build whose computed keys all agree. The rows carry
question_data.csat_set = 'csat-l2-t05' and csat_order 1-80 in the same layout as Tests 1-4, so the
test can be assembled in that order with question shuffling off."""
import csat_common as c
c.SET = "csat-l2-t05"
import csat_l2_t05_qa, csat_l2_t05_lr, csat_l2_t05_rc  # noqa: E402,F401  (loading them builds the rows)

c.interleave("Q")   # both modules are written topic by topic; spread each topic through the paper
c.interleave("L")
# The Quant and Reasoning modules were written easy to hard within each topic, which left hard items
# bunched in parts of the paper. PLACE (chosen by a small search, 2026-10-11) orders each topic's items
# within the positions they already hold: about three hard items in every ten positions, no three hard
# items in a row, and no answer letter more than three times running.
PLACE = {
    "Q": [
        ["qa-nt-hcf-from-prime-powers", "qa-nt-smallest-square-for-6-8-15", "qa-nt-triangular-number-with-equal-digits", "qa-nt-least-subtracted-for-a-square", "qa-nt-two-three-six-exponents", "qa-nt-remainder-one-for-2-and-3", "qa-nt-digit-sum-of-ten-to-25-less-25", "qa-nt-three-consecutive-even-numbers"],
        ["qa-rm-inverse-square-variation", "qa-rm-shares-as-fractions-of-the-others", "qa-rm-boys-leave-girls-join", "qa-rm-technicians-in-an-average", "qa-rm-joining-two-ratios"],
        ["qa-sdt-24-km-in-an-hour-and-20-minutes", "qa-sdt-gaining-2-km-each-hour", "qa-sdt-speeds-from-times-after-meeting", "qa-sdt-stolen-car-chased"],
        ["qa-ph-twenty-eight-handshakes", "qa-ph-race-margins-do-not-add", "qa-ph-matchsticks-for-a-row-of-squares", "qa-ph-exact-spend-on-pens-and-notebooks"],
        ["qa-pp-simple-interest-double-to-triple", "qa-pp-gain-equals-price-of-11-metres", "qa-pp-pass-mark-from-two-candidates"],
        ["qa-ss-sum-with-remainder-one-by-four", "qa-ss-squares-of-primes"],
        ["qa-pc-fifty-three-sundays", "qa-pc-password-letters-then-digits"],
        ["qa-gm-rhombus-from-its-diagonals", "qa-gm-turns-of-a-wheel"],
        ["qa-tw-three-pairs-of-workers", "qa-tw-wages-with-a-helper"],
    ],
    "L": [
        ["lr-sc-assumption-behind-a-second-bridge", "lr-sc-principle-applied-to-cases", "lr-sc-most-logical-conclusion"],
        ["lr-sa-houses-painted-in-a-row", "lr-sa-order-of-finishers", "lr-sa-rectangular-table-on-the-compass"],
        ["lr-br-daughters-share-a-brother", "lr-br-only-child-of-a-grandmother"],
        ["lr-dd-two-walkers-meet-again", "lr-dd-compass-names-turned"],
        ["lr-cd-rule-from-pythagorean-triples", "lr-cd-mirror-alphabet"],
    ],
}
order = c.place(c.assemble(), PLACE)
c.report(order)
c.write("csat_l2_t05.sql", order)
