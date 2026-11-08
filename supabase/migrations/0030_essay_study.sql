-- ============================================================================
-- JUNOONIAS — Mains: study tools around the essay library.
--
--   essay_marks          a student's star and "done" on a PYQ, an essay or a
--                        wiki snippet. done_at is stamped by the database, so
--                        a streak cannot be back-filled from the browser
--   essay_notes          a student's own notes, on an item or free-standing
--   essay_reads          one row per student, essay and day read: streaks for
--                        the student, reader counts for everyone (counts only)
--   essay_snippets       the Essay Wiki: openings, closings, quotes, anecdotes,
--                        examples and statistics taken verbatim from a topper's
--                        essay. They ARE the copy, so they sit behind its lock
--   essay_snippet_fits   which PYQs a snippet suits, with how to use it there
--   essay_ltw            Learn to Write: one guide per PYQ (spine, sides,
--                        arguments with model paragraphs, introductions,
--                        conclusions, pitfalls), citing the toppers' essays.
--                        Mains holders read it; others get a preview
--
-- Wiki and Learn to Write rows start as drafts; students see only published
-- ones. Depends on 0028 and 0029. Idempotent: safe to re-run.
-- ============================================================================

-- ---------------------------------------------------------------------------
-- 0. One updated_at trigger for this file's tables.
-- ---------------------------------------------------------------------------
create or replace function public.essay_study_touch()
returns trigger
language plpgsql
as $$
begin
  new.updated_at := now();
  return new;
end;
$$;

-- ---------------------------------------------------------------------------
-- 1. Stars and "done".
-- ---------------------------------------------------------------------------
create table if not exists public.essay_marks (
  user_id    uuid not null default auth.uid() references auth.users(id) on delete cascade,
  kind       text not null check (kind in ('pyq', 'answer', 'snippet')),
  item_id    uuid not null,
  starred    boolean not null default false,
  done       boolean not null default false,
  done_at    timestamptz,                       -- set by the trigger below, never by the client
  updated_at timestamptz not null default now(),
  primary key (user_id, kind, item_id)
);
create index if not exists essay_marks_user_idx on public.essay_marks (user_id, updated_at desc);

create or replace function public.essay_marks_stamp()
returns trigger
language plpgsql
as $$
begin
  if new.done and (tg_op = 'INSERT' or not old.done) then
    new.done_at := now();
  elsif not new.done then
    new.done_at := null;
  else
    new.done_at := old.done_at;
  end if;
  new.updated_at := now();
  return new;
end;
$$;

drop trigger if exists essay_marks_stamp on public.essay_marks;
create trigger essay_marks_stamp
  before insert or update on public.essay_marks
  for each row execute function public.essay_marks_stamp();

