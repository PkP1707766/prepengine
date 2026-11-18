-- 0046: Prelims PYQ Practice.
--
-- The owner's call (2026-11-19):
--   * Every Prelims previous-year question, by subject, topic, exam and year,
--     practised one at a time or as a timed test.
--   * A few questions in every subject are free (pyq_subjects.free_count,
--     editable by the admin). Everything else unlocks with one plan,
--     'pyq-practice', Rs 9 for now; the price is edited on the admin plan
--     screen like any other plan.
--   * UPSC CSE plus the other exams the same questions came from: CDS, CAPF
--     and the state commissions. CDS, CAPF, MPPSC and CGPSC are added to the
--     exam list here.
--
-- The questions live in their own table, not in public.questions. That table
-- feeds the mock-test generator; a PYQ drawn into a mock paper would be a
-- repeat the student has already seen, filed under the wrong exam.
--
-- Reading: pyq_catalog() and pyq_meta() are open to visitors (counts and
-- labels only). pyq_fetch() returns a question's text and answer only when the
-- caller may practise it: a free question, or any question for a student with
-- the plan. Writing: answers, bookmarks and test results go through the
-- functions below, which re-check access and work out correctness on the
-- server, so a student's accuracy cannot be typed in by the browser.

-- ------------------------------------------------------------ exams --
insert into public.exam_categories (code, label, full_name, conducted_by, region, sort_order, is_active) values
  ('cds',   'CDS',   'Combined Defence Services',                   'UPSC',  'National',       12, true),
  ('capf',  'CAPF',  'Central Armed Police Forces (AC)',            'UPSC',  'National',       14, true),
  ('mppsc', 'MPPSC', 'Madhya Pradesh Public Service Commission',    'MPPSC', 'Madhya Pradesh', 55, true),
  ('cgpsc', 'CGPSC', 'Chhattisgarh Public Service Commission',      'CGPSC', 'Chhattisgarh',   65, true)
on conflict (code) do nothing;

-- ------------------------------------------------------------ plan --
alter table public.plans add column if not exists includes_pyq boolean not null default false;

insert into public.plans (
  code, name, name_hi, tagline, tagline_hi, description, description_hi,
  price_paise, mrp_paise, currency, duration_days, features,
  is_active, sort_order, exam_category, includes_pyq
) values (
  'pyq-practice',
  'Prelims PYQ Practice: every subject',
  'प्रीलिम्स PYQ अभ्यास: सभी विषय',
  'Every previous-year Prelims question, by subject, topic, exam and year.',
  'प्रीलिम्स के पिछले वर्षों के सभी प्रश्न, विषय, टॉपिक, परीक्षा और वर्ष के अनुसार।',
  'Unlocks every question in PYQ Practice, in every subject as it is added: topic-wise and year-wise sets, timed tests with negative marking, and your accuracy by topic.',
  'PYQ अभ्यास का हर प्रश्न खोलता है, हर विषय में, जैसे-जैसे जुड़ते जाएँ: टॉपिक और वर्ष के अनुसार सेट, नेगेटिव मार्किंग वाले टाइम्ड टेस्ट, और टॉपिक के अनुसार आपकी सटीकता।',
  900, 900, 'INR', 365,
  '["Every question in every subject, as each is added", "Topic-wise, year-wise and exam-wise sets", "Timed tests with UPSC negative marking", "Accuracy by topic, mistakes to revise, bookmarks"]'::jsonb,
  true, 85, 'upsc', true
)
on conflict (code) do nothing;

/* The shop window lists active plans; this one is sold from the PYQ page, so
   the catalogue needs the flag to keep it out of the test-series grid. */
