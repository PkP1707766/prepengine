-- 0043: the free allowance for the Essay, the same way GS has it (0042).
--
-- The owner's call (2026-11-16): a student without the Essay plan may open
-- any 7 Essay topper copies and any 7 Essay Learn to Write guides of their
-- choice, counted apart from GS's 7 + 7. A locked Essay guide shows its shape
-- (the spine, the dimensions, both sides' labels, every argument title, the
-- kinds of opening and closing) with the prose replaced on the server by
-- filler of the same length, so the words never reach the browser.
--
-- The allowance is generic now: mains_free_status(section) and
-- mains_free_claim(section, kind, item) for section 'gs' or 'essay'.
-- gs_free_status() and gs_free_claim() stay as thin wrappers so the build
-- already live keeps working.

-- ---------------------------------------------------------------- limits --
insert into public.mains_settings (key, value, num) values
  ('essay_free_copies', true, 7),
  ('essay_free_guides', true, 7)
on conflict (key) do nothing;

-- ------------------------------------------------- one table, two sections --
alter table public.mains_free_opens
  add column if not exists section text not null default 'gs';
alter table public.mains_free_opens drop constraint if exists mains_free_opens_section_check;
alter table public.mains_free_opens add constraint mains_free_opens_section_check check (section in ('gs', 'essay'));

/* Has this student opened this copy or guide with a free open? Items are
   uuids unique across sections, so the section is not needed here. */
create or replace function public.mains_free_claimed(p_kind text, p_item uuid)
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
revoke execute on function public.mains_free_claimed(text, uuid) from public;
grant execute on function public.mains_free_claimed(text, uuid) to authenticated, service_role;

create or replace function public.mains_section_access(p_section text, p_user uuid default auth.uid())
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select case when p_section = 'gs' then public.has_gs_access(p_user) else public.has_mains_access(p_user) end;
$$;
revoke execute on function public.mains_section_access(text, uuid) from public;
grant execute on function public.mains_section_access(text, uuid) to authenticated, service_role;

-- ------------------------------------------- copies: paid, free, or claimed --
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
               or public.mains_free_claimed('copy', c.id)
               or case when public.copy_is_gs(c.id) then public.has_gs_access() else public.has_mains_access() end)
      );
$$;
grant execute on function public.can_read_topper_copy(uuid) to anon, authenticated, service_role;

drop policy if exists essay_ltw_read on public.essay_ltw;
create policy essay_ltw_read on public.essay_ltw for select
  using (public.is_admin() or (status = 'published' and (
    public.has_paper_access((select p.paper from public.essay_pyqs p where p.id = pyq_id))
    or public.mains_free_claimed('guide', pyq_id))));

-- ----------------------------------------------------- status and claim --
create or replace function public.mains_free_status(p_section text)
returns jsonb
language sql
stable
security definer
set search_path = public
as $$
  select jsonb_build_object(
    'section', p_section,
    'paid', public.mains_section_access(p_section),
    'copyLimit', coalesce((select num from public.mains_settings where key = p_section || '_free_copies'), 7),
    'guideLimit', coalesce((select num from public.mains_settings where key = p_section || '_free_guides'), 7),
    'copies', coalesce((select jsonb_agg(item_id order by opened_at) from public.mains_free_opens
                         where user_id = auth.uid() and section = p_section and kind = 'copy'), '[]'::jsonb),
    'guides', coalesce((select jsonb_agg(item_id order by opened_at) from public.mains_free_opens
                         where user_id = auth.uid() and section = p_section and kind = 'guide'), '[]'::jsonb))
  where auth.uid() is not null and p_section in ('gs', 'essay');
$$;
revoke execute on function public.mains_free_status(text) from public, anon;
grant execute on function public.mains_free_status(text) to authenticated, service_role;

