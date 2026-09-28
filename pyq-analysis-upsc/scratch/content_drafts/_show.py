import json, sys
rows = json.load(open('_kept_en_rows.json', encoding='utf-8'))
subj, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
rs = [r for r in rows if r['subject'] == subj][a:b]
for r in rs:
    qd = r['qd'] or {}
    print(f"## {r['id']} [{r['type']}]")
    print("B:", r['body'])
    for k in ('statements', 'list_1', 'list_2'):
        if k in qd: print(f"{k}:", " || ".join(qd[k]))
    for k in ('assertion', 'reason', 'reason_2'):
        if k in qd: print(f"{k}:", qd[k])
    if qd.get('closing') and qd['closing'] not in ('How many of the above statements are correct?', 'Which of the statements given above is/are correct?', 'How many of the pairs given above are correctly matched?', 'Which one of the following is correct in respect of the above statements?'):
        print("closing:", qd['closing'])
    if r['opts']: print("O:", " || ".join(f"{k}) {v}" for k, v in sorted(r['opts'].items())))
    print("E:", r['explanation'])