create or replace view public.catalog_v as
 select p.code, p.name, p.exam_category, p.tagline, p.description, p.name_hi, p.tagline_hi, p.description_hi,
    p.price_paise, p.mrp_paise, p.currency, p.duration_days, p.features, p.sort_order, p.brochure_url,
    ec.label as exam_label, ec.label_hi as exam_label_hi, ec.full_name as exam_full_name,
    ec.full_name_hi as exam_full_name_hi, ec.conducted_by, ec.sort_order as exam_sort_order,
    ((select count(*) from plan_tests pt join tests t on t.id = pt.test_id
       where pt.plan_code = p.code and t.is_published))::integer as test_count,
    ((select count(*) from plan_tests pt join tests t on t.id = pt.test_id
       where pt.plan_code = p.code and t.is_published and t.is_free))::integer as free_test_count,
    p.includes_mains, p.includes_gs, p.includes_pyq
   from plans p
   left join exam_categories ec on ec.code = p.exam_category
  where p.is_active;

create or replace function public.has_pyq_access(p_user uuid default auth.uid())
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
          and p.includes_pyq
      );
$$;
revoke execute on function public.has_pyq_access(uuid) from public;
grant execute on function public.has_pyq_access(uuid) to anon, authenticated, service_role;

-- ------------------------------------------------------------ bank --
create table if not exists public.pyq_subjects (
  code        text primary key,
  name        text not null,
  name_hi     text,
  blurb       text,
  blurb_hi    text,
  sort_order  integer not null default 0,
  free_count  integer not null default 10 check (free_count >= 0),
  is_active   boolean not null default true
);

create table if not exists public.pyq_topics (
  subject_code text not null references public.pyq_subjects(code) on update cascade on delete cascade,
  code         text not null,
  name         text not null,
  name_hi      text,
  sort_order   integer not null default 0,
  primary key (subject_code, code)
);

create table if not exists public.prelims_pyqs (
  id            uuid primary key default gen_random_uuid(),
  ref           text not null unique,                 -- stable import key
  subject       text not null references public.pyq_subjects(code) on update cascade,
  topic         text not null,
  also_topics   text[] not null default '{}',         -- 'subject/topic' of other homes
  exam          text not null references public.exam_categories(code) on update cascade,
  exam_label    text not null,                        -- as it appeared, e.g. 'UPPCS (Mains) 2014'
  year          integer not null check (year between 1970 and 2100),
  paper_kind    text not null default 'pre' check (paper_kind in ('pre', 'mains')),
  type          text not null check (type in ('mcq', 'statement_based', 'match_the_following', 'assertion_reason')),
  body          text not null,
  body_hi       text,
  question_data jsonb not null default '{}'::jsonb,
  options       jsonb not null,                       -- [{id, body, body_hi}]
  answer        text not null check (answer ~ '^[a-e]$'),
  explanation    text,
  explanation_hi text,
  concept_group text,                                 -- the same question asked in two years
  free_rank     integer,                              -- free while free_rank <= subject.free_count
  status        text not null default 'draft' check (status in ('draft', 'published', 'held', 'retired')),
  note          text,                                 -- admin-only
  created_at    timestamptz not null default now(),
  updated_at    timestamptz not null default now(),
  foreign key (subject, topic) references public.pyq_topics(subject_code, code) on update cascade
);
create index if not exists prelims_pyqs_subject_idx on public.prelims_pyqs (subject, status);
create index if not exists prelims_pyqs_also_idx on public.prelims_pyqs using gin (also_topics);

alter table public.pyq_subjects enable row level security;
alter table public.pyq_topics enable row level security;
alter table public.prelims_pyqs enable row level security;

drop policy if exists pyq_subjects_read on public.pyq_subjects;
create policy pyq_subjects_read on public.pyq_subjects for select using (true);
drop policy if exists pyq_subjects_admin on public.pyq_subjects;
create policy pyq_subjects_admin on public.pyq_subjects for all using (public.is_admin()) with check (public.is_admin());

drop policy if exists pyq_topics_read on public.pyq_topics;
create policy pyq_topics_read on public.pyq_topics for select using (true);
drop policy if exists pyq_topics_admin on public.pyq_topics;
create policy pyq_topics_admin on public.pyq_topics for all using (public.is_admin()) with check (public.is_admin());

