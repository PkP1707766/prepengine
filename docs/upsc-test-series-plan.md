# UPSC Prelims 2027 Test Series — the plan every test is built to

Written 2026-09-28. Prelims 2027 is on **Sunday 23 May 2027** (UPSC calendar, released 20 May 2026).

## What was wrong, and why

The first eleven UPSC tests (History ×4, Polity ×4, Environment ×3) ran from 12 to 48 questions. Each subject had one 120-question bank. The blueprint's Level-2 note said to "just split by era/sub-topic instead of served as one 120Q test", so that bank was cut across the subject's tests in proportion to PYQ weight: Art & Culture got 12, Medieval 20, Modern 45. That produced a sequence of uneven quizzes, not a mock test series.

The ForumIAS PTS 2027 brochure the blueprint adapts is explicit about format. Level 2 is "23 GS subject-wise full-length tests (100 questions, 2 hours)", and Levels 3 and 4 are "100 Q / 2 Hr". A sectional test narrows the syllabus. It does not shrink the paper. The eleven drafts are therefore superseded. They were never published, and the app now refuses to publish them because they are not a standard UPSC length.

## Paper formats (fixed; enforced in the app)

| Paper | Questions | Marks | Time | Marking |
|---|---|---|---|---|
| GS Paper I (every GS test: Level 2, 3, 4, Current Affairs) | 100 | 200 | 2 hours | +2, −0.66 |
| CSAT Paper II (Levels 2–4) | 80 | 200 | 2 hours | +2.5, −0.83 (qualifying at 33%) |
| GS half paper (Level 1 use only) | 50 | 100 | 1 hour | +2, −0.66 |
| CSAT half paper (Level 1 minis) | 40 | 100 | 1 hour | +2.5, −0.83 |

The admin enforces this for UPSC only (BPSC is unchanged):
- A blueprint can only be saved at one of these lengths.
- A generated paper can only be saved when it is complete, never short.
- A test can only be published at a standard length.

## Rules that keep the series credible

1. **Complete papers only.** A test goes live only when all of its questions exist, are fact-checked with a primary-source citation, and the paper has been dry-run.
2. **No repeats.** A question that appears in a published UPSC test is never drawn again, and publishing is refused if a test shares a question with another published UPSC test. Students who sit every test never see the same question twice. Unpublished drafts block nothing.
3. **Exam-true composition.** Every paper's sub-topic, question-type and difficulty mix is apportioned from the subject's PYQ weights (2015–26, recency-weighted; types and difficulty from the 2023–26 papers). This includes Statement-I/II/III, Roman-numbered statements and "how many pairs" formats in their real proportions.
4. **A published syllabus per test.** Every test lists what it covers and the standard books it draws on. The sourcing is Junoonias's own: NCERT, Laxmikanth, Bipan Chandra, R.S. Sharma, Satish Chandra, and primary sources such as the Constitution, Acts, IPCC, UNFCCC, RBI and the Economic Survey.
5. **Honest numbering.** Tests are numbered in the order the series runs, and belong to a named series per level. Students see "Level 2 · Test 9 — Environment 1: Ecology & Biodiversity", not an internal label.

## The structure (72 tests; the blueprint's ~75)

| Level | Tests | Format | Questions to write |
|---|---|---|---|
| 1 Foundation (NCERT) | 6 GS subject papers + 1 GS revision + 3 CSAT minis | 100 / 100 / 40 | 820 |
| 2 Sectional Mastery | 21 GS sectionals (incl. 1 GS revision) + 7 CSAT | 100 / 80 | 2,660 |
| 3 Integration & Precision | 6 GS comprehensive + 4 CSAT (harder) | 100 / 80 | 920 |
| 4 Simulation | 10 GS + 9 CSAT simulators | 100 / 80 | 1,720 |
| Current Affairs | 5 quarterly value-addition tests | 100 | 500 |
| **Total** | **72** | | **6,620** |

The bank today holds **378 UPSC GS questions**: History 132, Polity 121, Environment 120, all published, plus 5 Geography drafts. All of them are usable at Level 2. A credible full series is about **6,600 questions**, because no question may repeat.

## Level 2 — the 21 GS sectional tests (live content status)

Output of `node upsc_level2_targets.mjs upsc_bank_by_subtopic_2026-09-28.json` (live config, 100 questions each):

