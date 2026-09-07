-- ============================================================================
-- QA TESTER ACCESS — internal accounts that can attempt any test, in any
-- exam bundle, without buying anything. For pre-launch QA: does a paper
-- render correctly, does the timer/submission work, is post-submission
-- scoring right.
--
-- `can_access_test()` is the single choke point every access path already
-- goes through (exam_paper(), submit-attempt, and the exam-integrity/paper-
-- generation functions all call it; nothing else independently re-implements
-- entitlement). One short-circuit here covers all of them, for every current
-- and future exam bundle, with no per-plan enrollment rows.
--
-- A real bug surfaced while wiring this up, fixed in the same place:
-- `submit-attempt` calls `can_access_test` on a pure service-role client with
-- no user JWT forwarded, so `auth.uid()` was NULL inside that one call —
-- meaning the admin/tester/enrollment branches were silently unreachable from
-- submission, and only a *free* test could ever be submitted, for anyone.
-- (The `attempts` table has zero rows in production, which is consistent
-- with this never having been exercised against a paid test.) Fixed by
-- threading the caller's id through explicitly, defaulting to auth.uid() so
-- every existing 1-argument caller — exam_paper(), the exam-integrity and
-- paper-generation functions, and any future RLS use — is unaffected.
-- ============================================================================

-- ---------------------------------------------------------------------------
-- 1. The flag. Off by default; never implies `role = 'admin'`.
-- ---------------------------------------------------------------------------
alter table public.profiles
  add column if not exists is_tester boolean not null default false;

-- ---------------------------------------------------------------------------
-- 2. Client-side guard. Two layers, matching how `role` is protected —
--    Layer 1 (the real guarantee) is that `is_tester` is deliberately absent
--    from the `grant update (...) to authenticated` column list added in
--    0011_fix_privilege_escalation.sql: a bare Postgres grant, so a PATCH
--    touching this column is refused before any trigger runs. Do not add
--    `is_tester` to that grant list. Layer 2 is this trigger, for a clear
--    error instead of a bare permission-denied. Unlike `role`, there is no
--    admin-panel carve-out — granting/revoking tester status is a deliberate,
--    manual, SQL-editor-only action (see the revoke command shipped with this
--    feature), never a client-reachable toggle, not even for an admin.
-- ---------------------------------------------------------------------------
create or replace function public.guard_profile_role()
returns trigger
language plpgsql
security invoker
set search_path = public
as $fn$
begin
  if new.role is distinct from old.role
     and current_user in ('anon', 'authenticated')
     and not public.is_admin() then
    raise exception 'role cannot be changed from the client';
  end if;
  if new.is_tester is distinct from old.is_tester
     and current_user in ('anon', 'authenticated') then
    raise exception 'is_tester cannot be changed from the client';
  end if;
  new.updated_at := now();
  return new;
end;
$fn$;

revoke execute on function public.guard_profile_role() from public, anon, authenticated;

-- ---------------------------------------------------------------------------
-- 3. is_tester(): same shape as is_admin(), parameterised so a service-role
--    caller (an edge function, with no JWT-derived auth.uid()) can pass the
--    id it already validated instead of silently checking nobody.
-- ---------------------------------------------------------------------------
create or replace function public.is_tester(p_user uuid default auth.uid())
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (
    select 1 from public.profiles
    where id = p_user and is_tester
  );
$$;

grant execute on function public.is_tester(uuid) to anon, authenticated, service_role;

-- ---------------------------------------------------------------------------
-- 4. can_access_test(): add the tester short-circuit, and thread p_user
--    through the enrollment check for the same reason is_tester needs it.
--    (is_admin() is deliberately left untouched — it is inlined into ~30
--    live RLS policies and cannot safely be given a new signature without
--    rewriting all of them. Its branch here stays auth.uid()-only, so an
--    admin account specifically hitting submit-attempt for a non-free test
--    is the one narrow case this migration does not also fix. Admins are
--    staff, not the QA accounts this feature is for, and can be given
--    is_tester too if that ever matters.)
--
--    Dropped and recreated (not `create or replace`) because adding a
--    parameter changes the signature — `can_access_test(uuid)` and
--    `can_access_test(uuid, uuid)` would otherwise coexist as two distinct
--    overloads, and every existing 1-argument call site would keep resolving
--    to the OLD one, silently. Confirmed via pg_depend that nothing (no view,
--    no policy) hard-depends on the old signature, so the drop is safe.
-- ---------------------------------------------------------------------------
drop function if exists public.can_access_test(uuid);

create function public.can_access_test(p_test uuid, p_user uuid default auth.uid())
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select
    public.is_admin()
    or public.is_tester(p_user)
    or exists (select 1 from public.tests t where t.id = p_test and t.is_free and t.is_published)
    or exists (
      select 1
      from public.plan_tests pt
      join public.enrollments e
        on e.plan_code = pt.plan_code
       and e.student_id = p_user
       and e.status = 'active'
       and (e.expires_at is null or e.expires_at > now())
      where pt.test_id = p_test
    );
$$;

grant execute on function public.can_access_test(uuid, uuid) to anon, authenticated, service_role;

-- ---------------------------------------------------------------------------
-- 5. The two accounts. Keyed on auth.users, not profiles.email, so this
--    still works if a profile row's email was never backfilled (see 0001's
--    note on the same footgun for the admin grant).
--
--    Deliberately NOT touched: `role` (stays 'student'; is_tester is content-
--    access only, never backend/admin access) and `enrollments` (no row is
--    inserted — these accounts stay enrollment-less, so referral/withdrawal
--    eligibility, which reads `enrollments` directly, never counts them as
--    paying customers).
-- ---------------------------------------------------------------------------
update public.profiles p
   set is_tester = true
  from auth.users u
 where u.id = p.id
   and u.email in ('rjpranav201297@gmail.com', 'eranupam2000@gmail.com');
