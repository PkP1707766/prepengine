-- ============================================================================
-- JUNOONIAS — exam categories become data, not a CHECK constraint.
--
-- `plans.exam_category` was pinned by a CHECK list ('upsc','bpsc','uppcs',
-- 'ssc','other'). Every new exam then needed a migration, which is why the
-- JPSC bundle ended up filed under "Other". A lookup table means the admin
-- adds an exam themselves and it appears as a tab on the public site
-- immediately — no SQL, no deploy.
-- ============================================================================

create table if not exists public.exam_categories (
  code          text primary key,          -- 'upsc', 'jpsc', 'rpsc'
  label         text not null,             -- short, used on tabs: 'JPSC'
  full_name     text,                      -- 'Jharkhand Public Service Commission'
  conducted_by  text,                      -- 'UPSC', 'BPSC', 'RPSC'
  region        text,                      -- 'National', 'Jharkhand'
  sort_order    integer not null default 100,
  is_active     boolean not null default true,
  created_at    timestamptz not null default now()
);

-- Seeded with what JUNOONIAS actually sells or plans to. `full_name` is left
-- null where the exact expansion is not something to state on a student's
-- behalf without confirmation — the admin fills it in.
insert into public.exam_categories (code, label, full_name, conducted_by, region, sort_order) values
  ('upsc',   'UPSC',   'Union Public Service Commission — Civil Services',   'UPSC',  'National',     10),
  ('epfo',   'EPFO',   'EPFO Enforcement Officer / Accounts Officer',        'UPSC',  'National',     20),
  ('bpsc',   'BPSC',   'Bihar Public Service Commission',                    'BPSC',  'Bihar',        30),
  ('aedo',   'AEDO',   null,                                                 'BPSC',  'Bihar',        40),
  ('uppcs',  'UPPCS',  'Uttar Pradesh Public Service Commission',            'UPPSC', 'Uttar Pradesh',50),
  ('jpsc',   'JPSC',   'Jharkhand Public Service Commission',                'JPSC',  'Jharkhand',    60),
  ('rpsc',   'RPSC',   'Rajasthan Administrative Service (RAS)',             'RPSC',  'Rajasthan',    70),
  ('hpsc',   'HPSC',   'Haryana Civil Services (HCS)',                       'HPSC',  'Haryana',      80),
  ('ukpsc',  'UKPSC',  'Uttarakhand Public Service Commission',              'UKPSC', 'Uttarakhand',  90),
  ('ssc',    'SSC',    'Staff Selection Commission',                         'SSC',   'National',    100),
  ('other',  'Other',  null,                                                 null,    null,          999)
on conflict (code) do update
  set label        = excluded.label,
      full_name    = coalesce(public.exam_categories.full_name, excluded.full_name),
      conducted_by = coalesce(public.exam_categories.conducted_by, excluded.conducted_by),
      region       = coalesce(public.exam_categories.region, excluded.region),
      sort_order   = excluded.sort_order;

-- Swap the CHECK for a foreign key. ON UPDATE CASCADE so renaming a code later
-- carries through to every plan rather than orphaning them.
alter table public.plans drop constraint if exists plans_exam_category_chk;
do $$ begin
  alter table public.plans
    add constraint plans_exam_category_fk
    foreign key (exam_category) references public.exam_categories(code) on update cascade;
exception when duplicate_object then null; end $$;

-- The JPSC bundle was created before 'jpsc' existed, so it landed in "Other".
update public.plans set exam_category = 'jpsc', updated_at = now()
 where code = 'jpsc' and exam_category = 'other';

-- ---------------------------------------------------------------------------
-- RLS — public read (the tabs are part of the storefront), admin writes.
-- ---------------------------------------------------------------------------
alter table public.exam_categories enable row level security;

drop policy if exists exam_cat_read  on public.exam_categories;
drop policy if exists exam_cat_admin on public.exam_categories;

create policy exam_cat_read on public.exam_categories for select
  using (is_active or public.is_admin());
create policy exam_cat_admin on public.exam_categories for all
  using (public.is_admin()) with check (public.is_admin());

grant select on public.exam_categories to anon, authenticated;

-- The catalogue view now carries the label so the public site never has to
-- keep its own copy of the exam names.
create or replace view public.catalog_v
with (security_invoker = true) as
select
  p.code, p.name, p.exam_category, p.tagline, p.description,
  p.price_paise, p.mrp_paise, p.currency, p.duration_days, p.features, p.sort_order,
  ec.label       as exam_label,
  ec.full_name   as exam_full_name,
  ec.conducted_by,
  ec.sort_order  as exam_sort_order,
  (select count(*) from public.plan_tests pt join public.tests t on t.id = pt.test_id
    where pt.plan_code = p.code and t.is_published)::int as test_count,
  (select count(*) from public.plan_tests pt join public.tests t on t.id = pt.test_id
    where pt.plan_code = p.code and t.is_published and t.is_free)::int as free_test_count
from public.plans p
left join public.exam_categories ec on ec.code = p.exam_category
where p.is_active;

grant select on public.catalog_v to anon, authenticated;
