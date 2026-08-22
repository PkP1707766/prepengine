# JUNOONIAS — *An Academy of Inner Fire*

A production test-prep platform for UPSC, BPSC and State PSC aspirants:
real exam-style mock tests, question-wise analytics, All-India rank, study
material, and a Razorpay paywall. Bilingual (English / हिन्दी), light and dark.

React 19 + Vite · Supabase (Postgres, Auth, Storage, Edge Functions) · Razorpay · Vercel

---

## Quick start

```bash
npm install
cp .env.example .env.local   # fill in your Supabase + Razorpay values
npm run dev
```

| Command | What it does |
| --- | --- |
| `npm run dev` | Dev server on http://localhost:5173 |
| `npm run build` | Production build into `dist/` |
| `npm run preview` | Serve the production build locally |
| `npm run lint` | **Run before every commit** — see the note below |

> **Why lint matters here.** `npm run build` does *not* catch a call to a
> function that doesn't exist; that is a runtime error, and it once turned the
> whole exam screen into a blank white page. ESLint's `no-undef` does catch it.
> Treat a lint failure as a build failure.

---

## Architecture

```
src/
  App.jsx                 Root router — session, role gate, hash routes
  main.jsx                Mount point
  lib/
    supabase.js           One shared Supabase client
    db.js                 EVERY database read/write in the app
    format.js             Shared formatters (money, dates, grades)
    storage.js            localStorage with a real in-memory fallback
    i18n.jsx              Fonts, theme, English/Hindi copy
    contexts.js           Language + theme contexts
  ui/
    Brand.jsx             The diya mark
    ErrorBoundary.jsx     Stops a crash from becoming a blank page
    Feedback.jsx          Skeletons, empty states, error states
  screens/
    PublicSite.jsx        Storefront — hero, catalogue, bundle detail (no login)
    LoginScreen.jsx       Email / phone-OTP / Google, password reset
    JoinScreen.jsx        Checkout for one bundle + Razorpay
    StudentApp.jsx        Dashboard, tests, analytics, batches, material,
                          leaderboard, profile
    ExamApp.jsx           Exam engine — instructions, paper, scoring, report
    AdminApp.jsx          Question bank, test builder, courses, students, sales
supabase/
  migrations/             SQL — run these before the first deploy
  functions/              Deno edge functions (payments)
```

**One rule worth keeping:** screens never write SQL. Every query lives in
`src/lib/db.js`. The schema is not uniformly named — `enrollments` and
`attempts` key the student as `student_id`, while `payments` and
`notifications` use `user_id` — and a hand-written query that got this wrong is
what silently locked every paying student out of the product.

---

## Deployment runbook

### 1. Database

Run both migrations against your Supabase project, in order. Either paste them
into the SQL editor at
`https://supabase.com/dashboard/project/<ref>/sql`, or use the CLI:

```bash
npx supabase link --project-ref <your-project-ref>
npx supabase db push
```

`0001_core_schema.sql` is idempotent — safe to re-run. It adds the missing
columns, row-level security on every table, the signup trigger, the leaderboard
view, and the `plans` table that holds your pricing.

`0002_storage.sql` creates the `materials` and `avatars` buckets and their
access policies.

### 2. Make yourself an admin

There is deliberately **no way to grant yourself the admin role from the
browser** — a database trigger blocks it. Run this once in the SQL editor:

```sql
update public.profiles set role = 'admin' where email = 'you@example.com';
```

### 3. Bundles and pricing

Each exam is a separate, separately-purchasable bundle in `public.plans`.
Prices are edited in the admin panel under **Bundles & Pricing** — no SQL and
no redeploy needed. `join-order` re-reads the price from the database on every
order, so a tampered browser cannot buy access for ₹1.

**Bundles are isolated.** A student only unlocks the tests listed in
`plan_tests` for a bundle they hold. Assign tests to a bundle in
**Bundles & Pricing → (row) → Assign tests**. A published test that belongs to
no bundle is visible in the catalogue but sits locked for everyone.

Money is stored as integer paise (`price_paise`), not a float — Razorpay
transacts in paise, and integers mean a percentage discount can never leave a
fractional-paisa artefact on an invoice.

### 3a. Public storefront

