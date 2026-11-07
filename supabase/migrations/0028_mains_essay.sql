-- ============================================================================
-- JUNOONIAS — Mains, slice 1: essay PYQs, themes and topper copies.
--
-- The first piece of the Mains module (docs/upsc-essay-design.md). A student
-- picks an essay theme, sees UPSC's essay topics in it, and opens the topper
-- essays written on that topic -- each one at the page where the essay starts,
-- not on the cover of a 30-page scan.
--
-- Built around the spreadsheets we already keep, so they import as-is
-- (src/lib/mainsImport.js reads their CSV exports):
--   * essay PYQ + year, with two categories and a confidence for each
--   * subject, topper, rank, coaching, question, page, and a public PDF link
--     ending in #page=N
--   * a copy's essay topic and its similar PYQs, with confidence
--
-- What lives where:
--   essay_themes        the categories, bilingual, optionally grouped
--   essay_pyqs          UPSC essay topics by year
--   essay_pyq_themes    a PYQ's themes with confidence; the highest is its main
--                       theme, the rest are "also under"
--   toppers             who wrote a copy: rank, CSE year, real UPSC Essay score
--   topper_copies       one copy. Either a LINK (source_url, opened at the page
--                       in a new tab) or HOSTED (pages rendered to WebP in the
--                       private copy-pages bucket and read in the app), or both
--   topper_answers      one answer inside a copy, for any Mains paper, with its
--                       start page. Paper-agnostic so GS rows can be imported
--                       now; only paper = 'essay' is shown today
--   essay_answer_pyqs   which essay PYQs an essay answers: exact or related
--   essay_topic_map     "this mock topic is similar to that PYQ", imported from
--                       the similar-PYQ sheet; essay_autolink() turns it into
--                       links for every answer on that topic
--
-- Access. Themes and PYQs are public -- they are UPSC's own questions. Copy
-- metadata needs a session, so the locked state can say what a bundle adds.
-- Hosted page images are the protected part: storage only signs a URL when
-- can_read_topper_copy() passes (admin, tester, a free copy, or a live
-- enrollment on any plan with includes_mains). Which bundles include Mains is
-- a checkbox in Bundles & Pricing, not a code change. A LINK copy points at a
-- PDF that is already public on its publisher's site, so its URL is readable
-- by any signed-in student and the lock on it is presentational only.
--
-- Idempotent, like 0001: safe to re-run.
-- ============================================================================

-- ---------------------------------------------------------------------------
-- 0. Text key. Two spellings of one topic ("Q.1) Truth knows no color." and
--    "truth knows no colour") must meet. Lowercase, letters and digits only.
--    English text only -- a Hindi-only string keys to null, by design.
-- ---------------------------------------------------------------------------
create or replace function public.essay_key(p text)
returns text
language sql
immutable
as $$
  select nullif(regexp_replace(lower(coalesce(p, '')), '[^a-z0-9]+', '', 'g'), '');
$$;

-- ---------------------------------------------------------------------------
-- 1. Bundles: which plans include Mains.
-- ---------------------------------------------------------------------------
alter table public.plans
  add column if not exists includes_mains boolean not null default false;

-- ---------------------------------------------------------------------------
-- 2. Themes and PYQs.
-- ---------------------------------------------------------------------------
create table if not exists public.essay_themes (
  id          uuid primary key default gen_random_uuid(),
  slug        text not null unique,
  name        text not null,
  name_hi     text,
  parent_id   uuid references public.essay_themes(id) on delete set null,
  sort_order  integer not null default 0,
  created_at  timestamptz not null default now()
);

create table if not exists public.essay_pyqs (
  id           uuid primary key default gen_random_uuid(),
  year         integer not null check (year between 1990 and 2100),
  q_no         integer,
  section      text,                         -- 'A' / 'B' where the paper has them
  topic        text not null,
  topic_hi     text,
  topic_key    text generated always as (public.essay_key(topic)) stored,
  is_published boolean not null default true,
  created_at   timestamptz not null default now(),
  updated_at   timestamptz not null default now(),
  constraint essay_pyqs_year_topic_uniq unique (year, topic_key)
);
create index if not exists essay_pyqs_year_idx on public.essay_pyqs (year desc);
create index if not exists essay_pyqs_key_idx on public.essay_pyqs (topic_key);

