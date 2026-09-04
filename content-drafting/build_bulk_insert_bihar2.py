# -*- coding: utf-8 -*-
"""
Same pattern as build_bulk_insert_bihar.py (Paper I), applied to the 5 Bihar
Special Paper II batch files. Emits chunked Postgres INSERTs into
public.questions:
  - status='draft'
  - fresh uuid per option id, stamped at insert time
  - tags = ['bihar-special2-batch-0N'] per source file -- distinct from Paper
    I's 'bihar-special-batch-0N' tags, so the two papers' rows can be told
    apart even though they share subject='Bihar-Specific'. This is what lets
    the test-builder select exactly Paper II's 150 rows later, not Paper I's
    already-live 150 too.
"""
import json, os

CD = os.path.dirname(__file__)
OUT_DIR = r"C:\Users\Pk\AppData\Local\Temp\claude\C--Users-Pk-prepengine\e3743cc4-151c-40a8-aa37-fe43d0e89c16\scratchpad"

def load(name):
    with open(os.path.join(CD, name), encoding="utf-8") as f:
        return json.load(f)

FILES = [
    ("bihar_special2_batch_01_economy.json", "bihar-special2-batch-01"),
    ("bihar_special2_batch_02_polity.json", "bihar-special2-batch-02"),
    ("bihar_special2_batch_03_recent_dev.json", "bihar-special2-batch-03"),
    ("bihar_special2_batch_04_geography.json", "bihar-special2-batch-04"),
    ("bihar_special2_batch_05_history_culture.json", "bihar-special2-batch-05"),
]

rows = []
for fname, tag in FILES:
    data = load(fname)
    for q in data["questions"]:
        rows.append((q, tag))

payload = []
for q, tag in rows:
    payload.append({
        "subject": q["subject"],
        "topic": q["topic"],
        "type": q["type"],
        "difficulty": q["difficulty"],
        "body": q["body"],
        "question_data": q.get("question_data", {}),
        "options": q["options"],
        "marks_correct": q["marks_correct"],
        "marks_wrong": q["marks_wrong"],
        "explanation": q["explanation"],
        "concept_group_id": q["concept_group_id"],
        "source_citation": q["source_citation"],
        "batch_tag": tag,
    })

CHUNK_SIZE = 25
chunks = [payload[i:i+CHUNK_SIZE] for i in range(0, len(payload), CHUNK_SIZE)]

os.makedirs(OUT_DIR, exist_ok=True)
for idx, chunk in enumerate(chunks, start=1):
    json_chunk = json.dumps(chunk, ensure_ascii=False)
    chunk_sql = f"""insert into public.questions
  (subject, topic, type, difficulty, body, question_data, options,
   marks_correct, marks_wrong, explanation, concept_group_id, source_citation,
   status, tags, is_active)
select
  x.subject, x.topic, x.type, x.difficulty, x.body, x.question_data,
  (
    select jsonb_agg(
      jsonb_set(opt, '{{id}}', to_jsonb(gen_random_uuid()::text))
    )
    from jsonb_array_elements(x.options) as opt
  ) as options_with_ids,
  x.marks_correct, x.marks_wrong, x.explanation, x.concept_group_id, x.source_citation,
  'draft'::text as status,
  ARRAY[x.batch_tag]::text[] as tags,
  true as is_active
from jsonb_to_recordset($JN${json_chunk}$JN$::jsonb) as x(
  subject text, topic text, type text, difficulty text, body text,
  question_data jsonb, options jsonb,
  marks_correct numeric, marks_wrong numeric,
  explanation text, concept_group_id text, source_citation text,
  batch_tag text
)
returning id;
"""
    chunk_path = os.path.join(OUT_DIR, f"bihar2_bulk_insert_chunk_{idx:02d}.sql")
    with open(chunk_path, "w", encoding="utf-8") as f:
        f.write(chunk_sql)
    print(f"  chunk {idx}: {len(chunk)} rows, {len(chunk_sql)} bytes -> {chunk_path}")

print(f"\ntotal rows across chunks: {sum(len(c) for c in chunks)}")
print(f"total chunks: {len(chunks)}")
