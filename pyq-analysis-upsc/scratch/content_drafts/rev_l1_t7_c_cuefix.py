# -*- coding: utf-8 -*-
"""Level 1 Test 7, part C -- cue fix found by the manual cross-item read, after insertion:
- l1-rev-wetland-definition-peatlands: statement 3 (false) said wetlands play no part in recharging groundwater or
  controlling floods, which the Geography lakes item (part D, statement 1: lakes prevent floods and keep up a
  river's flow) undercut. It now tests whether draining a peatland keeps its carbon locked away. Key unchanged
  (Only two).
Rebuilds rev_l1_t7_c.sql from the edited module and writes rev_l1_t7_c_cuefix.sql, which rewrites that one
draft row in place."""
import contextlib, io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draft_common as d

CG = "l1-rev-wetland-definition-peatlands"
with contextlib.redirect_stdout(io.StringIO()):
    import rev_l1_t7_c  # noqa: F401  (rebuilds rev_l1_t7_c.sql)
d.ROWS[:] = [r for r in d.ROWS if r["concept_group_id"] == CG]
assert len(d.ROWS) == 1
d.write_updates("rev_l1_t7_c_cuefix.sql")
print("rev_l1_t7_c_cuefix.sql: 1 row")
