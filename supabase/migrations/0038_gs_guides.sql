-- 0038: Learn to Write guides for GS questions.
--
-- A GS guide lives in essay_ltw like an essay guide (one row per PYQ, the
-- guide as a jsonb doc), with doc.kind 'gs' (an answer) or 'gs-case' (a
-- GS-IV case study). Two things change:
--
--   * who may read a published guide: the entitlement of the PYQ's own
--     paper (has_paper_access), so GS guides follow GS access and Essay
--     guides keep following the Essay's;
--   * the free preview a locked student sees: for a GS guide it is what the
--     question asks and the body headings, not the essay's spine and sides.

drop policy if exists essay_ltw_read on public.essay_ltw;
create policy essay_ltw_read on public.essay_ltw for select
  using (public.is_admin() or (status = 'published' and public.has_paper_access(
    (select p.paper from public.essay_pyqs p where p.id = pyq_id))));

create or replace function public.essay_ltw_preview(p_pyq uuid)
returns jsonb
language sql
stable
security definer
set search_path = public
as $$
  select case when coalesce(l.doc ->> 'kind', '') like 'gs%' then
    jsonb_build_object(
      'kind', l.doc -> 'kind',
      'demand', l.doc -> 'demand',
      'headings', coalesce((
        select jsonb_agg(b -> 'heading' order by ord)
        from jsonb_array_elements(coalesce(l.doc -> 'body', l.doc -> 'issues', '[]'::jsonb)) with ordinality as x(b, ord)
      ), '[]'::jsonb))
  else
    jsonb_build_object(
      'spine', l.doc -> 'spine',
      'sides', coalesce(l.doc -> 'sides', '[]'::jsonb),
      'titles', coalesce((
        select jsonb_agg(jsonb_build_object('side', a -> 'side', 'title', a -> 'title') order by ord)
        from jsonb_array_elements(coalesce(l.doc -> 'arguments', '[]'::jsonb)) with ordinality as x(a, ord)
      ), '[]'::jsonb),
      'introductions', jsonb_array_length(coalesce(l.doc -> 'introductions', '[]'::jsonb)),
      'conclusions', jsonb_array_length(coalesce(l.doc -> 'conclusions', '[]'::jsonb)))
  end
  from public.essay_ltw l
  where l.pyq_id = p_pyq
    and l.status = 'published'
    and auth.uid() is not null;
$$;

revoke execute on function public.essay_ltw_preview(uuid) from public, anon;
grant execute on function public.essay_ltw_preview(uuid) to authenticated, service_role;
