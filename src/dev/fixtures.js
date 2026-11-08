/**
 * DEV-ONLY fixtures for the responsiveness harness.
 *
 * These let the real StudentApp / AdminApp / ExamApp components render with
 * realistic content so their layout can be measured at every breakpoint,
 * without anyone having to hand over a password.
 *
 * Deliberately awkward content: long names, long test titles, a long email,
 * a Devanagari string and big numbers — the things that actually break layouts.
 * Nothing here is imported in a production build (see the guard in db.js).
 */
const day = 86400000;
const iso = (daysAgo) => new Date(Date.now() - daysAgo * day).toISOString();

export const FX_USER = { id: "fx-user", email: "a.very.long.student.address@gmail.com" };

export const FX_PROFILE = {
  id: "fx-user",
  full_name: "Chandrashekhar Venkataraman Subrahmanyan",
  email: "a.very.long.student.address@gmail.com",
  role: "student",
  target_exam: "UPSC Prelims 2026",
  target_date: new Date(Date.now() + 120 * day).toISOString().slice(0, 10),
  city: "Muzaffarpur",
  avatar_url: null,
  prefs: {},
  created_at: iso(200),
};

/* Shared review rows (§7) — one of each BPSC format, a mix of right/wrong/
   skipped, carrying the new fields (shown-order options, difficulty, source,
   crowd correct_rate). Used by the result screen, the past-attempt solutions,
   and the My-Performance drill-down so all three render in dev. */
export const FX_REVIEW_ROWS = [
  {
    id: "frv-1", num: 1, section: "General Studies", type: "statement_based", topic: "Constitutional provisions", subject: "Polity",
    text: "Consider the following statements about the Fundamental Rights in the Indian Constitution:",
    text_hi: "भारतीय संविधान में मौलिक अधिकारों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
    data: {
      statements: [
        "The Right to Constitutional Remedies is itself a Fundamental Right.",
        "The Right to Property is a Fundamental Right under Part III.",
        "The Right to Education was inserted as Article 21A by the 86th Amendment.",
      ],
      statements_hi: [
        "संवैधानिक उपचारों का अधिकार स्वयं एक मौलिक अधिकार है।",
        "संपत्ति का अधिकार भाग-III के अंतर्गत एक मौलिक अधिकार है।",
        "शिक्षा का अधिकार 86वें संशोधन द्वारा अनुच्छेद 21क के रूप में जोड़ा गया।",
      ],
      closing: "Which of the statements given above is/are correct?",
      closing_hi: "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
    },
    options: ["Only 1 and 3", "Only 2 and 3", "Only 1 and 2", "All of the above"],
    options_hi: ["केवल 1 और 3", "केवल 2 और 3", "केवल 1 और 2", "उपर्युक्त सभी"],
    explanation: "Statement 2 is wrong: the 44th Amendment (1978) removed the Right to Property as a Fundamental Right; it is now a legal right under Article 300A. Statements 1 and 3 are correct — so 'Only 1 and 3'.",
    explanation_hi: "कथन 2 गलत है: 44वें संशोधन (1978) ने संपत्ति के अधिकार को मौलिक अधिकार से हटा दिया; अब यह अनुच्छेद 300क के अंतर्गत विधिक अधिकार है। कथन 1 और 3 सही हैं — अतः 'केवल 1 और 3'।",
    difficulty: "medium", sourceCitation: "NCERT Indian Polity; 44th Amendment Act, 1978", correctRate: 41,
    responseId: "sr-1", yourVal: 3, correctVal: 0, attempted: true, correct: false, awarded: -0.66, time: 52,
  },
  {
    id: "frv-2", num: 2, section: "General Studies", type: "mcq", topic: "Physical", subject: "Geography",
    text: "Which river is known as the 'Sorrow of Bihar'?",
    text_hi: "किस नदी को 'बिहार का शोक' कहा जाता है?",
    data: {},
    options: ["Ganga", "Kosi", "Son", "Gandak"],
    options_hi: ["गंगा", "कोसी", "सोन", "गंडक"],
    explanation: "The Kosi is called the 'Sorrow of Bihar' for its frequent devastating floods and its shifting course across north Bihar.",
    explanation_hi: "कोसी को उसकी बार-बार आने वाली विनाशकारी बाढ़ और उत्तर बिहार में मार्ग बदलने के कारण 'बिहार का शोक' कहा जाता है।",
    difficulty: "easy", sourceCitation: "Bihar Economic Survey 2024–25", correctRate: 73,
    responseId: "sr-2", yourVal: 1, correctVal: 1, attempted: true, correct: true, awarded: 2, time: 24,
  },
  {
    id: "frv-3", num: 3, section: "General Studies", type: "match_the_following", topic: "Ancient", subject: "History",
    text: "Match List-I (Scholar) with List-II (Field) and select the correct answer using the code given below:",
    text_hi: "सूची-I (विद्वान) का सूची-II (क्षेत्र) से मिलान कीजिए और नीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
    data: {
      list_1: ["a. Charaka", "b. Aryabhata", "c. Sushruta", "d. Brahmagupta"],
      list_2: ["1. Astronomy", "2. Surgery", "3. Medicine", "4. Mathematics"],
      list_1_hi: ["a. चरक", "b. आर्यभट", "c. सुश्रुत", "d. ब्रह्मगुप्त"],
      list_2_hi: ["1. खगोलशास्त्र", "2. शल्यचिकित्सा", "3. आयुर्विज्ञान", "4. गणित"],
    },
    options: ["a-3, b-1, c-2, d-4", "a-2, b-1, c-3, d-4", "a-3, b-4, c-2, d-1", "a-1, b-3, c-4, d-2"],
    options_hi: ["a-3, b-1, c-2, d-4", "a-2, b-1, c-3, d-4", "a-3, b-4, c-2, d-1", "a-1, b-3, c-4, d-2"],
    explanation: "Charaka — Medicine (3); Aryabhata — Astronomy (1); Sushruta — Surgery (2); Brahmagupta — Mathematics (4). So a-3, b-1, c-2, d-4.",
    explanation_hi: "चरक — आयुर्विज्ञान (3); आर्यभट — खगोलशास्त्र (1); सुश्रुत — शल्यचिकित्सा (2); ब्रह्मगुप्त — गणित (4)। अतः a-3, b-1, c-2, d-4।",
    difficulty: "hard", sourceCitation: "NCERT Ancient India", correctRate: 38,
    responseId: "sr-3", yourVal: 2, correctVal: 0, attempted: true, correct: false, awarded: -0.66, time: 71,
  },
  {
    id: "frv-4", num: 4, section: "CSAT (Aptitude)", type: "reasoning_aptitude", topic: "Quantitative/Numerical", subject: "Reasoning & Aptitude",
    text: "Find the missing term in the following number series:",
    text_hi: "निम्नलिखित संख्या श्रृंखला में लुप्त पद ज्ञात कीजिए:",
    data: { series: "2, 6, 12, 20, 30, ?", series_hi: "2, 6, 12, 20, 30, ?" },
    options: ["40", "42", "44", "46"],
    options_hi: ["40", "42", "44", "46"],
    explanation: "The differences run 4, 6, 8, 10, so the next is 12: 30 + 12 = 42 (the pattern is n² + n).",
    explanation_hi: "अंतर 4, 6, 8, 10 चलते हैं, अगला 12 है: 30 + 12 = 42 (पैटर्न n² + n है)।",
    difficulty: "medium", sourceCitation: "PYQ, 70th BPSC Prelims", correctRate: 55,
    responseId: "sr-4", yourVal: null, correctVal: 1, attempted: false, correct: false, awarded: 0, time: 0,
  },
];