-- No read policy for students: the text and the answer leave only through pyq_fetch().
drop policy if exists prelims_pyqs_admin on public.prelims_pyqs;
create policy prelims_pyqs_admin on public.prelims_pyqs for all using (public.is_admin()) with check (public.is_admin());

grant select on public.pyq_subjects, public.pyq_topics to anon, authenticated;
grant insert, update, delete on public.pyq_subjects, public.pyq_topics, public.prelims_pyqs to authenticated;
grant select on public.prelims_pyqs to authenticated;
grant all on public.pyq_subjects, public.pyq_topics, public.prelims_pyqs to service_role;

-- ------------------------------------------------------------ student data --
create table if not exists public.prelims_pyq_answers (
  user_id       uuid not null default auth.uid() references auth.users(id) on delete cascade,
  question_id   uuid not null references public.prelims_pyqs(id) on delete cascade,
  choice        text,
  is_correct    boolean not null,
  first_correct boolean not null,
  attempts      integer not null default 1,
  updated_at    timestamptz not null default now(),
  primary key (user_id, question_id)
);

create table if not exists public.prelims_pyq_marks (
  user_id     uuid not null default auth.uid() references auth.users(id) on delete cascade,
  question_id uuid not null references public.prelims_pyqs(id) on delete cascade,
  created_at  timestamptz not null default now(),
  primary key (user_id, question_id)
);

create table if not exists public.prelims_pyq_sessions (
  id         uuid primary key default gen_random_uuid(),
  user_id    uuid not null default auth.uid() references auth.users(id) on delete cascade,
  mode       text not null check (mode in ('practice', 'test')),
  title      text,
  filters    jsonb not null default '{}'::jsonb,
  total      integer not null,
  correct    integer not null,
  wrong      integer not null,
  skipped    integer not null,
  score      numeric(7, 2) not null,
  max_score  numeric(7, 2) not null,
  seconds    integer not null default 0,
  created_at timestamptz not null default now()
);
create index if not exists prelims_pyq_sessions_user_idx on public.prelims_pyq_sessions (user_id, created_at desc);

alter table public.prelims_pyq_answers enable row level security;
alter table public.prelims_pyq_marks enable row level security;
alter table public.prelims_pyq_sessions enable row level security;
drop policy if exists prelims_pyq_answers_own on public.prelims_pyq_answers;
create policy prelims_pyq_answers_own on public.prelims_pyq_answers for select using (user_id = auth.uid() or public.is_admin());
drop policy if exists prelims_pyq_marks_own on public.prelims_pyq_marks;
create policy prelims_pyq_marks_own on public.prelims_pyq_marks for select using (user_id = auth.uid() or public.is_admin());
drop policy if exists prelims_pyq_sessions_own on public.prelims_pyq_sessions;
create policy prelims_pyq_sessions_own on public.prelims_pyq_sessions for select using (user_id = auth.uid() or public.is_admin());
grant select on public.prelims_pyq_answers, public.prelims_pyq_marks, public.prelims_pyq_sessions to authenticated;
grant all on public.prelims_pyq_answers, public.prelims_pyq_marks, public.prelims_pyq_sessions to service_role;

-- ------------------------------------------------------------ helpers --
/* May the caller see this question's text and answer? */
create or replace function public.pyq_can_read(p_id uuid)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (
    select 1 from public.prelims_pyqs q join public.pyq_subjects s on s.code = q.subject
    where q.id = p_id and q.status = 'published'
      and (q.free_rank is not null and q.free_rank <= s.free_count or public.has_pyq_access()));
$$;
revoke execute on function public.pyq_can_read(uuid) from public;
grant execute on function public.pyq_can_read(uuid) to anon, authenticated, service_role;

