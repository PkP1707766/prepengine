-- ============================================================================
-- JUNOONIAS — Phase 2: public content hub.
--
-- Syllabus, previous-year papers, NCERT books, daily current affairs and FAQ.
-- Every one of these is a real table with an admin CRUD screen, not hardcoded
-- page content — the whole point of the last few weeks was getting invented
-- data out of this product, and a syllabus baked into a JSX file would be the
-- same mistake wearing a different hat.
--
-- All of it is readable without an account. That is the point of section 3 of
-- the public-flow spec: a first-time visitor needs real reasons to stay.
-- ============================================================================

-- ---------------------------------------------------------------------------
-- 1. SYLLABUS — exam → paper → section → topic
-- ---------------------------------------------------------------------------
create table if not exists public.syllabus_topics (
  id           uuid primary key default gen_random_uuid(),
  exam         text not null,              -- matches plans.exam_category
  paper        text not null,              -- 'Prelims GS Paper I', 'CSAT Paper II'
  section      text,                       -- 'Indian Polity and Governance'
  topic        text not null,
  detail       text,
  sort_order   integer not null default 0,
  is_published boolean not null default true,
  created_at   timestamptz not null default now(),
  updated_at   timestamptz not null default now()
);
create index if not exists syllabus_exam_idx on public.syllabus_topics (exam, paper, sort_order);

-- ---------------------------------------------------------------------------
-- 2. PREVIOUS YEAR PAPERS
-- ---------------------------------------------------------------------------
create table if not exists public.pyq_papers (
  id            uuid primary key default gen_random_uuid(),
  exam          text not null,
  year          integer not null,
  paper         text not null,             -- 'Prelims GS Paper I'
  title         text not null,
  paper_url     text,                      -- question paper
  solution_url  text,                      -- solved / answer key
  question_count integer,
  notes         text,
  is_published  boolean not null default true,
  created_at    timestamptz not null default now()
);
create index if not exists pyq_exam_year_idx on public.pyq_papers (exam, year desc);

-- ---------------------------------------------------------------------------
-- 3. NCERT BOOKS
-- ---------------------------------------------------------------------------
create table if not exists public.ncert_books (
  id           uuid primary key default gen_random_uuid(),
  class_level  integer not null check (class_level between 1 and 12),
  subject      text not null,
  title        text not null,
  language     text not null default 'en' check (language in ('en', 'hi')),
  url          text,
  is_published boolean not null default true,
  sort_order   integer not null default 0,
  created_at   timestamptz not null default now()
);
create index if not exists ncert_class_idx on public.ncert_books (class_level, subject);

-- ---------------------------------------------------------------------------
-- 4. DAILY CURRENT AFFAIRS
-- ---------------------------------------------------------------------------
create table if not exists public.current_affairs (
  id           uuid primary key default gen_random_uuid(),
  published_on date not null default (now() at time zone 'Asia/Kolkata')::date,
  title        text not null,
  summary      text,
  body         text,
  tags         text[] not null default '{}',
  source_name  text,
  source_url   text,
  exam_tags    text[] not null default '{}',
  is_published boolean not null default true,
  created_by   uuid references auth.users(id) on delete set null,
  created_at   timestamptz not null default now()
);
create index if not exists ca_date_idx on public.current_affairs (published_on desc);

-- ---------------------------------------------------------------------------
-- 5. FAQ
-- ---------------------------------------------------------------------------
create table if not exists public.faqs (
  id           uuid primary key default gen_random_uuid(),
  category     text not null default 'general',
  question     text not null,
  answer       text not null,
  sort_order   integer not null default 0,
  is_published boolean not null default true,
  created_at   timestamptz not null default now()
);

-- ---------------------------------------------------------------------------
-- 6. RLS — public read of published rows, admin-only writes.
-- ---------------------------------------------------------------------------
alter table public.syllabus_topics enable row level security;
alter table public.pyq_papers      enable row level security;
alter table public.ncert_books     enable row level security;
alter table public.current_affairs enable row level security;
alter table public.faqs            enable row level security;

do $$
declare r record;
begin
  for r in select policyname, tablename from pg_policies
           where schemaname='public'
             and tablename in ('syllabus_topics','pyq_papers','ncert_books','current_affairs','faqs')
  loop execute format('drop policy %I on public.%I', r.policyname, r.tablename); end loop;
end $$;

create policy syllabus_read  on public.syllabus_topics for select using (is_published or public.is_admin());
create policy syllabus_admin on public.syllabus_topics for all using (public.is_admin()) with check (public.is_admin());

create policy pyq_read  on public.pyq_papers for select using (is_published or public.is_admin());
create policy pyq_admin on public.pyq_papers for all using (public.is_admin()) with check (public.is_admin());

create policy ncert_read  on public.ncert_books for select using (is_published or public.is_admin());
create policy ncert_admin on public.ncert_books for all using (public.is_admin()) with check (public.is_admin());

create policy ca_read  on public.current_affairs for select using (is_published or public.is_admin());
create policy ca_admin on public.current_affairs for all using (public.is_admin()) with check (public.is_admin());

create policy faq_read  on public.faqs for select using (is_published or public.is_admin());
create policy faq_admin on public.faqs for all using (public.is_admin()) with check (public.is_admin());

-- ---------------------------------------------------------------------------
-- 7. Free study material becomes publicly visible.
--
--    The existing policy required a signed-in user for everything, which meant
--    the "free materials" page would have been empty for exactly the visitors
--    it is meant to convince. Free + published is now open; paid material
--    still needs a live enrollment.
-- ---------------------------------------------------------------------------
drop policy if exists materials_select on public.materials;
create policy materials_select on public.materials for select
  using (
    public.is_admin()
    or (is_published and is_free)
    or (is_published and auth.uid() is not null and exists (
      select 1 from public.enrollments e
      where e.student_id = auth.uid()
        and e.status = 'active'
        and (e.expires_at is null or e.expires_at > now())
        and (e.batch_id is null or e.batch_id = public.materials.batch_id)
    ))
  );

grant select on public.syllabus_topics, public.pyq_papers, public.ncert_books,
                public.current_affairs, public.faqs to anon, authenticated;
