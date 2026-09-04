# BPSC CSE Prelims — PYQ Analysis Notes

**Status: final.** Scope locked at 6 cycles (66th excluded permanently — mismatched
key, not revisiting). All open convention questions below are resolved and applied.

Scope: **6 cycles, 900 questions** — 67th re-exam (30 Sep 2022), 68th (12 Feb 2023),
69th (30 Sep 2023), 70th (13 Dec 2024), 70th re-exam (4 Jan 2025), 71st (13 Sep 2025).
Excluded: 66th (provided key was for a different exam sitting — mismatched, verified
against unambiguous questions), 67th 1st attempt (annulled after a paper leak, per
user instruction).

All tagging done from the **English version** (BPSC's stated official standard where
English/Hindi differ). `correct_option` comes from the official answer key for each
paper's specific booklet series/set — never guessed. Key status per paper is in
`correct_option`'s sibling column `key_status` (`final` vs `provisional`); provisional
keys can still change on BPSC objection review (documented case: 70th, see below).

## Files in this folder

| File | Content |
|---|---|
| `combined_dataset.csv` | **Output 1.** All 900 rows, one per question, full taxonomy. |
| `summary_2_subject_by_year.csv` | **Output 2.** Subject % per cycle + average. |
| `summary_3_subtopic_within_subject.csv` | **Output 3.** Sub-topic % within each subject (pooled — see Methodology). |
| `summary_4a_type_overall.csv` | **Output 4.** Question-type % across all 900. |
| `summary_4b_type_by_subject.csv` | **Output 4.** Question-type % within each subject. |
| `summary_4c_type_by_year.csv` | Question-type % per cycle — surfaces the 69th outlier (see Trends). |
| `summary_5a_statement_count_distribution.csv` | **Output 5.** How many numbered statements (2/3/4/7...) per statement_based Q. |
| `summary_5b_option_combination_pattern.csv` | **Output 5.** Frequency of each option-combination pattern text. |
| `summary_5c_all_none_correct_rate.csv` | **Output 5.** How often All/None is actually the answer (functional vs. literal — see Methodology). |
| `summary_6_match_list_item_count.csv` | **Output 6.** List-I/II size distribution for match_the_following. |
| `summary_7_ambiguous_subject_flagged.csv` | **Output 7.** All 84 questions flagged ambiguous, for manual review. |
| `summary_8_low_confidence_cells.csv` | **Output 8.** Subject×type / subject×sub-topic cells with n<10. |
| `summary_9a_bihar_specific_recency_weighted.csv` | Bihar-Specific: flat vs. recency-weighted average (see Config recommendations). |
| `summary_9b_statement_based_baseline_excl_69th.csv` | statement_based baseline with the 69th outlier excluded. |
| `summary_9c_reasoning_aptitude_fixed_count.csv` | reasoning_aptitude as a fixed per-paper count, not a %. |
| `sme_recheck_70th_family.csv` | **12 questions (70th + 70th-reexam) with contradictory provisional answers — hold out of any item bank until an SME verifies or BPSC publishes a final key.** |
| `67th_re.csv` ... `71st.csv` | Per-paper source files (also individually delivered earlier). |

`combined_dataset.csv` now carries two extra columns beyond the original per-paper
files: `needs_sme_recheck` (TRUE for exactly those 12 rows) and `sme_recheck_reason`.
If this dataset feeds a live item bank, filter `WHERE needs_sme_recheck = FALSE`
before ingestion — the flagged 12 are still in the file (they were still asked on
the real exam) but their `correct_option` should not be trusted until verified.

## Trends — NOT averaged away, called out explicitly per instruction

**1. Bihar-Specific dropped by half between the 5-option and 4-option eras, then partly recovered.**
67th-re 20.7% → 68th 22.0% → **69th 10.0%** → 70th 16.0% → **70th-re 10.7%** → 71st 14.7%.
The two lowest points (69th, 70th-re) are both ~10%, well under half the 67th-re/68th
rate. This isn't drift — it's a step change. A flat 15.7% average hides that; see
Config recommendations below for the recency-weighted figure to use instead.

**2. `statement_based` question share: the 69th is a genuine outlier, not the norm.**
23.3% (35/150) of the 69th's questions are statement-based, against a **4.0% baseline**
in every other paper (67th-re, 68th, 70th, 70th-re all sit at exactly 4.0-4.0%; 71st is
somewhat higher at 8.0%). Pooling all 6 papers gives 7.4% overall — a number that
doesn't represent any single paper well; see Config recommendations for the
69th-excluded baseline to use instead.

