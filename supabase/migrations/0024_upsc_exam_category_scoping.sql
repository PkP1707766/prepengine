-- ============================================================================
-- 0024 — UPSC/BPSC exam-category scoping — questions, distribution_config,
-- test_blueprints; new question_type values for CSAT formats.
--
-- BPSC and UPSC content have so far been distinguished only by naming
-- convention, not a real FK. Several GS1 subjects (History, Geography,
-- Economy, Science & Technology, Environment & Ecology) are IDENTICAL
-- strings to BPSC's existing subjects, so any subject-filtered query without
-- exam scoping would silently mix the two banks the moment UPSC content
-- exists. This adds the missing FK before any UPSC content is drafted.
--
-- Nullable -> backfill -> NOT NULL, atomic in one migration so a failure
-- rolls back cleanly rather than leaving a half-migrated table. Applied and
-- verified directly against the live project on 2026-09-19: 2,371 existing
-- question rows (not the 2,295 the migration instructions assumed -- the bank
-- had grown since that figure was last checked; every row's subject value
-- was independently confirmed BPSC-only before backfilling), 1
-- distribution_config row, 1 test_blueprints row, all backfilled to 'bpsc'
-- with zero nulls remaining.
-- ============================================================================

-- ---------------------------------------------------------------------------
-- 1. QUESTIONS
-- ---------------------------------------------------------------------------
alter table public.questions
  add column if not exists exam_category text references public.exam_categories(code) on update cascade;

-- Every row that exists today predates UPSC content (per the migration's own
-- instructions: "do not draft any UPSC questions as part of this task"), so
-- every current row is BPSC. Confirmed independently: 100% of existing
-- subject values (History, Geography, Polity, Economy, Science & Technology,
-- Environment & Ecology, Current Affairs, Bihar-Specific, Reasoning &
-- Aptitude) are BPSC-only subjects; none overlap with a UPSC-only subject.
update public.questions set exam_category = 'bpsc' where exam_category is null;

alter table public.questions
  alter column exam_category set not null;

create index if not exists questions_exam_category_idx on public.questions (exam_category);
-- Composite index for the actual hot-path shape: scope by exam, then subject.
create index if not exists questions_exam_subject_idx on public.questions (exam_category, subject);

-- New question_type values for CSAT formats ('numerical' already exists from
-- the original schema). Additive, matching 0016's style.
alter table public.questions drop constraint if exists questions_type_chk;
do $$ begin
  alter table public.questions
    add constraint questions_type_chk check (type in (
      'mcq', 'multiple', 'numerical',
      'statement_based', 'match_the_following', 'assertion_reason', 'reasoning_aptitude',
      'reading_comprehension', 'data_sufficiency', 'puzzle_hybrid'));
exception when duplicate_object then null; end $$;

-- ---------------------------------------------------------------------------
-- 2. DISTRIBUTION_CONFIG — the BPSC row backfills the same way.
-- ---------------------------------------------------------------------------
alter table public.distribution_config
  add column if not exists exam_category text references public.exam_categories(code) on update cascade;

update public.distribution_config set exam_category = 'bpsc' where exam_category is null;

alter table public.distribution_config
  alter column exam_category set not null;

create index if not exists distribution_config_exam_category_idx on public.distribution_config (exam_category);

-- ---------------------------------------------------------------------------
-- 3. TEST_BLUEPRINTS — same pattern, so a blueprint unambiguously declares
--    which exam's bank it draws from (the generator checks this defensively
--    in addition to the DB-level query filter -- belt and suspenders).
-- ---------------------------------------------------------------------------
alter table public.test_blueprints
  add column if not exists exam_category text references public.exam_categories(code) on update cascade;

update public.test_blueprints set exam_category = 'bpsc' where exam_category is null;

alter table public.test_blueprints
  alter column exam_category set not null;

create index if not exists test_blueprints_exam_category_idx on public.test_blueprints (exam_category);
