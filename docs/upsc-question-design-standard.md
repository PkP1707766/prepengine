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

- **One checkable fact per statement,** stated precisely: the right body, article, year, place, number or mechanism. A student who half-knows the topic must be unsure.
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

## 6. Levels

- **Level 1 (Foundation):** NCERT facts and concepts, mostly easy to medium, same formats.
- **Level 2 (Sectional):** the subject's full syllabus at real-paper difficulty (per-subject PYQ weights).
- **Level 3 (Integration):** harder, cross-topic statements (a Polity question that needs Economy; Geography with Environment).
- **Level 4 (Simulation):** full papers in the real subject, type and difficulty mix, with the current-affairs share UPSC now sets.
