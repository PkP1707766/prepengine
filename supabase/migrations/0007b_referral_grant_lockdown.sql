-- Follow-up to 0007. Supabase ships ALTER DEFAULT PRIVILEGES granting ALL on
-- new functions and tables in `public` to anon/authenticated. Revoking from
-- PUBLIC (the phase-3 fix) does not touch those explicit role grants, so they
-- have to be revoked by name too.
--
-- Neither function leaks anything to anon as it stands — both key off
-- auth.uid() and return nothing without a session — but the grant should match
-- the intent rather than relying on the function body to be defensive.
revoke execute on function public.bind_referral(text)  from anon;
revoke execute on function public.my_referral_stats()  from anon;

-- Least privilege on the tables. RLS already denies student writes, but the
-- grants should not be the only thing between a future careless policy and a
-- student writing their own referral rows.
revoke all on public.referrals from anon, authenticated;
grant select on public.referrals to authenticated;

revoke all on public.app_config from anon, authenticated;
grant select on public.app_config to anon, authenticated;