-- ------------------------------------------------------------ catalogue --
create or replace function public.pyq_catalog()
returns jsonb
language sql
stable
security definer
set search_path = public
as $$
  with q as (select * from public.prelims_pyqs where status = 'published')
  select jsonb_build_object(
    'plan', (select jsonb_build_object('code', code, 'price', price_paise / 100.0,
                      'mrp', coalesce(mrp_paise, price_paise) / 100.0, 'days', duration_days)
             from public.plans where code = 'pyq-practice' and is_active),
    'access', public.has_pyq_access(),
    'signedIn', auth.uid() is not null,
    'total', (select count(*) from q),
    'years', jsonb_build_array((select min(year) from q), (select max(year) from q)),
    'papers', (select count(distinct exam_label) from q),
    'exams', coalesce((select jsonb_agg(jsonb_build_object('code', e.code, 'label', e.label, 'count', x.c) order by e.sort_order)
                       from (select exam, count(*) c from q group by exam) x join public.exam_categories e on e.code = x.exam), '[]'::jsonb),
    'subjects', coalesce((
      select jsonb_agg(jsonb_build_object(
        'code', s.code, 'name', s.name, 'nameHi', s.name_hi, 'blurb', s.blurb, 'blurbHi', s.blurb_hi,
        'total', (select count(*) from q where q.subject = s.code),
        'free', (select count(*) from q where q.subject = s.code and q.free_rank <= s.free_count),
        'freeCount', s.free_count,
        'upsc', (select count(*) from q where q.subject = s.code and q.exam = 'upsc'),
        'topics', coalesce((
          select jsonb_agg(jsonb_build_object('code', t.code, 'name', t.name, 'nameHi', t.name_hi,
                   'total', (select count(*) from q where (q.subject = s.code and q.topic = t.code)
                                                       or (s.code || '/' || t.code) = any (q.also_topics)))
                 order by t.sort_order)
          from public.pyq_topics t where t.subject_code = s.code), '[]'::jsonb))
        order by s.sort_order)
      from public.pyq_subjects s where s.is_active), '[]'::jsonb));
$$;
revoke execute on function public.pyq_catalog() from public;
grant execute on function public.pyq_catalog() to anon, authenticated, service_role;

/* Every published question of a subject as a light row: enough to filter,
   count and pick a set in the browser, without any text or answer. A
   question filed under another subject but also belonging to this one comes
   too, with this subject's topic. */
create or replace function public.pyq_meta(p_subject text)
returns jsonb
language sql
stable
security definer
set search_path = public
as $$
  select coalesce(jsonb_agg(jsonb_build_object(
    'id', q.id,
    't', (select coalesce(jsonb_agg(distinct x), '[]'::jsonb) from (
            select q.topic as x where q.subject = p_subject
            union all
            select split_part(a, '/', 2) from unnest(q.also_topics) a where split_part(a, '/', 1) = p_subject) z),
    'e', q.exam, 'l', q.exam_label, 'y', q.year, 'k', q.paper_kind,
    'ty', case when q.question_data ? 'pairs' then 'pairs' else q.type end,
    'f', (q.free_rank is not null and q.free_rank <= s.free_count),
    'fr', q.free_rank,
    'r', case when a.question_id is null then null when a.is_correct then 'c' else 'w' end,
    'b', (m.question_id is not null))
    order by q.year desc, q.exam_label, q.ref), '[]'::jsonb)
  from public.prelims_pyqs q
  join public.pyq_subjects s on s.code = q.subject
  left join public.prelims_pyq_answers a on a.question_id = q.id and a.user_id = auth.uid()
  left join public.prelims_pyq_marks m on m.question_id = q.id and m.user_id = auth.uid()
  where q.status = 'published'
    and (q.subject = p_subject or exists (select 1 from unnest(q.also_topics) a2 where split_part(a2, '/', 1) = p_subject));
$$;
revoke execute on function public.pyq_meta(text) from public;
grant execute on function public.pyq_meta(text) to anon, authenticated, service_role;

/* The questions themselves, in the order asked. A question the caller may
   not read comes back as {id, locked: true} and nothing else. */
