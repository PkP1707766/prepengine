-- Publish the 27 Level-2 papers of the UPSC Prelims 2027 series (owner's go-ahead, 2026-10-11), after the
-- answer-(d) fix (l2_dshare_fix.sql) and the re-run of upsc_series_setup.sql.
-- Checks done first (same rules as the admin's Publish button): every paper is a standard length (100 / 80),
-- one section each, 2,560 slots holding 2,560 distinct questions, none shared with another published UPSC test,
-- none free, none past-dated, all linked to the prelims-2026 plan.
-- Effect: each paper shows to entitled students as "upcoming" until its scheduled_for time, and its questions are
-- marked published so the bank reflects their use (the generator draws only published rows).
-- Level 1 Test 1 is not in this series and stays unpublished (its timing is still the owner's call).
begin;
update public.questions q set status = 'published', updated_at = now()
where q.status in ('draft', 'reviewed')
  and q.id::text in (select x.v from public.tests t, jsonb_array_elements(t.sections) s, jsonb_array_elements_text(s->'questionIds') x(v)
                     where t.exam_category = 'upsc' and t.series_id = '2bd2e098-2e48-4ebf-95a1-d86166211a77');
update public.tests set is_published = true, updated_at = now()
where exam_category = 'upsc' and series_id = '2bd2e098-2e48-4ebf-95a1-d86166211a77' and not is_published;
commit;
select (select count(*) from public.tests where exam_category = 'upsc' and is_published) as upsc_tests_published,
       (select count(*) from public.tests where exam_category = 'upsc' and not is_published) as upsc_tests_unpublished,
       (select count(*) from public.tests t, jsonb_array_elements(t.sections) s, jsonb_array_elements_text(s->'questionIds') x(v)
          join public.questions q on q.id::text = x.v
        where t.exam_category = 'upsc' and t.is_published and q.status <> 'published') as unpublished_rows_in_published_tests,
       (select count(*) from public.questions where exam_category = 'upsc' and status = 'published') as upsc_published_rows;
