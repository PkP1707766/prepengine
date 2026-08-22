-- ============================================================================
-- JUNOONIAS — Phase 3: coupons.
--
-- The one rule that shapes this whole file: the browser sends a code, never a
-- price. Everything about what that code is worth is decided in Postgres and
-- read by the order-creation edge function.
--
-- Two deliberate departures from the written spec:
--
--  1. The spec puts `unique (coupon_id, student_id)` on redemptions to enforce
--     max_uses_per_user. That only works when the limit is exactly 1 — the
--     moment an admin sets max_uses_per_user = 2 the constraint blocks the
--     second legitimate use. The uniqueness here is on (coupon_id, payment_id)
--     instead, which is what actually needs to be idempotent (a webhook that
--     fires twice must not double-count), and the per-user limit is enforced
--     by a counted check inside redeem_coupon().
--
--  2. Money stays integer paise, like the rest of the system. A 33% coupon on
--     ₹499 is 16467 paise off, exactly — no float dust on an invoice.
-- ============================================================================

create table if not exists public.coupons (
  id                    uuid primary key default gen_random_uuid(),
  code                  text unique not null,
  description           text,
  discount_type         text not null check (discount_type in ('percent', 'flat')),
  discount_value        numeric not null check (discount_value > 0),
  max_discount_paise    integer,          -- caps a percent coupon; null = uncapped
  min_order_paise       integer not null default 0,
  applicable_plan_codes text[],           -- null/empty = every bundle
  max_uses              integer,          -- null = unlimited
  used_count            integer not null default 0,
  max_uses_per_user     integer not null default 1,
  valid_from            timestamptz not null default now(),
  valid_until           timestamptz,
  is_active             boolean not null default true,
  created_by            uuid references auth.users(id) on delete set null,
  created_at            timestamptz not null default now()
);

-- Codes are matched case-insensitively; students type them in every casing.
create unique index if not exists coupons_code_lower_uidx on public.coupons (lower(code));

create table if not exists public.coupon_redemptions (
  id             uuid primary key default gen_random_uuid(),
  coupon_id      uuid not null references public.coupons(id) on delete cascade,
  student_id     uuid not null references auth.users(id) on delete cascade,
  payment_id     uuid references public.payments(id) on delete set null,
  discount_paise integer not null default 0,
  redeemed_at    timestamptz not null default now()
);

-- Idempotency: one redemption per payment, so a replayed webhook cannot
-- burn a second use of the same coupon.
create unique index if not exists coupon_redemption_payment_uidx
  on public.coupon_redemptions (coupon_id, payment_id) where payment_id is not null;
create index if not exists coupon_redemption_user_idx
  on public.coupon_redemptions (coupon_id, student_id);

alter table public.payments
  add column if not exists coupon_id      uuid references public.coupons(id) on delete set null,
  add column if not exists discount_paise integer not null default 0,
  add column if not exists gross_paise    integer;

-- ---------------------------------------------------------------------------
-- QUOTE — the single source of truth for what a code is worth.
--
-- Used by the checkout preview AND by order creation, so the price a student
-- is shown and the price they are charged can never drift apart.
-- ---------------------------------------------------------------------------
create or replace function public.coupon_quote(p_code text, p_plan text, p_user uuid)
returns table (
  valid          boolean,
  reason         text,
  coupon_id      uuid,
  code           text,
  gross_paise    integer,
  discount_paise integer,
  final_paise    integer,
  label          text
)
language plpgsql
stable
security definer
set search_path = public
as $$
declare
  c      public.coupons%rowtype;
  price  integer;
  disc   integer;
  used_by_user integer;
begin
  select p.price_paise into price from public.plans p
   where p.code = p_plan and p.is_active;

  if price is null then
    return query select false, 'plan_not_found', null::uuid, null::text, 0, 0, 0, null::text;
    return;
  end if;

  select * into c from public.coupons
   where lower(coupons.code) = lower(trim(p_code));

  if c.id is null then
    return query select false, 'not_found', null::uuid, null::text, price, 0, price, null::text;
    return;
  end if;

  if not c.is_active then
    return query select false, 'inactive', c.id, c.code, price, 0, price, null::text; return;
  end if;
  if now() < c.valid_from then
    return query select false, 'not_started', c.id, c.code, price, 0, price, null::text; return;
  end if;
  if c.valid_until is not null and now() > c.valid_until then
    return query select false, 'expired', c.id, c.code, price, 0, price, null::text; return;
  end if;
  if c.max_uses is not null and c.used_count >= c.max_uses then
    return query select false, 'exhausted', c.id, c.code, price, 0, price, null::text; return;
  end if;
  if c.applicable_plan_codes is not null
     and array_length(c.applicable_plan_codes, 1) > 0
     and not (p_plan = any (c.applicable_plan_codes)) then
    return query select false, 'wrong_plan', c.id, c.code, price, 0, price, null::text; return;
  end if;
  if price < c.min_order_paise then
    return query select false, 'below_minimum', c.id, c.code, price, 0, price, null::text; return;
  end if;

  if p_user is not null then
    select count(*) into used_by_user
      from public.coupon_redemptions r
     where r.coupon_id = c.id and r.student_id = p_user;
    if used_by_user >= c.max_uses_per_user then
      return query select false, 'already_used', c.id, c.code, price, 0, price, null::text; return;
    end if;
  end if;

  -- Integer paise throughout; percent rounds to the nearest paisa.
  if c.discount_type = 'percent' then
    disc := round(price * c.discount_value / 100.0);
    if c.max_discount_paise is not null then
      disc := least(disc, c.max_discount_paise);
    end if;
  else
    disc := round(c.discount_value * 100);
  end if;

  -- Never below ₹1: Razorpay rejects a zero-amount order, and a 100% coupon
  -- should be granted as a free enrollment by an admin, not run through
  -- checkout.
  disc := greatest(0, least(disc, price - 100));

  return query select
    true, 'ok', c.id, c.code, price, disc, price - disc,
    case when c.discount_type = 'percent'
         then trim(to_char(c.discount_value, 'FM999990.##')) || '% off'
         else '₹' || trim(to_char(c.discount_value, 'FM999999990')) || ' off'
    end;
