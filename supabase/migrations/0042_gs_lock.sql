-- 0042: the GS lock, made ready (but not switched on).
--
-- The owner's call (2026-11-16):
--   * GS alone Rs 1,999 (MRP Rs 5,999); Essay alone stays Rs 999 (MRP 1,999);
--     Essay + GS combo Rs 2,499 (MRP Rs 4,998, i.e. 50% off). 365 days each.
--     Prices stay editable from the admin plan screen.
--   * A student without GS gets 7 topper copies and 7 Learn to Write guides
--     of their own choosing, free. After that the rest stay locked.
--   * A locked guide still shows its shape: the question, the parts, every
--     section and heading. The text under them is blurred. The server sends
--     filler of the same length, never the real words, so nothing leaks.
--
-- Nothing here locks GS. While mains_settings.gs_open is true, has_gs_access()
-- is true for every signed-in student and none of this is visible. The lock
-- itself is still:
--     update public.plans set is_active = true where code in ('mains-gs', 'mains-combo');
--     update public.mains_settings set value = false where key = 'gs_open';
--
-- It also fixes a gap: a GS topper copy's pages and text were gated by the
-- Essay entitlement (has_mains_access), so even with GS open nobody without
-- an Essay plan could read a GS copy. A copy now follows its own paper.

-- ---------------------------------------------------------------- limits --
alter table public.mains_settings add column if not exists num integer;
insert into public.mains_settings (key, value, num) values
  ('gs_free_copies', true, 7),
  ('gs_free_guides', true, 7)
on conflict (key) do nothing;

-- ---------------------------------------------------------- free opens --
create table if not exists public.mains_free_opens (
  user_id    uuid not null default auth.uid() references auth.users(id) on delete cascade,
  kind       text not null check (kind in ('copy', 'guide')),
  item_id    uuid not null,
  opened_at  timestamptz not null default now(),
  primary key (user_id, kind, item_id)
);
alter table public.mains_free_opens enable row level security;
drop policy if exists mains_free_opens_own on public.mains_free_opens;
create policy mains_free_opens_own on public.mains_free_opens for select
  using (user_id = auth.uid() or public.is_admin());
grant select on public.mains_free_opens to authenticated;
grant all on public.mains_free_opens to service_role;
-- Rows are written only by gs_free_claim(), which checks the limit.

create or replace function public.gs_free_claimed(p_kind text, p_item uuid)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select auth.uid() is not null and exists (
    select 1 from public.mains_free_opens
    where user_id = auth.uid() and kind = p_kind and item_id = p_item);
$$;
revoke execute on function public.gs_free_claimed(text, uuid) from public;
grant execute on function public.gs_free_claimed(text, uuid) to authenticated, service_role;

/* Is this topper copy a GS copy? A copy holds one paper's answers. */
create or replace function public.copy_is_gs(p_copy uuid)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (select 1 from public.topper_answers a where a.copy_id = p_copy and a.paper like 'gs%');
$$;
revoke execute on function public.copy_is_gs(uuid) from public;
grant execute on function public.copy_is_gs(uuid) to anon, authenticated, service_role;

-- ------------------------------------------- copies follow their paper --
create or replace function public.can_read_topper_copy(p_copy uuid)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select public.is_admin()
      or exists (
        select 1 from public.topper_copies c
        where c.id = p_copy
          and c.is_published
          and (c.is_free
               or case when public.copy_is_gs(c.id)
                       then public.has_gs_access() or public.gs_free_claimed('copy', c.id)
                       else public.has_mains_access() end)
      );
$$;
grant execute on function public.can_read_topper_copy(uuid) to anon, authenticated, service_role;

-- ------------------------------------------ guides: paid or claimed --
drop policy if exists essay_ltw_read on public.essay_ltw;
create policy essay_ltw_read on public.essay_ltw for select
  using (public.is_admin() or (status = 'published' and (
    public.has_paper_access((select p.paper from public.essay_pyqs p where p.id = pyq_id))
    or public.gs_free_claimed('guide', pyq_id))));

