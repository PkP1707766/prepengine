/**
 * Every database read and write in the app goes through this module.
 *
 * Two reasons it exists:
 *  1. The schema is not uniformly named — `enrollments`/`attempts` key the
 *     student as `student_id`, while `payments`/`notifications` use `user_id`.
 *     Hand-written queries got this wrong before (the access check queried a
 *     column that does not exist and therefore always denied access).
 *  2. Screens should never see raw rows. Everything below returns app-shaped
 *     objects, so a column rename is a one-file change.
 */
import { getSupabase } from "./supabase.js";
import { bandFor } from "./format.js";
import { sortTests } from "./testOrder.js";
import { loadKey, saveKey, removeKey } from "./storage.js";
import { essayKey, copyLinkAt } from "./mainsKeys.js";

/* ---------------------------------------------------------------------------
 * DEV-ONLY responsiveness harness.
 *
 * Setting `#/__dev/student` (etc.) turns this on so the real authenticated
 * screens can be rendered and measured at every breakpoint without anyone
 * having to hand over a password. `import.meta.env.DEV` means the whole branch
 * is dead code in a production build and gets tree-shaken out.
 * ------------------------------------------------------------------------ */
export const FIXTURES_ON = () =>
  // FX must be loaded too: a hot reload can clear the module while the window
  // flag survives, and every fixture call would then throw on null.
  import.meta.env.DEV && typeof window !== "undefined" && window.__JN_FIXTURES === true && FX !== null;

let FX = null;
export async function enableFixtures() {
  if (!import.meta.env.DEV) return false;
  FX = await import("../dev/fixtures.js");
  window.__JN_FIXTURES = true;
  return true;
}
const fx = () => FX;

/* ------------------------------------------------------------------ auth -- */

export async function currentUser() {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_USER;
  const sb = await getSupabase();
  const { data } = await sb.auth.getUser();
  return data?.user ?? null;
}

export async function currentSession() {
  const sb = await getSupabase();
  const { data } = await sb.auth.getSession();
  return data?.session ?? null;
}

export async function getProfile(userId) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_PROFILE;
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("profiles")
    .select("id, full_name, email, phone, role, avatar_url, target_exam, target_date, city, prefs, created_at")
    .eq("id", userId)
    .maybeSingle();
  if (error) throw error;
  return data;
}

/**
 * Profile row, guaranteed non-null. If the signup trigger has not fired yet
 * (or the user predates it) the row is created from the auth record.
 */
export async function ensureProfile(user) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_PROFILE;
  const existing = await getProfile(user.id).catch(() => null);
  if (existing) return existing;
  const sb = await getSupabase();
  const fallbackName =
    user.user_metadata?.full_name ||
    user.user_metadata?.name ||
    (user.email ? user.email.split("@")[0] : "Aspirant");
  const { data } = await sb
    .from("profiles")
    .insert({ id: user.id, full_name: fallbackName, email: user.email ?? null, phone: user.phone ?? null })
    .select()
    .maybeSingle();
  return data ?? { id: user.id, full_name: fallbackName, email: user.email, role: "student" };
}

export async function updateProfile(userId, patch) {
  const sb = await getSupabase();
  // `role` and `id` are deliberately not forwardable — the database rejects a
  // role change anyway, but stripping them here keeps the error out of the
  // user's face and makes the intent explicit.
  const safe = { ...patch };
  delete safe.role;
  delete safe.id;
  const { data, error } = await sb
    .from("profiles")
    .update({ ...safe, updated_at: new Date().toISOString() })
    .eq("id", userId)
    .select()
    .single();
  if (error) throw error;
  return data;
}

/* ---------------------------------------------------------------- access -- */

/**
 * Does this student have a live enrollment?
 *
 * The old implementation filtered on `user_id` and selected `expires_at`,
 * neither of which existed on `enrollments`, so the query errored, the catch
 * swallowed it, and every paying student was bounced back to the paywall.
 */
export async function hasActiveAccess(userId) {
  if (import.meta.env.DEV && FIXTURES_ON()) return true;
  if (!userId) return false;
  const sb = await getSupabase();
  // Both queries fired in parallel: cost of the second query is dwarfed by
  // the roundtrip we'd add if the profile check went first-then-fetch.
  //
  // Tester accounts (internal QA) must pass this check even with zero
  // enrollment rows -- the whole point of is_tester is that they can attempt
  // any test without buying one. Without this branch, a tester with no live
  // enrollment (which is the SUPPORTED shape for testers per migration 0020)
  // was routed to the paywall on every sign-in and never reached the dashboard,
  // making the QA bypass unreachable through the UI.
  const [{ data: prof }, { data, error }] = await Promise.all([
    sb.from("profiles").select("is_tester").eq("id", userId).maybeSingle(),
    sb.from("enrollments").select("id, expires_at, status")
      .eq("student_id", userId).eq("status", "active"),
  ]);
  if (prof?.is_tester) return true;
  if (error) {
    console.error("access check failed", error);
    return false;
  }
  const now = Date.now();
  return (data ?? []).some((e) => !e.expires_at || new Date(e.expires_at).getTime() > now);
}

export async function listEnrollments(userId) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_ENROLLMENTS;
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("enrollments")
    .select("id, plan_code, batch_id, status, expires_at, enrolled_at, plans(name, exam_category), batches(name, course_id, end_date, courses(title, exam_target))")
    .eq("student_id", userId)
    .order("enrolled_at", { ascending: false });
  if (error) throw error;
  return data ?? [];
}

export async function getPlan(code = "prelims-2026") {
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("plans")
    .select("code, name, exam_category, tagline, description, price_paise, mrp_paise, currency, duration_days, features")
    .eq("code", code)
    .eq("is_active", true)
    .maybeSingle();
  if (error) throw error;
  return data;
}

/* -------------------------------------------------------------- catalogue -- */

const bundleFromRow = (r) => ({
  code: r.code,
  name: r.name,
  exam: r.exam_category,
  examLabel: r.exam_label || String(r.exam_category || "").toUpperCase(),
  examFullName: r.exam_full_name || "",
  conductedBy: r.conducted_by || "",
  examSort: r.exam_sort_order ?? 999,
  tagline: r.tagline || "",
  description: r.description || "",
  price: (r.price_paise ?? 0) / 100,
  mrp: r.mrp_paise ? r.mrp_paise / 100 : null,
  currency: r.currency || "INR",
  durationDays: r.duration_days,
  features: Array.isArray(r.features) ? r.features : [],
  testCount: r.test_count ?? 0,
  freeTestCount: r.free_test_count ?? 0,
  // A Mains plan sells the Mains section, not papers (0033).
  includesMains: r.includes_mains === true,
  sortOrder: r.sort_order ?? 0,
  // Null when no PDF has been uploaded yet -- the UI reads this as "don't
  // render the brochure button at all", so a plan without a flyer is silent
  // rather than showing a broken/disabled control.
  brochureUrl: r.brochure_url || null,
});

/**
 * The shop window. Deliberately readable without an account — a visitor must
 * be able to see what JUNOONIAS sells and what it costs before being asked to
 * create anything.
 */
export async function listBundles() {
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("catalog_v").select("*")
    .order("exam_sort_order", { nullsFirst: false })
    .order("sort_order");
  if (error) throw error;
  return (data ?? []).map(bundleFromRow);
}

/**
 * Exam categories. These used to be a CHECK constraint in the schema and a
 * hardcoded label map in the UI, which is how a JPSC bundle ended up filed
 * under "Other". Now the admin adds an exam and the tab appears by itself.
 */
export async function examCategories({ includeInactive = false } = {}) {
  const sb = await getSupabase();
  let q = sb.from("exam_categories").select("*").order("sort_order");
  if (!includeInactive) q = q.eq("is_active", true);
  const { data, error } = await q;
  if (error) throw error;
  return (data ?? []).map((r) => ({
    code: r.code, label: r.label, fullName: r.full_name || "",
    conductedBy: r.conducted_by || "", region: r.region || "",
    sortOrder: r.sort_order, isActive: r.is_active !== false,
  }));
}

export async function upsertExamCategory(c) {
  const sb = await getSupabase();
  const { data, error } = await sb.from("exam_categories").upsert({
    code: String(c.code || "").trim().toLowerCase(),
    label: c.label,
    full_name: c.fullName || null,
    conducted_by: c.conductedBy || null,
    region: c.region || null,
    sort_order: Number(c.sortOrder || 100),
    is_active: c.isActive !== false,
  }).select().single();
  if (error) throw error;
  return data;
}

export async function deleteExamCategory(code) {
  const sb = await getSupabase();
  const { error } = await sb.from("exam_categories").delete().eq("code", code);
  if (error) throw error;
}

export async function getBundle(code) {
  const sb = await getSupabase();
  const { data, error } = await sb.from("catalog_v").select("*").eq("code", code).maybeSingle();
  if (error) throw error;
  return data ? bundleFromRow(data) : null;
}

/** The tests inside one bundle — titles only, safe to show publicly. */
export async function bundleTests(code) {
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("plan_tests")
    .select("test_id, tests(id, exam_category, title, title_hi, series_id, test_series(title, title_hi), duration_min, total_questions, total_marks, is_free, is_published, scheduled_for, created_at)")
    .eq("plan_code", code);
  if (error) throw error;
  return sortTests((data ?? [])
    .map((r) => r.tests)
    .filter((t) => t && t.is_published)
    .map((t) => ({
      id: t.id,
      examCategory: t.exam_category,
      title: t.title,
      titleHi: t.title_hi || "",
      seriesId: t.series_id,
      seriesTitle: t.test_series?.title || "",
      seriesTitleHi: t.test_series?.title_hi || "",
      durationMin: t.duration_min,
      totalQuestions: t.total_questions,
      totalMarks: Number(t.total_marks || 0),
      isFree: !!t.is_free,
      scheduledFor: t.scheduled_for,
      createdAt: t.created_at,
    })));
}

/** Which bundles does this student hold right now?
 *
 *  Testers "own" every active plan virtually -- so the storefront shows every
 *  bundle as owned (no Enroll button leading to a paywall), and JoinScreen
 *  short-circuits its bootstrap to send them straight through to the dashboard
 *  if they ever land on it via a pending-plan deep link. Otherwise a tester
 *  clicking Enroll on a bundle would hit Razorpay for something they already
 *  had free access to. */
export async function myPlanCodes(userId) {
  if (!userId) return new Set();
  const sb = await getSupabase();
  const [{ data: prof }, { data, error }] = await Promise.all([
    sb.from("profiles").select("is_tester").eq("id", userId).maybeSingle(),
    sb.from("enrollments").select("plan_code, status, expires_at")
      .eq("student_id", userId).eq("status", "active"),
  ]);
  if (prof?.is_tester) {
    const { data: plans } = await sb.from("plans").select("code").eq("is_active", true);
    return new Set((plans ?? []).map((p) => p.code).filter(Boolean));
  }
  if (error) return new Set();
  const now = Date.now();
  return new Set(
    (data ?? [])
      .filter((e) => !e.expires_at || new Date(e.expires_at).getTime() > now)
      .map((e) => e.plan_code)
      .filter(Boolean),
  );
}

/* ------------------------------------------------------ admin: bundles -- */

export async function adminListBundles() {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_BUNDLES;
  const sb = await getSupabase();
  const { data, error } = await sb.from("plans").select("*").order("sort_order");
  if (error) throw error;
  return (data ?? []).map((r) => ({
    code: r.code,
    name: r.name,
    exam: r.exam_category,
    tagline: r.tagline || "",
    description: r.description || "",
    price: (r.price_paise ?? 0) / 100,
    mrp: r.mrp_paise ? r.mrp_paise / 100 : "",
    durationDays: r.duration_days ?? "",
    features: Array.isArray(r.features) ? r.features : [],
    isActive: r.is_active !== false,
    sortOrder: r.sort_order ?? 0,
    brochureUrl: r.brochure_url || null,
    // Undefined until migration 0028 adds the column, so a bundle saved by a
    // build deployed ahead of that migration never sends a column that is
    // not there yet.
    includesMains: "includes_mains" in r ? r.includes_mains === true : undefined,
  }));
}

export async function upsertBundle(b) {
  const sb = await getSupabase();
  // Money is stored in paise as an integer. Rupees only exist for display, so
  // a percentage discount can never leave a fractional-paisa artefact.
  const row = {
    code: b.code,
    name: b.name,
    exam_category: b.exam,
    tagline: b.tagline || null,
    description: b.description || null,
    price_paise: Math.round(Number(b.price || 0) * 100),
    mrp_paise: b.mrp === "" || b.mrp == null ? null : Math.round(Number(b.mrp) * 100),
    duration_days: b.durationDays === "" || b.durationDays == null ? null : Number(b.durationDays),
    features: b.features || [],
    is_active: b.isActive !== false,
    sort_order: Number(b.sortOrder || 0),
    // Undefined means "don't touch"; explicit null clears an old upload
    // (the form uses an explicit removal button for that). An empty string
    // is normalised to null so the DB stays clean.
    ...(b.brochureUrl === undefined ? {} : { brochure_url: b.brochureUrl || null }),
    // Same "undefined means don't touch" rule, so a save from an older form
    // can never quietly switch Mains off for a bundle.
    ...(b.includesMains === undefined ? {} : { includes_mains: b.includesMains === true }),
    updated_at: new Date().toISOString(),
  };
  const { data, error } = await sb.from("plans").upsert(row).select().single();
  if (error) throw error;
  return data;
}

const MAX_BROCHURE = 20 * 1024 * 1024;

/**
 * Upload a programme brochure PDF for one plan and return its public URL.
 * Admin-only -- the `brochures` bucket policy enforces that server-side.
 *
 * Each upload lives under `{plan_code}/{timestamp}.pdf`, so replacing a
 * brochure is a fresh URL (no browser caching the old PDF at the same path)
 * and old files are simply orphaned in the bucket -- cheap, and an admin can
 * clean them up manually if disk ever matters. The `plans.brochure_url`
 * column always points at the LATEST upload.
 */
export async function uploadBrochure(planCode, file) {
  if (!file) throw new Error("No file selected.");
  if (file.type !== "application/pdf") throw new Error("Brochure must be a PDF file.");
  if (file.size > MAX_BROCHURE) throw new Error("Brochure must be under 20 MB.");
  const sb = await getSupabase();
  const path = `${planCode}/${Date.now()}.pdf`;
  const { error } = await sb.storage.from("brochures").upload(path, file, {
    cacheControl: "31536000",
    upsert: false,
    contentType: "application/pdf",
  });
  if (error) throw error;
  const { data } = sb.storage.from("brochures").getPublicUrl(path);
  return { url: data.publicUrl, path };
}

/**
 * Which published tests this student can actually open, mirroring the
 * database's can_access_test(): a tester opens everything, anyone opens a free
 * test, and otherwise a test must sit in a bundle the student holds right now.
 *
 * The catalogue used to list every published test of every exam, so a UPSC
 * buyer saw the BPSC papers marked "Included" and got "You don't have access"
 * on clicking one. `byPlan` also lets each bundle card count its own tests.
 */
