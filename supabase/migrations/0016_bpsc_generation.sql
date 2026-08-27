-- ============================================================================
-- 0016 — BPSC question-bank & test-generation engine (Milestone 1)
--
-- Layers an auto-generation subsystem onto the existing hand-built model
-- WITHOUT disturbing the exam engine:
--
--  * Paper ordering stays in tests.sections[].questionIds — array order IS the
--    spec's `position`, and exam_paper() already preserves it with
--    `with ordinality`. No junction table, so ExamApp / submit-attempt / the
--    review are untouched.
--  * The 5 BPSC formats reuse the existing `type` column and single-correct
--    scoring. Only the stem shape (question_data) and rendering differ, so
--    submit-attempt needs no new branch.
--  * A separate question_usages table carries cross-test AND cross-theme-group
--    concept dedup plus usage counters, decoupled from the paper.
--
-- Additive and idempotent throughout, matching the house style of 0001–0015.
-- ============================================================================

-- ---------------------------------------------------------------------------
-- 1. QUESTIONS — tagging, provenance, usage and recalibration columns
-- ---------------------------------------------------------------------------
alter table public.questions
  add column if not exists question_data     jsonb   not null default '{}'::jsonb,
  -- text, not uuid: this is hand-tagged by a reviewer, so a memorable slug
  -- ("bihar-first-governor") reuses far more reliably than a generated uuid,
  -- and equality is all dedup needs. Same rationale that took subjects off an
  -- enum onto free text.
  add column if not exists concept_group_id  text,
  add column if not exists source_type       text,
  add column if not exists source_citation   text,
  add column if not exists status            text    not null default 'published',
  add column if not exists times_used        integer not null default 0,
  add column if not exists last_used_test_id uuid,
  add column if not exists last_used_date    timestamptz,
  add column if not exists correct_rate      double precision,
  add column if not exists ca_valid_until    date,
  add column if not exists review_due_date   date;

-- The 5 BPSC formats join the original three. Every new format scores as a
-- single correct option, so submit-attempt's scoring loop is unchanged — only
-- the authoring shape (question_data) and the rendering differ. Drop-then-add
-- because the old constraint already exists; existing rows (mcq/multiple/
-- numerical) all satisfy the wider check.
alter table public.questions drop constraint if exists questions_type_chk;
do $$ begin
  alter table public.questions
    add constraint questions_type_chk check (type in (
      'mcq', 'multiple', 'numerical',
      'statement_based', 'match_the_following', 'assertion_reason', 'reasoning_aptitude'));
exception when duplicate_object then null; end $$;

-- Draft/reviewed/published/retired is the authoring workflow the generator
-- filters on (eligible = published). Defaulting to 'published' keeps every
-- existing question eligible; `is_active` stays the soft-delete flag. The full
-- two-reviewer sign-off that drives these transitions is Phase 2.
do $$ begin
  alter table public.questions
    add constraint questions_status_chk check (status in ('draft','reviewed','published','retired'));
exception when duplicate_object then null; end $$;

create index if not exists questions_concept_group_idx on public.questions (concept_group_id) where concept_group_id is not null;
create index if not exists questions_status_idx        on public.questions (status);
create index if not exists questions_times_used_idx    on public.questions (times_used);

comment on column public.questions.question_data is
  'Type-specific stem for BPSC formats: {statements[], list_1[], list_2[], assertion, reason, series} with parallel *_hi keys for Hindi. Part of the prompt, never the answer, so exam_paper() ships it whole.';
comment on column public.questions.concept_group_id is
  'Questions testing the same underlying concept share this id. Human-tagged at authoring time (text-match dedup is unreliable for statement/match formats). The generator never places two from one group in a test, or across tests sharing a theme_group_id.';

