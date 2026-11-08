# Mains: the Essay section and topper copies

The Essay paper has no syllabus, so the themes are the syllabus. A student picks a theme, sees every UPSC essay topic in it, and reads how toppers wrote on that topic or a close cousin of it. Each essay opens at the page where it starts, not on the cover of a 30-page scan.

Slice 1 (7 November 2026, migration `0028_mains_essay.sql`) is the library: themes, PYQs, toppers, copies, and the reader. Nothing a student reads is generated: it is UPSC's own text or the topper's own copy.

## 1. The model

| Table | Holds |
|---|---|
| `essay_themes` | the categories students browse by, with an optional Hindi name |
| `essay_pyqs` | UPSC essay topics by year, with an optional Hindi topic |
| `essay_pyq_themes` | a PYQ's themes with a confidence; the highest is its main theme, the rest show as "also under" |
| `toppers` | name, the AIR and CSE year we show, the real UPSC Essay mark, and a note of every attempt |
| `topper_copies` | one copy: a **link** (a publisher's public PDF), **hosted** (pages in our storage), or both |
| `topper_answers` | one answer in a copy, for any Mains paper (`essay`, `gs1`–`gs4`, `optional`), with its start and end page |
| `essay_answer_pyqs` | which essay PYQs an essay answer answers: `exact` or `related` |
| `essay_topic_map` | "this mock topic is similar to that PYQ", from the similar-PYQ sheet |

Answers carry a paper so GS rows can be imported now and used when the GS sections are built. Only `essay` is shown to students today.

Topics, names and questions meet through `essay_key()`: lowercase letters and digits only. "Q.1) Truth knows no color." and "truth knows no colour" key differently (the spelling differs), but punctuation, case and spacing do not matter. The same rule is `essayKey()` in `src/lib/mainsKeys.js`.

## 2. Access

- Themes and PYQs are public.
- Copy metadata (who, where, which page) needs a session, so a locked copy can say what a bundle adds.
- Hosted page images are in the private `copy-pages` bucket. The app asks for ten-minute signed URLs, and storage signs them only when `can_read_topper_copy()` passes: an admin, a tester, a copy marked free, or a live enrollment on any plan with `includes_mains`. The lock on a hosted copy is enforced by the database.
- A link copy points at a PDF that is already public on its publisher's site. Its URL is readable by any signed-in student, so its lock is presentational only.
- Which bundles include Mains is the "Mains: Essay and topper copies" setting in Bundles & Pricing.

## 3. Getting data in

Admin → Mains & Essay → Import sheets. Export each Google Sheet tab as CSV (File → Download → Comma-separated values) and add it; several files can be picked at once. The importer recognises these layouts by their header row, wherever it sits:

| Layout | Header | Creates |
|---|---|---|
| PYQs with categories | `PYQ`, `Categories…` (cells like `Truth knows no color.(2025)` and `{Justice(70), Power(80)}`) | themes, PYQs, theme links with confidence |
| Topper essays | `File name`, `Topper Copy (Hand written)`, `Question from Topper Copy`, `Similar PYQs…`; optional `Topper`, `Source`, `AIR`, `Essay marks` | the similar-PYQ map, then writers, link copies and essay answers (no start page) |
| Topper answers | `Subject, Year, Rank, Topper, Coaching, Question, Page, Link` | toppers, link copies (one per PDF, `#page` stripped), answers with their start page |
| Similar-PYQ map | `Question from Topper Copy`, `Similar PYQs…` (entries like `Topic.(2025) (Confidence: 90)`) | `essay_topic_map` rows |
| Link list | `file_name`, `drive_id` | nothing by itself: it resolves the topper-essay tab's file names |
| Essay texts | `File name`, `Topper Copy (Hand written)`, `Question from Topper Copy`, `Text` | each essay's full text (paragraphs split by a blank line), matched to an imported essay by its copy and question; a newer text replaces the old |

Import the PYQs first, so the others have something to link to; then the topper essays; then the topper answers. Each import ends by running `essay_autolink()`, which links every essay answer whose topic matches a PYQ (exact) or appears in the map (related). Re-importing a newer export is safe: every step is an upsert that ignores duplicates, so existing rows, including any an admin edited, are kept.

**The topper-essay tab** needs its HandwrittenLinks list picked with it: the tab's copy links are `HYPERLINK(VLOOKUP(…))` formulas, and a CSV export keeps only the word "Link". The importer matches each file name to its Drive file and links the copy there (`…/file/d/<id>/view`); a Drive link opens at the first page, since Drive's viewer ignores `#page`. The writer comes from the file name ("VisionIAS Toppers Answer Booklet <Name>_<n>.pdf", "<Name> AIR211 Essay(149)-1.pdf", "<Name> - Essay …"). A row whose file name names nobody ("1.pdf", "230718 Essay Practice.pdf") is skipped and listed: some of these are evaluated practice copies, not toppers'. A `Topper` column replaces the file name as the source of the writer, so a reviewed CSV can name them and be imported again. The TypedLinks list (machine transcripts of the same copies) is recognised but not imported yet. The essay tab alone, without a link list, still imports its similar-PYQ map.

The importer also repairs what the sheets carry: `Q.2)` prefixes, `â€™`-style mojibake, a stray ` Domain` glued onto some topics (`…a selfish medium Domain.(2017)`), `2025, 2024, 2023` against `217, 267, 297` (the best rank and its year are shown; every attempt goes in the note), and coaching names ("Forumias" becomes "Forum IAS", "Vision" Vision IAS, "Mgp" Forum IAS). Rows with no link or no question are skipped and listed with the reason.

## 4. Hosting a copy

Copies → Upload a PDF copy, or Host pages from a PDF on an existing link copy. In the admin's own browser:

1. The file is checked: a `%PDF-` header, at most 150 MB. Its SHA-256 is compared against the library, so the same PDF cannot be added twice.
2. The original goes to the private `copy-pdfs` bucket (50 MB limit; a larger file is skipped with a warning, and its pages are still hosted).
3. pdf.js renders every page to a 1240 px WebP (A4 at 150 dpi) and uploads it as `copy-pages/<copy id>/p<N>.webp`. "Stop after this page" keeps what is done.
4. The copy is marked hosted with its page count and goes live if it was set to.

pdf.js only loads in this flow, in its own chunk; no student downloads it. pdf.js 5 has no eval path to switch off. The guards are size limits: the file size, a 50-megapixel cap per embedded image, and a 6,000 px cap on page height.

Then mark where each answer starts and ends. Use the PDF page, not the booklet's printed number. Link essay answers to PYQs in the answer editor, which suggests PYQs by word overlap with the answer's topic and also searches.

## 5. The student side

Dashboard → Essay.

- **On the home page.** A "Mains · Essay" section sits between the quote strip and the test series: live counts, the five biggest themes as tiles (each quoting a recent topic), and the bundle that includes Mains. A tile opens the dashboard on Essay at that theme; a visitor signs in first.
- **Essay PYQs.** A theme or year rail (a dropdown on phones), PYQ cards with the main theme and "also under", and "Read N topper essays".
- **A PYQ's topper essays.** The same question first, then each related topic, each group best UPSC Essay mark first.
- **Topper essays.** The whole essay library, sorted by marks, newest or oldest, filtered by year, with search.
- **Opening an essay.**
  - A hosted copy opens in the reader at its start page, with the essay's pages edged in gold.
  - A link copy opens the publisher's PDF at `#page=N` in a new tab.
  - A locked copy explains which bundles include it.
  - **Read as text** opens the essay's typed transcript, with its word count and a note that a third party typed it from the handwritten copy. The text sits behind the copy's own lock (`topper_answer_texts`, readable only where `can_read_topper_copy()` passes).
- **Search** in the library matches topics, toppers and any word inside an essay's text (`search_topper_essays()`, ids only).

The reader paints pages onto canvases, so no image URL sits in the page. It loads only the pages near the reader and releases far ones (4 of 27 painted on opening a fixture copy). It re-signs URLs before they expire.

## 5b. Study tools (slice 2, migration `0030_essay_study.sql`)

| Table / function | Holds |
|---|---|
| `essay_marks` | a student's star and done per PYQ, essay or wiki passage; `done_at` is stamped by a trigger |
| `essay_notes` | a student's notes (on an item, or free), with the item's label at the time; 1,000 per student |
| `essay_reads` + `essay_reader_counts()` | one row per student, essay and IST day; inserts only for today or yesterday. Counts are public to signed-in users, rows are not |
| `essay_snippets` + `essay_snippet_fits` | wiki passages (verbatim, behind `can_read_topper_copy()`), each fitted to PYQs with a "use it here" note; `review_note` is for admins |
| `essay_wiki_counts()` | published passages per theme and kind, for tab counts and locked views |
| `essay_ltw` + `essay_ltw_ready()` + `essay_ltw_preview()` | one Learn to Write guide per PYQ as JSON; readable with Mains, an outline (spine, sides, argument titles) for everyone signed in |

Wiki passages and guides are drafts until an admin publishes them.

**Drafting** happens outside the app (`mains-import/essay-drafting/`, kept out of git): the essays and PYQs are exported, split into batches (16 of 15 essays for the wiki, 24 of 4 PYQs for guides), drafted to a written spec, checked by `validate.mjs`, and turned into SQL by `to_sql.mjs`. Loading twice changes nothing: a passage already in place is skipped, and a published guide is never overwritten.

**Start pages** come from the admin's own copy of the PDF, drawn in the browser by the same pdf.js chunk the upload uses.

## 6. Still to decide or do

- **Tick Mains** on the bundle(s) that should include it (0028 is applied).
- **Which copies to host.** Most sheet rows link to coaching institutes' own PDFs, or to Drive copies of them; linking does not re-publish their work, hosting does. A Drive link depends on its owner keeping it shared.
- **Writers for the unnamed essay copies.** 48 copies in the topper-essay tab name no writer; fill a `Topper` column only where the writer is known.
- **The topper-answer sheet** needs its names and ranks reviewed before import: its AIR disagrees with the publisher's own file name on 72 copies, a few names are misspellings of another topper's, and its essay rows are mostly headings from inside the essays rather than topics. 117 of its 626 PDF links are dead (nextias.com and cdn.visionias.in).
- **Typed transcripts.** Their text is imported per essay (migration 0029): students read it as text, see word counts and search it. They carry no page numbers, so start and end pages still need the scans.
- **Hindi.** All 25 themes have Hindi names (8 Nov 2026). PYQ topics still fall back to English, and the admin flags each missing one in red; UPSC's own Hindi wording is the source to use for them.
- **Writer details.** Only 2 of the 68 essay writers have an AIR or Essay mark, and no copy has a year written, so the library's marks and year sorting have little to work with until these are filled (Admin → Copies → Edit).
- **Builds need Node 22.13 or newer**, because pdf.js 5 requires it.

## 7. Next slices

1. **Find answers inside a copy automatically.** Page images → a vision model in an edge function → each question and its start page, reviewed before saving. This is what makes uploading hundreds of copies practical.
2. **Learn to Write per PYQ.** Generated from the PYQ's linked topper answers, with every claim citing a copy and page, approved before publishing.
3. **An essay wiki.** Openings, quotes, anecdotes and closings mined from the copies, each with where it fits.
4. **Meaning-based search** (pgvector) over PYQs, answers and snippets, and better PYQ suggestions in the admin.
5. **Note tools in the reader:** text from a selected region, saved crops.