const mkAttempt = (i, title, score, max, acc) => ({
  id: "fx-att-" + i,
  testId: "fx-test-" + (i % 6),
  title,
  series: "BPSC Prelims Test Series 2026 — Foundation Batch",
  date: iso(60 - i * 7),
  score,
  maxScore: max,
  scorePct: (score / max) * 100,
  totalQ: 100,
  correct: Math.round(acc),
  wrong: 100 - Math.round(acc) - 8,
  skipped: 8,
  accuracy: acc,
  percentile: 40 + i * 7,
  rank: 420 - i * 45,
  totalStudents: 980,
  timeSec: 5400 - i * 120,
  durationMin: 120,
  sections: [
    { name: "General Studies", score: score * 0.6, max: max * 0.6, correct: 30, wrong: 12, unattempted: 4 },
    { name: "CSAT (Aptitude)", score: score * 0.4, max: max * 0.4, correct: 20, wrong: 9, unattempted: 4 },
  ],
  topics: [
    { name: "Polity", subject: "Polity", correct: 12, total: 15, acc: 80, band: "strong" },
    { name: "Modern History", subject: "History", correct: 9, total: 15, acc: 60, band: "average" },
    { name: "Geography", subject: "Geography", correct: 5, total: 15, acc: 33, band: "weak" },
    { name: "Economy", subject: "Economy", correct: 7, total: 15, acc: 47, band: "weak" },
    { name: "Environment & Ecology", subject: "Environment & Ecology", correct: 11, total: 14, acc: 79, band: "strong" },
  ],
  review: FX_REVIEW_ROWS,
  answers: {},
});

export const FX_ATTEMPTS = [
  mkAttempt(0, "BPSC Prelims Mock 01 — Full Length", 88, 200, 52),
  mkAttempt(1, "Polity Sectional Test (Articles 1–150)", 104, 200, 58),
  mkAttempt(2, "BPSC Prelims Mock 02 — Full Length", 96, 200, 55),
  mkAttempt(3, "Modern History Sectional — Freedom Struggle", 122, 200, 64),
  mkAttempt(4, "CSAT Full Mock 01 — Aptitude & Comprehension", 138, 200, 71),
  mkAttempt(5, "BPSC Prelims Mock 03 — All India Grand Test", 151, 200, 76),
];

/* The result of the just-submitted dev paper (§7). submitAttempt returns this
   in fixtures mode so the result screen — breakdowns, per-question review, trend
   strip — renders without a backend. */
export const FX_EXAM_RESULT = {
  attemptId: "fx-att-live", testId: "fx-test-0",
  title: "BPSC Prelims Mock 04 — All India Grand Test",
  title_hi: "बीपीएससी प्रारंभिक मॉक 04 — अखिल भारतीय ग्रैंड टेस्ट",
  seriesTitle: "BPSC Prelims Test Series 2026",
  durationMin: 120, startedAt: iso(0),
  score: 3.34, maxScore: 8, scorePct: 41.75, accuracy: 50,
  attempted: 3, total: 4, unattempted: 1, correct: 1, wrong: 2, timeUsed: 147,
  sections: [
    { name: "General Studies", score: 0.68, max: 6, correct: 1, wrong: 2, unattempted: 0 },
    { name: "CSAT (Aptitude)", score: 0, max: 2, correct: 0, wrong: 0, unattempted: 1 },
  ],
  topics: [
    { name: "Polity", subject: "Polity", correct: 0, total: 1, acc: 0, band: "weak" },
    { name: "Geography", subject: "Geography", correct: 1, total: 1, acc: 100, band: "strong" },
    { name: "Ancient History", subject: "History", correct: 0, total: 1, acc: 0, band: "weak" },
    { name: "Number Series", subject: "Reasoning & Aptitude", correct: 0, total: 1, acc: 0, band: "weak" },
  ],
  difficultyStats: [
    { name: "easy", correct: 1, total: 1, acc: 100 },
    { name: "medium", correct: 0, total: 2, acc: 0 },
    { name: "hard", correct: 0, total: 1, acc: 0 },
  ],
  typeStats: [
    { name: "mcq", correct: 1, total: 1, acc: 100 },
    { name: "statement_based", correct: 0, total: 1, acc: 0 },
    { name: "match_the_following", correct: 0, total: 1, acc: 0 },
    { name: "reasoning_aptitude", correct: 0, total: 1, acc: 0 },
  ],
  review: FX_REVIEW_ROWS,
  percentile: 47.5, rank: 512, totalStudents: 980, peerAvg: 44.2, peerBest: 92.5,
};

/* The My-Performance drill-down (§7): the questions the student got wrong. */
export const FX_MY_REVIEW = FX_REVIEW_ROWS.filter((r) => r.attempted && !r.correct);

