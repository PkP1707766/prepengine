-- Sanitising exam_paper() was only half the fix. `questions_select` still let
-- an entitled student read the table directly:
--
--     GET /rest/v1/questions?select=*
--
-- which returns options[].isCorrect, numeric_answer and explanation for every
-- question in every test they can access — the entire answer key, before the
-- paper has even started. Serving a clean paper is pointless while the raw
-- table stays readable.
--
-- Students now have no direct read at all. Nothing legitimate needs one:
--   * the live paper comes from exam_paper(), which is SECURITY DEFINER and
--     therefore bypasses RLS while returning no answers;
--   * the post-attempt review is served from attempts.review, a snapshot
--     written by the server at submit time.
-- Admins keep full access through questions_admin (is_admin()).
drop policy if exists questions_select on public.questions;

comment on table public.questions is
  'No direct student read. Live papers come from exam_paper() (answers stripped); review comes from attempts.review. Admins read via questions_admin.';
