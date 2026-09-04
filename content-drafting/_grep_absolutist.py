import json, re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
files = sys.argv[1:]
WORDS = {'every','all','entirely','ever','always','never','only','none'}
for f in files:
    data = json.load(open(f, encoding='utf-8'))
    for q in data['questions']:
        for i, o in enumerate(q['options']):
            words = re.findall(r"[a-zA-Z']+", o['body'].lower())
            hits = set(words) & WORDS
            if hits:
                print(f, q['batch_ref'], 'abcd'[i], o['isCorrect'], hits, '::', o['body'])
