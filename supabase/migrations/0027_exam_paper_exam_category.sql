-- exam_paper: carry the test's exam category and each section's Hindi name.
--
-- 1. 'examCategory' lets the exam screen present a UPSC paper the way UPSC prints
--    it: no per-question topic tag (a tag like "Pollution, Waste & Resources"
--    narrows the answer before the stem is read). BPSC papers are unchanged.
-- 2. sections[].name_hi -- a generated paper's single section is named after its
--    blueprint, and a Hindi-mode candidate saw that name only in English.
--
-- Otherwise identical to the live definition (0016 + the preview/tester access of
-- 0020/0026): answer-free, both languages, staff can open unpublished papers.
create or replace function public.exam_paper(p_test uuid)
returns jsonb
language plpgsql
stable
security definer
set search_path = public
as $function$
declare
  t      public.tests%rowtype;
  result jsonb;
begin
  select * into t from public.tests where id = p_test and (is_published or public.is_admin() or public.is_tester(auth.uid()));
  if t.id is null then
    raise exception 'test_not_found';
  end if;

  if not public.can_access_test(p_test) then
    raise exception 'no_access';
  end if;

  select jsonb_build_object(
    'id', t.id,
    'isPreview', not t.is_published,
    'examCategory', t.exam_category,
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
                 'name_hi', nullif(trim(coalesce(sec.value ->> 'name_hi', '')), ''),
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
$function$;

revoke execute on function public.exam_paper(uuid) from public, anon;
grant  execute on function public.exam_paper(uuid) to authenticated, service_role;