-- ---------------------------------------------------------------------------
-- 2. DISTRIBUTION CONFIG — PYQ-derived target weights.
--    Weights key on the EXISTING free-text subject/topic values; no new enum,
--    matching the app's deliberate move away from CHECK-enumerated categories
--    (see the exam_categories note in db.js).
-- ---------------------------------------------------------------------------
create table if not exists public.distribution_config (
  id                    uuid primary key default gen_random_uuid(),
  name                  text not null,
  -- {subject: weight}
  subject_weights       jsonb not null default '{}'::jsonb,
  difficulty_weights    jsonb not null default '{"easy":0.30,"medium":0.50,"hard":0.20}'::jsonb,
  -- per-subject {subject: {type: weight}}, or a flat {type: weight} fallback
  question_type_weights jsonb not null default '{}'::jsonb,
  -- per-subject {subject: {sub_topic: weight}} for sectional tests
  sub_topic_weights     jsonb not null default '{}'::jsonb,
  created_at            timestamptz not null default now(),
  updated_at           timestamptz not null default now()
);

-- ---------------------------------------------------------------------------
-- 3. TEST BLUEPRINTS — the 25-test series plan. Hangs off the existing
--    test_series (reused as the blueprint container); generated tests keep
--    their series_id link and gain a blueprint_id.
-- ---------------------------------------------------------------------------
create table if not exists public.test_blueprints (
  id                     uuid primary key default gen_random_uuid(),
  series_id              uuid references public.test_series(id) on delete cascade,
  sequence_position      integer not null default 1,
  title                  text not null,
  title_hi               text,
  pattern_type           text not null check (pattern_type in ('sectional','half_length','full_length')),
  question_count         integer not null default 150,
  -- sectional: {subject, sub_topic_weights}; half_length: {subject, ca_date_range};
  -- full_length: {distribution_config_id} or inline
  subject_scope          jsonb not null default '{}'::jsonb,
  distribution_config_id uuid references public.distribution_config(id) on delete set null,
  -- links parts of one repeated theme (Bihar Special I/II/III; the CA tests; the
  -- two aptitude tests). Dedup is checked across every blueprint sharing this
  -- slug. Text for the same hand-set reason as concept_group_id.
  theme_group_id         text,
  theme_part_index       integer,
  created_at             timestamptz not null default now(),
  updated_at             timestamptz not null default now()
);
create index if not exists test_blueprints_series_idx on public.test_blueprints (series_id, sequence_position);
create index if not exists test_blueprints_theme_idx  on public.test_blueprints (theme_group_id) where theme_group_id is not null;

alter table public.tests
  add column if not exists blueprint_id uuid references public.test_blueprints(id) on delete set null;

-- ---------------------------------------------------------------------------
-- 4. QUESTION USAGES — the dedup / analytics ledger. This is the reconciled
--    stand-in for the spec's test_questions: it does NOT drive the paper (that
--    stays in tests.sections), it drives cooldown, cross-test / cross-theme
--    concept dedup, and the times_used counter.
-- ---------------------------------------------------------------------------
create table if not exists public.question_usages (
  id               uuid primary key default gen_random_uuid(),
  question_id      uuid not null references public.questions(id) on delete cascade,
  test_id          uuid not null references public.tests(id) on delete cascade,
  blueprint_id     uuid references public.test_blueprints(id) on delete set null,
  theme_group_id   text,
  concept_group_id text,
  used_at          timestamptz not null default now()
);
create index if not exists question_usages_question_idx on public.question_usages (question_id);
create index if not exists question_usages_concept_idx  on public.question_usages (concept_group_id) where concept_group_id is not null;
create index if not exists question_usages_theme_idx    on public.question_usages (theme_group_id) where theme_group_id is not null;
create index if not exists question_usages_test_idx     on public.question_usages (test_id);

-- ---------------------------------------------------------------------------
-- 5. ROW LEVEL SECURITY — all three new tables are admin-only planning
--    artifacts. Generated tests reach students as ordinary published `tests`.
-- ---------------------------------------------------------------------------
alter table public.distribution_config enable row level security;
alter table public.test_blueprints     enable row level security;
alter table public.question_usages     enable row level security;