export async function testAccess(userId) {
  if (import.meta.env.DEV && FIXTURES_ON()) return { all: true, ids: new Set(), byPlan: new Map() };
  const sb = await getSupabase();
  const [{ data: prof }, { data: enr, error }] = await Promise.all([
    sb.from("profiles").select("is_tester").eq("id", userId).maybeSingle(),
    sb.from("enrollments").select("plan_code, expires_at")
      .eq("student_id", userId).eq("status", "active"),
  ]);
  if (error) throw error;
  // byPlan covers every active-status bundle, expired ones too, so an expired
  // card still counts its own tests; only unexpired bundles unlock (ids).
  const now = Date.now();
  const rows = (enr ?? []).filter((e) => e.plan_code);
  const live = new Set(rows.filter((e) => !e.expires_at || new Date(e.expires_at).getTime() > now).map((e) => e.plan_code));
  const byPlan = new Map(rows.map((e) => [e.plan_code, new Set()]));
  if (byPlan.size > 0) {
    const { data, error: ptErr } = await sb.from("plan_tests").select("plan_code, test_id").in("plan_code", [...byPlan.keys()]);
    if (ptErr) throw ptErr;
    for (const r of data ?? []) byPlan.get(r.plan_code)?.add(r.test_id);
  }
  const ids = new Set([...byPlan].filter(([c]) => live.has(c)).flatMap(([, s]) => [...s]));
  return { all: !!prof?.is_tester, ids, byPlan };
}

/** Which tests are currently assigned to a bundle. */
export async function bundleTestIds(code) {
  if (import.meta.env.DEV && FIXTURES_ON()) return ["fx-test-0", "fx-test-1"];
  const sb = await getSupabase();
  const { data, error } = await sb.from("plan_tests").select("test_id").eq("plan_code", code);
  if (error) throw error;
  return (data ?? []).map((r) => r.test_id);
}

/** Replace a bundle's test list in one shot. */
export async function setBundleTests(code, testIds) {
  const sb = await getSupabase();
  const { error: delErr } = await sb.from("plan_tests").delete().eq("plan_code", code);
  if (delErr) throw delErr;
  if (testIds.length === 0) return;
  const { error } = await sb
    .from("plan_tests")
    .insert(testIds.map((id) => ({ plan_code: code, test_id: id })));
  if (error) throw error;
}

/* ------------------------------------------------------------- questions -- */

export function questionFromRow(r) {
  return {
    id: r.id,
    examCategory: r.exam_category,
    subject: r.subject,
    topic: r.topic || "",
    type: r.type,
    difficulty: r.difficulty,
    body: r.body,
    bodyHi: r.body_hi || "",
    // Type-specific stem for the BPSC formats (statements / list_1+list_2 /
    // assertion+reason / series). Hindi rides inside as parallel *_hi keys.
    questionData: r.question_data && typeof r.question_data === "object" ? r.question_data : {},
    // Option translations ride inside the option object as `body_hi`, keyed to
    // the option's own id — a parallel array would fall out of step the first
    // time an option is reordered or removed.
    options: Array.isArray(r.options) ? r.options : [],
    numericAnswer: r.numeric_answer,
    numericTolerance: r.numeric_tolerance ?? 0.01,
    marksCorrect: Number(r.marks_correct ?? 2),
    marksWrong: Number(r.marks_wrong ?? 0),
    explanation: r.explanation || "",
    explanationHi: r.explanation_hi || "",
    tags: r.tags || [],
    isActive: r.is_active !== false,
    // Tagging / provenance the generator and the QC workflow read.
    conceptGroupId: r.concept_group_id || "",
    sourceType: r.source_type || "",
    sourceCitation: r.source_citation || "",
    status: r.status || "published",
    caValidUntil: r.ca_valid_until || "",
    reviewDueDate: r.review_due_date || "",
    // System-managed usage/recalibration fields — read-only from the editor.
    timesUsed: r.times_used ?? 0,
    lastUsedDate: r.last_used_date || null,
    correctRate: r.correct_rate ?? null,
    createdAt: r.created_at,
  };
}

export function questionToRow(q) {
  // Mandatory, never inferred: every write states which exam this question
  // belongs to explicitly. questionToRow is the single choke point every
  // caller (QuestionForm, bulk import, starter pack) goes through.
  if (!q.examCategory) throw new Error("A question must have an exam (BPSC/UPSC) before it can be saved.");
  return {
    id: q.id,
    exam_category: q.examCategory,
    subject: q.subject,
    topic: q.topic || null,
    type: q.type,
    difficulty: q.difficulty,
    body: q.body,
    body_hi: (q.bodyHi || "").trim() || null,
    // {} for the plain formats; the BPSC formats carry their stem here.
    question_data: q.questionData && typeof q.questionData === "object" ? q.questionData : {},
    options: q.options || [],
    numeric_answer: q.type === "numerical" ? q.numericAnswer : null,
    numeric_tolerance: q.numericTolerance ?? 0.01,
    marks_correct: q.marksCorrect,
    marks_wrong: q.marksWrong,
    explanation: q.explanation || null,
    explanation_hi: (q.explanationHi || "").trim() || null,
    tags: q.tags || [],
    concept_group_id: q.conceptGroupId || null,
    source_type: q.sourceType || null,
    source_citation: q.sourceCitation || null,
    status: q.status || "published",
    ca_valid_until: q.caValidUntil || null,
    review_due_date: q.reviewDueDate || null,
    // times_used / last_used_* / correct_rate are written by the server
    // (commit_generated_test and the Phase-2 recalibration loop), never here —
    // a counter the editor could overwrite is a counter two paths disagree on.
    updated_at: new Date().toISOString(),
  };
}

// PostgREST caps any single response at this many rows (its own server-side
// default), silently -- no error, just a truncated result. Below 1000 total
// rows any of the paginated list-fetches below only ever loop once, so this
// was invisible for months; once the questions bank crossed that line, the
// oldest rows in whatever page didn't fit (History, in practice) simply
// stopped coming back. Every unbounded table-list fetch in this file loops
// past the cap using this same page size, rather than tripping over it.
const DB_PAGE_SIZE = 1000;

// `examCategory` is REQUIRED, not optional and never inferred from context —
// BPSC and UPSC share several subject names (History, Geography, Economy...)
// as plain strings, so a fetch that forgot to scope by exam would silently
// hand the caller a mixed bank. Every consumer (admin bank browser, manual
// test builder, the auto-generator) inherits this filter by going through
// here; there is deliberately no "give me everything" fallback.
export async function listQuestions(examCategory) {
  if (!examCategory) throw new Error("listQuestions requires an examCategory");
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_QUESTIONS.filter((q) => q.examCategory === examCategory);
  const sb = await getSupabase();
  const rows = [];
  for (let from = 0; ; from += DB_PAGE_SIZE) {
    const { data, error } = await sb
      .from("questions")
      .select("*")
      .eq("is_active", true)
      .eq("exam_category", examCategory)
      .order("created_at", { ascending: false })
      // Bulk imports insert many rows in one statement, so they share one
      // created_at down to the microsecond -- range() pagination needs a
      // unique tiebreaker or it can skip/repeat rows across page boundaries.
      .order("id", { ascending: true })
      .range(from, from + DB_PAGE_SIZE - 1);
    if (error) throw error;
    rows.push(...(data ?? []));
    if (!data || data.length < DB_PAGE_SIZE) break;
  }
  return rows.map(questionFromRow);
}

/**
 * Cheap totals for the dashboard -- total active count plus a per-subject
 * breakdown -- without pulling every question's full body/options/explanation
 * over the wire just to display a handful of numbers (that's what
 * listQuestions() is for, when the actual rows are needed).
 *
 * The total is a true server-side count (zero rows transferred). The
 * per-subject breakdown still has to page through `subject` values one
 * column wide, since PostgREST's select() has no GROUP BY -- but it pages
 * past the same 1000-row cap above rather than being capped by it, which is
 * the actual bug this replaces.
 */
export async function getQuestionStats(examCategory) {
  if (!examCategory) throw new Error("getQuestionStats requires an examCategory");
  if (import.meta.env.DEV && FIXTURES_ON()) {
    const qs = fx().FX_QUESTIONS.filter((q) => q.examCategory === examCategory);
    const bySubject = {};
    qs.forEach((q) => { bySubject[q.subject] = (bySubject[q.subject] || 0) + 1; });
    return { total: qs.length, bySubject };
  }
  const sb = await getSupabase();

  const { count, error: countErr } = await sb
    .from("questions")
    .select("*", { count: "exact", head: true })
    .eq("is_active", true)
    .eq("exam_category", examCategory);
  if (countErr) throw countErr;

  const bySubject = {};
  for (let from = 0; ; from += DB_PAGE_SIZE) {
    const { data, error } = await sb
      .from("questions")
      .select("subject")
      .eq("is_active", true)
      .eq("exam_category", examCategory)
      .order("id", { ascending: true })
      .range(from, from + DB_PAGE_SIZE - 1);
    if (error) throw error;
    (data ?? []).forEach((r) => { bySubject[r.subject] = (bySubject[r.subject] || 0) + 1; });
    if (!data || data.length < DB_PAGE_SIZE) break;
  }

  return { total: count ?? 0, bySubject };
}

export async function upsertQuestion(q) {
  const sb = await getSupabase();
  const { data, error } = await sb.from("questions").upsert(questionToRow(q)).select().single();
  if (error) throw error;
  return questionFromRow(data);
}

export async function deleteQuestion(id) {
  const sb = await getSupabase();
  // Soft delete: a question referenced by a past attempt must stay resolvable
  // or the student's review screen breaks.
  const { error } = await sb.from("questions").update({ is_active: false }).eq("id", id);
  if (error) throw error;
}

export async function insertQuestions(list) {
  const sb = await getSupabase();
  const rows = list.map((q) => {
    const row = questionToRow(q);
    delete row.id; // let the database mint ids for bulk imports
    return row;
  });
  const { data, error } = await sb.from("questions").insert(rows).select();
  if (error) throw error;
  return (data ?? []).map(questionFromRow);
}

/* ------------------------------------------------- courses/batches/series -- */

const crud = (table, mapRow = (r) => r, mapApp = (o) => o) => ({
  async list(order = "created_at") {
    if (import.meta.env.DEV && FIXTURES_ON()) {
      if (table === "materials") return fx().FX_MATERIALS;
      return [];
    }
    const sb = await getSupabase();
    const rows = [];
    for (let from = 0; ; from += DB_PAGE_SIZE) {
      const { data, error } = await sb
        .from(table)
        .select("*")
        .order(order, { ascending: false })
        .order("id", { ascending: true }) // tiebreaker so range() pagination can't skip/repeat rows that share an order value
        .range(from, from + DB_PAGE_SIZE - 1);
      if (error) throw error;
      rows.push(...(data ?? []));
      if (!data || data.length < DB_PAGE_SIZE) break;
    }
    return rows.map(mapRow);
  },
  async upsert(obj) {
    const sb = await getSupabase();
    const { data, error } = await sb.from(table).upsert(mapApp(obj)).select().single();
    if (error) throw error;
    return mapRow(data);
  },
  async remove(id) {
    const sb = await getSupabase();
    const { error } = await sb.from(table).delete().eq("id", id);
    if (error) throw error;
  },
});

export const courses = crud(
  "courses",
  (r) => ({ id: r.id, title: r.title, examTarget: r.exam_target || "", description: r.description || "", isPublished: !!r.is_published, createdAt: r.created_at }),
  (c) => ({ id: c.id, title: c.title, exam_target: c.examTarget || null, description: c.description || null, is_published: !!c.isPublished }),
);

export const batches = crud(
  "batches",
  (r) => ({ id: r.id, courseId: r.course_id, name: r.name, price: Number(r.price || 0), seatLimit: r.seat_limit, startDate: r.start_date || "", endDate: r.end_date || "", isActive: !!r.is_active, createdAt: r.created_at }),
  (b) => ({ id: b.id, course_id: b.courseId || null, name: b.name, price: Number(b.price || 0), seat_limit: b.seatLimit ? Number(b.seatLimit) : null, start_date: b.startDate || null, end_date: b.endDate || null, is_active: !!b.isActive }),
);

export const materials = crud(
  "materials",
  (r) => ({ id: r.id, title: r.title, description: r.description || "", subject: r.subject || "", type: r.type, url: r.url || "", batchId: r.batch_id, isFree: !!r.is_free, isPublished: !!r.is_published, createdAt: r.created_at }),
  (m) => ({ id: m.id, title: m.title, description: m.description || null, subject: m.subject || null, type: m.type, url: m.url || null, batch_id: m.batchId || null, is_free: !!m.isFree, is_published: m.isPublished !== false }),
);

const seriesFromRow = (r) => ({ id: r.id, title: r.title, description: r.description || "", batchId: r.batch_id, price: Number(r.price || 0), isFree: !!r.is_free, examCategory: r.exam_category, createdAt: r.created_at });
export const series = crud(
  "test_series",
  seriesFromRow,
  (s) => ({ id: s.id, title: s.title, description: s.description || null, batch_id: s.batchId || null, price: Number(s.price || 0), is_free: !!s.isFree, exam_category: s.examCategory }),
);

/** Series of one exam only (migration 0025) -- the admin's pickers never offer another exam's series. */
export async function listSeries(examCategory) {
  if (!examCategory) throw new Error("listSeries requires an examCategory");
  if (import.meta.env.DEV && FIXTURES_ON()) return [];
  const sb = await getSupabase();
  const { data, error } = await sb.from("test_series").select("*").eq("exam_category", examCategory).order("created_at", { ascending: false });
  if (error) throw error;
  return (data ?? []).map(seriesFromRow);
}

/* ------------------------------------------------------------------ tests -- */

function testFromRow(r) {
  return {
    id: r.id,
    examCategory: r.exam_category,
    title: r.title,
    titleHi: r.title_hi || "",
    description: r.description || "",
    seriesId: r.series_id,
    seriesTitle: r.test_series?.title || "",
    seriesTitleHi: r.test_series?.title_hi || "",
    durationMin: r.duration_min ?? 60,
    sections: Array.isArray(r.sections) ? r.sections : [],
    isFree: !!r.is_free,
    isPublished: !!r.is_published,
    shuffleQuestions: !!r.shuffle_questions,
    shuffleOptions: !!r.shuffle_options,
    scheduledFor: r.scheduled_for,
    totalQuestions: r.total_questions ?? 0,
    totalMarks: Number(r.total_marks ?? 0),
    createdAt: r.created_at,
  };
}

function testToRow(t) {
  return {
    id: t.id,
    // A test belongs to one exam (migration 0025). The DB guard fills it from
    // the blueprint/series/questions when absent and refuses any mixing.
    exam_category: t.examCategory || null,
    title: t.title,
    title_hi: (t.titleHi || "").trim() || null,
    description: t.description || null,
    series_id: t.seriesId || null,
    duration_min: Number(t.durationMin || 60),
    sections: t.sections || [],
    is_free: !!t.isFree,
    is_published: !!t.isPublished,
    shuffle_questions: !!t.shuffleQuestions,
    shuffle_options: !!t.shuffleOptions,
    scheduled_for: t.scheduledFor || null,
  };
}

// examCategory scopes the list to one exam (the admin workspace always passes
// it); the student catalogue omits it and stays gated by bundles.
export async function listTests({ publishedOnly = false, examCategory = null } = {}) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_TESTS.filter((t) => (!publishedOnly || t.isPublished) && (!examCategory || (t.examCategory || "bpsc") === examCategory));
  const sb = await getSupabase();
  const rows = [];
  for (let from = 0; ; from += DB_PAGE_SIZE) {
    let q = sb
      .from("tests")
      .select("*, test_series(title, title_hi)")
      .order("created_at", { ascending: false })
      .order("id", { ascending: true }) // tiebreaker so range() pagination can't skip/repeat rows that share an order value
      .range(from, from + DB_PAGE_SIZE - 1);
    if (publishedOnly) q = q.eq("is_published", true);
    if (examCategory) q = q.eq("exam_category", examCategory);
    const { data, error } = await q;
    if (error) throw error;
    rows.push(...(data ?? []));
    if (!data || data.length < DB_PAGE_SIZE) break;
  }
  // Level 1 before Level 2, Test 1 before Test 2 -- see lib/testOrder.js.
  return sortTests(rows.map(testFromRow));
}

