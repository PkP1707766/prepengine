-- The referrer needs to see WHO joined on their link, but `profiles` is
-- readable only by its owner (profiles_select: id = auth.uid() or is_admin()).
-- Widening that policy to expose invitees would leak far more than needed, so
-- this returns a deliberately masked projection instead: enough for the
-- referrer to recognise their own invite, not enough to harvest contact details.
create or replace function public.my_referral_list()
returns table (
  masked_name  text,
  joined_at    timestamptz,
  has_paid     boolean,
  bonus_status text
)
language sql
stable
security definer
set search_path = public
as $fn$
  select
    case
      when coalesce(trim(p.full_name), '') = '' then 'Aspirant'
      else split_part(trim(p.full_name), ' ', 1) ||
           case when position(' ' in trim(p.full_name)) > 0
                then ' ' || upper(substr(split_part(trim(p.full_name), ' ', 2), 1, 1)) || '.'
                else '' end
    end,
    r.created_at,
    exists (select 1 from public.enrollments e
             where e.student_id = r.referred_id and e.status = 'active'),
    r.bonus_status
  from public.referrals r
  join public.profiles p on p.id = r.referred_id
  where r.referrer_id = auth.uid()
  order by r.created_at desc
  limit 200;
$fn$;

revoke execute on function public.my_referral_list() from public, anon;
grant  execute on function public.my_referral_list() to authenticated, service_role;
