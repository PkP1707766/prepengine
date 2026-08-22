-- ==========================================================================
-- JUNOONIAS — RUN THIS ONCE, THEN DELETE THIS FILE.
--
-- Paste the whole thing into the Supabase SQL editor:
--   https://supabase.com/dashboard/project/jcdlgfpaoebsapjaqzah/sql/new
-- and press Run. It is idempotent — re-running it is safe.
--
-- This is simply migrations 0001 + 0002 concatenated, for people who would
-- rather not install the Supabase CLI. If you use the CLI instead, run
--   npx supabase link --project-ref jcdlgfpaoebsapjaqzah && npx supabase db push
-- and ignore this file.
-- ==========================================================================

-- ============================================================================
-- JUNOONIAS — core schema, hardening and missing columns.
--
-- Safe to run repeatedly: every statement is idempotent. It is written to be
-- applied on top of the tables that already exist in the project
-- (profiles, questions, enrollments, tests, attempts, payments, courses,
--  batches, materials, test_series, notifications).
--
-- Column naming note: `enrollments`/`attempts` key the student as `student_id`
-- while `payments`/`notifications` use `user_id`. Both point at auth.users(id).
-- The app reads these through src/lib/db.js, which is the single place that
-- knows the difference — do not hand-write queries elsewhere.
-- ============================================================================

create extension if not exists "pgcrypto";

-- ---------------------------------------------------------------------------
-- 1. PROFILES — one row per auth user, created automatically on signup.
-- ---------------------------------------------------------------------------
alter table public.profiles
  add column if not exists full_name      text,
  add column if not exists email          text,
  add column if not exists phone          text,
  add column if not exists role           text    not null default 'student',
  add column if not exists avatar_url     text,
  add column if not exists target_exam    text    default 'UPSC Prelims 2026',
  add column if not exists target_date    date,
  add column if not exists city           text,
  add column if not exists prefs          jsonb   not null default '{}'::jsonb,
  add column if not exists last_seen_at   timestamptz,
  add column if not exists created_at     timestamptz not null default now(),
  add column if not exists updated_at     timestamptz not null default now();

do $$ begin
  alter table public.profiles
    add constraint profiles_role_chk check (role in ('student', 'admin'));
exception when duplicate_object then null; end $$;

-- Creates the profile row the moment a user signs up (email, phone or Google).
create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  insert into public.profiles (id, full_name, email, phone)
  values (
    new.id,
    coalesce(new.raw_user_meta_data ->> 'full_name',
             new.raw_user_meta_data ->> 'name',
             split_part(coalesce(new.email, ''), '@', 1)),
    new.email,
    new.phone
  )
  on conflict (id) do update
    set email = coalesce(excluded.email, public.profiles.email),
        phone = coalesce(excluded.phone, public.profiles.phone);
  return new;
end;
$$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

-- Backfill: accounts that existed before the trigger was installed may have a
-- profile row with a NULL email (or no row at all). That matters because the
-- obvious way to grant yourself admin --
--   update public.profiles set role = 'admin' where email = '...';
-- -- silently matches ZERO rows when the email was never copied across.
insert into public.profiles (id, full_name, email, phone)
select u.id,
       coalesce(u.raw_user_meta_data ->> 'full_name',
                u.raw_user_meta_data ->> 'name',
                split_part(coalesce(u.email, ''), '@', 1)),
       u.email,
       u.phone
from auth.users u
on conflict (id) do update
  set email = coalesce(public.profiles.email, excluded.email),
      phone = coalesce(public.profiles.phone, excluded.phone);

-- Privilege escalation guard: a user may edit their own profile but may never
-- hand themselves the admin role. Only the service role can change `role`.
create or replace function public.guard_profile_role()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  -- PostgREST switches the connection role to anon / authenticated /
  -- service_role per request, so `current_user` is the reliable signal here.
  -- (The per-claim GUCs like request.jwt.claim.role were removed in
  -- PostgREST 9, so checking those would silently never match.)
  if new.role is distinct from old.role
     and current_user in ('anon', 'authenticated') then
    raise exception 'role cannot be changed from the client';
  end if;
  new.updated_at := now();
  return new;