export async function upsertTest(t) {
  const sb = await getSupabase();
  const { data, error } = await sb.from("tests").upsert(testToRow(t)).select("*, test_series(title, title_hi)").single();
  if (error) throw error;
  return testFromRow(data);
}

export async function deleteTest(id) {
  const sb = await getSupabase();
  const { error } = await sb.from("tests").delete().eq("id", id);
  if (error) throw error;
}

/* ----------------------------------------------- generation: config & blueprints -- */

/**
 * distribution_config — the PYQ-derived target weights the generator matches.
 * Weights key on the existing free-text subject/topic values (no enum), so a
 * new subject the admin adds simply becomes another weightable key.
 */
export const distributionConfigs = crud(
  "distribution_config",
  (r) => ({
    id: r.id,
    examCategory: r.exam_category,
    name: r.name,
    subjectWeights: r.subject_weights || {},
    difficultyWeights: r.difficulty_weights || {},
    questionTypeWeights: r.question_type_weights || {},
    subTopicWeights: r.sub_topic_weights || {},
    createdAt: r.created_at,
  }),
  (c) => ({
    id: c.id || undefined,
    exam_category: c.examCategory,
    name: c.name,
    subject_weights: c.subjectWeights || {},
    difficulty_weights: c.difficultyWeights || {},
    question_type_weights: c.questionTypeWeights || {},
    sub_topic_weights: c.subTopicWeights || {},
    updated_at: new Date().toISOString(),
  }),
);

const blueprintFromRow = (r) => ({
  id: r.id,
  examCategory: r.exam_category,
  seriesId: r.series_id,
  sequencePosition: r.sequence_position ?? 1,
  title: r.title,
  titleHi: r.title_hi || "",
  patternType: r.pattern_type,
  questionCount: r.question_count ?? 150,
  subjectScope: r.subject_scope || {},
  distributionConfigId: r.distribution_config_id || "",
  themeGroupId: r.theme_group_id || "",
  themePartIndex: r.theme_part_index ?? "",
  createdAt: r.created_at,
});

const blueprintToRow = (b) => ({
  id: b.id || undefined,
  exam_category: b.examCategory,
  series_id: b.seriesId || null,
  sequence_position: Number(b.sequencePosition || 1),
  title: b.title,
  title_hi: (b.titleHi || "").trim() || null,
  pattern_type: b.patternType,
  question_count: Number(b.questionCount || 150),
  subject_scope: b.subjectScope || {},
  distribution_config_id: b.distributionConfigId || null,
  theme_group_id: b.themeGroupId || null,
  theme_part_index: b.themePartIndex === "" || b.themePartIndex == null ? null : Number(b.themePartIndex),
  updated_at: new Date().toISOString(),
});

/** Blueprints for a series (or all of them), ordered by their sequence. */
export async function listBlueprints(seriesId = null) {
  const sb = await getSupabase();
  let q = sb.from("test_blueprints").select("*").order("sequence_position");
  if (seriesId) q = q.eq("series_id", seriesId);
  const { data, error } = await q;
  if (error) throw error;
  return (data ?? []).map(blueprintFromRow);
}

export async function upsertBlueprint(b) {
  const sb = await getSupabase();
  const { data, error } = await sb.from("test_blueprints").upsert(blueprintToRow(b)).select().single();
  if (error) throw error;
  return blueprintFromRow(data);
}

export async function deleteBlueprint(id) {
  const sb = await getSupabase();
  const { error } = await sb.from("test_blueprints").delete().eq("id", id);
  if (error) throw error;
}

/** The whole usage ledger — the generator reads it for cooldown + theme dedup. */
export async function questionUsages() {
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("question_usages")
    .select("question_id, test_id, blueprint_id, theme_group_id, concept_group_id, used_at");
  if (error) throw error;
  return (data ?? []).map((u) => ({
    questionId: u.question_id,
    testId: u.test_id,
    blueprintId: u.blueprint_id,
    themeGroupId: u.theme_group_id,
    conceptGroupId: u.concept_group_id,
    usedAt: u.used_at,
  }));
}

/** The most recent N test ids — the cooldown window for the generator. */
export async function recentTestIds(limit = 5) {
  const sb = await getSupabase();
  const { data, error } = await sb.from("tests").select("id").order("created_at", { ascending: false }).limit(limit);
  if (error) throw error;
  return (data ?? []).map((r) => r.id);
}

/**
 * Persist a generated paper atomically. The server writes the test row, records
 * one question_usages line per question, and recomputes each question's
 * times_used from that ledger — so the counters stay honest even on a re-commit.
 */
export async function commitGeneratedTest(test, { blueprintId = null, themeGroupId = null } = {}) {
  const sb = await getSupabase();
  const p_test = {
    id: test.id || undefined,
    title: test.title,
    title_hi: (test.titleHi || "").trim() || null,
    description: test.description || null,
    series_id: test.seriesId || null,
    duration_min: Number(test.durationMin || 60),
    sections: test.sections || [],
    is_free: !!test.isFree,
    is_published: !!test.isPublished,
    shuffle_questions: test.shuffleQuestions !== false,
    shuffle_options: test.shuffleOptions !== false,
    scheduled_for: test.scheduledFor || null,
  };
  const { data, error } = await sb.rpc("commit_generated_test", {
    p_test,
    p_blueprint: blueprintId || null,
    p_theme_group: themeGroupId || null,
  });
  if (error) throw error;
  return data; // the persisted test id
}

/**
 * Load one test in the exact shape the exam engine wants.
 *
 * Correct answers ARE included — this is a client-side-scored mock, the same
 * as every competitor in this market. If that changes, move `evaluate()` into
 * an edge function and strip `correct`/`explanation` here.
 */
export async function loadExamTest(testId) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_EXAM;
  const sb = await getSupabase();

  // The paper comes from a database function that strips every answer field.
  // It used to be `select * from questions`, which put options[].isCorrect,
  // numeric_answer and the explanation in the browser before the student had
  // answered anything — readable straight from the Network tab mid-exam.
  const { data, error } = await sb.rpc("exam_paper", { p_test: testId });
  if (error) {
    const msg = String(error.message || "");
    if (msg.includes("no_access")) throw new Error("You don't have access to this test.");
    if (msg.includes("test_not_found")) throw new Error("This test is not available.");
    throw error;
  }
  const paper = data;
  if (!paper || !Array.isArray(paper.sections)) throw new Error("This test has no questions yet.");

  const shuffle = (arr) => {
    const a = [...arr];
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  };

  // Shuffling stays client-side and is now harmless: an option carries its own
  // id, and that id is what travels back at submit time, so the order the
  // student saw cannot change what counts as correct.
  const sections = paper.sections
    .map((sec) => {
      let qs = Array.isArray(sec.questions) ? sec.questions : [];
      if (paper.shuffleQuestions) qs = shuffle(qs);
      return {
        name: sec.name || "Section",
        name_hi: sec.name_hi || "",
        questions: qs.map((q) => ({
          ...q,
          // Answer ladders ("Only one / Only two / All three / None", the A-R
          // verdicts) read in a fixed order on the real paper; a question opts
          // out of option shuffling with question_data.fixed_option_order.
          options: paper.shuffleOptions && Array.isArray(q.options) && !q.data?.fixed_option_order
            ? shuffle(q.options) : (q.options || []),
        })),
      };
    })
    .filter((s) => s.questions.length > 0);

  if (sections.length === 0) throw new Error("This test has no questions yet.");

  return {
    id: paper.id,
    title: paper.title,
    // The exam screen renders inLang(lang, EXAM.title, EXAM.title_hi); these two
    // were dropped here, so a Hindi-mode paper always showed its English title.
    title_hi: paper.title_hi || "",
    seriesTitle: paper.seriesTitle || "",
    seriesTitle_hi: paper.seriesTitle_hi || "",
    // Which exam the paper belongs to (migration 0027) -- the exam screen hides
    // the sub-topic tag on UPSC papers, as the real paper carries none.
    examCategory: paper.examCategory || "",
    durationSec: (paper.durationMin ?? 60) * 60,
    durationMin: paper.durationMin ?? 60,
    shuffleQuestions: !!paper.shuffleQuestions,
    shuffleOptions: !!paper.shuffleOptions,
    // Only staff can open an unpublished paper (migration 0026).
    isPreview: !!paper.isPreview,
    sections,
  };
}

/**
 * Submit a finished paper. The browser sends which option ids were chosen and
 * nothing else — the score, the section and topic breakdowns, the rank and the
 * percentile are all computed server-side and written by the service role.
 * `attempts` is no longer writable from the client at all.
 */
export async function submitAttempt({ testId, answers, timeSpent, timeUsed, startedAt, shownOrder, marked }) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_EXAM_RESULT;
  const sb = await getSupabase();
  const { data, error } = await sb.functions.invoke("submit-attempt", {
    body: { testId, answers, timeSpent, timeUsed, startedAt, shownOrder, marked },
  });
  if (error) {
    const detail = await error?.context?.json?.().catch(() => null);
    if (detail?.error === "no_access") throw new Error("You don't have access to this test.");
    throw error;
  }
  return data;
}

export function attemptFromRow(r) {
  const max = Number(r.max_score || 0);
  const score = Number(r.score || 0);
  return {
    id: r.id,
    testId: r.test_id,
    title: r.test_title || r.tests?.title || "Test",
    series: r.series_title || "",
    date: r.submitted_at || r.started_at,
    score,
    maxScore: max,
    scorePct: max > 0 ? (score / max) * 100 : 0,
    totalQ: r.total_questions ?? 0,
    correct: r.correct_count ?? 0,
    wrong: r.wrong_count ?? 0,
    skipped: Math.max(0, (r.total_questions ?? 0) - (r.correct_count ?? 0) - (r.wrong_count ?? 0)),
    accuracy: Number(r.accuracy || 0),
    // Snapshot taken when the paper was submitted. Rank drifts as more people
    // attempt, so `refreshAttemptStanding` re-reads it when a report is opened.
    percentile: r.percentile != null ? Number(r.percentile) : null,
    rank: r.rank_in_test ?? null,
    totalStudents: r.total_peers ?? null,
    timeSec: r.time_taken_sec ?? 0,
    durationMin: r.duration_min ?? 0,
    sections: Array.isArray(r.section_stats) ? r.section_stats : [],
    topics: Array.isArray(r.topic_stats) ? r.topic_stats : [],
    difficultyStats: Array.isArray(r.difficulty_stats) ? r.difficulty_stats : [],
    typeStats: Array.isArray(r.type_stats) ? r.type_stats : [],
    review: Array.isArray(r.review) ? r.review : [],
    answers: r.answers || {},
  };
}

export async function listAttempts(userId, { limit = 100 } = {}) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_ATTEMPTS;
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("attempts")
    .select("*")
    .eq("student_id", userId)
    .eq("status", "submitted")
    .order("submitted_at", { ascending: true })
    .limit(limit);
  if (error) throw error;
  return (data ?? []).map(attemptFromRow);
}

/**
 * The cross-attempt review drill-down (§7). Returns this student's own answered
 * questions — optionally one subject, optionally only the wrong ones — each in
 * the review-row shape ReviewCard renders, with explanation, source and the
 * crowd success rate. Goes through the SECURITY DEFINER my_review() because
 * students have no direct read on `questions`; the function only ever returns
 * the caller's own rows.
 */
export async function myReview(subject = null, { wrongOnly = false } = {}) {
  if (import.meta.env.DEV && FIXTURES_ON()) {
    let rows = fx().FX_MY_REVIEW;
    if (subject) rows = rows.filter((r) => r.subject === subject);
    return rows;
  }
  const sb = await getSupabase();
  const { data, error } = await sb.rpc("my_review", {
    p_subject: subject || null,
    p_wrong_only: !!wrongOnly,
  });
  if (error) throw error;
  return Array.isArray(data) ? data : [];
}


/** Persist the standing snapshot so the report still shows a rank after a
    reload — it used to be computed once and then thrown away. */

/** Recompute a stored standing — cheap enough to run when a report is opened. */

/** Real rank + percentile for a submitted attempt, computed in Postgres. */
export async function attemptStanding(attemptId) {
  try {
    const sb = await getSupabase();
    const { data, error } = await sb.rpc("attempt_standing", { p_attempt: attemptId });
    if (error) throw error;
    const row = Array.isArray(data) ? data[0] : data;
    if (!row) return null;
    return { rank: row.rank, total: row.total, percentile: Number(row.percentile) };
  } catch (e) {
    console.warn("standing unavailable", e);
    return null;
  }
}

/** Peer figures for one test — what "batch average" and "topper" actually are. */
export async function testStats(testId) {
  if (import.meta.env.DEV && FIXTURES_ON()) return { takers: 980, avgPct: 54.2, bestPct: 91.5 };
  if (!testId) return null;
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("attempts")
    .select("score, max_score")
    .eq("test_id", testId)
    .eq("status", "submitted");
  if (error) throw error;
  const rows = (data ?? []).filter((r) => Number(r.max_score) > 0);
  if (rows.length === 0) return null;
  const pcts = rows.map((r) => (Number(r.score) / Number(r.max_score)) * 100);
  return {
    takers: rows.length,
    avgPct: pcts.reduce((a, b) => a + b, 0) / pcts.length,
    bestPct: Math.max(...pcts),
  };
}

/* ------------------------------------------------------------- analytics -- */

/** Per-subject accuracy across every attempt — replaces the hardcoded map. */
export function subjectStrength(attempts) {
  const agg = {};
  attempts.forEach((a) => {
    (a.topics || []).forEach((t) => {
      const key = t.subject || t.name;
      if (!key) return;
      if (!agg[key]) agg[key] = { correct: 0, total: 0 };
      agg[key].correct += t.correct ?? 0;
      agg[key].total += t.total ?? 0;
    });
  });
  return Object.entries(agg)
    .filter(([, v]) => v.total > 0)
    .map(([name, v]) => {
      const acc = (v.correct / v.total) * 100;
      return { name, acc: Math.round(acc), band: bandFor(acc), attempts: v.total };
    })
    .sort((a, b) => b.acc - a.acc);
}

export async function studyActivity(userId, days = 84) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_ACTIVITY;
  const sb = await getSupabase();
  const from = new Date(Date.now() - (days - 1) * 86400000).toISOString().slice(0, 10);
  const { data, error } = await sb
    .from("study_activity")
    .select("day, count")
    .eq("student_id", userId)
    .gte("day", from);
  if (error) throw error;

  const byDay = new Map((data ?? []).map((r) => [r.day, r.count]));
  const out = [];
  for (let i = days - 1; i >= 0; i--) {
    const d = new Date(Date.now() - i * 86400000);
    const key = d.toISOString().slice(0, 10);
    out.push({ date: d, count: Math.min(4, byDay.get(key) ?? 0) });
  }
  return out;
}

export function streakFrom(activity) {
  let s = 0;
  for (let i = activity.length - 1; i >= 0; i--) {
    if (activity[i].count > 0) s++;
    else break;
  }
  return s;
}