export const FX_TESTS = [
  { id: "fx-test-0", title: "BPSC Prelims Mock 04 — All India Grand Test", seriesTitle: "BPSC Prelims Test Series 2026", durationMin: 120, totalQuestions: 100, totalMarks: 200, isFree: false, isPublished: true, scheduledFor: null, sections: [{ id: "s1", name: "GS", questionIds: ["q1", "q2"] }] },
  { id: "fx-test-1", title: "Current Affairs — June 2026 Monthly Compilation Test", seriesTitle: "Monthly CA Series", durationMin: 45, totalQuestions: 50, totalMarks: 100, isFree: true, isPublished: true, scheduledFor: null, sections: [{ id: "s1", name: "CA", questionIds: ["q3"] }] },
  { id: "fx-test-2", title: "CSAT Full Mock 02", seriesTitle: "CSAT Series", durationMin: 120, totalQuestions: 80, totalMarks: 200, isFree: false, isPublished: true, scheduledFor: null, sections: [{ id: "s1", name: "CSAT", questionIds: ["q4"] }] },
  { id: "fx-test-3", title: "Bihar Special — State GK Sprint", seriesTitle: "BPSC Prelims Test Series 2026", durationMin: 60, totalQuestions: 60, totalMarks: 120, isFree: false, isPublished: true, scheduledFor: new Date(Date.now() + 6 * day).toISOString(), sections: [] },
  { id: "fx-test-4", title: "Environment & Ecology Sectional", seriesTitle: "Sectional Series", durationMin: 45, totalQuestions: 40, totalMarks: 80, isFree: false, isPublished: true, scheduledFor: new Date(Date.now() + 13 * day).toISOString(), sections: [] },
  { id: "fx-test-5", title: "अखिल भारतीय ग्रैंड टेस्ट — हिन्दी माध्यम", seriesTitle: "Grand Test Series", durationMin: 120, totalQuestions: 100, totalMarks: 200, isFree: false, isPublished: false, scheduledFor: null, sections: [] },
];

export const FX_MATERIALS = [
  { id: "fx-m1", title: "Polity NCERT — Quick Revision Notes (Class 9–12 consolidated)", subject: "Polity", type: "pdf", url: "https://example.com/a.pdf", isFree: true, isPublished: true },
  { id: "fx-m2", title: "Modern History One-Liner Capsule", subject: "History", type: "note", url: "https://example.com/b", isFree: true, isPublished: true },
  { id: "fx-m3", title: "Geography Mapping — Video Series", subject: "Geography", type: "video", url: "https://example.com/c", isFree: false, isPublished: true },
  { id: "fx-m4", title: "Economic Survey 2026 — Key Highlights", subject: "Economy", type: "pdf", url: "https://example.com/d.pdf", isFree: false, isPublished: true },
  { id: "fx-m5", title: "CSAT Reasoning — Shortcut Tricks", subject: "Reasoning & Aptitude", type: "video", url: "https://example.com/e", isFree: true, isPublished: true },
];

export const FX_ENROLLMENTS = [
  { id: "fx-e1", plan_code: "prelims-2026", batch_id: null, status: "active", expires_at: new Date(Date.now() + 300 * day).toISOString(), enrolled_at: iso(60), plans: { name: "UPSC Prelims 2027 — Full Test Series", exam_category: "upsc" }, batches: null },
  { id: "fx-e2", plan_code: "bpsc-2026", batch_id: null, status: "active", expires_at: new Date(Date.now() + 5 * day).toISOString(), enrolled_at: iso(120), plans: { name: "BPSC Prelims 2026 — Full Test Series", exam_category: "bpsc" }, batches: null },
];

export const FX_ACTIVITY = Array.from({ length: 84 }, (_, i) => ({
  date: new Date(Date.now() - (83 - i) * day),
  count: [0, 1, 0, 2, 3, 1, 4, 0, 2][i % 9],
}));

export const FX_LEADERBOARD = [
  { student_id: "fx-a", name: "Ananya Mishra", avatar_url: null, tests_taken: 11, avg_pct: 78.5, best_pct: 88, avg_accuracy: 74, rank: 1 },
  { student_id: "fx-b", name: "Rohan Gupta", avatar_url: null, tests_taken: 12, avg_pct: 76.0, best_pct: 85, avg_accuracy: 71, rank: 2 },
  { student_id: "fx-c", name: "Sneha Kumari", avatar_url: null, tests_taken: 10, avg_pct: 74.2, best_pct: 83, avg_accuracy: 70, rank: 3 },
  { student_id: "fx-user", name: "Chandrashekhar Venkataraman Subrahmanyan", avatar_url: null, tests_taken: 6, avg_pct: 62.7, best_pct: 76, avg_accuracy: 63, rank: 4 },
  { student_id: "fx-e", name: "Kritika Sharma", avatar_url: null, tests_taken: 11, avg_pct: 60.1, best_pct: 72, avg_accuracy: 61, rank: 5 },
  { student_id: "fx-f", name: "विवेक आनंद", avatar_url: null, tests_taken: 8, avg_pct: 58.0, best_pct: 70, avg_accuracy: 59, rank: 6 },
];

export const FX_NOTIFICATIONS = [
  { id: "fx-n1", kind: "success", title: "Result published — BPSC Prelims Mock 03", body: "You scored in the 76th percentile. Your detailed analysis is ready.", read_at: null, created_at: iso(1) },
  { id: "fx-n2", kind: "test", title: "All-India Grand Test 01 is scheduled", body: "Starts in 6 days — set a reminder so you don't miss it.", read_at: null, created_at: iso(2) },
  { id: "fx-n3", kind: "material", title: "New material added", body: "Economic Survey 2026 — Key Highlights", read_at: iso(3), created_at: iso(3) },
];

export const FX_QUESTIONS = Array.from({ length: 12 }, (_, i) => ({
  id: "fx-q" + i,
  examCategory: "bpsc",
  subject: ["Polity", "History", "Geography", "Economy", "Environment & Ecology"][i % 5],
  topic: ["Constitutional provisions", "Modern", "Physical", "Macroeconomic concepts", "Conservation & Policy"][i % 5],
  type: ["mcq", "multiple", "numerical"][i % 3],
  difficulty: ["easy", "medium", "hard"][i % 3],
  body: "Which Article of the Indian Constitution was described by Dr. B. R. Ambedkar as the 'heart and soul' of the Constitution, and why does that description matter for the enforcement of Fundamental Rights?",
  options: [
    { id: "o1", body: "Article 14", isCorrect: false },
    { id: "o2", body: "Article 19", isCorrect: false },
    { id: "o3", body: "Article 32", isCorrect: true },
    { id: "o4", body: "Article 21", isCorrect: false },
  ],
  numericAnswer: i % 3 === 2 ? 36 : null,
  numericTolerance: 0.01,
  marksCorrect: 2,
  marksWrong: 0.66,
  explanation: "Article 32 lets citizens move the Supreme Court directly to enforce Fundamental Rights.",
  tags: [],
  createdAt: iso(i),
}));

export const FX_STUDENTS = Array.from({ length: 8 }, (_, i) => ({
  id: "fx-s" + i,
  name: ["Chandrashekhar Venkataraman Subrahmanyan", "Rahul Verma", "Sneha Kumari", "अनुपम कुमार", "Amit Raj", "Pooja Singh", "Vikash Anand", "Dharmendra Das"][i],
  email: ["a.very.long.student.address@gmail.com", "rahul.v@gmail.com", "sneha.k@gmail.com", "anupam@gmail.com", "amit.raj@gmail.com", "pooja.s@gmail.com", "vikash.a@gmail.com", "dd@gmail.com"][i],
  phone: i % 2 ? "+91 98765 4321" + i : "",
  joined: iso(180 - i * 12),
  target: "UPSC Prelims 2026",
  attempts: [12, 18, 7, 9, 21, 0, 3, 14][i],
  avg: [64, 78, 52, 71, 83, 0, 41, 69][i],
  enrolled: i % 3 !== 2,
}));

