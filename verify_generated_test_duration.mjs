// Generated-test duration by exam (review item #10): BPSC keeps 0.8 min/question;
// a UPSC paper of a standard format takes that format's time (GS Paper I and CSAT
// Paper II both two hours, half papers one hour), anything else 1.2 min/question.
// Run: node verify_generated_test_duration.mjs
import { testDurationFor, upscPaperFormat } from "./src/lib/generate.js";
const cases = [
  ["bpsc", 150, 120, "BPSC full-length 150 Q"],
  ["bpsc", 75, 60, "BPSC 75 Q"],
  ["bpsc", 80, 64, "BPSC 80 Q keeps BPSC's pace (the CSAT rule is UPSC-only)"],
  ["upsc", 100, 120, "UPSC GS Paper I, 100 Q"],
  ["upsc", 80, 120, "UPSC CSAT Paper II, 80 Q -- two hours, not 96 minutes"],
  ["upsc", 50, 60, "UPSC GS half paper, 50 Q"],
  ["upsc", 40, 60, "UPSC CSAT half paper, 40 Q"],
  ["upsc", 43, 52, "a non-standard length (the old History L2 Ancient draft) falls back to 1.2 min/Q"],
  ["jpsc", 100, 80, "exam without its own pace falls back to BPSC's"],
];
const formats = [[100, true], [80, true], [50, true], [40, true], [120, false], [46, false], [12, false]];
for (const [n, ok] of formats) {
  if (!!upscPaperFormat(n) !== ok) { console.log(`FAIL  upscPaperFormat(${n}) should be ${ok}`); process.exit(1); }
}
console.log("PASS  upscPaperFormat accepts only 100 / 80 / 50 / 40");
let fail = 0;
for (const [exam, n, want, label] of cases) {
  const got = testDurationFor(exam, n);
  console.log(`${got === want ? "PASS" : "FAIL"}  ${label}: ${exam} ${n} Q -> ${got} min (expected ${want})`);
  if (got !== want) fail++;
}
console.log(fail ? `\n${fail} FAILED` : "\nALL PASS");
process.exit(fail ? 1 : 0);
