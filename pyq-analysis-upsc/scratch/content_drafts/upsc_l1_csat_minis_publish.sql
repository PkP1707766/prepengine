-- Publish Level 1 CSAT Minis 1-3 (the one-hour CSAT half papers), undated like Level 1 Tests 1-6, owner's go-ahead
-- 2026-10-16 ("yes publish and go ahead", in reply to "Shall I publish Test 7 and the three CSAT Minis?").
-- Checks first, per paper, inside the transaction (same rules as the GS papers): one section of 40 questions, 40
-- distinct, none shared with another published UPSC test, not free, 60 minutes. A paper that fails any check stays
-- unpublished. Their question rows stay 'draft', which keeps them out of the auto-generator; exam_paper does not
-- filter on question status.
begin;
with t as (
  select id, sections, is_free, duration_min from public.tests
  where exam_category = 'upsc' and title like 'Level 1 · CSAT Mini %' and not is_published
), ids as (
  select t.id as tid, x.v from t, jsonb_array_elements(t.sections) s, jsonb_array_elements_text(s->'questionIds') x(v)
), ok as (
  select t.id from t
  where jsonb_array_length(t.sections) = 1
    and (select count(*) from ids where ids.tid = t.id) = 40
    and (select count(distinct v) from ids where ids.tid = t.id) = 40
    and not t.is_free and t.duration_min = 60
    and not exists (
      select 1 from public.tests p, jsonb_array_elements(p.sections) s2, jsonb_array_elements_text(s2->'questionIds') y(v)
      where p.exam_category = 'upsc' and p.is_published and y.v in (select v from ids where ids.tid = t.id))
)
update public.tests set is_published = true, updated_at = now()
where id in (select id from ok);
commit;
select title, is_published, scheduled_for, duration_min, total_questions from public.tests
where exam_category = 'upsc' and title like 'Level 1%' order by title;