export const FX_PAYMENTS = Array.from({ length: 7 }, (_, i) => ({
  id: "fx-p" + i,
  name: FX_STUDENTS[i].name,
  email: FX_STUDENTS[i].email,
  item: ["prelims-2026", "bpsc-2026", "uppcs-2026"][i % 3],
  amount: [499, 399, 399, 499, 399, 499, 399][i],
  status: ["paid", "paid", "failed", "paid", "paid", "refunded", "paid"][i],
  method: ["upi", "card", "netbanking", "upi", "upi", "card", "wallet"][i],
  ref: "pay_Nq" + i + "XyZaBcDeFg",
  date: iso(30 - i * 4),
}));

export const FX_BUNDLES = [
  { code: "prelims-2026", name: "UPSC Prelims 2026 — Full Test Series", exam: "upsc", tagline: "Complete GS + CSAT coverage with All-India ranking", description: "", price: 499, mrp: 999, durationDays: 365, features: ["30 full-length mock tests", "Detailed solutions"], isActive: true, sortOrder: 1 },
  { code: "bpsc-2026", name: "BPSC Prelims 2026 — Full Test Series", exam: "bpsc", tagline: "Bihar-focused GS with current affairs depth", description: "", price: 399, mrp: 799, durationDays: 365, features: ["20 mock tests"], isActive: true, sortOrder: 2 },
  { code: "uppcs-2026", name: "UPPCS Prelims 2026 — Full Test Series", exam: "uppcs", tagline: "UP-focused GS with CSAT practice", description: "", price: 399, mrp: 799, durationDays: 365, features: ["20 mock tests"], isActive: false, sortOrder: 3 },
];

