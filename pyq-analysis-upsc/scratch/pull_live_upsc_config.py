# -*- coding: utf-8 -*-
"""Re-pull live_upsc_config.json from the live distribution_config row e6f68e99, in the shape the
gap-report scripts read (name, subjectWeights, subTopicWeights, difficultyWeights, questionTypeWeights).
Run after applying a <subject>_weights_update.sql, piping the signed-in CLI's JSON output in:
  supabase db query --linked -o json "select name, subject_weights, sub_topic_weights, difficulty_weights,
    question_type_weights from public.distribution_config where id = 'e6f68e99-3cc7-45de-8b7e-9de24273ff89'"
    | python pull_live_upsc_config.py
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "live_upsc_config.json")


def main():
    row = json.loads(sys.stdin.buffer.read().decode("utf-8"))["rows"][0]
    cfg = {"name": row["name"], "subjectWeights": row["subject_weights"], "subTopicWeights": row["sub_topic_weights"],
           "difficultyWeights": row["difficulty_weights"], "questionTypeWeights": row["question_type_weights"]}
    open(OUT, "w", encoding="utf-8").write(json.dumps(cfg, ensure_ascii=False))
    print("wrote", os.path.normpath(OUT), "--", ", ".join(f"{k}: {len(v)}" for k, v in cfg["subTopicWeights"].items()))


if __name__ == "__main__":
    main()