do $$
declare r record;
begin
  for r in
    select policyname, tablename from pg_policies
    where schemaname = 'public'
      and tablename in ('distribution_config','test_blueprints','question_usages')
  loop
    execute format('drop policy %I on public.%I', r.policyname, r.tablename);
  end loop;
end $$;

create policy distribution_config_admin on public.distribution_config for all
  using (public.is_admin()) with check (public.is_admin());
create policy test_blueprints_admin on public.test_blueprints for all
  using (public.is_admin()) with check (public.is_admin());
create policy question_usages_admin on public.question_usages for all
  using (public.is_admin()) with check (public.is_admin());

-- ---------------------------------------------------------------------------
-- 6. commit_generated_test() — persist a generated paper atomically.
--    The JS engine (src/lib/generate.js) computes the ordered sections; this
--    function writes the test, records usage, and recomputes times_used in one
--    transaction. Admin-guarded and SECURITY DEFINER so it can write past RLS.
--    times_used is DERIVED from question_usages (never a free-standing counter
--    two code paths can disagree about — the same rule as the wallet balance),
--    so a re-commit of the same test stays correct.
-- ---------------------------------------------------------------------------
create or replace function public.commit_generated_test(
  p_test        jsonb,
  p_blueprint   uuid default null,
  p_theme_group text default null
) returns uuid
language plpgsql
security definer
set search_path = public
as $fn$
declare
  v_id   uuid;
  v_qids uuid[];
begin
  if not public.is_admin() then
    raise exception 'not_authorized';
  end if;

  v_id := coalesce(nullif(p_test->>'id','')::uuid, gen_random_uuid());

  insert into public.tests (
    id, title, title_hi, description, series_id, blueprint_id,
    duration_min, sections, is_free, is_published,
    shuffle_questions, shuffle_options, scheduled_for
  ) values (
    v_id,
    p_test->>'title',
    nullif(trim(coalesce(p_test->>'title_hi','')), ''),
    nullif(trim(coalesce(p_test->>'description','')), ''),
    nullif(p_test->>'series_id','')::uuid,
    p_blueprint,
    coalesce((p_test->>'duration_min')::int, 60),
    coalesce(p_test->'sections', '[]'::jsonb),
    coalesce((p_test->>'is_free')::boolean, false),
    coalesce((p_test->>'is_published')::boolean, false),
    coalesce((p_test->>'shuffle_questions')::boolean, true),
    coalesce((p_test->>'shuffle_options')::boolean, true),
    nullif(p_test->>'scheduled_for','')::timestamptz
  )
  on conflict (id) do update set
    title             = excluded.title,
    title_hi          = excluded.title_hi,
    description       = excluded.description,
    series_id         = excluded.series_id,
    blueprint_id      = excluded.blueprint_id,
    duration_min      = excluded.duration_min,
    sections          = excluded.sections,
    is_free           = excluded.is_free,
    is_published      = excluded.is_published,
    shuffle_questions = excluded.shuffle_questions,
    shuffle_options   = excluded.shuffle_options,
    scheduled_for     = excluded.scheduled_for,
    updated_at        = now();

  -- Flatten the ordered questionIds out of the sections.
  select array_agg(qid::uuid)
    into v_qids
  from jsonb_array_elements(coalesce(p_test->'sections','[]'::jsonb)) sec,
       jsonb_array_elements_text(coalesce(sec->'questionIds','[]'::jsonb)) qid;

  -- Re-commit safe: clear prior usage rows for this test before re-recording.
  delete from public.question_usages where test_id = v_id;

  if v_qids is not null then
    insert into public.question_usages (question_id, test_id, blueprint_id, theme_group_id, concept_group_id)
    select q.id, v_id, p_blueprint, p_theme_group, q.concept_group_id
      from public.questions q
     where q.id = any(v_qids);

    update public.questions q set
      times_used        = (select count(*) from public.question_usages qu where qu.question_id = q.id),
      last_used_test_id = v_id,
      last_used_date    = now()
    where q.id = any(v_qids);
  end if;

  return v_id;
