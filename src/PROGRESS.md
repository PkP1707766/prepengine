# JUNOONIAS — Market-Launch Readiness Tracker

Last updated: 22 Aug 2026

Status key: 🔴 Not started · 🟡 In progress · 🟢 Done & verified

---

## The headline change (20 Aug 2026)

The app was a polished demo sitting on top of almost nothing real. Three things
made it "demo mode", and all three are fixed:

1. **Nothing persisted.** `loadKey`/`saveKey` called `window.storage` — an API
   that does not exist in any browser. Every read silently returned the
   fallback and every write silently vanished. Every course, batch, test and
   material an admin created disappeared on refresh. Replaced with Supabase
   (`src/lib/db.js`) plus a real `localStorage` wrapper for preferences.

2. **Paying students were locked out.** `hasAccess()` filtered `enrollments` on
   `user_id` and selected `expires_at` — neither column existed. The query
   threw, a bare `catch` swallowed it, and the function returned `false`. Every
   student who paid was bounced straight back to the paywall, forever. Fixed in
   both the schema (`0001_core_schema.sql`) and the query.

3. **The student side was 100% invented.** `ATTEMPTS`, `NEW_TESTS`,
   `SUBJECT_STRENGTH`, `BATCHES`, `MATERIALS`, `LEADERBOARD`, the activity
   heatmap and the "980 students / rank #88" figures were all hardcoded arrays.
   Every one is now a real query, with an honest empty state when there is no
   data yet.

---

## 22 Aug 2026 — Phase 4: referral capture & binding (bundles spec §2.4, §7)

Tracking only — no wallet, no payout. What this phase buys is the record
everything later depends on: a permanent, unforgeable statement of who
introduced whom.

Migrations `0007`, `0007b`, `0008`, `0009`.

### The shape of it

Every profile now carries an 8-character `referral_code` (alphabet excludes
0/O/1/I/L — these get read off phone screens and dictated aloud). A trigger
generates one on insert, and all 12 existing profiles were backfilled, because
a share link has to work for everyone the day it ships, not just for people who
sign up afterwards.

`?ref=CODE` is read on page load, normalised, stored, and **stripped from the
address bar** so it can't ride along into anything the student later shares.
It waits in local storage until they eventually sign up — surviving the trip
through Google OAuth or a magic link — and binds on the first resolve after
their profile row exists.

There is deliberately **no "enter a referral code" field** anywhere. A typed
box invites students to trade codes in comment sections, which is the exact
abuse the link-only rule exists to prevent.

### What makes the binding trustworthy

`referrals.referred_id` is `UNIQUE`. That constraint — not application code —
is what makes "one referrer per person, set once, never editable" true.
`bind_referral(p_code)` keys off `auth.uid()` rather than accepting a user id,
so a caller can only ever bind their *own* account, which is what makes it safe
to expose to signed-in users at all.

Verified by impersonation, 23 assertions across three runs: anonymous callers,
empty/null codes, self-referral by own code, unknown codes, lowercase and
padded input, re-binding with the same code, re-binding with a *different*
code, a second account sharing an email in different casing, students trying
to insert their own referral row, a referred student trying to rewrite who gets
credit for them, and anon reads. All refused or normalised as intended.

### Two findings worth recording

**`profiles.phone` is UNIQUE but `email` is not.** So the phone half of the
duplicate-account check can never fire today — it is kept as defence in depth
against that constraint being relaxed. More importantly, this rule only ever
catches the *lazy* duplicate: someone reusing the same contact detail. A second
account with a fresh email and number is invisible to it. Real duplicate
detection has to happen at payout review time, which lands in phase 6.

