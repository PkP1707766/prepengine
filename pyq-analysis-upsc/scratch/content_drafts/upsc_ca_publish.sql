-- Publish the quarterly current-affairs tests that are complete and dated (Saturdays at 9:30 am, 12 December 2026 to
-- 10 April 2027), under the owner's standing go-ahead ("yes publish and go ahead for next"; "no need to ask me on each
-- step"). Re-run it as each test is set up: a published paper is skipped, since it is already frozen.
-- Checks first, per paper, inside the transaction (as for Levels 3 and 4): one section of 100 questions, 100 distinct,
-- none shared with another published UPSC test, not free, 120 minutes, a date set; and every question row present,
-- bilingual, with exactly one correct option. A paper that fails any check stays unpublished. Question rows stay
-- 'draft', which keeps them out of the auto-generator; exam_paper does not filter on question status.
begin;
with t as (
  select id, sections, is_free, duration_min, scheduled_for from public.tests
  where exam_category = 'upsc' and title like 'Current Affairs · Test %' and not is_published
), ids as (
  select t.id as tid, x.v from t, jsonb_array_elements(t.sections) s, jsonb_array_elements_text(s->'questionIds') x(v)
), ok as (
  select t.id from t
  where jsonb_array_length(t.sections) = 1
    and (select count(*) from ids where ids.tid = t.id) = 100
    and (select count(distinct v) from ids where ids.tid = t.id) = 100
    and not t.is_free and t.duration_min = 120 and t.scheduled_for is not null
    and (select count(*) from public.questions qq join ids on ids.v::uuid = qq.id
         where ids.tid = t.id and qq.body_hi is not null and qq.explanation_hi is not null
           and (select count(*) from jsonb_array_elements(qq.options) o where (o->>'isCorrect')::boolean) = 1) = 100
    and not exists (
      select 1 from public.tests p, jsonb_array_elements(p.sections) s2, jsonb_array_elements_text(s2->'questionIds') y(v)
      where p.exam_category = 'upsc' and p.is_published and y.v in (select v from ids where ids.tid = t.id))
)
update public.tests set is_published = true, updated_at = now()
where id in (select id from ok);
commit;
select title, is_published, scheduled_for, duration_min, total_questions from public.tests
where exam_category = 'upsc' and title like 'Current Affairs%' order by title;