export async function leaderboard({ limit = 50 } = {}) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_LEADERBOARD;
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("leaderboard_v")
    .select("*")
    .order("rank", { ascending: true })
    .limit(limit);
  if (error) throw error;
  return data ?? [];
}

/* --------------------------------------------------- notifications & misc -- */

export async function listNotifications(userId) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_NOTIFICATIONS;
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("notifications")
    .select("*")
    .or(`user_id.eq.${userId},user_id.is.null`)
    .order("created_at", { ascending: false })
    .limit(20);
  if (error) throw error;
  return data ?? [];
}

export async function markNotificationsRead(userId) {
  const sb = await getSupabase();
  await sb
    .from("notifications")
    .update({ read_at: new Date().toISOString() })
    .eq("user_id", userId)
    .is("read_at", null);
}

export async function listReminders(userId) {
  if (import.meta.env.DEV && FIXTURES_ON()) return new Set(["fx-test-3"]);
  const sb = await getSupabase();
  const { data } = await sb.from("test_reminders").select("test_id").eq("student_id", userId);
  return new Set((data ?? []).map((r) => r.test_id));
}

export async function toggleReminder(userId, testId, on) {
  const sb = await getSupabase();
  if (on) {
    const { error } = await sb.from("test_reminders").insert({ student_id: userId, test_id: testId });
    if (error && error.code !== "23505") throw error;
  } else {
    const { error } = await sb.from("test_reminders").delete().eq("student_id", userId).eq("test_id", testId);
    if (error) throw error;
  }
}

/* listBookmarks() removed. It embedded questions(options, explanation,
   numeric_answer) — the answer key — and no screen ever called it. Students no
   longer have any direct read on `questions`, so it would return nothing
   anyway. If a bookmarks screen is built later it must read from
   attempts.review, or go through a SECURITY DEFINER function that checks the
   student actually sat the paper first. toggleBookmark() below still works:
   it only writes. */


export async function toggleBookmark(userId, questionId, on) {
  const sb = await getSupabase();
  if (on) {
    const { error } = await sb.from("bookmarks").insert({ student_id: userId, question_id: questionId });
    if (error && error.code !== "23505") throw error;
  } else {
    const { error } = await sb.from("bookmarks").delete().eq("student_id", userId).eq("question_id", questionId);
    if (error) throw error;
  }
}

/* ---------------------------------------------------------------- files -- */

const MAX_AVATAR = 3 * 1024 * 1024;
const MAX_MATERIAL = 50 * 1024 * 1024;

function extOf(file) {
  const m = /\.([A-Za-z0-9]+)$/.exec(file.name || "");
  return m ? m[1].toLowerCase() : "bin";
}

/**
 * Upload a study-material file and return its public URL.
 * Admin-only — the storage policy enforces that, not this function.
 */
export async function uploadMaterialFile(file, onProgress) {
  if (!file) throw new Error("No file selected.");
  if (file.size > MAX_MATERIAL) throw new Error("File must be under 50 MB.");
  const sb = await getSupabase();
  const path = `${new Date().getFullYear()}/${crypto.randomUUID()}.${extOf(file)}`;
  onProgress?.(10);
  const { error } = await sb.storage.from("materials").upload(path, file, {
    cacheControl: "31536000",
    upsert: false,
    contentType: file.type || undefined,
  });
  if (error) throw error;
  onProgress?.(100);
  const { data } = sb.storage.from("materials").getPublicUrl(path);
  return { url: data.publicUrl, path };
}

/**
 * Upload a profile photo into the caller's own folder and return its URL.
 * Photos used to be inlined as base-64 data URLs on the profiles row.
 */
export async function uploadAvatar(userId, file) {
  if (!file) throw new Error("No file selected.");
  if (!file.type.startsWith("image/")) throw new Error("Please choose an image file.");
  if (file.size > MAX_AVATAR) throw new Error("Image must be under 3 MB.");
  const sb = await getSupabase();
  // A stable name per user means old photos are replaced, not accumulated.
  const path = `${userId}/avatar.${extOf(file)}`;
  const { error } = await sb.storage.from("avatars").upload(path, file, {
    cacheControl: "3600",
    upsert: true,
    contentType: file.type,
  });
  if (error) throw error;
  const { data } = sb.storage.from("avatars").getPublicUrl(path);
  // Cache-bust so the new photo shows immediately.
  return `${data.publicUrl}?v=${Date.now()}`;
}


/* ------------------------------------------------------- public content -- */
/* Syllabus, PYQ, NCERT, current affairs and FAQ. All readable without an
   account — that is the whole point of the content hub. */

/** Syllabus grouped exam → paper → rows, ready to render. */
export async function syllabus(exam) {
  const sb = await getSupabase();
  let q = sb.from("syllabus_topics").select("*").eq("is_published", true).order("sort_order");
  if (exam) q = q.eq("exam", exam);
  const { data, error } = await q;
  if (error) throw error;
  const byPaper = new Map();
  (data ?? []).forEach((r) => {
    if (!byPaper.has(r.paper)) byPaper.set(r.paper, []);
    byPaper.get(r.paper).push({ id: r.id, section: r.section || "", topic: r.topic, detail: r.detail || "" });
  });
  return [...byPaper.entries()].map(([paper, topics]) => ({ paper, topics }));
}

export async function syllabusExams() {
  const sb = await getSupabase();
  const { data } = await sb.from("syllabus_topics").select("exam").eq("is_published", true);
  return [...new Set((data ?? []).map((r) => r.exam))];
}

export async function pyqPapers() {
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("pyq_papers").select("*").eq("is_published", true)
    .order("year", { ascending: false }).order("paper");
  if (error) throw error;
  return (data ?? []).map((r) => ({
    id: r.id, exam: r.exam, year: r.year, paper: r.paper, title: r.title,
    paperUrl: r.paper_url || "", solutionUrl: r.solution_url || "",
    questionCount: r.question_count, notes: r.notes || "",
  }));
}

export async function ncertBooks() {
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("ncert_books").select("*").eq("is_published", true)
    .order("class_level").order("sort_order").order("subject");
  if (error) throw error;
  return (data ?? []).map((r) => ({
    id: r.id, classLevel: r.class_level, subject: r.subject,
    title: r.title, language: r.language, url: r.url || "",
  }));
}

export async function currentAffairs({ limit = 40 } = {}) {
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("current_affairs").select("*").eq("is_published", true)
    .order("published_on", { ascending: false }).limit(limit);
  if (error) throw error;
  return (data ?? []).map((r) => ({
    id: r.id, date: r.published_on, title: r.title, summary: r.summary || "",
    body: r.body || "", tags: r.tags || [], examTags: r.exam_tags || [],
    sourceName: r.source_name || "", sourceUrl: r.source_url || "",
  }));
}

export async function faqs() {
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("faqs").select("*").eq("is_published", true).order("sort_order");
  if (error) throw error;
  return (data ?? []).map((r) => ({
    id: r.id, category: r.category, question: r.question, answer: r.answer,
    // Nullable, same opt-in shape as every other bilingual field in this
    // schema -- a row with no translation yet just falls back to English.
    questionHi: r.question_hi || "", answerHi: r.answer_hi || "",
  }));
}

/** Free study material — the one page that must work for logged-out visitors. */
export async function freeMaterials() {
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("materials").select("*")
    .eq("is_published", true).eq("is_free", true)
    .order("created_at", { ascending: false });
  if (error) throw error;
  return (data ?? []).map((r) => ({
    id: r.id, title: r.title, description: r.description || "", subject: r.subject || "",
    type: r.type, url: r.url || "",
  }));
}

/* ---------------------------------------------------- admin: content CRUD -- */

const contentCrud = (table, order = "sort_order") => ({
  async list() {
    const sb = await getSupabase();
    const { data, error } = await sb.from(table).select("*").order(order, { ascending: order !== "published_on" && order !== "year" });
    if (error) throw error;
    return data ?? [];
  },
  async upsert(row) {
    const sb = await getSupabase();
    const { data, error } = await sb.from(table).upsert(row).select().single();
    if (error) throw error;
    return data;
  },
  async remove(id) {
    const sb = await getSupabase();
    const { error } = await sb.from(table).delete().eq("id", id);
    if (error) throw error;
  },
});

export const adminSyllabus = contentCrud("syllabus_topics");
export const adminPyq      = contentCrud("pyq_papers", "year");
export const adminNcert    = contentCrud("ncert_books");
export const adminCA       = contentCrud("current_affairs", "published_on");
export const adminFaqs     = contentCrud("faqs");


/* ---------------------------------------------------------------- coupons -- */

/**
 * Ask the server what a code is worth. Deliberately an edge-function call and
 * not a table read: the coupons table is admin-only, so a student can never
 * list every code on the site — they learn one code's value by submitting it.
 */
export async function checkCoupon(code, planCode) {
  const sb = await getSupabase();
  const { data, error } = await sb.functions.invoke("coupon-check", {
    body: { code, plan: planCode },
  });
  if (error) {
    // supabase-js turns a non-2xx into an error; the body still carries the
    // reason, so surface that rather than a generic failure.
    const body = await error?.context?.json?.().catch(() => null);
    if (body) return body;
    throw error;
  }
  return data;
}

/* ------------------------------------------------------- admin: coupons -- */

const couponFromRow = (r) => ({
  id: r.id,
  code: r.code,
  description: r.description || "",
  discountType: r.discount_type,
  discountValue: Number(r.discount_value),
  maxDiscount: r.max_discount_paise ? r.max_discount_paise / 100 : "",
  minOrder: r.min_order_paise ? r.min_order_paise / 100 : "",
  planCodes: r.applicable_plan_codes || [],
  maxUses: r.max_uses ?? "",
  usedCount: r.used_count ?? 0,
  maxUsesPerUser: r.max_uses_per_user ?? 1,
  validFrom: r.valid_from,
  validUntil: r.valid_until,
  isActive: r.is_active !== false,
  createdAt: r.created_at,
});

export async function adminListCoupons() {
  const sb = await getSupabase();
  const { data, error } = await sb.from("coupons").select("*").order("created_at", { ascending: false });
  if (error) throw error;
  return (data ?? []).map(couponFromRow);
}

export async function upsertCoupon(c) {
  const sb = await getSupabase();
  const row = {
    id: c.id || undefined,
    code: String(c.code || "").trim().toUpperCase(),
    description: c.description || null,
    discount_type: c.discountType,
    discount_value: Number(c.discountValue),
    // Rupees in the form, paise in the column — same rule as bundle pricing.
    max_discount_paise: c.maxDiscount === "" || c.maxDiscount == null ? null : Math.round(Number(c.maxDiscount) * 100),
    min_order_paise: c.minOrder === "" || c.minOrder == null ? 0 : Math.round(Number(c.minOrder) * 100),
    applicable_plan_codes: (c.planCodes && c.planCodes.length) ? c.planCodes : null,
    max_uses: c.maxUses === "" || c.maxUses == null ? null : Number(c.maxUses),
    max_uses_per_user: Number(c.maxUsesPerUser || 1),
    valid_until: c.validUntil || null,
    is_active: c.isActive !== false,
  };
  const { data, error } = await sb.from("coupons").upsert(row).select().single();
  if (error) throw error;
  return couponFromRow(data);
}

export async function deleteCoupon(id) {
  const sb = await getSupabase();
  const { error } = await sb.from("coupons").delete().eq("id", id);
  if (error) throw error;
}

/** Who used a code, and when — for the admin's redemption view. */
export async function couponRedemptions(couponId) {
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("coupon_redemptions")
    .select("id, student_id, discount_paise, redeemed_at")
    .eq("coupon_id", couponId)
    .order("redeemed_at", { ascending: false });
  if (error) throw error;
  const ids = [...new Set((data ?? []).map((r) => r.student_id))];
  const names = new Map();
  if (ids.length) {
    const { data: profs } = await sb.from("profiles").select("id, full_name, email").in("id", ids);
    (profs ?? []).forEach((p) => names.set(p.id, p));
  }
  return (data ?? []).map((r) => ({
    id: r.id,
    name: names.get(r.student_id)?.full_name || "—",
    email: names.get(r.student_id)?.email || "—",
    discount: (r.discount_paise ?? 0) / 100,
    at: r.redeemed_at,
  }));
}

/* ------------------------------------------------------------- referrals -- */

/**
 * Referrals are captured from a `?ref=CODE` link and applied automatically.
 * There is deliberately no "enter a referral code" box anywhere in the UI —
 * a typed field invites students to swap codes in comment sections, which is
 * exactly the abuse the link-only rule exists to prevent.
 */
const REF_KEY = "pending_ref";

/**
 * Read `?ref=` off the landing URL and remember it.
 *
 * Stored rather than used immediately because the visitor is almost never
 * signed in at this point: they read the homepage, maybe browse for days, and
 * only then create an account. The code has to survive all of that, plus the
 * round-trip through Google OAuth or an emailed magic link.
 *
 * The param is stripped from the address bar afterwards so the code does not
 * ride along into anything the student later shares or bookmarks.
 */
export function capturePendingReferral() {
  if (typeof window === "undefined") return null;
  let code = null;
  try {
    const url = new URL(window.location.href);
    const raw = url.searchParams.get("ref");
    if (raw) {
      // Codes are 8 chars from a fixed alphabet; anything else is noise or a
      // probe and is not worth storing.
      const clean = raw.trim().toUpperCase();
      if (/^[A-Z0-9]{4,16}$/.test(clean)) {
        code = clean;
        saveKey(REF_KEY, { code, at: Date.now() });
      }
      url.searchParams.delete("ref");
      window.history.replaceState(null, "", url.pathname + url.search + url.hash);
    }
  } catch { /* malformed URL — nothing to capture */ }
  return code || loadKey(REF_KEY, null)?.code || null;
}

export function pendingReferral() {
  return loadKey(REF_KEY, null)?.code || null;
}

/**
 * Bind the stored code to the signed-in student. Safe to call on every boot:
 * the database refuses a second binding, and `already_bound` is a success from
 * the caller's point of view.
 *
 * The profile row must exist first — `referrals.referred_id` is a foreign key
 * to it — so this runs after ensureProfile().
 */
export async function claimPendingReferral() {
  const code = pendingReferral();
  if (!code) return null;

  try {
    const sb = await getSupabase();
    const { data, error } = await sb.rpc("bind_referral", { p_code: code });
    if (error) throw error;

    // Every outcome except a transient failure is final: stop retrying so a
    // stale code cannot follow someone around forever.
    if (data !== "not_signed_in") removeKey(REF_KEY);
    return data;
  } catch (e) {
    console.warn("referral binding deferred", e?.message || e);
    return null; // keep the code and try again next boot
  }
}

export async function myReferralStats() {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_REFERRAL_STATS;
  const sb = await getSupabase();
  const { data, error } = await sb.rpc("my_referral_stats");
  if (error) throw error;
  const r = Array.isArray(data) ? data[0] : data;
  if (!r) return null;
  return {
    code: r.code || "",
    total: r.total_referred ?? 0,
    paid: r.paid_referred ?? 0,
    pending: r.pending_bonus ?? 0,
    bonus: (r.bonus_paise ?? 0) / 100,
  };
}

export async function myReferrals() {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_REFERRAL_LIST;
  const sb = await getSupabase();
  const { data, error } = await sb.rpc("my_referral_list");
  if (error) throw error;
  return (data ?? []).map((r) => ({
    name: r.masked_name || "Aspirant",
    joined: r.joined_at,
    paid: !!r.has_paid,
    status: r.bonus_status || "pending",
  }));
}

