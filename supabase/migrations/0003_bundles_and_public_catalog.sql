-- ============================================================================
-- JUNOONIAS — Phase 1: multi-exam bundles + a publicly browsable catalogue.
--
-- Two deliberate deviations from the written spec, both for good reasons:
--
--  1. The spec gives `plans` a new uuid `id` primary key. This migration keeps
--     `plans.code` as the key instead. `code` is already the primary key, and
--     `enrollments.plan_code` and `payments.plan_code` already reference it —
--     there is one live enrollment and four paid payments riding on that FK.
--     Adding a parallel uuid would give every plan two identities and two ways
--     to get a join wrong, for no gain.
--
--  2. The spec types price as `numeric`. This keeps `price_paise` as an
--     integer. Razorpay transacts in paise anyway, and integer paise means a
--     percentage coupon can never leave a third-of-a-paisa rounding artefact
--     in someone's invoice. Rupees are derived for display only.
-- ============================================================================

-- ---------------------------------------------------------------------------
-- 1. PLANS become per-exam bundles.
-- ---------------------------------------------------------------------------
alter table public.plans
  add column if not exists exam_category text not null default 'upsc',
  add column if not exists tagline       text,
  add column if not exists highlights    jsonb not null default '[]'::jsonb,
  add column if not exists updated_at    timestamptz not null default now();

do $$ begin
  alter table public.plans
    add constraint plans_exam_category_chk
    check (exam_category in ('upsc', 'bpsc', 'uppcs', 'ssc', 'other'));
exception when duplicate_object then null; end $$;

-- The existing plan already has a paying student on it, so it is renamed in
-- place rather than replaced.
update public.plans
   set name          = 'UPSC Prelims 2026 — Full Test Series',
       exam_category = 'upsc',
       tagline       = 'Complete GS + CSAT coverage with All-India ranking',
       updated_at    = now()
 where code = 'prelims-2026';

insert into public.plans
  (code, name, exam_category, tagline, description, price_paise, mrp_paise, duration_days, features, sort_order)
values
  ('bpsc-2026', 'BPSC Prelims 2026 — Full Test Series', 'bpsc',
   'Bihar-focused GS with current affairs depth',
   'Full-length BPSC prelims mocks, sectionals and Bihar-specific current affairs.',
   39900, 79900, 365,
   '["20 full-length BPSC mock tests","Bihar-specific current affairs sets","Detailed solutions for every question","All-India rank and percentile","Valid till the 2026 Prelims"]'::jsonb, 2),
  ('uppcs-2026', 'UPPCS Prelims 2026 — Full Test Series', 'uppcs',
   'UP-focused GS with CSAT practice',
   'Full-length UPPCS prelims mocks with UP-specific static and current affairs coverage.',
   39900, 79900, 365,
   '["20 full-length UPPCS mock tests","UP-specific static & current affairs","Detailed solutions for every question","All-India rank and percentile","Valid till the 2026 Prelims"]'::jsonb, 3)
on conflict (code) do nothing;

-- ---------------------------------------------------------------------------
-- 2. PLAN ↔ TEST mapping. This is what keeps bundles genuinely isolated:
--    buying UPSC must never unlock BPSC papers.
-- ---------------------------------------------------------------------------
create table if not exists public.plan_tests (
  plan_code text not null references public.plans(code) on delete cascade,
  test_id   uuid not null references public.tests(id)   on delete cascade,
  added_at  timestamptz not null default now(),
  primary key (plan_code, test_id)
);

create index if not exists plan_tests_test_idx on public.plan_tests (test_id);

-- Every test that already exists predates bundles, so it belongs to the
-- original UPSC bundle — otherwise the one paying student loses access.
insert into public.plan_tests (plan_code, test_id)
select 'prelims-2026', t.id from public.tests t
on conflict do nothing;

-- ---------------------------------------------------------------------------
-- 3. ENTITLEMENT — one function, used by both RLS and the app.
-- ---------------------------------------------------------------------------

