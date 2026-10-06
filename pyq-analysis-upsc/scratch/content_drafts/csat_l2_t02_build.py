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
order = c.assemble()
c.report(order)
c.write("csat_l2_t02.sql", order)
