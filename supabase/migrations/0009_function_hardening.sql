-- Two classes of advisor warning, both cheap to close.
--
-- 1. Trigger functions were reachable as PostgREST RPCs (/rest/v1/rpc/...).
--    Calling one that way errors out ("can only be called as a trigger"), so
--    this is surface rather than a live hole — but it is surface with no
--    reason to exist. Verified first, on a scratch table, that PostgreSQL does
--    NOT re-check EXECUTE when a trigger fires, so revoking cannot break
--    signup or any other write path that depends on these.
revoke execute on function public.set_referral_code()   from public, anon, authenticated;
revoke execute on function public.handle_new_user()     from public, anon, authenticated;
revoke execute on function public.guard_profile_role()  from public, anon, authenticated;
revoke execute on function public.log_study_activity()  from public, anon, authenticated;
revoke execute on function public.touch_updated_at()    from public, anon, authenticated;
revoke execute on function public.sync_test_counters()  from public, anon, authenticated;

-- 2. Mutable search_path. ALTER rather than CREATE OR REPLACE so the function
--    bodies are untouched.
alter function public.gen_referral_code()      set search_path = public;
alter function public.touch_updated_at()       set search_path = public;
alter function public.sync_test_counters()     set search_path = public;
alter function public.is_enrolled(uuid)        set search_path = public;
