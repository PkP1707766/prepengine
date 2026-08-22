-- ============================================================================
-- JUNOONIAS — Phase 4: referral capture and binding.
--
-- Tracking only. No wallet, no bonus, no payout yet — those are phases 5 and 6.
-- What this establishes is the thing everything later depends on: a permanent,
-- unforgeable record of who introduced whom.
--
-- Three rules from the spec shape the whole file:
--   * The code travels in a ?ref= link and is applied automatically. There is
--     no "enter a referral code" field anywhere, by design.
--   * Binding happens once and can never be changed afterwards.
--   * Self-referral is blocked — including the same person using a second
--     account with their own email or phone.
-- ============================================================================

-- ---------------------------------------------------------------------------
-- 1. Every profile gets its own code.
-- ---------------------------------------------------------------------------
alter table public.profiles add column if not exists referral_code text;

do $$ begin
  alter table public.profiles add constraint profiles_referral_code_key unique (referral_code);
exception when duplicate_object then null; end $$;

/* 8 characters from an alphabet with no 0/O/1/I/L — these codes get read off
   phone screens and dictated over the phone. */
create or replace function public.gen_referral_code()
returns text
language plpgsql
volatile
as $$
declare
  alphabet constant text := 'ABCDEFGHJKMNPQRSTUVWXYZ23456789';
  candidate text;
  i integer;
begin
  loop
    candidate := '';
    for i in 1..8 loop
      candidate := candidate || substr(alphabet, 1 + floor(random() * length(alphabet))::int, 1);
    end loop;
    exit when not exists (select 1 from public.profiles where referral_code = candidate);
  end loop;
  return candidate;
end;
$$;

create or replace function public.set_referral_code()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  if new.referral_code is null then
    new.referral_code := public.gen_referral_code();
  end if;
  return new;
end;
$$;

drop trigger if exists profiles_set_referral_code on public.profiles;
create trigger profiles_set_referral_code
  before insert on public.profiles
  for each row execute function public.set_referral_code();

-- Existing students get one too — the share link has to work for everybody
-- from the moment this ships, not only for people who sign up after it.
update public.profiles
   set referral_code = public.gen_referral_code()
 where referral_code is null;

-- ---------------------------------------------------------------------------
-- 2. The binding record.
--
-- `referred_id` is UNIQUE: that constraint, not application code, is what
-- makes "one referrer per person, set once" true.
-- ---------------------------------------------------------------------------
create table if not exists public.referrals (
  id                 uuid primary key default gen_random_uuid(),
  referrer_id        uuid not null references public.profiles(id) on delete cascade,
  referred_id        uuid not null unique references public.profiles(id) on delete cascade,
  referral_code_used text not null,
  bonus_status       text not null default 'pending'
                     check (bonus_status in ('pending', 'credited', 'reversed', 'blocked')),
  created_at         timestamptz not null default now(),
  constraint referrals_no_self check (referrer_id <> referred_id)
);
create index if not exists referrals_referrer_idx on public.referrals (referrer_id);

-- ---------------------------------------------------------------------------
-- 3. Config — the bonus amount lives in a table so it can change without a
--    redeploy. Nothing spends it yet; the student-facing copy reads it so the
--    promise on screen and the payout logic later share one number.
-- ---------------------------------------------------------------------------
create table if not exists public.app_config (
  key         text primary key,
  value       jsonb not null,
  description text,
  updated_at  timestamptz not null default now()
);

insert into public.app_config (key, value, description) values
  ('referral_bonus_paise', '9900'::jsonb, 'Credited to the referrer when a referred student completes a paid enrollment.'),
  ('withdrawal_min_paise', '50000'::jsonb, 'Wallet balance required before a withdrawal can be requested.')
on conflict (key) do nothing;

