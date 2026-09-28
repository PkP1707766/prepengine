# Hindi for the UPSC series — style

Every UPSC question is written in both languages at the time it is drafted; the Hindi is not a later pass. The aim is Hindi that a Hindi-medium aspirant reads as easily as the English: correct, plain, and in the words they learnt from their books.

## The frame: UPSC's own Hindi-paper wording

Stems, closings and answer ladders use the fixed wording of UPSC's Hindi paper, which students already know (`bilingual.py` holds it and applies it automatically):

| English | Hindi |
|---|---|
| Consider the following statements: | निम्नलिखित कथनों पर विचार कीजिए: |
| How many of the above statements are correct? | उपर्युक्त में से कितने कथन सही हैं? |
| Which of the statements given above is/are correct? | उपर्युक्त कथनों में से कौन-सा/से सही है/हैं? |
| How many of the pairs given above are correctly matched? | उपर्युक्त में से कितने युग्म सही सुमेलित हैं? |
| Which one of the following is correct in respect of the above statements? | उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-सा एक सही है? |
| Only one / Only two / All three / None | केवल एक / केवल दो / सभी तीन / कोई नहीं |
| 1 and 2 only / Both 1 and 2 / Neither 1 nor 2 | केवल 1 और 2 / 1 और 2 दोनों / न तो 1, न ही 2 |
| Statement-I is correct but Statement-II is incorrect | कथन-I सही है, किंतु कथन-II गलत है |

## The content: plain standard Hindi

- **Short sentences, common words**, as in the NCERT Hindi textbooks. Prefer "बढ़ाना" to "संवर्धित करना", "लागू होना" to "प्रवर्तन में आना", unless the formal word is the one the syllabus uses.
- **The student's own terms for the subject.** Polity uses the vocabulary of the Constitution's Hindi text and the standard Hindi polity books: मौलिक अधिकार, राज्य के नीति निदेशक तत्व, संसद, विधानमंडल, संचित निधि, महाभियोग, अध्यादेश, प्रसादपर्यंत. Article letters follow the Hindi Constitution: 21क, 243थ, 239कक, 371छ.
- **English in brackets for a technical term on first use** when the Hindi word is less familiar than the English one, e.g. जैव-आवर्धन (biomagnification), पारिस्थितिक संक्रमण क्षेत्र (ecotone), समुद्रापगामी (anadromous). Acronyms stay as they are (NDC, IPCC, CITES, GST).
- **Proper nouns** in the form Hindi writing uses: महात्मा गांधी, लॉर्ड कर्ज़न, ह्वेनसांग, फाह्यान, कैबिनेट मिशन, राष्ट्रीय हरित अधिकरण. Scientific names stay in Latin.
- **Numerals stay Western** (1, 2, 3; अनुच्छेद 324; 2,695 मी), as on the UPSC paper.
- **Meaning, not word order.** A Hindi statement must be true or false for exactly the same reason as the English one. A translation that softens a qualifier ("केवल", "सभी", "पहली बार") changes the answer and is a defect.

## Where it is stored

`body_hi`, `explanation_hi`; inside `question_data`: `statements_hi`, `list_1_hi`, `list_2_hi`, `assertion_hi`, `reason_hi`, `reason_2_hi`, `closing_hi`; inside each option: `body_hi`. Tests, series and blueprints carry `title_hi`; a generated section carries `name_hi`. The builders (`rewrite_common.py`, `hindi_common.py`) refuse a row with any visible part missing its Hindi.
