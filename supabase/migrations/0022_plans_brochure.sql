-- ============================================================================
-- Programme brochures — a downloadable PDF flyer per plan.
--
-- Nullable on purpose: only BPSC has a finalised flyer today. UPSC / UPPCS /
-- JPSC and any future plan start out without one, and the storefront must
-- render exactly the same as before for those (no button, not a broken button)
-- until an admin uploads the PDF for that plan.
--
-- The storage bucket is public because the whole point of a marketing flyer
-- is that anyone can share the link. Admin-only writes; RLS enforces that.
-- ============================================================================

-- 1. Column on plans.
alter table public.plans
  add column if not exists brochure_url text;

-- 2. Rebuild catalog_v to expose brochure_url. The view enumerates its
--    columns (not SELECT *), so a plain column add is invisible to it until
--    we recreate. `create or replace` won't take a NEW column inserted in
--    the middle of the existing column list (that would silently renumber
--    columns for anything reading the view by position, so Postgres refuses
--    outright with `cannot change name of view column`); drop-and-recreate
--    is the sanctioned path.
drop view if exists public.catalog_v;
create view public.catalog_v as
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
     where pt.plan_code = p.code and t.is_published and t.is_free))::integer as free_test_count
from public.plans p
left join public.exam_categories ec on ec.code = p.exam_category
where p.is_active;

grant select on public.catalog_v to anon, authenticated;

-- 3. Storage bucket: brochures. Public read (marketing PDFs), admin write.
--    20 MB cap -- a 4-5 page flyer is well under this even before PDF
--    compression. PDF-only MIME whitelist so nothing else can be dropped in
--    (a stray .exe / .docx here would be a Bad Time).
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('brochures', 'brochures', true, 20971520,
        array['application/pdf'])
on conflict (id) do update
  set public = excluded.public,
      file_size_limit = excluded.file_size_limit,
      allowed_mime_types = excluded.allowed_mime_types;

-- 4. Storage RLS: mirror the 'materials' pattern.
drop policy if exists jn_brochures_read   on storage.objects;
drop policy if exists jn_brochures_write  on storage.objects;
drop policy if exists jn_brochures_update on storage.objects;
drop policy if exists jn_brochures_delete on storage.objects;

create policy jn_brochures_read on storage.objects for select
  using (bucket_id = 'brochures');
create policy jn_brochures_write on storage.objects for insert
  with check (bucket_id = 'brochures' and public.is_admin());
create policy jn_brochures_update on storage.objects for update
  using  (bucket_id = 'brochures' and public.is_admin())
  with check (bucket_id = 'brochures' and public.is_admin());
create policy jn_brochures_delete on storage.objects for delete
  using  (bucket_id = 'brochures' and public.is_admin());