export const FX_EXAM = {
  id: "fx-test-0",
  title: "BPSC Prelims Mock 04 — All India Grand Test",
  seriesTitle: "BPSC Prelims Test Series 2026",
  durationSec: 120 * 60,
  durationMin: 120,
  shuffleQuestions: true,
  shuffleOptions: true,
  sections: [
    {
      name: "General Studies",
      questions: Array.from({ length: 8 }, (_, i) => ({
        id: "fx-eq" + i,
        topic: ["Constitutional provisions", "Modern", "Physical", "Macroeconomic concepts"][i % 4],
        subject: ["Polity", "History", "Geography", "Economy"][i % 4],
        type: i === 3 ? "multiple" : "mcq",
        marks: 2,
        negative: 0.66,
        text: "Which Article of the Indian Constitution was described by Dr. B. R. Ambedkar as the 'heart and soul' of the Constitution, and why does that description matter for the enforcement of Fundamental Rights in practice?",
        text_hi: "भारतीय संविधान के किस अनुच्छेद को डॉ. बी. आर. आंबेडकर ने संविधान की आत्मा और हृदय कहा था, और व्यवहार में मौलिक अधिकारों के प्रवर्तन के लिए यह कथन क्यों महत्वपूर्ण है?",
        options: [
          { id: "fx-eq" + i + "-a", body: "Article 14 — Equality before law", body_hi: "अनुच्छेद 14 — विधि के समक्ष समता" },
          { id: "fx-eq" + i + "-b", body: "Article 19 — Freedom of speech and expression", body_hi: "अनुच्छेद 19 — वाक् एवं अभिव्यक्ति की स्वतंत्रता" },
          { id: "fx-eq" + i + "-c", body: "Article 32 — Right to Constitutional Remedies", body_hi: "अनुच्छेद 32 — संवैधानिक उपचारों का अधिकार" },
          { id: "fx-eq" + i + "-d", body: "Article 21 — Protection of life and personal liberty", body_hi: "अनुच्छेद 21 — प्राण एवं दैहिक स्वतंत्रता का संरक्षण" },
        ],
      })),
    },
    {
      name: "CSAT (Aptitude)",
      questions: Array.from({ length: 4 }, (_, i) => ({
        id: "fx-ec" + i,
        topic: "Quantitative/Numerical",
        subject: "Reasoning & Aptitude",
        type: i === 1 ? "numerical" : "mcq",
        marks: 2.5,
        negative: i === 1 ? 0 : 0.83,
        text: "A train 150 metres long crosses a stationary pole in 15 seconds. What is the speed of the train in km/h?",
        options: i === 1 ? [] : [
          { id: "fx-ec" + i + "-a", body: "24 km/h" },
          { id: "fx-ec" + i + "-b", body: "30 km/h" },
          { id: "fx-ec" + i + "-c", body: "36 km/h" },
          { id: "fx-ec" + i + "-d", body: "45 km/h" },
        ],
      })),
    },
    {
      name: "BPSC Formats",
      questions: [
        {
          id: "fx-eb0", subject: "Polity", topic: "Constitutional provisions", type: "statement_based", marks: 2, negative: 0.66,
          text: "Consider the following statements about the Fundamental Rights in the Indian Constitution:",
          text_hi: "भारतीय संविधान में मौलिक अधिकारों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
          data: {
            statements: [
              "The Right to Constitutional Remedies is itself a Fundamental Right.",
              "The Right to Property is a Fundamental Right under Part III.",
              "The Right to Education was inserted as Article 21A by the 86th Amendment.",
            ],
            statements_hi: [
              "संवैधानिक उपचारों का अधिकार स्वयं एक मौलिक अधिकार है।",
              "संपत्ति का अधिकार भाग-III के अंतर्गत एक मौलिक अधिकार है।",
              "शिक्षा का अधिकार 86वें संशोधन द्वारा अनुच्छेद 21क के रूप में जोड़ा गया।",
            ],
            closing: "Which of the statements given above is/are correct?",
            closing_hi: "उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
          },
          options: [
            { id: "fx-eb0-a", body: "Only 1 and 3", body_hi: "केवल 1 और 3" },
            { id: "fx-eb0-b", body: "Only 2 and 3", body_hi: "केवल 2 और 3" },
            { id: "fx-eb0-c", body: "Only 1 and 2", body_hi: "केवल 1 और 2" },
            { id: "fx-eb0-d", body: "All of the above", body_hi: "उपर्युक्त सभी" },
          ],
        },
        {
          id: "fx-eb1", subject: "History", topic: "Ancient", type: "match_the_following", marks: 2, negative: 0.66,
          text: "Match List-I (Scholar) with List-II (Field) and select the correct answer using the code given below:",
          text_hi: "सूची-I (विद्वान) का सूची-II (क्षेत्र) से मिलान कीजिए और नीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
          data: {
            list_1: ["a. Charaka", "b. Aryabhata", "c. Sushruta", "d. Brahmagupta"],
            list_2: ["1. Astronomy", "2. Surgery", "3. Medicine", "4. Mathematics"],
            list_1_hi: ["a. चरक", "b. आर्यभट", "c. सुश्रुत", "d. ब्रह्मगुप्त"],
            list_2_hi: ["1. खगोलशास्त्र", "2. शल्यचिकित्सा", "3. आयुर्विज्ञान", "4. गणित"],
          },
          options: [
            { id: "fx-eb1-a", body: "a-3, b-1, c-2, d-4", body_hi: "a-3, b-1, c-2, d-4" },
            { id: "fx-eb1-b", body: "a-2, b-1, c-3, d-4", body_hi: "a-2, b-1, c-3, d-4" },
            { id: "fx-eb1-c", body: "a-3, b-4, c-2, d-1", body_hi: "a-3, b-4, c-2, d-1" },
            { id: "fx-eb1-d", body: "a-1, b-3, c-4, d-2", body_hi: "a-1, b-3, c-4, d-2" },
          ],
        },
        {
          id: "fx-eb2", subject: "Geography", topic: "Physical", type: "assertion_reason", marks: 2, negative: 0.66,
          text: "Read the Assertion (A) and the Reason (R) below and choose the correct option:",
          text_hi: "नीचे दिए गए अभिकथन (A) और कारण (R) को पढ़िए और सही विकल्प चुनिए:",
          data: {
            assertion: "The Ganga is the longest river flowing within India.",
            reason: "The Ganga originates from the Gangotri glacier in Uttarakhand.",
            assertion_hi: "गंगा भारत के भीतर बहने वाली सबसे लंबी नदी है।",
            reason_hi: "गंगा का उद्गम उत्तराखंड में गंगोत्री हिमनद से होता है।",
          },
          options: [
            { id: "fx-eb2-a", body: "Both A and R are true and R is the correct explanation of A", body_hi: "A और R दोनों सही हैं तथा R, A की सही व्याख्या है" },
            { id: "fx-eb2-b", body: "Both A and R are true but R is NOT the correct explanation of A", body_hi: "A और R दोनों सही हैं परन्तु R, A की सही व्याख्या नहीं है" },
            { id: "fx-eb2-c", body: "A is true but R is false", body_hi: "A सही है परन्तु R गलत है" },
            { id: "fx-eb2-d", body: "A is false but R is true", body_hi: "A गलत है परन्तु R सही है" },
          ],
        },
        {
          // UPSC wording of the same format (question_data.ar_labels = "statement").
          id: "fx-eb2u", subject: "Polity", topic: "Parliament & State Legislature", type: "assertion_reason", marks: 2, negative: 0.66,
          text: "Consider the following statements:",
          data: {
            assertion: "The Rajya Sabha is not subject to dissolution.",
            reason: "One-third of the members of the Rajya Sabha retire every second year.",
            ar_labels: "statement",
            closing: "Which one of the following is correct in respect of the above statements?",
            fixed_option_order: true,
          },
          options: [
            { id: "fx-eb2u-a", body: "Both Statement-I and Statement-II are correct and Statement-II is the correct explanation for Statement-I" },
            { id: "fx-eb2u-b", body: "Both Statement-I and Statement-II are correct and Statement-II is not the correct explanation for Statement-I" },
            { id: "fx-eb2u-c", body: "Statement-I is correct but Statement-II is incorrect" },
            { id: "fx-eb2u-d", body: "Statement-I is incorrect but Statement-II is correct" },
          ],
        },
        {
          // UPSC 2025 three-statement form (question_data.reason_2 = Statement-III).
          id: "fx-eb2u3", subject: "Environment & Ecology", topic: "Pollution, Waste & Resources", type: "assertion_reason", marks: 2, negative: 0.66,
          text: "Consider the following statements:",
          data: {
            assertion: "A circular economy reduces the emission of greenhouse gases.",
            reason: "A circular economy reduces the use of raw materials as inputs.",
            reason_2: "A circular economy reduces wastage in the production process.",
            ar_labels: "statement",
            closing: "Which one of the following is correct in respect of the above statements?",
            fixed_option_order: true,
          },
          options: [
            { id: "fx-eb2u3-a", body: "Both Statement II and Statement III are correct and both of them explain Statement I" },
            { id: "fx-eb2u3-b", body: "Both Statement II and Statement III are correct but only one of them explains Statement I" },
            { id: "fx-eb2u3-c", body: "Only one of the Statements II and III is correct and that explains Statement I" },
            { id: "fx-eb2u3-d", body: "Neither Statement II nor Statement III is correct" },
          ],
        },
        {
          // UPSC 2025-style Roman-numbered statements (question_data.numbering = "roman").
          id: "fx-eb0r", subject: "Environment & Ecology", topic: "Climate Science & Mitigation", type: "statement_based", marks: 2, negative: 0.66,
          text: "With reference to the planet Earth, consider the following statements:",
          data: {
            statements: [
              "Marine phytoplankton and photosynthetic bacteria produce a large share of the world's oxygen.",
              "Methane has a higher 100-year global warming potential than nitrous oxide.",
              "Ground-level ozone forms from nitrogen oxides and volatile organic compounds in sunlight.",
            ],
            closing: "Which of the statements given above is/are correct?",
            numbering: "roman",
            fixed_option_order: true,
          },
          options: [
            { id: "fx-eb0r-a", body: "I and II only" },
            { id: "fx-eb0r-b", body: "I and III only" },
            { id: "fx-eb0r-c", body: "II and III only" },
            { id: "fx-eb0r-d", body: "I, II and III" },
          ],
        },
        {
          // UPSC concept-linkage form: Roman statements, then a numbered list of principles (data.sublist).
          id: "fx-eb0l", subject: "Polity", topic: "Constitutional Framework", type: "statement_based", marks: 2, negative: 0.66,
          text: "Consider the following statements:",
          text_hi: "निम्नलिखित कथनों पर विचार कीजिए:",
          data: {
            numbering: "roman",
            statements: [
              "Parliament can amend any part of the Constitution, but not so as to destroy its basic structure.",
              "A law can be struck down by the courts if it violates a Fundamental Right.",
            ],
            statements_hi: [
              "संसद संविधान के किसी भी भाग में संशोधन कर सकती है, पर उसके मूल ढाँचे को नष्ट करने वाला नहीं।",
              "मौलिक अधिकार का उल्लंघन करने वाले क़ानून को न्यायालय रद्द कर सकते हैं।",
            ],
            sublist_lead: "The above statements reflect which of the following?",
            sublist_lead_hi: "उपर्युक्त कथन निम्नलिखित में से किसे दर्शाते हैं?",
            sublist: ["Parliamentary sovereignty", "Constitutional supremacy"],
            sublist_hi: ["संसदीय संप्रभुता", "संवैधानिक सर्वोच्चता"],
            closing: "Select the correct answer using the code given below:",
            closing_hi: "नीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
          },
          options: [
            { id: "fx-eb0l-a", body: "1 only", body_hi: "केवल 1" },
            { id: "fx-eb0l-b", body: "2 only", body_hi: "केवल 2" },
            { id: "fx-eb0l-c", body: "Both 1 and 2", body_hi: "1 और 2 दोनों" },
            { id: "fx-eb0l-d", body: "Neither 1 nor 2", body_hi: "न तो 1, न ही 2" },
          ],
        },
        {
          id: "fx-eb3", subject: "Reasoning & Aptitude", topic: "Quantitative/Numerical", type: "reasoning_aptitude", marks: 2, negative: 0.66,
          text: "Find the missing term in the following number series:",
          text_hi: "निम्नलिखित संख्या श्रृंखला में लुप्त पद ज्ञात कीजिए:",
          data: { series: "2, 6, 12, 20, 30, ?", series_hi: "2, 6, 12, 20, 30, ?" },
          options: [
            { id: "fx-eb3-a", body: "40" },
            { id: "fx-eb3-b", body: "42" },
            { id: "fx-eb3-c", body: "44" },
            { id: "fx-eb3-d", body: "46" },
          ],
        },
      ],
    },
  ],
};

