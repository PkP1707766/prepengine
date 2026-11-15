-- 0040: Fact Bank cards linked straight to a syllabus topic.
--
-- Until now a wiki card reached a topic only through the PYQs it fits
-- (essay_snippet_fits -> essay_pyq_themes). Some GS syllabus topics have no
-- recent PYQ, so their cards had nowhere to appear. A card may now also be
-- linked to a topic directly, with a note on how to use it in answers on
-- that topic. The wiki's topic counts include these links.

create table if not exists public.essay_snippet_topics (
  snippet_id uuid not null references public.essay_snippets(id) on delete cascade,
  theme_id   uuid not null references public.essay_themes(id) on delete cascade,
  use_note   text not null check (length(btrim(use_note)) > 0),   -- how to use it in this topic's answers
  primary key (snippet_id, theme_id)
);
create index if not exists essay_snippet_topics_theme_idx on public.essay_snippet_topics (theme_id);

alter table public.essay_snippet_topics enable row level security;
drop policy if exists essay_snippet_topics_read on public.essay_snippet_topics;
drop policy if exists essay_snippet_topics_admin on public.essay_snippet_topics;
-- Readable when its card is (the card's own policy decides).
create policy essay_snippet_topics_read on public.essay_snippet_topics for select
  using (exists (select 1 from public.essay_snippets s where s.id = snippet_id));
create policy essay_snippet_topics_admin on public.essay_snippet_topics for all
  using (public.is_admin()) with check (public.is_admin());
grant select, insert, update, delete on public.essay_snippet_topics to authenticated;

/* Published snippets per theme and kind: through the PYQs they fit, and
   through direct topic links. Counts only. */
create or replace function public.essay_wiki_counts()
returns table (theme_id uuid, kind text, n integer)
language sql
stable
security definer
set search_path = public
as $$
  select x.theme_id, x.kind, count(distinct x.id)::integer
  from (
    select pt.theme_id, s.kind, s.id
    from public.essay_snippets s
    join public.essay_snippet_fits f on f.snippet_id = s.id
    join public.essay_pyq_themes pt on pt.pyq_id = f.pyq_id
    where s.status = 'published'
    union all
    select st.theme_id, s.kind, s.id
    from public.essay_snippets s
    join public.essay_snippet_topics st on st.snippet_id = s.id
    where s.status = 'published'
  ) x
  group by x.theme_id, x.kind;
$$;
