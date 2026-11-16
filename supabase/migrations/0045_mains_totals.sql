-- 0045: one set of Mains totals for the homepage band, Essay and GS together.
--
-- The band heads both sections, but its numbers came from essay_catalog(),
-- which counts the Essay alone (68 toppers, 233 essays). Adding the GS
-- catalogue's counts to it would count a topper who wrote both papers twice,
-- and the Essay catalogue has no copy count, so the totals are read here, once.
-- Counts only; nothing a visitor could not count on the site.

create or replace function public.mains_totals()
returns jsonb
language sql
stable
security definer
set search_path = public
as $$
  with ans as (
    select a.id, a.copy_id, c.topper_id
    from public.topper_answers a
    join public.topper_copies c on c.id = a.copy_id
    where c.is_published and (a.paper = 'essay' or a.paper like 'gs%')
  ),
  q as (
    select id, paper, year from public.essay_pyqs
    where is_published and (paper = 'essay' or paper like 'gs%')
  )
  select jsonb_build_object(
    'toppers',   (select count(distinct topper_id) from ans),
    'copies',    (select count(distinct copy_id) from ans),
    'answers',   (select count(*) from ans),
    'questions', (select count(*) from q),
    'essay_y1',  (select min(year) from q where paper = 'essay'),
    'gs_y1',     (select min(year) from q where paper like 'gs%'),
    'guides',    (select count(*) from public.essay_ltw l join q on q.id = l.pyq_id where l.status = 'published'),
    'cards',     (select count(*) from public.essay_snippets
                  where status = 'published' and (paper = 'essay' or paper like 'gs%'))
  );
$$;
revoke execute on function public.mains_totals() from public;
grant execute on function public.mains_totals() to anon, authenticated, service_role;
