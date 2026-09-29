update public.distribution_config set
  sub_topic_weights = jsonb_set(sub_topic_weights, '{"Science & Technology"}', '{"IT, Communication & Emerging Technologies": 0.2203, "Energy & Environmental Technology": 0.1786, "Chemistry & Materials": 0.1412, "Astronomy & Earth Science": 0.1281, "Defence, Aerospace & Security Technology": 0.1008, "Physics & Everyday Science": 0.0853, "Biology, Health & Biotechnology": 0.0846, "Space Technology & Missions": 0.0611}'::jsonb),
  question_type_weights = jsonb_set(question_type_weights, '{"Science & Technology"}', '{"statement_based": 0.6735, "mcq": 0.2245, "assertion_reason": 0.102}'::jsonb),
  difficulty_weights = jsonb_set(difficulty_weights, '{"Science & Technology"}', '{"easy": 0.2041, "medium": 0.6122, "hard": 0.1837}'::jsonb),
  updated_at = now()
where id = 'e6f68e99-3cc7-45de-8b7e-9de24273ff89' and exam_category = 'upsc'
returning sub_topic_weights->'Science & Technology' as sub, question_type_weights->'Science & Technology' as type, difficulty_weights->'Science & Technology' as diff;