**Supabase's default privileges re-opened the phase-3 hole in a new shape.**
Revoking `EXECUTE` from `PUBLIC` is not enough: `ALTER DEFAULT PRIVILEGES`
grants every new function and table in `public` to `anon`/`authenticated`
explicitly, and those grants survive a `revoke ... from public`. Both referral
functions were reachable by `anon`. Neither leaked anything (both return
nothing without a session), but the grant now matches the intent. Same pass
tightened the table grants and closed six trigger functions that were exposed
as REST endpoints — after first proving on a scratch table that PostgreSQL does
**not** re-check `EXECUTE` when a trigger fires, so revoking couldn't break
signup. Security advisor warnings: 27 → 14, and the 14 that remain are the
intentional student-facing helpers plus one dashboard toggle.

### Privacy

The referrer sees who joined on their link, but `profiles` is readable only by
its owner. Rather than widening that policy, `my_referral_list()` returns a
masked projection — first name plus last initial, no email, no phone. Enough to
recognise your own invite; not enough to harvest contacts.

### Open question for you

The share card advertises ₹99 per paid referral while the wallet that pays it
doesn't exist yet. Referral rows are stored with `bonus_status = 'pending'`, so
phase 5 can credit retroactively and the promise is keepable — but if you'd
rather not advertise a number before it can be paid, say so and I'll drop the
amount from the card until phase 5 lands.

---

## 22 Aug 2026 — Phase 1: mobile & tablet responsiveness (public-flow §2.3)

Measured at 375 / 767 / 1024 px across all five shells, using a DEV-only
fixture harness (`#/__dev/student|admin|exam`, `src/dev/fixtures.js`) so the
real authenticated screens could be rendered without anyone handing over a
password. The harness is stripped from production builds — verified by
grepping the built bundle for fixture strings.

### The bug behind "doesn't render at proper size on mobile"

Every input in the app was 13–14.5px. **iOS Safari zooms the entire page when
you focus an input under 16px**, and leaves the viewport zoomed afterwards —
so one tap on any field made the whole site look broken. Inputs are now 16px on
touch devices. Keyed on `pointer: coarse`, not a width breakpoint: an iPad in
landscape is 1024px wide and zooms just the same, so a `max-width` rule would
have missed it.

### Two flex/grid blowouts, same root cause

`min-width` defaults to `auto` on flex and grid children, meaning they refuse
to shrink below their content:

- **Student/admin topbar** overflowed 8–59px depending on page title. The `h1`
  had `min-width:0` but its two ancestors did not, so the title could not
  ellipsis and shoved the right-hand controls off-screen.
- **Admin dashboard overflowed by 938px at 375px.** `grid-template-columns:1fr`
  is really `minmax(auto, 1fr)`; a "Recently added" question title with
  `white-space:nowrap` forced its track to the width of the un-wrapped string —
  the column computed to 1286px. This one is live in production whenever a long
  question exists.

### Fixed once, in a shared baseline

All five shells failed identically, so the fix lives in one place
(`src/lib/i18n.jsx`) rather than five: input zoom, 44px touch-target floor,
grid/flex blowout guard, long-string `overflow-wrap`, media `max-width:100%`,
iOS landscape text-inflation, and safe-area insets for notched phones.

`ChromeControls` needed a source change too — it was inline-styled, and inline
styles beat any stylesheet, so its sizing moved to a `.jn-pill` class.

### Result

| Shell | Views checked | 375 | 767 | 1024 |
|---|---|---|---|---|
| Public + login + join | 3 | clean | clean | clean |
| Student | 7 | clean | clean | clean |
| Admin | 8 | clean | clean | clean |
| Exam (instructions / paper / report) | 3 | clean | — | — |

Clean = no horizontal overflow, no touch target under 44px. Desktop sizing is
unchanged; everything is gated behind `pointer: coarse`.

---

## 21 Aug 2026 — public storefront + multi-exam bundles (specs 1 & 2)

### Shipped

| Item | Source | Status |
|---|---|---|
| Public browsing before login | public-flow spec §1 | 🟢 Live |
| Multi-exam bundles (UPSC / BPSC / UPPCS) | bundles spec phase 1 | 🟢 Live |
| Admin bundle + price editing | bundles spec phase 2 | 🟢 Live |
| Theme/language toggles inside the app | public-flow spec §2.1 | 🟢 Fixed |
| Phone number removed sitewide | public-flow spec §2.2 | 🟢 Done |
| Payment edge functions deployed | — | 🟢 All three live |

