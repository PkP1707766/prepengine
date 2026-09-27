-- ============================================================================
-- 0025 — exam-category scoping for tests and test series, plus database-level
-- guards against mixing exams inside a test, a series or a bundle.
--
-- 0024 scoped questions, distribution_config and test_blueprints, but tests
-- and test_series still had no exam at all, so the admin's UPSC workspace
-- listed and counted all 30 tests (26 of them BPSC), the blueprint and test
-- editors offered the BPSC series inside UPSC, and a bundle's test picker
-- offered every exam's tests. Found on the live admin on 2026-09-27.
--
-- Backfill facts, queried live immediately before writing this migration:
--   * 26 tests have no blueprint and contain only exam_category='bpsc'
--     questions; 4 tests (the History Level-2 drafts) come from UPSC
--     blueprints and contain only 'upsc' questions; 0 tests reference a
--     missing question; no test mixes exams.
--   * 1 series ('BPSC CCE Full Mock Series'), whose 26 tests are all BPSC.
--   * plan_tests: bpsc-2026 -> 25 BPSC tests; every other plan has none.
-- ============================================================================

-- ---------------------------------------------------------------------------
-- 1. TESTS.exam_category — from the blueprint, else from the questions.
-- ---------------------------------------------------------------------------
alter table public.tests
  add column if not exists exam_category text references public.exam_categories(code) on update cascade;

update public.tests t
   set exam_category = b.exam_category
  from public.test_blueprints b
 where b.id = t.blueprint_id and t.exam_category is null;

update public.tests t
   set exam_category = x.exam_category
  from (
    select t2.id, min(q.exam_category) as exam_category
      from public.tests t2,
           jsonb_array_elements(coalesce(t2.sections, '[]'::jsonb)) s,
           jsonb_array_elements_text(coalesce(s->'questionIds', '[]'::jsonb)) qid
      join public.questions q on q.id = qid::uuid
     group by t2.id
  ) x
 where x.id = t.id and t.exam_category is null;

-- ---------------------------------------------------------------------------
-- 2. TEST_SERIES.exam_category — from its tests. (There is no series editor
--    in the admin; series are created in SQL, so NOT NULL breaks no writer.)
-- ---------------------------------------------------------------------------
alter table public.test_series
  add column if not exists exam_category text references public.exam_categories(code) on update cascade;

update public.test_series s
   set exam_category = x.exam_category
  from (select series_id, min(exam_category) as exam_category from public.tests where series_id is not null group by series_id) x
 where x.series_id = s.id and s.exam_category is null;

alter table public.test_series alter column exam_category set not null;
create index if not exists test_series_exam_category_idx on public.test_series (exam_category);

-- ---------------------------------------------------------------------------
-- 3. Guard trigger on tests: fill a missing exam (blueprint -> series ->
--    questions), then refuse any test whose questions or series belong to
--    another exam. Filling first keeps older callers that do not send
--    exam_category (commit_generated_test, an admin tab loaded before this
--    deploy) working, while the check makes mixing impossible at the source.
-- ---------------------------------------------------------------------------
create or replace function public.tests_exam_scope_guard()
returns trigger
language plpgsql
as $fn$
declare
  v_other int;
  v_series_exam text;
begin
  if new.exam_category is null and new.blueprint_id is not null then
    select exam_category into new.exam_category from public.test_blueprints where id = new.blueprint_id;
  end if;
  if new.exam_category is null and new.series_id is not null then
    select exam_category into new.exam_category from public.test_series where id = new.series_id;
  end if;
  if new.exam_category is null then
    select min(q.exam_category) into new.exam_category
      from jsonb_array_elements(coalesce(new.sections, '[]'::jsonb)) s,
           jsonb_array_elements_text(coalesce(s->'questionIds', '[]'::jsonb)) qid
      join public.questions q on q.id = qid::uuid;
  end if;
  if new.exam_category is null then
    raise exception 'A test must belong to an exam (exam_category) — none given and none could be inferred.';
  end if;

  select count(*) into v_other
    from jsonb_array_elements(coalesce(new.sections, '[]'::jsonb)) s,
         jsonb_array_elements_text(coalesce(s->'questionIds', '[]'::jsonb)) qid
    join public.questions q on q.id = qid::uuid
   where q.exam_category <> new.exam_category;
  if v_other > 0 then
    raise exception 'This % test contains % question(s) from another exam; a test cannot mix exams.', upper(new.exam_category), v_other;
  end if;

  if new.series_id is not null then
    select exam_category into v_series_exam from public.test_series where id = new.series_id;
    if v_series_exam is distinct from new.exam_category then
      raise exception 'Series exam (%) and test exam (%) differ; a test can only join a series of its own exam.', upper(coalesce(v_series_exam, '?')), upper(new.exam_category);
    end if;
  end if;
  return new;
end;
$fn$;

drop trigger if exists trg_tests_exam_scope_guard on public.tests;
create trigger trg_tests_exam_scope_guard
  before insert or update of exam_category, sections, series_id, blueprint_id on public.tests
  for each row execute function public.tests_exam_scope_guard();

alter table public.tests alter column exam_category set not null;
create index if not exists tests_exam_category_idx on public.tests (exam_category);

-- ---------------------------------------------------------------------------
-- 4. Guard trigger on plan_tests: a bundle only unlocks tests of its own exam.
-- ---------------------------------------------------------------------------
create or replace function public.plan_tests_exam_scope_guard()
returns trigger
language plpgsql
as $fn$
declare
  v_plan_exam text;
  v_test_exam text;
begin
  select exam_category into v_plan_exam from public.plans where code = new.plan_code;
  select exam_category into v_test_exam from public.tests where id = new.test_id;
  if v_plan_exam is distinct from v_test_exam then
    raise exception 'A % bundle cannot include a % test.', upper(coalesce(v_plan_exam, '?')), upper(coalesce(v_test_exam, '?'));
  end if;
  return new;
end;
$fn$;

drop trigger if exists trg_plan_tests_exam_scope_guard on public.plan_tests;
create trigger trg_plan_tests_exam_scope_guard
  before insert or update on public.plan_tests
  for each row execute function public.plan_tests_exam_scope_guard();