end;
$$;

drop trigger if exists profiles_guard_role on public.profiles;
create trigger profiles_guard_role
  before update on public.profiles
  for each row execute function public.guard_profile_role();

-- Single source of truth for "is the caller an admin?". SECURITY DEFINER so it
-- can read profiles without tripping the very policies that call it.
create or replace function public.is_admin()
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (
    select 1 from public.profiles
    where id = auth.uid() and role = 'admin'
  );
$$;

-- ---------------------------------------------------------------------------
-- 2. PLANS — the paywall price lives in the database, never in client code.
-- ---------------------------------------------------------------------------
create table if not exists public.plans (
  code            text primary key,
  name            text not null,
  description     text,
  price_paise     integer not null check (price_paise >= 0),
  mrp_paise       integer,
  currency        text not null default 'INR',
  duration_days   integer,                       -- null = lifetime
  features        jsonb not null default '[]'::jsonb,
  is_active       boolean not null default true,
  sort_order      integer not null default 0,
  created_at      timestamptz not null default now()
);

insert into public.plans (code, name, description, price_paise, mrp_paise, duration_days, features, sort_order)
values
  ('prelims-2026', 'Prelims 2026 — Full Access',
   'Every mock test, full solutions, analytics and All-India rank for the 2026 cycle.',
   49900, 99900, 365,
   '["All UPSC & BPSC mock tests","Detailed solutions with explanations","Question-wise time & accuracy analytics","All-India rank and percentile","Valid till the 2026 Prelims"]'::jsonb,
   1)
on conflict (code) do nothing;

-- ---------------------------------------------------------------------------
-- 3. COURSES / BATCHES / TEST SERIES / TESTS — content hierarchy.
-- ---------------------------------------------------------------------------
alter table public.courses
  add column if not exists description   text,
  add column if not exists exam_target   text,
  add column if not exists is_published  boolean not null default false,
  add column if not exists created_by    uuid references auth.users(id) on delete set null,
  add column if not exists created_at    timestamptz not null default now();

alter table public.batches
  add column if not exists course_id   uuid references public.courses(id) on delete cascade,
  add column if not exists price       numeric(10,2) not null default 0,
  add column if not exists seat_limit  integer,
  add column if not exists start_date  date,
  add column if not exists end_date    date,
  add column if not exists is_active   boolean not null default true,
  add column if not exists created_at  timestamptz not null default now();

alter table public.test_series
  add column if not exists description text,
  add column if not exists batch_id    uuid references public.batches(id) on delete set null,
  add column if not exists price       numeric(10,2) not null default 0,
  add column if not exists is_free     boolean not null default false,
  add column if not exists created_by  uuid references auth.users(id) on delete set null,
  add column if not exists created_at  timestamptz not null default now();

alter table public.tests
  add column if not exists series_id        uuid references public.test_series(id) on delete set null,
  add column if not exists description      text,
  add column if not exists duration_min     integer not null default 60,
  add column if not exists sections         jsonb   not null default '[]'::jsonb,
  add column if not exists is_free          boolean not null default false,
  add column if not exists is_published     boolean not null default false,
  add column if not exists shuffle_questions boolean not null default false,
  add column if not exists shuffle_options   boolean not null default false,
  add column if not exists scheduled_for    timestamptz,
  add column if not exists total_questions  integer not null default 0,
  add column if not exists total_marks      numeric(8,2) not null default 0,
  add column if not exists created_by       uuid references auth.users(id) on delete set null,
  add column if not exists created_at       timestamptz not null default now(),
  add column if not exists updated_at       timestamptz not null default now();

-- `sections` is [{ id, name, questionIds: [uuid] }]. Keep the denormalised
-- counters honest so listing screens never have to load every question.
create or replace function public.sync_test_counters()
returns trigger
language plpgsql
as $$
declare
  ids uuid[];