create or replace function public.pyq_fetch(p_ids uuid[])
returns jsonb
language sql
stable
security definer
set search_path = public
as $$
  select coalesce(jsonb_agg(
    case when public.pyq_can_read(q.id) then jsonb_build_object(
      'id', q.id, 'subject', q.subject, 'topic', q.topic, 'exam', q.exam, 'label', q.exam_label,
      'year', q.year, 'type', q.type, 'body', q.body, 'bodyHi', q.body_hi, 'data', q.question_data,
      'options', q.options, 'answer', q.answer, 'explanation', q.explanation, 'explanationHi', q.explanation_hi,
      'mine', a.choice, 'marked', (m.question_id is not null))
    else jsonb_build_object('id', q.id, 'locked', true, 'label', q.exam_label, 'year', q.year, 'topic', q.topic) end
    order by i.ord), '[]'::jsonb)
  from unnest(p_ids[1:200]) with ordinality as i(id, ord)
  join public.prelims_pyqs q on q.id = i.id and q.status = 'published'
  left join public.prelims_pyq_answers a on a.question_id = q.id and a.user_id = auth.uid()
  left join public.prelims_pyq_marks m on m.question_id = q.id and m.user_id = auth.uid();
$$;
revoke execute on function public.pyq_fetch(uuid[]) from public;
grant execute on function public.pyq_fetch(uuid[]) to anon, authenticated, service_role;

-- ------------------------------------------------------------ answering --
/* One answer in practice mode. Correctness is decided here. */
create or replace function public.pyq_answer(p_id uuid, p_choice text)
returns jsonb
language plpgsql
security definer
set search_path = public
as $$
declare
  v_answer text;
  v_ok boolean;
begin
  if auth.uid() is null then return jsonb_build_object('ok', false, 'reason', 'not_signed_in'); end if;
  if not public.pyq_can_read(p_id) then return jsonb_build_object('ok', false, 'reason', 'locked'); end if;
  select answer into v_answer from public.prelims_pyqs where id = p_id;
  v_ok := lower(coalesce(p_choice, '')) = v_answer;
  insert into public.prelims_pyq_answers as x (user_id, question_id, choice, is_correct, first_correct)
  values (auth.uid(), p_id, lower(p_choice), v_ok, v_ok)
  on conflict (user_id, question_id) do update
    set choice = excluded.choice, is_correct = excluded.is_correct,
        attempts = x.attempts + 1, updated_at = now();
  return jsonb_build_object('ok', true, 'correct', v_ok, 'answer', v_answer);
end;
$$;
revoke execute on function public.pyq_answer(uuid, text) from public, anon;
grant execute on function public.pyq_answer(uuid, text) to authenticated, service_role;

/* The end of a set. In a test the answers arrive together and are recorded
   here; in practice they were recorded one by one, so only the result is kept.
   Scoring is UPSC's: +2 for a right answer, minus a third of that for a wrong
   one, nothing for a skip. */
create or replace function public.pyq_finish(p_mode text, p_title text, p_filters jsonb, p_items jsonb, p_seconds integer)
returns jsonb
language plpgsql
security definer
set search_path = public
as $$
declare
  v_uid uuid := auth.uid();
  it jsonb;
  v_id uuid;
  v_choice text;
  v_answer text;
  v_total int := 0; v_right int := 0; v_wrong int := 0; v_skip int := 0;
  v_score numeric; v_session uuid;
