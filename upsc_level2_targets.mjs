// Level-2 of the UPSC Prelims 2027 series at the real format: every GS sectional is a
// full GS Paper I -- 100 questions, 200 marks, 2 hours -- as in the ForumIAS PTS 2027
// model the blueprint adapts (its Level 2: "23 GS subject-wise full-length tests (100
// questions, 2 hours)"). The old drafts split one 120-question bank per subject across
// its tests, which is why they ran from 12 to 48 questions.
//
// For every Level-2 test this runs the real buildCells() apportionment at 100 questions
// against the live config, then compares each sub-topic's target with the live bank.
// Run: node upsc_level2_targets.mjs upsc_bank_by_subtopic_2026-09-28.json
import { readFileSync } from "node:fs";
import { buildCells } from "./src/lib/generate.js";

export const PAPER = 100;
// Test numbers follow the order the series runs in; subjects whose banks are furthest
// along come first. Economy and S&T still need their sub-topics re-tagged from PYQ
// content (the same catch-all problem Geography had), so their scopes are pending.
export const LEVEL2 = [
  { no: 1, title: "Polity 1: Constitutional Framework & Rights", subject: "Polity", subs: ["Constitutional Framework", "Fundamental Rights, DPSP & Duties"] },
  { no: 2, title: "Polity 2: Parliament & Executive", subject: "Polity", subs: ["Parliament & State Legislature", "Union & State Executive"] },
  { no: 3, title: "Polity 3: Judiciary, Bodies, Elections & Laws", subject: "Polity", subs: ["Judiciary", "Judicial-Verdicts", "Constitutional & Statutory Bodies", "Elections", "Statutory-Laws"] },
  { no: 4, title: "Polity 4: Federalism, Local Government & Governance", subject: "Polity", subs: ["Federalism & Special Provisions", "Panchayati Raj & Local Governance", "Governance"] },
  { no: 5, title: "History 1: Modern India", subject: "History", subs: ["Modern"] },
  { no: 6, title: "History 2: Ancient India", subject: "History", subs: ["Ancient"] },
  { no: 7, title: "History 3: Medieval India", subject: "History", subs: ["Medieval"] },
  { no: 8, title: "History 4: Art & Culture", subject: "History", subs: ["Architecture", "Painting", "Music & Dance", "Iconography", "Culture-Other"] },
  { no: 9, title: "Environment 1: Ecology & Biodiversity", subject: "Environment & Ecology", subs: ["Fauna & Animal Behaviour", "Flora, Fungi & Forests", "Ecosystems & Ecological Processes"] },
  { no: 10, title: "Environment 2: Climate Change & Pollution", subject: "Environment & Ecology", subs: ["Climate Science & Mitigation", "Climate Agreements & Carbon Markets", "Pollution, Waste & Resources"] },
  { no: 11, title: "Environment 3: Policies & Conservation", subject: "Environment & Ecology", subs: ["Protected Areas & Wildlife Protection", "International Conventions & Organisations", "Indian Environmental Laws & Bodies"] },
  { no: 12, title: "Geography 1: World Physical Geography", subject: "Geography", subs: ["Geomorphology & Earth's Interior", "Climatology & Biomes", "Oceanography & Hydrosphere", "World Regions, Water Bodies & Places"] },
  { no: 13, title: "Geography 2: Indian Physical Geography", subject: "Geography", subs: ["Indian Rivers, Lakes & Wetlands", "Indian Physiography, Climate & Regions"] },
  { no: 14, title: "Geography 3: Human & Economic Geography", subject: "Geography", subs: ["Resources: Minerals, Energy & Agriculture", "Transport, Ports & Human Geography"] },
  { no: 15, title: "Economy 1: Basic Concepts, Money & Banking", subject: "Economy", subs: null },
  { no: 16, title: "Economy 2: Growth, Development & External Sector", subject: "Economy", subs: null },
  { no: 17, title: "Economy 3: Fiscal Policy, Budget & Economic Survey", subject: "Economy", subs: null },
  { no: 18, title: "Economy 4: Sectors of the Economy & Inclusive Growth", subject: "Economy", subs: null },
  { no: 19, title: "Science & Technology 1: General Science", subject: "Science & Technology", subs: null },
  { no: 20, title: "Science & Technology 2: Applied S&T & Agriculture", subject: "Science & Technology", subs: null },
  { no: 21, title: "GS Comprehensive Revision (full syllabus)", subject: null, subs: null },
];

const isMain = import.meta.url === new URL(process.argv[1], "file://").href || process.argv[1]?.endsWith("upsc_level2_targets.mjs");
const cfg = JSON.parse(readFileSync(new URL("./live_upsc_config.json", import.meta.url), "utf8"));
const bank = isMain ? JSON.parse(readFileSync(process.argv[2], "utf8")) : null;

if (isMain) {
let need = 0, have = 0;
console.log(`Level 2 -- ${LEVEL2.length} GS sectional tests, ${PAPER} questions each (live config: ${cfg.name})\n`);
for (const t of LEVEL2) {
  if (!t.subs) {
    const why = t.subject ? "sub-topics not yet re-tagged from PYQ content" : "draws on every subject once Level 2 is written; needs its own 100";
    console.log(`Test ${String(t.no).padStart(2)}  ${t.title.padEnd(56)} have   0 / ${PAPER}   to draft ${PAPER}   (${why})`);
    need += PAPER;
    continue;
  }
  const cells = buildCells({ blueprint: { examCategory: "upsc", patternType: "sectional", questionCount: PAPER, subjectScope: { subject: t.subject, sub_topics: t.subs } }, config: cfg, pool: [] });
  const target = {};
  for (const c of cells) target[c.subTopic] = (target[c.subTopic] || 0) + c.n;
  const got = t.subs.reduce((s, x) => s + Math.min(bank[t.subject]?.[x] || 0, target[x] || 0), 0);
  const parts = t.subs.map((x) => `${x} ${Math.min(bank[t.subject]?.[x] || 0, target[x] || 0)}/${target[x] || 0}`);
  console.log(`Test ${String(t.no).padStart(2)}  ${t.title.padEnd(56)} have ${String(got).padStart(3)} / ${PAPER}   to draft ${String(PAPER - got).padStart(3)}`);
  console.log(`         ${parts.join("  |  ")}`);
  need += PAPER - got; have += got;
}
console.log(`\nLevel 2 GS total: ${LEVEL2.length * PAPER} questions -- usable in the bank now ${have}, still to draft ${need}`);
}
