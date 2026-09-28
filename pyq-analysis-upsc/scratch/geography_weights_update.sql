update public.distribution_config set
  sub_topic_weights = jsonb_set(sub_topic_weights, '{Geography}', '{"World Regions, Water Bodies & Places": 0.2099, "Climatology & Biomes": 0.2004, "Indian Physiography, Climate & Regions": 0.1666, "Indian Rivers, Lakes & Wetlands": 0.1401, "Geomorphology & Earth''s Interior": 0.1099, "Resources: Minerals, Energy & Agriculture": 0.0681, "Transport, Ports & Human Geography": 0.0677, "Oceanography & Hydrosphere": 0.0373}'::jsonb),
  question_type_weights = jsonb_set(question_type_weights, '{Geography}', '{"statement_based": 0.5111, "mcq": 0.2444, "assertion_reason": 0.1778, "match_the_following": 0.0667}'::jsonb),
  difficulty_weights = jsonb_set(difficulty_weights, '{Geography}', '{"easy": 0.1778, "medium": 0.6, "hard": 0.2222}'::jsonb),
  updated_at = now()
where id = 'e6f68e99-3cc7-45de-8b7e-9de24273ff89' and exam_category = 'upsc'
returning sub_topic_weights->'Geography' as sub, question_type_weights->'Geography' as type, difficulty_weights->'Geography' as diff;
