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
  review: [],
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
        options: [
          { id: "fx-eq" + i + "-a", body: "Article 14 — Equality before law" },
          { id: "fx-eq" + i + "-b", body: "Article 19 — Freedom of speech and expression" },
          { id: "fx-eq" + i + "-c", body: "Article 32 — Right to Constitutional Remedies" },
          { id: "fx-eq" + i + "-d", body: "Article 21 — Protection of life and personal liberty" },
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