/* Referral fixtures. Long masked names and a mix of converted/unconverted so
   the share card and the admin table can be measured with realistic content. */
export const FX_REFERRAL_STATS = { code: "K7MTQ2XR", total: 4, paid: 3, pending: 1, bonus: 99 };

export const FX_REFERRAL_LIST = [
  { name: "Shubhangi P.", joined: "2026-08-14T09:12:00Z", paid: true, status: "credited" },
  { name: "Ravi K.", joined: "2026-08-11T17:40:00Z", paid: true, status: "credited" },
  { name: "Aparajita B.", joined: "2026-08-06T06:05:00Z", paid: true, status: "credited" },
  { name: "Aspirant", joined: "2026-07-29T13:20:00Z", paid: false, status: "pending" },
];

export const FX_ADMIN_REFERRALS = Array.from({ length: 9 }, (_, i) => ({
  id: "fx-ref-" + i,
  referrer: ["Praveen Priyadarshee", "Anupam Kumar Chaturvedi", "Sneha R."][i % 3],
  referrerEmail: ["praveen.priyadarshee.upsc@gmail.com", "anupam.chaturvedi2000@gmail.com", "sneha.r@gmail.com"][i % 3],
  referred: ["Shubhangi Prasad", "Ravi Kumar Singh", "Aparajita Bhattacharya"][i % 3],
  referredEmail: ["shubhangi.prasad.aspirant@gmail.com", "ravi.k.singh@gmail.com", "aparajita.b@gmail.com"][i % 3],
  code: ["K7MTQ2XR", "9PDWNH3S", "TZ4KRB6M"][i % 3],
  paid: i % 3 === 0,
  status: i % 3 === 0 ? "pending" : "pending",
  at: new Date(Date.now() - i * 3 * 86400000).toISOString(),
}));

/* Wallet fixtures — a balance below the withdrawal threshold and no active
   course, so the blocked-eligibility copy is what gets measured. */
export const FX_WALLET = {
  // Deliberately consistent with FX_WALLET_TX below: three credited bonuses
  // (297) minus one 100 withdrawal = 197. The reversed line counts toward
  // neither, which is the whole point of keeping it in the ledger.
  balance: 197, lifetime: 297, pending: 0, bonus: 99,
  minWithdraw: 500, canWithdraw: false, hasActiveCourse: false,
};

const BONUS_NOTE = "Referral bonus — a friend you invited bought a test series";
export const FX_WALLET_TX = [
  { id: "w1", amount: 99,   type: "referral_bonus", status: "completed", note: BONUS_NOTE, at: "2026-08-20T10:15:00Z" },
  { id: "w2", amount: -100, type: "withdrawal",     status: "completed", note: "Withdrawal to UPI", at: "2026-08-16T08:00:00Z" },
  { id: "w3", amount: 99,   type: "referral_bonus", status: "completed", note: BONUS_NOTE, at: "2026-08-14T09:12:00Z" },
  { id: "w4", amount: 99,   type: "referral_bonus", status: "completed", note: BONUS_NOTE, at: "2026-08-11T17:40:00Z" },
  { id: "w5", amount: 99,   type: "referral_bonus", status: "reversed",  note: BONUS_NOTE, at: "2026-08-02T11:05:00Z" },
];

/* Feedback fixtures — a mix of statuses so the queue and the student's own
   list can both be measured with something realistic in them. */
export const FX_MY_FEEDBACK = [
  { id: "f1", kind: "bug", rating: 4, status: "resolved",
    message: "On my phone the timer sat on top of the question text in the last section.",
    reply: "Fixed on 22 Aug — the header no longer overlaps at narrow widths. Thank you for the exact detail.",
    at: "2026-08-19T11:20:00Z" },
  { id: "f2", kind: "content", rating: 5, status: "seen",
    message: "Polity paper 3, question 14 — the explanation cites Article 21 but the answer key says 32.",
    reply: "", at: "2026-08-21T08:05:00Z" },
];

export const FX_ADMIN_FEEDBACK = Array.from({ length: 7 }, (_, i) => ({
  id: "af" + i,
  name: ["Shubhangi Prasad", "Ravi Kumar Singh", "Aparajita Bhattacharya"][i % 3],
  email: ["shubhangi.prasad.aspirant@gmail.com", "ravi.k.singh@gmail.com", "aparajita.b@gmail.com"][i % 3],
  kind: ["bug", "content", "suggestion", "payment", "test", "general"][i % 6],
  rating: (i % 5) + 1,
  message: [
    "On my phone the timer sat on top of the question text in the last section.",
    "Polity paper 3, question 14 — the explanation cites Article 21 but the answer key says 32.",
    "Please add a Hindi option for the CSAT papers too.",
    "Paid yesterday but the series did not unlock for about ten minutes.",
    "The rank showed as estimated even after 40 people had attempted.",
  ][i % 5],
  page: ["/exam", "/tests", "/", "/join", "/performance"][i % 5],
  status: ["new", "seen", "in_progress", "resolved"][i % 4],
  reply: i % 4 === 3 ? "Fixed and deployed. Thanks for the report." : "",
  at: new Date(Date.now() - i * 2 * 86400000).toISOString(),
}));

