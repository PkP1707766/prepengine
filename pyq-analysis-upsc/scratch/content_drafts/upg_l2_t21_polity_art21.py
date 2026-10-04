# -*- coding: utf-8 -*-
"""Level 2 · Test 21 -- one-row fix of 2026-10-04. Statement 1 of rights-internet-defamation-sleep used
Anuradha Bhasin (internet shutdowns), which Test 3's verdicts-anuradha-bhasin-internet already tests, so it
now uses Paschim Banga Khet Mazdoor Samity (1996): emergency treatment as part of Article 21. Same key
(Only two). The row's text lives in gs_l2_t21_polity_v2.py, whose rename to this concept id is already
live, so this file rewrites only that row, matched on its new id."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
import gs_l2_t21_polity_v2  # noqa: F401 -- registers the Test 21 Polity rows

d.ROWS[:] = [r for r in d.ROWS if r["concept_group_id"] == "rights-internet-defamation-sleep"]
assert len(d.ROWS) == 1

if __name__ == "__main__":
    d.write_updates("upg_l2_t21_polity_art21.sql")
