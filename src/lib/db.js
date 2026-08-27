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
import { loadKey, saveKey, removeKey } from "./storage.js";

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
  const { data, error } = await sb
    .from("enrollments")
    .select("id, expires_at, status")
    .eq("student_id", userId)
    .eq("status", "active");
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
    .select("id, plan_code, batch_id, status, expires_at, enrolled_at, batches(name, course_id, end_date, courses(title, exam_target))")
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
  sortOrder: r.sort_order ?? 0,
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
    .select("test_id, tests(id, title, duration_min, total_questions, total_marks, is_free, is_published, scheduled_for)")
    .eq("plan_code", code);
  if (error) throw error;
  return (data ?? [])
    .map((r) => r.tests)
    .filter((t) => t && t.is_published)
    .map((t) => ({
      id: t.id,
      title: t.title,
      durationMin: t.duration_min,
      totalQuestions: t.total_questions,
      totalMarks: Number(t.total_marks || 0),
      isFree: !!t.is_free,
      scheduledFor: t.scheduled_for,
    }));
}

/** Which bundles does this student hold right now? */
export async function myPlanCodes(userId) {
  if (!userId) return new Set();
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("enrollments")
    .select("plan_code, status, expires_at")
    .eq("student_id", userId)
    .eq("status", "active");
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
    updated_at: new Date().toISOString(),
  };
  const { data, error } = await sb.from("plans").upsert(row).select().single();
  if (error) throw error;
  return data;
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
  return {
    id: q.id,
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

export async function listQuestions() {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_QUESTIONS;
  const sb = await getSupabase();
  const { data, error } = await sb
    .from("questions")
    .select("*")
    .eq("is_active", true)
    .order("created_at", { ascending: false });
  if (error) throw error;
  return (data ?? []).map(questionFromRow);
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
    const { data, error } = await sb.from(table).select("*").order(order, { ascending: false });
    if (error) throw error;
    return (data ?? []).map(mapRow);
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

export const series = crud(
  "test_series",
  (r) => ({ id: r.id, title: r.title, description: r.description || "", batchId: r.batch_id, price: Number(r.price || 0), isFree: !!r.is_free, createdAt: r.created_at }),
  (s) => ({ id: s.id, title: s.title, description: s.description || null, batch_id: s.batchId || null, price: Number(s.price || 0), is_free: !!s.isFree }),
);

/* ------------------------------------------------------------------ tests -- */

function testFromRow(r) {
  return {
    id: r.id,
    title: r.title,
    description: r.description || "",
    seriesId: r.series_id,
    seriesTitle: r.test_series?.title || "",
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
    title: t.title,
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

export async function listTests({ publishedOnly = false } = {}) {
  if (import.meta.env.DEV && FIXTURES_ON()) return fx().FX_TESTS.filter((t) => !publishedOnly || t.isPublished);
  const sb = await getSupabase();
  let q = sb.from("tests").select("*, test_series(title)").order("created_at", { ascending: false });
  if (publishedOnly) q = q.eq("is_published", true);
  const { data, error } = await q;
  if (error) throw error;
  return (data ?? []).map(testFromRow);
}

export async function upsertTest(t) {
  const sb = await getSupabase();
  const { data, error } = await sb.from("tests").upsert(testToRow(t)).select("*, test_series(title)").single();
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
    name: r.name,
    subjectWeights: r.subject_weights || {},
    difficultyWeights: r.difficulty_weights || {},
    questionTypeWeights: r.question_type_weights || {},
    subTopicWeights: r.sub_topic_weights || {},
    createdAt: r.created_at,
  }),
  (c) => ({
    id: c.id || undefined,
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
        questions: qs.map((q) => ({
          ...q,
          options: paper.shuffleOptions && Array.isArray(q.options) ? shuffle(q.options) : (q.options || []),
        })),
      };
    })
    .filter((s) => s.questions.length > 0);

  if (sections.length === 0) throw new Error("This test has no questions yet.");

  return {
    id: paper.id,
    title: paper.title,
    seriesTitle: paper.seriesTitle || "",
    durationSec: (paper.durationMin ?? 60) * 60,
    durationMin: paper.durationMin ?? 60,
    shuffleQuestions: !!paper.shuffleQuestions,
    shuffleOptions: !!paper.shuffleOptions,
    sections,
  };
}

/**
 * Submit a finished paper. The browser sends which option ids were chosen and
 * nothing else — the score, the section and topic breakdowns, the rank and the
 * percentile are all computed server-side and written by the service role.
 * `attempts` is no longer writable from the client at all.
 */
export async function submitAttempt({ testId, answers, timeSpent, timeUsed, startedAt }) {
  const sb = await getSupabase();
  const { data, error } = await sb.functions.invoke("submit-attempt", {
    body: { testId, answers, timeSpent, timeUsed, startedAt },
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
    .select("id, full_name, email, phone, created_at, target_exam")
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