/* ---------------------------------------------------------------- mains --
   Essay PYQs are UPSC's real topics; toppers, ranks and marks are invented,
   in this file's usual awkward lengths. Themes are named like the categories
   our PYQ sheet carries. Copies 1 and 3 are hosted (their pages
   are drawn below as SVG answer-booklet pages); copy 2 is a link copy. */

const TH = (id, name, nameHi = "") => ({ id, slug: id, name, nameHi, parentId: null, sortOrder: 0 });
export const FX_ESSAY_THEMES = [
  TH("th-happy", "Happiness", "सुख"),
  TH("th-self", "Self-discovery or journey of life", "आत्म-खोज और जीवन-यात्रा"),
  TH("th-wisdom", "Knowledge & Wisdom", "ज्ञान और विवेक"),
  TH("th-mind", "Mindfulness or inner work or tranquility"),
  TH("th-justice", "Justice", "न्याय"),
  TH("th-power", "Power", "शक्ति"),
  TH("th-rise", "Rising every time we fall/failure/facing challenges"),
  TH("th-excel", "Excellence or Perfection"),
  TH("th-env", "Environment Sustainability", "पर्यावरणीय स्थिरता"),
  TH("th-tech", "Technology/AI", "प्रौद्योगिकी और AI"),
  TH("th-edu", "Education", "शिक्षा"),
  TH("th-fem", "Feminism & Patriarchy"),
];

const PQ = (id, year, topic, themes, essayCount = 0, exactCount = 0, topicHi = "") =>
  ({ id, year, qNo: null, section: "", topic, topicHi, isPublished: true,
     themes: themes.map(([tid, c]) => ({ id: tid, confidence: c })), essayCount, exactCount });

export const FX_ESSAY_PYQS = [
  PQ("pq-1", 2025, "Truth knows no color.", [["th-justice", 70]]),
  PQ("pq-2", 2025, "The supreme art of war is to subdue the enemy without fighting.", [["th-power", 80], ["th-wisdom", 60]], 2, 0),
  PQ("pq-3", 2025, "Best lessons are learnt through bitter experiences.", [["th-rise", 90], ["th-self", 70]], 1, 0),
  PQ("pq-4", 2025, "Contentment is natural wealth; luxury is artificial poverty.", [["th-happy", 90], ["th-mind", 70]]),
  PQ("pq-5", 2024, "There is no path to happiness; Happiness is the path.", [["th-happy", 90], ["th-self", 70]], 3, 2,
     "सुख का कोई मार्ग नहीं है; सुख स्वयं मार्ग है।"),
  PQ("pq-6", 2024, "Forests precede civilizations and deserts follow them.", [["th-env", 90]]),
  PQ("pq-7", 2024, "The empires of the future will be the empires of the mind.", [["th-wisdom", 90], ["th-tech", 60]]),
  PQ("pq-8", 2023, "Thinking is like a game; it does not begin unless there is an opposite team.", [["th-wisdom", 80]]),
  PQ("pq-9", 2022, "A ship in harbour is safe, but that is not what ship is for.", [["th-rise", 85], ["th-self", 70]], 1, 0),
  PQ("pq-10", 2019, "Courage to accept and dedication to improve are two keys to success.", [["th-excel", 90], ["th-rise", 70]], 2, 0),
  PQ("pq-11", 2017, "Destiny of a nation is shaped in its classrooms.", [["th-edu", 90]]),
  PQ("pq-12", 2015, "Lending hands to someone is better than giving a dole.", [["th-justice", 80]]),
  PQ("pq-13", 2015, "Education without values, as useful as it is, seems rather to make a man more clever devil.",
     [["th-edu", 90], ["th-justice", 60]]),
  PQ("pq-14", 2021, "Hand that rocks the cradle rules the world.", [["th-fem", 90]]),
];

const TOP = {
  t1: { id: "tp-1", name: "Aishwaryalakshmi Venkatasubramanian", rank: 7, cseYear: 2024, essayMarks: 151 },
  t2: { id: "tp-2", name: "Raghvendra Pratap Singh Chauhan", rank: 112, cseYear: 2023, essayMarks: 128 },
  t3: { id: "tp-3", name: "Zoya Khan", rank: 289, cseYear: 2025, essayMarks: null },
};
const COPY = {
  c1: { copyId: "fxc-1", source: "Vision IAS", title: "Essay test 12", writtenYear: 2024, sourceUrl: "", pageCount: 27, hosted: true, isFree: true },
  c2: { copyId: "fxc-2", source: "Forum IAS", title: "Mains guidance copy 3", writtenYear: 2023, sourceUrl: "https://example.org/forum-ias/sample-copy-3.pdf", pageCount: 0, hosted: false, isFree: false },
  c3: { copyId: "fxc-3", source: "Next IAS", title: "Essay practice 4", writtenYear: 2025, sourceUrl: "", pageCount: 19, hosted: true, isFree: false },
};
// Sample essay texts for the harness: original placeholder prose, not taken
// from any copy.
const FX_TEXTS = {
  "fa-1": "Happiness is often described as a destination: a promotion, a house, a result day. Yet people who reach these places rarely stay happy for long, because the mind quickly resets to its old level.\n\n"
    + "The Buddha's middle path, Aristotle's eudaimonia and the Gita's idea of action without attachment all point the other way: happiness is the quality of the walk, not the view at the end.\n\n"
    + "For a society, this means measuring well-being as well as income. Bhutan's Gross National Happiness index and a growing focus on mental health show the idea moving from philosophy into policy.\n\n"
    + "The path, then, is the happiness: curiosity, kindness and steady effort, practised daily.",
  "fa-2": "In 1930, a march to the sea for a pinch of salt shook an empire that armies could not. Persuasion works because it changes what people want, while force only changes what they do while watched.\n\n"
    + "At home, sanitation campaigns succeeded where fines alone had failed. Abroad, soft power through culture, yoga and diaspora goodwill opens doors that pressure keeps shut.\n\n"
    + "Force still has a place against those who will not be persuaded, but it buys time, not consent. Lasting change is talked into being.",
  "fa-4": "A batter who fails in the nets on Monday and keeps practising until Friday is not lucky when the century comes. Champions are made by the willingness to be wrong many times before being right once.\n\n"
    + "In public life too, missions improve through trial, error and correction rather than a perfect first plan.\n\n"
    + "The lesson for a student is simple: keep playing until you get it right, and treat each mistake as information.",
};
const fxWords = (s) => (s ? (s.match(/\S+/g) || []).length : null);
const ANS = (answerId, copy, topper, question, startPage, endPage, links) => ({
  answerId, paper: "essay", paperLabel: "", question, startPage, endPage, ...copy, isPublished: true, topper, links,
  words: fxWords(FX_TEXTS[answerId]),
});