-- ---------------------------------------------------------------------------
-- 4. BIND — the only way a referral is ever created.
--
-- Deliberately keyed on auth.uid() rather than taking a user id: a caller can
-- only ever bind their OWN account, so exposing this to signed-in users is
-- safe. It is idempotent and refuses every abuse case rather than throwing.
-- ---------------------------------------------------------------------------
create or replace function public.bind_referral(p_code text)
returns text
language plpgsql
security definer
set search_path = public
as $$
declare
  me        uuid := auth.uid();
  my_email  text;
  my_phone  text;
  ref       public.profiles%rowtype;
  code      text := upper(trim(coalesce(p_code, '')));
begin
  if me is null then return 'not_signed_in'; end if;
  if code = '' then return 'no_code'; end if;

  -- One referrer per person, ever. Already bound is a success, not an error —
  -- the client calls this on every login and must not see it as a failure.
  if exists (select 1 from public.referrals where referred_id = me) then
    return 'already_bound';
  end if;

  select * into ref from public.profiles where referral_code = code;
  if ref.id is null then return 'invalid_code'; end if;
  if ref.id = me then return 'self_referral'; end if;

  -- Same human, second account: block when the two accounts share an email or
  -- a phone number. Cheap to check, and it closes the laziest form of fraud.
  select p.email, p.phone into my_email, my_phone from public.profiles p where p.id = me;
  if (my_email is not null and ref.email is not null and lower(my_email) = lower(ref.email))
     or (my_phone is not null and ref.phone is not null and my_phone = ref.phone) then
    return 'self_referral';
  end if;

  insert into public.referrals (referrer_id, referred_id, referral_code_used)
  values (ref.id, me, code)
  on conflict (referred_id) do nothing;

  return 'bound';
end;
$$;

-- ---------------------------------------------------------------------------
-- 5. Summary for the student's own share card.
-- ---------------------------------------------------------------------------
create or replace function public.my_referral_stats()
returns table (
  code            text,
  total_referred  integer,
  paid_referred   integer,
  pending_bonus   integer,
  bonus_paise     integer
)
language sql
stable
security definer
set search_path = public
as $$
  select
    p.referral_code,
    (select count(*) from public.referrals r where r.referrer_id = p.id)::int,
    -- "Paid" means the referred student actually bought something. That is the
    -- only kind of referral that will ever be worth money.
    (select count(*) from public.referrals r
      join public.enrollments e on e.student_id = r.referred_id and e.status = 'active'
     where r.referrer_id = p.id)::int,
    (select count(*) from public.referrals r
      where r.referrer_id = p.id and r.bonus_status = 'pending')::int,
    coalesce((select (value #>> '{}')::int from public.app_config
               where key = 'referral_bonus_paise'), 9900)
  from public.profiles p
  where p.id = auth.uid();
$$;

-- ---------------------------------------------------------------------------
-- 6. RLS
-- ---------------------------------------------------------------------------
alter table public.referrals  enable row level security;
alter table public.app_config enable row level security;

drop policy if exists referrals_read   on public.referrals;
drop policy if exists referrals_admin  on public.referrals;
drop policy if exists app_config_read  on public.app_config;
drop policy if exists app_config_admin on public.app_config;

-- A student can see the referrals they made and the one that made them —
-- never anybody else's.
create policy referrals_read on public.referrals for select
  using (referrer_id = auth.uid() or referred_id = auth.uid() or public.is_admin());
create policy referrals_admin on public.referrals for all
  using (public.is_admin()) with check (public.is_admin());

create policy app_config_read  on public.app_config for select using (true);
create policy app_config_admin on public.app_config for all
  using (public.is_admin()) with check (public.is_admin());

-- Function grants: PUBLIC gets EXECUTE by default on every new function, which
-- is wider than intended. Narrow it explicitly (the coupon phase learned this
-- the hard way).
revoke execute on function public.gen_referral_code()   from public;
revoke execute on function public.bind_referral(text)   from public;
revoke execute on function public.my_referral_stats()   from public;
grant  execute on function public.bind_referral(text)   to authenticated, service_role;
grant  execute on function public.my_referral_stats()   to authenticated, service_role;
grant  execute on function public.gen_referral_code()   to service_role;

grant select on public.app_config to anon, authenticated;
