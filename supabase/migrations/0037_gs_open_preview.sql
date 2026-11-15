-- 0037: GS open while it is being built; the GS plan, priced and waiting.
--
-- The owner's call (2026-11-15): GS opens to every signed-in student while
-- it is still being filled in, and the lock goes on once it is complete.
-- The switch is one row, so locking it later is
--     update public.mains_settings set value = false where key = 'gs_open';
-- and nothing else changes: has_gs_access() then answers from plans again.
--
-- The GS plan (Rs 999, MRP Rs 1,999, 365 days) is created now but inactive:
-- it is switched on when the lock goes on. catalog_v gains includes_gs so
-- the test-series catalogue can leave a GS plan out, as it does Mains ones.

create table if not exists public.mains_settings (
  key        text primary key,
  value      boolean not null,
  updated_at timestamptz not null default now()
);
alter table public.mains_settings enable row level security;
drop policy if exists mains_settings_read on public.mains_settings;
create policy mains_settings_read on public.mains_settings for select using (true);
drop policy if exists mains_settings_admin on public.mains_settings;
create policy mains_settings_admin on public.mains_settings for all
  using (public.is_admin()) with check (public.is_admin());
grant select on public.mains_settings to anon, authenticated;

insert into public.mains_settings (key, value) values ('gs_open', true)
on conflict (key) do nothing;

create or replace function public.has_gs_access(p_user uuid default auth.uid())
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select public.is_admin()
      or public.is_tester(p_user)
      or (p_user is not null and coalesce((select value from public.mains_settings where key = 'gs_open'), false))
      or exists (
        select 1
        from public.enrollments e
        join public.plans p on p.code = e.plan_code
        where e.student_id = p_user
          and e.status = 'active'
          and (e.expires_at is null or e.expires_at > now())
          and p.includes_gs
      );
$$;

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
  p.includes_mains,
  p.includes_gs
from public.plans p
left join public.exam_categories ec on ec.code = p.exam_category
where p.is_active;

grant select on public.catalog_v to anon, authenticated;

insert into public.plans (
  code, name, name_hi, tagline, tagline_hi, description, description_hi,
  price_paise, mrp_paise, currency, duration_days, features,
  is_active, sort_order, exam_category, includes_mains, includes_gs
) values (
  'mains-gs',
  'UPSC Mains General Studies — GS I to IV',
  'UPSC मेन्स सामान्य अध्ययन — GS I से IV',
  'Every GS question UPSC has set, filed by syllabus topic, with toppers'' answers on each topic.',
  'UPSC के हर GS प्रश्न, सिलेबस टॉपिक के अनुसार, हर टॉपिक पर टॉपर्स के उत्तरों के साथ।',
  'The General Studies section of JUNOONIAS Mains: UPSC''s GS Paper I to IV questions filed by syllabus topic, toppers'' answer copies on every topic, and notes.',
  'JUNOONIAS मेन्स का सामान्य अध्ययन सेक्शन: सिलेबस टॉपिक के अनुसार UPSC के GS पेपर I से IV के प्रश्न, हर टॉपिक पर टॉपर्स की उत्तर कॉपियाँ, और नोट्स।',
  99900, 199900, 'INR', 365,
  '["UPSC GS Paper I to IV questions, by syllabus topic and by year", "Toppers'' answer copies on every topic", "Notes, marks and a reading streak", "365 days of access"]'::jsonb,
  false, 91, 'upsc', false, true
)
on conflict (code) do nothing;
