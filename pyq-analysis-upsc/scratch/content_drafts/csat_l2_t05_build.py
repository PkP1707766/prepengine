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
order = c.assemble()
c.report(order)
c.write("csat_l2_t05.sql", order)
