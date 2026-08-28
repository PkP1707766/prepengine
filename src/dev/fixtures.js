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
    id: "frv-1", num: 1, section: "General Studies", type: "statement_based", topic: "Polity", subject: "Polity",
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
    id: "frv-2", num: 2, section: "General Studies", type: "mcq", topic: "Geography", subject: "Geography",
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
    id: "frv-3", num: 3, section: "General Studies", type: "match_the_following", topic: "Ancient History", subject: "Ancient History",
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
    id: "frv-4", num: 4, section: "CSAT (Aptitude)", type: "reasoning_aptitude", topic: "Number Series", subject: "Reasoning",
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
    { name: "Modern History", subject: "Modern History", correct: 9, total: 15, acc: 60, band: "average" },
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
    { name: "Ancient History", subject: "Ancient History", correct: 0, total: 1, acc: 0, band: "weak" },
    { name: "Number Series", subject: "Reasoning", correct: 0, total: 1, acc: 0, band: "weak" },
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
  { id: "fx-m2", title: "Modern History One-Liner Capsule", subject: "Modern History", type: "note", url: "https://example.com/b", isFree: true, isPublished: true },
  { id: "fx-m3", title: "Geography Mapping — Video Series", subject: "Geography", type: "video", url: "https://example.com/c", isFree: false, isPublished: true },
  { id: "fx-m4", title: "Economic Survey 2026 — Key Highlights", subject: "Economy", type: "pdf", url: "https://example.com/d.pdf", isFree: false, isPublished: true },
  { id: "fx-m5", title: "CSAT Reasoning — Shortcut Tricks", subject: "Reasoning", type: "video", url: "https://example.com/e", isFree: true, isPublished: true },
];

export const FX_ENROLLMENTS = [
  { id: "fx-e1", plan_code: "prelims-2026", batch_id: null, status: "active", expires_at: new Date(Date.now() + 300 * day).toISOString(), enrolled_at: iso(60), batches: null },
  { id: "fx-e2", plan_code: "bpsc-2026", batch_id: null, status: "active", expires_at: new Date(Date.now() + 5 * day).toISOString(), enrolled_at: iso(120), batches: null },
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
  subject: ["Polity", "Modern History", "Geography", "Economy", "Environment"][i % 5],
  topic: "Fundamental Rights and Directive Principles of State Policy",
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
        topic: ["Polity", "Modern History", "Geography", "Economy"][i % 4],
        subject: ["Polity", "Modern History", "Geography", "Economy"][i % 4],
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
        topic: "Quantitative Aptitude",
        subject: "Quantitative Aptitude",
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
          id: "fx-eb0", subject: "Polity", topic: "Fundamental Rights", type: "statement_based", marks: 2, negative: 0.66,
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
          id: "fx-eb1", subject: "Ancient History", topic: "Science", type: "match_the_following", marks: 2, negative: 0.66,
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
          id: "fx-eb2", subject: "Geography", topic: "Rivers", type: "assertion_reason", marks: 2, negative: 0.66,
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
          id: "fx-eb3", subject: "Reasoning", topic: "Number Series", type: "reasoning_aptitude", marks: 2, negative: 0.66,
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