create table if not exists public.essay_pyq_themes (
  pyq_id     uuid not null references public.essay_pyqs(id) on delete cascade,
  theme_id   uuid not null references public.essay_themes(id) on delete cascade,
  confidence smallint check (confidence between 0 and 100),
  primary key (pyq_id, theme_id)
);
create index if not exists essay_pyq_themes_theme_idx on public.essay_pyq_themes (theme_id);

-- ---------------------------------------------------------------------------
-- 3. Toppers, copies and the answers inside them.
-- ---------------------------------------------------------------------------
create table if not exists public.toppers (
  id          uuid primary key default gen_random_uuid(),
  name        text not null,
  name_key    text generated always as (public.essay_key(name)) stored,
  rank        integer,                       -- best/latest AIR we show
  cse_year    integer,                       -- the CSE year of that rank
  essay_marks integer check (essay_marks between 0 and 250),
  note        text,                          -- e.g. the raw "217, 267, 297"
  created_at  timestamptz not null default now(),
  constraint toppers_name_key_uniq unique (name_key)
);

create table if not exists public.topper_copies (
  id           uuid primary key default gen_random_uuid(),
  topper_id    uuid not null references public.toppers(id) on delete restrict,
  source       text,                         -- 'Forum IAS', 'Vision IAS', ...
  title        text,                         -- optional label, e.g. the file name
  written_year integer,
  source_url   text,                         -- public PDF, without #page
  page_count   integer not null default 0,
  pages_ready  boolean not null default false,
  sha256       text,
  pdf_path     text,
  is_free      boolean not null default false,
  is_published boolean not null default true,
  created_by   uuid references auth.users(id) on delete set null,
  created_at   timestamptz not null default now(),
  updated_at   timestamptz not null default now(),
  constraint topper_copies_url_uniq unique (source_url),
  constraint topper_copies_sha_uniq unique (sha256)
);
create index if not exists topper_copies_topper_idx on public.topper_copies (topper_id);

create table if not exists public.topper_answers (
  id           uuid primary key default gen_random_uuid(),
  copy_id      uuid not null references public.topper_copies(id) on delete cascade,
  paper        text not null default 'essay'
               check (paper in ('essay', 'gs1', 'gs2', 'gs3', 'gs4', 'optional', 'other')),
  paper_label  text,                         -- the sheet's own label, e.g. 'Sociology'
  question     text not null,
  question_key text generated always as (public.essay_key(question)) stored,
  start_page   integer check (start_page >= 1),
  end_page     integer,
  page_key     integer generated always as (coalesce(start_page, 0)) stored,
  sort_order   integer not null default 0,
  created_at   timestamptz not null default now(),
  constraint topper_answers_pages_chk check (end_page is null or start_page is null or end_page >= start_page),
  constraint topper_answers_uniq unique (copy_id, question_key, page_key)
);
create index if not exists topper_answers_copy_idx on public.topper_answers (copy_id);
create index if not exists topper_answers_paper_key_idx on public.topper_answers (paper, question_key);

create table if not exists public.essay_answer_pyqs (
  answer_id  uuid not null references public.topper_answers(id) on delete cascade,
  pyq_id     uuid not null references public.essay_pyqs(id) on delete cascade,
  kind       text not null check (kind in ('exact', 'related')),
  confidence smallint check (confidence between 0 and 100),
  primary key (answer_id, pyq_id)
);
create index if not exists essay_answer_pyqs_pyq_idx on public.essay_answer_pyqs (pyq_id);

create table if not exists public.essay_topic_map (
  topic_key  text not null,
  topic      text not null,
  pyq_id     uuid not null references public.essay_pyqs(id) on delete cascade,
  confidence smallint check (confidence between 0 and 100),
  primary key (topic_key, pyq_id)
);

-- ---------------------------------------------------------------------------
-- 4. Entitlement.
-- ---------------------------------------------------------------------------

/* Does this user hold Mains? Admin, tester, or a live enrollment on any plan
   that includes it. p_user is a parameter for the same reason is_tester() has
   one (0020): an edge function can pass the id it already validated. */
create or replace function public.has_mains_access(p_user uuid default auth.uid())
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select public.is_admin()
      or public.is_tester(p_user)
      or exists (
        select 1
        from public.enrollments e
        join public.plans p on p.code = e.plan_code
        where e.student_id = p_user
          and e.status = 'active'
          and (e.expires_at is null or e.expires_at > now())
          and p.includes_mains
      );
