# -*- coding: utf-8 -*-
"""
Reads content-drafting/history_batch_01.json + history_batch_02.json and emits
a single Postgres INSERT (into public.questions) that:
  - imports every question as status='draft' (drafting rule; matches JSON)
  - stamps each option with a fresh uuid id at insert time via gen_random_uuid()
    (required by the exam UI's stable option-id tracking after the Aug 23 audit)
  - tags every row with 'history-<batch>' so the SME can filter in the Question
    Bank, and delete them wholesale if the pilot is aborted
  - lets Postgres mint the question id via the schema's default gen_random_uuid()

The SQL is written to scratchpad and echoed to stdout for review.
"""
import json, os, sys

CD = os.path.dirname(__file__)
OUT_DIR = os.path.abspath(os.path.join(CD, "..", "..", "AppData", "Local", "Temp", "claude",
                                        "C--Users-Pk-prepengine",
                                        "849b4650-40e3-461f-b37a-107b959298e7", "scratchpad"))

def load(name):
    with open(os.path.join(CD, name), encoding="utf-8") as f:
        return json.load(f)

b1 = load("history_batch_01.json")
b2 = load("history_batch_02.json")

rows = []
for q in b1["questions"]:
    rows.append((q, "history-batch-01"))
for q in b2["questions"]:
    rows.append((q, "history-batch-02"))

# Build one big jsonb array literal. Each element carries every column value
# except the auto-generated question id and the auto-stamped option ids.
payload = []
for q, tag in rows:
    payload.append({
        "subject": q["subject"],
        "topic": q["topic"],
        "type": q["type"],
        "difficulty": q["difficulty"],
        "body": q["body"],
        "question_data": q.get("question_data", {}),
        "options": q["options"],  # kept without ids; SQL stamps ids per option
        "marks_correct": q["marks_correct"],
        "marks_wrong": q["marks_wrong"],
        "explanation": q["explanation"],
        "concept_group_id": q["concept_group_id"],
        "source_citation": q["source_citation"],
        "batch_tag": tag,
    })

# Chunk into ~15KB payload pieces so each SQL fits comfortably in one mcp
# execute_sql call. jsonb_to_recordset works the same on a 20-row payload as
# on a 149-row one.
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
    chunk_path = os.path.join(OUT_DIR, f"bulk_insert_chunk_{idx:02d}.sql")
    with open(chunk_path, "w", encoding="utf-8") as f:
        f.write(chunk_sql)
    print(f"  chunk {idx}: {len(chunk)} rows, {len(chunk_sql)} bytes -> {chunk_path}")

print(f"\ntotal rows across chunks: {sum(len(c) for c in chunks)}")
print(f"total chunks: {len(chunks)}")

# Also write the original single-file for provenance (won't be used for exec).
json_payload = json.dumps(payload, ensure_ascii=False)

# Dollar-quoted to avoid escape hell; the tag $JN$ won't appear inside the JSON.
sql = f"""insert into public.questions
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
from jsonb_to_recordset($JN${json_payload}$JN$::jsonb) as x(
  subject text, topic text, type text, difficulty text, body text,
  question_data jsonb, options jsonb,
  marks_correct numeric, marks_wrong numeric,
  explanation text, concept_group_id text, source_citation text,
  batch_tag text
)
returning id, type, topic, difficulty, tags;
"""

os.makedirs(OUT_DIR, exist_ok=True)
out_path = os.path.join(OUT_DIR, "bulk_insert_history_batches.sql")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(sql)

print(f"rows to insert: {len(rows)}")
print(f"payload bytes: {len(json_payload)}")
print(f"sql size: {len(sql)} bytes")
print(f"wrote SQL to {out_path}")
