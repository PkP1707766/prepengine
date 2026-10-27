# Current-affairs papers: how they are framed and built

The series has five current-affairs papers, one for each quarter from January 2026 to March 2027. Each has 100 bilingual questions, takes two hours and is set on a Saturday at 9:30 am, after its quarter has ended. The dates are in `CA_DATES` in `upsc_series_setup.py`:

| Paper | Window | Date |
|---|---|---|
| CA 1 | January–March 2026 | 12 December 2026 |
| CA 2 | April–June 2026 | 16 January 2027 |
| CA 3 | July–September 2026 | 13 February 2027 |
| CA 4 | October–December 2026 | 6 March 2027 |
| CA 5 | January–March 2027 | 10 April 2027 |

Each row is tagged `question_data.ca_window` (`2026-Q1` and so on). Its concept id starts `ca-tN-`, followed by the subject (`ca`, `eco`, `pol`, `env`, `sci`, `his`, `geo`).

## 1. How an item is framed

UPSC rarely asks about the news itself. It asks about the static concept the news points to. Every item starts from one event in its window and is built in this order:

1. **Event.** Something that happened in the window: a report, a ruling, a summit, a scheme, a launch or an Act. Leads come from daily current-affairs lists. Every fact is then checked against PIB, the ministry, the regulator or the treaty body. The lead source is never named in a question or explanation, and a fact with no official confirmation is dropped.
2. **Static background.** Ask about the constitutional article, Act, institution, geography or science concept behind the event, not about the headline. For example, the CPI's new series leads to how weights move headline inflation, and the Hormuz closure leads to which ports lie outside the strait.
3. **Government focus areas.** Flagship schemes and missions, Budget announcements and the Economic Survey.
4. **Anniversaries.** Check whether the window holds a 5th, 10th, 20th, 25th, 30th, 35th, 40th, 50th, 75th or 100th year of an Act, institution, scheme, movement, treaty or event linked to the subject. CA 1 used the RRB Act (50 years), the Trade Unions Act (100), Goddard's liquid-fuel rocket (100), the Naujawan Bharat Sabha (100), the first Asian Games (75) and Bhuj (25).
5. **PYQ check.** Read the 2023–2026 PYQs on the same topic, options included. Do not repeat a question the paper has already asked. CA 1's first drafts did: the AI Summit was 2026 Q65, and minor minerals was 2025 Q89. Do borrow the paper's trap for the topic.

## 2. The 2026 paper's shape, which these papers follow

Our reading of the 2026 GS paper:

- **Multi-statement items** are about two-thirds of the paper. Most use combination codes ("1 and 2 only", "1, 2 and 3"). The "How many ... ?" count fell back to about six items.
- **List-I/List-II matching with codes** came back, with about ten items.
- **Negative items** ("NOT correctly matched", "which is NOT") number about five.
- **Statement relationships** appear in about three items. These ask whether Statement II supports Statement I, and whether Statement III contradicts or extends it.
- **Exact figures and dates** from official releases are asked: the precise number, the year, the parent body.

The `docs/upsc-question-design-standard.md` still applies in full: depth, crafts, no cues, keys balanced, an explanation that teaches. These papers add the 2026 mix on top.

| Format | CA 1 (built) | Target from CA 2 |
|---|---|---|
| Combination code (3–4 statements) | 65 | 55–60 |
| "How many" count (incl. all "None" items) | 9 | 6–8 |
| Two statements | 12 | 10–12 |
| List-I/List-II with codes | 2 | 5–6 |
| Negative ("NOT correctly matched" / "NOT") | 1 | 3–5 |
| Statement-I/II and I/II/III | 2 | 3 |
| Direct MCQ and chronology | 9 | 8–10 |

**Traps, from the 2026 paper's families:**
- scope inflation ("all", "only", "first", "every");
- the neighbouring date or number;
- the right fact on the wrong ministry or body;
- a famous name in the wrong context;
- a true fact that does not explain the claim;
- the currency trap, where a fact changed in the window, always with an explicit date.

## 3. The build

All of these are in `pyq-analysis-upsc/scratch/content_drafts/`.

