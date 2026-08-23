/* Does the Hindi actually hold together?
 *
 * Three failures this catches that a screenshot would not:
 *   1. a screen asking for a key the dictionary never defines — t() falls back
 *      to returning the key itself, so the UI silently shows "fb_send"
 *   2. an entry with no Hindi value at all
 *   3. an entry whose Hindi is just the English copied across
 */
import fs from "node:fs";

import path from "node:path";
import { fileURLToPath } from "node:url";
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..") + path.sep;
const i18n = fs.readFileSync(root + "src/lib/i18n.jsx", "utf8");

const entryRe = /^ {2}([a-z][a-z0-9_]*):\s*\{\s*en:\s*("(?:[^"\\]|\\.)*")\s*,\s*hi:\s*("(?:[^"\\]|\\.)*")\s*\}/gm;
const anyKeyRe = /^ {2}([a-z][a-z0-9_]*):\s*\{\s*en:/gm;

const defined = new Set([...i18n.matchAll(anyKeyRe)].map((m) => m[1]));

const files = [
  "src/screens/PublicSite.jsx", "src/screens/StudentApp.jsx", "src/screens/ExamApp.jsx",
  "src/screens/ContentPages.jsx", "src/screens/JoinScreen.jsx", "src/screens/LoginScreen.jsx",
  "src/screens/authChrome.jsx",
];
const used = new Map();
for (const f of files) {
  const src = fs.readFileSync(root + f, "utf8");
  for (const m of src.matchAll(/\bt\(\s*"([a-z][a-z0-9_]*)"\s*\)/g)) {
    if (!used.has(m[1])) used.set(m[1], new Set());
    used.get(m[1]).add(f.split("/").pop());
  }
}
// resources.js holds dictionary keys in data, resolved via t(x) later.
// Only labelKey/blurbKey/tKey/sKey are dictionary keys — a bare `key:` in
// RESOURCES or in the achievements array is a route id or an achievement id,
// not a translation key, and counting those produced twenty false failures.
for (const f of ["src/lib/resources.js"]) {
  const src = fs.readFileSync(root + f, "utf8");
  for (const m of src.matchAll(/(?:labelKey|blurbKey|tKey|sKey):\s*"([a-z][a-z0-9_]*)"/g)) {
    if (!used.has(m[1])) used.set(m[1], new Set());
    used.get(m[1]).add(f.split("/").pop());
  }
}

// The dashboard's NAV/META_KEY pair: NAV carries `key`, and the page header
// resolves both <key> and <key>_s. Scoped to those two blocks so ledger and
// achievement keys are not swept in.
{
  const src = fs.readFileSync(root + "src/screens/StudentApp.jsx", "utf8");
  const navBlock = src.slice(src.indexOf("const NAV = ["), src.indexOf("const NOTIF_ICON"));
  for (const m of navBlock.matchAll(/key:\s*"(sd_[a-z_]+)"/g)) {
    for (const k of [m[1], m[1] + "_s"]) {
      if (!used.has(k)) used.set(k, new Set());
      used.get(k).add("StudentApp.jsx");
    }
  }
  // LEDGER_KEY values are plain keys with no _s variant.
  const ledger = src.slice(src.indexOf("const LEDGER_KEY = {"), src.indexOf("const LEDGER_KEY = {") + 400);
  for (const m of ledger.matchAll(/:\s*"(sd_[a-z_]+)"/g)) {
    if (!used.has(m[1])) used.set(m[1], new Set());
    used.get(m[1]).add("StudentApp.jsx");
  }
}

const missing = [...used.keys()].filter((k) => !defined.has(k));

const KEEP_SAME = /^"(FAQ|GSTIN|CIN|JUNOONIAS|NCERT|UPSC|BPSC|UPPCS|Rank|OTP)"$/;
const noHi = [], sameAsEn = [];
for (const m of i18n.matchAll(entryRe)) {
  const [, k, en, hi] = m;
  if (hi === '""') noHi.push(k);
  else if (en === hi && !KEEP_SAME.test(en)) sameAsEn.push(`${k} = ${en}`);
}

const line = (ok, msg) => console.log((ok ? "PASS  " : "FAIL  ") + msg);

console.log(`dictionary entries : ${defined.size}`);
console.log(`keys referenced    : ${used.size}`);
console.log("");
line(missing.length === 0,
  missing.length ? `${missing.length} key(s) a screen asks for are NOT in the dictionary: ${missing.join(", ")}`
                 : "every key a screen asks for exists in the dictionary");
line(noHi.length === 0,
  noHi.length ? `${noHi.length} entr(ies) have an empty Hindi value: ${noHi.join(", ")}`
              : "every entry has a Hindi value");
line(sameAsEn.length === 0,
  sameAsEn.length ? `${sameAsEn.length} Hindi value(s) are just the English: ${sameAsEn.slice(0, 10).join(" | ")}`
                  : "no Hindi value is merely the English copied across");

process.exit(missing.length || noHi.length || sameAsEn.length ? 1 : 0);
