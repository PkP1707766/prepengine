# Replace one builder block (S(/M( ... "<concept id>", ...)) in a content module with new text.
import io
import os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"

def swap(mod, cg, new):
    p = D + mod
    s = io.open(p, encoding="utf-8").read()
    i = s.index('"' + cg + '"')
    start = max(s.rfind("\nS(", 0, i), s.rfind("\nM(", 0, i)) + 1
    end = s.index('")\n', i) + 2
    s = s[:start] + new.strip("\n") + s[end:]
    io.open(p, "w", encoding="utf-8").write(s)
    print("swapped", cg)