/** The shareable link itself. Built from the live origin so it is correct on
 *  the Vercel domain, a preview deploy and localhost alike. */
export function referralLink(code) {
  if (!code) return "";
  const origin = typeof window !== "undefined" ? window.location.origin : "";
  return `${origin}/?ref=${code}`;
}


/* ---------------------------------------------------------------- wallet -- */

/**
 * Balance is never stored — it is `sum(amount_paise)` over completed ledger
 * lines, computed on read. A stored balance is a number two code paths can
 * disagree about, and when they disagree it is real money that is wrong.
 *
 * `can_withdraw` is evaluated fresh on every call, never cached: eligibility
 * turns on and off as enrollments expire and renew (spec fraud rule 8).
 */
export async function myWallet() {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_WALLET;
  const sb = await getSupabase();
  const { data, error } = await sb.rpc("my_wallet");
  if (error) throw error;
  const r = Array.isArray(data) ? data[0] : data;
  if (!r) return null;
  return {
    balance: (r.balance_paise ?? 0) / 100,
    lifetime: (r.lifetime_paise ?? 0) / 100,
    pending: (r.pending_paise ?? 0) / 100,
    bonus: (r.bonus_paise ?? 0) / 100,
    minWithdraw: (r.min_withdraw_paise ?? 0) / 100,
    canWithdraw: !!r.can_withdraw,
    hasActiveCourse: !!r.has_active_course,
  };
}

/** The student's own ledger. RLS restricts this to their rows; there is no
 *  write path from the browser at all — every line is written by a
 *  service-role function behind a verified payment. */
export async function myWalletTransactions({ limit = 50 } = {}) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_WALLET_TX;
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("wallet_transactions")
    .select("id, amount_paise, type, status, note, created_at")
    .order("created_at", { ascending: false })
    .limit(limit);
  if (error) throw error;
  return (data ?? []).map((t) => ({
    id: t.id,
    amount: (t.amount_paise ?? 0) / 100,
    type: t.type,
    status: t.status,
    note: t.note || "",
    at: t.created_at,
  }));
}


/* ------------------------------------------------------------ newsletter -- */

/**
 * Footer newsletter signup. Open to signed-out visitors on purpose — that is
 * the whole point of a footer form. The table grants INSERT only: the list
 * cannot be read back with the anon key, or the form would double as an
 * email-harvesting endpoint.
 */
export async function subscribeEmail(email, source = "footer") {
  const clean = String(email || "").trim().toLowerCase();
  if (!/^[^@\s]+@[^@\s]+\.[a-z]{2,}$/i.test(clean)) return { ok: false, reason: "invalid" };
  const sb = await getSupabase();
  const { error } = await sb.from("subscribers").insert({ email: clean, source });
  if (error) {
    // 23505 is the unique index on lower(email): already on the list, which is
    // a success from the reader's point of view, not an error to show them.
    if (error.code === "23505") return { ok: true, reason: "already" };
    console.error("subscribe failed", error);
    return { ok: false, reason: "failed" };
  }
  return { ok: true, reason: "added" };
}

/* -------------------------------------------------------------- feedback -- */

/**
 * A student's own report. The row is written with their own id — RLS refuses
 * an insert claiming to be anyone else — and cannot be edited afterwards, so
 * the admin queue stays trustworthy.
 *
 * name and email are snapshotted rather than joined: the report should stay
 * readable if the account is later deleted.
 */
export async function submitFeedback({ kind, rating, message, page, testId }) {
  const sb = await getSupabase();
  const { data: { user } } = await sb.auth.getUser();
  if (!user) throw new Error("not_signed_in");

  const profile = await getProfile(user.id).catch(() => null);
  const { error } = await sb.from("feedback").insert({
    student_id: user.id,
    name: profile?.full_name || null,
    email: profile?.email || user.email || null,
    kind: kind || "general",
    rating: rating || null,
    message: String(message || "").trim(),
    page: page || null,
    test_id: testId || null,
  });
  if (error) throw error;
  return true;
}

/** What this student has sent, and anything an admin wrote back. */
export async function myFeedback() {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_MY_FEEDBACK;
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("feedback")
    .select("id, kind, rating, message, status, admin_note, created_at")
    .order("created_at", { ascending: false })
    .limit(50);
  if (error) throw error;
  return (data ?? []).map((f) => ({
    id: f.id, kind: f.kind, rating: f.rating, message: f.message,
    status: f.status, reply: f.admin_note || "", at: f.created_at,
  }));
}

export async function adminFeedback() {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_ADMIN_FEEDBACK;
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("feedback")
    .select("id, name, email, kind, rating, message, page, status, admin_note, created_at")
    .order("created_at", { ascending: false })
    .limit(500);
  if (error) throw error;
  return (data ?? []).map((f) => ({
    id: f.id,
    name: f.name || "Aspirant",
    email: f.email || "—",
    kind: f.kind, rating: f.rating, message: f.message,
    page: f.page || "", status: f.status, reply: f.admin_note || "",
    at: f.created_at,
  }));
}

/** Admin-only: RLS refuses this for anyone else. */
export async function updateFeedback(id, patch) {
  const sb = await getSupabase();
  const { error } = await sb.from("feedback")
    .update({ status: patch.status, admin_note: patch.reply ?? null })
    .eq("id", id);
  if (error) throw error;
  return true;
}

/* ----------------------------------------------------------- admin views -- */

export async function adminStudents() {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_STUDENTS;
  const sb = await getSupabase();
  const { data: profiles, error } = await sb
    .from("profiles")
    .select("id, full_name, email, phone, created_at, target_exam, is_tester")
    .eq("role", "student")
    .order("created_at", { ascending: false })
    .limit(500);
  if (error) throw error;

  const ids = (profiles ?? []).map((p) => p.id);
  if (ids.length === 0) return [];

  const [{ data: attempts }, { data: enrolls }] = await Promise.all([
    sb.from("attempts").select("student_id, score, max_score").in("student_id", ids).eq("status", "submitted"),
    sb.from("enrollments").select("student_id, status, expires_at, plan_code").in("student_id", ids),
  ]);

  const stats = new Map();
  (attempts ?? []).forEach((a) => {
    const cur = stats.get(a.student_id) || { n: 0, sum: 0 };
    cur.n += 1;
    cur.sum += a.max_score > 0 ? (a.score / a.max_score) * 100 : 0;
    stats.set(a.student_id, cur);
  });

  const active = new Set(
    (enrolls ?? [])
      .filter((e) => e.status === "active" && (!e.expires_at || new Date(e.expires_at) > new Date()))
      .map((e) => e.student_id),
  );

  return (profiles ?? []).map((p) => {
    const s = stats.get(p.id);
    return {
      id: p.id,
      name: p.full_name || "Aspirant",
      email: p.email || "—",
      phone: p.phone || "",
      joined: p.created_at,
      target: p.target_exam || "—",
      attempts: s?.n ?? 0,
      avg: s && s.n ? Math.round(s.sum / s.n) : 0,
      enrolled: active.has(p.id),
      tester: !!p.is_tester,
    };
  });
}

export async function adminPayments() {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_PAYMENTS;
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("payments")
    .select("id, amount, currency, status, plan_code, razorpay_payment_id, method, created_at, verified_at, user_id")
    .order("created_at", { ascending: false })
    .limit(500);
  if (error) throw error;
  const rows = data ?? [];

  // `payments.user_id` and `profiles.id` both reference auth.users, so there is
  // no foreign key between them for PostgREST to embed across. Look the buyers
  // up in one extra query instead.
  const ids = [...new Set(rows.map((p) => p.user_id).filter(Boolean))];
  const byId = new Map();
  if (ids.length > 0) {
    const { data: profs } = await sb.from("profiles").select("id, full_name, email").in("id", ids);
    (profs ?? []).forEach((pr) => byId.set(pr.id, pr));
  }

  return rows.map((p) => {
    const buyer = byId.get(p.user_id);
    return {
      id: p.id,
      name: buyer?.full_name || "—",
      email: buyer?.email || "—",
      item: p.plan_code || "—",
      amount: Number(p.amount || 0),
      status: p.status,
      method: p.method || "—",
      ref: p.razorpay_payment_id || "—",
      date: p.created_at,
    };
  });
}

export async function adminReferrals() {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_ADMIN_REFERRALS;
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("referrals")
    .select("id, referrer_id, referred_id, referral_code_used, bonus_status, created_at")
    .order("created_at", { ascending: false })
    .limit(500);
  if (error) throw error;
  const rows = data ?? [];
  if (rows.length === 0) return [];

  // `referrals` has two foreign keys into `profiles`, so a PostgREST embed
  // would need disambiguating hints on both. One lookup query is clearer and
  // cannot break when a constraint is renamed.
  const ids = [...new Set(rows.flatMap((r) => [r.referrer_id, r.referred_id]).filter(Boolean))];
  const byId = new Map();
  const { data: profs } = await sb.from("profiles").select("id, full_name, email").in("id", ids);
  (profs ?? []).forEach((p) => byId.set(p.id, p));

  // Which invitees actually paid — that is the only referral that will ever
  // cost money, so it is the column an admin scans.
  //
  // Deliberately NOT filtered on expires_at. "Did this referral convert?" is a
  // question about a purchase that happened, not about access that is still
  // running; a student whose six months lapsed still earned their referrer a
  // bonus. my_referral_stats() counts it the same way, so the student's card
  // and this table can never disagree.
  const referredIds = rows.map((r) => r.referred_id);
  const { data: enrolls } = await sb
    .from("enrollments")
    .select("student_id, status")
    .in("student_id", referredIds);
  const paid = new Set(
    (enrolls ?? []).filter((e) => e.status === "active").map((e) => e.student_id),
  );

  return rows.map((r) => {
    const from = byId.get(r.referrer_id);
    const to = byId.get(r.referred_id);
    return {
      id: r.id,
      referrer: from?.full_name || "—",
      referrerEmail: from?.email || "—",
      referred: to?.full_name || "—",
      referredEmail: to?.email || "—",
      code: r.referral_code_used,
      paid: paid.has(r.referred_id),
      status: r.bonus_status,
      at: r.created_at,
    };
  });
}

/* ------------------------------------------------------------ mains -- */
/* Mains, slice 1 (migration 0028): essay themes and PYQs, toppers, their
 * copies and the answers inside them.
 *
 * Themes and PYQs are public. Everything about copies needs a session. A copy
 * is a LINK (a publisher's public PDF, opened at the page in a new tab), or
 * HOSTED (pages rendered to WebP in the private copy-pages bucket), or both.
 * Hosted pages come back as ten-minute signed URLs, which storage only signs
 * when can_read_topper_copy() passes -- so the lock on a hosted copy is real,
 * not a button the browser could skip. */

const COPY_PAGES = "copy-pages";
const COPY_PDFS = "copy-pdfs";
export const COPY_URL_TTL = 600;

export { essayKey, copyLinkAt };

/* Long `in.(...)` lists overflow the request URL, so lookups go in chunks.
 * URLs are long, uuids short: the caller picks the size. */
async function selectIn(sb, table, cols, col, values, size = 150) {
  const out = [];
  for (let i = 0; i < values.length; i += size) {
    const { data, error } = await sb.from(table).select(cols).in(col, values.slice(i, i + size));
    if (error) throw error;
    out.push(...(data ?? []));
  }
  return out;
}

async function inBatches(rows, size, fn) {
  for (let i = 0; i < rows.length; i += size) await fn(rows.slice(i, i + size), i);
}

function themeFromRow(r) {
  return { id: r.id, slug: r.slug, name: r.name, nameHi: r.name_hi || "", parentId: r.parent_id || null, sortOrder: r.sort_order ?? 0 };
}

export async function essayThemes() {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_ESSAY_THEMES;
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("essay_themes")
    .select("id, slug, name, name_hi, parent_id, sort_order")
    .order("sort_order")
    .order("name");
  if (error) throw error;
  return (data ?? []).map(themeFromRow);
}

/**
 * Every essay PYQ, newest first, with its themes (highest confidence first --
 * the first is the main theme, the rest are "also under") and how many
 * published topper essays answer it.
 */
export async function essayPyqs({ includeDrafts = false } = {}) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_ESSAY_PYQS;
  const sb = await getSupabase();
  let q = sb
    .from("essay_pyqs")
    .select("id, year, q_no, section, topic, topic_hi, is_published, essay_pyq_themes(theme_id, confidence)")
    .order("year", { ascending: false })
    .order("q_no", { ascending: true, nullsFirst: false })
    .order("topic");
  if (!includeDrafts) q = q.eq("is_published", true);
  const [{ data, error }, { data: stats }] = await Promise.all([
    q,
    // The counts read copies, which need a session; a visitor just gets none.
    sb.from("essay_pyq_stats_v").select("pyq_id, essay_count, exact_count"),
  ]);
  if (error) throw error;
  const n = new Map((stats ?? []).map((s) => [s.pyq_id, s]));
  return (data ?? []).map((r) => ({
    id: r.id,
    year: r.year,
    qNo: r.q_no ?? null,
    section: r.section || "",
    topic: r.topic,
    topicHi: r.topic_hi || "",
    isPublished: r.is_published !== false,
    themes: (r.essay_pyq_themes ?? [])
      .slice()
      .sort((a, b) => (b.confidence ?? 0) - (a.confidence ?? 0))
      .map((x) => ({ id: x.theme_id, confidence: x.confidence ?? null })),
    essayCount: Number(n.get(r.id)?.essay_count ?? 0),
    exactCount: Number(n.get(r.id)?.exact_count ?? 0),
  }));
}

/** Codes of the live bundles that include Mains. Readable without an
 *  account, so the public site can say which bundle brings the copies. */
export async function mainsBundleCodes() {
  if (import.meta.env.DEV && FIXTURES_ON()) return [];
  const sb = await getSupabase();
  const { data, error } = await sb.from("plans").select("code").eq("includes_mains", true).eq("is_active", true);
  if (error) throw error;
  return (data ?? []).map((r) => r.code);
}

/**
 * What sits behind the Essay section, counted for a visitor (0032): topper
 * essays and toppers, essays per PYQ, the PYQs with a guide, wiki entries by
 * kind, the free part of one guide and one Editor's pick. Null when the
 * function is not there yet, so the public page simply shows less.
 */
export async function essayCatalog() {
  if (import.meta.env.DEV && FIXTURES_ON()) return null;
  const sb = await getSupabase();
  const { data, error } = await sb.rpc("essay_catalog");
  if (error) { console.warn("essay catalogue unavailable", error.message); return null; }
  if (!data) return null;
  const sample = data.guide_sample;
  return {
    essays: Number(data.essays) || 0,
    words: Number(data.words) || 0,
    arguments: Number(data.arguments) || 0,
    openings: Number(data.openings) || 0,
    toppers: Number(data.toppers) || 0,
    topMarks: data.top_marks == null ? null : Number(data.top_marks),
    perPyq: new Map(Object.entries(data.per_pyq || {}).map(([k, v]) => [k, Number(v) || 0])),
    guides: new Set(data.guides || []),
    kinds: data.kinds || {},
    guideSample: sample ? {
      pyqId: sample.pyq_id, topic: sample.topic, year: sample.year, spine: sample.spine || "",
      sides: Array.isArray(sample.sides) ? sample.sides : [],
      titles: Array.isArray(sample.titles) ? sample.titles : [],
    } : null,
    pick: data.pick?.body ? { body: data.pick.body, attribution: data.pick.attribution || "" } : null,
  };
}