export function fxEssayText(answerId) {
  return FX_TEXTS[answerId] ? { body: FX_TEXTS[answerId], source: "typed transcript", updatedAt: "2026-11-08T00:00:00Z" } : null;
}
export function fxSearchEssayIds(needle) {
  const n = needle.toLowerCase();
  return Object.keys(FX_TEXTS).filter((id) => FX_TEXTS[id].toLowerCase().includes(n));
}
const FX_ANSWERS = [
  ANS("fa-1", COPY.c1, TOP.t1, "There is no path to happiness. Happiness is the path.", 3, 14, [["pq-5", "exact", 100]]),
  ANS("fa-2", COPY.c1, TOP.t1, "Gentle persuasion succeeds where force fails.", 15, 27, [["pq-2", "related", 85]]),
  ANS("fa-3", COPY.c2, TOP.t2, "There is no path to happiness; happiness is the path.", 17, null, [["pq-5", "exact", 100]]),
  ANS("fa-4", COPY.c2, TOP.t2, "Champions keep playing until they get it right.", 5, null, [["pq-10", "related", 90], ["pq-3", "related", 60]]),
  ANS("fa-5", COPY.c3, TOP.t3, "Joy is the simplest form of gratitude.", 2, 10, [["pq-5", "related", 70]]),
  ANS("fa-6", COPY.c3, TOP.t3, "A smooth sea never made a skilled sailor.", 11, 19, [["pq-9", "related", 90], ["pq-10", "related", 75], ["pq-2", "related", 55]]),
];

export function fxLibrary({ sort = "marks", year = null, q = "", offset = 0, limit = 24 } = {}) {
  const needle = q.trim().toLowerCase();
  let list = FX_ANSWERS.filter((a) => (!year || a.writtenYear === year)
    && (!needle || a.question.toLowerCase().includes(needle) || a.topper.name.toLowerCase().includes(needle)
      || (FX_TEXTS[a.answerId] || "").toLowerCase().includes(needle)));
  list = list.slice().sort((a, b) => sort === "marks"
    ? (b.topper.essayMarks ?? -1) - (a.topper.essayMarks ?? -1) || b.writtenYear - a.writtenYear
    : sort === "oldest" ? a.writtenYear - b.writtenYear : b.writtenYear - a.writtenYear);
  return { items: list.slice(offset, offset + limit).map((a) => ({ ...a, links: undefined })), total: list.length };
}

export function fxLibraryYears() {
  return [...new Set(FX_ANSWERS.map((a) => a.writtenYear))].sort((a, b) => b - a);
}

export function fxEssaysForPyq(pyqId) {
  return FX_ANSWERS.flatMap(({ links, ...a }) =>
    links.filter(([p]) => p === pyqId).map(([, kind, confidence]) => ({ ...a, kind, confidence })));
}

export function fxAdminCopies({ q = "" } = {}) {
  const needle = q.trim().toLowerCase();
  const items = Object.values(COPY).map((c) => {
    const answers = FX_ANSWERS.filter((a) => a.copyId === c.copyId);
    return {
      id: c.copyId, source: c.source, title: c.title, writtenYear: c.writtenYear, sourceUrl: c.sourceUrl,
      pageCount: c.pageCount, hosted: c.hosted, isFree: c.isFree, isPublished: true,
      topper: answers[0].topper, answerCount: answers.length,
    };
  }).filter((c) => !needle || c.topper.name.toLowerCase().includes(needle));
  return { items, total: items.length };
}

export function fxCopyAnswers(copyId) {
  return FX_ANSWERS.filter((a) => a.copyId === copyId).map((a) => ({
    id: a.answerId, paper: "essay", paperLabel: "", question: a.question,
    startPage: a.startPage ?? "", endPage: a.endPage ?? "",
    links: a.links.map(([pyqId, kind, confidence]) => ({ pyqId, kind, confidence })),
  }));
}

/* A ruled answer-booklet page with wavy "handwriting", page number and a
   heading on the pages where a fixture essay starts. Deterministic per
   (copy, page), so a page looks the same every time it is drawn. */
export function fxPageImage(copyId, page) {
  let seed = [...`${copyId}:${page}`].reduce((h, ch) => (h * 31 + ch.charCodeAt(0)) >>> 0, 7);
  const rnd = () => ((seed = (seed * 1103515245 + 12345) >>> 0) / 4294967296);
  const W = 1240, H = 1754;
  const starts = FX_ANSWERS.filter((a) => a.copyId === copyId && a.startPage === page);
  const lines = [];
  for (let y = 300; y < H - 140; y += 58) {
    const x0 = 190, x1 = x0 + 640 + rnd() * 330;
    let d = `M${x0} ${y}`;
    for (let x = x0; x < x1; x += 34) d += ` q8 ${-10 - rnd() * 8} 17 0 t17 0`;
    lines.push(`<path d="${d}" fill="none" stroke="#24318f" stroke-width="3.2" stroke-linecap="round" opacity="${0.75 + rnd() * 0.2}"/>`);
  }
  const rules = Array.from({ length: Math.floor((H - 420) / 58) }, (_, i) =>
    `<line x1="160" x2="${W - 70}" y1="${312 + i * 58}" y2="${312 + i * 58}" stroke="#c9d6ea" stroke-width="2"/>`).join("");
  const heading = starts.map((a) =>
    `<text x="620" y="250" font-family="Georgia,serif" font-size="40" text-anchor="middle" fill="#1d2a6e" font-style="italic">${a.question.replace(/[<&>]/g, "").slice(0, 48)}</text>`).join("");
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">`
    + `<rect width="${W}" height="${H}" fill="#fffef9"/>`
    + `<rect x="60" y="60" width="${W - 120}" height="120" fill="none" stroke="#333" stroke-width="3"/>`
    + `<text x="${W / 2}" y="138" font-family="Georgia,serif" font-size="56" text-anchor="middle" fill="#222">ANSWER BOOKLET</text>`
    + `<line x1="150" x2="150" y1="200" y2="${H - 90}" stroke="#d24a5e" stroke-width="3"/>`
    + rules + heading + lines.join("")
    + `<text x="${W / 2}" y="${H - 50}" font-family="Georgia,serif" font-size="34" text-anchor="middle" fill="#555">— ${page} —</text>`
    + `</svg>`;
  return `data:image/svg+xml;charset=utf-8,${encodeURIComponent(svg)}`;
}