### Bug 2.1 — the real cause was bigger than "component not mounted"

The toggles weren't broken; there was simply nothing listening. `data-theme`
was being set on `<html>` correctly all along, but **only the auth screens had
any dark CSS** — student, admin and exam had zero `[data-theme="dark"]` rules,
so the toggle flipped the attribute and nothing changed. On top of that,
`ChromeControls` was never mounted in admin or exam.

Fixed three ways: a dark palette for every shell, surface colours moved out of
hardcoded inline styles into tokens (inline styles can't be overridden by a
stylesheet), and the control mounted in the admin topbar and the exam
instructions screen. Verified: page, card, text and border colours all flip.

### A security hole found while gating bundles

`questions` RLS was `auth.uid() is not null` — meaning **any signed-in account,
including one that had never paid, could read the entire question bank** off
the REST endpoint. Now gated behind `can_access_test()`. Verified by
impersonation:

| | Paying student | Signed-in non-payer | Anonymous |
|---|---|---|---|
| Bundles visible | 3 | 3 | 3 |
| Tests visible | 1 | 1 | 1 |
| Questions readable | 8 | **0** | **0** |

### Deviations from the written spec, and why

- **`plans` keeps `code` as its primary key** instead of gaining a uuid `id`.
  `enrollments.plan_code` and `payments.plan_code` already reference it, with a
  live enrollment and four paid payments riding on that FK. A parallel uuid
  would give every plan two identities and two ways to get a join wrong.
- **Money stays integer paise, not `numeric`.** Razorpay transacts in paise,
  and integers mean a percentage coupon can't leave a fractional-paisa
  artefact on an invoice.

### Bundles spec phases 3–6

3. ✅ Coupons (`coupons`, `coupon_redemptions`, server-side validation in
   `join-order`) — **live**
4. ✅ Referral capture + binding — **live**, tracking only
5. ⬜ Wallet ledger + ₹99 bonus on verified paid referral
6. ⬜ Withdrawal requests + admin payout panel

The spec's own advice — don't ship all six at once — is worth keeping.

### Data note

The migration assigned every pre-existing test to the original UPSC bundle so
the one paying student kept access. "BPSC MOCK TEST 01" is currently sitting in
the UPSC bundle for that reason — move it under **Bundles & Pricing → BPSC →
Assign tests**.

---

## Pages & features

| # | Page / Feature | Design | Real data | Status |
|---|---|---|---|---|
| 1 | Login / Signup | 🟢 + forgot-password, friendly error copy, no account enumeration | 🟢 Supabase Auth (email, phone OTP, Google) | 🟢 Done |
| 2 | Paywall / Join | 🟢 Price + features rendered from the DB | 🟢 Server-priced Razorpay order, signature-verified | 🟢 Done |
| 3 | Home dashboard | 🟢 + first-run state for new students | 🟢 Attempts, tests, streak, enrollment | 🟢 Done |
| 4 | Test Series | 🟢 Search, sort, empty states | 🟢 Real published tests; each card starts *its own* test | 🟢 Done |
| 5 | My Performance | 🟢 | 🟢 Trend, subject map, real peer benchmark | 🟢 Done |
| 6 | My Batches | 🟢 Expiry + urgency badges | 🟢 Real enrollments and progress | 🟢 Done |
| 7 | Study Material | 🟢 | 🟢 Real files from Supabase Storage; RLS decides visibility | 🟢 Done |
| 8 | Leaderboard | 🟢 Podium, search, native share | 🟢 `leaderboard_v` — computed from real attempts | 🟢 Done |
| 9 | Profile | 🟢 | 🟢 Saves to `profiles`; photo goes to Storage, not base-64 | 🟢 Done |
| 10 | Exam screen | 🟢 Marking scheme read off the real paper | 🟢 Loads the selected test; saves the attempt; real rank | 🟢 Done |
| 11 | Admin — Question Bank | 🟢 | 🟢 Supabase CRUD, soft delete, bulk import | 🟢 Done |
| 12 | Admin — Tests & Series | 🟢 Series dropdown, scheduling, free/paid | 🟢 Persists to `tests` | 🟢 Done |
| 13 | Admin — Courses & Batches | 🟢 | 🟢 Persists to `courses` / `batches` | 🟢 Done |
| 14 | Admin — Materials | 🟢 Real file upload | 🟢 Supabase Storage | 🟢 Done |
| 15 | Admin — Students | 🟢 Search, filter, CSV export | 🟢 Real accounts, attempts, conversion | 🟢 Done |
| 16 | Admin — Sales | 🟢 Revenue trend, CSV export | 🟢 Real verified Razorpay transactions | 🟢 Done |

