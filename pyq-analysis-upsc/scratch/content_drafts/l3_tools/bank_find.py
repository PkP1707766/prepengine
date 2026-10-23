# Usage: python bank_find.py "<regex>;<regex>;..."
# Case-insensitive search of the local bank dump (stems, statements, options AND explanations).
import io, json, os, re, sys
S = os.path.dirname(os.path.abspath(__file__))
b = json.load(io.open(os.path.join(S, '_data', 'bank_dump.json'), encoding='utf-8'))
terms = sys.argv[-1].split(';')
for t in terms:
    rx = re.compile(t, re.I)
    h = [r['cg'] for r in b if rx.search(r['txt'])]
    print(f"{t[:34]:34s} {len(h):3d} {h[:5]}")