**3. `reasoning_aptitude` is a fixed quota, not a weighted proportion.**
Every single one of the 6 papers carries **exactly 9 or 10** reasoning/aptitude
questions (6.0-6.7%), with no exceptions. This reads as a structural BPSC design
choice (a fixed block of ~10 questions) rather than a proportionally-scaled subject;
see Config recommendations.

**4. Environment & Ecology is trending up, off a small base.**
0.7% → 2.7% → 4.0% → 1.3% → 2.0% → **6.0%** (71st). The 71st's count (9) is nearly
double any other paper's. Total N is still only 25 across all 6 papers combined — real
signal, but treat as low-confidence per Output 8 below.

**5. Polity has crept up fairly steadily.**
5.3% → 6.7% → 8.7% → 8.0% → 9.3% → 9.3%. Closer to a genuine gradual rise than noise,
roughly monotonic across all 6 cycles.

## Config recommendations — confirmed figures to use in `distribution_config`

**Bihar-Specific weight: use 14.3%, not the flat 15.7%.**
Recency-weighted average (linear weights 1→6, oldest→newest cycle; see
`summary_9a_bihar_specific_recency_weighted.csv`):

| Cycle | Weight | Bihar-Specific % |
|---|---|---|
| 67th-reexam | 1 | 20.7% |
| 68th | 2 | 22.0% |
| 69th | 3 | 10.0% |
| 70th | 4 | 16.0% |
| 70th-reexam | 5 | 10.7% |
| 71st | 6 | 14.7% |
| **Recency-weighted average** | — | **14.3%** |
| (flat average, for comparison) | — | (15.7%) |

**statement_based weight: use 4.3%, not the 7.4% pooled figure.**
Baseline computed from the 5 non-69th cycles only (`summary_9b_...csv`):
67th-re 4.0%, 68th 4.0%, 70th 4.0%, 70th-re 1.3%, 71st 8.0% → **baseline = 4.3%**
(32 statement_based / 750 questions). The 69th's 23.3% is excluded as a confirmed
outlier, not blended in.

**reasoning_aptitude: encode as a fixed count of 10 per 150-question paper (9 in one
observed cycle), not a percentage weight.** Per-paper counts: 67th-re 10, 68th 10,
69th 10, 70th 10, 70th-re **9**, 71st 10 (`summary_9c_...csv`). Mode = 10 across all
6 cycles; only one paper ever deviated, and only by one question. If
`distribution_config` currently expresses this subject as a %, this is worth changing
to a literal fixed-count rule (`n = 10` per full-length 150-question paper) since the
data shows essentially no proportional variation — it behaves like a fixed exam
section, not a weighted subject.

## SME recheck — do not trust these 12 answers without verification

Both 70th-family papers (70th main, 13 Dec 2024, and its 4 Jan 2025 re-exam) still
carry **provisional** keys, and 12 of their questions have answers that contradict
well-established, easily-checkable facts (a wrong Amendment number, a wrong author
attribution, a mismatched minister/CM, etc.) — see `sme_recheck_70th_family.csv` for
the full list with reasons. **These 12 rows are flagged `needs_sme_recheck = TRUE` in
`combined_dataset.csv` and must not be ingested into a live question bank as-is.**
Options, once BPSC or an SME resolves them:
1. Wait for BPSC's final key for these two papers (final keys typically follow
   objection review, as happened for 68th and 71st) and re-verify then.
2. Have a subject-matter expert independently confirm/correct each of the 12 before
   use.
3. Exclude these 12 permanently if neither becomes available.

## Methodology notes (judgment calls made explicit)

- **Recent flagship government schemes** (PLI, SVAMITVA, NEP 2020, U-WIN, Bharatmala,
  etc.) are tagged under **Current Affairs → Schemes & Indices**, not Economy —
  confirmed convention. Established/structural economic concepts (Five-Year Plans,
  fiscal deficit, LFPR, banking mechanics) stay under Economy.
- **BPSC's static-GK/miscellaneous items** (fashion terms, festivals, World Heritage
  Sites, sportspeople) are tagged to the nearest-fitting subject and flagged
  `ambiguous_subject = TRUE` with a note, rather than given a dedicated "General
  Knowledge" bucket — confirmed convention, unchanged.

