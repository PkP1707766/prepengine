-- Publish Level 3 CSAT Tests 1-4 (Paper II, Advanced), dated Saturdays 27 March to 17 April 2027 at 2:30 pm, owner's
-- go-ahead 2026-10-24 ("yes publish and go ahead for next"). Checks first, per paper, inside the transaction (the rules
-- used for the Level 1 CSAT Minis, at full length): one section of 80 questions, 80 distinct, none shared with another
-- published UPSC test, not free, 120 minutes, a date set; and every question row present, bilingual, with exactly one
-- correct option. A paper that fails any check stays unpublished. The question rows stay 'draft', which keeps them out
-- of the auto-generator; exam_paper does not filter on question status.
begin;
with t as (
  select id, sections, is_free, duration_min, scheduled_for from public.tests
  where exam_category = 'upsc' and title like 'Level 3 · CSAT Test %' and not is_published
), ids as (
  select t.id as tid, x.v from t, jsonb_array_elements(t.sections) s, jsonb_array_elements_text(s->'questionIds') x(v)
), ok as (
  select t.id from t
  where jsonb_array_length(t.sections) = 1
    and (select count(*) from ids where ids.tid = t.id) = 80
    and (select count(distinct v) from ids where ids.tid = t.id) = 80
    and not t.is_free and t.duration_min = 120 and t.scheduled_for is not null
    and (select count(*) from public.questions qq join ids on ids.v::uuid = qq.id
         where ids.tid = t.id and qq.body_hi is not null and qq.explanation_hi is not null
           and (select count(*) from jsonb_array_elements(qq.options) o where (o->>'isCorrect')::boolean) = 1) = 80
    and not exists (
      select 1 from public.tests p, jsonb_array_elements(p.sections) s2, jsonb_array_elements_text(s2->'questionIds') y(v)
      where p.exam_category = 'upsc' and p.is_published and y.v in (select v from ids where ids.tid = t.id))
)
update public.tests set is_published = true, updated_at = now()
where id in (select id from ok);
commit;
select title, is_published, scheduled_for, duration_min, total_questions from public.tests
where exam_category = 'upsc' and title like 'Level 3%' order by title;
