-- 0031: Editor's picks in the Essay Wiki.
--
-- Until now every wiki snippet was a verbatim passage from a topper's essay,
-- so essay_snippets.answer_id was required. Editor's picks are short
-- anecdotes and quotes written and fact-checked by the editors themselves;
-- they belong to no topper essay. They are rows with answer_id = null.
--
-- Access: a published pick is readable by anyone with Mains access (the same
-- rule as Learn to Write guides); topper snippets keep their per-copy rule.

alter table public.essay_snippets alter column answer_id drop not null;

-- The (answer_id, body_key) unique constraint does not catch duplicates when
-- answer_id is null, so editor's picks get their own uniqueness on body_key.
create unique index if not exists essay_snippets_pick_uniq
  on public.essay_snippets (body_key) where answer_id is null;

drop policy if exists essay_snippets_read on public.essay_snippets;
create policy essay_snippets_read on public.essay_snippets for select
  using (public.is_admin() or (status = 'published' and (
    (answer_id is null and public.has_mains_access())
    or exists (
      select 1 from public.topper_answers a
      where a.id = answer_id and public.can_read_topper_copy(a.copy_id)))));
