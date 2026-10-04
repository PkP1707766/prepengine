# -*- coding: utf-8 -*-
"""Build the depth-standard rewrite of a batch file (docs/upsc-question-design-standard.md §6).

  python _make_v2.py <batch.py> <spec.py>

<spec.py> defines:
  OUT     -- the new file name, e.g. "gs_l2_t21_history_v2.py"
  HEADER  -- the new module docstring (what changed and why)
  CRAFT   -- {concept_group_id: craft} for EVERY row of the batch
  NEW     -- {concept_group_id: source of the replacement builder call}, for rewritten rows only
  REPLACES (optional) -- {new concept id: old concept id} when a rewrite changes the concept

The rewrite keeps every row's concept id, so write_updates() overwrites the same draft rows. Kept rows
get their craft tag; rewritten rows are spliced in whole. The new file sets REQUIRE_CRAFT and writes
<OUT>.sql as in-place UPDATEs."""
import re, runpy, sys

src, spec = sys.argv[1], runpy.run_path(sys.argv[2])
s = open(src, encoding="utf-8").read()
lines = s.split("\n")

def call_span(cg):
    """(start, end) line indexes of the builder call that ends with this concept id."""
    hit = [i for i, l in enumerate(lines) if re.search(r'^\s*"' + re.escape(cg) + r'"\s*[,)]', l)]
    assert len(hit) == 1, f"{cg}: {len(hit)} matches"
    end = hit[0]
    while not lines[end].rstrip().endswith(")"):
        end += 1
    start = max(i for i in range(hit[0] + 1) if re.match(r"^[SMPAC]\(", lines[i]))
    return start, end

ids = [m for m in re.findall(r'^\s*"([a-z0-9][a-z0-9-]+)"\s*[,)]', s, re.M)]
missing = set(ids) - set(spec["CRAFT"])
assert not missing, f"no craft for {sorted(missing)}"
for cg in sorted(set(spec["NEW"]) - set(ids)):
    raise SystemExit(f"{cg} is not a row of {src}")

# rewritten rows first (spans move as lines change, so recompute each time)
for cg, block in spec["NEW"].items():
    a, b = call_span(cg)
    lines[a:b + 1] = block.split("\n")
# craft on kept rows: append to the end of the call
for cg, craft in spec["CRAFT"].items():
    if cg in spec["NEW"]:
        continue
    a, b = call_span(cg)
    last = lines[b].rstrip()
    assert last.endswith(")") and "craft=" not in "\n".join(lines[a:b + 1]), cg
    lines[b] = last[:-1] + f', craft="{craft}")'

out = "\n".join(lines)
out = re.sub(r'^"""[\s\S]*?"""\n', '"""' + spec["HEADER"].strip() + '"""\n', out.split("\n", 1)[1], count=1)
out = "# -*- coding: utf-8 -*-\n" + out
out = re.sub(r"from draft_common import ([^\n]*)\bwrite\b", lambda m: "from draft_common import " + m.group(1) + "write_updates, CODE", out, count=1)
out = re.sub(r'(d\.SUBJECT = "[^"]+"\n)', r"\1d.REQUIRE_CRAFT = True\n", out, count=1)
rep = spec.get("REPLACES") or {}
args = f'"{spec["OUT"].replace(".py", ".sql")}"' + (f", replaces={rep!r}" if rep else "")
out = re.sub(r'    write\("[^"]+"\)', f"    write_updates({args})", out, count=1)
open(spec["OUT"], "w", encoding="utf-8").write(out)
print("wrote", spec["OUT"], "--", len(spec["NEW"]), "rewritten,", len(spec["CRAFT"]) - len(spec["NEW"]), "tagged")
