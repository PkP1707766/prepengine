-- exam_paper() ships BOTH languages in one payload rather than taking a
-- language argument.
--
-- The reason is the switch mid-attempt. If the paper were fetched per
-- language, a student changing language halfway would need it re-fetched — and
-- with shuffleQuestions/shuffleOptions on, the re-fetch reshuffles, so the
-- paper they are halfway through rearranges underneath them. Carrying both
-- languages makes the swap a re-render: instant, order untouched, and no
-- second round trip on a screen where the clock is running.
--
-- There is no secrecy cost. The question text is not the answer; nothing in
-- this payload reveals which option is correct, in either language.
drop function if exists public.exam_paper(uuid, text);
drop function if exists public.exam_paper(uuid);

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
