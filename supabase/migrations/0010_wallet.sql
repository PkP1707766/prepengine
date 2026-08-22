-- ============================================================================
-- JUNOONIAS — Phase 5: wallet ledger + referral bonus crediting.
--
-- The rule that shapes this file: there is no balance column. A balance is
-- always `sum(amount_paise) where status = 'completed'`, derived on read. A
-- stored balance is a number two code paths can disagree about, and when they
-- disagree it is real money that is wrong.
--
-- Deviation from the spec, consistent with the coupon phase: the spec writes
-- `amount numeric`. Money here stays integer paise like everywhere else in the
-- system, so a bonus cannot pick up float dust on its way through a sum.
-- ============================================================================

create table if not exists public.wallet_transactions (
  id           uuid primary key default gen_random_uuid(),
  student_id   uuid not null references public.profiles(id) on delete cascade,
  amount_paise integer not null,        -- positive = credit, negative = debit
  type         text not null check (type in ('referral_bonus','withdrawal','adjustment','reversal')),
  reference_id uuid,                    -- the referral / withdrawal this line came from
  status       text not null default 'completed'
               check (status in ('pending','completed','reversed')),
  note         text,
  created_at   timestamptz not null default now()
);

create index if not exists wallet_tx_student_idx
  on public.wallet_transactions (student_id, created_at desc);

-- The idempotency guarantee. One referral produces exactly one bonus line,
-- ever — so the browser's confirmation and the Razorpay webhook can both call
-- the credit function for the same payment and only one of them can win.
create unique index if not exists wallet_tx_referral_bonus_uidx
  on public.wallet_transactions (reference_id) where type = 'referral_bonus';

insert into public.app_config (key, value, description) values
  ('referral_reversal_window_days', '7'::jsonb,
   'A refund inside this many days claws the referral bonus back. Beyond it the money may already have been withdrawn.')
on conflict (key) do nothing;

-- ---------------------------------------------------------------------------
-- Balance. Takes a user id, so it is service-role only — a student passing
-- another person's id would otherwise read their balance. Students use
-- my_wallet() below, which cannot be pointed at anyone but the caller.
-- ---------------------------------------------------------------------------
create or replace function public.wallet_balance(p_user uuid)
returns integer
language sql
stable
security definer
set search_path = public
as $fn$
  select coalesce(sum(amount_paise), 0)::int
    from public.wallet_transactions
   where student_id = p_user and status = 'completed';
$fn$;