-- ------------------------------------------------------ claim / status --
create or replace function public.gs_free_status()
returns jsonb
language sql
stable
security definer
set search_path = public
as $$
  select jsonb_build_object(
    'paid', public.has_gs_access(),
    'copyLimit', coalesce((select num from public.mains_settings where key = 'gs_free_copies'), 7),
    'guideLimit', coalesce((select num from public.mains_settings where key = 'gs_free_guides'), 7),
    'copies', coalesce((select jsonb_agg(item_id order by opened_at) from public.mains_free_opens
                         where user_id = auth.uid() and kind = 'copy'), '[]'::jsonb),
    'guides', coalesce((select jsonb_agg(item_id order by opened_at) from public.mains_free_opens
                         where user_id = auth.uid() and kind = 'guide'), '[]'::jsonb))
  where auth.uid() is not null;
$$;
revoke execute on function public.gs_free_status() from public, anon;
grant execute on function public.gs_free_status() to authenticated, service_role;

create or replace function public.gs_free_claim(p_kind text, p_item uuid)
returns jsonb
language plpgsql
security definer
set search_path = public
as $$
declare
  v_uid   uuid := auth.uid();
  v_limit integer;
  v_used  integer;
begin
  if v_uid is null then return jsonb_build_object('ok', false, 'reason', 'not_signed_in'); end if;
  if p_kind not in ('copy', 'guide') then return jsonb_build_object('ok', false, 'reason', 'bad_kind'); end if;
  if public.has_gs_access(v_uid) then return jsonb_build_object('ok', true, 'paid', true); end if;

  if p_kind = 'copy' then
    if not exists (select 1 from public.topper_copies c where c.id = p_item and c.is_published)
       or not public.copy_is_gs(p_item) then
      return jsonb_build_object('ok', false, 'reason', 'not_found');
    end if;
  else
    if not exists (select 1 from public.essay_ltw l join public.essay_pyqs p on p.id = l.pyq_id
                   where l.pyq_id = p_item and l.status = 'published' and p.paper like 'gs%') then
      return jsonb_build_object('ok', false, 'reason', 'not_found');
    end if;
  end if;

  -- One student's claims are counted one at a time, so two taps cannot pass the limit.
  perform pg_advisory_xact_lock(hashtext('gs_free:' || v_uid::text));

  if exists (select 1 from public.mains_free_opens where user_id = v_uid and kind = p_kind and item_id = p_item) then
    return jsonb_build_object('ok', true, 'already', true);
  end if;

  v_limit := coalesce((select num from public.mains_settings
                        where key = case p_kind when 'copy' then 'gs_free_copies' else 'gs_free_guides' end), 7);
  select count(*) into v_used from public.mains_free_opens where user_id = v_uid and kind = p_kind;
  if v_used >= v_limit then
    return jsonb_build_object('ok', false, 'reason', 'limit', 'used', v_used, 'limit', v_limit);
  end if;

  insert into public.mains_free_opens (user_id, kind, item_id) values (v_uid, p_kind, p_item);
  return jsonb_build_object('ok', true, 'used', v_used + 1, 'limit', v_limit);
end;
$$;
revoke execute on function public.gs_free_claim(text, uuid) from public, anon;
grant execute on function public.gs_free_claim(text, uuid) to authenticated, service_role;

-- ------------------------------------------------ the blurred skeleton --
/* Filler with the same number of words as t: the real text never leaves. */
create or replace function public.gs_blur(t text)
returns text
language sql
immutable
as $$
  select case when coalesce(btrim(t), '') = '' then '' else (
    select string_agg(w[(i % array_length(w, 1)) + 1], ' ' order by i)
    from (select array['lorem','ipsum','dolor','sit','amet','consectetur','adipiscing','elit','sed','do',
                       'eiusmod','tempor','incididunt','ut','labore','et','dolore','magna','aliqua','enim',
                       'minim','veniam','quis','nostrud','exercitation','ullamco','laboris','nisi','aliquip','commodo'] as w) a,
         generate_series(0, array_length(regexp_split_to_array(btrim(t), '\s+'), 1) - 1) as i
  ) end;
$$;

create or replace function public.gs_blur_list(a jsonb)
returns jsonb
language sql
immutable
as $$
  select coalesce(jsonb_agg(to_jsonb(public.gs_blur(x)) order by o), '[]'::jsonb)
  from jsonb_array_elements_text(case when jsonb_typeof(a) = 'array' then a else '[]'::jsonb end) with ordinality as e(x, o);
$$;

/* Typed variants ({type, text}) keep their type and lose their words. */
create or replace function public.gs_blur_typed(a jsonb)
returns jsonb
language sql
immutable
as $$
  select coalesce(jsonb_agg(jsonb_build_object('type', x -> 'type', 'text', public.gs_blur(x ->> 'text')) order by o), '[]'::jsonb)
  from jsonb_array_elements(case when jsonb_typeof(a) = 'array' then a else '[]'::jsonb end) with ordinality as e(x, o);