- **Sub-topic-within-subject (Output 3) is pooled across all 6 papers, not averaged
  year-by-year.** Many subject×sub-topic cells are single digits in any one paper
  (e.g., Economy > Banking & finance might be 2-3 questions in a given cycle), so an
  unweighted average of six noisy percentages would swing wildly on 1-question
  differences. Pooling (summing counts across all 900 rows before taking %) is
  equivalent to a count-weighted average and is the statistically defensible choice
  here. If you want the literal per-year-then-averaged version instead, it's a
  mechanical change to `build_analysis.py`.
- **`is_all_or_none_correct` vs. `all_none_literal_phrasing`** (confirmed convention):
  the first is TRUE whenever the correct answer functionally means "all the listed
  items" or "none of them" — including coded combinations like "1, 2 and 3" when every
  statement given is correct. The second is TRUE only when the option's literal text
  reads "All of the above" / "None of the above". Across all 900 questions: **37
  (4.1%) are functionally all/none-correct; 31 (3.4%) have the literal phrasing.**
  Both figures are computed across the *whole* dataset (not just statement_based),
  since 5-option papers (67th-re, 68th) carry a permanent "(E) None of the
  above/More than one of the above" choice on nearly every simple_mcq too.
- **`difficulty_guess`** is my judgment call throughout, per the prompt's instruction —
  never an official rating. BPSC does not publish difficulty data.
- **`source_type_guess`** is similarly inferential (NCERT-level / Bihar state board
  level / specialized reference / current_affairs), based on how specialized the fact
  is, not on any stated source.
- **`ca_recency_months`** is filled only where I could confidently date the underlying
  event; left blank rather than guessed where the timing was unclear.
- **Provisional vs. final keys.** 68th and 71st ship **FINAL** answer keys (post-
  objection, authoritative). 67th-re, 69th, 70th, and 70th-re are still
  **provisional** — BPSC could revise individual answers after objections. The 70th
  (13 Dec 2024) provisional key in particular contains several answers that
  contradict well-established facts (flagged inline in `question_text_en` for Q104,
  117, 129, 135, 139, 141, 150) — this was the cycle that triggered public
  controversy and the 4 Jan 2025 re-exam, so treat its `correct_option` values as the
  least reliable in this dataset until/unless a final key is published.
- **Deleted questions.** BPSC drops questions after upheld objections; these keep
  their row (they were still asked) with `correct_option = "Deleted"`. Counts: 69th=2,
  70th=0, 70th-re=3, 71st=5, 68th=1, 67th-re=0. 16 total across 900.

## Output 7 — ambiguous-subject questions

**84 of 900 questions (9.3%)** were flagged as straddling two subjects — see
`summary_7_ambiguous_subject_flagged.csv` for the full list with notes. Recurring
patterns worth your attention: Bihar-linked history/geography facts tagged under the
parent subject (e.g., "Rajgriha" under History>Ancient, noted as Bihar-linked) rather
than Bihar-Specific — a deliberate call per your confirmed convention (best primary +
flag, don't force), but worth a manual pass since it affects both History and
Bihar-Specific totals depending on how you want to count them downstream.

## Output 8 — sample-size / low-confidence cells

16 subject×type or subject×sub-topic cells have fewer than 10 questions across **all
900 combined** — see `summary_8_low_confidence_cells.csv`. Headline ones to treat as
low-confidence, not settled ratios:
- **assertion_reason: 1 question total**, across all 6 papers. Essentially no signal
  on this question type's real frequency — do not configure a meaningful weight for
  it from this data.
- **Environment & Ecology** as a subject: 25 total, and several of its sub-topics
  (Biodiversity, Climate & Pollution, Conservation & Policy) are each under 10.
- **match_the_following within most subjects** (Geography, Polity, Economy,
  Environment & Ecology) is 1-3 questions each — the list_item_count distribution in
  Output 6 is more reliable pooled across subjects than split by subject.
- A handful of Bihar-Specific and Economy sub-topics (e.g., Panchayati Raj &
  governance sub-splits) sit at single digits too.

## What this does NOT include

- No `correct_option` guessing anywhere — every value traces to an official key you
  provided, matched to the paper's specific series/set.
- No fabricated difficulty confidence — `difficulty_guess` is labelled as exactly
  that throughout.
- 66th and 67th-1st are absent by design (mismatched key / annulled exam), not
  oversight — see the file-mapping memory note if you want to revisit either later.
