-- ============================================================================
-- Exam integrity. Two halves of one hole, both closed here.
--
-- 1. The paper was fetched with `select * from questions`, so every correct
--    answer, the numeric answer and the explanation sat in the browser before
--    the student had answered anything — readable straight from the Network
--    tab, mid-paper.
--
-- 2. The browser computed its own score and inserted it, and
--    saveAttemptStanding() let it write its own `percentile` and
--    `rank_in_test` directly. A student could skip the paper entirely and
--    post score 200/200, rank 1. The leaderboard and the All-India Rank — the
--    headline paid feature — were unverifiable.
-- ============================================================================

-- exam_paper(): the question paper with every answer field removed.
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
    'title', t.title,
    'seriesTitle', coalesce((select ts.title from public.test_series ts where ts.id = t.series_id), ''),
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
                       'text', q.body,
                       'marks', coalesce(q.marks_correct, 2),
                       'negative', coalesce(q.marks_wrong, 0),
                       -- Options carry their stable id and body only. No
                       -- isCorrect, so shuffling client-side stays harmless:
                       -- the answer travels back as an option id.
                       'options', coalesce((
                         select jsonb_agg(jsonb_build_object('id', o.value ->> 'id', 'body', o.value ->> 'body')
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

-- Scores, percentiles and ranks are now written only by the submit-attempt
-- edge function, running as service_role. Students keep their read.
drop policy if exists attempts_insert on public.attempts;
drop policy if exists attempts_update on public.attempts;
revoke insert, update on public.attempts from anon, authenticated;