begin
  if v_uid is null then return jsonb_build_object('ok', false, 'reason', 'not_signed_in'); end if;
  if p_mode not in ('practice', 'test') then return jsonb_build_object('ok', false, 'reason', 'bad_mode'); end if;
  if jsonb_typeof(p_items) <> 'array' or jsonb_array_length(p_items) = 0 or jsonb_array_length(p_items) > 200 then
    return jsonb_build_object('ok', false, 'reason', 'bad_items');
  end if;

  for it in select * from jsonb_array_elements(p_items) loop
    begin v_id := (it ->> 'id')::uuid; exception when others then continue; end;
    if not public.pyq_can_read(v_id) then continue; end if;
    select answer into v_answer from public.prelims_pyqs where id = v_id;
    v_choice := nullif(lower(coalesce(it ->> 'choice', '')), '');
    v_total := v_total + 1;
    if v_choice is null then v_skip := v_skip + 1;
    elsif v_choice = v_answer then v_right := v_right + 1;
    else v_wrong := v_wrong + 1; end if;
    if p_mode = 'test' and v_choice is not null then
      insert into public.prelims_pyq_answers as x (user_id, question_id, choice, is_correct, first_correct)
      values (v_uid, v_id, v_choice, v_choice = v_answer, v_choice = v_answer)
      on conflict (user_id, question_id) do update
        set choice = excluded.choice, is_correct = excluded.is_correct,
            attempts = x.attempts + 1, updated_at = now();
    end if;
  end loop;

  if v_total = 0 then return jsonb_build_object('ok', false, 'reason', 'nothing_readable'); end if;
  v_score := round(v_right * 2 - v_wrong * 2.0 / 3, 2);
  insert into public.prelims_pyq_sessions (user_id, mode, title, filters, total, correct, wrong, skipped, score, max_score, seconds)
  values (v_uid, p_mode, left(p_title, 160), coalesce(p_filters, '{}'::jsonb), v_total, v_right, v_wrong, v_skip,
          v_score, v_total * 2, greatest(coalesce(p_seconds, 0), 0))
  returning id into v_session;
  return jsonb_build_object('ok', true, 'id', v_session, 'total', v_total, 'correct', v_right,
                            'wrong', v_wrong, 'skipped', v_skip, 'score', v_score, 'max', v_total * 2);
end;
$$;
revoke execute on function public.pyq_finish(text, text, jsonb, jsonb, integer) from public, anon;
grant execute on function public.pyq_finish(text, text, jsonb, jsonb, integer) to authenticated, service_role;

create or replace function public.pyq_mark(p_id uuid, p_on boolean)
returns boolean
language plpgsql
security definer
set search_path = public
as $$
begin
  if auth.uid() is null then return false; end if;
  if p_on then
    if not exists (select 1 from public.prelims_pyqs where id = p_id and status = 'published') then return false; end if;
    insert into public.prelims_pyq_marks (user_id, question_id) values (auth.uid(), p_id) on conflict do nothing;
  else
    delete from public.prelims_pyq_marks where user_id = auth.uid() and question_id = p_id;
  end if;
  return p_on;
end;
$$;
revoke execute on function public.pyq_mark(uuid, boolean) from public, anon;
grant execute on function public.pyq_mark(uuid, boolean) to authenticated, service_role;

/* The student's own picture: by subject and topic, recent sets, and the days
   they practised in the last four weeks. */
create or replace function public.pyq_progress()
returns jsonb
language sql
stable
security definer
set search_path = public
as $$
  with a as (
    select a.*, q.subject, q.topic from public.prelims_pyq_answers a
    join public.prelims_pyqs q on q.id = a.question_id
    where a.user_id = auth.uid())
  select jsonb_build_object(
    'subjects', coalesce((select jsonb_agg(jsonb_build_object('code', subject, 'done', n, 'right', r)) from (
        select subject, count(*) n, count(*) filter (where is_correct) r from a group by subject) s), '[]'::jsonb),
    'topics', coalesce((select jsonb_agg(jsonb_build_object('subject', subject, 'code', topic, 'done', n, 'right', r)) from (
        select subject, topic, count(*) n, count(*) filter (where is_correct) r from a group by subject, topic) t), '[]'::jsonb),
    'sessions', coalesce((select jsonb_agg(to_jsonb(s) - 'user_id' - 'filters' order by s.created_at desc) from (
        select * from public.prelims_pyq_sessions where user_id = auth.uid() order by created_at desc limit 8) s), '[]'::jsonb),
    'days', coalesce((select jsonb_agg(d order by d) from (
        select distinct (updated_at at time zone 'Asia/Kolkata')::date d from a
        where updated_at > now() - interval '28 days') x), '[]'::jsonb),
    'marked', (select count(*) from public.prelims_pyq_marks where user_id = auth.uid()))
  where auth.uid() is not null;
$$;
revoke execute on function public.pyq_progress() from public, anon;
grant execute on function public.pyq_progress() to authenticated, service_role;

