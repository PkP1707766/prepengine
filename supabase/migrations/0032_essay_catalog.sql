-- 0032: the Essay catalogue on the public page.
--
-- A visitor may read PYQs and themes but nothing behind them, so the public
-- catalogue could only say "96 topics" -- not how many topper copies, guides
-- and wiki entries sit behind each one. This hands out those COUNTS, plus two
-- small tasters chosen here rather than by the caller: the free part of one
-- guide (the same spine, sides and argument titles any signed-in student
-- already sees as a preview) and one Editor's pick quote. No copy, no page,
-- no paragraph of a guide leaves through it.

create or replace function public.essay_catalog()
returns jsonb
language sql
stable
security definer
set search_path = public
as $$
  with cp as (
    select ap.pyq_id, a.id as answer_id, c.topper_id
    from public.essay_answer_pyqs ap
    join public.topper_answers a on a.id = ap.answer_id
    join public.topper_copies c on c.id = a.copy_id
    join public.essay_pyqs p on p.id = ap.pyq_id and p.is_published
    where c.is_published
  ),
  sample as (
    select l.pyq_id, l.doc, p.topic, p.year
    from public.essay_ltw l
    join public.essay_pyqs p on p.id = l.pyq_id and p.is_published
    where l.status = 'published'
    order by p.year desc, p.q_no asc nulls last, p.topic
    limit 1
  ),
  pick as (
    select s.body, s.attribution
    from public.essay_snippets s
    where s.status = 'published' and s.answer_id is null and s.kind = 'quote'
      and s.attribution is not null and length(s.body) between 40 and 170
    order by s.body_key
    limit 1
  )
  select jsonb_build_object(
    'essays',  (select count(distinct answer_id) from cp),
    'toppers', (select count(distinct topper_id) from cp),
    'top_marks', (select max(t.essay_marks) from public.toppers t
                  where t.id in (select topper_id from cp)),
    'per_pyq', coalesce((select jsonb_object_agg(pyq_id, n)
                         from (select pyq_id, count(distinct answer_id) as n from cp group by pyq_id) x), '{}'::jsonb),
    'guides',  coalesce((select jsonb_agg(l.pyq_id) from public.essay_ltw l
                         join public.essay_pyqs p on p.id = l.pyq_id and p.is_published
                         where l.status = 'published'), '[]'::jsonb),
    'kinds',   coalesce((select jsonb_object_agg(kind, n)
                         from (select kind, count(*) as n from public.essay_snippets
                               where status = 'published' group by kind) k), '{}'::jsonb),
    'guide_sample', (select jsonb_build_object(
        'pyq_id', s.pyq_id, 'topic', s.topic, 'year', s.year,
        'spine', s.doc -> 'spine',
        'sides', coalesce(s.doc -> 'sides', '[]'::jsonb),
        'titles', coalesce((
          select jsonb_agg(jsonb_build_object('side', a -> 'side', 'title', a -> 'title') order by ord)
          from jsonb_array_elements(coalesce(s.doc -> 'arguments', '[]'::jsonb)) with ordinality as x(a, ord)
        ), '[]'::jsonb))
      from sample s),
    'pick', (select jsonb_build_object('body', body, 'attribution', attribution) from pick)
  );
$$;

revoke execute on function public.essay_catalog() from public;
grant execute on function public.essay_catalog() to anon, authenticated, service_role;