create or replace function public.mains_free_claim(p_section text, p_kind text, p_item uuid)
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
  if p_section not in ('gs', 'essay') then return jsonb_build_object('ok', false, 'reason', 'bad_section'); end if;
  if p_kind not in ('copy', 'guide') then return jsonb_build_object('ok', false, 'reason', 'bad_kind'); end if;
  if public.mains_section_access(p_section, v_uid) then return jsonb_build_object('ok', true, 'paid', true); end if;

  -- The item must be a published one of this section.
  if p_kind = 'copy' then
    if not exists (select 1 from public.topper_copies c where c.id = p_item and c.is_published)
       or public.copy_is_gs(p_item) <> (p_section = 'gs') then
      return jsonb_build_object('ok', false, 'reason', 'not_found');
    end if;
  else
    if not exists (select 1 from public.essay_ltw l join public.essay_pyqs p on p.id = l.pyq_id
                   where l.pyq_id = p_item and l.status = 'published'
                     and case when p_section = 'gs' then p.paper like 'gs%' else p.paper = 'essay' end) then
      return jsonb_build_object('ok', false, 'reason', 'not_found');
    end if;
  end if;

  -- One student's claims are counted one at a time, so two taps cannot pass the limit.
  perform pg_advisory_xact_lock(hashtext('mains_free:' || v_uid::text));

  if exists (select 1 from public.mains_free_opens where user_id = v_uid and kind = p_kind and item_id = p_item) then
    return jsonb_build_object('ok', true, 'already', true);
  end if;

  v_limit := coalesce((select num from public.mains_settings
                        where key = p_section || case p_kind when 'copy' then '_free_copies' else '_free_guides' end), 7);
  select count(*) into v_used from public.mains_free_opens
   where user_id = v_uid and section = p_section and kind = p_kind;
  if v_used >= v_limit then
    return jsonb_build_object('ok', false, 'reason', 'limit', 'used', v_used, 'limit', v_limit);
  end if;

  insert into public.mains_free_opens (user_id, section, kind, item_id) values (v_uid, p_section, p_kind, p_item);
  return jsonb_build_object('ok', true, 'used', v_used + 1, 'limit', v_limit);
end;
$$;
revoke execute on function public.mains_free_claim(text, text, uuid) from public, anon;
grant execute on function public.mains_free_claim(text, text, uuid) to authenticated, service_role;

-- The GS names stay, as wrappers, for the build already live.
create or replace function public.gs_free_status()
returns jsonb
language sql
stable
security definer
set search_path = public
as $$ select public.mains_free_status('gs'); $$;

create or replace function public.gs_free_claim(p_kind text, p_item uuid)
returns jsonb
language sql
security definer
set search_path = public
as $$ select public.mains_free_claim('gs', p_kind, p_item); $$;

-- ------------------------------------------- the blurred Essay skeleton --
create or replace function public.essay_skeleton(d jsonb)
returns jsonb
language sql
immutable
as $$
  select jsonb_build_object(
    'spine', d -> 'spine',
    'dimensions', coalesce(d -> 'dimensions', '[]'::jsonb),
    'how_to', public.gs_blur_list(d -> 'how_to'),
    'sides', coalesce((select jsonb_agg(jsonb_build_object('label', x -> 'label', 'blurb', public.gs_blur(x ->> 'blurb')) order by o)
                       from jsonb_array_elements(coalesce(d -> 'sides', '[]'::jsonb)) with ordinality e(x, o)), '[]'::jsonb),
    'arguments', coalesce((select jsonb_agg(jsonb_build_object('side', x -> 'side', 'title', x -> 'title',
                              'point', public.gs_blur(x ->> 'point'), 'paragraph', public.gs_blur(x ->> 'paragraph')) order by o)
                           from jsonb_array_elements(coalesce(d -> 'arguments', '[]'::jsonb)) with ordinality e(x, o)), '[]'::jsonb),
    'introductions', public.gs_blur_typed(d -> 'introductions'),
    'conclusions', public.gs_blur_typed(d -> 'conclusions'),
    'pitfalls', public.gs_blur_list(d -> 'pitfalls'));
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
      -- The sides' blurbs are prose: blurred here too, not only in the skeleton.
      'sides', public.essay_skeleton(l.doc) -> 'sides',
      'titles', coalesce((
        select jsonb_agg(jsonb_build_object('side', a -> 'side', 'title', a -> 'title') order by ord)
        from jsonb_array_elements(coalesce(l.doc -> 'arguments', '[]'::jsonb)) with ordinality as x(a, ord)
      ), '[]'::jsonb),
      'introductions', jsonb_array_length(coalesce(l.doc -> 'introductions', '[]'::jsonb)),
      'conclusions', jsonb_array_length(coalesce(l.doc -> 'conclusions', '[]'::jsonb)),
      'skeleton', public.essay_skeleton(l.doc))
  end
  from public.essay_ltw l
  where l.pyq_id = p_pyq
    and l.status = 'published'
    and auth.uid() is not null;
$$;
revoke execute on function public.essay_ltw_preview(uuid) from public, anon;
grant execute on function public.essay_ltw_preview(uuid) to authenticated, service_role;
