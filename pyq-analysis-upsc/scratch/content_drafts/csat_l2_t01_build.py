# -*- coding: utf-8 -*-
"""Build CSAT Level 2 · Test 1 (80 items) from its three sections and write one INSERT (status 'draft').

  PYTHONIOENCODING=utf-8 python csat_l2_t01_build.py

Every Quant and Reasoning key is re-derived in code while the sections load (csat_common.N/T/S2/SC/DS
take check=...), so a build that finishes is a build whose computed keys all agree. The rows carry
question_data.csat_set = 'csat-l2-t01' and csat_order 1-80 (the paper's UPSC-style sequence: Quant and
Reasoning between ten passages, the data-sufficiency block in the second half), so the test can be
assembled in that order with question shuffling off."""
import csat_common as c
c.SET = "csat-l2-t01"
import csat_l2_t01_qa, csat_l2_t01_lr, csat_l2_t01_rc  # noqa: E402,F401  (loading them builds the rows)

# The Quant and Reasoning modules were written easy to hard within each topic, which left hard items
# bunched in parts of the paper. PLACE (chosen by a small search, 2026-10-11) orders each topic's items
# within the positions they already hold: about three hard items in every ten positions, no three hard
# items in a row, and no answer letter more than three times running.
PLACE = {
    "Q": [
        ["qa-nt-remainder-5-divisible-7", "qa-nt-n3-n5-divisibility", "qa-nt-hcf-12-lcm-360-pairs", "qa-nt-hundred-sevens-mod-37", "qa-nt-6-or-15-not-both", "qa-nt-digit-7-one-to-300", "qa-nt-square-divisors-720", "qa-nt-three-digit-digit-sum-10"],
        ["qa-sdt-train-overtakes-walker", "qa-sdt-boat-still-water", "qa-sdt-circular-track-opposite", "qa-sdt-round-trip-two-speeds"],
        ["qa-rm-partnership-mid-year", "qa-rm-alloy-alligation", "qa-rm-teacher-raises-average", "qa-rm-repeated-dilution", "qa-rm-ages-two-ratios"],
        ["qa-pp-divide-instead-of-multiply", "qa-pp-markup-discount-false-weight", "qa-pp-more-than-less-than"],
        ["qa-ss-sum-k-times-k-plus-1", "qa-ss-two-term-sum-sequence"],
        ["qa-pc-triangles-four-collinear", "qa-pc-arrange-rr-together"],
        ["qa-tw-pipes-outlet-closed", "qa-tw-partner-leaves"],
        ["qa-gm-crossing-paths", "qa-gm-rectangles-3-by-4"],
        ["qa-ph-courier-insufficient", "qa-ph-coins-each-value-used", "qa-ph-minimum-measures-87", "qa-ph-fast-clock-correct-time"],
    ],
    "L": [
        ["lr-sc-umbrella-neither", "lr-sc-scholarship-contrapositive", "lr-sc-advertisement-assumptions"],
        ["lr-sa-rank-from-bottom", "lr-sa-circle-facing-centre", "lr-sa-six-in-a-row"],
        ["lr-br-coded-maternal-uncle", "lr-br-only-daughter-of-my-mother"],
        ["lr-dd-north-right-right", "lr-dd-morning-shadow-facing"],
        ["lr-cd-reverse-and-shift", "lr-cd-sentence-number-code"],
    ],
}
order = c.place(c.assemble(), PLACE)
c.report(order)
c.write("csat_l2_t01.sql", order)