create or replace function public.my_wallet()
returns table (
  balance_paise      integer,
  lifetime_paise     integer,
  pending_paise      integer,
  bonus_paise        integer,
  min_withdraw_paise integer,
  can_withdraw       boolean,
  has_active_course  boolean
)
language sql
stable
security definer
set search_path = public
as $fn$
  select
    coalesce((select sum(amount_paise) from public.wallet_transactions
               where student_id = auth.uid() and status = 'completed'), 0)::int,
    -- Lifetime earned counts credits only, so a withdrawal does not make it
    -- look as though the student never earned anything.
    coalesce((select sum(amount_paise) from public.wallet_transactions
               where student_id = auth.uid() and status = 'completed'
                 and amount_paise > 0), 0)::int,
    coalesce((select sum(amount_paise) from public.wallet_transactions
               where student_id = auth.uid() and status = 'pending'), 0)::int,
    coalesce((select (value #>> '{}')::int from public.app_config
               where key = 'referral_bonus_paise'), 9900),
    coalesce((select (value #>> '{}')::int from public.app_config
               where key = 'withdrawal_min_paise'), 50000),
    -- Both conditions, evaluated right now. Never cached: eligibility flips on
    -- and off as enrollments expire and renew (fraud rule 8).
    (coalesce((select sum(amount_paise) from public.wallet_transactions
                where student_id = auth.uid() and status = 'completed'), 0)
       >= coalesce((select (value #>> '{}')::int from public.app_config
                     where key = 'withdrawal_min_paise'), 50000))
    and exists (select 1 from public.enrollments e
                 where e.student_id = auth.uid() and e.status = 'active'
                   and (e.expires_at is null or e.expires_at > now())),
    exists (select 1 from public.enrollments e
             where e.student_id = auth.uid() and e.status = 'active'
               and (e.expires_at is null or e.expires_at > now()));
$fn$;

-- ---------------------------------------------------------------------------
-- CREDIT — the only way a referral bonus is ever created.
--
-- Driven by a payment, never by a signup and never by anything the client can
-- say (fraud rule 1). An account that never pays never earns its referrer a
-- rupee.
-- ---------------------------------------------------------------------------
create or replace function public.credit_referral_bonus(p_payment uuid)
returns text
language plpgsql
security definer
set search_path = public
as $fn$
declare
  pay public.payments%rowtype;
  ref public.referrals%rowtype;
  amt integer;
  bal integer;
begin
  select * into pay from public.payments where id = p_payment;
  if pay.id is null       then return 'payment_not_found'; end if;
  if pay.status <> 'paid' then return 'payment_not_paid';  end if;
  if pay.user_id is null  then return 'no_buyer';          end if;

  -- Was this buyer introduced by someone?
  select * into ref from public.referrals where referred_id = pay.user_id;
  if ref.id is null then return 'no_referral'; end if;

  -- One bonus per referred person, not per purchase. Their second and third
  -- bundle do not pay the referrer again.
  if ref.bonus_status <> 'pending' then return 'already_' || ref.bonus_status; end if;

  amt := coalesce((select (value #>> '{}')::int from public.app_config
                    where key = 'referral_bonus_paise'), 9900);

  insert into public.wallet_transactions
    (student_id, amount_paise, type, reference_id, status, note)
  values
    (ref.referrer_id, amt, 'referral_bonus', ref.id, 'completed',
     'Referral bonus — a friend you invited bought a test series')
  on conflict (reference_id) where type = 'referral_bonus' do nothing;

  -- The unique index rejected it: another caller credited this referral first.
  if not found then return 'already_credited'; end if;

  update public.referrals set bonus_status = 'credited' where id = ref.id;

  select public.wallet_balance(ref.referrer_id) into bal;

  insert into public.notifications (user_id, kind, title, body, link)
  values (ref.referrer_id, 'success',
          'Referral bonus credited',
          'Aapke refer se ' || (amt / 100)::text || ' rupee ka bonus mila. Wallet balance ab '
            || (bal / 100)::text || ' rupee hai.',
          '/refer');

  return 'credited';
end;
$fn$;

-- ---------------------------------------------------------------------------
-- REVERSE — refund/chargeback claw-back (fraud rule 4).
--
-- Bounded by a window because beyond it the referrer may already have
-- withdrawn the money, and a reversal would just manufacture a debt nobody can
-- collect. Inside the window a reversal CAN push a balance negative if they
-- withdrew in the meantime; that is intended — the shortfall has to be earned
-- back before the withdrawal threshold is reachable again.
-- ---------------------------------------------------------------------------
create or replace function public.reverse_referral_bonus(p_payment uuid)
returns text
language plpgsql
security definer
set search_path = public
as $fn$
declare
  pay public.payments%rowtype;
  ref public.referrals%rowtype;
  tx  public.wallet_transactions%rowtype;
  win integer;
begin
  select * into pay from public.payments where id = p_payment;
  if pay.id is null or pay.user_id is null then return 'payment_not_found'; end if;

  select * into ref from public.referrals where referred_id = pay.user_id;
  if ref.id is null then return 'no_referral'; end if;

  select * into tx from public.wallet_transactions
   where type = 'referral_bonus' and reference_id = ref.id;
  if tx.id is null          then return 'no_bonus';         end if;
  if tx.status = 'reversed' then return 'already_reversed'; end if;

  win := coalesce((select (value #>> '{}')::int from public.app_config
                    where key = 'referral_reversal_window_days'), 7);
  if now() > tx.created_at + make_interval(days => win) then
    return 'outside_window';
  end if;

  update public.wallet_transactions set status = 'reversed' where id = tx.id;
  update public.referrals set bonus_status = 'reversed' where id = ref.id;

  insert into public.notifications (user_id, kind, title, body, link)
  values (ref.referrer_id, 'info',
          'Referral bonus reversed',
          'Aapke refer kiye gaye student ka payment refund ho gaya, isliye '
            || (tx.amount_paise / 100)::text || ' rupee ka bonus wapas le liya gaya hai.',
          '/refer');

  return 'reversed';
end;
$fn$;

-- ---------------------------------------------------------------------------
-- RLS. Students read their own ledger and nothing else. They can never write
-- to it — every credit and debit comes from a service-role function (rule 5).
-- ---------------------------------------------------------------------------
alter table public.wallet_transactions enable row level security;

drop policy if exists wallet_own_read on public.wallet_transactions;
drop policy if exists wallet_admin    on public.wallet_transactions;

create policy wallet_own_read on public.wallet_transactions for select
  using (student_id = auth.uid() or public.is_admin());
create policy wallet_admin on public.wallet_transactions for all
  using (public.is_admin()) with check (public.is_admin());

revoke all on public.wallet_transactions from anon, authenticated;
grant select on public.wallet_transactions to authenticated;

-- Supabase's default privileges grant new functions to anon+authenticated
-- explicitly, and those survive REVOKE ... FROM PUBLIC. Revoke by name.
revoke execute on function public.credit_referral_bonus(uuid)  from public, anon, authenticated;
revoke execute on function public.reverse_referral_bonus(uuid) from public, anon, authenticated;
revoke execute on function public.wallet_balance(uuid)         from public, anon, authenticated;
revoke execute on function public.my_wallet()                  from public, anon;
grant  execute on function public.credit_referral_bonus(uuid)  to service_role;
grant  execute on function public.reverse_referral_bonus(uuid) to service_role;
grant  execute on function public.wallet_balance(uuid)         to service_role;
grant  execute on function public.my_wallet()                  to authenticated, service_role;