begin
  select coalesce(array_agg(qid::uuid), '{}')
    into ids
  from jsonb_array_elements(coalesce(new.sections, '[]'::jsonb)) sec,
       jsonb_array_elements_text(coalesce(sec -> 'questionIds', '[]'::jsonb)) qid;

  new.total_questions := coalesce(array_length(ids, 1), 0);
  select coalesce(sum(marks_correct), 0) into new.total_marks
    from public.questions where id = any(ids);
  new.updated_at := now();
  return new;
end;
$$;

drop trigger if exists tests_sync_counters on public.tests;
create trigger tests_sync_counters
  before insert or update of sections on public.tests
  for each row execute function public.sync_test_counters();

-- ---------------------------------------------------------------------------
-- 4. QUESTIONS
-- ---------------------------------------------------------------------------
alter table public.questions
  add column if not exists topic             text,
  add column if not exists difficulty        text not null default 'medium',
  add column if not exists options           jsonb not null default '[]'::jsonb,
  add column if not exists explanation       text,
  add column if not exists marks_correct     numeric(6,2) not null default 2,
  add column if not exists marks_wrong       numeric(6,2) not null default 0.66,
  add column if not exists numeric_answer    numeric,
  add column if not exists numeric_tolerance numeric not null default 0.01,
  add column if not exists tags              text[] not null default '{}',
  add column if not exists source_year       integer,
  add column if not exists is_active         boolean not null default true,
  add column if not exists created_by        uuid references auth.users(id) on delete set null,
  add column if not exists created_at        timestamptz not null default now(),
  add column if not exists updated_at        timestamptz not null default now();

do $$ begin
  alter table public.questions
    add constraint questions_type_chk check (type in ('mcq', 'multiple', 'numerical'));
exception when duplicate_object then null; end $$;

do $$ begin
  alter table public.questions
    add constraint questions_difficulty_chk check (difficulty in ('easy', 'medium', 'hard'));
exception when duplicate_object then null; end $$;

create index if not exists questions_subject_idx    on public.questions (subject);
create index if not exists questions_difficulty_idx on public.questions (difficulty);
create index if not exists questions_active_idx     on public.questions (is_active) where is_active;

-- ---------------------------------------------------------------------------
-- 5. ENROLLMENTS — what actually unlocks the product for a student.
--    The app previously queried `user_id`/`expires_at`, neither of which
--    existed, so *every* access check silently failed. Both are added here and
--    `student_id` stays the canonical key.
-- ---------------------------------------------------------------------------
alter table public.enrollments
  add column if not exists student_id  uuid references auth.users(id) on delete cascade,
  add column if not exists batch_id    uuid references public.batches(id) on delete set null,
  add column if not exists plan_code   text references public.plans(code) on delete set null,
  add column if not exists source      text not null default 'purchase',
  add column if not exists status      text not null default 'active',
  add column if not exists expires_at  timestamptz,          -- null = never expires
  add column if not exists enrolled_at timestamptz not null default now(),
  add column if not exists created_at  timestamptz not null default now();

do $$ begin
  alter table public.enrollments
    add constraint enrollments_status_chk check (status in ('active', 'cancelled', 'refunded'));
exception when duplicate_object then null; end $$;

-- NULLS NOT DISTINCT (PG15+) so a plan-only enrollment (batch_id null) still
-- collides with itself — that is what makes the payment webhook idempotent.
create unique index if not exists enrollments_student_plan_uidx
  on public.enrollments (student_id, plan_code, batch_id) nulls not distinct;

create index if not exists enrollments_student_idx on public.enrollments (student_id);

