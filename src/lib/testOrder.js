/* One order for every list of tests: the admin's Tests page, the bundle
   editor, the storefront's bundle page and the student's catalogue.

   They all used to print tests newest-first, straight from created_at. A
   series therefore read backwards ("CSAT Mini 3" on top, "Test 1" at the
   bottom), and Level 2 sat above Level 1 only because its series row happened
   to be created first.

   The order a student should meet them in:
     1. the exam, so a student holding two bundles sees each one together;
     2. the series level -- "Level 1", "Level 2", ... read from the test title,
        else from its series title. Series without a level follow the levels;
     3. the series itself, so its tests stay together;
     4. inside a levelled series: GS papers first, then CSAT (Paper II), each
        by the number it carries ("Test 7", "CSAT Mini 2");
     5. then the order the tests were created in, then the title.
   Series without a level (the BPSC mock series) go by creation order first:
   their titles mix "Test 2" with "Special II", so the number only orders a
   batch created together ("GS Test 1" ... "GS Test 7", then "Final
   Rehearsal", which carries none). */

const LEVEL = /\bLevel\s+(\d+)\b/i;
const CSAT = /\bCSAT\b|\bPaper[\s-]*II\b/i;
// The paper's own number: "Level 2 · CSAT Test 3 — Paper II" -> 3.
const NUMBER = /\b(?:Test|Mini|Mock)\s+(\d+)\b/i;
const LAST = 1e9;

function keyOf(t) {
  const title = t.title || "";
  const lv = LEVEL.exec(title) || LEVEL.exec(t.seriesTitle || "");
  const level = lv ? Number(lv[1]) : LAST;
  const n = NUMBER.exec(title);
  const at = Date.parse(t.createdAt || "");
  return {
    exam: t.examCategory || "",
    level,
    series: t.seriesTitle || "",
    csat: level < LAST && CSAT.test(title) ? 1 : 0,
    n: n ? Number(n[1]) : LAST,
    at: Number.isNaN(at) ? 0 : at,
  };
}

export function compareTests(a, b) {
  const x = keyOf(a), y = keyOf(b);
  return x.exam.localeCompare(y.exam)
    || x.level - y.level
    || x.series.localeCompare(y.series, "en", { numeric: true })
    || (x.level < LAST
      ? x.csat - y.csat || x.n - y.n || x.at - y.at
      : x.at - y.at || x.n - y.n)
    || String(a.title || "").localeCompare(String(b.title || ""), "en", { numeric: true });
}

export const sortTests = (tests) => [...tests].sort(compareTests);

/** Consecutive runs of one series, in the order given (sort first). */
export function groupBySeries(tests) {
  const groups = [];
  for (const t of tests) {
    const key = t.seriesId || t.seriesTitle || "";
    const last = groups[groups.length - 1];
    if (last && last.key === key) last.tests.push(t);
    else groups.push({ key, title: t.seriesTitle || "", titleHi: t.seriesTitleHi || "", tests: [t] });
  }
  return groups;
}

/** "UPSC Prelims 2027 — Level 1: NCERT Foundation" -> "Level 1: NCERT Foundation".
    The bundle around the list already names the exam and year. */
export function seriesLabel(title) {
  const s = String(title || "");
  const i = s.lastIndexOf(" — ");
  return i > 0 ? s.slice(i + 3) : s;
}

/** "Level 1 · Test 1 — Polity (NCERT Foundation)" -> "Level 1 · Test 1". */
export function shortTestTitle(title) {
  const s = String(title || "");
  const i = s.indexOf(" — ");
  return i > 0 ? s.slice(0, i) : s;
}

/** The title in the reader's language, falling back to English. */
export const titleIn = (lang, t) => (lang === "hi" && t.titleHi ? t.titleHi : t.title);
export const seriesIn = (lang, g) => seriesLabel(lang === "hi" && g.titleHi ? g.titleHi : g.title);
