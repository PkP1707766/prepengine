# UPSC question bank audit — 28 September 2026

Every UPSC question in the bank (378: Polity 121, History 132, Environment 120, Geography 5 drafts) was read in full against its sources, its test's syllabus and UPSC's current question design. This is what was found and what was done.

## 1. Relevance: is each question in the right test?

Every question was checked against the syllabus of the Level-2 test its sub-topic feeds (docs/upsc-test-series-plan.md). No question sat in the wrong subject or the wrong test. The Polity split follows the standard book's own arrangement: Emergency is under *Federalism & Special Provisions* (Test 4), as the system-of-government part of the syllabus, and statutes are under Test 3. So no row had to be moved. Easy, NCERT-level rows stay in the bank; they are the easy band that both Level 1 and a real paper need.

## 2. Accuracy and currency

| Row | Problem | Fix |
|---|---|---|
| Polity: MGNREGA social audit (Statement-I/II) | Stale. The MGNREGA was repealed by the Viksit Bharat–Guarantee for Rozgar and Ajeevika Mission (Gramin) Act, 2025 (assent December 2025; 125 days; 60:40 cost sharing) | Rewritten on the new Act (PRS Bill Summary, PIB) |
| Polity: President's veto | "No time limit ... which makes a pocket veto possible" is contested after the April 2025 Tamil Nadu Governor judgment and the November 2025 Presidential Reference | Reworded to the uncontested fact (Article 111 prescribes no time limit), explanation updated |
| History: Karachi session 1931 (MCQ) | A distractor ("ratified the Gandhi-Irwin Pact") was also true, so the question had two right answers | Distractors replaced |
| History: leaders and newspapers | "Gandhi founded Young India" is false (he edited it) | Rewritten as a 'how many pairs' row with correct facts |
| History: Later Vedic period | "Untouchability emerged" in the Later Vedic period is contested | Statement replaced |
| History: Direct Action Day | "In response to the Congress's rejection of the Cabinet Mission Plan" is contested | Replaced by the League's withdrawal of its acceptance (29 July 1946) |
| History: Cripps Mission | Attribution of "a post-dated cheque on a crashing bank" is disputed | Replaced |

## 3. Question design: loopholes a test-wise student could use

**History (80 rows rewritten in place).** The earliest History rows could often be answered without knowing any history:
- a planted false statement that announced itself ("without dispute among historians", "caused entirely by a single factor", "exclusively Buddhist", "welcomed unconditionally", "fully accepted by both the Congress and the League");
- statements that contradicted each other (Fa-Hien "visited under Chandragupta II" and "visited under Harsha"), so one had to be false;
- school-level one-liners ("Who founded the Mauryan Empire?", "Which Mughal built the Taj Mahal?", "In which year was Quit India launched?");
- the pre-2020 "A-2, B-1, C-4, D-3" code format, which UPSC has replaced with "How many of the pairs given above are correctly matched?".
Each was rewritten with a specific, plausible trap drawn from UPSC's trap families (place, author, dynasty and title swaps; the right fact on the wrong ruler; a real feature of the same object in the wrong place; the absolute-sounding *true* statement), or replaced by a question on a real distinction (Samaharta vs Sannidhata, the Navaratnas without Aryabhata, pietra dura at I'timad-ud-Daula, the battle of Ghaghra, the four Calcutta 1906 resolutions).

**Answer spread.** In Environment, 12 of 17 three-statement "how many" rows answered "Only two", no four-statement row answered "Only one", and no two-statement row answered "Neither". Sixteen rows were re-seeded. The spread by format after the audit:

| Bank | 3-statement: one / two / all / none | 4-statement: one / two / three / all |
|---|---|---|
| Polity | 10 / 10 / 8 / 7 | 5 / 6 / 8 / 7 |
| Environment | 5 / 6 / 4 / 2 | 3 / 6 / 7 / 4 |
| History, Ancient | 6 / 9 / 8 / 1 | — |
| History, Medieval | 4 / 4 / 3 / 1 | — |
| History, Modern | 8 / 7 / 7 / 5 | — |
| History, Art & Culture | 3 / 3 / 2 / 1 | — |

**Length cue.** In 9 of 22 Environment MCQs, and several in Polity and History, the correct option was the longest and most qualified one. Fifteen option sets were rebalanced; the builder now refuses an MCQ whose answer is the longest option.

**Presentation.** The exam screen tagged every question with its sub-topic ("Pollution, Waste & Resources") during the attempt. The UPSC paper has no such tag, and it narrows the answer before the stem is read. It is now hidden on UPSC papers (the review keeps it).

## 4. Hindi

Every one of the 378 questions is now bilingual in every visible part: the stem, statements, list columns, Statement-I/II/III, the closing line, every option and the explanation (docs/upsc-hindi-style.md). Checked live in Hindi mode on a 48-question preview paper, including the three-statement and pairs formats. Two display bugs were fixed on the way: the exam loader dropped the Hindi test title, and generated tests never inherited a Hindi title.

## Files

`pyq-analysis-upsc/scratch/content_drafts/`: `history_rewrite_ancient.py`, `history_rewrite_medieval_culture.py`, `history_rewrite_modern.py`, `env_polity_audit_fixes.py`, `hindi_*.py` (each with its `.sql`), `bilingual.py`, `rewrite_common.py`, `hindi_common.py`. Migration `0027_exam_paper_exam_category.sql`.