| # | Test | Syllabus (what it covers) | Main sources | Have / 100 | To write |
|---|---|---|---|---|---|
| 1 | Polity 1: Constitutional Framework & Rights | Historical background, making of the Constitution, Preamble, salient features, basic structure, Union & territory, citizenship; Fundamental Rights, DPSP, Fundamental Duties, amendment | Laxmikanth; NCERT XI *Indian Constitution at Work*; the Constitution | 29 | 71 |
| 2 | Polity 2: Parliament & Executive | Parliament & State Legislatures (composition, sessions, law-making, budget, committees, privileges); President, VP, PM & Council of Ministers, AG; Governor, CM | Laxmikanth; the Constitution | 30 | 70 |
| 3 | Polity 3: Judiciary, Bodies, Elections & Laws | Supreme Court & High Courts, writs, tribunals, landmark judgments; constitutional & statutory bodies; elections, RPA, anti-defection; key statutes | Laxmikanth; the Acts | 30 | 70 |
| 4 | Polity 4: Federalism, Local Government & Governance | Centre–state relations, emergency, special provisions (Fifth & Sixth Schedules, Art. 371), UTs; Panchayats & Municipalities, co-operatives; RTI, e-governance, civil services | Laxmikanth; ARC reports | 32 | 68 |
| 5 | History 1: Modern India | Europeans & British expansion, 1857, reform movements, rise of nationalism, INC phases, Gandhian movements, revolutionaries, constitutional reforms 1909–1935, independence & partition | Bipan Chandra; NCERT *Our Pasts III*, *Themes III* | 47 | 53 |
| 6 | History 2: Ancient India | Prehistory, Harappan, Vedic age, Mahajanapadas, Buddhism & Jainism, Mauryas, post-Mauryan, Sangam, Guptas, post-Gupta to c. 750 CE | R.S. Sharma; NCERT *Themes I* | 45 | 55 |
| 7 | History 3: Medieval India | Early medieval kingdoms, Delhi Sultanate, Vijayanagara & Bahmani, Bhakti & Sufi, Mughals, Marathas, regional states | Satish Chandra; NCERT *Our Pasts II*, *Themes II* | 21 | 79 |
| 8 | History 4: Art & Culture | Architecture, sculpture & iconography, painting, music & dance, theatre & puppetry, literature, philosophy, festivals, heritage lists | NCERT *An Introduction to Indian Art*; CCRT; Ministry of Culture | 19 | 81 |
| 9 | Environment 1: Ecology & Biodiversity | Ecosystems (energy flow, cycles, succession), fauna & flora, forests & biomes | NCERT XII Biology (ecology unit); IUCN; BSI/ZSI | 46 | 54 |
| 10 | Environment 2: Climate Change & Pollution | Climate science & mitigation, UNFCCC/Kyoto/Paris, carbon markets, India's commitments; air, water, noise, waste pollution and their rules | IPCC AR6; UNFCCC; CPCB; MoEFCC | 48 | 52 |
| 11 | Environment 3: Policies & Conservation | Protected areas (NP, WLS, TR, BR, Ramsar), WPA 2022, conservation projects; Indian environmental laws & bodies; international conventions & organisations | MoEFCC; WPA; Ramsar/UNESCO lists | 26 | 74 |
| 12 | Geography 1: World Physical Geography | Earth's interior, plates, earthquakes & volcanoes, rocks, landforms; atmosphere, winds, cyclones, climate types, biomes; oceans; world regions & mapping | NCERT XI *Fundamentals of Physical Geography*; G.C. Leong; atlas | 3 | 97 |
| 13 | Geography 2: Indian Physical Geography | Physiography, drainage, lakes & wetlands, monsoon & climate, soils, vegetation, states & borders | NCERT XI *India: Physical Environment*; atlas | 2 | 98 |
| 14 | Geography 3: Human & Economic Geography | Minerals & energy, agriculture, industry, transport & ports, population (India & world) | NCERT XII human geography pair | 0 | 100 |
| 15–18 | Economy 1–4 (Basic concepts, money & banking · Growth, development & external sector · Fiscal policy, Budget & Survey · Sectors & inclusive growth) | as titled | NCERT; Economic Survey; Budget; RBI | 0 | 400 |
| 19–20 | Science & Technology 1–2 (General science · Applied S&T & agriculture) | as titled | NCERT Science & Biology; DST/ISRO/DBT | 0 | 200 |
| 21 | GS Comprehensive Revision | Full GS syllabus on the UPSC pattern | — | 0 | 100 |
| | **Level 2 GS total** | | | **378** | **1,722** |

Economy and S&T still need the content re-tag Geography had, because their decoder sub-topics are catch-alls (Macroeconomics 66%, Tech & Innovation 85%). Their four and two tests get sub-topic scopes then. The seven CSAT tests (80 questions each) are Level 2's remaining 560 questions.

## Schedule (proposal; each test is scheduled only once it is complete)

- **Level 2:** weekly on Sundays, 1 November 2026 to 21 March 2027 (21 GS tests), with CSAT 1–7 on alternate Saturdays. This needs about 80 new, verified questions a week from October.
- **Level 3:** late March to April 2027.
- **Level 4:** April to 16 May 2027, two simulators a week in the final stretch, the last one a week before the exam.
- **Current Affairs:** quarterly (Jan–Mar, Apr–Jun, Jul–Sep, Oct–Dec 2026, Jan–Mar 2027 windows).
- **Level 1** would have to run in October–November alongside Level 2's drafting. For the 2027 cycle it may be better offered self-paced, or folded into Level 2's first weeks (a decision below).

## Decisions for the owner

1. **Scope for Prelims 2027.** All four levels (≈6,600 questions) is the brochure's scale. Level 2 + Level 4 + Current Affairs first (≈4,900) is the minimum credible product. Level 2 alone (2,660) is the first milestone either way.
2. **Hindi.** The reference series publishes bilingual papers. Every question has Hindi fields that are empty today. Adding Hindi is best done per batch while drafting, not afterwards.
3. **Current affairs inside sectionals.** The reference adds that month's current affairs to each sectional paper. Recommended: about 10–15 of the 100 questions, which keeps each paper closer to the real exam's static/current mix.
4. **Old drafts.** The eleven superseded draft tests and the two old 120-question "Full Syllabus" blueprints can be deleted from the admin; nothing depends on them.

## What changed on 2026-09-28

- App: UPSC paper formats enforced at blueprint save, paper save and publish; CSAT papers timed at two hours; UPSC generation draws around every published UPSC test (no repeats) instead of BPSC's last-five cooldown.
- Data: a "UPSC Prelims 2027 — Level 2: Sectional Mastery" series. The eleven Level-2 blueprints moved to 100 questions, numbered titles and fresh theme groups. Geography's three Level-2 blueprints were added (tests 12–14).
- Files: `upsc_level2_targets.mjs` (+ `_output.txt`), `upsc_level2_series_setup.sql`, this plan.