const LIB_COLS_BASE =
  "answer_id, paper, paper_label, question, start_page, end_page, copy_id, source, title, written_year, " +
  "source_url, page_count, pages_ready, is_free, is_published, topper_id, topper_name, topper_rank, cse_year, essay_marks";

// body_words arrives with migration 0029. Asking for a column that does not
// exist yet fails the whole query, so a build that goes out before the
// migration drops the word count (once) rather than the Essay section.
let libHasWords = true;
const libCols = () => (libHasWords ? `${LIB_COLS_BASE}, body_words` : LIB_COLS_BASE);
const isMissingWords = (error) => libHasWords && /body_words/.test(String(error?.message || ""));
async function withLibCols(run) {
  try {
    return await run(libCols());
  } catch (e) {
    if (!isMissingWords(e)) throw e;
    libHasWords = false;
    return run(libCols());
  }
}

export function libraryEntryFromRow(r) {
  return {
    answerId: r.answer_id,
    paper: r.paper,
    paperLabel: r.paper_label || "",
    question: r.question,
    startPage: r.start_page ?? null,
    endPage: r.end_page ?? null,
    copyId: r.copy_id,
    source: r.source || "",
    title: r.title || "",
    writtenYear: r.written_year ?? null,
    sourceUrl: r.source_url || "",
    pageCount: r.page_count ?? 0,
    hosted: r.pages_ready === true,
    isFree: r.is_free === true,
    isPublished: r.is_published !== false,
    words: r.body_words ?? null,   // set when the essay has its text
    topper: {
      id: r.topper_id,
      name: r.topper_name,
      rank: r.topper_rank ?? null,
      cseYear: r.cse_year ?? null,
      essayMarks: r.essay_marks ?? null,
    },
  };
}

/** Ids of the published essays whose text contains these words (websearch
 *  syntax), best match first. Empty when nothing matches, the query is only
 *  stop words, or the search does not exist yet (before migration 0029). */
export async function searchEssayIds(q, limit = 100) {
  const needle = String(q || "").trim();
  if (!needle) return [];
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxSearchEssayIds(needle);
  const sb = await getSupabase();
  const { data, error } = await sb.rpc("search_topper_essays", { p_q: needle, p_limit: limit });
  if (error) {
    console.warn("essay text search unavailable", error.message);
    return [];
  }
  return (data ?? []).map((r) => r.answer_id);
}

/** One page of the topper-answer library for a paper. `q` matches the
 *  question, the topper's name, or any word in the essay's text. */
export async function topperLibrary({ paper = "essay", sort = "marks", year = null, q = "", offset = 0, limit = 24 } = {}) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxLibrary({ paper, sort, year, q, offset, limit });
  const sb = await getSupabase();
  // Commas and brackets are PostgREST's own syntax inside or(); a stray one
  // would break the filter rather than match nothing.
  const needle = String(q || "").replace(/[%,()*\\]/g, " ").trim();
  // Text matches ride along as ids. 100 keeps the request line well short of
  // proxy limits; the search ranks, so these are the best hundred.
  const textIds = needle && paper === "essay" ? await searchEssayIds(q, 100) : [];
  const { data, count } = await withLibCols(async (cols) => {
    let query = sb.from("topper_library_v").select(cols, { count: "exact" })
      .eq("paper", paper)
      .eq("is_published", true);
    if (year) query = query.eq("written_year", year);
    if (needle) {
      const ors = [`question.ilike.%${needle}%`, `topper_name.ilike.%${needle}%`];
      if (textIds.length) ors.push(`answer_id.in.(${textIds.join(",")})`);
      query = query.or(ors.join(","));
    }
    if (sort === "marks") query = query.order("essay_marks", { ascending: false, nullsFirst: false });
    // Most essays have no marks and no year yet; without a readable tie-break
    // they came out in answer_id (random uuid) order. answer_id stays last so
    // paging stays stable.
    query = query
      .order("written_year", { ascending: sort === "oldest", nullsFirst: false })
      .order("topper_name")
      .order("question")
      .order("answer_id");
    const res = await query.range(offset, offset + limit - 1);
    if (res.error) throw res.error;
    return res;
  });
  return { items: (data ?? []).map(libraryEntryFromRow), total: count ?? 0 };
}

/** An essay's text, or null when it has none -- or when the reader may not
 *  open this copy (the text sits behind the copy's own lock). */
export async function essayText(answerId) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxEssayText(answerId);
  const sb = await getSupabase();
  const { data, error } = await sb.from("topper_answer_texts")
    .select("body, source, updated_at").eq("answer_id", answerId).maybeSingle();
  if (error) throw error;
  return data ? { body: data.body, source: data.source || "", updatedAt: data.updated_at } : null;
}

/** The years that actually have answers, for the year filter. */
export async function topperLibraryYears(paper = "essay") {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxLibraryYears(paper);
  const sb = await getSupabase();
  const { data, error } = await sb.from("topper_library_v").select("written_year")
    .eq("paper", paper).eq("is_published", true).not("written_year", "is", null).limit(1000);
  if (error) throw error;
  return [...new Set((data ?? []).map((r) => r.written_year))].sort((a, b) => b - a);
}

/**
 * A PYQ's topper essays, grouped the way a student reads them: the same
 * question first, then each related topic, each group best score first.
 */
export async function essaysForPyq(pyqId) {
  if (import.meta.env.DEV && FIXTURES_ON()) return groupEssays(fx().fxEssaysForPyq(pyqId));
  const sb = await getSupabase();
  const { data: links, error } = await sb
    .from("essay_answer_pyqs").select("answer_id, kind, confidence").eq("pyq_id", pyqId);
  if (error) throw error;
  if (!links?.length) return [];
  const meta = new Map(links.map((l) => [l.answer_id, l]));
  const rows = (await withLibCols((cols) => selectIn(sb, "topper_library_v", cols, "answer_id", [...meta.keys()])))
    .filter((r) => r.is_published !== false);
  return groupEssays(rows.map((r) => ({
    ...libraryEntryFromRow(r),
    kind: meta.get(r.answer_id)?.kind || "related",
    confidence: meta.get(r.answer_id)?.confidence ?? null,
  })));
}

export function groupEssays(entries) {
  const groups = new Map();
  for (const e of entries) {
    const key = essayKey(e.question) || e.answerId;
    if (!groups.has(key)) groups.set(key, { key, question: e.question, kind: e.kind, confidence: e.confidence ?? null, entries: [] });
    const g = groups.get(key);
    if (e.kind === "exact") g.kind = "exact";
    if ((e.confidence ?? -1) > (g.confidence ?? -1)) g.confidence = e.confidence;
    g.entries.push(e);
  }
  const byScore = (a, b) =>
    (b.topper.essayMarks ?? -1) - (a.topper.essayMarks ?? -1)
    || (a.topper.rank ?? 1e6) - (b.topper.rank ?? 1e6)
    || (b.writtenYear ?? 0) - (a.writtenYear ?? 0);
  const list = [...groups.values()];
  list.forEach((g) => g.entries.sort(byScore));
  return list.sort((a, b) =>
    (a.kind === "exact" ? 0 : 1) - (b.kind === "exact" ? 0 : 1)
    || (b.confidence ?? 0) - (a.confidence ?? 0)
    || b.entries.length - a.entries.length);
}

/** Does this student hold Mains? Failing closed: an error means "locked",
 *  and free copies still open. */
export async function mainsAccess() {
  if (import.meta.env.DEV && FIXTURES_ON()) return true;
  const sb = await getSupabase();
  const { data, error } = await sb.rpc("has_mains_access");
  if (error) { console.error("mains access check failed", error); return false; }
  return data === true;
}

/**
 * Signed URLs for some pages of one hosted copy, as { page: url }. A page the
 * caller may not read simply comes back missing.
 */
export async function copyPageUrls(copyId, pages) {
  if (import.meta.env.DEV && FIXTURES_ON()) {
    return Object.fromEntries(pages.map((p) => [p, fx().fxPageImage(copyId, p)]));
  }
  const sb = await getSupabase();
  const paths = pages.map((p) => `${copyId}/p${p}.webp`);
  const { data, error } = await sb.storage.from(COPY_PAGES).createSignedUrls(paths, COPY_URL_TTL);
  if (error) throw error;
  const out = {};
  (data ?? []).forEach((d, i) => { if (d && !d.error && d.signedUrl) out[pages[i]] = d.signedUrl; });
  return out;
}

/* ------------------------------------------------- mains: study tools -- */
/* Migration 0030. A student's own stars, "done" marks, notes and reading log
 * (row-level security keeps each to its owner), the Essay Wiki (verbatim
 * passages behind the copy's lock) and Learn to Write (behind Mains, with a
 * preview for everyone signed in). Before 0030 is applied every read here
 * comes back empty instead of failing the Essay section. */

const missingTable = (error) => /does not exist|schema cache|Could not find/i.test(String(error?.message || ""));
const IST_DAY = () => new Date(Date.now() + 5.5 * 3600e3).toISOString().slice(0, 10);

/** Every star and "done" this student has, as { pyq, answer, snippet } maps of
 *  item id → { starred, done, doneAt }. */
export async function essayMyMarks() {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxEssayMarks();
  const sb = await getSupabase();
  const empty = { pyq: new Map(), answer: new Map(), snippet: new Map() };
  const { data, error } = await sb.from("essay_marks").select("kind, item_id, starred, done, done_at").limit(5000);
  if (error) { if (missingTable(error)) return empty; throw error; }
  for (const r of data ?? []) empty[r.kind]?.set(r.item_id, { starred: r.starred, done: r.done, doneAt: r.done_at });
  return empty;
}

/** Star or mark done. A row with neither is removed. */
export async function setEssayMark(kind, itemId, { starred, done }) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxSetEssayMark(kind, itemId, { starred, done });
  const sb = await getSupabase();
  if (!starred && !done) {
    const { error } = await sb.from("essay_marks").delete().eq("kind", kind).eq("item_id", itemId);
    if (error) throw error;
    return null;
  }
  const { data, error } = await sb.from("essay_marks")
    .upsert({ kind, item_id: itemId, starred: !!starred, done: !!done }, { onConflict: "user_id,kind,item_id" })
    .select("starred, done, done_at").single();
  if (error) throw error;
  return { starred: data.starred, done: data.done, doneAt: data.done_at };
}

function noteFromRow(r) {
  return { id: r.id, kind: r.kind, itemId: r.item_id ?? null, label: r.label || "", body: r.body, createdAt: r.created_at, updatedAt: r.updated_at };
}

/** This student's notes, newest first. */
export async function essayNotes() {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxEssayNotes();
  const sb = await getSupabase();
  const { data, error } = await sb.from("essay_notes")
    .select("id, kind, item_id, label, body, created_at, updated_at")
    .order("updated_at", { ascending: false }).limit(1000);
  if (error) { if (missingTable(error)) return []; throw error; }
  return (data ?? []).map(noteFromRow);
}

/** Add a note (no id) or change one. */
export async function saveEssayNote({ id, kind, itemId = null, label = "", body }) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxSaveEssayNote({ id, kind, itemId, label, body });
  const sb = await getSupabase();
  const text = String(body || "").trim();
  const q = id
    ? sb.from("essay_notes").update({ body: text }).eq("id", id)
    : sb.from("essay_notes").insert({ kind, item_id: kind === "free" ? null : itemId, label: String(label || "").slice(0, 300) || null, body: text });
  const { data, error } = await q.select("id, kind, item_id, label, body, created_at, updated_at").single();
  if (error) throw error;
  return noteFromRow(data);
}

export async function deleteEssayNote(id) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxDeleteEssayNote(id);
  const sb = await getSupabase();
  const { error } = await sb.from("essay_notes").delete().eq("id", id);
  if (error) throw error;
}

/** Count today's reading of an essay (once a day per essay). Never throws:
 *  a missed log must not break the reader. */
export async function logEssayRead(answerId) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxLogEssayRead(answerId);
  try {
    const sb = await getSupabase();
    const { error } = await sb.from("essay_reads").insert({ answer_id: answerId });
    if (error && error.code !== "23505" && !missingTable(error)) console.warn("essay read not logged", error.message);
  } catch (e) { console.warn("essay read not logged", e); }
}

/** The days (India time, YYYY-MM-DD) this student read an essay or finished a
 *  PYQ, for the streak. */
export async function essayActivityDays(days = 120) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxEssayActivityDays();
  const sb = await getSupabase();
  const since = new Date(Date.now() - days * 864e5).toISOString().slice(0, 10);
  const [reads, marks] = await Promise.all([
    sb.from("essay_reads").select("read_on").gte("read_on", since).limit(5000),
    sb.from("essay_marks").select("done_at").eq("done", true).gte("done_at", since).limit(5000),
  ]);
  if (reads.error && !missingTable(reads.error)) throw reads.error;
  const out = new Set((reads.data ?? []).map((r) => r.read_on));
  (marks.data ?? []).forEach((m) => { if (m.done_at) out.add(new Date(new Date(m.done_at).getTime() + 5.5 * 3600e3).toISOString().slice(0, 10)); });
  return [...out].sort();
}

/** Days in a row, ending today or yesterday, with any essay activity. */
export function essayStreak(days, today = IST_DAY()) {
  const set = new Set(days);
  const step = (d) => new Date(Date.parse(`${d}T00:00:00Z`) - 864e5).toISOString().slice(0, 10);
  let d = set.has(today) ? today : step(today);
  let n = 0;
  while (set.has(d)) { n += 1; d = step(d); }
  return n;
}

/** How many students have read each essay: Map answerId → count. */
export async function essayReaderCounts(ids) {
  if (!ids?.length) return new Map();
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxEssayReaderCounts(ids);
  const sb = await getSupabase();
  const { data, error } = await sb.rpc("essay_reader_counts", { p_ids: ids.slice(0, 300) });
  if (error) { console.warn("reader counts unavailable", error.message); return new Map(); }
  return new Map((data ?? []).map((r) => [r.answer_id, r.readers]));
}

/** Ids of the PYQs that have a published Learn to Write guide. */
export async function essayLtwReady() {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxLtwReady();
  const sb = await getSupabase();
  const { data, error } = await sb.rpc("essay_ltw_ready");
  if (error) { if (!missingTable(error)) console.warn("ltw list unavailable", error.message); return new Set(); }
  return new Set((data ?? []).map((r) => (typeof r === "string" ? r : r.essay_ltw_ready)));
}

/** A PYQ's guide: { doc } when this student may read it, { preview } when it
 *  is locked, or null when there is none. */
export async function essayLtw(pyqId) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxLtw(pyqId);
  const sb = await getSupabase();
  const { data, error } = await sb.from("essay_ltw").select("doc, status, updated_at").eq("pyq_id", pyqId).maybeSingle();
  if (error && !missingTable(error)) throw error;
  if (data?.doc) return { doc: data.doc, status: data.status, updatedAt: data.updated_at };
  const { data: preview, error: e2 } = await sb.rpc("essay_ltw_preview", { p_pyq: pyqId });
  if (e2) { if (!missingTable(e2)) console.warn("ltw preview unavailable", e2.message); return null; }
  return preview ? { preview } : null;
}

function snippetFromRow(s, fit = null) {
  return {
    id: s.id, answerId: s.answer_id, kind: s.kind, body: s.body, attribution: s.attribution || "",
    why: s.why || "", page: s.page ?? null, status: s.status,
    use: fit?.use_note || "", fitPyqId: fit?.pyq_id || null,
  };
}