-- ---------------------------------------------------------------------------
-- 6. ATTEMPTS — one row per test a student sits, with the full analysis.
-- ---------------------------------------------------------------------------
alter table public.attempts
  add column if not exists student_id     uuid references auth.users(id) on delete cascade,
  add column if not exists test_id        uuid references public.tests(id) on delete set null,
  add column if not exists test_title     text,
  add column if not exists series_title   text,
  add column if not exists score          numeric(8,2) not null default 0,
  add column if not exists max_score      numeric(8,2) not null default 0,
  add column if not exists total_questions integer not null default 0,
  add column if not exists correct_count  integer not null default 0,
  add column if not exists wrong_count    integer not null default 0,
  add column if not exists accuracy       numeric(5,2) not null default 0,
  add column if not exists percentile     numeric(5,2),
  add column if not exists rank_in_test   integer,
  add column if not exists total_peers    integer,
  add column if not exists time_taken_sec integer not null default 0,
  add column if not exists duration_min   integer not null default 0,
  add column if not exists answers        jsonb not null default '{}'::jsonb,
  add column if not exists section_stats  jsonb not null default '[]'::jsonb,
  add column if not exists topic_stats    jsonb not null default '[]'::jsonb,
  add column if not exists review         jsonb not null default '[]'::jsonb,
  add column if not exists status         text not null default 'submitted',
  add column if not exists started_at     timestamptz not null default now(),
  add column if not exists submitted_at   timestamptz;

do $$ begin
  alter table public.attempts
    add constraint attempts_status_chk check (status in ('in_progress', 'submitted', 'abandoned'));
exception when duplicate_object then null; end $$;

create index if not exists attempts_student_idx   on public.attempts (student_id, submitted_at desc);
create index if not exists attempts_test_idx      on public.attempts (test_id);

-- ---------------------------------------------------------------------------
-- 7. PAYMENTS — every Razorpay interaction, verified server-side only.
-- ---------------------------------------------------------------------------
alter table public.payments
  add column if not exists user_id             uuid references auth.users(id) on delete set null,
  add column if not exists plan_code           text references public.plans(code) on delete set null,
  add column if not exists amount              numeric(10,2) not null default 0,
  add column if not exists currency            text not null default 'INR',
  add column if not exists status              text not null default 'created',
  add column if not exists razorpay_order_id   text,
  add column if not exists razorpay_payment_id text,
  add column if not exists razorpay_signature  text,
  add column if not exists method              text,
  add column if not exists notes               jsonb not null default '{}'::jsonb,
  add column if not exists failure_reason      text,
  add column if not exists verified_at         timestamptz,
  add column if not exists created_at          timestamptz not null default now();

do $$ begin
  alter table public.payments
    add constraint payments_status_chk check (status in ('created', 'paid', 'failed', 'refunded'));
exception when duplicate_object then null; end $$;

-- Idempotency: Razorpay retries webhooks, and the client also confirms. Both
-- paths converge on the same row instead of double-crediting.
create unique index if not exists payments_order_uidx
  on public.payments (razorpay_order_id) where razorpay_order_id is not null;

create index if not exists payments_user_idx on public.payments (user_id, created_at desc);

-- ---------------------------------------------------------------------------
-- 8. MATERIALS
-- ---------------------------------------------------------------------------
alter table public.materials
  add column if not exists description  text,
  add column if not exists subject      text,
  add column if not exists type         text not null default 'pdf',
  add column if not exists url          text,
  add column if not exists batch_id     uuid references public.batches(id) on delete set null,
  add column if not exists is_free      boolean not null default true,
  add column if not exists is_published boolean not null default true,
  add column if not exists sort_order   integer not null default 0,
  add column if not exists created_at   timestamptz not null default now();

do $$ begin
  alter table public.materials
    add constraint materials_type_chk check (type in ('pdf', 'note', 'video', 'link'));
exception when duplicate_object then null; end $$;

-- ---------------------------------------------------------------------------
-- 9. NOTIFICATIONS
-- ---------------------------------------------------------------------------
alter table public.notifications
  add column if not exists user_id    uuid references auth.users(id) on delete cascade,
  add column if not exists title      text not null default '',
  add column if not exists body       text,
  add column if not exists kind       text not null default 'info',
  add column if not exists link       text,
  add column if not exists read_at    timestamptz,
  add column if not exists created_at timestamptz not null default now();

create index if not exists notifications_user_idx on public.notifications (user_id, created_at desc);

