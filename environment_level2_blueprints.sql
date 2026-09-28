-- Environment's three Level-2 blueprints (build-out v2, task 2), matching
-- verify_environment_level2_split.mjs: 46 / 48 / 26 = the sectional's 120.
-- Same shape as the Polity Level-2 blueprints (config e6f68e99, theme group, part index).
insert into public.test_blueprints
  (exam_category, sequence_position, title, pattern_type, question_count, subject_scope, distribution_config_id, theme_group_id, theme_part_index)
values
  ('upsc', 1, 'Environment L2 · 1 — Ecology & Biodiversity', 'sectional', 46,
   '{"subject": "Environment & Ecology", "sub_topics": ["Fauna & Animal Behaviour", "Flora, Fungi & Forests", "Ecosystems & Ecological Processes"]}'::jsonb,
   'e6f68e99-3cc7-45de-8b7e-9de24273ff89', 'upsc-l2-environment', 1),
  ('upsc', 2, 'Environment L2 · 2 — Climate Change & Pollution', 'sectional', 48,
   '{"subject": "Environment & Ecology", "sub_topics": ["Climate Science & Mitigation", "Climate Agreements & Carbon Markets", "Pollution, Waste & Resources"]}'::jsonb,
   'e6f68e99-3cc7-45de-8b7e-9de24273ff89', 'upsc-l2-environment', 2),
  ('upsc', 3, 'Environment L2 · 3 — Policies & Conservation', 'sectional', 26,
   '{"subject": "Environment & Ecology", "sub_topics": ["Protected Areas & Wildlife Protection", "International Conventions & Organisations", "Indian Environmental Laws & Bodies"]}'::jsonb,
   'e6f68e99-3cc7-45de-8b7e-9de24273ff89', 'upsc-l2-environment', 3)
returning id, title, question_count;