---

## Security fixed

- **Row-level security on every table.** A student reads only their own
  attempts, enrollments, payments and notifications.
- **Roles can't be self-assigned.** A trigger raises an exception on any
  client-side change to `profiles.role`. Admin is granted by SQL only.
- **Enrollments can't be self-granted.** Only edge functions running as
  `service_role`, after verifying a Razorpay HMAC signature, can create one.
- **The price is server-side.** `join-order` reads the amount from the `plans`
  table, so a tampered client can't buy access for ₹1.
- **Payment webhook is signature-verified** with a timing-safe comparison, and
  is idempotent (unique index on `razorpay_order_id`), so a replayed webhook
  can't double-credit.
- **Password reset doesn't leak which emails exist** — the same message either
  way.

## Reliability fixed

- **Error boundaries** around each sub-app. A runtime error now shows a
  recoverable screen instead of a blank white page — the exact failure that
  took down the exam screen before.
- **Missing env vars** show an explicit "Site not configured" page.
- **A failed save is surfaced**, not swallowed. Local state is updated from the
  row the database actually returned.
- **Routes are mirrored into the URL hash**, so refresh and browser-back work.
- **`beforeunload` guard** during a live exam.
- **The attempt is saved after the report renders**, so a network hiccup can't
  cost a student the analysis they just earned — and if the save does fail,
  they're told.

## Honesty fixed

Everything that used to be quietly fabricated now either shows real data or
says it has none:

- Percentile is labelled "Estimated" until enough peers have taken the paper.
- The batch-average / topper benchmark is hidden when there are no peers,
  instead of showing invented 48% / 91% bars.
- Starter questions are loaded by an explicit button, never auto-seeded into a
  live database.
- "Sample data" banners are gone because the data is no longer sampled.

---

## Still open

- **Client-side scoring.** Answer keys reach the browser. Fine for a
  self-paced mock (this is what competitors do); move `evaluate()` into an edge
  function before running a proctored All-India test with prizes.
- **Razorpay is still on a test key** (`rzp_test_…`). Swap to live keys, and run
  one real ₹1 transaction end-to-end before launch.
- **Notification delivery.** Reminders and preferences are stored, and
  in-app notifications work; email/SMS/WhatsApp fan-out needs a scheduled
  function.
- **No automated tests.** `npm run lint` is the current safety net and it does
  catch the blank-page class of bug. A few end-to-end tests around
  signup → pay → attempt → report would be the highest-value addition next.

---

## Process note

`npm run build` does **not** catch a call to a function that doesn't exist —
that's a runtime error, and it is exactly how the exam screen turned into a
blank page. `npm run lint` (`no-undef`) does catch it. Run both.

---

## Earlier log

- **17 Aug 2026** — Login/Signup polish; found and fixed a CSS specificity bug
  (`.sd-root button{background:none}` overriding `.btn-primary`) in four
  scopes using `:where(button)`; fixed the invisible "Continue practice" and
  "I am ready to begin" buttons; fixed the exam screen crashing to a blank page
  because it called `loadKey`, which lived in the admin panel's scope.