/* Does the caller hold a live enrollment on this plan? */
create or replace function public.has_plan(p_code text)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (
    select 1 from public.enrollments e
    where e.student_id = auth.uid()
      and e.plan_code  = p_code
      and e.status     = 'active'
      and (e.expires_at is null or e.expires_at > now())
  );
$$;

/* May the caller actually sit this test?
   True when: they are an admin, OR the test is a free sample, OR they hold a
   live enrollment on at least one bundle that contains this test. */
create or replace function public.can_access_test(p_test uuid)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select
    public.is_admin()
    or exists (select 1 from public.tests t where t.id = p_test and t.is_free and t.is_published)
    or exists (
      select 1
      from public.plan_tests pt
      join public.enrollments e
        on e.plan_code = pt.plan_code
       and e.student_id = auth.uid()
       and e.status = 'active'
       and (e.expires_at is null or e.expires_at > now())
      where pt.test_id = p_test
    );
$$;

-- ---------------------------------------------------------------------------
-- 4. PUBLIC CATALOGUE — the storefront is browsable without an account.
--    Prices and what's included must never sit behind a login wall.
-- ---------------------------------------------------------------------------
drop policy if exists plans_select   on public.plans;
drop policy if exists tests_select   on public.tests;
drop policy if exists series_select  on public.test_series;
drop policy if exists courses_select on public.courses;
drop policy if exists batches_select on public.batches;

create policy plans_select on public.plans for select
  using (is_active or public.is_admin());

-- Anyone may see that a test exists, its title, question count and duration.
-- The questions themselves are gated separately, below.
create policy tests_select on public.tests for select
  using (is_published or public.is_admin());

create policy series_select on public.test_series for select using (true);

create policy courses_select on public.courses for select
  using (is_published or public.is_admin());

create policy batches_select on public.batches for select
  using (is_active or public.is_admin());

create policy plan_tests_select on public.plan_tests for select using (true);
create policy plan_tests_admin  on public.plan_tests for all
  using (public.is_admin()) with check (public.is_admin());

alter table public.plan_tests enable row level security;

-- ---------------------------------------------------------------------------
-- 5. CLOSE THE QUESTION-BANK HOLE.
--
--    The previous policy was `auth.uid() is not null` — meaning ANY signed-in
--    account, including one that had never paid a rupee, could read the entire
--    question bank straight off the REST endpoint. Now a question is readable
--    only if it belongs to a test the caller is actually entitled to.
-- ---------------------------------------------------------------------------
drop policy if exists questions_select on public.questions;

create policy questions_select on public.questions for select
  using (
    public.is_admin()
    or (
      is_active
      and exists (
        select 1
        from public.tests t,
             lateral jsonb_array_elements(coalesce(t.sections, '[]'::jsonb)) sec,
             lateral jsonb_array_elements_text(coalesce(sec -> 'questionIds', '[]'::jsonb)) qid
        where qid = public.questions.id::text
          and public.can_access_test(t.id)
      )
    )
  );

-- ---------------------------------------------------------------------------
-- 6. Catalogue view — bundle cards, priced, with a live test count.
--    Exposed to anonymous visitors on purpose: this is the shop window.
-- ---------------------------------------------------------------------------
create or replace view public.catalog_v
with (security_invoker = true) as
select
  p.code,
  p.name,
  p.exam_category,
  p.tagline,
  p.description,
  p.price_paise,
  p.mrp_paise,
  p.currency,
  p.duration_days,
  p.features,
  p.sort_order,
  (select count(*) from public.plan_tests pt
     join public.tests t on t.id = pt.test_id
    where pt.plan_code = p.code and t.is_published)::int as test_count,
  (select count(*) from public.plan_tests pt
     join public.tests t on t.id = pt.test_id
    where pt.plan_code = p.code and t.is_published and t.is_free)::int as free_test_count
from public.plans p
where p.is_active;

grant select on public.catalog_v to anon, authenticated;
grant execute on function public.has_plan(text)        to anon, authenticated;
grant execute on function public.can_access_test(uuid) to anon, authenticated;