-- ---------------------------------------------------------------------------
-- 2. Notes. `label` is what the note was about when it was written (a PYQ's
--    topic, an essay's question), so the notes list reads on its own.
-- ---------------------------------------------------------------------------
create table if not exists public.essay_notes (
  id         uuid primary key default gen_random_uuid(),
  user_id    uuid not null default auth.uid() references auth.users(id) on delete cascade,
  kind       text not null check (kind in ('pyq', 'answer', 'snippet', 'free')),
  item_id    uuid,
  label      text check (label is null or length(label) <= 300),
  body       text not null check (length(btrim(body)) between 1 and 5000),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  constraint essay_notes_item check ((kind = 'free') = (item_id is null))
);
create index if not exists essay_notes_user_idx on public.essay_notes (user_id, updated_at desc);
create index if not exists essay_notes_item_idx on public.essay_notes (user_id, kind, item_id);

drop trigger if exists essay_notes_touch on public.essay_notes;
create trigger essay_notes_touch
  before update on public.essay_notes
  for each row execute function public.essay_study_touch();

/* A ceiling, so one account cannot fill the table. */
create or replace function public.essay_notes_cap()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  if (select count(*) from public.essay_notes where user_id = new.user_id) >= 1000 then
    raise exception 'You have 1,000 essay notes. Delete some to add more.' using errcode = 'P0001';
  end if;
  return new;
end;
$$;

drop trigger if exists essay_notes_cap on public.essay_notes;
create trigger essay_notes_cap
  before insert on public.essay_notes
  for each row execute function public.essay_notes_cap();

-- ---------------------------------------------------------------------------
-- 3. Reading log: one row per student, essay and day (India time). The
--    insert policy only accepts today or yesterday, so streaks stay honest.
-- ---------------------------------------------------------------------------
create table if not exists public.essay_reads (
  user_id   uuid not null default auth.uid() references auth.users(id) on delete cascade,
  answer_id uuid not null references public.topper_answers(id) on delete cascade,
  read_on   date not null default (now() at time zone 'Asia/Kolkata')::date,
  primary key (user_id, answer_id, read_on)
);
create index if not exists essay_reads_answer_idx on public.essay_reads (answer_id);

/* How many students have read each of these essays. Counts only. */
create or replace function public.essay_reader_counts(p_ids uuid[])
returns table (answer_id uuid, readers integer)
language sql
stable
security definer
set search_path = public
as $$
  select r.answer_id, count(distinct r.user_id)::integer
  from public.essay_reads r
  where auth.uid() is not null
    and r.answer_id = any ((coalesce(p_ids, '{}'::uuid[]))[1:300])
  group by r.answer_id;
$$;

-- ---------------------------------------------------------------------------
-- 4. The Essay Wiki.
-- ---------------------------------------------------------------------------
create table if not exists public.essay_snippets (
  id          uuid primary key default gen_random_uuid(),
  answer_id   uuid not null references public.topper_answers(id) on delete cascade,
  kind        text not null
              check (kind in ('opening', 'closing', 'quote', 'anecdote', 'example', 'statistic')),
  body        text not null check (length(btrim(body)) > 0),   -- verbatim from the essay
  attribution text,                                            -- quotes: who the topper credits
  why         text,                                            -- our note: what makes it work
  review_note text,                                            -- for the admin: a doubt to check
  page        integer check (page is null or page >= 1),
  status      text not null default 'draft' check (status in ('draft', 'published')),
  body_key    text generated always as (md5(lower(regexp_replace(btrim(body), '\s+', ' ', 'g')))) stored,
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now(),
  constraint essay_snippets_uniq unique (answer_id, body_key)
);
create index if not exists essay_snippets_answer_idx on public.essay_snippets (answer_id);
create index if not exists essay_snippets_status_idx on public.essay_snippets (status, kind);

create table if not exists public.essay_snippet_fits (
  snippet_id uuid not null references public.essay_snippets(id) on delete cascade,
  pyq_id     uuid not null references public.essay_pyqs(id) on delete cascade,
  use_note   text not null check (length(btrim(use_note)) > 0),  -- where it goes in that essay
  rank       smallint not null default 1,
  primary key (snippet_id, pyq_id)
);
create index if not exists essay_snippet_fits_pyq_idx on public.essay_snippet_fits (pyq_id);

drop trigger if exists essay_snippets_touch on public.essay_snippets;
create trigger essay_snippets_touch
  before update on public.essay_snippets
  for each row execute function public.essay_study_touch();

/* Published snippets per theme and kind, for a locked student's view of the
   wiki and for the tab counts. Counts only. */
create or replace function public.essay_wiki_counts()
returns table (theme_id uuid, kind text, n integer)
language sql
stable
security definer
set search_path = public
as $$
  select pt.theme_id, s.kind, count(distinct s.id)::integer
  from public.essay_snippets s
  join public.essay_snippet_fits f on f.snippet_id = s.id
  join public.essay_pyq_themes pt on pt.pyq_id = f.pyq_id
  where s.status = 'published'
  group by pt.theme_id, s.kind;
$$;

-- ---------------------------------------------------------------------------
-- 5. Learn to Write.
-- ---------------------------------------------------------------------------
create table if not exists public.essay_ltw (
  pyq_id     uuid primary key references public.essay_pyqs(id) on delete cascade,
  doc        jsonb not null check (jsonb_typeof(doc) = 'object'),
  status     text not null default 'draft' check (status in ('draft', 'published')),
  source     text not null default 'drafted',
  updated_by uuid references auth.users(id) on delete set null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

drop trigger if exists essay_ltw_touch on public.essay_ltw;
create trigger essay_ltw_touch
  before update on public.essay_ltw
  for each row execute function public.essay_study_touch();

/* Which PYQs have a published guide. Ids only. */
create or replace function public.essay_ltw_ready()
returns setof uuid
language sql
stable
security definer
set search_path = public
as $$
  select l.pyq_id from public.essay_ltw l where l.status = 'published';
$$;

/* The free part of a published guide: its spine, its three sides and the
   argument titles. The paragraphs stay behind Mains. */
create or replace function public.essay_ltw_preview(p_pyq uuid)
returns jsonb
language sql
stable
security definer
set search_path = public
as $$
  select jsonb_build_object(
    'spine', l.doc -> 'spine',
    'sides', coalesce(l.doc -> 'sides', '[]'::jsonb),
    'titles', coalesce((
      select jsonb_agg(jsonb_build_object('side', a -> 'side', 'title', a -> 'title') order by ord)
      from jsonb_array_elements(coalesce(l.doc -> 'arguments', '[]'::jsonb)) with ordinality as x(a, ord)
    ), '[]'::jsonb),
    'introductions', jsonb_array_length(coalesce(l.doc -> 'introductions', '[]'::jsonb)),
    'conclusions', jsonb_array_length(coalesce(l.doc -> 'conclusions', '[]'::jsonb))
  )
  from public.essay_ltw l
  where l.pyq_id = p_pyq
    and l.status = 'published'
    and auth.uid() is not null;
$$;

-- ---------------------------------------------------------------------------
-- 6. Row-level security.
-- ---------------------------------------------------------------------------
alter table public.essay_marks enable row level security;
alter table public.essay_notes enable row level security;
alter table public.essay_reads enable row level security;
alter table public.essay_snippets enable row level security;
alter table public.essay_snippet_fits enable row level security;
alter table public.essay_ltw enable row level security;

drop policy if exists essay_marks_own on public.essay_marks;
create policy essay_marks_own on public.essay_marks for all
  using (user_id = auth.uid()) with check (user_id = auth.uid());

drop policy if exists essay_notes_own on public.essay_notes;
create policy essay_notes_own on public.essay_notes for all
  using (user_id = auth.uid()) with check (user_id = auth.uid());

drop policy if exists essay_reads_own_read on public.essay_reads;
drop policy if exists essay_reads_own_add on public.essay_reads;
create policy essay_reads_own_read on public.essay_reads for select
  using (user_id = auth.uid());
create policy essay_reads_own_add on public.essay_reads for insert
  with check (
    user_id = auth.uid()
    and read_on between (now() at time zone 'Asia/Kolkata')::date - 1
                    and (now() at time zone 'Asia/Kolkata')::date
  );

drop policy if exists essay_snippets_read on public.essay_snippets;
drop policy if exists essay_snippets_admin on public.essay_snippets;
create policy essay_snippets_read on public.essay_snippets for select
  using (public.is_admin() or (status = 'published' and exists (
    select 1 from public.topper_answers a
    where a.id = answer_id and public.can_read_topper_copy(a.copy_id))));
create policy essay_snippets_admin on public.essay_snippets for all
  using (public.is_admin()) with check (public.is_admin());

-- A fit is visible exactly when its snippet is (the subquery runs under the
-- snippet policy above).
drop policy if exists essay_snippet_fits_read on public.essay_snippet_fits;
drop policy if exists essay_snippet_fits_admin on public.essay_snippet_fits;
create policy essay_snippet_fits_read on public.essay_snippet_fits for select
  using (exists (select 1 from public.essay_snippets s where s.id = snippet_id));
create policy essay_snippet_fits_admin on public.essay_snippet_fits for all
  using (public.is_admin()) with check (public.is_admin());

drop policy if exists essay_ltw_read on public.essay_ltw;
drop policy if exists essay_ltw_admin on public.essay_ltw;
create policy essay_ltw_read on public.essay_ltw for select
  using (public.is_admin() or (status = 'published' and public.has_mains_access()));
create policy essay_ltw_admin on public.essay_ltw for all
  using (public.is_admin()) with check (public.is_admin());

-- ---------------------------------------------------------------------------
-- 7. Grants. Visitors get nothing here but the ready-list and the counts.
-- ---------------------------------------------------------------------------
grant select, insert, update, delete on public.essay_marks to authenticated;
grant select, insert, update, delete on public.essay_notes to authenticated;
grant select, insert on public.essay_reads to authenticated;
grant select, insert, update, delete on public.essay_snippets to authenticated;
grant select, insert, update, delete on public.essay_snippet_fits to authenticated;
grant select, insert, update, delete on public.essay_ltw to authenticated;
grant all on public.essay_marks, public.essay_notes, public.essay_reads,
             public.essay_snippets, public.essay_snippet_fits, public.essay_ltw to service_role;

-- Supabase's default privileges also hand new tables to anon; visitors get none
-- of these (a free copy's passages would otherwise be readable signed out).
revoke all on public.essay_marks, public.essay_notes, public.essay_reads,
              public.essay_snippets, public.essay_snippet_fits, public.essay_ltw from anon;

-- Supabase grants new functions to anon directly, so revoke from it by name.
revoke execute on function public.essay_reader_counts(uuid[]) from public, anon;
revoke execute on function public.essay_ltw_preview(uuid) from public, anon;
revoke execute on function public.essay_notes_cap() from public, anon, authenticated;
grant execute on function public.essay_reader_counts(uuid[]) to authenticated, service_role;
grant execute on function public.essay_ltw_preview(uuid) to authenticated, service_role;
grant execute on function public.essay_wiki_counts() to anon, authenticated, service_role;
grant execute on function public.essay_ltw_ready() to anon, authenticated, service_role;
