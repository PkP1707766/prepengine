# Level 4 GS simulators: design

Level 4 has ten GS Paper I simulators: 100 questions, two hours, +2/-0.66. They run at 9:30 am from 17 April to 16 May 2027 (`L4_GS_DATES` in `upsc_series_setup.py`). Like the Level 4 CSAT simulators, each one mirrors the shape of one recent paper, so that a candidate is ready for the year-to-year swing rather than for one fixed mix.

## Shapes

The subject mixes are counted from the tagged papers in `pyq-analysis-upsc/upsc_gs1_combined_2015-2026.csv`:

| Shape | Polity | History | Environment | Geography | Economy | S&T | Current affairs | Easy / hard of static |
|---|---|---|---|---|---|---|---|---|
| A (2023/24) | 16 | 11 | 15 | 15 | 15 | 10 | 18 | 20% / 22% |
| B (2025) | 13 | 17 | 10 | 6 | 16 | 14 | 24 | 9% / 36% |
| C (2026) | 12 | 22 | 9 | 9 | 19 | 15 | 14 | 6% / 40% |

- **Rotation.** The simulators run A, B, C, A, B, C, A, B, C, C, so the last one is the latest shape.
- **Difficulty.** It follows the papers, which grew harder. Easy questions fell from 29 in 2023 to 5 in 2026, and hard ones rose from 23 to 41.
- **Format.** Shape A leans on "How many" counts and has about 10 Statement-I/II items, as 2023 and 2024 did. Shape B keeps about 9 Statement-I/II items, Statement III included. Shape C follows the 2026 paper: combination codes, about 9 List-I/II items, negatives and only 3 Statement-I/II items.

## Build

- **Targets.** `pyq-analysis-upsc/scratch/upsc_l4_gs_cell_targets.mjs` writes `l3_tools/l4_gs_targets.jsonl`. It takes each subject's sub-topic and type cells from the engine's sectional mix at that size, then re-weights difficulty and type to the shape.
- **The static part is written now.** It is 82, 76 or 86 questions, in `content_drafts/gs_l4_sNN_{a..f}.py` (a Polity, b History, c Environment, d Geography, e Economy, f S&T). Concept ids start `l4-sNN-`.
- **The current-affairs part is written in March and April 2027.** It is 18, 24 or 14 questions, written nearer the paper dates, as for Level 3, so that it is current when the paper runs.
- **Checks.**
  - Run `l3_tools/l3_check.py N gs_l4_sNN l4-sNN- l4_gs_targets.jsonl`. It reports the cells, key letters, the longest-key lint in both languages and the cue pairs.
  - Run `l3_tools/overlap_scan.py N gs_l4_sNN 4` after each part, and read every hit.
- **The bank is saturated.** It held 5,315 rows when Level 4 began, and nearly every standard Polity fact was already tested.
  - Search the specific clause or case before drafting, as in the Level 3 notes.
  - Prefer untested provisions, such as Articles 130, 139, 144, 146, 177, 243ZC, 309, 311(2), 339 and 340, and the Fifth Schedule's paragraph 3.
  - Prefer recent laws and rulings, and application items that combine provisions in a new case.
  - In Simulator 1's first draft, the overlap scan caught three repeats that `bank_find` had cleared: the re-election rule for a dissolved body (Article 243U, already asked for panchayats), ratification of amendments, and the Rajya Sabha's special majorities.
