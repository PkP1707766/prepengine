-- UPSC Prelims 2027, Level 2 (Sectional Mastery) at the real format: every GS sectional
-- is a full GS Paper I (100 questions, 200 marks, 2 hours), numbered in the order the
-- series runs (upsc_level2_targets.mjs, docs/upsc-test-series-plan.md).
--
-- 1. One Level-2 series for UPSC (price stays at the column default 0 until pricing is set
--    under Bundles & Pricing; students never see a series row, only its tests' title).
-- 2. The eleven existing Level-2 blueprints move to 100 questions, student-facing titles,
--    the series, their test numbers and fresh theme groups. Fresh theme groups matter: the
--    generator bars a sibling from reusing a concept already used under the same theme
--    group, and the old 12-48 question drafts were saved under the old ones.
-- 3. Geography's three Level-2 blueprints are added the same way.
-- The old draft tests themselves are left untouched (unpublished, and now blocked from
-- publishing because they are not a standard UPSC length).
with s as (
  insert into public.test_series (title, description, exam_category)
  values ('UPSC Prelims 2027 — Level 2: Sectional Mastery',
          'Subject-by-subject GS papers on the UPSC pattern: 21 sectional GS Paper I tests (100 questions, 200 marks, 2 hours each) and 7 CSAT Paper II tests (80 questions, 2 hours).',
          'upsc')
  returning id
), upd as (
  update public.test_blueprints b set
    title = v.title, question_count = 100, series_id = (select id from s),
    sequence_position = v.no, theme_group_id = v.theme, theme_part_index = v.part, updated_at = now()
  from (values
    ('4d197c4b-34de-4f4e-a1d4-a6f89373615c'::uuid, 1, 'Level 2 · Test 1 — Polity 1: Constitutional Framework & Rights', 'upsc27-l2-polity', 1),
    ('d537a884-e9d4-4a5c-8b8f-5551b5b7de90'::uuid, 2, 'Level 2 · Test 2 — Polity 2: Parliament & Executive', 'upsc27-l2-polity', 2),
    ('98d4de60-907b-4183-a6fa-e50884157d3f'::uuid, 3, 'Level 2 · Test 3 — Polity 3: Judiciary, Bodies, Elections & Laws', 'upsc27-l2-polity', 3),
    ('3fca9f81-6358-4450-a511-4972efcd00f9'::uuid, 4, 'Level 2 · Test 4 — Polity 4: Federalism, Local Government & Governance', 'upsc27-l2-polity', 4),
    ('2beac8f6-9a2a-42cd-a0e9-90b5d6bbc2c7'::uuid, 5, 'Level 2 · Test 5 — History 1: Modern India', 'upsc27-l2-history', 1),
    ('4063e542-f332-451b-8522-0212286f84e5'::uuid, 6, 'Level 2 · Test 6 — History 2: Ancient India', 'upsc27-l2-history', 2),
    ('6a6fcb43-f934-4f6a-994f-990ba032ffac'::uuid, 7, 'Level 2 · Test 7 — History 3: Medieval India', 'upsc27-l2-history', 3),
    ('c8c1f4f7-b7cd-48ad-be6b-f8afa8d85e90'::uuid, 8, 'Level 2 · Test 8 — History 4: Art & Culture', 'upsc27-l2-history', 4),
    ('5338f30b-0809-4320-949b-de58ebb69c72'::uuid, 9, 'Level 2 · Test 9 — Environment 1: Ecology & Biodiversity', 'upsc27-l2-environment', 1),
    ('fa894e46-bedd-4d8b-9f31-7671ea84c05d'::uuid, 10, 'Level 2 · Test 10 — Environment 2: Climate Change & Pollution', 'upsc27-l2-environment', 2),
    ('661e7256-d378-4bf6-b8fa-8ad2a5f853cb'::uuid, 11, 'Level 2 · Test 11 — Environment 3: Policies & Conservation', 'upsc27-l2-environment', 3)
  ) as v(id, no, title, theme, part)
  where b.id = v.id and b.exam_category = 'upsc'
  returning b.id
), geo as (
  insert into public.test_blueprints
    (exam_category, series_id, sequence_position, title, pattern_type, question_count, subject_scope, distribution_config_id, theme_group_id, theme_part_index)
  select 'upsc', (select id from s), v.no, v.title, 'sectional', 100, v.scope::jsonb, 'e6f68e99-3cc7-45de-8b7e-9de24273ff89', 'upsc27-l2-geography', v.part
  from (values
    (12, 'Level 2 · Test 12 — Geography 1: World Physical Geography', '{"subject": "Geography", "sub_topics": ["Geomorphology & Earth''s Interior", "Climatology & Biomes", "Oceanography & Hydrosphere", "World Regions, Water Bodies & Places"]}', 1),
    (13, 'Level 2 · Test 13 — Geography 2: Indian Physical Geography', '{"subject": "Geography", "sub_topics": ["Indian Rivers, Lakes & Wetlands", "Indian Physiography, Climate & Regions"]}', 2),
    (14, 'Level 2 · Test 14 — Geography 3: Human & Economic Geography', '{"subject": "Geography", "sub_topics": ["Resources: Minerals, Energy & Agriculture", "Transport, Ports & Human Geography"]}', 3)
  ) as v(no, title, scope, part)
  returning id
)
select (select id from s) as series_id, (select count(*) from upd) as blueprints_updated, (select count(*) from geo) as geography_added;