-- ------------------------------------------------------------ seed: subjects --
insert into public.pyq_subjects (code, name, name_hi, blurb, blurb_hi, sort_order, free_count) values
  ('ancient', 'Ancient History', 'प्राचीन इतिहास',
   'From the Stone Age and Harappa to the Guptas and Harsha.',
   'पाषाण युग और हड़प्पा से गुप्त और हर्ष तक।', 10, 10),
  ('medieval', 'Medieval History', 'मध्यकालीन इतिहास',
   'Early medieval kingdoms, the Sultanate, Vijayanagara, the Mughals and the Marathas.',
   'प्रारंभिक मध्यकालीन राज्य, सल्तनत, विजयनगर, मुग़ल और मराठा।', 20, 10),
  ('art-culture', 'Art & Culture', 'कला एवं संस्कृति',
   'Architecture, painting, literature, music and dance, religion and philosophy, coins and festivals.',
   'स्थापत्य, चित्रकला, साहित्य, संगीत और नृत्य, धर्म और दर्शन, सिक्के और त्योहार।', 30, 10)
on conflict (code) do nothing;

insert into public.pyq_topics (subject_code, code, name, name_hi, sort_order) values
  ('ancient', 'prehistory',  'Prehistoric & Harappan',            'प्रागैतिहासिक एवं हड़प्पा', 10),
  ('ancient', 'vedic',       'Vedic Age',                         'वैदिक काल', 20),
  ('ancient', 'religions',   'Buddhism, Jainism & other sects',   'बौद्ध, जैन एवं अन्य संप्रदाय', 30),
  ('ancient', 'maurya',      'Mahajanapadas & Mauryas',           'महाजनपद एवं मौर्य', 40),
  ('ancient', 'post-maurya', 'Post-Mauryan & Sangam Age',         'मौर्योत्तर एवं संगम काल', 50),
  ('ancient', 'gupta',       'Gupta & Post-Gupta',                'गुप्त एवं गुप्तोत्तर काल', 60),
  ('medieval', 'early-medieval', 'Early Medieval Kingdoms',       'प्रारंभिक मध्यकालीन राज्य', 10),
  ('medieval', 'sultanate',      'Delhi Sultanate',               'दिल्ली सल्तनत', 20),
  ('medieval', 'bhakti-sufi',    'Bhakti & Sufi Movements',       'भक्ति एवं सूफ़ी आंदोलन', 30),
  ('medieval', 'vijayanagara',   'Vijayanagara, Bahmani & Deccan','विजयनगर, बहमनी एवं दक्कन', 40),
  ('medieval', 'mughals',        'Mughal Empire',                 'मुग़ल साम्राज्य', 50),
  ('medieval', 'marathas',       'Marathas & 18th-century Powers','मराठा एवं 18वीं सदी की शक्तियाँ', 60),
  ('art-culture', 'architecture', 'Architecture & Sculpture',     'स्थापत्य एवं मूर्तिकला', 10),
  ('art-culture', 'painting',     'Painting',                     'चित्रकला', 20),
  ('art-culture', 'literature',   'Literature',                   'साहित्य', 30),
  ('art-culture', 'performing',   'Music, Dance & Theatre',       'संगीत, नृत्य एवं रंगमंच', 40),
  ('art-culture', 'philosophy',   'Religion & Philosophy',        'धर्म एवं दर्शन', 50),
  ('art-culture', 'bhakti-sufi',  'Bhakti & Sufi',                'भक्ति एवं सूफ़ी', 60),
  ('art-culture', 'coins',        'Coins & Currency',             'सिक्के एवं मुद्रा', 70),
  ('art-culture', 'festivals',    'Fairs, Festivals & Heritage',  'मेले, त्योहार एवं धरोहर', 80),
  ('art-culture', 'science',      'Science, Scripts & Languages', 'विज्ञान, लिपियाँ एवं भाषाएँ', 90),
  ('art-culture', 'misc',         'Miscellaneous',                'विविध', 100)
on conflict do nothing;
