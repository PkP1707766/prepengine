-- Bilingual content columns.
--
-- The UI switched to Hindi but the paper did not: a Hindi-medium student got a
-- Hindi interface wrapped around an English question.
--
-- Two rules throughout:
--
--  1. English is the fallback, always. `coalesce(nullif(trim(x_hi), ''), x)`
--     means a half-translated question bank still works — anything without a
--     Hindi version shows the English one, so translation happens gradually
--     rather than as a big-bang migration.
--
--  2. Option translations live INSIDE each option object as `body_hi`, not in
--     a parallel array. The Hindi text is bound to the option's own id and
--     cannot drift out of alignment with it — which a second array would do
--     the first time someone reorders or deletes an option.
alter table public.questions
  add column if not exists body_hi        text,
  add column if not exists explanation_hi text;

alter table public.tests       add column if not exists title_hi text;
alter table public.test_series add column if not exists title_hi text;

alter table public.plans
  add column if not exists name_hi        text,
  add column if not exists tagline_hi     text,
  add column if not exists description_hi text;

alter table public.exam_categories
  add column if not exists label_hi     text,
  add column if not exists full_name_hi text;

comment on column public.questions.body_hi is
  'Hindi question text. Null or blank falls back to body. Option translations live in options[].body_hi.';

-- Catalogue carries both languages so the storefront can pick without a
-- second round trip.
drop view if exists public.catalog_v;
create view public.catalog_v
with (security_invoker = true) as
select
  p.code, p.name, p.exam_category, p.tagline, p.description,
  p.name_hi, p.tagline_hi, p.description_hi,
  p.price_paise, p.mrp_paise, p.currency, p.duration_days, p.features, p.sort_order,
  ec.label        as exam_label,
  ec.label_hi     as exam_label_hi,
  ec.full_name    as exam_full_name,
  ec.full_name_hi as exam_full_name_hi,
  ec.conducted_by,
  ec.sort_order   as exam_sort_order,
  (select count(*) from public.plan_tests pt join public.tests t on t.id = pt.test_id
    where pt.plan_code = p.code and t.is_published)::int as test_count,
  (select count(*) from public.plan_tests pt join public.tests t on t.id = pt.test_id
    where pt.plan_code = p.code and t.is_published and t.is_free)::int as free_test_count
from public.plans p
left join public.exam_categories ec on ec.code = p.exam_category
where p.is_active;

grant select on public.catalog_v to anon, authenticated;