/** Published wiki snippets per theme and kind: [{ themeId, kind, n }]. */
export async function essayWikiCounts() {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxWikiCounts();
  const sb = await getSupabase();
  const { data, error } = await sb.rpc("essay_wiki_counts");
  if (error) { if (!missingTable(error)) console.warn("wiki counts unavailable", error.message); return []; }
  return (data ?? []).map((r) => ({ themeId: r.theme_id, kind: r.kind, n: r.n }));
}

/** The snippets that fit any of these PYQs, each once, with the essay it came
 *  from and every fit among these PYQs. Locked ones are simply absent. */
export async function essaySnippetsForPyqs(pyqIds) {
  if (!pyqIds?.length) return [];
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxSnippetsForPyqs(pyqIds);
  const sb = await getSupabase();
  const fits = await selectIn(sb, "essay_snippet_fits",
    "snippet_id, pyq_id, use_note, rank, essay_snippets!inner(id, answer_id, kind, body, attribution, why, page, status)",
    "pyq_id", pyqIds, 100).catch((e) => { if (missingTable(e)) return []; throw e; });
  const byId = new Map();
  for (const f of fits) {
    const s = f.essay_snippets;
    if (!s || s.status !== "published") continue;
    if (!byId.has(s.id)) byId.set(s.id, { ...snippetFromRow(s), fits: [] });
    byId.get(s.id).fits.push({ pyqId: f.pyq_id, use: f.use_note, rank: f.rank ?? 1 });
  }
  const list = [...byId.values()];
  const answers = [...new Set(list.map((s) => s.answerId).filter(Boolean))];
  const rows = answers.length ? await withLibCols((cols) => selectIn(sb, "topper_library_v", cols, "answer_id", answers)) : [];
  const entry = new Map(rows.map((r) => [r.answer_id, libraryEntryFromRow(r)]));
  // Editor's picks have no essay (answerId null); topper snippets need theirs.
  return list.map((s) => ({ ...s, entry: entry.get(s.answerId) || null })).filter((s) => s.entry || !s.answerId);
}

/** Library entries for these essays (e.g. a student's starred ones). */
export async function libraryEntries(ids) {
  if (!ids?.length) return [];
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxLibraryEntries(ids);
  const sb = await getSupabase();
  const rows = await withLibCols((cols) => selectIn(sb, "topper_library_v", cols, "answer_id", ids));
  return rows.filter((r) => r.is_published !== false).map(libraryEntryFromRow);
}

/** These snippets with their essays (e.g. a student's starred ones). */
export async function snippetsByIds(ids) {
  if (!ids?.length) return [];
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxSnippetsByIds(ids);
  const sb = await getSupabase();
  const rows = await selectIn(sb, "essay_snippets",
    "id, answer_id, kind, body, attribution, why, page, status, essay_snippet_fits(pyq_id, use_note, rank)", "id", ids)
    .catch((e) => { if (missingTable(e)) return []; throw e; });
  const list = rows.filter((s) => s.status === "published").map((s) => ({
    ...snippetFromRow(s),
    fits: (s.essay_snippet_fits ?? []).map((f) => ({ pyqId: f.pyq_id, use: f.use_note, rank: f.rank ?? 1 })).sort((a, b) => a.rank - b.rank),
  }));
  const entries = new Map((await libraryEntries([...new Set(list.map((s) => s.answerId).filter(Boolean))])).map((e) => [e.answerId, e]));
  return list.map((s) => ({ ...s, entry: entries.get(s.answerId) || null })).filter((s) => s.entry || !s.answerId);
}

/* ------------------------------------------------------ admin: mains -- */

export function slugify(s) {
  return String(s || "").toLowerCase().normalize("NFKD").replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 80) || "theme";
}

export async function upsertEssayTheme(th) {
  const sb = await getSupabase();
  const row = {
    ...(th.id ? { id: th.id } : {}),
    slug: th.slug || slugify(th.name),
    name: th.name.trim(),
    name_hi: (th.nameHi || "").trim() || null,
    parent_id: th.parentId || null,
    sort_order: Number(th.sortOrder || 0),
  };
  const { data, error } = await sb.from("essay_themes").upsert(row).select().single();
  if (error) throw error;
  return themeFromRow(data);
}

export async function deleteEssayTheme(id) {
  const sb = await getSupabase();
  const { error } = await sb.from("essay_themes").delete().eq("id", id);
  if (error) throw error;
}

/** Save one PYQ and, when `themes` is given, replace its themes. */
export async function upsertEssayPyq(p) {
  const sb = await getSupabase();
  const row = {
    ...(p.id ? { id: p.id } : {}),
    year: Number(p.year),
    q_no: p.qNo === "" || p.qNo == null ? null : Number(p.qNo),
    section: (p.section || "").trim() || null,
    topic: p.topic.trim(),
    topic_hi: (p.topicHi || "").trim() || null,
    is_published: p.isPublished !== false,
    updated_at: new Date().toISOString(),
  };
  const { data, error } = await sb.from("essay_pyqs").upsert(row).select("id").single();
  if (error) throw error;
  if (Array.isArray(p.themes)) {
    const { error: e1 } = await sb.from("essay_pyq_themes").delete().eq("pyq_id", data.id);
    if (e1) throw e1;
    const links = p.themes.filter((x) => x.id).map((x) => ({ pyq_id: data.id, theme_id: x.id, confidence: x.confidence ?? null }));
    if (links.length) {
      const { error: e2 } = await sb.from("essay_pyq_themes").insert(links);
      if (e2) throw e2;
    }
  }
  return data.id;
}

export async function deleteEssayPyq(id) {
  const sb = await getSupabase();
  const { error } = await sb.from("essay_pyqs").delete().eq("id", id);
  if (error) throw error;
}

/** Copies for the admin list, newest first, with topper and answer count. */
export async function adminCopies({ q = "", paper = "", offset = 0, limit = 40 } = {}) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxAdminCopies({ q, paper, offset, limit });
  const sb = await getSupabase();
  const needle = String(q || "").replace(/[%,()*\\]/g, " ").trim();
  const topperEmbed = needle ? "toppers!inner(id, name, rank, cse_year, essay_marks)" : "toppers(id, name, rank, cse_year, essay_marks)";
  const answersEmbed = paper ? "topper_answers!inner(paper)" : "topper_answers(count)";
  let query = sb.from("topper_copies")
    .select(`id, source, title, written_year, source_url, page_count, pages_ready, is_free, is_published, created_at, ${topperEmbed}, ${answersEmbed}`, { count: "exact" })
    .order("created_at", { ascending: false });
  if (needle) query = query.ilike("toppers.name", `%${needle}%`);
  if (paper) query = query.eq("topper_answers.paper", paper);
  const { data, error, count } = await query.range(offset, offset + limit - 1);
  if (error) throw error;
  return {
    total: count ?? 0,
    items: (data ?? []).map((r) => ({
      id: r.id,
      source: r.source || "",
      title: r.title || "",
      writtenYear: r.written_year ?? null,
      sourceUrl: r.source_url || "",
      pageCount: r.page_count ?? 0,
      hosted: r.pages_ready === true,
      isFree: r.is_free === true,
      isPublished: r.is_published !== false,
      topper: {
        id: r.toppers?.id,
        name: r.toppers?.name || "—",
        rank: r.toppers?.rank ?? null,
        cseYear: r.toppers?.cse_year ?? null,
        essayMarks: r.toppers?.essay_marks ?? null,
      },
      answerCount: paper ? (r.topper_answers ?? []).length : Number(r.topper_answers?.[0]?.count ?? 0),
    })),
  };
}

/** One copy, in the same shape as an adminCopies() row. */
export async function adminCopy(id) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxAdminCopies({}).items.find((c) => c.id === id) || null;
  const sb = await getSupabase();
  const { data, error } = await sb.from("topper_copies")
    .select("id, source, title, written_year, source_url, page_count, pages_ready, is_free, is_published, toppers(id, name, rank, cse_year, essay_marks), topper_answers(count)")
    .eq("id", id)
    .maybeSingle();
  if (error) throw error;
  if (!data) return null;
  return {
    id: data.id,
    source: data.source || "",
    title: data.title || "",
    writtenYear: data.written_year ?? null,
    sourceUrl: data.source_url || "",
    pageCount: data.page_count ?? 0,
    hosted: data.pages_ready === true,
    isFree: data.is_free === true,
    isPublished: data.is_published !== false,
    topper: {
      id: data.toppers?.id,
      name: data.toppers?.name || "—",
      rank: data.toppers?.rank ?? null,
      cseYear: data.toppers?.cse_year ?? null,
      essayMarks: data.toppers?.essay_marks ?? null,
    },
    answerCount: Number(data.topper_answers?.[0]?.count ?? 0),
  };
}

/** Find a topper by name (the same essay_key() rule), or create one. */
export async function findOrCreateTopper({ name, rank = null, cseYear = null, essayMarks = null, note = null }) {
  const sb = await getSupabase();
  const key = essayKey(name);
  if (!key) throw new Error("A topper needs a name.");
  const { data: hit } = await sb.from("toppers").select("id").eq("name_key", key).maybeSingle();
  if (hit) return hit.id;
  const { data, error } = await sb.from("toppers")
    .insert({ name: name.trim(), rank, cse_year: cseYear, essay_marks: essayMarks, note })
    .select("id").single();
  if (error) throw error;
  return data.id;
}

export async function updateTopper(id, patch) {
  const sb = await getSupabase();
  const num = (v) => (v === "" || v == null ? null : Number(v));
  const row = {};
  if (patch.name !== undefined) row.name = patch.name.trim();
  if (patch.rank !== undefined) row.rank = num(patch.rank);
  if (patch.cseYear !== undefined) row.cse_year = num(patch.cseYear);
  if (patch.essayMarks !== undefined) row.essay_marks = num(patch.essayMarks);
  const { error } = await sb.from("toppers").update(row).eq("id", id);
  if (error) throw error;
}

export async function createCopy(c) {
  const sb = await getSupabase();
  const { data: { user } } = await sb.auth.getUser();
  const { data, error } = await sb.from("topper_copies").insert({
    topper_id: c.topperId,
    source: c.source || null,
    title: c.title || null,
    written_year: c.writtenYear ? Number(c.writtenYear) : null,
    source_url: c.sourceUrl ? copyLinkAt(c.sourceUrl) : null,
    sha256: c.sha256 || null,
    is_free: c.isFree === true,
    is_published: c.isPublished !== false,
    created_by: user?.id ?? null,
  }).select("id").single();
  if (error) throw error;
  return data.id;
}

export async function updateCopy(id, patch) {
  const sb = await getSupabase();
  const map = {
    source: "source", title: "title", writtenYear: "written_year", sourceUrl: "source_url", pageCount: "page_count",
    hosted: "pages_ready", sha256: "sha256", pdfPath: "pdf_path", isFree: "is_free", isPublished: "is_published",
  };
  const row = { updated_at: new Date().toISOString() };
  for (const [k, col] of Object.entries(map)) if (patch[k] !== undefined) row[col] = patch[k] === "" ? null : patch[k];
  const { error } = await sb.from("topper_copies").update(row).eq("id", id);
  if (error) throw error;
}

export async function copyBySha(sha) {
  const sb = await getSupabase();
  const { data } = await sb.from("topper_copies").select("id, toppers(name)").eq("sha256", sha).maybeSingle();
  return data ? { id: data.id, topper: data.toppers?.name || "" } : null;
}

export async function uploadCopyPdf(copyId, file) {
  const sb = await getSupabase();
  const path = `${copyId}/copy.pdf`;
  const { error } = await sb.storage.from(COPY_PDFS).upload(path, file, { upsert: true, contentType: "application/pdf" });
  if (error) throw error;
  return path;
}

export async function uploadCopyPage(copyId, n, blob) {
  const sb = await getSupabase();
  const { error } = await sb.storage.from(COPY_PAGES)
    .upload(`${copyId}/p${n}.webp`, blob, { upsert: true, contentType: "image/webp", cacheControl: "3600" });
  if (error) throw error;
}

/** Delete a copy, its answers (cascade) and every stored file of it. */
export async function deleteCopy(id) {
  const sb = await getSupabase();
  for (const bucket of [COPY_PAGES, COPY_PDFS]) {
    const { data: files } = await sb.storage.from(bucket).list(id, { limit: 1000 });
    const paths = (files ?? []).map((f) => `${id}/${f.name}`);
    if (paths.length) await sb.storage.from(bucket).remove(paths);
  }
  const { error } = await sb.from("topper_copies").delete().eq("id", id);
  if (error) throw error;
}

/** A copy's answers, each with its linked essay PYQs. */
export async function copyAnswers(copyId) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxCopyAnswers(copyId);
  const sb = await getSupabase();
  const { data, error } = await sb.from("topper_answers")
    .select("id, paper, paper_label, question, start_page, end_page, sort_order, body_words, essay_answer_pyqs(pyq_id, kind, confidence)")
    .eq("copy_id", copyId)
    .order("start_page", { ascending: true, nullsFirst: false })
    .order("sort_order");
  if (error) throw error;
  return (data ?? []).map((r) => ({
    id: r.id,
    paper: r.paper,
    paperLabel: r.paper_label || "",
    question: r.question,
    startPage: r.start_page ?? "",
    endPage: r.end_page ?? "",
    words: r.body_words ?? null,
    links: (r.essay_answer_pyqs ?? []).map((l) => ({ pyqId: l.pyq_id, kind: l.kind, confidence: l.confidence ?? null })),
  }));
}

/** Save an essay's text from the admin. A new text is marked as entered by
 *  an admin; an edit keeps its source. An empty text removes it. */
export async function saveEssayText(answerId, body, { isNew = false } = {}) {
  const sb = await getSupabase();
  if (!String(body || "").trim()) {
    const { error } = await sb.from("topper_answer_texts").delete().eq("answer_id", answerId);
    if (error) throw error;
    return;
  }
  const row = { answer_id: answerId, body, ...(isNew ? { source: "entered by admin" } : {}) };
  const { error } = await sb.from("topper_answer_texts").upsert(row, { onConflict: "answer_id" });
  if (error) throw error;
}

export async function upsertAnswer(a) {
  const sb = await getSupabase();
  const num = (v) => (v === "" || v == null ? null : Number(v));
  const row = {
    ...(a.id ? { id: a.id } : {}),
    copy_id: a.copyId,
    paper: a.paper || "essay",
    paper_label: a.paperLabel || null,
    question: a.question.trim(),
    start_page: num(a.startPage),
    end_page: num(a.endPage),
  };
  const { data, error } = await sb.from("topper_answers").upsert(row).select("id").single();
  if (error) throw error;
  return data.id;
}

export async function deleteAnswer(id) {
  const sb = await getSupabase();
  const { error } = await sb.from("topper_answers").delete().eq("id", id);
  if (error) throw error;
}

/** Replace an essay answer's PYQ links with exactly this list. */
export async function setAnswerLinks(answerId, links) {
  const sb = await getSupabase();
  const { error } = await sb.from("essay_answer_pyqs").delete().eq("answer_id", answerId);
  if (error) throw error;
  if (!links.length) return;
  const { error: e2 } = await sb.from("essay_answer_pyqs").insert(
    links.map((l) => ({ answer_id: answerId, pyq_id: l.pyqId, kind: l.kind, confidence: l.confidence ?? null })));
  if (e2) throw e2;
}

