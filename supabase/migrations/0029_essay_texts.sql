-- ============================================================================
-- JUNOONIAS — Mains: the text of each topper essay.
--
-- Most copies come with a typed transcript, which gives every essay its full
-- text. Students can read an essay as text beside the handwritten copy, every
-- essay gets a word count, and search finds an essay by any word in it.
--
--   topper_answer_texts    one essay's text. Readable only by whoever may read
--                          the copy's hosted pages (can_read_topper_copy):
--                          the text IS the copy, so it sits behind the same lock
--   topper_answers.body_words
--                          the word count, kept by a trigger. Visible wherever
--                          the essay's row is: a length benchmark, not content
--   search_topper_essays() which essays contain these words. Ids and a rank
--                          only, never text, so a locked essay can still be
--                          found and its lock explained
--
-- Depends on 0028_mains_essay.sql. Idempotent: safe to re-run.
-- ============================================================================

-- ---------------------------------------------------------------------------
-- 1. The word count on the answer.
-- ---------------------------------------------------------------------------
alter table public.topper_answers
  add column if not exists body_words integer check (body_words is null or body_words >= 0);

-- ---------------------------------------------------------------------------
-- 2. The text.
-- ---------------------------------------------------------------------------
create table if not exists public.topper_answer_texts (
  answer_id   uuid primary key references public.topper_answers(id) on delete cascade,
  body        text not null check (length(btrim(body)) > 0),  -- paragraphs split by a blank line
  source      text not null default 'typed transcript',       -- where the text came from
  source_url  text,                                           -- e.g. the transcript's PDF
  body_tsv    tsvector generated always as (to_tsvector('english', body)) stored,
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now()
);
create index if not exists topper_answer_texts_tsv_idx on public.topper_answer_texts using gin (body_tsv);

-- ---------------------------------------------------------------------------
-- 3. Keep updated_at and topper_answers.body_words in step with the text.
-- ---------------------------------------------------------------------------
create or replace function public.topper_answer_texts_touch()
returns trigger
language plpgsql
as $$
begin
  new.updated_at := now();
  return new;
end;
$$;

create or replace function public.topper_answer_texts_count()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  if tg_op = 'DELETE' then
    update public.topper_answers set body_words = null where id = old.answer_id;
    return old;
  end if;
  update public.topper_answers
     set body_words = coalesce(array_length(regexp_split_to_array(btrim(new.body), '\s+'), 1), 0)
   where id = new.answer_id;
  return new;
end;
$$;

drop trigger if exists topper_answer_texts_touch on public.topper_answer_texts;
create trigger topper_answer_texts_touch
  before update on public.topper_answer_texts
  for each row execute function public.topper_answer_texts_touch();

drop trigger if exists topper_answer_texts_count on public.topper_answer_texts;
create trigger topper_answer_texts_count
  after insert or update of body or delete on public.topper_answer_texts
  for each row execute function public.topper_answer_texts_count();

-- ---------------------------------------------------------------------------
-- 4. Row-level security: the copy's lock, and admin writes.
-- ---------------------------------------------------------------------------
alter table public.topper_answer_texts enable row level security;

drop policy if exists topper_answer_texts_read on public.topper_answer_texts;
drop policy if exists topper_answer_texts_admin on public.topper_answer_texts;

create policy topper_answer_texts_read on public.topper_answer_texts for select
  using (public.is_admin() or exists (
    select 1 from public.topper_answers a
    where a.id = answer_id and public.can_read_topper_copy(a.copy_id)));
create policy topper_answer_texts_admin on public.topper_answer_texts for all
  using (public.is_admin()) with check (public.is_admin());

grant select, insert, update, delete on public.topper_answer_texts to authenticated;
grant all on public.topper_answer_texts to service_role;

-- ---------------------------------------------------------------------------
-- 5. Search: which published essays contain these words. Signed-in only;
--    returns ids and a rank, never text. websearch syntax: "quoted phrase",
--    or, -exclude. A query of stop words alone matches nothing.
-- ---------------------------------------------------------------------------
create or replace function public.search_topper_essays(p_q text, p_limit integer default 200)
returns table (answer_id uuid, rank real)
language sql
stable
security definer
set search_path = public
as $$
  select t.answer_id, ts_rank(t.body_tsv, q.query) as rank
  from public.topper_answer_texts t
  join public.topper_answers a on a.id = t.answer_id
  join public.topper_copies c on c.id = a.copy_id
  cross join lateral (select websearch_to_tsquery('english', coalesce(p_q, '')) as query) q
  where auth.uid() is not null
    and (c.is_published or public.is_admin())
    and t.body_tsv @@ q.query
  order by rank desc
  limit least(greatest(coalesce(p_limit, 200), 1), 500);
$$;

-- Supabase grants new functions to anon directly, not through PUBLIC, so the
-- anon grant needs its own revoke. (The body also answers nothing without a
-- signed-in user.)
revoke all on function public.search_topper_essays(text, integer) from public;
revoke all on function public.search_topper_essays(text, integer) from anon;
grant execute on function public.search_topper_essays(text, integer) to authenticated, service_role;

-- ---------------------------------------------------------------------------
-- 6. The library view gains the word count. Columns are 0028's, in order,
--    with body_words appended (create or replace view may only add at the end).
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
  t.essay_marks,
  a.body_words
from public.topper_answers a
join public.topper_copies c on c.id = a.copy_id
join public.toppers t on t.id = c.topper_id;
