-- ============================================================================
-- 0018 — tests.total_questions / tests.total_marks always derived, never
-- hand-set.
--
-- Neither existing write path ever populated these two columns:
--   * the admin panel's manual test builder (testToRow() in src/lib/db.js)
--     never includes them in the row object it upserts
--   * commit_generated_test() (0016) never includes them in its INSERT/UPDATE
--     column list either
-- so every test built through either path has sat at the column default (0)
-- since the day those columns were added. This is not a "computed but failed
-- to persist" bug in either path — neither ever attempted to compute them for
-- persistence at all (TestEditor computes a `totals` value client-side, but
-- only for the on-screen "150 questions / 150 marks" label; it never rides
-- along in the object passed to onSave).
--
-- exam_paper() itself was never affected by this — it reads marks_correct /
-- marks_wrong live per question at serve time, not from these two summary
-- columns — so no student-facing scoring was ever wrong. Only the two display
-- columns (bundle/catalog listings, admin list) that read tests.total_questions
-- / total_marks directly would have shown 0/0.
--
-- Fixed at the DB layer with a BEFORE INSERT OR UPDATE OF sections trigger
-- rather than patching both call sites: a trigger can't be forgotten by some
-- future third write path the way two separate JS call sites already were.
-- It recomputes both columns from tests.sections using the exact same
-- traversal + is_active filter exam_paper() itself uses, so the stored
-- summary and what actually gets served can never disagree. Whatever
-- total_questions/total_marks a caller tries to pass is silently overwritten
-- — these become fully derived columns, immune to any future call site
-- getting it wrong (including passing an explicit wrong value, not just
-- omitting them).
--
-- Deliberately NOT covered: a question's marks_correct changing AFTER it is
-- already embedded in a built test's sections does not retroactively update
-- that test's stored total_marks (this trigger only fires on writes to
-- `tests` itself, not on writes to `questions`). exam_paper() would still
-- serve the new marks value live and correctly to students; only the stored
-- summary column on that one test would drift stale. Flagged, not fixed —
-- out of scope for the bug actually reported (tests starting at 0/0), and
-- accepting it avoids a second, more invasive trigger on `questions` that
-- would need to scan every test's JSONB for containment on every single mark
-- edit, most of which touch no test at all.
-- ============================================================================

create or replace function public.recompute_test_totals()
returns trigger
language plpgsql
security definer
set search_path = public
as $fn$
declare
  v_count int;
  v_marks numeric;
begin
  select count(*), coalesce(sum(q.marks_correct), 0)
    into v_count, v_marks
  from jsonb_array_elements(coalesce(new.sections, '[]'::jsonb)) sec,
       jsonb_array_elements_text(coalesce(sec->'questionIds', '[]'::jsonb)) qid(value)
  join public.questions q on q.id::text = qid.value and q.is_active;

  new.total_questions := v_count;
  new.total_marks     := v_marks;
  return new;
end;
$fn$;

drop trigger if exists trg_recompute_test_totals on public.tests;
create trigger trg_recompute_test_totals
  before insert or update of sections on public.tests
  for each row
  execute function public.recompute_test_totals();

-- One-time backfill for any row that predates this trigger, and a built-in
-- self-check: "UPDATE OF sections" fires on any UPDATE that touches the
-- sections column, whether or not the value actually changes, so this makes
-- every existing test re-derive its totals immediately rather than waiting
-- for its next unrelated edit.
update public.tests set sections = sections;
