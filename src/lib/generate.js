/**
 * BPSC test-generation engine — pure, dependency-free, deterministic (seedable).
 *
 * Given a blueprint, a distribution_config, the question bank and the usage
 * ledger, it returns an ordered list of questionIds plus a report. It does NOT
 * touch the database — the admin runs it against `listQuestions()` and the
 * usage rows, previews the report, then persists through `commitGeneratedTest`.
 *
 * The four stages mirror the spec:
 *   1. apportion  — turn weights into an exact per-cell target for N questions
 *      (subject × difficulty × question_type, plus sub_topic for sectional).
 *   2. select     — fill each cell from eligible questions, cheapest-used first,
 *      never repeating a concept_group; backfill short cells within the subject.
 *   3. sequence   — constrained shuffle + repair so no run of same difficulty /
 *      subject / sub_topic / type clusters together.
 *   4. validate   — assert the constraints hold and report answer-letter balance.
 *
 * Everything is reported rather than thrown: a thin bank still produces a paper,
 * with the gaps surfaced so content effort can be aimed at the right cells.
 */

/* --------------------------------------------------------------- rng utils -- */

// mulberry32 — a tiny seedable PRNG so a generated paper is reproducible in a
// test and re-runnable by the admin. Falls back to Math.random with no seed.
function makeRng(seed) {
  if (seed == null) return Math.random;
  let a = seed >>> 0;
  return function () {
    a |= 0; a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function shuffleInPlace(arr, rng) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(rng() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

/* ------------------------------------------------------------ apportionment -- */

/**
 * Largest-remainder split of `total` across weighted keys: floor each share,
 * then give the leftover units to the biggest fractional remainders.
 */
function largestRemainder(entries, total) {
  const sum = entries.reduce((s, [, v]) => s + v, 0);
  const rows = entries.map(([k, v], i) => {
    const exact = sum > 0 ? (total * v) / sum : 0;
    return { k, i, n: Math.floor(exact), rem: exact - Math.floor(exact) };
  });
  let left = total - rows.reduce((s, r) => s + r.n, 0);
  // Remainders within float noise are a genuine tie (e.g. 28 x 0.8409 and 28 x 0.0909
  // both leave .5452); break it by config order so the result is deterministic.
  const byRem = (a, b) => (Math.abs(b.rem - a.rem) > 1e-9 ? b.rem - a.rem : a.i - b.i);
  [...rows].sort(byRem).forEach((r) => { if (left > 0) { r.n += 1; left -= 1; } });
  return new Map(rows.map((r) => [r.k, r.n]));
}

// The totals every paper must honour: per subject, and within each subject its
// difficulty, question-type and sub-topic splits.
const MARGINS = [
  (c) => `s|${c.subject}`,
  (c) => `d|${c.subject}|${c.difficulty}`,
  (c) => `t|${c.subject}|${c.questionType}`,
  (c) => `st|${c.subject}|${c.subTopic}`,
];

/**
 * Turn fractional cell targets into integers that sum to exactly `total` AND
 * keep every marginal (subject; subject×difficulty, ×type, ×sub-topic) at its
 * own largest-remainder total. Plain largest-remainder over the flat cell list
 * only guarantees the grand total: with many sub-1 cells the leftover seats all
 * go to the heavily weighted buckets, so a 5% difficulty share of 120 came out
 * at 3 instead of 6. Cells are floored, leftover seats go to the largest
 * remainder whose margins still have room, and a repair pass moves single seats
 * between cells until no margin is off (or no move helps).
 */
function apportion(cells, total) {
  const rawSum = cells.reduce((s, c) => s + c.raw, 0);
  const scale = rawSum > 0 ? total / rawSum : 0;
  const work = cells.map((c, i) => {
    const raw = c.raw * scale;
    return { ...c, i, x: raw, n: Math.floor(raw), keys: MARGINS.map((f) => f(c)) };
  });

  // Integer target for every margin: subjects split the total, then each
  // subject's own difficulty / type / sub-topic shares split that subject's seats.
  const target = new Map();
  const bySubject = new Map();
  for (const c of work) bySubject.set(c.subject, (bySubject.get(c.subject) || 0) + c.x);
  const subjSeats = largestRemainder([...bySubject], total);
  for (const [s, n] of subjSeats) target.set(`s|${s}`, n);
  for (const dim of [1, 2, 3]) {
    const groups = new Map();
    for (const c of work) {
      const g = groups.get(c.subject) || new Map();
      g.set(c.keys[dim], (g.get(c.keys[dim]) || 0) + c.x);
      groups.set(c.subject, g);
    }
    for (const [s, g] of groups) for (const [k, n] of largestRemainder([...g], subjSeats.get(s))) target.set(k, n);
  }

  const tally = new Map();
  const bump = (c, d) => { c.n += d; for (const k of c.keys) tally.set(k, (tally.get(k) || 0) + d); };
  for (const c of work) for (const k of c.keys) tally.set(k, (tally.get(k) || 0) + c.n);
  const room = (c) => c.keys.filter((k) => (tally.get(k) || 0) < target.get(k)).length;

  // Leftover seats: prefer cells with room in all four margins, then the most room,
  // then the largest remainder.
  let left = total - work.reduce((s, c) => s + c.n, 0);
  while (left > 0 && work.length) {
    let best = null, bestRoom = -1, bestRem = -Infinity;
    for (const c of work) {
      const r = room(c), rem = c.x - c.n;
      if (r > bestRoom || (r === bestRoom && rem > bestRem)) { best = c; bestRoom = r; bestRem = rem; }
    }
    bump(best, 1); left -= 1;
  }

  // Repair: move one seat between two cells whenever it reduces total margin error.
  const err = (k, t = tally.get(k) || 0) => Math.abs(t - target.get(k));
  for (let iter = 0; iter < total * 4; iter++) {
    let bestGain = 0, move = null;
    for (const a of work) {
      if (a.n === 0) continue;
      for (const b of work) {
        if (a === b) continue;
        let gain = 0;
        for (let d = 0; d < MARGINS.length; d++) {
          const ka = a.keys[d], kb = b.keys[d];
          if (ka === kb) continue;
          gain += err(ka) - err(ka, tally.get(ka) - 1) + err(kb) - err(kb, tally.get(kb) + 1);
        }
        // Tie-break toward keeping cells close to their exact share.
        const drift = Math.abs(a.n - 1 - a.x) + Math.abs(b.n + 1 - b.x) - Math.abs(a.n - a.x) - Math.abs(b.n - b.x);
        const score = gain - drift * 1e-6;
        if (gain > 0 && score > bestGain) { bestGain = score; move = [a, b]; }
      }
    }
    if (!move) break;
    bump(move[0], -1); bump(move[1], 1);
  }

  return work.filter((c) => c.n > 0).map(({ i, x, keys, ...c }) => c);
}

/* ------------------------------------------------------------------- pacing -- */

// Minutes per question for a generated paper, by exam. BPSC Prelims: 150 Q in
// 120 min. UPSC GS Paper I: 100 Q in 120 min. Other exams default to BPSC's pace.
export const MINUTES_PER_QUESTION = { bpsc: 0.8, upsc: 1.2 };

// The only shapes a UPSC mock may take: a full GS Paper I or CSAT Paper II (two
// hours each, as in the exam), or a one-hour half paper. A UPSC paper of any
// other length is not a credible mock (docs/upsc-test-series-plan.md).
export const UPSC_PAPER_FORMATS = [
  { questions: 100, minutes: 120, label: "GS Paper I — 100 questions, 2 hours" },
  { questions: 80, minutes: 120, label: "CSAT Paper II — 80 questions, 2 hours" },
  { questions: 50, minutes: 60, label: "GS half paper — 50 questions, 1 hour" },
  { questions: 40, minutes: 60, label: "CSAT half paper — 40 questions, 1 hour" },
];
export const upscPaperFormat = (n) => UPSC_PAPER_FORMATS.find((f) => f.questions === Number(n)) || null;

export function testDurationFor(examCategory, questionCount) {
  // CSAT's 80 questions get the full two hours, not 80 x 1.2 = 96 minutes.
  const format = examCategory === "upsc" ? upscPaperFormat(questionCount) : null;
  if (format) return format.minutes;
  const pace = MINUTES_PER_QUESTION[examCategory] ?? MINUTES_PER_QUESTION.bpsc;
  return Math.max(1, Math.round(questionCount * pace));
}

/* ------------------------------------------------------------------ weights -- */

const DEFAULT_DIFFICULTY = { easy: 0.3, medium: 0.5, hard: 0.2 };

function normWeights(obj, fallbackKeys) {
  const entries = Object.entries(obj || {}).filter(([, w]) => Number(w) > 0);
  if (entries.length === 0) {
    if (!fallbackKeys || fallbackKeys.length === 0) return [["*", 1]];
    const w = 1 / fallbackKeys.length;
    return fallbackKeys.map((k) => [k, w]);
  }
  const sum = entries.reduce((s, [, w]) => s + Number(w), 0);
  return entries.map(([k, w]) => [k, Number(w) / sum]);
}

// question_type_weights may be nested per-subject ({subject:{type:w}}) or a flat
// global map ({type:w}). Detect by whether the first value is an object.
function typeWeightsForSubject(config, subject) {
  const tw = config.questionTypeWeights || {};
  const first = Object.values(tw)[0];
  if (first && typeof first === "object") return tw[subject] || {};
  return tw; // flat/global
}

// difficulty_weights holds the global mix as flat keys ({easy,medium,hard}) and may
// also carry per-subject overrides ({..., "Polity": {easy,medium,hard}}). A subject
// without an override falls back to the flat keys, so flat-only configs are unchanged.
function difficultyWeightsForSubject(config, subject) {
  const dw = config.difficultyWeights || DEFAULT_DIFFICULTY;
  const own = dw[subject];
  if (own && typeof own === "object") return own;
  return Object.fromEntries(Object.entries(dw).filter(([, v]) => typeof v !== "object"));
}

/* ---------------------------------------------------------------- eligibility -- */

function inSubjectScope(q, blueprint) {
  if (blueprint.patternType === "full_length") return true;
  const scope = blueprint.subjectScope || {};
  if (scope.subject && q.subject !== scope.subject) return false;
  // A sub-topic-scoped paper (e.g. one of the four Level-2 History tests) draws
  // only from its own sub-topics -- backfill included, since it reads this pool.
  const subTopics = subTopicScope(blueprint);
  if (subTopics && !subTopics.has(q.topic || "")) return false;
  return true;
}

// subjectScope.sub_topics: the question.topic values a sectional/half paper is
// limited to. Absent or empty means the whole subject, exactly as before.
function subTopicScope(blueprint) {
  if (blueprint.patternType === "full_length") return null;
  const list = (blueprint.subjectScope || {}).sub_topics;
  return Array.isArray(list) && list.length > 0 ? new Set(list.map(String)) : null;
}

// Defense in depth: `listQuestions(examCategory)` already scopes the bank at
// the DB layer, so in the normal path this filter never actually removes
// anything. It exists so that if some future caller ever hands generateTest()
// an unscoped or wrongly-scoped bank, the generator itself still refuses to
// mix BPSC and UPSC questions into one paper rather than silently trusting
// the caller. blueprint.examCategory is required, matching the same
// "mandatory, never inferred" rule listQuestions() enforces.
function inExamScope(q, blueprint) {
  if (!blueprint.examCategory) throw new Error("generateTest: blueprint.examCategory is required");
  return q.examCategory === blueprint.examCategory;
}

function caInWindow(q, blueprint, now) {
  // Expired current-affairs questions are always out (spec §2).
  if (q.caValidUntil && new Date(q.caValidUntil) < now) return false;
  const range = (blueprint.subjectScope || {}).ca_date_range;
  if (!range || !q.caValidUntil) return true;
  const d = new Date(q.caValidUntil);
  if (range.from && d < new Date(range.from)) return false;
  if (range.to && d > new Date(range.to)) return false;
  return true;
}

/**
 * The eligible pool for this blueprint: published, active, in scope, in the CA
 * window, not on cooldown, and — the theme-group rule — carrying no concept
 * already used by any sibling test sharing this blueprint's theme_group_id.
 */
function eligiblePool({ blueprint, bank, usages, cooldownTestIds, now }) {
  const themeUsedConcepts = new Set(
    (usages || [])
      .filter((u) => blueprint.themeGroupId && u.themeGroupId === blueprint.themeGroupId && u.conceptGroupId)
      .map((u) => u.conceptGroupId),
  );
  const cooldown = new Set(cooldownTestIds || []);
  const onCooldown = new Set(
    (usages || []).filter((u) => cooldown.has(u.testId)).map((u) => u.questionId),
  );

  return (bank || []).filter((q) => {
    if (q.status && q.status !== "published") return false;
    if (q.isActive === false) return false;
    if (!inExamScope(q, blueprint)) return false;
    if (!inSubjectScope(q, blueprint)) return false;
    if (!caInWindow(q, blueprint, now)) return false;
    if (onCooldown.has(q.id)) return false;
    if (blueprint.themeGroupId && q.conceptGroupId && themeUsedConcepts.has(q.conceptGroupId)) return false;
    return true;
  });
}

// Cheapest-used first: fewest times_used, then longest since last used
// (never-used counts as oldest). Ties broken deterministically by id.
function byLeastUsed(a, b) {
  const ta = a.timesUsed ?? 0, tb = b.timesUsed ?? 0;
  if (ta !== tb) return ta - tb;
  const da = a.lastUsedDate ? new Date(a.lastUsedDate).getTime() : 0;
  const db = b.lastUsedDate ? new Date(b.lastUsedDate).getTime() : 0;
  if (da !== db) return da - db;
  return String(a.id).localeCompare(String(b.id));
}

/* ----------------------------------------------------------------- targeting -- */

// Exported (in addition to being used internally by generateTest) so the
// target apportionment can be inspected on its own -- this matters because
// generateTest() short-circuits to a single generic warning when the
// eligible pool is completely empty (see the early-return in generateTest
// below), skipping the per-cell gap breakdown entirely. That's invisible for
// an established bank (BPSC's pool has never been literally zero), but it's
// exactly the situation every brand-new UPSC subject starts from, where the
// row-by-row target *is* the thing a drafter needs to see. buildCells()
// itself needs no pool content for a sectional blueprint (subject comes from
// blueprint.subjectScope.subject, not from the pool), so it works standalone
// against an empty bank. Pure function, no behavior change to generateTest().
export function buildCells({ blueprint, config, pool }) {
  const count = blueprint.questionCount || 150;
  const scope = blueprint.subjectScope || {};

  // Subjects: full-length spans the config's subject weights (or an equal split
  // over the pool's subjects); sectional/half is a single subject at weight 1.
  let subjectEntries;
  if (blueprint.patternType === "full_length") {
    const poolSubjects = [...new Set(pool.map((q) => q.subject))];
    subjectEntries = normWeights(config.subjectWeights, poolSubjects);
  } else {
    subjectEntries = [[scope.subject || pool[0]?.subject || "General", 1]];
  }

  const cells = [];
  for (const [subject, ws] of subjectEntries) {
    const diffEntries = normWeights(difficultyWeightsForSubject(config, subject), ["easy", "medium", "hard"]);
    const typeEntries = normWeights(typeWeightsForSubject(config, subject), null);
    // sub_topic only splits sectional papers; the weights come off the blueprint
    // scope first, then the config, else a single wildcard. A sub-topic-scoped
    // paper keeps only its own sub-topics' weights (renormalised), or splits
    // evenly across them if none of them carries a weight.
    let subTopicSrc = blueprint.patternType === "sectional"
      ? (scope.sub_topic_weights || (config.subTopicWeights || {})[subject] || {})
      : {};
    const subTopics = blueprint.patternType === "sectional" ? subTopicScope(blueprint) : null;
    if (subTopics) subTopicSrc = Object.fromEntries(Object.entries(subTopicSrc).filter(([k]) => subTopics.has(k)));
    const subTopicEntries = normWeights(subTopicSrc, subTopics ? [...subTopics] : null);

    for (const [difficulty, wd] of diffEntries) {
      for (const [questionType, wt] of typeEntries) {
        for (const [subTopic, wst] of subTopicEntries) {
          cells.push({
            subject, difficulty, questionType, subTopic,
            raw: count * ws * wd * wt * wst,
          });
        }
      }
    }
  }
  return apportion(cells, count);
}

function matchesCell(q, cell) {
  if (q.subject !== cell.subject) return false;
  if (q.difficulty !== cell.difficulty) return false;
  if (cell.questionType !== "*" && q.type !== cell.questionType) return false;
  if (cell.subTopic && cell.subTopic !== "*" && (q.topic || "") !== cell.subTopic) return false;
  return true;
}

/* ------------------------------------------------------------------ selection -- */

function selectForCells({ cells, pool, report }) {
  const chosen = [];
  const chosenIds = new Set();
  const chosenConcepts = new Set();

  const take = (candidates, n) => {
    let took = 0;
    for (const q of candidates) {
      if (took >= n) break;
      if (chosenIds.has(q.id)) continue;
      // No two questions from one concept group in a single test (spec §2).
      if (q.conceptGroupId && chosenConcepts.has(q.conceptGroupId)) continue;
      chosen.push(q);
      chosenIds.add(q.id);
      if (q.conceptGroupId) chosenConcepts.add(q.conceptGroupId);
      took += 1;
    }
    return took;
  };

  const DIFF_ADJACENT = { easy: ["medium"], medium: ["easy", "hard"], hard: ["medium"] };

  for (const cell of cells) {
    const primary = pool.filter((q) => matchesCell(q, cell)).sort(byLeastUsed);
    const primaryGot = take(primary, cell.n);
    let got = primaryGot;

    if (got < cell.n) {
      // Backfill order (spec §3.3): same subject + same type, adjacent
      // difficulty first; then same subject, any type. Never cross-subject.
      const adj = DIFF_ADJACENT[cell.difficulty] || [];
      const sameTypeAdjacent = pool
        .filter((q) => q.subject === cell.subject && q.type === cell.questionType && adj.includes(q.difficulty))
        .sort(byLeastUsed);
      got += take(sameTypeAdjacent, cell.n - got);

      if (got < cell.n) {
        const sameSubjectAny = pool.filter((q) => q.subject === cell.subject).sort(byLeastUsed);
        got += take(sameSubjectAny, cell.n - got);
      }

      if (got > primaryGot) {
        report.backfills.push({
          subject: cell.subject, difficulty: cell.difficulty, type: cell.questionType,
          subTopic: cell.subTopic, requested: cell.n, fromExact: primaryGot, backfilled: got - primaryGot,
        });
      }
      if (got < cell.n) {
        report.gaps.push({
          subject: cell.subject, difficulty: cell.difficulty, type: cell.questionType,
          subTopic: cell.subTopic, short: cell.n - got,
        });
      }
    }
  }

  if (chosen.length < cells.reduce((s, c) => s + c.n, 0)) {
    report.warnings.push(
      `Bank too thin: produced ${chosen.length} of ${cells.reduce((s, c) => s + c.n, 0)} target questions. See gaps.`,
    );
  }
  return chosen;
}

/* ------------------------------------------------------------------ sequencing -- */

// How many of the given key repeat immediately before position `i` in `seq`.
function runBefore(seq, i, keyOf) {
  const k = keyOf(seq[i]);
  let n = 0;
  for (let j = i - 1; j >= 0 && keyOf(seq[j]) === k; j--) n++;
  return n;
}

function violatesAt(seq, i, constraints) {
  for (const c of constraints) {
    if (runBefore(seq, i, c.keyOf) >= c.max) return true;
  }
  return false;
}

/**
 * Constrained shuffle (spec §4): shuffle, then walk position by position and,
 * where a question would extend a forbidden run, swap it with the nearest later
 * question that fits and doesn't break its own new neighbourhood. A final pass
 * reports any residue rather than looping forever.
 */
function sequence({ questions, rng, report }) {
  const seq = shuffleInPlace([...questions], rng);

  const distinctSubjects = new Set(seq.map((q) => q.subject)).size;
  const distinctSubTopics = new Set(seq.map((q) => q.topic || "")).size;

  // Subject / sub_topic constraints only make sense when the paper actually
  // mixes them — a single-subject sectional paper must not fight itself.
  const constraints = [{ keyOf: (q) => q.difficulty, max: 2 }, { keyOf: (q) => q.type, max: 2 }];
  if (distinctSubjects > 1) constraints.push({ keyOf: (q) => q.subject, max: 3 });
  if (distinctSubTopics > 1) constraints.push({ keyOf: (q) => q.topic || "", max: 2 });

  for (let i = 1; i < seq.length; i++) {
    if (!violatesAt(seq, i, constraints)) continue;
    let swapped = false;
    for (let j = i + 1; j < seq.length; j++) {
      // Try seq[j] at position i: it must fit here, and moving seq[i] to j must
      // not break position j.
      const trial = [...seq];
      [trial[i], trial[j]] = [trial[j], trial[i]];
      if (!violatesAt(trial, i, constraints) && !violatesAt(trial, j, constraints)) {
        [seq[i], seq[j]] = [seq[j], seq[i]];
        swapped = true;
        break;
      }
    }
    void swapped;
  }

  // Validation pass — count anything the repair could not resolve.
  const residual = [];
  for (let i = 1; i < seq.length; i++) {
    if (violatesAt(seq, i, constraints)) {
      residual.push({ position: i + 1, subject: seq[i].subject, difficulty: seq[i].difficulty, type: seq[i].type });
    }
  }
  report.sequence = {
    length: seq.length,
    constraints: constraints.map((c) => c.max),
    residualViolations: residual.length,
    residual,
    ok: residual.length === 0,
  };
  return seq;
}

/* -------------------------------------------------------------- answer balance -- */

// Informational only: options are re-shuffled per student at serve time, so a
// stored letter bias never reaches anyone. Still worth surfacing if the bank
// itself clusters correct answers on one letter (spec §5).
function answerBalance(questions) {
  const letters = { a: 0, b: 0, c: 0, d: 0, other: 0 };
  for (const q of questions) {
    const opts = Array.isArray(q.options) ? q.options : [];
    const idx = opts.findIndex((o) => o.isCorrect);
    const key = ["a", "b", "c", "d"][idx];
    if (key) letters[key] += 1; else letters.other += 1;
  }
  return letters;
}

/* ----------------------------------------------------------------------- main -- */

/**
 * @param {object}   args
 * @param {object}   args.blueprint    — { examCategory, patternType, questionCount, subjectScope, themeGroupId, title }
 * @param {object}   args.config       — distribution_config (subjectWeights, difficultyWeights, questionTypeWeights, subTopicWeights)
 * @param {object[]} args.bank         — app-shaped questions from listQuestions()
 * @param {object[]} [args.usages]     — question_usages rows { questionId, testId, themeGroupId, conceptGroupId }
 * @param {object}   [args.options]    — { cooldownTestIds?: string[], now?: Date|string, seed?: number }
 * @returns {{ sections: {id,name,questionIds}[], questionIds: string[], report: object }}
 */
export function generateTest({ blueprint, config = {}, bank = [], usages = [], options = {} }) {
  const report = { warnings: [], gaps: [], backfills: [], distribution: {}, sequence: {}, answerBalance: {} };
  const now = options.now ? new Date(options.now) : new Date();
  const rng = makeRng(options.seed);

  const pool = eligiblePool({ blueprint, bank, usages, cooldownTestIds: options.cooldownTestIds, now });
  report.poolSize = pool.length;
  if (pool.length === 0) {
    report.warnings.push("No eligible questions for this blueprint (check scope, cooldown and theme dedup).");
    return { sections: [{ id: cryptoId(), name: blueprint.title || "Paper", questionIds: [] }], questionIds: [], report };
  }

  const cells = buildCells({ blueprint, config, pool });
  const selected = selectForCells({ cells, pool, report });

  // What the paper actually hit, by subject/difficulty/type — for the admin
  // to compare against the target before publishing.
  for (const q of selected) {
    const bucket = report.distribution;
    bucket.subject ??= {}; bucket.difficulty ??= {}; bucket.type ??= {}; bucket.subTopic ??= {};
    bucket.subject[q.subject] = (bucket.subject[q.subject] || 0) + 1;
    bucket.subTopic[q.topic || "(none)"] = (bucket.subTopic[q.topic || "(none)"] || 0) + 1;
    bucket.difficulty[q.difficulty] = (bucket.difficulty[q.difficulty] || 0) + 1;
    bucket.type[q.type] = (bucket.type[q.type] || 0) + 1;
  }

  const ordered = sequence({ questions: selected, rng, report });
  report.answerBalance = answerBalance(ordered);
  report.selected = ordered.length;
  report.target = blueprint.questionCount || 150;

  const questionIds = ordered.map((q) => q.id);
  return {
    sections: [{ id: cryptoId(), name: blueprint.title || "Paper", questionIds }],
    questionIds,
    report,
  };
}

// Small id for the section wrapper. Real UUIDs come from the callers; the
// section id is cosmetic and never leaves the sections array.
function cryptoId() {
  if (typeof crypto !== "undefined" && crypto.randomUUID) return crypto.randomUUID();
  return "sec-" + Math.random().toString(36).slice(2, 10);
}
