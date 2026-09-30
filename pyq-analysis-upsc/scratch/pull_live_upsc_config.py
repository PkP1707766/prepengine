# -*- coding: utf-8 -*-
"""Re-pull live_upsc_config.json from the live distribution_config row e6f68e99, in the shape the
gap-report scripts read (name, subjectWeights, subTopicWeights, difficultyWeights, questionTypeWeights).
Run after applying a <subject>_weights_update.sql, piping the signed-in CLI's JSON output in:
  supabase db query --linked -o json "select name, subject_weights::text subject_weights,
    sub_topic_weights::text sub_topic_weights, difficulty_weights::text difficulty_weights,
    question_type_weights::text question_type_weights from public.distribution_config
    where id = 'e6f68e99-3cc7-45de-8b7e-9de24273ff89'" | python pull_live_upsc_config.py

Select the weight columns ::text. The CLI is a Go program and re-encodes jsonb objects with their keys sorted
alphabetically, while the app reads them through PostgREST in jsonb's own order (shorter keys first). Key order
matters: buildCells breaks rounding ties in key order, and History's Painting, Iconography and Architecture share
one weight, so an alphabetical snapshot shifts one Test 8 cell and makes the gap report disagree with the paper
the app would build. Text columns keep the database order; plain jsonb columns are still accepted.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "live_upsc_config.json")


def main():
    row = json.loads(sys.stdin.buffer.read().decode("utf-8"))["rows"][0]
    for k in ("subject_weights", "sub_topic_weights", "difficulty_weights", "question_type_weights"):
        if isinstance(row[k], str):
            row[k] = json.loads(row[k])
    cfg = {"name": row["name"], "subjectWeights": row["subject_weights"], "subTopicWeights": row["sub_topic_weights"],
           "difficultyWeights": row["difficulty_weights"], "questionTypeWeights": row["question_type_weights"]}
    open(OUT, "w", encoding="utf-8").write(json.dumps(cfg, ensure_ascii=False))
    print("wrote", os.path.normpath(OUT), "--", ", ".join(f"{k}: {len(v)}" for k, v in cfg["subTopicWeights"].items()))


if __name__ == "__main__":
    main()
