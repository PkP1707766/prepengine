-- ============================================================================
-- 0026 — preview attempts: staff can sit a draft test exactly as a student
-- would, without publishing it and without their attempt touching any
-- student-facing statistic.
--
-- Until now exam_paper() and submit-attempt only ever served published tests,
-- so the only way to try a new paper end to end was to publish it first -- to
-- students. The QA-tester flag (0020) granted access to every bundle but still
-- only to published tests.
--
-- * attempts.is_preview marks an attempt by an admin or a QA tester
--   (submit-attempt sets it; any staff attempt counts as a preview, published
--   test or not).
-- * exam_paper() also serves unpublished tests, to admins and testers only,
--   and tells the client it is a preview.
-- * Previews never count: leaderboard_v, attempt_standing() peers (other than
--   the preview attempt itself, so its own result still shows a standing) and
--   refresh_correct_rate() all skip them.
-- ============================================================================

alter table public.attempts
  add column if not exists is_preview boolean not null default false;

comment on column public.attempts.is_preview is
  'Attempt by an admin or QA tester (set by submit-attempt). Excluded from the leaderboard, per-test standing and question correct_rate.';

-- exam_paper(): patch the published-only gate in the live definition rather
-- than re-typing the whole function, and fail loudly if the text has drifted.
do $mig$
declare
  d  text := pg_get_functiondef('public.exam_paper(uuid)'::regprocedure);
  d2 text;
begin
  d2 := replace(d,
    'select * into t from public.tests where id = p_test and is_published;',
    'select * into t from public.tests where id = p_test and (is_published or public.is_admin() or public.is_tester(auth.uid()));');
  if d2 = d then raise exception 'exam_paper(): published-only gate not found; definition has drifted'; end if;
  d := d2;
  d2 := replace(d, $q$'id', t.id,$q$, $q$'id', t.id,
    'isPreview', not t.is_published,$q$);
  if d2 = d then raise exception 'exam_paper(): result object anchor not found; definition has drifted'; end if;
  execute d2;
end
$mig$;

create or replace view public.leaderboard_v
with (security_invoker = true) as
select
  p.id                                         as student_id,
  coalesce(nullif(trim(p.full_name), ''), 'Aspirant') as name,
  p.avatar_url,
  count(a.id)::int                             as tests_taken,
  round(avg(case when a.max_score > 0 then a.score / a.max_score * 100 else 0 end)::numeric, 1) as avg_pct,
  round(max(case when a.max_score > 0 then a.score / a.max_score * 100 else 0 end)::numeric, 1) as best_pct,
  round(avg(a.accuracy)::numeric, 1)           as avg_accuracy,
  rank() over (
    order by avg(case when a.max_score > 0 then a.score / a.max_score * 100 else 0 end) desc,
             count(a.id) desc
  )::int                                       as rank
from public.profiles p
join public.attempts a
  on a.student_id = p.id and a.status = 'submitted' and not a.is_preview
where p.role = 'student'
group by p.id, p.full_name, p.avatar_url;

create or replace function public.attempt_standing(p_attempt uuid)
returns table (rank int, total int, percentile numeric)
language sql
stable
security definer
set search_path = public
as $$
  with target as (
    select test_id, score from public.attempts where id = p_attempt
  ),
  peers as (
    select a.id, a.score
    from public.attempts a, target t
    where a.test_id = t.test_id and a.status = 'submitted'
      and (not a.is_preview or a.id = p_attempt)
  )
  select
    (select count(*) + 1 from peers p, target t where p.score > t.score)::int,
    (select count(*) from peers)::int,
    case when (select count(*) from peers) <= 1 then 100::numeric
         else round(
           (select count(*) from peers p, target t where p.score <= t.score)::numeric
           / (select count(*) from peers)::numeric * 100, 1)
    end;
$$;

create or replace function public.refresh_correct_rate(p_ids uuid[])
returns void
language sql
security definer
set search_path = public
as $$
  update public.questions q set correct_rate = sub.rate
  from (
    select sr.question_id, avg(case when sr.is_correct then 1 else 0 end)::double precision as rate
      from public.student_responses sr
      join public.attempts a on a.id = sr.attempt_id and not a.is_preview
     where sr.question_id = any(p_ids) and sr.is_correct is not null
     group by sr.question_id
  ) sub
  where q.id = sub.question_id;
$$;
