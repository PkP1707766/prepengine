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
 * Largest-remainder apportionment: turn fractional targets into integers that
 * sum to exactly `total`. Floor everything, then hand the leftover seats to the
 * cells with the biggest remainders. Without this, rounding each cell
 * independently drifts a 150-question paper to 147 or 153.
 */
function apportion(cells, total) {
  const withFloor = cells.map((c) => {
    const floor = Math.floor(c.raw);
    return { ...c, n: floor, rem: c.raw - floor };
  });
  let used = withFloor.reduce((s, c) => s + c.n, 0);
  const order = [...withFloor].sort((a, b) => b.rem - a.rem);
  let i = 0;
  while (used < total && order.length) {
    order[i % order.length].n += 1;
    used += 1;
    i += 1;
  }
  // If weights over-shot (rare with sane configs), trim smallest remainders.
  if (used > total) {
    const trim = [...withFloor].sort((a, b) => a.rem - b.rem);
    let k = 0;
    while (used > total) {
      const cell = trim[k % trim.length];
      if (cell.n > 0) { cell.n -= 1; used -= 1; }
      k += 1;
      if (k > trim.length * 4) break;
    }
  }
  return withFloor.filter((c) => c.n > 0);
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

/* ---------------------------------------------------------------- eligibility -- */

function inSubjectScope(q, blueprint) {
  if (blueprint.patternType === "full_length") return true;
  const scope = blueprint.subjectScope || {};
  if (scope.subject) return q.subject === scope.subject;
  return true;
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

function buildCells({ blueprint, config, pool }) {
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

  const diffEntries = normWeights(config.difficultyWeights || DEFAULT_DIFFICULTY, ["easy", "medium", "hard"]);

  const cells = [];
  for (const [subject, ws] of subjectEntries) {
    const typeEntries = normWeights(typeWeightsForSubject(config, subject), null);
    // sub_topic only splits sectional papers; the weights come off the blueprint
    // scope first, then the config, else a single wildcard.
    const subTopicSrc = blueprint.patternType === "sectional"
      ? (scope.sub_topic_weights || (config.subTopicWeights || {})[subject] || {})
      : {};
    const subTopicEntries = normWeights(subTopicSrc, null);

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
 * @param {object}   args.blueprint    — { patternType, questionCount, subjectScope, themeGroupId, title }
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
    bucket.subject ??= {}; bucket.difficulty ??= {}; bucket.type ??= {};
    bucket.subject[q.subject] = (bucket.subject[q.subject] || 0) + 1;
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