-- ---------------------------------------------------------------------------
-- 10. NEW: bookmarks, reminders, study activity.
-- ---------------------------------------------------------------------------
create table if not exists public.bookmarks (
  id          uuid primary key default gen_random_uuid(),
  student_id  uuid not null references auth.users(id) on delete cascade,
  question_id uuid not null references public.questions(id) on delete cascade,
  note        text,
  created_at  timestamptz not null default now(),
  unique (student_id, question_id)
);

create table if not exists public.test_reminders (
  id         uuid primary key default gen_random_uuid(),
  student_id uuid not null references auth.users(id) on delete cascade,
  test_id    uuid not null references public.tests(id) on delete cascade,
  created_at timestamptz not null default now(),
  unique (student_id, test_id)
);

-- Powers the streak + 12-week heatmap without recomputing from attempts.
create table if not exists public.study_activity (
  student_id uuid not null references auth.users(id) on delete cascade,
  day        date not null,
  count      integer not null default 0,
  primary key (student_id, day)
);

create or replace function public.log_study_activity()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  if new.status = 'submitted' and new.student_id is not null then
    insert into public.study_activity (student_id, day, count)
    values (new.student_id, (coalesce(new.submitted_at, now()) at time zone 'Asia/Kolkata')::date, 1)
    on conflict (student_id, day) do update set count = public.study_activity.count + 1;
  end if;
  return new;
end;
$$;

drop trigger if exists attempts_log_activity on public.attempts;
create trigger attempts_log_activity
  after insert on public.attempts
  for each row execute function public.log_study_activity();

-- ---------------------------------------------------------------------------
-- 11. LEADERBOARD — a real, computed ranking (no more hardcoded names).
-- ---------------------------------------------------------------------------
create or replace view public.leaderboard_v
with (security_invoker = true) as
select
  p.id                                         as student_id,
  coalesce(nullif(trim(p.full_name), ''), 'Aspirant') as name,
  p.avatar_url,
  count(a.id)::int                             as tests_taken,
  round(avg(case when a.max_score > 0 then a.score / a.max_score * 100 else 0 end)::numeric, 1) as avg_pct,
  round(max(case when a.max_score > 0 then a.score / a.max_score * 100 else 0 end)::numeric, 1) as best_pct,
  round(avg(a.accuracy)::numeric, 1)           as avg_accuracy,
  rank() over (
    order by avg(case when a.max_score > 0 then a.score / a.max_score * 100 else 0 end) desc,
             count(a.id) desc
  )::int                                       as rank
from public.profiles p
join public.attempts a
  on a.student_id = p.id and a.status = 'submitted'
where p.role = 'student'
group by p.id, p.full_name, p.avatar_url;

-- Percentile/rank for a single attempt, against everyone who took that test.
create or replace function public.attempt_standing(p_attempt uuid)
returns table (rank int, total int, percentile numeric)
language sql
stable
security definer
set search_path = public
as $$
  with target as (
    select test_id, score from public.attempts where id = p_attempt
  ),
  peers as (
    select a.id, a.score
    from public.attempts a, target t
    where a.test_id = t.test_id and a.status = 'submitted'
  )
  select
    (select count(*) + 1 from peers p, target t where p.score > t.score)::int,
    (select count(*) from peers)::int,
    case when (select count(*) from peers) <= 1 then 100::numeric
         else round(
           (select count(*) from peers p, target t where p.score <= t.score)::numeric
           / (select count(*) from peers)::numeric * 100, 1)
    end;
$$;

-- ---------------------------------------------------------------------------
-- 12. ROW LEVEL SECURITY
-- ---------------------------------------------------------------------------
alter table public.profiles       enable row level security;
alter table public.plans          enable row level security;
alter table public.courses        enable row level security;
alter table public.batches        enable row level security;
alter table public.test_series    enable row level security;
alter table public.tests          enable row level security;
alter table public.questions      enable row level security;
alter table public.enrollments    enable row level security;
alter table public.attempts       enable row level security;
alter table public.payments       enable row level security;
alter table public.materials      enable row level security;
alter table public.notifications  enable row level security;
alter table public.bookmarks      enable row level security;
alter table public.test_reminders enable row level security;
alter table public.study_activity enable row level security;