- **Parts.** `ca_tN_a.py … g.py`, one per subject group, written with the usual builders (`S`, `M`, `A`, `C`, `P`). Statements are authored with their truth stated in the explanation's first sentence ("Statements 1 and 3 are correct"), using the count ladders.
- **`ca_common.py`**:
  - `combo(truth, pos)` gives four combination options. The distractors are near misses, and no statement appears in all four options or in none.
  - `MX(...)` builds List-I/List-II items with A-3, B-1 codes.
  - `finish(name, FORMAT, window)` turns the planned items into combination codes and reorders the statements. It renumbers the explanations in both languages, checks the planned truth against both the count key and the explanation, and tags the window.
- **`l3_tools/ca_plan.py ca_tN`** writes `ca_tN_format.py`:
  - It reorders statements so that each position is true about equally often, because authors tend to put the true statement first.
  - It swaps about half the "1 only" items to "2 only".
  - It sets the combination key letters so the paper comes to 25 per letter, with no three in a row.
  - It keeps a "How many" count for the items with no true statement and for those named in `KEEP_COUNT`.
  - It takes the key positions of MCQ and matching items from `POS`.
- **`l3_tools/ca_check.py ca_tN ca-tN-`** reports:
  - subjects, difficulty, the format tally and the letters;
  - the longest-key lint in both languages;
  - stray plan entries;
  - a cue scan between the paper's own items;
  - a PYQ look-alike scan against 2024–2026.
- **`l3_tools/overlap_scan.py N ca_tN 3`, then `… 5`.** This checks against the whole bank, refreshed from `l3_tools/bank_dump.sql`. Read every hit at threshold 5. In CA 1, four repeats appeared only at 5: the cess and surcharge SI, CCI as a statutory body, the FD/RD share of borrowing, and the CDS's lack of operational command.

## 4. Revising a paper after it is set up

A paper can be revised only before anyone sits it; `attempts` must be 0. Run `python ca_tN_x.py --update` to write `ca_tN_x_upd.sql`:

- It rewrites each row in place, matched on its concept id, and keeps its question id, so the paper's order and its usages stand.
- A row whose concept changed is listed in that part's `RENAMED = {new: old}`. The update renames its `question_usages` too.

After applying the update, check that:

- the database rows match the local build (key, options, statements, type);
- no key is bad, no Hindi is missing and no text has a CR;
- no old concept id is left;
- every usage's concept id equals its question's;
- the series-wide no-repeat count holds: published slots equal distinct questions.

## 5. Lessons from CA 1

- **Truth leaks by position.** Authors put the true statement first: before reordering, statement 1 was true far more often than statements 2–4. Reordering in `ca_plan` fixes this, and `ca_check` reports true-by-position.
- **MCQ keys bunch.** Seven of the first nine direct MCQs were keyed (d). Set `POS` deliberately.
- **Cues travel between items.** A figure in one stem (41 per cent) or a fact in one statement can answer another item's statement. Read the cue scan pair by pair.
- **Easy items are under-supplied.** Writers drift to medium and hard. Aim for about 15 easy items, which should be true current-affairs recall with a clean trap.
- **The bank is saturated on core economics.** It already covers effective capital expenditure, PMI, the impossible trinity, supply shocks and SIDBI. Search before drafting (`bank_find.py`), and prefer the window's own new numbers: a new threshold, a new series, a new list.

## 6. Lessons from CA 2

- **Truth leaks by count, too.** Reordering spreads the true statements across positions, but not across counts. In CA 2's first draft, 62 of 67 three-statement items had exactly two true statements, so "1, 2 and 3" and the single-statement codes could be ruled out blind. Twenty-six items were rewritten, in both languages, to 6 with none true, 19 with one, 24 with two and 18 with all three; CA 1 had 7, 22, 20 and 16. `ca_check` now prints "true statements per item": read it before `ca_plan`.
- **Statement-relationship keys bunch as well.** Four of the five SI items were first keyed "both correct, II explains I". Vary them: CA 2 ended with two of that key, and one each of "II does not explain", "I correct, II incorrect" and "I incorrect, II correct".
- **A negative MCQ's explanation must not name an option's position.** `M()` moves the key to its `POS`, so "the first statement is wrong" can end up pointing at the wrong option. Name the statement by what it says.
- **An item's stem can answer another item's statement.** A "Home Minister launched" stem, next to an item asking which ministry the NCRB is under, was a cue; the stem now says "the Centre".
- **A published paper keeps its order.** `upsc_series_setup.py` reads `ca_tN_order.txt` (one question id per line, written from the database after publishing) when it exists. Without it, a paper whose rows are revised, as CA 1's were, would be re-arranged in the setup file, although the database guard leaves the live order alone.
