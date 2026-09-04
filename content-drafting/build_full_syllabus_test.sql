-- Reusable template: assemble a "BPSC <Subject> Full Syllabus" sectional test
-- from every live, active question in that subject. Used first for History
-- (test id 40f1a3c1-ba7f-4d7e-a000-7af0bf5bb0a4, 2026-09-02) -- proven correct
-- against that run before being saved as a template.
--
-- HOW TO REUSE: edit the 4 literals in Part 1 below, then run Part 1, note the
-- returned test id, substitute it into Part 2 and Part 3, and run those in
-- order. Do NOT chain all three into one statement -- a data-modifying CTE
-- cannot see another data-modifying CTE's writes in the same statement (learned
-- the hard way while building the History test), so question_usages/times_used
-- must be separate, sequential statements after the test row is committed.
--
-- Marks are read live per-question at serve time by exam_paper() (see
-- migration 0016), NOT frozen into this test at build time -- so total_marks
-- below is a snapshot for display only; it stays correct as long as every
-- question in the subject carries the same marks_correct value at build time.

-- ============================================================
-- PART 1 -- build the test row. Edit these 4 values:
--   v_subject      the exact `subject` value to pull every active question from
--   v_title         "BPSC <Subject> Full Syllabus"
--   v_series_id     the target row in test_series (see Series & Blueprints)
--   v_duration_min  120 for a full prelims-length paper; adjust for shorter sectionals
-- ============================================================
with params as (
  select
    'History'::text                                as v_subject,
    'BPSC History Full Syllabus'::text              as v_title,
    '5c58d0f4-045f-4f51-af36-fbaf21fc40e1'::uuid    as v_series_id,
    120::int                                        as v_duration_min
),
ordered as (
  select q.id, q.marks_correct
  from public.questions q, params p
  where q.subject = p.v_subject and q.is_active
  order by
    -- History-specific chronological ordering for reviewability; harmless for
    -- subjects without a topic column that varies this way (falls through to
    -- created_at only). shuffle_questions=true means the stored order never
    -- reaches the student -- this only affects what an SME sees while reviewing.
    case q.topic when 'Ancient' then 1 when 'Medieval' then 2 when 'Modern' then 3 else 9 end,
    case q.difficulty when 'easy' then 1 when 'medium' then 2 when 'hard' then 3 else 9 end,
    q.created_at
),
agg as (
  select jsonb_agg(id::text) as ids, count(*) as n, sum(marks_correct) as total_marks from ordered
)
insert into public.tests (
  title, description, series_id, duration_min, sections,
  is_free, is_published, shuffle_questions, shuffle_options,
  total_questions, total_marks
)
select
  p.v_title,
  'Full-syllabus sectional mock covering the complete live ' || p.v_subject || ' question bank.',
  p.v_series_id,
  p.v_duration_min,
  jsonb_build_array(jsonb_build_object('id', gen_random_uuid()::text, 'name', p.v_subject, 'questionIds', agg.ids)),
  false,  -- is_free = false => "Paid students only"
  false,  -- is_published = false => draft; admin reviews & publishes manually
  true,   -- shuffle_questions
  true,   -- shuffle_options
  agg.n, agg.total_marks
from params p, agg
returning id, title, total_questions, total_marks;
-- >>> copy the returned `id` into Part 2 and Part 3 below as v_test_id, and
--     copy v_subject again into both (must match Part 1 exactly).

-- ============================================================
-- PART 2 -- record the usage ledger (run AFTER Part 1 has committed).
-- ============================================================
insert into public.question_usages (question_id, test_id, blueprint_id, theme_group_id, concept_group_id)
select id, '<v_test_id>'::uuid, null, null, concept_group_id
from public.questions
where subject = '<v_subject>' and is_active
returning question_id;

-- ============================================================
-- PART 3 -- bump times_used / last_used_* (run AFTER Part 2 has committed --
-- its subquery counts rows in question_usages, which must already be visible).
-- ============================================================
update public.questions q
set times_used = (select count(*) from public.question_usages qu where qu.question_id = q.id),
    last_used_test_id = '<v_test_id>'::uuid,
    last_used_date = now()
where q.subject = '<v_subject>' and q.is_active
returning q.id, q.times_used;

-- ============================================================
-- VERIFY -- run after Part 3, before telling anyone it's done.
-- ============================================================
-- select t.title, t.total_questions, t.total_marks, t.is_published, t.is_free,
--        t.shuffle_questions, t.shuffle_options, t.duration_min,
--        (select title from public.test_series where id = t.series_id) as series_title
-- from public.tests t where t.id = '<v_test_id>';