/** Save start and end pages for several answers of one copy at once. */
export async function setAnswerPages(list) {
  const sb = await getSupabase();
  const num = (v) => (v === "" || v == null ? null : Number(v));
  for (const a of list) {
    const { error } = await sb.from("topper_answers")
      .update({ start_page: num(a.startPage), end_page: num(a.endPage) }).eq("id", a.id);
    if (error) throw error;
  }
}

/* ------------------------------------------- admin: wiki and Learn to Write -- */

/** One page of wiki snippets for review, with each one's essay and fits. */
export async function adminSnippets({ status = "", kind = "", q = "", offset = 0, limit = 30 } = {}) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxAdminSnippets({ status, kind, q, offset, limit });
  const sb = await getSupabase();
  let query = sb.from("essay_snippets")
    .select("id, answer_id, kind, body, attribution, why, review_note, page, status, updated_at, "
      + "essay_snippet_fits(pyq_id, use_note, rank), topper_answers(question, topper_copies(toppers(name)))", { count: "exact" });
  if (status) query = query.eq("status", status);
  if (kind) query = query.eq("kind", kind);
  const needle = String(q || "").replace(/[%,()*\\]/g, " ").trim();
  if (needle) query = query.or(`body.ilike.%${needle}%,attribution.ilike.%${needle}%`);
  const { data, error, count } = await query
    .order("answer_id").order("kind").order("id")
    .range(offset, offset + limit - 1);
  if (error) { if (missingTable(error)) return { items: [], total: 0, missing: true }; throw error; }
  return {
    total: count ?? 0,
    items: (data ?? []).map((s) => ({
      ...snippetFromRow(s),
      reviewNote: s.review_note || "",
      question: s.topper_answers?.question || "",
      topperName: s.topper_answers?.topper_copies?.toppers?.name || "",
      fits: (s.essay_snippet_fits ?? []).slice().sort((a, b) => (a.rank ?? 1) - (b.rank ?? 1))
        .map((f) => ({ pyqId: f.pyq_id, use: f.use_note, rank: f.rank ?? 1 })),
    })),
  };
}

/** Counts of snippets by status, and Learn to Write guides by status. */
export async function adminStudyStats() {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxAdminStudyStats();
  const sb = await getSupabase();
  const head = (t, s) => sb.from(t).select("*", { count: "exact", head: true }).eq("status", s);
  const res = await Promise.all([head("essay_snippets", "draft"), head("essay_snippets", "published"), head("essay_ltw", "draft"), head("essay_ltw", "published")]);
  if (res.some((r) => r.error && missingTable(r.error))) return { missing: true, snippets: { draft: 0, published: 0 }, ltw: { draft: 0, published: 0 } };
  const bad = res.find((r) => r.error);
  if (bad) throw bad.error;
  return { snippets: { draft: res[0].count ?? 0, published: res[1].count ?? 0 }, ltw: { draft: res[2].count ?? 0, published: res[3].count ?? 0 } };
}

export async function updateSnippet(id, patch) {
  const sb = await getSupabase();
  const row = {};
  if (patch.body !== undefined) row.body = String(patch.body).trim();
  if (patch.kind !== undefined) row.kind = patch.kind;
  if (patch.attribution !== undefined) row.attribution = String(patch.attribution || "").trim() || null;
  if (patch.why !== undefined) row.why = String(patch.why || "").trim() || null;
  if (patch.reviewNote !== undefined) row.review_note = String(patch.reviewNote || "").trim() || null;
  if (patch.status !== undefined) row.status = patch.status;
  const { error } = await sb.from("essay_snippets").update(row).eq("id", id);
  if (error) throw error;
}

/** Publish or unpublish many snippets at once. */
export async function setSnippetsStatus(ids, status) {
  const sb = await getSupabase();
  await inBatches(ids, 150, async (part) => {
    const { error } = await sb.from("essay_snippets").update({ status }).in("id", part);
    if (error) throw error;
  });
}

export async function deleteSnippet(id) {
  const sb = await getSupabase();
  const { error } = await sb.from("essay_snippets").delete().eq("id", id);
  if (error) throw error;
}

/** Every Learn to Write guide's state, by PYQ id. */
export async function adminLtwList() {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxAdminLtwList();
  const sb = await getSupabase();
  const { data, error } = await sb.from("essay_ltw").select("pyq_id, status, source, updated_at");
  if (error) { if (missingTable(error)) return new Map(); throw error; }
  return new Map((data ?? []).map((r) => [r.pyq_id, { status: r.status, source: r.source, updatedAt: r.updated_at }]));
}

export async function adminLtw(pyqId) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().fxLtw(pyqId);
  const sb = await getSupabase();
  const { data, error } = await sb.from("essay_ltw").select("doc, status, source, updated_at").eq("pyq_id", pyqId).maybeSingle();
  if (error) throw error;
  return data ? { doc: data.doc, status: data.status, source: data.source, updatedAt: data.updated_at } : null;
}

export async function saveLtw(pyqId, doc, status) {
  const sb = await getSupabase();
  const { data: { user } = {} } = await sb.auth.getUser();
  const { error } = await sb.from("essay_ltw")
    .upsert({ pyq_id: pyqId, doc, status, updated_by: user?.id ?? null }, { onConflict: "pyq_id" });
  if (error) throw error;
}

export async function deleteLtw(pyqId) {
  const sb = await getSupabase();
  const { error } = await sb.from("essay_ltw").delete().eq("pyq_id", pyqId);
  if (error) throw error;
}

export async function essayAutolink() {
  const sb = await getSupabase();
  const { data, error } = await sb.rpc("essay_autolink");
  if (error) throw error;
  return data || { exact: 0, related: 0 };
}

/* ------------------------------------------------------- mains import -- */
/* The importers take rows already parsed by lib/mainsImport.js. Each step is
 * an upsert that ignores duplicates, so re-importing the same sheet -- or a
 * newer version of it -- adds what is new and leaves edited rows alone. */

/** PYQs with their categories: themes, PYQs and theme links. */
export async function importEssayPyqs(items, onStep = () => {}) {
  const sb = await getSupabase();

  const themeNames = new Map();
  items.forEach((it) => it.themes.forEach((t) => {
    const slug = slugify(t.name);
    if (!themeNames.has(slug)) themeNames.set(slug, t.name);
  }));
  onStep("themes");
  await inBatches([...themeNames], 500, async (chunk) => {
    const { error } = await sb.from("essay_themes")
      .upsert(chunk.map(([slug, name]) => ({ slug, name })), { onConflict: "slug", ignoreDuplicates: true });
    if (error) throw error;
  });
  const themes = await selectIn(sb, "essay_themes", "id, slug", "slug", [...themeNames.keys()], 100);
  const themeId = new Map(themes.map((t) => [t.slug, t.id]));

  onStep("pyqs");
  await inBatches(items, 500, async (chunk) => {
    const { error } = await sb.from("essay_pyqs")
      .upsert(chunk.map((it) => ({ year: it.year, topic: it.topic })), { onConflict: "year,topic_key", ignoreDuplicates: true });
    if (error) throw error;
  });
  const years = [...new Set(items.map((it) => it.year))];
  const pyqs = await selectIn(sb, "essay_pyqs", "id, year, topic_key", "year", years, 50);
  const pyqId = new Map(pyqs.map((p) => [`${p.year}|${p.topic_key}`, p.id]));

  onStep("links");
  const links = [];
  for (const it of items) {
    const id = pyqId.get(`${it.year}|${essayKey(it.topic)}`);
    if (!id) continue;
    for (const t of it.themes) {
      const tid = themeId.get(slugify(t.name));
      if (tid) links.push({ pyq_id: id, theme_id: tid, confidence: t.confidence ?? null });
    }
  }
  await inBatches(links, 500, async (chunk) => {
    const { error } = await sb.from("essay_pyq_themes").upsert(chunk, { onConflict: "pyq_id,theme_id" });
    if (error) throw error;
  });
  return { themes: themeNames.size, pyqs: items.length, links: links.length };
}

/** Toppers, link copies and answers from parsed items (topper answers or
 *  topper essays). Existing rows are kept: every step ignores duplicates. */
async function saveCopiesAndAnswers(sb, items, onStep) {
  onStep("toppers");
  const toppers = new Map();
  items.forEach((it) => {
    const k = essayKey(it.topper.name);
    if (k && !toppers.has(k)) toppers.set(k, it.topper);
  });
  await inBatches([...toppers.values()], 500, async (chunk) => {
    const { error } = await sb.from("toppers").upsert(
      chunk.map((t) => ({ name: t.name, rank: t.rank, cse_year: t.cseYear, note: t.note || null, essay_marks: t.essayMarks ?? null })),
      { onConflict: "name_key", ignoreDuplicates: true });
    if (error) throw error;
  });
  const topperRows = await selectIn(sb, "toppers", "id, name_key", "name_key", [...toppers.keys()], 100);
  const topperId = new Map(topperRows.map((t) => [t.name_key, t.id]));

  onStep("copies");
  const copies = new Map();
  items.forEach((it) => {
    if (!it.url || copies.has(it.url)) return;
    const tid = topperId.get(essayKey(it.topper.name));
    if (tid) {
      copies.set(it.url, {
        topper_id: tid, source: it.coaching || null, written_year: it.topper.cseYear || null,
        source_url: it.url, title: it.title || null,
      });
    }
  });
  await inBatches([...copies.values()], 300, async (chunk) => {
    const { error } = await sb.from("topper_copies").upsert(chunk, { onConflict: "source_url", ignoreDuplicates: true });
    if (error) throw error;
  });
  // URLs are long; 20 per lookup keeps the request line short.
  const copyRows = await selectIn(sb, "topper_copies", "id, source_url", "source_url", [...copies.keys()], 20);
  const copyId = new Map(copyRows.map((c) => [c.source_url, c.id]));

  onStep("answers");
  const answers = [];
  const seen = new Set();
  for (const it of items) {
    const cid = copyId.get(it.url);
    if (!cid) continue;
    const dedupe = `${cid}|${essayKey(it.question)}|${it.page || 0}`;
    if (seen.has(dedupe)) continue;
    seen.add(dedupe);
    answers.push({ copy_id: cid, paper: it.paper, paper_label: it.paperLabel || null, question: it.question, start_page: it.page || null });
  }
  await inBatches(answers, 500, async (chunk) => {
    const { error } = await sb.from("topper_answers")
      .upsert(chunk, { onConflict: "copy_id,question_key,page_key", ignoreDuplicates: true });
    if (error) throw error;
  });
  return { toppers: toppers.size, copies: copies.size, answers: answers.length };
}

/** Topper answers (any paper): toppers, link copies and answers, then links. */
export async function importTopperAnswers(items, onStep = () => {}) {
  const sb = await getSupabase();
  const saved = await saveCopiesAndAnswers(sb, items, onStep);
  onStep("linking");
  const linked = await essayAutolink();
  return { ...saved, ...linked };
}

/** The topper-essay tab: its similar-PYQ map, then each essay with its
 *  writer and copy, then links. Either part may be empty. */
export async function importTopperEssays(items, topics = [], onStep = () => {}) {
  const sb = await getSupabase();
  const map = topics.length ? await saveTopicMap(sb, topics, onStep) : { mapped: 0, unmatched: [] };
  const saved = items.length ? await saveCopiesAndAnswers(sb, items, onStep) : { toppers: 0, copies: 0, answers: 0 };
  onStep("linking");
  const linked = await essayAutolink();
  return { essays: saved.answers, copies: saved.copies, writers: saved.toppers, mapped: map.mapped, ...linked, unmatched: map.unmatched };
}

/** Essay texts (typed transcripts): each matched to an imported essay by its
 *  copy (link, else file name as the copy's title) and its question. A newer
 *  text replaces the old one -- the transcript is the source of truth. */
export async function importEssayTexts(items, onStep = () => {}) {
  const sb = await getSupabase();
  onStep("matching");
  const titleOf = (file) => String(file || "").replace(/\.pdf$/i, "");
  const urls = [...new Set(items.map((it) => it.url).filter(Boolean))];
  const titles = [...new Set(items.map((it) => titleOf(it.file)).filter(Boolean))];
  const copies = [
    ...(await selectIn(sb, "topper_copies", "id, source_url, title", "source_url", urls, 20)),
    ...(await selectIn(sb, "topper_copies", "id, source_url, title", "title", titles, 20)),
  ];
  const byUrl = new Map(copies.map((c) => [c.source_url, c.id]));
  const byTitle = new Map(copies.filter((c) => c.title).map((c) => [c.title, c.id]));
  const answers = await selectIn(sb, "topper_answers", "id, copy_id, question_key", "copy_id", [...new Set(copies.map((c) => c.id))], 50);
  const answerId = new Map(answers.map((a) => [`${a.copy_id}|${a.question_key}`, a.id]));

  const rows = new Map();
  const missing = [];
  for (const it of items) {
    const cid = (it.url && byUrl.get(it.url)) || byTitle.get(titleOf(it.file));
    const aid = cid && answerId.get(`${cid}|${essayKey(it.question)}`);
    if (!aid) { missing.push(`${titleOf(it.file) || it.url} — ${it.question}`.slice(0, 180)); continue; }
    rows.set(aid, { answer_id: aid, body: it.body, source: "typed transcript", source_url: it.source || null });
  }
  onStep("saving");
  // Each text is a few kilobytes: 25 a request keeps each body small.
  await inBatches([...rows.values()], 25, async (chunk) => {
    const { error } = await sb.from("topper_answer_texts").upsert(chunk, { onConflict: "answer_id" });
    if (error) throw error;
  });
  const words = [...rows.values()].reduce((n, r) => n + (r.body.match(/\S+/g) || []).length, 0);
  return { texts: rows.size, words, missing };
}

/** "Similar PYQs" per mock topic: essay_topic_map, then links. */
export async function importTopicMap(items, onStep = () => {}) {
  const sb = await getSupabase();
  const { mapped, unmatched } = await saveTopicMap(sb, items, onStep);
  onStep("linking");
  const linked = await essayAutolink();
  return { topics: items.length, mapped, unmatched, ...linked };
}

/** essay_topic_map rows for each topic's similar PYQs, matched by year and
 *  topic (or topic alone). Returns how many rows and which PYQs had no match. */
async function saveTopicMap(sb, items, onStep) {
  onStep("matching");
  const pyqs = await essayPyqs({ includeDrafts: true });
  const byKeyYear = new Map(pyqs.map((p) => [`${p.year}|${essayKey(p.topic)}`, p.id]));
  const byKey = new Map();
  pyqs.forEach((p) => {
    const k = essayKey(p.topic);
    if (!byKey.has(k)) byKey.set(k, p.id);
  });

  const rows = new Map();
  const unmatched = new Set();
  for (const it of items) {
    const tk = essayKey(it.topic);
    if (!tk) continue;
    for (const s of it.similar) {
      const sk = essayKey(s.topic);
      const id = byKeyYear.get(`${s.year}|${sk}`) || byKey.get(sk);
      if (!id) { unmatched.add(s.year ? `${s.topic} (${s.year})` : s.topic); continue; }
      const key = `${tk}|${id}`;
      if (!rows.has(key) || (rows.get(key).confidence ?? 0) < (s.confidence ?? 0)) {
        rows.set(key, { topic_key: tk, topic: it.topic, pyq_id: id, confidence: s.confidence ?? null });
      }
    }
  }
  onStep("saving");
  await inBatches([...rows.values()], 500, async (chunk) => {
    const { error } = await sb.from("essay_topic_map").upsert(chunk, { onConflict: "topic_key,pyq_id" });
    if (error) throw error;
  });
  return { mapped: rows.size, unmatched: [...unmatched] };
}
