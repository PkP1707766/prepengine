-- 0044: honest public catalogues for the Essay and for GS.
--
-- 1. essay_catalog() predates GS. It counted every published guide and every
--    published snippet, so once GS went live the Essay page claimed 964
--    guides (96 are the Essay's, 868 GS) and 2,918 wiki entries (1,666 are
--    the Essay's, 1,252 the GS Fact Bank). It now counts the Essay alone.
-- 2. gs_catalog() gives the GS public page the same kind of read: counts per
--    paper, the toppers and their answers, the guides, the GS-IV case studies,
--    the Fact Bank by type, and three small tasters -- the free part of one
--    guide (what the question asks and its headings, as any locked student
--    sees), the headings of one case study, and one Fact Bank card. No answer,
--    no page and no guide text beyond that leaves through it.

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
    join public.essay_pyqs p on p.id = ap.pyq_id and p.is_published and p.paper = 'essay'
    where c.is_published
  ),
  g as (
    select l.pyq_id, l.doc, p.topic, p.year, p.q_no
    from public.essay_ltw l
    join public.essay_pyqs p on p.id = l.pyq_id and p.is_published and p.paper = 'essay'
    where l.status = 'published'
  ),
  sample as (select * from g order by year desc, q_no asc nulls last, topic limit 1),
  pick as (
    select s.body, s.attribution
    from public.essay_snippets s
    where s.status = 'published' and s.answer_id is null and s.paper = 'essay' and s.kind = 'quote'
      and s.attribution is not null and length(s.body) between 40 and 170
    order by s.body_key
    limit 1
  )
  select jsonb_build_object(
    'essays',  (select count(distinct answer_id) from cp),
    'words',   (select coalesce(sum(a.body_words), 0) from public.topper_answers a
                where a.id in (select answer_id from cp)),
    'arguments', (select coalesce(sum(jsonb_array_length(coalesce(doc -> 'arguments', '[]'::jsonb))), 0) from g),
    'openings',  (select coalesce(sum(jsonb_array_length(coalesce(doc -> 'introductions', '[]'::jsonb))
                                    + jsonb_array_length(coalesce(doc -> 'conclusions', '[]'::jsonb))), 0) from g),
    'toppers', (select count(distinct topper_id) from cp),
    'top_marks', (select max(t.essay_marks) from public.toppers t
                  where t.id in (select topper_id from cp)),
    'per_pyq', coalesce((select jsonb_object_agg(pyq_id, n)
                         from (select pyq_id, count(distinct answer_id) as n from cp group by pyq_id) x), '{}'::jsonb),
    'guides',  coalesce((select jsonb_agg(pyq_id) from g), '[]'::jsonb),
    'kinds',   coalesce((select jsonb_object_agg(kind, n)
                         from (select kind, count(*) as n from public.essay_snippets
                               where status = 'published' and paper = 'essay' group by kind) k), '{}'::jsonb),
    'guide_sample', (select jsonb_build_object(
        'pyq_id', s.pyq_id, 'topic', s.topic, 'year', s.year,
        'spine', s.doc -> 'spine',
        'sides', coalesce((select jsonb_agg(jsonb_build_object('label', x -> 'label') order by o)
                           from jsonb_array_elements(coalesce(s.doc -> 'sides', '[]'::jsonb)) with ordinality e(x, o)), '[]'::jsonb),
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

create or replace function public.gs_catalog()
returns jsonb
language sql
stable
security definer
set search_path = public
as $$
  with q as (
    select id, paper, year, q_no, section, topic from public.essay_pyqs
    where is_published and paper like 'gs%'
  ),
  ans as (
    select a.id, a.copy_id, a.paper, a.theme_id, c.topper_id
    from public.topper_answers a
    join public.topper_copies c on c.id = a.copy_id
    where c.is_published and a.paper like 'gs%'
  ),
  g as (
    select l.pyq_id, l.doc, q.paper, q.year, q.q_no, q.topic
    from public.essay_ltw l join q on q.id = l.pyq_id
    where l.status = 'published'
  ),
  per as (
    -- A topper answer belongs to a question when they share a syllabus theme,
    -- the same way the GS section files them.
    select pt.pyq_id, count(distinct a.id) as n
    from public.essay_pyq_themes pt
    join q on q.id = pt.pyq_id
    join ans a on a.theme_id = pt.theme_id
    group by pt.pyq_id
  ),
  sample as (
    select * from g where doc ->> 'kind' = 'gs' and paper = 'gs2'
    order by year desc, q_no desc limit 1
  ),
  cs as (
    select * from g where doc ->> 'kind' = 'gs-case'
    order by year desc, q_no asc limit 1
  ),
  fact as (
    select s.body, s.kind
    from public.essay_snippets s
    where s.status = 'published' and s.paper like 'gs%' and s.answer_id is null
      and s.kind in ('judgment', 'statistic', 'report', 'scheme') and length(s.body) between 60 and 190
    order by s.body_key
    limit 1
  )
  select jsonb_build_object(
    'questions', (select count(*) from q),
    'years', jsonb_build_array((select min(year) from q), (select max(year) from q)),
    'papers', coalesce((select jsonb_object_agg(paper, jsonb_build_object(
                  'questions', nq,
                  'guides', (select count(*) from g where g.paper = x.paper),
                  'cases', (select count(*) from g where g.paper = x.paper and g.doc ->> 'kind' = 'gs-case'),
                  'answers', (select count(*) from ans where ans.paper = x.paper)))
                from (select paper, count(*) as nq from q group by paper) x), '{}'::jsonb),
    'answers', (select count(*) from ans),
    'copies',  (select count(distinct copy_id) from ans),
    'toppers', (select count(distinct topper_id) from ans),
    'guides',  coalesce((select jsonb_agg(pyq_id) from g), '[]'::jsonb),
    'cases',   (select count(*) from g where doc ->> 'kind' = 'gs-case'),
    'headings', (select coalesce(sum(jsonb_array_length(coalesce(doc -> 'body', doc -> 'issues', '[]'::jsonb))), 0) from g),
    'per_pyq', coalesce((select jsonb_object_agg(pyq_id, n) from per), '{}'::jsonb),
    'facts',   (select count(*) from public.essay_snippets where status = 'published' and paper like 'gs%'),
    'kinds',   coalesce((select jsonb_object_agg(kind, n)
                         from (select kind, count(*) as n from public.essay_snippets
                               where status = 'published' and paper like 'gs%' group by kind) k), '{}'::jsonb),
    'guide_sample', (select jsonb_build_object(
        'pyq_id', s.pyq_id, 'topic', s.topic, 'year', s.year, 'paper', s.paper,
        'directive', s.doc -> 'directive', 'demand', s.doc -> 'demand',
        'headings', coalesce((select jsonb_agg(b -> 'heading' order by o)
                              from jsonb_array_elements(coalesce(s.doc -> 'body', '[]'::jsonb)) with ordinality e(b, o)), '[]'::jsonb),
        'intro', coalesce((select jsonb_agg(b -> 'type' order by o)
                           from jsonb_array_elements(coalesce(s.doc -> 'intro', '[]'::jsonb)) with ordinality e(b, o)), '[]'::jsonb),
        'value_adds', jsonb_array_length(coalesce(s.doc -> 'value_adds', '[]'::jsonb)))
      from sample s),
    'case_sample', (select jsonb_build_object(
        'pyq_id', c.pyq_id, 'topic', c.topic, 'year', c.year,
        'issues', coalesce((select jsonb_agg(b -> 'heading' order by o)
                            from jsonb_array_elements(coalesce(c.doc -> 'issues', '[]'::jsonb)) with ordinality e(b, o)), '[]'::jsonb),
        'stakeholders', jsonb_array_length(coalesce(c.doc -> 'stakeholders', '[]'::jsonb)),
        'options', jsonb_array_length(coalesce(c.doc -> 'options', '[]'::jsonb)))
      from cs c),
    'fact', (select jsonb_build_object('body', body, 'kind', kind) from fact)
  );
$$;
revoke execute on function public.gs_catalog() from public;
grant execute on function public.gs_catalog() to anon, authenticated, service_role;
