update public.distribution_config set
  sub_topic_weights = jsonb_set(sub_topic_weights, '{Economy}', '{"Financial Markets, Instruments & Fintech": 0.2627, "Industry, Infrastructure, Energy & Services": 0.1777, "Agriculture & Food Economy": 0.1323, "Money, Banking & Monetary Policy": 0.115, "External Sector & International Institutions": 0.0868, "Budget, Deficits & Public Debt": 0.0619, "Macro Concepts, National Income & Inflation": 0.0546, "Taxation & Fiscal Federalism": 0.0451, "Inclusive Growth, Welfare & Demography": 0.0368, "Growth, Development, Poverty & Planning": 0.0271}'::jsonb),
  question_type_weights = jsonb_set(question_type_weights, '{Economy}', '{"statement_based": 0.6154, "mcq": 0.2, "assertion_reason": 0.1538, "match_the_following": 0.0308}'::jsonb),
  difficulty_weights = jsonb_set(difficulty_weights, '{Economy}', '{"easy": 0.2, "medium": 0.6, "hard": 0.2}'::jsonb),
  updated_at = now()
where id = 'e6f68e99-3cc7-45de-8b7e-9de24273ff89' and exam_category = 'upsc'
returning sub_topic_weights->'Economy' as sub, question_type_weights->'Economy' as type, difficulty_weights->'Economy' as diff;