$$;

create or replace function public.gs_skeleton(d jsonb)
returns jsonb
language sql
immutable
as $$
  select jsonb_build_object(
    'kind', d -> 'kind', 'directive', d -> 'directive', 'demand', d -> 'demand',
    'parts', coalesce(d -> 'parts', '[]'::jsonb),
    'conclusion', public.gs_blur_typed(d -> 'conclusion'),
    'pitfalls', public.gs_blur_list(d -> 'pitfalls'))
  || case when d ->> 'kind' = 'gs-case' then jsonb_build_object(
    'facts', public.gs_blur_list(d -> 'facts'),
    'stakeholders', coalesce((select jsonb_agg(jsonb_build_object('who', x -> 'who', 'stake', public.gs_blur(x ->> 'stake')) order by o)
                              from jsonb_array_elements(coalesce(d -> 'stakeholders', '[]'::jsonb)) with ordinality e(x, o)), '[]'::jsonb),
    'issues', coalesce((select jsonb_agg(jsonb_build_object('heading', x -> 'heading', 'note', public.gs_blur(x ->> 'note')) order by o)
                        from jsonb_array_elements(coalesce(d -> 'issues', '[]'::jsonb)) with ordinality e(x, o)), '[]'::jsonb),
    'options', coalesce((select jsonb_agg(jsonb_build_object('option', public.gs_blur(x ->> 'option'),
                                  'merits', public.gs_blur_list(x -> 'merits'), 'demerits', public.gs_blur_list(x -> 'demerits')) order by o)
                         from jsonb_array_elements(coalesce(d -> 'options', '[]'::jsonb)) with ordinality e(x, o)), '[]'::jsonb),
    'course', public.gs_blur_list(d -> 'course'),
    'values', public.gs_blur_list(d -> 'values'))
  else jsonb_build_object(
    'intro', public.gs_blur_typed(d -> 'intro'),
    'body', coalesce((select jsonb_agg(jsonb_build_object('heading', x -> 'heading', 'points', public.gs_blur_list(x -> 'points')) order by o)
                      from jsonb_array_elements(coalesce(d -> 'body', '[]'::jsonb)) with ordinality e(x, o)), '[]'::jsonb),
    'value_adds', public.gs_blur_typed(d -> 'value_adds'),
    'way_forward', public.gs_blur_list(d -> 'way_forward'),
    'keywords', public.gs_blur_list(d -> 'keywords'))
  end;
$$;

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
      ), '[]'::jsonb),
      'skeleton', public.gs_skeleton(l.doc))
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

-- ----------------------------------------------------------------- plans --
update public.plans
   set price_paise = 199900, mrp_paise = 599900, duration_days = 365
 where code = 'mains-gs';

insert into public.plans (
  code, name, name_hi, tagline, tagline_hi, description, description_hi,
  price_paise, mrp_paise, currency, duration_days, features,
  is_active, sort_order, exam_category, includes_mains, includes_gs
) values (
  'mains-combo',
  'UPSC Mains Essay + General Studies',
  'UPSC मेन्स निबंध + सामान्य अध्ययन',
  'The whole of JUNOONIAS Mains: the Essay and GS I to IV, with toppers'' copies and Learn to Write guides.',
  'पूरा JUNOONIAS मेन्स: निबंध और GS I से IV, टॉपर्स की कॉपियों और लर्न टू राइट गाइड्स के साथ।',
  'Everything in the Essay plan and the GS plan together: every UPSC Essay and GS question by topic, toppers'' answer copies, Learn to Write guides, the Essay Wiki and the GS Fact Bank.',
  'निबंध प्लान और GS प्लान की हर चीज़ एक साथ: विषय के अनुसार UPSC के हर निबंध और GS प्रश्न, टॉपर्स की उत्तर कॉपियाँ, लर्न टू राइट गाइड्स, निबंध विकी और GS तथ्य कोश।',
  249900, 499800, 'INR', 365,
  '["The Essay and GS Paper I to IV, by topic and by year", "Toppers'' answer copies and Learn to Write guides for both", "Essay Wiki and GS Fact Bank", "365 days of access"]'::jsonb,
  false, 90, 'upsc', true, true
)
on conflict (code) do nothing;
