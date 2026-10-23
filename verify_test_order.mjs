// Test order everywhere tests are listed (admin, bundle editor, storefront,
// student catalogue): Level 1 before Level 2; inside a level, dated papers by
// the day they open (the timetable, GS and CSAT interleaved), undated ones GS
// before CSAT, Test 1 before Test 2 -- whatever order the rows arrive in. The
// live UPSC rows used to print newest-first, so "CSAT Mini 3" led and Level 2
// sat above Level 1.
// Run: node verify_test_order.mjs
import { sortTests, groupBySeries, seriesLabel, shortTestTitle } from "./src/lib/testOrder.js";

const L1 = "UPSC Prelims 2027 — Level 1: NCERT Foundation";
const L2 = "UPSC Prelims 2027 — Level 2: Sectional Mastery";
const BP = "BPSC CCE Full Mock Series";
// Creation times and schedules as on the live rows: the Level 2 series was set
// up first; its GS papers open weekly from Sun 1 Nov, its CSAT papers every
// third Saturday from 7 Nov. Level 1 is undated.
const day = (iso, plus) => new Date(Date.parse(iso) + plus * 86400000).toISOString();
const CSAT_DAYS = ["2026-11-07", "2026-11-28", "2026-12-19", "2027-01-09", "2027-01-30", "2027-02-20", "2027-03-13"];
const upsc = [
  ...Array.from({ length: 20 }, (_, i) => [`Level 2 · Test ${i + 1} — GS`, L2, "2026-10-11T08:00:00Z", day("2026-11-01T04:00:00Z", 7 * i)]),
  ...CSAT_DAYS.map((d, i) => [`Level 2 · CSAT Test ${i + 1} — Paper II: Aptitude & Comprehension`, L2, "2026-10-11T08:00:00Z", `${d}T09:00:00Z`]),
  ...Array.from({ length: 7 }, (_, i) => [`Level 1 · Test ${i + 1} — NCERT Foundation`, L1, `2026-10-1${i < 3 ? 1 : 2}T09:00:00Z`, null]),
  ...Array.from({ length: 3 }, (_, i) => [`Level 1 · CSAT Mini ${i + 1} — Paper II Half Paper`, L1, "2026-10-16T09:00:00Z", null]),
];
const bpsc = [
  ["BPSC History Full Syllabus Test", "2026-09-02T20:00:00Z"],
  ["BPSC Bihar Special I", "2026-09-03T12:21:00Z"],
  ["BPSC Full Length GS — Final Rehearsal", "2026-09-17T19:06:00Z"],
  ["BPSC Full Length GS Test 2", "2026-09-17T19:06:00Z"],
  ["BPSC Full Length GS Test 1", "2026-09-17T19:06:00Z"],
  ["BPSC History Full Syllabus Test 2 — Advanced", "2026-09-18T16:19:00Z"],
];
const rows = [
  ...upsc.map(([title, seriesTitle, createdAt, scheduledFor]) => ({ examCategory: "upsc", title, seriesTitle, seriesId: seriesTitle, createdAt, scheduledFor })),
  ...bpsc.map(([title, createdAt]) => ({ examCategory: "bpsc", title, seriesTitle: BP, seriesId: BP, createdAt })),
];

let fail = 0;
const check = (ok, label) => { console.log(`${ok ? "PASS" : "FAIL"}  ${label}`); if (!ok) fail++; };

// Newest-first (how the database hands them over) and reversed must both come out the same.
const newestFirst = [...rows].sort((a, b) => b.createdAt.localeCompare(a.createdAt));
const a = sortTests(newestFirst).map((t) => t.title);
const b = sortTests([...newestFirst].reverse()).map((t) => t.title);
check(a.join("|") === b.join("|"), "order does not depend on the order rows arrive in");

const u = sortTests(rows.filter((t) => t.examCategory === "upsc")).map((t) => shortTestTitle(t.title));
// Level 2 timetable: a CSAT paper the Saturday before GS Tests 2, 5, 8, 11, 14, 17, 20.
const l2 = [];
for (let k = 1, c = 1; k <= 20; k++) {
  if ([2, 5, 8, 11, 14, 17, 20].includes(k)) l2.push(`Level 2 · CSAT Test ${c++}`);
  l2.push(`Level 2 · Test ${k}`);
}
const want = [
  ...Array.from({ length: 7 }, (_, i) => `Level 1 · Test ${i + 1}`),
  ...Array.from({ length: 3 }, (_, i) => `Level 1 · CSAT Mini ${i + 1}`),
  ...l2,
];
check(u.join("|") === want.join("|"), "UPSC: Level 1 Tests 1-7, CSAT Minis 1-3, then Level 2 by opening day");
console.log("      Level 2 reads: " + u.slice(10, 17).join(", ") + ", ...");

const groups = groupBySeries(sortTests(rows.filter((t) => t.examCategory === "upsc")));
check(groups.map((g) => `${seriesLabel(g.title)} (${g.tests.length})`).join(", ") === "Level 1: NCERT Foundation (10), Level 2: Sectional Mastery (27)",
  "UPSC groups: Level 1: NCERT Foundation (10), Level 2: Sectional Mastery (27)");

const bp = sortTests(rows.filter((t) => t.examCategory === "bpsc")).map((t) => t.title);
check(bp.join("|") === [
  "BPSC History Full Syllabus Test", "BPSC Bihar Special I",
  "BPSC Full Length GS Test 1", "BPSC Full Length GS Test 2", "BPSC Full Length GS — Final Rehearsal",
  "BPSC History Full Syllabus Test 2 — Advanced",
].join("|"), "BPSC (no levels): creation order; a batch created together goes by its number, unnumbered last");

check(seriesLabel("UPSC प्रारंभिक परीक्षा 2027 — स्तर 1: एनसीईआरटी आधार") === "स्तर 1: एनसीईआरटी आधार", "Hindi series heading drops the exam-and-year prefix");

console.log(fail ? `\n${fail} FAILED` : "\nALL PASS");
process.exit(fail ? 1 : 0);
