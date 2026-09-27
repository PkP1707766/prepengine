// Generated-test duration by exam (review item #10): BPSC keeps 0.8 min/question,
// UPSC GS Paper I gets 1.2. Run: node verify_generated_test_duration.mjs
import { testDurationFor } from "./src/lib/generate.js";
const cases = [
  ["bpsc", 150, 120, "BPSC full-length 150 Q"],
  ["bpsc", 75, 60, "BPSC 75 Q"],
  ["upsc", 100, 120, "UPSC GS1 100 Q"],
  ["upsc", 43, 52, "History L2 Ancient"],
  ["upsc", 20, 24, "History L2 Medieval"],
  ["upsc", 45, 54, "History L2 Modern"],
  ["upsc", 12, 14, "History L2 Art & Culture"],
  ["jpsc", 100, 80, "exam without its own pace falls back to BPSC's"],
];
let fail = 0;
for (const [exam, n, want, label] of cases) {
  const got = testDurationFor(exam, n);
  console.log(`${got === want ? "PASS" : "FAIL"}  ${label}: ${exam} ${n} Q -> ${got} min (expected ${want})`);
  if (got !== want) fail++;
}
console.log(fail ? `\n${fail} FAILED` : "\nALL PASS");
process.exit(fail ? 1 : 0);