-- Helper so re-running the migration replaces policies cleanly.
do $$
declare r record;
begin
  for r in
    select schemaname, tablename, policyname
    from pg_policies
    where schemaname = 'public'
      and tablename in ('profiles','plans','courses','batches','test_series','tests',
                        'questions','enrollments','attempts','payments','materials',
                        'notifications','bookmarks','test_reminders','study_activity')
  loop
    execute format('drop policy %I on %I.%I', r.policyname, r.schemaname, r.tablename);
  end loop;
end $$;

-- profiles: read your own (and admins read all); update only your own.
create policy profiles_select on public.profiles for select
  using (id = auth.uid() or public.is_admin());
create policy profiles_update on public.profiles for update
  using (id = auth.uid() or public.is_admin())
  with check (id = auth.uid() or public.is_admin());
create policy profiles_insert on public.profiles for insert
  with check (id = auth.uid());

-- plans: public price list; admin-managed.
create policy plans_select on public.plans for select using (is_active or public.is_admin());
create policy plans_admin  on public.plans for all using (public.is_admin()) with check (public.is_admin());

-- Catalogue: signed-in users see published items, admins see everything.
create policy courses_select on public.courses for select
  using (is_published or public.is_admin());
create policy courses_admin on public.courses for all
  using (public.is_admin()) with check (public.is_admin());

create policy batches_select on public.batches for select
  using (is_active or public.is_admin());
create policy batches_admin on public.batches for all
  using (public.is_admin()) with check (public.is_admin());

create policy series_select on public.test_series for select using (true);
create policy series_admin  on public.test_series for all
  using (public.is_admin()) with check (public.is_admin());

create policy tests_select on public.tests for select
  using (is_published or public.is_admin());
create policy tests_admin on public.tests for all
  using (public.is_admin()) with check (public.is_admin());

-- Questions: readable by any signed-in user (the paywall is enforced by which
-- *tests* a student can start, and free tests are meant to be sampled), but
-- only admins can write.
create policy questions_select on public.questions for select
  using (auth.uid() is not null and (is_active or public.is_admin()));
create policy questions_admin on public.questions for all
  using (public.is_admin()) with check (public.is_admin());

-- Enrollments are granted by the payment webhook (service role) only. A student
-- can read their own; nobody can self-insert one.
create policy enrollments_select on public.enrollments for select
  using (student_id = auth.uid() or public.is_admin());
create policy enrollments_admin on public.enrollments for all
  using (public.is_admin()) with check (public.is_admin());

-- Attempts: a student owns their own; admins can read all for analytics.
create policy attempts_select on public.attempts for select
  using (student_id = auth.uid() or public.is_admin());
create policy attempts_insert on public.attempts for insert
  with check (student_id = auth.uid());
create policy attempts_update on public.attempts for update
  using (student_id = auth.uid()) with check (student_id = auth.uid());
create policy attempts_admin_all on public.attempts for all
  using (public.is_admin()) with check (public.is_admin());

-- Payments are written exclusively by edge functions running as service_role.
create policy payments_select on public.payments for select
  using (user_id = auth.uid() or public.is_admin());
create policy payments_admin on public.payments for all
  using (public.is_admin()) with check (public.is_admin());

-- Materials: free ones are open to signed-in users; paid ones need an
-- active enrollment on the owning batch.
create policy materials_select on public.materials for select
  using (
    public.is_admin()
    or (is_published and auth.uid() is not null and (
      is_free
      or exists (
        select 1 from public.enrollments e
        where e.student_id = auth.uid()
          and e.status = 'active'
          and (e.expires_at is null or e.expires_at > now())
          and (e.batch_id is null or e.batch_id = public.materials.batch_id)
      )
    ))
  );
create policy materials_admin on public.materials for all
  using (public.is_admin()) with check (public.is_admin());

create policy notifications_select on public.notifications for select
  using (user_id = auth.uid() or user_id is null or public.is_admin());
