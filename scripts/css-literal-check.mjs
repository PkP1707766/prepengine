/* A backtick inside a CSS block terminates the JS template literal the
 * stylesheet lives in. It has broken the build four separate times in this
 * project, always the same way: someone quotes a selector inside a /* … *​/
 * comment. ESLint only reports it as an unhelpful "Unexpected token" a hundred
 * lines away, so this names it directly.
 *
 * Run by `npm run css:check`, and folded into `npm run verify`.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const files = [
  "src/screens/PublicSite.jsx",
  "src/screens/StudentApp.jsx",
  "src/screens/AdminApp.jsx",
  "src/screens/ExamApp.jsx",
  "src/lib/i18n.jsx",
];

let bad = 0;
for (const rel of files) {
  const abs = path.join(root, rel);
  if (!fs.existsSync(abs)) continue;
  const lines = fs.readFileSync(abs, "utf8").split("\n");

  // Walk the file tracking whether we are inside `const CSS = ` … ` .
  let inCss = false;
  lines.forEach((line, i) => {
    const opens = /^\s*(const|let)\s+\w*CSS\w*\s*=\s*`/.test(line);
    if (opens) { inCss = true; return; }
    if (inCss && line.trim() === "`;") { inCss = false; return; }
    if (inCss && line.includes("`")) {
      console.log(`${rel}:${i + 1}  backtick inside the CSS literal — this ends the string early`);
      console.log(`    ${line.trim().slice(0, 100)}`);
      bad++;
    }
  });
}

console.log(bad === 0
  ? "PASS  no stray backticks inside any CSS template literal"
  : `FAIL  ${bad} stray backtick(s) — the stylesheet will terminate early`);
process.exit(bad === 0 ? 0 : 1);