end;
$fn$;

revoke execute on function public.commit_generated_test(jsonb, uuid, text) from public, anon;
grant  execute on function public.commit_generated_test(jsonb, uuid, text) to authenticated, service_role;

-- ---------------------------------------------------------------------------
-- 7. exam_paper() — ship question_data so the 5 BPSC formats can render.
--    Identical to 0015 except each question object now also carries `data`
--    (the whole question_data jsonb, Hindi keys included). It is answer-free by
--    construction — statements / lists / assertion+reason never reveal which
--    option is correct — so shipping it whole is safe, and the client picks
--    EN/HI per sub-field just like it does for text_hi / body_hi.
-- ---------------------------------------------------------------------------
create or replace function public.exam_paper(p_test uuid)
returns jsonb
language plpgsql
stable
security definer
set search_path = public
as $fn$
declare
  t      public.tests%rowtype;
  result jsonb;
begin
  select * into t from public.tests where id = p_test and is_published;
  if t.id is null then
    raise exception 'test_not_found';
  end if;

  if not public.can_access_test(p_test) then
    raise exception 'no_access';
  end if;

  select jsonb_build_object(
    'id', t.id,
    'title',      t.title,
    'title_hi',   nullif(trim(coalesce(t.title_hi, '')), ''),
    'seriesTitle', coalesce((select ts.title from public.test_series ts where ts.id = t.series_id), ''),
    'seriesTitle_hi', (select nullif(trim(coalesce(ts.title_hi, '')), '')
                         from public.test_series ts where ts.id = t.series_id),
    'durationMin', coalesce(t.duration_min, 60),
    'shuffleQuestions', coalesce(t.shuffle_questions, false),
    'shuffleOptions', coalesce(t.shuffle_options, false),
    'sections', coalesce((
      select jsonb_agg(sec_obj order by sec_ord)
      from (
        select sec.ord as sec_ord,
               jsonb_build_object(
                 'name', coalesce(sec.value ->> 'name', 'Section'),
                 'questions', coalesce((
                   select jsonb_agg(
                     jsonb_build_object(
                       'id', q.id,
                       'subject', q.subject,
                       'topic', coalesce(nullif(q.topic, ''), q.subject, 'General'),
                       'type', q.type,
                       'text',    q.body,
                       'text_hi', nullif(trim(coalesce(q.body_hi, '')), ''),
                       -- Type-specific stem (statements / lists / assertion+reason).
                       -- Answer-free, so it ships whole; empty for plain formats.
                       'data', coalesce(q.question_data, '{}'::jsonb),
                       'marks', coalesce(q.marks_correct, 2),
                       'negative', coalesce(q.marks_wrong, 0),
                       'options', coalesce((
                         select jsonb_agg(jsonb_build_object(
                                  'id',      o.value ->> 'id',
                                  'body',    o.value ->> 'body',
                                  'body_hi', nullif(trim(coalesce(o.value ->> 'body_hi', '')), ''))
                                          order by o.ord)
                           from jsonb_array_elements(coalesce(q.options, '[]'::jsonb)) with ordinality o(value, ord)
                       ), '[]'::jsonb)
                     ) order by qid.ord)
                     from jsonb_array_elements_text(coalesce(sec.value -> 'questionIds', '[]'::jsonb))
                          with ordinality qid(value, ord)
                     join public.questions q on q.id::text = qid.value and q.is_active
                 ), '[]'::jsonb)
               ) as sec_obj
          from jsonb_array_elements(coalesce(t.sections, '[]'::jsonb)) with ordinality sec(value, ord)
      ) s
    ), '[]'::jsonb)
  ) into result;

  return result;
end;
$fn$;

revoke execute on function public.exam_paper(uuid) from public, anon;
grant  execute on function public.exam_paper(uuid) to authenticated, service_role;
