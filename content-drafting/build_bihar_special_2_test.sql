-- Bihar Special II test-build, adapted from build_full_syllabus_test.sql.
--
-- DIFFERENCE FROM THE GENERIC TEMPLATE: that template selects by
-- `subject = v_subject`, which worked for Paper I only because Paper I's 150
-- rows were the ONLY subject='Bihar-Specific' rows in existence at the time.
-- Paper I's 150 are now already live and published as their own test, so
-- selecting on subject alone here would double up Paper I's rows into this
-- test too. Instead this selects by the batch tags stamped on Paper II's rows
-- at insert time (build_bulk_insert_bihar2.py), which cleanly isolates
-- exactly Paper II's 150 regardless of what else shares the same subject.
--
-- Run PART 0 first to confirm exactly 150 rows match before building anything.
-- Same three-separate-statements rule as the generic template applies (a
-- data-modifying CTE can't see another data-modifying CTE's writes in the
-- same statement) -- do not chain Parts 1/2/3 together.

-- ============================================================
-- PART 0 -- pre-flight check. Run this FIRST; must return exactly 150.
-- ============================================================
-- select count(*) from public.questions
-- where 'bihar-special2-batch-01' = any(tags)
--    or 'bihar-special2-batch-02' = any(tags)
--    or 'bihar-special2-batch-03' = any(tags)
--    or 'bihar-special2-batch-04' = any(tags)
--    or 'bihar-special2-batch-05' = any(tags);

-- ============================================================
-- PART 1 -- build the test row.
-- ============================================================
with params as (
  select
    'BPSC Bihar Special II'::text                  as v_title,
    '5c58d0f4-045f-4f51-af36-fbaf21fc40e1'::uuid    as v_series_id,
    120::int                                        as v_duration_min,
    array['bihar-special2-batch-01','bihar-special2-batch-02',
          'bihar-special2-batch-03','bihar-special2-batch-04',
          'bihar-special2-batch-05']::text[]        as v_tags
),
ordered as (
  select q.id, q.marks_correct
  from public.questions q, params p
  where q.tags && p.v_tags and q.is_active
  order by
    -- reviewability ordering only; shuffle_questions=true means students
    -- never see this stored order.
    case q.topic
      when 'History & Culture' then 1
      when 'Geography' then 2
      when 'Economy' then 3
      when 'Recent Developments' then 4
      when 'Polity & Governance' then 5
      else 9
    end,
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
  'Third full-length mock in the BPSC CCE Full Mock Series, covering Bihar-Specific content across History & Culture, Geography, Economy, Recent Developments and Polity & Governance.',
  p.v_series_id,
  p.v_duration_min,
  jsonb_build_array(jsonb_build_object('id', gen_random_uuid()::text, 'name', 'Bihar-Specific', 'questionIds', agg.ids)),
  false,  -- is_free = false => "Paid students only"
  false,  -- is_published = false => draft; admin reviews & publishes manually
  true,   -- shuffle_questions
  true,   -- shuffle_options
  agg.n, agg.total_marks
from params p, agg
returning id, title, total_questions, total_marks;
-- >>> copy the returned `id` into Part 2 and Part 3 below as v_test_id.

-- ============================================================
-- PART 2 -- record the usage ledger (run AFTER Part 1 has committed).
-- ============================================================
insert into public.question_usages (question_id, test_id, blueprint_id, theme_group_id, concept_group_id)
select id, '<v_test_id>'::uuid, null, null, concept_group_id
from public.questions
where ('bihar-special2-batch-01' = any(tags) or 'bihar-special2-batch-02' = any(tags)
    or 'bihar-special2-batch-03' = any(tags) or 'bihar-special2-batch-04' = any(tags)
    or 'bihar-special2-batch-05' = any(tags))
  and is_active
returning question_id;

-- ============================================================
-- PART 3 -- bump times_used / last_used_* (run AFTER Part 2 has committed).
-- ============================================================
update public.questions q
set times_used = (select count(*) from public.question_usages qu where qu.question_id = q.id),
    last_used_test_id = '<v_test_id>'::uuid,
    last_used_date = now()
where ('bihar-special2-batch-01' = any(q.tags) or 'bihar-special2-batch-02' = any(q.tags)
    or 'bihar-special2-batch-03' = any(q.tags) or 'bihar-special2-batch-04' = any(q.tags)
    or 'bihar-special2-batch-05' = any(q.tags))
  and q.is_active
returning q.id, q.times_used;

-- ============================================================
-- VERIFY -- run after Part 3, before telling anyone it's done.
-- ============================================================
-- select t.title, t.total_questions, t.total_marks, t.is_published, t.is_free,
--        t.shuffle_questions, t.shuffle_options, t.duration_min,
--        (select title from public.test_series where id = t.series_id) as series_title
-- from public.tests t where t.id = '<v_test_id>';
