# How a UPSC question is built in this series

UPSC's Prelims has grown harder and more deliberate every year. It now rarely asks a bare fact. It asks the candidate to verify several facts independently, to separate a true fact from a wrong inference, and to resist the shortcuts coaching teaches. A mock that is easier or more predictable than the real paper gives a false sense of readiness. Every question in this series is built to the standard below, which is taken from our reading of the 2023–2026 papers (`pyq-analysis-upsc/upsc-question-pattern-playbook-2023-2026.md`).

## 1. Form: follow the paper's current mix

- **"How many of the above ... are correct?"** is now the dominant form (about half of statement questions in 2025–26), usually with 3 or 4 statements. It cannot be solved by eliminating one statement: each must be judged on its own.
- **Two-statement "which is/are correct"** stays, at a lower share.
- **Statement-I / Statement-II**, and UPSC 2025's three-statement form (are II and III correct, and do they explain I?), mainly in Polity, Geography and Environment.
- **"How many pairs are correctly matched"**, including the *NOT correctly matched* variant. The old A-2, B-1 code format is not used.
- **Direct questions** where the paper uses them (Geography's places and resources, Science's concepts), with four equally plausible options.
- Each subject's type and difficulty mix comes from its own PYQ data (the live distribution config), not a generic split.

## 2. Depth: what makes a statement worth asking

- **Each statement is checkable, and each probes a different dimension of one concept:** its definition, a condition or exception, an actor, a consequence. Three unrelated trivia about one entity ("it lies in X; it was set up in Y; it is chaired by Z") is a recall drill, not a UPSC question. A student who half-knows the topic must be unsure.
- **Traps from UPSC's own families:** the right fact on the wrong body, article, ruler, author or place (Governor vs President; Art. 123 vs 213; Kailasa at Ellora vs Kailasanatha at Kanchi); two real features of the same thing swapped (Iodine-131 and Caesium-137); the reversed relation (Mathura vs Gandhara influence); the neighbouring number or date; the currency trap (a fact that changed), always with an explicit date; the fact that is true but does not support the claim.
- **The absolute-sounding true statement.** Sometimes "only", "all" or "never" is exactly right. This defeats the shortcut that absolute words mean false.
- **"All correct" and "none correct" appear,** as on the real paper, so that a candidate hunting for the one planted error is caught.
- **Why, not only what,** wherever the syllabus allows: a mechanism (why Arctic warming is amplified), a consequence (why a pocket veto is contested), an inference from evidence.

## 3. Loopholes the series must never leave

- **No giveaway wording.** A false statement must not announce itself ("without any dispute", "entirely", "unconditionally", "fully accepted by all").
- **No statements that contradict each other** inside one question.
- **No length cue.** The correct option is never the longest or most qualified one. The builder refuses such a row.
- **Balanced answer keys.** Within every paper, no answer (e.g. "Only two", option "b") dominates a format; the spread is tracked per batch and per paper.
- **No topic tag on the exam screen** during a UPSC attempt.
- **No question repeats** across published tests (enforced at generation and at publish).
- **No ambiguity.** A statement that experts dispute is not asked unless the dispute itself is the point and the stem says so.

## 4. The explanation teaches the concept

Every explanation says which statements are right and which are wrong and why, names the trap, and gives the correct fact with its anchor (article, Act, year, source). A student should be able to answer the next ten variants of the question from it. Every row cites a primary or standard source.

## 5. Both languages

The Hindi is written with the English, to the same standard (`docs/upsc-hindi-style.md`). A qualifier lost in translation changes the answer, so the Hindi is checked for meaning, statement by statement.

## 6. Depth quota and construction recipes (from October 2026)

An audit on 2026-10-04 found the bank accurate but too often shallow. 49% of all rows were "how many are correct" over 3-4 single-fact statements about one entity. There were no case or scenario items, no concept-linkage items, and no 5- or 6-item lists, and some "easy" rows were school-level. The count format itself is right: it is rising in UPSC's own papers. The fault was what the statements asked. The owner shared recent mock papers from a reputed coaching institute as a benchmark. They are used here only to learn construction; their wording, sources, numbering and branding never enter the bank. The recipes below hold every paper from now on.

**Quota per 100-question paper (and per sectional test):**
- At least **35 analytic rows**. An analytic row uses recipe A, B, C or E below: application, inference, linkage or multi-item judgement.
- About 35 **precision rows** (recipe D): exact conditions, exceptions, near-miss traps.
- At most **30 pure-recall rows**, meaning what, where, who or when about a single entity, with no condition, mechanism or application. History and world places lean on recall by nature; the other subjects and the current-affairs share make up for it, so the cap holds for the paper.
- Hard rows near the recent UPSC share for the subject (History about 40%; see the playbook). A row is labelled hard only if it needs two or more independent verifications with a trap, or an application or inference.
- Every row records its recipe in `question_data.craft`: `recall`, `precision`, `application`, `inference`, `linkage` or `multi`. The share is reported per paper.

**Recipes:**
- **A. Application (case or scenario).** A concrete situation the student must test against a rule. Examples: a law punishing an act done before the law existed; a boy of 15 working in a hazardous unit; six cases to test against the definition of national income or domestic territory; a disaster during a sitting, asking which parliamentary device fits. The options are the provisions, devices or cases. The trap is the neighbouring provision.
- **B. Inference or implication.** "If X is observed, what follows?"; "which best describes ...?"; "which is most likely ...?" The student reasons from a relation, not from a remembered sentence. Examples: GDP at market price above GDP at factor cost means net indirect taxes are positive; a fall in ICOR at a constant investment rate means faster growth.
- **C. Concept linkage.** "The above statements are associated with which principle?"; "which of the following support the assertion?"; "which relationship among Statements I-III holds?" Each item is true, so the work is judging relevance and direction. This is the fact-vs-inference trap of the 2026 papers. The second list renders through `question_data.sublist`.
- **D. Precision.** The exact constitutional or statutory condition, exception or recent change, set against its near-miss. Examples: "six months shall not intervene between sittings" against "twice a year"; which of six heads make a Money Bill; when a Bill lapses on dissolution. A changed fact is always given with its date.
- **E. Multi-item judgement.** Lists of 4-6 items ("Only two ... All five"), each needing its own judgement against one concept. Every item is a plausible member; no filler.

**Option craft:**
- Every MCQ distractor is the neighbouring concept a half-prepared candidate would choose: adjournment against calling-attention against short-duration discussion; margin requirement against credit rationing against moral suasion. A "best describes" item defines by mechanism, never by name-match.
- Up to 10% of 3-4 statement rows may use the hybrid conclusion options ("There are two correct statements, that include statement 3"). These defeat both elimination and blind counting.
- A false statement is built from the adjacent condition, actor or direction, never from a crude negation.

**CSAT** follows the same idea:
- Comprehension asks for inference, assumption, strengthening or weakening, the crucial message, and "most difficult to realise if".
- Quant and reasoning are multi-step and lean on number theory. They include data sufficiency, "how many statements are needed", and truth-teller puzzles, matching the playbook's 2026 shift.

## 7. Levels

- **Level 1 (Foundation):** NCERT facts and concepts, mostly easy to medium, same formats.
- **Level 2 (Sectional):** the subject's full syllabus at real-paper difficulty (per-subject PYQ weights).
- **Level 3 (Integration):** harder, cross-topic statements (a Polity question that needs Economy; Geography with Environment).
- **Level 4 (Simulation):** full papers in the real subject, type and difficulty mix, with the current-affairs share UPSC now sets.
