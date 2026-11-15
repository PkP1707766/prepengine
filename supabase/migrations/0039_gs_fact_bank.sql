-- 0039: the GS Fact Bank, on the Essay Wiki's tables.
--
-- The Essay Wiki keeps short snippets (essay_snippets) linked to the PYQs they
-- fit (essay_snippet_fits, each with a note on how to use it there). A GS
-- fact card is the same shape: an editor-written, fact-checked item (a data
-- point, a judgment, a committee or report, a scheme or law, an example, a
-- constitutional provision, a piece of history, a thinker or a quote) linked
-- to the GS PYQs it strengthens. Three things change:
--
--   * kinds: the GS card types join the Essay's six;
--   * essay_snippets.paper: which section a snippet belongs to, so that
--   * an editor's pick (answer_id null) is read by the entitlement of its own
--     paper (has_paper_access), not always by the Essay's. Topper snippets
--     keep their per-copy rule.
--
-- Existing rows keep paper = 'essay', so the Essay Wiki reads as before.

alter table public.essay_snippets drop constraint if exists essay_snippets_kind_check;
alter table public.essay_snippets add constraint essay_snippets_kind_check
  check (kind in ('opening', 'closing', 'quote', 'anecdote', 'example', 'statistic',
                  'judgment', 'report', 'scheme', 'constitution', 'history', 'thinker'));

alter table public.essay_snippets
  add column if not exists paper text not null default 'essay';
do $$ begin
  if not exists (select 1 from pg_constraint where conname = 'essay_snippets_paper_chk') then
    alter table public.essay_snippets add constraint essay_snippets_paper_chk
      check (paper in ('essay', 'gs1', 'gs2', 'gs3', 'gs4'));
  end if;
end $$;
create index if not exists essay_snippets_paper_idx on public.essay_snippets (paper, status, kind);

drop policy if exists essay_snippets_read on public.essay_snippets;
create policy essay_snippets_read on public.essay_snippets for select
  using (public.is_admin() or (status = 'published' and (
    (answer_id is null and public.has_paper_access(paper))
    or exists (
      select 1 from public.topper_answers a
      where a.id = answer_id and public.can_read_topper_copy(a.copy_id)))));
