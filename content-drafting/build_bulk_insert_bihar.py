# -*- coding: utf-8 -*-
"""
Same pattern as build_bulk_insert.py (History), applied to the 5 Bihar Special
Paper I batch files. Emits chunked Postgres INSERTs into public.questions:
  - status='draft'
  - fresh uuid per option id, stamped at insert time
  - tags = ['bihar-special-batch-0N'] per source file, for SME filtering /
    wholesale rollback if needed
"""
import json, os

CD = os.path.dirname(__file__)
OUT_DIR = os.path.abspath(os.path.join(CD, "..", "..", "AppData", "Local", "Temp", "claude",
                                        "C--Users-Pk-prepengine",
                                        "849b4650-40e3-461f-b37a-107b959298e7", "scratchpad"))

def load(name):
    with open(os.path.join(CD, name), encoding="utf-8") as f:
        return json.load(f)

FILES = [
    ("bihar_special_batch_01_history_culture.json", "bihar-special-batch-01"),
    ("bihar_special_batch_02_geography.json", "bihar-special-batch-02"),
    ("bihar_special_batch_03_economy.json", "bihar-special-batch-03"),
    ("bihar_special_batch_04_polity.json", "bihar-special-batch-04"),
    ("bihar_special_batch_05_recent_developments.json", "bihar-special-batch-05"),
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
    chunk_path = os.path.join(OUT_DIR, f"bihar_bulk_insert_chunk_{idx:02d}.sql")
    with open(chunk_path, "w", encoding="utf-8") as f:
        f.write(chunk_sql)
    print(f"  chunk {idx}: {len(chunk)} rows, {len(chunk_sql)} bytes -> {chunk_path}")

print(f"\ntotal rows across chunks: {sum(len(c) for c in chunks)}")
print(f"total chunks: {len(chunks)}")
