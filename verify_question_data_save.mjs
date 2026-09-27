// Run: node verify_question_data_save.mjs
// Extracts buildCleanData/buildTypeData from AdminApp.jsx and checks what a save keeps.
import { readFileSync } from "node:fs";
const src = readFileSync("src/screens/AdminApp.jsx", "utf8");
const grab = (name) => { const i = src.indexOf(`function ${name}(`); let depth = 0, j = src.indexOf("{", i); for (let k = j; k < src.length; k++) { if (src[k] === "{") depth++; else if (src[k] === "}" && --depth === 0) return src.slice(i, k + 1); } };
const buildCleanData = new Function(`${grab("buildTypeData")}\n${grab("buildCleanData")}\nreturn buildCleanData;`)();
let fail = 0; const check = (label, ok, got) => { console.log(`${ok ? "PASS" : "FAIL"}  ${label}${ok ? "" : "  got " + JSON.stringify(got)}`); if (!ok) fail++; };
const ar = { assertion: "S1", reason: "S2", ar_labels: "statement", closing: "Which one of the following is correct in respect of the above statements?", fixed_option_order: true };
const outAr = buildCleanData("assertion_reason", ar);
check("Statement-I/II row keeps ar_labels", outAr.ar_labels === "statement", outAr);
check("Statement-I/II row keeps its closing line", outAr.closing === ar.closing, outAr);
check("Statement-I/II row keeps fixed_option_order", outAr.fixed_option_order === true, outAr);
const outBpsc = buildCleanData("assertion_reason", { assertion: "A", reason: "R" });
check("BPSC-style A/R row gains no new keys", JSON.stringify(Object.keys(outBpsc)) === JSON.stringify(["assertion", "reason"]), outBpsc);
const outMatch = buildCleanData("match_the_following", { list_1: ["1. x"], list_2: ["y"], closing: "How many of the pairs given above are correctly matched?", fixed_option_order: true });
check("match row still keeps its closing line (earlier fix)", !!outMatch.closing && outMatch.fixed_option_order === true, outMatch);
const outStmt = buildCleanData("statement_based", { statements: ["a", "b"], closing: "Which of the statements given above is/are correct?", fixed_option_order: true });
check("statement row keeps closing + fixed order", !!outStmt.closing && outStmt.fixed_option_order === true, outStmt);
console.log(fail ? `\n${fail} FAILED` : "\nALL PASS"); process.exit(fail ? 1 : 0);