The site is browsable with no account: hero, catalogue by exam, per-bundle
detail with the full test list and price. Sign-in is required only when a
visitor clicks **Enroll now**, and they're returned to checkout for the exact
bundle they picked.

Row-level security backs this up rather than the UI: `plans`, `tests`,
`catalog_v` and `plan_tests` are readable anonymously, while `questions` is
readable only for tests the caller is actually entitled to.

### 4. Edge functions (payments)

```bash
npx supabase secrets set \
  RAZORPAY_KEY_ID=rzp_live_xxxxxxxx \
  RAZORPAY_KEY_SECRET=xxxxxxxx \
  RAZORPAY_WEBHOOK_SECRET=xxxxxxxx \
  ALLOWED_ORIGINS=https://your-domain.com

npx supabase functions deploy join-order
npx supabase functions deploy verify-payment
npx supabase functions deploy razorpay-webhook --no-verify-jwt
```

The webhook must be deployed with `--no-verify-jwt` — Razorpay does not send a
Supabase JWT. It is not unauthenticated: every request is rejected unless its
HMAC-SHA256 signature matches `RAZORPAY_WEBHOOK_SECRET`.

Then in the Razorpay dashboard → **Settings → Webhooks**, add:

- URL: `https://<project-ref>.supabase.co/functions/v1/razorpay-webhook`
- Secret: the same `RAZORPAY_WEBHOOK_SECRET`
- Events: `payment.captured`, `payment.failed`, `order.paid`, `refund.processed`

### 5. Supabase Auth settings

In **Authentication → URL Configuration**:

- Site URL: `https://your-domain.com`
- Redirect URLs: add `https://your-domain.com` and `http://localhost:5173`

Enable the Google provider if you want the Google button to work, and a phone
provider (Twilio / MSG91) if you want OTP login. Both fail gracefully with a
readable message when not configured.

### 6. Vercel

Set these environment variables for **Production**, **Preview** and
**Development**:

| Variable | Value |
| --- | --- |
| `VITE_SUPABASE_URL` | `https://<project-ref>.supabase.co` |
| `VITE_SUPABASE_ANON_KEY` | your anon/publishable key |

That's all the client needs. The Razorpay key id is returned by the
`join-order` function, and the secret never leaves the server.

If either variable is missing the app shows an explicit "Site not configured"
page instead of a blank screen.

---

## Going live — checklist

- [ ] Both migrations applied
- [ ] Your account promoted to `admin`
- [ ] Bundle prices set in the admin panel (**Bundles & Pricing**)
- [ ] Each published test assigned to the right bundle
- [ ] Razorpay switched from `rzp_test_…` to **live** keys
- [ ] Webhook registered and firing (check Razorpay → Webhooks → recent deliveries)
- [ ] One real ₹1 test transaction end-to-end, then refunded
- [ ] Questions added and at least one test **published**
- [ ] `npm run lint && npm run build` both clean
- [ ] Custom domain pointed at Vercel, and `ALLOWED_ORIGINS` updated to match
- [ ] Update the URLs in `index.html`, `public/robots.txt` and
      `public/sitemap.xml` from the `.vercel.app` placeholder to your domain

---

## Security notes

- **RLS is on for every table.** A student can read only their own attempts,
  enrollments, payments and notifications.
- **Roles cannot be self-assigned.** `guard_profile_role()` raises an exception
  on any client-side attempt to change `profiles.role`.
- **Enrollments are never granted by the browser.** Only the edge functions,
  running as `service_role` after verifying a Razorpay signature, can create
  one.
- **Prices are server-side.** `join-order` reads the amount from `plans`, and
  refuses to sell a bundle the caller already owns.
- **The question bank is entitlement-gated.** Before this, any signed-in
  account — including one that had never paid — could read every question
  straight off the REST endpoint. `questions` now requires
  `can_access_test()` to pass for a test containing that question.
- **The service-role key must never appear in a `VITE_*` variable** — anything
  prefixed `VITE_` is compiled into the JavaScript bundle and is public.

Answer keys are sent to the browser, because the exam is scored client-side —
the same as every competitor in this market. If you later need tamper-proof
scoring (for a proctored All-India test, say), move `evaluate()` out of
`ExamApp.jsx` into an edge function and strip `correct` and `explanation` from
`loadExamTest()`.

---

## Contact

junoonias123@gmail.com
