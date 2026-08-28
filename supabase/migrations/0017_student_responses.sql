-- ============================================================================
-- 0017 — Post-test results & review (§7): the normalized response ledger.
--
-- The per-test result screen already renders from attempts.review (a jsonb
-- snapshot). That blob is the fast path and stays. What it cannot answer is the
-- cross-attempt question — "every Environment question this student got wrong,
-- across all attempts" — so this adds a normalized row-per-question ledger that
-- can, plus the crowd correct_rate and the recalibration foundation.
--
-- Same reconciliation shape as 0016's question_usages: keep the working
-- denormalized path, add a queryable table alongside it, both written in the
-- one server call (submit-attempt).
-- ============================================================================

-- ---------------------------------------------------------------------------
-- 1. STUDENT_RESPONSES — one row per question per attempt.
--    subject / sub_topic / difficulty / question_type are snapshotted so the
--    drill-down filters without joining, and stays correct if a question is
--    later edited. display_option_order records the shuffled order the student
--    actually saw (§7), so the per-test review reconstructs the exact screen.
-- ---------------------------------------------------------------------------
create table if not exists public.student_responses (
  id                  uuid primary key default gen_random_uuid(),
  attempt_id          uuid not null references public.attempts(id) on delete cascade,
  student_id          uuid not null references auth.users(id) on delete cascade,
  test_id             uuid references public.tests(id) on delete set null,
  question_id         uuid references public.questions(id) on delete set null,
  subject             text,
  sub_topic           text,
  difficulty          text,
  question_type       text,
  -- canonical option letters in the on-screen positions, e.g. ["c","a","d","b"]
  display_option_order jsonb not null default '[]'::jsonb,
  -- canonical a/b/c/d the student chose; null if not attempted
  selected_option     text,
  is_correct          boolean,           -- null = not attempted
  time_taken_seconds  integer,
  marked_for_review   boolean not null default false,
  created_at          timestamptz not null default now()
);

create index if not exists student_responses_student_subject_idx on public.student_responses (student_id, subject);
create index if not exists student_responses_question_idx        on public.student_responses (question_id);
create index if not exists student_responses_attempt_idx         on public.student_responses (attempt_id);
create index if not exists student_responses_student_correct_idx on public.student_responses (student_id, is_correct);

-- A student sees a question once per attempt.
create unique index if not exists student_responses_attempt_q_uidx
  on public.student_responses (attempt_id, question_id);

-- Difficulty- and question-type-wise accuracy on the result page, persisted so
-- past attempts show them too (siblings of the existing section_stats/topic_stats).
alter table public.attempts
  add column if not exists difficulty_stats jsonb not null default '[]'::jsonb,
  add column if not exists type_stats       jsonb not null default '[]'::jsonb;

-- ---------------------------------------------------------------------------
-- 2. RLS — a student reads only their own responses; nobody writes from the
--    browser. Only the submit-attempt edge function (service role) inserts,
--    exactly like attempts after 0012.
-- ---------------------------------------------------------------------------
alter table public.student_responses enable row level security;

do $$
declare r record;
begin
  for r in select policyname from pg_policies
           where schemaname = 'public' and tablename = 'student_responses'
  loop execute format('drop policy %I on public.student_responses', r.policyname); end loop;
end $$;

create policy student_responses_select on public.student_responses for select
  using (student_id = auth.uid() or public.is_admin());

-- No insert/update/delete grant to anon/authenticated — service role only.
revoke insert, update, delete on public.student_responses from anon, authenticated;