$$;

/* May the caller read this copy's hosted pages? */
create or replace function public.can_read_topper_copy(p_copy uuid)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select public.is_admin()
      or exists (
        select 1 from public.topper_copies c
        where c.id = p_copy
          and c.is_published
          and (c.is_free or public.has_mains_access())
      );
$$;

/* Storage policies see a folder name, not a uuid. A malformed name must
   answer false, not raise -- a cast error inside a policy fails the request. */
create or replace function public.can_read_copy_folder(p_folder text)
returns boolean
language plpgsql
stable
security definer
set search_path = public
as $$
begin
  if p_folder is null
     or p_folder !~* '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$' then
    return false;
  end if;
  return public.can_read_topper_copy(p_folder::uuid);
end;
$$;

grant execute on function public.essay_key(text) to anon, authenticated, service_role;
grant execute on function public.has_mains_access(uuid) to anon, authenticated, service_role;
grant execute on function public.can_read_topper_copy(uuid) to anon, authenticated, service_role;
grant execute on function public.can_read_copy_folder(text) to anon, authenticated, service_role;

-- ---------------------------------------------------------------------------
-- 5. Linking. Exact: the answer's topic is the PYQ's topic. Related: the
--    similar-PYQ map says so. Idempotent -- links an admin removed by hand
--    come back only if the source data still says they belong.
-- ---------------------------------------------------------------------------
create or replace function public.essay_autolink()
returns jsonb
language plpgsql
security definer
set search_path = public
as $$
declare
  n_exact   integer := 0;
  n_related integer := 0;
begin
  if not public.is_admin() then
    raise exception 'admin_only';
  end if;

  insert into public.essay_answer_pyqs (answer_id, pyq_id, kind, confidence)
  select a.id, p.id, 'exact', 100
  from public.topper_answers a
  join public.essay_pyqs p on p.topic_key = a.question_key
  where a.paper = 'essay' and a.question_key is not null
  on conflict (answer_id, pyq_id) do nothing;
  get diagnostics n_exact = row_count;

  insert into public.essay_answer_pyqs (answer_id, pyq_id, kind, confidence)
  select a.id, m.pyq_id, 'related', m.confidence
  from public.topper_answers a
  join public.essay_topic_map m on m.topic_key = a.question_key
  where a.paper = 'essay'
  on conflict (answer_id, pyq_id) do nothing;
  get diagnostics n_related = row_count;

  return jsonb_build_object('exact', n_exact, 'related', n_related);
end;
$$;

grant execute on function public.essay_autolink() to authenticated;

-- ---------------------------------------------------------------------------
-- 6. Views. security_invoker, so the caller's row-level security applies: a
--    student sees published copies only.
-- ---------------------------------------------------------------------------
create or replace view public.topper_library_v
with (security_invoker = true) as
select
  a.id           as answer_id,
  a.paper,
  a.paper_label,
  a.question,
  a.start_page,
  a.end_page,
  c.id           as copy_id,
  c.source,
  c.title,
  c.written_year,
  c.source_url,
  c.page_count,
  c.pages_ready,
  c.is_free,
  c.is_published,
  t.id           as topper_id,
  t.name         as topper_name,
  t.rank         as topper_rank,
  t.cse_year,
  t.essay_marks
from public.topper_answers a
join public.topper_copies c on c.id = a.copy_id
join public.toppers t on t.id = c.topper_id;

create or replace view public.essay_pyq_stats_v
with (security_invoker = true) as
select
  ap.pyq_id,
  count(*)                                   as essay_count,
  count(*) filter (where ap.kind = 'exact')  as exact_count
from public.essay_answer_pyqs ap
join public.topper_answers a on a.id = ap.answer_id
join public.topper_copies c on c.id = a.copy_id
where c.is_published
group by ap.pyq_id;

-- ---------------------------------------------------------------------------
-- 7. Row-level security.
-- ---------------------------------------------------------------------------
alter table public.essay_themes      enable row level security;
alter table public.essay_pyqs        enable row level security;
alter table public.essay_pyq_themes  enable row level security;
alter table public.toppers           enable row level security;
alter table public.topper_copies     enable row level security;
alter table public.topper_answers    enable row level security;
alter table public.essay_answer_pyqs enable row level security;
alter table public.essay_topic_map   enable row level security;

