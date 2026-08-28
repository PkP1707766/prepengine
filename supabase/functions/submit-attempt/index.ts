// POST /functions/v1/submit-attempt
//   { testId, answers: { [questionId]: optionId | optionId[] | "12.5" },
//     timeSpent: { [questionId]: seconds }, timeUsed, startedAt }
//
// Scoring lives here, not in the browser.
//
// It used to work the other way round: the paper was fetched with
// `select * from questions`, so every correct answer and explanation was in the
// browser before the student answered anything, and the resulting score,
// percentile and rank were written to `attempts` by the client. A student could
// read the answers mid-paper, or skip the paper entirely and insert
// `score: 200, rank_in_test: 1`. The leaderboard and the All-India Rank — the
// headline paid feature — were unverifiable.
//
// Now the client sends only which option ids it chose. Everything else is
// derived here, from the database, under the service role.
import { adminClient, callerFromRequest } from "../_shared/supabase.ts";
import { json, preflight } from "../_shared/cors.ts";

const bandFor = (accuracy: number) =>
  accuracy >= 75 ? "strong" : accuracy >= 50 ? "average" : "weak";

type Opt = { id?: string; body?: string; body_hi?: string | null; isCorrect?: boolean };

Deno.serve(async (req) => {
  const pre = preflight(req);
  if (pre) return pre;
  if (req.method !== "POST") return json(req, { error: "method_not_allowed" }, 405);

  const user = await callerFromRequest(req);
  if (!user) return json(req, { error: "unauthorized" }, 401);

  let body: {
    testId?: string;
    answers?: Record<string, unknown>;
    timeSpent?: Record<string, number>;
    timeUsed?: number;
    startedAt?: string;
    // The exact on-screen option order per question, so the review can show
    // the paper as it was sat rather than in canonical order.
    shownOrder?: Record<string, string[]>;
    marked?: string[];
  };
  try {
    body = await req.json();
  } catch {
    return json(req, { error: "bad_request" }, 400);
  }

  const testId = String(body.testId ?? "");
  if (!testId) return json(req, { error: "bad_request" }, 400);
  const answers = (body.answers ?? {}) as Record<string, unknown>;
  const timeSpent = (body.timeSpent ?? {}) as Record<string, number>;
  const shownOrder = (body.shownOrder ?? {}) as Record<string, string[]>;
  const markedSet = new Set(Array.isArray(body.marked) ? body.marked : []);

  const sb = adminClient();

  // Entitlement is re-checked server-side. A student who never had access
  // cannot submit an attempt for a paper they were not entitled to open.
  const { data: allowed, error: accErr } = await sb.rpc("can_access_test", { p_test: testId });
  if (accErr) {
    console.error("can_access_test failed", accErr);
    return json(req, { error: "server_error" }, 500);
  }
  if (!allowed) return json(req, { error: "no_access" }, 403);

  const { data: test } = await sb
    .from("tests")
    .select("id, title, title_hi, duration_min, sections, series_id, is_published, test_series(title, title_hi)")
    .eq("id", testId)
    .eq("is_published", true)
    .single();
  if (!test) return json(req, { error: "test_not_found" }, 404);

  const sections: { name?: string; questionIds?: string[] }[] =
    Array.isArray(test.sections) ? test.sections : [];
  const allIds = sections.flatMap((s) => s.questionIds ?? []);
  if (allIds.length === 0) return json(req, { error: "empty_test" }, 400);

  const { data: qRows } = await sb
    .from("questions")
    .select("id, subject, topic, type, difficulty, body, body_hi, question_data, options, numeric_answer, numeric_tolerance, marks_correct, marks_wrong, explanation, explanation_hi, source_citation, correct_rate")
    .in("id", allIds);
  const byId = new Map((qRows ?? []).map((q) => [q.id, q]));

  // ---- scoring -----------------------------------------------------------
  const review: Record<string, unknown>[] = [];
  const sectionAgg: Record<string, {
    name: string; score: number; max: number; correct: number; wrong: number; unattempted: number;
  }> = {};
  const topicAgg: Record<string, { name: string; subject: string; correct: number; total: number }> = {};
  // Difficulty- and question-type-wise accuracy (§7 result-page breakdowns).
  const diffAgg: Record<string, { name: string; correct: number; total: number }> = {};
  const typeAgg: Record<string, { name: string; correct: number; total: number }> = {};
  // One normalized row per question, written to student_responses after the
  // attempt is saved (needs its id).
  const responseRows: Record<string, unknown>[] = [];

  let score = 0, maxScore = 0, attempted = 0, correctN = 0, wrongN = 0;

  const times = allIds.map((id) => Number(timeSpent[id]) || 0);
  const avgTime = times.reduce((a, b) => a + b, 0) / (times.length || 1);
  const slowThreshold = Math.max(avgTime * 1.6, 25);

  for (const sec of sections) {
    const name = sec.name || "Section";
    sectionAgg[name] ??= { name, score: 0, max: 0, correct: 0, wrong: 0, unattempted: 0 };

    for (const qid of sec.questionIds ?? []) {
      const q = byId.get(qid);
      if (!q) continue;

      const marks = Number(q.marks_correct ?? 2);
      const negative = Number(q.marks_wrong ?? 0);
      const opts: Opt[] = Array.isArray(q.options) ? q.options : [];
      const raw = answers[qid];

      let isAttempted = false;
      let isCorrect = false;
      let yourVal: unknown = null;
      let correctVal: unknown = null;

      if (q.type === "numerical") {
        correctVal = Number(q.numeric_answer);
        const tol = Number(q.numeric_tolerance ?? 0.01);
        const typed = raw === null || raw === undefined || raw === "" ? null : Number(raw);
        isAttempted = typed !== null && Number.isFinite(typed);
        if (isAttempted) {
          yourVal = typed;
          isCorrect = Math.abs((typed as number) - (correctVal as number)) <= tol;
        }
      } else {
        // Options are matched by their stable id, so shuffling the paper in the
        // browser cannot change what counts as right.
        const correctIdx = opts.reduce<number[]>((acc, o, i) => (o.isCorrect ? [...acc, i] : acc), []);
        const idToIdx = new Map(opts.map((o, i) => [String(o.id), i]));

        if (q.type === "multiple") {
          correctVal = correctIdx;
          const chosen = Array.isArray(raw) ? raw : [];
          const chosenIdx = chosen
            .map((id) => idToIdx.get(String(id)))
            .filter((i): i is number => i !== undefined)
            .sort((a, b) => a - b);
          isAttempted = chosenIdx.length > 0;
          if (isAttempted) {
            yourVal = chosenIdx;
            const want = [...correctIdx].sort((a, b) => a - b);
            isCorrect = chosenIdx.length === want.length && chosenIdx.every((v, i) => v === want[i]);
          }
        } else {
          correctVal = correctIdx[0] ?? -1;
          const idx = raw === null || raw === undefined ? undefined : idToIdx.get(String(raw));
          isAttempted = idx !== undefined;
          if (isAttempted) {
            yourVal = idx;
            isCorrect = idx === correctVal;
          }
        }
      }

      // Reconstruct the exact on-screen order the student saw, so the review
      // shows the paper as sat. Falls back to canonical order when no order was
      // sent (numerical, shuffle off, or an older client).
      const canonicalIds = opts.map((o) => String(o.id));
      const shown = Array.isArray(shownOrder[qid]) && shownOrder[qid].length === canonicalIds.length
        ? shownOrder[qid].map(String)
        : canonicalIds;
      const toShownIdx = (canonIdx: number) => {
        const pos = shown.indexOf(canonicalIds[canonIdx]);
        return pos === -1 ? canonIdx : pos;
      };
      const shownOpts = shown.map((id) => opts[canonicalIds.indexOf(id)] ?? { body: "", body_hi: null });
      // display_option_order: canonical letter (a/b/c/d) at each shown position.
      const displayOrder = shown.map((id) => String.fromCharCode(97 + canonicalIds.indexOf(id)));

      let correctShown: unknown = correctVal;
      let yourShown: unknown = yourVal;
      if (q.type === "multiple") {
        correctShown = (correctVal as number[]).map(toShownIdx).sort((a, b) => a - b);
        yourShown = isAttempted ? (yourVal as number[]).map(toShownIdx).sort((a, b) => a - b) : yourVal;
      } else if (q.type !== "numerical") {
        correctShown = toShownIdx(correctVal as number);
        yourShown = isAttempted ? toShownIdx(yourVal as number) : yourVal;
      }

      // Canonical letter of the chosen option, for the normalized ledger.
      const selectedOption = (q.type !== "numerical" && q.type !== "multiple" && isAttempted)
        ? String.fromCharCode(97 + (yourVal as number))
        : null;

      const awarded = !isAttempted ? 0 : isCorrect ? marks : -negative;
      const topic = q.topic || q.subject || "General";
      const diff = q.difficulty || "medium";
      const qtype = q.type || "mcq";
      diffAgg[diff] ??= { name: diff, correct: 0, total: 0 };
      typeAgg[qtype] ??= { name: qtype, correct: 0, total: 0 };
      diffAgg[diff].total += 1;
      typeAgg[qtype].total += 1;

      maxScore += marks;
      score += awarded;
      sectionAgg[name].max += marks;
      sectionAgg[name].score += awarded;

      topicAgg[topic] ??= { name: topic, subject: q.subject || topic, correct: 0, total: 0 };
      topicAgg[topic].total += 1;

      if (isAttempted) {
        attempted++;
        if (isCorrect) {
          correctN++; sectionAgg[name].correct++; topicAgg[topic].correct++;
          diffAgg[diff].correct++; typeAgg[qtype].correct++;
        } else { wrongN++; sectionAgg[name].wrong++; }
      } else {
        sectionAgg[name].unattempted++;
      }

      const t = Number(timeSpent[qid]) || 0;
      review.push({
        id: q.id, num: review.length + 1, section: name,
        type: q.type, topic,
        // Both languages are snapshotted, so a student can read their report in
        // either one later — and it stays readable even if the question is
        // edited or translated after the attempt.
        text: q.body,
        text_hi: q.body_hi || null,
        // Type-specific stem (statements / lists / assertion+reason), snapshotted
        // so the report renders the BPSC formats exactly as sat. Answer-free.
        data: q.question_data && typeof q.question_data === "object" ? q.question_data : {},
        // Bodies in the order the student saw them (see shownOpts above); the
        // answer travels as an index into this same shown order.
        options: shownOpts.map((o) => o.body ?? ""),
        options_hi: shownOpts.map((o) => o.body_hi ?? null),
        explanation: q.explanation || "",
        explanation_hi: q.explanation_hi || null,
        // §7 additions: difficulty, the cited source, and the crowd success rate
        // (prior attempts; refreshed just below to include this one).
        difficulty: diff,
        sourceCitation: q.source_citation || "",
        correctRate: q.correct_rate != null ? Math.round(Number(q.correct_rate) * 100) : null,
        yourVal: yourShown, correctVal: correctShown,
        attempted: isAttempted, correct: isCorrect, awarded,
        time: t, slow: t >= slowThreshold && t > 0,
      });

      responseRows.push({
        test_id: test.id,
        question_id: q.id,
        subject: q.subject || null,
        sub_topic: q.topic || null,
        difficulty: diff,
        question_type: qtype,
        display_option_order: displayOrder,
        selected_option: selectedOption,
        is_correct: isAttempted ? isCorrect : null,
        time_taken_seconds: t,
        marked_for_review: markedSet.has(qid),
      });
    }
  }

  const total = review.length;
  const unattempted = total - attempted;
  const accuracy = attempted > 0 ? (correctN / attempted) * 100 : 0;
  const scorePct = maxScore > 0 ? (Math.max(0, score) / maxScore) * 100 : 0;

  const topics = Object.values(topicAgg).map((t) => {
    const acc = t.total > 0 ? (t.correct / t.total) * 100 : 0;
    return { name: t.name, subject: t.subject, correct: t.correct, total: t.total, acc, band: bandFor(acc) };
  });

  const DIFF_ORDER: Record<string, number> = { easy: 0, medium: 1, hard: 2 };
  const difficultyStats = Object.values(diffAgg)
    .map((d) => ({ name: d.name, correct: d.correct, total: d.total, acc: d.total > 0 ? (d.correct / d.total) * 100 : 0 }))
    .sort((a, b) => (DIFF_ORDER[a.name] ?? 9) - (DIFF_ORDER[b.name] ?? 9));
  const typeStats = Object.values(typeAgg)
    .map((ty) => ({ name: ty.name, correct: ty.correct, total: ty.total, acc: ty.total > 0 ? (ty.correct / ty.total) * 100 : 0 }))
    .sort((a, b) => b.total - a.total);

  // ---- persist -----------------------------------------------------------
  const startedAt = body.startedAt || new Date().toISOString();
  const durationMin = Number(test.duration_min ?? 60);
  const series = (test as { test_series?: { title?: string; title_hi?: string } }).test_series;

  const { data: saved, error: insErr } = await sb
    .from("attempts")
    .insert({
      student_id: user.id,
      test_id: test.id,
      test_title: test.title,
      series_title: series?.title ?? null,
      score: Number(score.toFixed(2)),
      max_score: maxScore,
      total_questions: total,
      correct_count: correctN,
      wrong_count: wrongN,
      accuracy: Number(accuracy.toFixed(2)),
      time_taken_sec: Math.round(Number(body.timeUsed) || 0),
      duration_min: durationMin,
      answers,
      section_stats: Object.values(sectionAgg),
      topic_stats: topics,
      difficulty_stats: difficultyStats,
      type_stats: typeStats,
      review,
      status: "submitted",
      started_at: startedAt,
      submitted_at: new Date().toISOString(),
    })
    .select("id")
    .single();

  if (insErr || !saved) {
    console.error("attempt insert failed", insErr);
    return json(req, { error: "save_failed" }, 500);
  }

  // The normalized response ledger (§7). One row per question, tagged with the
  // shown option order — this is what the cross-attempt drill-down and the
  // crowd correct_rate read. A failure here must not fail the submit: the
  // student's score is already saved, and the ledger is a best-effort analytics
  // layer, so it is logged and swallowed.
  try {
    const rows = responseRows.map((r) => ({ ...r, attempt_id: saved.id, student_id: user.id }));
    const { error: srErr } = await sb.from("student_responses").insert(rows);
    if (srErr) throw srErr;
    // Refresh the crowd success rate for these questions now that this
    // attempt's answers are counted.
    await sb.rpc("refresh_correct_rate", { p_ids: allIds });
  } catch (e) {
    console.warn("student_responses write failed", e);
  }

  // Standing is computed and stored here too — the client used to write its
  // own percentile and rank straight into the row.
  let percentile = null, rank = null, totalStudents = null;
  try {
    const { data: st } = await sb.rpc("attempt_standing", { p_attempt: saved.id });
    const row = Array.isArray(st) ? st[0] : st;
    if (row) {
      rank = row.rank ?? null;
      totalStudents = row.total ?? null;
      percentile = row.percentile === null || row.percentile === undefined ? null : Number(row.percentile);
      await sb.from("attempts")
        .update({ percentile, rank_in_test: rank, total_peers: totalStudents })
        .eq("id", saved.id);
    }
  } catch (e) {
    console.warn("standing unavailable", e);
  }

  // Peer benchmarks, for the "where you stand" panel.
  let peerAvg = null, peerBest = null;
  try {
    const { data: peers } = await sb
      .from("attempts")
      .select("score, max_score")
      .eq("test_id", test.id)
      .eq("status", "submitted");
    const pcts = (peers ?? [])
      .filter((p) => Number(p.max_score) > 0)
      .map((p) => (Math.max(0, Number(p.score)) / Number(p.max_score)) * 100);
    if (pcts.length > 0) {
      peerAvg = pcts.reduce((a, b) => a + b, 0) / pcts.length;
      peerBest = Math.max(...pcts);
    }
  } catch { /* benchmarks are a nicety, not a requirement */ }

  return json(req, {
    attemptId: saved.id,
    testId: test.id,
    title: test.title,
    title_hi: test.title_hi ?? null,
    seriesTitle: series?.title ?? "",
    seriesTitle_hi: series?.title_hi ?? null,
    durationMin,
    startedAt,
    answers,
    score: Number(score.toFixed(2)),
    maxScore, scorePct, attempted, total, unattempted,
    correct: correctN, wrong: wrongN, accuracy,
    timeUsed: Math.round(Number(body.timeUsed) || 0),
    sections: Object.values(sectionAgg),
    topics, review,
    difficultyStats, typeStats,
    percentile, rank, totalStudents, peerAvg, peerBest,
  });
});