create policy notifications_update on public.notifications for update
  using (user_id = auth.uid()) with check (user_id = auth.uid());
create policy notifications_admin on public.notifications for all
  using (public.is_admin()) with check (public.is_admin());

create policy bookmarks_own on public.bookmarks for all
  using (student_id = auth.uid()) with check (student_id = auth.uid());

create policy reminders_own on public.test_reminders for all
  using (student_id = auth.uid()) with check (student_id = auth.uid());

create policy activity_select on public.study_activity for select
  using (student_id = auth.uid() or public.is_admin());

-- ---------------------------------------------------------------------------
-- 13. Grants (RLS still applies on top of these).
-- ---------------------------------------------------------------------------
grant usage on schema public to anon, authenticated;
grant select on public.leaderboard_v to authenticated;
grant execute on function public.attempt_standing(uuid) to authenticated;
grant execute on function public.is_admin() to authenticated;


-- ============================================================================
-- Storage buckets.
--
-- Before this, study material could only be a pasted external link, and a
-- student's profile photo was stored as a base-64 data URL inside the profiles
-- row (a 3 MB image became a ~4 MB text column, sent on every profile read).
-- ============================================================================

-- Study material: PDFs, notes and video files an admin uploads.
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values (
  'materials', 'materials', true, 52428800,   -- 50 MB
  array['application/pdf','image/png','image/jpeg','image/webp',
        'video/mp4','video/webm','text/plain',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document']
)
on conflict (id) do update
  set public = excluded.public,
      file_size_limit = excluded.file_size_limit,
      allowed_mime_types = excluded.allowed_mime_types;

-- Profile photos.
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('avatars', 'avatars', true, 3145728,   -- 3 MB
        array['image/png','image/jpeg','image/webp','image/gif'])
on conflict (id) do update
  set public = excluded.public,
      file_size_limit = excluded.file_size_limit,
      allowed_mime_types = excluded.allowed_mime_types;

-- Reset policies so this migration is re-runnable.
do $$
declare r record;
begin
  for r in
    select policyname from pg_policies
    where schemaname = 'storage' and tablename = 'objects'
      and policyname like 'jn_%'
  loop
    execute format('drop policy %I on storage.objects', r.policyname);
  end loop;
end $$;

-- Materials: world-readable (the bucket is public and links are unguessable),
-- writable only by admins.
create policy jn_materials_read on storage.objects for select
  using (bucket_id = 'materials');
create policy jn_materials_write on storage.objects for insert
  with check (bucket_id = 'materials' and public.is_admin());
create policy jn_materials_update on storage.objects for update
  using (bucket_id = 'materials' and public.is_admin())
  with check (bucket_id = 'materials' and public.is_admin());
create policy jn_materials_delete on storage.objects for delete
  using (bucket_id = 'materials' and public.is_admin());

-- Avatars: readable by anyone, but a user may only write inside a folder named
-- after their own user id — so nobody can overwrite someone else's photo.
create policy jn_avatars_read on storage.objects for select
  using (bucket_id = 'avatars');
create policy jn_avatars_write on storage.objects for insert
  with check (bucket_id = 'avatars' and (storage.foldername(name))[1] = auth.uid()::text);
create policy jn_avatars_update on storage.objects for update
  using (bucket_id = 'avatars' and (storage.foldername(name))[1] = auth.uid()::text)
  with check (bucket_id = 'avatars' and (storage.foldername(name))[1] = auth.uid()::text);
create policy jn_avatars_delete on storage.objects for delete
  using (bucket_id = 'avatars' and (storage.foldername(name))[1] = auth.uid()::text);

-- ==========================================================================
-- LAST STEP: make yourself an admin (there is deliberately no way to do
-- this from the browser). Keyed on auth.users, NOT profiles.email, so it
-- works even if the profile row was never populated:
-- ==========================================================================
-- update public.profiles p set role = 'admin'
--   from auth.users u
--  where u.id = p.id and u.email = 'praveenpriyadarshee@gmail.com';
