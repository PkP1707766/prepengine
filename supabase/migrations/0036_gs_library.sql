-- 0036: what the GS screens read.
--
-- A GS topper answer is filed under a syllabus topic (0034), and a GS PYQ
-- page shows the answers of its topic. The library view gains that topic
-- (appended, as create or replace view requires), and a small view counts
-- the answers behind each topic so a PYQ card can say how many there are.
-- Both are security_invoker: a student still sees published copies only.

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
  a.body_words,
  a.theme_id
from public.topper_answers a
join public.topper_copies c on c.id = a.copy_id
join public.toppers t on t.id = c.topper_id;

create or replace view public.topper_theme_counts_v
with (security_invoker = true) as
select a.theme_id, a.paper, count(*)::integer as answers
from public.topper_answers a
join public.topper_copies c on c.id = a.copy_id
where a.theme_id is not null and c.is_published
group by a.theme_id, a.paper;

grant select on public.topper_library_v to authenticated;
grant select on public.topper_theme_counts_v to authenticated;

/* May the caller read this paper's Mains material? The Essay keeps its own
   entitlement; GS I-IV share one. */
create or replace function public.has_paper_access(p_paper text)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select case when p_paper like 'gs%' then public.has_gs_access() else public.has_mains_access() end;
$$;

revoke execute on function public.has_paper_access(text) from public;
grant execute on function public.has_paper_access(text) to anon, authenticated, service_role;