do $$
declare r record;
begin
  for r in select policyname, tablename from pg_policies
           where schemaname = 'public'
             and tablename in ('essay_themes', 'essay_pyqs', 'essay_pyq_themes', 'toppers',
                               'topper_copies', 'topper_answers', 'essay_answer_pyqs', 'essay_topic_map')
  loop execute format('drop policy %I on public.%I', r.policyname, r.tablename); end loop;
end $$;

-- Public: UPSC's own questions and our taxonomy of them.
create policy essay_themes_read  on public.essay_themes for select using (true);
create policy essay_themes_admin on public.essay_themes for all
  using (public.is_admin()) with check (public.is_admin());

create policy essay_pyqs_read  on public.essay_pyqs for select using (is_published or public.is_admin());
create policy essay_pyqs_admin on public.essay_pyqs for all
  using (public.is_admin()) with check (public.is_admin());

create policy essay_pyq_themes_read  on public.essay_pyq_themes for select using (true);
create policy essay_pyq_themes_admin on public.essay_pyq_themes for all
  using (public.is_admin()) with check (public.is_admin());

-- Signed-in: who wrote what, and where it starts.
create policy toppers_read  on public.toppers for select using (auth.uid() is not null);
create policy toppers_admin on public.toppers for all
  using (public.is_admin()) with check (public.is_admin());

create policy topper_copies_read on public.topper_copies for select
  using ((auth.uid() is not null and is_published) or public.is_admin());
create policy topper_copies_admin on public.topper_copies for all
  using (public.is_admin()) with check (public.is_admin());

create policy topper_answers_read on public.topper_answers for select
  using (public.is_admin() or (auth.uid() is not null and exists (
    select 1 from public.topper_copies c where c.id = copy_id and c.is_published)));
create policy topper_answers_admin on public.topper_answers for all
  using (public.is_admin()) with check (public.is_admin());

create policy essay_answer_pyqs_read on public.essay_answer_pyqs for select
  using (public.is_admin() or (auth.uid() is not null and exists (
    select 1 from public.topper_answers a
    join public.topper_copies c on c.id = a.copy_id
    where a.id = answer_id and c.is_published)));
create policy essay_answer_pyqs_admin on public.essay_answer_pyqs for all
  using (public.is_admin()) with check (public.is_admin());

-- Admin working data.
create policy essay_topic_map_admin on public.essay_topic_map for all
  using (public.is_admin()) with check (public.is_admin());

-- ---------------------------------------------------------------------------
-- 8. Storage. Both buckets are private (public = false): nothing in them has
--    a permanent URL. Page images are signed per request for ten minutes.
-- ---------------------------------------------------------------------------
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('copy-pages', 'copy-pages', false, 5242880,          -- 5 MB per page image
        array['image/webp', 'image/jpeg', 'image/png'])
on conflict (id) do update
  set public = excluded.public,
      file_size_limit = excluded.file_size_limit,
      allowed_mime_types = excluded.allowed_mime_types;

insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('copy-pdfs', 'copy-pdfs', false, 52428800,           -- 50 MB, as materials
        array['application/pdf'])
on conflict (id) do update
  set public = excluded.public,
      file_size_limit = excluded.file_size_limit,
      allowed_mime_types = excluded.allowed_mime_types;

-- Named copy_* rather than jn_*: 0002 drops every jn_% storage policy when it
-- is re-run, and these must survive that.
do $$
declare r record;
begin
  for r in select policyname from pg_policies
           where schemaname = 'storage' and tablename = 'objects' and policyname like 'copy\_%'
  loop execute format('drop policy %I on storage.objects', r.policyname); end loop;
end $$;

create policy copy_pages_read on storage.objects for select
  using (bucket_id = 'copy-pages' and public.can_read_copy_folder((storage.foldername(name))[1]));
create policy copy_pages_insert on storage.objects for insert
  with check (bucket_id = 'copy-pages' and public.is_admin());
create policy copy_pages_update on storage.objects for update
  using (bucket_id = 'copy-pages' and public.is_admin())
  with check (bucket_id = 'copy-pages' and public.is_admin());
create policy copy_pages_delete on storage.objects for delete
  using (bucket_id = 'copy-pages' and public.is_admin());

create policy copy_pdfs_admin on storage.objects for all
  using (bucket_id = 'copy-pdfs' and public.is_admin())
  with check (bucket_id = 'copy-pdfs' and public.is_admin());