-- ---------------------------------------------------------------------------
-- 3. my_review() — the drill-down source. Returns the caller's own responses
--    joined to questions, shaped like the per-test review rows so ONE
--    ReviewCard renders both. SECURITY DEFINER because students have no direct
--    read on questions (0013); it only ever returns the caller's own rows and
--    only for questions they actually answered, so no answer key leaks.
--
--    Options come back in CANONICAL order here (concept review across attempts,
--    not reconstruction of one specific screen — that fidelity lives on the
--    per-test result, driven by display_option_order in submit-attempt).
-- ---------------------------------------------------------------------------
create or replace function public.my_review(
  p_subject    text default null,
  p_wrong_only boolean default false
) returns jsonb
language plpgsql
stable
security definer
set search_path = public
as $fn$
declare
  uid    uuid := auth.uid();
  result jsonb;
begin
  if uid is null then raise exception 'not_signed_in'; end if;

  select coalesce(jsonb_agg(row_obj order by created_at desc), '[]'::jsonb)
    into result
  from (
    select sr.created_at,
      jsonb_build_object(
        'responseId', sr.id,
        'attemptId',  sr.attempt_id,
        'testId',     sr.test_id,
        'id',         q.id,
        'subject',    sr.subject,
        'topic',      sr.sub_topic,
        'difficulty', sr.difficulty,
        'type',       sr.question_type,
        'text',       q.body,
        'text_hi',    nullif(trim(coalesce(q.body_hi, '')), ''),
        'data',       coalesce(q.question_data, '{}'::jsonb),
        'options',    coalesce((select jsonb_agg(o.value ->> 'body' order by o.ord)
                                  from jsonb_array_elements(coalesce(q.options, '[]'::jsonb)) with ordinality o(value, ord)), '[]'::jsonb),
        'options_hi', coalesce((select jsonb_agg(nullif(trim(coalesce(o.value ->> 'body_hi', '')), '') order by o.ord)
                                  from jsonb_array_elements(coalesce(q.options, '[]'::jsonb)) with ordinality o(value, ord)), '[]'::jsonb),
        'correctVal', (select o.ord - 1 from jsonb_array_elements(coalesce(q.options, '[]'::jsonb)) with ordinality o(value, ord)
                        where (o.value ->> 'isCorrect')::boolean limit 1),
        'yourVal',    case when sr.selected_option is null then null else ascii(sr.selected_option) - ascii('a') end,
        'attempted',  sr.is_correct is not null,
        'correct',    coalesce(sr.is_correct, false),
        'explanation',    q.explanation,
        'explanation_hi', nullif(trim(coalesce(q.explanation_hi, '')), ''),
        'sourceCitation', q.source_citation,
        'correctRate', (select round(avg(case when x.is_correct then 1 else 0 end) * 100)::int
                          from public.student_responses x
                         where x.question_id = q.id and x.is_correct is not null)
      ) as row_obj
    from public.student_responses sr
    join public.questions q on q.id = sr.question_id
    where sr.student_id = uid
      and (p_subject is null or sr.subject = p_subject)
      and (not p_wrong_only or sr.is_correct = false)
  ) s;

  return result;
end;
$fn$;

revoke execute on function public.my_review(text, boolean) from public, anon;
grant  execute on function public.my_review(text, boolean) to authenticated, service_role;

-- ---------------------------------------------------------------------------
-- 4. refresh_correct_rate() — recompute questions.correct_rate for a set of
--    questions from the response ledger. Called by submit-attempt after it
--    writes the new responses. This is the crowd number the result page shows
--    and the seed for the Phase-2 difficulty-recalibration loop. Kept a
--    fraction (0..1); the UI multiplies by 100.
-- ---------------------------------------------------------------------------
create or replace function public.refresh_correct_rate(p_ids uuid[])
returns void
language sql
security definer
set search_path = public
as $$
  update public.questions q set correct_rate = sub.rate
  from (
    select question_id, avg(case when is_correct then 1 else 0 end)::double precision as rate
      from public.student_responses
     where question_id = any(p_ids) and is_correct is not null
     group by question_id
  ) sub
  where q.id = sub.question_id;
$$;

revoke execute on function public.refresh_correct_rate(uuid[]) from public, anon, authenticated;
grant  execute on function public.refresh_correct_rate(uuid[]) to service_role;
