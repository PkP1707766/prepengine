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

order = c.assemble()
c.report(order)
c.write("csat_l2_t01.sql", order)
