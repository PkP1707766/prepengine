-- ============================================================================
-- Extend `is_tester` bypass to paid materials as well.
--
-- 0020_qa_tester_access made testers pass can_access_test() so they can OPEN
-- and SUBMIT any test, but the materials_select RLS policy (last set in
-- 0004_public_content) still required a live enrollment for anything paid.
-- Testers by design have no enrollment row -- that's the whole point, they're
-- excluded from paying-customer counts -- so they'd see only free materials
-- and get an empty state everywhere else. That defeats a chunk of what QA
-- accounts are for (checking that a purchased-material link renders, plays,
-- downloads, is language-toggled, etc).
--
-- Kept minimal: adds one `or public.is_tester()` branch and nothing else.
-- Admin, free-and-published, and paid-with-enrollment paths are untouched.
-- ============================================================================
drop policy if exists materials_select on public.materials;
create policy materials_select on public.materials for select
  using (
    public.is_admin()
    or public.is_tester()
    or (is_published and is_free)
    or (is_published and auth.uid() is not null and exists (
      select 1 from public.enrollments e
      where e.student_id = auth.uid()
        and e.status = 'active'
        and (e.expires_at is null or e.expires_at > now())
        and (e.batch_id is null or e.batch_id = public.materials.batch_id)
    ))
  );
