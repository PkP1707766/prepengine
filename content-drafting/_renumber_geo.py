# -*- coding: utf-8 -*-
import json, re

path = "bihar_special2_batch_04_geography.json"
raw = open(path, encoding="utf-8").read()

# bs2-401g..bs2-448g -> bs2-501..bs2-548 (drop trailing 'g', shift numeric base to 500s
# to avoid colliding with Polity's bs2-401..bs2-405)
def repl(m):
    n = int(m.group(1))
    return f"bs2-{n + 100}"

raw2 = re.sub(r"bs2-4(\d{2})g", lambda m: f"bs2-5{m.group(1)}", raw)
remaining = re.findall(r"bs2-4\d{2}g", raw2)
assert not remaining, f"still has: {remaining}"
open(path, "w", encoding="utf-8").write(raw2)
print("renumbered, sample check:", re.findall(r"bs2-5\d{2}", raw2)[:5])

