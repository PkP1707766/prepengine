-- 0034: General Studies I-IV on the Mains tables.
--
-- The Essay module's tables were built paper-agnostic on the topper side
-- (topper_answers.paper already takes gs1..gs4) but Essay-only on the PYQ
-- side. This opens the PYQ side to GS:
--
--   essay_themes.paper   a theme belongs to one paper; for GS a theme is a
--                        syllabus topic ("Federalism & Centre-State Relations")
--   essay_pyqs.paper     plus the marks and word limit a GS question carries
--   topper_answers.theme_id
--                        GS topper answers come from test series, not from
--                        UPSC papers, so they are filed under a syllabus topic
--                        and shown beside the PYQs of that topic
--   plans.includes_gs    GS is sold apart from the Essay: includes_mains keeps
--                        meaning the Essay section, includes_gs opens GS
--
-- Existing rows keep paper = 'essay', so the Essay section reads as before.

alter table public.essay_themes
  add column if not exists paper text not null default 'essay';
do $$ begin
  if not exists (select 1 from pg_constraint where conname = 'essay_themes_paper_chk') then
    alter table public.essay_themes add constraint essay_themes_paper_chk
      check (paper in ('essay', 'gs1', 'gs2', 'gs3', 'gs4'));
  end if;
end $$;
create index if not exists essay_themes_paper_idx on public.essay_themes (paper, sort_order);

alter table public.essay_pyqs
  add column if not exists paper text not null default 'essay',
  add column if not exists marks smallint check (marks between 1 and 250),
  add column if not exists word_limit smallint check (word_limit between 1 and 2000);
do $$ begin
  if not exists (select 1 from pg_constraint where conname = 'essay_pyqs_paper_chk') then
    alter table public.essay_pyqs add constraint essay_pyqs_paper_chk
      check (paper in ('essay', 'gs1', 'gs2', 'gs3', 'gs4'));
  end if;
  -- A topic is unique per paper. The older (year, topic_key) key stays for
  -- now: the admin importer still upserts on it, and no wording has been
  -- asked in two papers in one year. It goes when that importer moves over.
  if not exists (select 1 from pg_constraint where conname = 'essay_pyqs_paper_year_topic_uniq') then
    alter table public.essay_pyqs add constraint essay_pyqs_paper_year_topic_uniq
      unique (paper, year, topic_key);
  end if;
end $$;
create index if not exists essay_pyqs_paper_idx on public.essay_pyqs (paper, year desc);

alter table public.topper_answers
  add column if not exists theme_id uuid references public.essay_themes(id) on delete set null;
create index if not exists topper_answers_theme_idx on public.topper_answers (theme_id);

alter table public.plans
  add column if not exists includes_gs boolean not null default false;

/* May this user read the GS section? Admins and testers, or an active
   enrolment on a plan that includes GS. */
create or replace function public.has_gs_access(p_user uuid default auth.uid())
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select public.is_admin()
      or public.is_tester(p_user)
      or exists (
        select 1
        from public.enrollments e
        join public.plans p on p.code = e.plan_code
        where e.student_id = p_user
          and e.status = 'active'
          and (e.expires_at is null or e.expires_at > now())
          and p.includes_gs
      );
$$;

revoke execute on function public.has_gs_access(uuid) from public;
grant execute on function public.has_gs_access(uuid) to anon, authenticated, service_role;
