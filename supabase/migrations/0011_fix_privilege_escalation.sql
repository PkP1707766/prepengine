-- ============================================================================
-- CRITICAL FIX: any signed-in student could make themselves an admin.
--
-- guard_profile_role() was declared SECURITY DEFINER. Inside a SECURITY
-- DEFINER function `current_user` is the function OWNER (postgres), never the
-- caller's role — so the check `current_user in ('anon','authenticated')` was
-- never true, and the guard silently passed every update it was written to
-- stop. The app strips `role` client-side, but that is cosmetic; a
-- hand-written REST call was all it took:
--
--     PATCH /rest/v1/profiles?id=eq.<self>   {"role":"admin"}
--
-- Found by attempting the attack against the live database rather than by
-- reading the policy and assuming it worked.
--
-- Fixed in two independent layers, precisely because one subtly-wrong trigger
-- is what caused this in the first place.
-- ============================================================================

-- Layer 1 — column-level privileges. The hard guarantee: it depends on no
-- trigger, no policy, and no correct detection of the caller's role. Postgres
-- refuses any UPDATE that touches a column the role has no write grant on.
revoke update on public.profiles from anon, authenticated;
grant  update (full_name, phone, email, avatar_url, target_exam, city,
               target_date, prefs, last_seen_at, updated_at)
  on public.profiles to authenticated;

-- `role`, `id`, `created_at` and `referral_code` are deliberately absent from
-- that list: role is privilege, id is identity, created_at is history, and
-- referral_code is the key every rupee of referral money is attributed by.

-- Layer 2 — the trigger, now actually functioning. SECURITY INVOKER so that
-- current_user is the role PostgREST switched to for this request.
create or replace function public.guard_profile_role()
returns trigger
language plpgsql
security invoker
set search_path = public
as $fn$
begin
  -- An admin legitimately changes roles from the admin panel, and service_role
  -- (edge functions) is not a client at all. Everyone else is refused.
  if new.role is distinct from old.role
     and current_user in ('anon', 'authenticated')
     and not public.is_admin() then
    raise exception 'role cannot be changed from the client';
  end if;
  new.updated_at := now();
  return new;
end;
$fn$;

revoke execute on function public.guard_profile_role() from public, anon, authenticated;