end;
$$;

-- ---------------------------------------------------------------------------
-- REDEEM — called only after a payment is verified. Atomic: the row lock on
-- the coupon serialises concurrent checkouts against the same last use.
-- ---------------------------------------------------------------------------
create or replace function public.redeem_coupon(p_coupon uuid, p_user uuid, p_payment uuid, p_discount integer)
returns boolean
language plpgsql
security definer
set search_path = public
as $$
declare
  c public.coupons%rowtype;
  used_by_user integer;
begin
  if p_coupon is null then return false; end if;

  -- Already recorded for this payment? Nothing to do — a webhook retry and
  -- the browser's own confirmation both land here.
  if exists (select 1 from public.coupon_redemptions
              where coupon_id = p_coupon and payment_id = p_payment) then
    return true;
  end if;

  select * into c from public.coupons where id = p_coupon for update;
  if c.id is null then return false; end if;

  if c.max_uses is not null and c.used_count >= c.max_uses then return false; end if;

  select count(*) into used_by_user
    from public.coupon_redemptions where coupon_id = p_coupon and student_id = p_user;
  if used_by_user >= c.max_uses_per_user then return false; end if;

  insert into public.coupon_redemptions (coupon_id, student_id, payment_id, discount_paise)
  values (p_coupon, p_user, p_payment, coalesce(p_discount, 0));

  update public.coupons set used_count = used_count + 1 where id = p_coupon;
  return true;
end;
$$;

-- ---------------------------------------------------------------------------
-- RLS. Students never read the coupons table — that would hand them every
-- code on the site. They learn a code's worth only by submitting it.
-- ---------------------------------------------------------------------------
alter table public.coupons            enable row level security;
alter table public.coupon_redemptions enable row level security;

drop policy if exists coupons_admin        on public.coupons;
drop policy if exists redemptions_admin    on public.coupon_redemptions;
drop policy if exists redemptions_own_read on public.coupon_redemptions;

create policy coupons_admin on public.coupons for all
  using (public.is_admin()) with check (public.is_admin());

create policy redemptions_own_read on public.coupon_redemptions for select
  using (student_id = auth.uid() or public.is_admin());
create policy redemptions_admin on public.coupon_redemptions for all
  using (public.is_admin()) with check (public.is_admin());

-- Both functions run as service_role from the edge functions only. Students
-- reach them through /functions/v1/coupon-check, never directly.
--
-- IMPORTANT: Postgres grants EXECUTE on every new function to PUBLIC. Revoking
-- from anon/authenticated alone leaves that PUBLIC grant intact, and both
-- functions stay callable over PostgREST — a student could have hit
-- redeem_coupon directly and burned a coupon use with no payment behind it.
-- Revoke from PUBLIC, then grant back only to service_role.
revoke execute on function public.coupon_quote(text, text, uuid)           from public, anon, authenticated;
revoke execute on function public.redeem_coupon(uuid, uuid, uuid, integer) from public, anon, authenticated;
grant  execute on function public.coupon_quote(text, text, uuid)           to service_role;
grant  execute on function public.redeem_coupon(uuid, uuid, uuid, integer) to service_role;

-- Same audit applied to the SECURITY DEFINER helpers from earlier migrations:
-- these ARE meant to be reachable by a signed-in student, but PUBLIC is still
-- wider than it should be.
revoke execute on function public.attempt_standing(uuid) from public;
grant  execute on function public.attempt_standing(uuid) to authenticated, service_role;
revoke execute on function public.has_plan(text)        from public;
revoke execute on function public.can_access_test(uuid) from public;
grant  execute on function public.has_plan(text)        to anon, authenticated, service_role;
grant  execute on function public.can_access_test(uuid) to anon, authenticated, service_role;
