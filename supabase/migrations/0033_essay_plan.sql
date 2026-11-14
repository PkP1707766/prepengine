-- 0033: an Essay-only plan, sold from the Essay catalogue.
--
-- Until now the only way into Mains was the UPSC Prelims bundle, so the
-- Essay card's Enroll sold Prelims. This adds a Mains plan of its own:
-- Rs 99 (MRP Rs 499) for 365 days. includes_mains is what opens the Essay
-- section (has_mains_access), so nothing else changes for access.
--
-- The plan has no tests. The test-series catalogue must not list it as a
-- series "with papers being finalised", so catalog_v now says which plans
-- include Mains (a new column at the end; create or replace may only add
-- columns there). join-order lets a Mains plan through its empty-plan rule.

create or replace view public.catalog_v as
select
  p.code, p.name, p.exam_category, p.tagline, p.description,
  p.name_hi, p.tagline_hi, p.description_hi,
  p.price_paise, p.mrp_paise, p.currency, p.duration_days,
  p.features, p.sort_order, p.brochure_url,
  ec.label as exam_label, ec.label_hi as exam_label_hi,
  ec.full_name as exam_full_name, ec.full_name_hi as exam_full_name_hi,
  ec.conducted_by, ec.sort_order as exam_sort_order,
  ((select count(*) from public.plan_tests pt
      join public.tests t on t.id = pt.test_id
     where pt.plan_code = p.code and t.is_published))::integer as test_count,
  ((select count(*) from public.plan_tests pt
      join public.tests t on t.id = pt.test_id
     where pt.plan_code = p.code and t.is_published and t.is_free))::integer as free_test_count,
  p.includes_mains
from public.plans p
left join public.exam_categories ec on ec.code = p.exam_category
where p.is_active;

grant select on public.catalog_v to anon, authenticated;

insert into public.plans (
  code, name, name_hi, tagline, tagline_hi, description, description_hi,
  price_paise, mrp_paise, currency, duration_days, features,
  is_active, sort_order, exam_category, includes_mains
) values (
  'mains-essay',
  'UPSC Mains Essay — Complete Catalogue',
  'UPSC मेन्स निबंध — पूरा कैटलॉग',
  'Every essay topic since 2014, the toppers'' own copies, and how to write your own.',
  '2014 से हर निबंध विषय, टॉपर्स की अपनी कॉपियाँ, और अपना लिखना कैसे सीखें।',
  'The Essay section of JUNOONIAS Mains: every essay topic UPSC has set since 2014, filed by theme and by year; topper copies to read page by page; a Learn to Write guide for every topic; and the Essay Wiki of openings, closings, quotes, stories, examples and data matched to each topic.',
  'JUNOONIAS मेन्स का निबंध सेक्शन: 2014 से UPSC का हर निबंध विषय, थीम और साल के हिसाब से; पन्ना-दर-पन्ना पढ़ने के लिए टॉपर कॉपियाँ; हर विषय के लिए लिखना सीखें गाइड; और हर विषय से जुड़े शुरुआत, समापन, उद्धरण, कहानियाँ, उदाहरण और आँकड़ों वाला निबंध विकी।',
  9900, 49900, 'INR', 365,
  '["Every UPSC essay topic since 2014, by theme and by year", "200+ topper copies from 60+ toppers", "A Learn to Write guide for every topic", "1,600+ quotes, stories, examples and data", "Notes, marks and a reading streak", "365 days of access"]'::jsonb,
  true, 90, 'upsc', true
)
on conflict (code) do nothing;
