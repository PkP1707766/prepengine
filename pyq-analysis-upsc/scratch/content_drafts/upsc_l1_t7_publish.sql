-- Publish Level 1 Test 7 (GS Foundation Revision), owner's go-ahead 2026-10-16 ("yes publish and go ahead", in reply to
-- "Shall I publish Test 7 and the three CSAT Minis, undated like Tests 1-6?"), to match Level 1 Tests 1-6, published undated.
-- Checks first (same rules as for the Level-2 publish): one section of 100 questions, 100 distinct, none shared
-- with another published UPSC test, not free. Like Tests 1-6 it stays undated (self-paced), and its question rows
-- stay 'draft', which keeps them out of the auto-generator; exam_paper does not filter on question status.
-- The checks run inside the transaction, and the update happens only if all of them pass.
begin;
with t as (
  select id, sections, is_free from public.tests
  where exam_category = 'upsc' and title like 'Level 1 · Test 7 %' and not is_published
), ids as (
  select x.v from t, jsonb_array_elements(t.sections) s, jsonb_array_elements_text(s->'questionIds') x(v)
), ok as (
  select (select count(*) from t) = 1
     and (select jsonb_array_length(sections) from t) = 1
     and (select count(*) from ids) = 100
     and (select count(distinct v) from ids) = 100
     and not (select is_free from t)
     and not exists (
       select 1 from public.tests p, jsonb_array_elements(p.sections) s2, jsonb_array_elements_text(s2->'questionIds') y(v)
       where p.exam_category = 'upsc' and p.is_published and y.v in (select v from ids)) as pass
)
update public.tests set is_published = true, updated_at = now()
where id = (select id from t) and (select pass from ok);
commit;
select title, is_published, scheduled_for, total_questions from public.tests
where exam_category = 'upsc' and title like 'Level 1%' order by title;
