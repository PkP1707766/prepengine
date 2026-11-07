/**
 * Reads the Mains spreadsheets we already keep, exported from Google Sheets
 * as CSV (File → Download → Comma-separated values), and turns them into rows
 * the db.js importers can save. Pure functions: nothing here touches the
 * network, so a preview can be shown before anything is written.
 *
 * Three layouts are recognised by their header row, wherever it sits (the
 * topper sheet has two blank rows above its header):
 *
 *   pyq_categories    PYQ | Categories (with confidence levels)
 *                     "Truth knows no color.(2025)" | "{Justice(70), Power(80)}"
 *   topper_answers    Subject | Year | Rank | Topper | Coaching | Question | Page | Link
 *   topic_map         ... | Question from Topper Copy | Similar PYQs | ...
 *                     "Similar PYQs" holds "Topic.(2025) (Confidence: 90)" entries
 *
 * Imports only mainsKeys.js, so it runs under plain Node for checking a
 * sheet too.
 */
import { essayKey, copyLinkAt } from "./mainsKeys.js";

export { essayKey, copyLinkAt };

/* ---------------------------------------------------------------- CSV -- */

/** RFC 4180: quoted fields may hold commas, doubled quotes and newlines. */
export function parseCsv(text) {
  let s = String(text || "");
  // Google Sheets' CSV starts with a byte-order mark.
  if (s.charCodeAt(0) === 0xfeff) s = s.slice(1);
  const rows = [];
  let row = [];
  let field = "";
  let quoted = false;
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (quoted) {
      if (c === '"') {
        if (s[i + 1] === '"') { field += '"'; i++; }
        else quoted = false;
      } else field += c;
    } else if (c === '"') quoted = true;
    else if (c === ",") { row.push(field); field = ""; }
    else if (c === "\n" || c === "\r") {
      if (c === "\r" && s[i + 1] === "\n") i++;
      row.push(field); rows.push(row); row = []; field = "";
    } else field += c;
  }
  if (field !== "" || row.length) { row.push(field); rows.push(row); }
  return rows;
}

/* ------------------------------------------------------------ cleaning -- */

/* UTF-8 read as Windows-1252 somewhere upstream: the sheet itself holds
   "â€˜my terroristâ€™". These are the sequences that actually occur. */
const ch = (...codes) => String.fromCharCode(...codes);
const MOJIBAKE = [
  [ch(0xe2, 0x20ac, 0x2dc), ch(0x2018)],   // left single quote
  [ch(0xe2, 0x20ac, 0x2122), ch(0x2019)],  // right single quote / apostrophe
  [ch(0xe2, 0x20ac, 0x153), ch(0x201c)],   // left double quote
  [ch(0xe2, 0x20ac, 0x9d), ch(0x201d)],    // right double quote
  [ch(0xe2, 0x20ac, 0xfffd), ch(0x201d)],  // right double quote, last byte lost
  [ch(0xe2, 0x20ac, 0x201c), ch(0x2013)],  // en dash
  [ch(0xe2, 0x20ac, 0x201d), ch(0x2014)],  // em dash
  [ch(0xe2, 0x20ac, 0xa6), ch(0x2026)],    // ellipsis
  [ch(0xc2, 0xa0), " "],                   // no-break space
];

export function cleanText(s) {
  let out = String(s ?? "");
  for (const [bad, good] of MOJIBAKE) out = out.split(bad).join(good);
  return out.replace(/\s+/g, " ").trim();
}

/** "Q.2) Elucidate…", "Q.12 The…", "Q 3. …" → the question alone. */
export function cleanQuestion(s) {
  return cleanText(s).replace(/^\s*Q\s*\.?\s*\d{1,3}\s*[).:\-–]?\s*/i, "").trim();
}

const COACHING = {
  forumias: "Forum IAS", visionias: "Vision IAS", nextias: "Next IAS", vajiramandravi: "Vajiram & Ravi",
  vajiram: "Vajiram & Ravi", drishtiias: "Drishti IAS", drishti: "Drishti IAS", insightsias: "Insights IAS",
  shankarias: "Shankar IAS", ksgindia: "KSG", ksg: "KSG", rauias: "Rau's IAS", sleepyclasses: "Sleepy Classes",
};
export function cleanCoaching(s) {
  const t = cleanText(s);
  return COACHING[essayKey(t)] || t;
}

/** GS1…GS4, Essay, or an optional by name. */
export function paperOf(subject) {
  const s = cleanText(subject);
  if (!s) return null;
  if (/essay/i.test(s)) return { paper: "essay", label: "" };
  const gs = s.match(/^(?:gs|general\s*studies)\s*[-–]?\s*(?:paper\s*)?([1-4]|i{1,3}|iv)\b/i);
  if (gs) {
    const n = { i: 1, ii: 2, iii: 3, iv: 4 }[gs[1].toLowerCase()] || Number(gs[1]);
    return { paper: `gs${n}`, label: "" };
  }
  return { paper: "optional", label: s };
}

/** "2025, 2024, 2023" + "217, 267, 297" → the best rank with its year, and a
 *  note that keeps every attempt. */
export function rankAndYear(yearsCell, ranksCell) {
  const years = String(yearsCell || "").match(/\d{4}/g)?.map(Number) || [];
  const ranks = String(ranksCell || "").match(/\d+/g)?.map(Number) || [];
  const pairs = ranks.map((r, i) => ({ rank: r, year: years[i] ?? years[0] ?? null }));
  if (!pairs.length) return { rank: null, cseYear: years[0] ?? null, note: null };
  const best = pairs.reduce((a, b) => (b.rank < a.rank ? b : a));
  const note = pairs.length > 1 ? pairs.map((p) => (p.year ? `AIR ${p.rank} (${p.year})` : `AIR ${p.rank}`)).join(" · ") : null;
  return { rank: best.rank, cseYear: best.year, note };
}

function titleFromUrl(url) {
  try {
    const last = decodeURIComponent(new URL(url).pathname.split("/").pop() || "");
    return last.replace(/\.pdf$/i, "").replace(/[-_]+/g, " ").trim().slice(0, 140) || null;
  } catch { return null; }
}

/* ------------------------------------------------------------- formats -- */

const norm = (h) => cleanText(h).toLowerCase();

function findHeader(rows, test) {
  for (let i = 0; i < Math.min(rows.length, 12); i++) {
    const cells = rows[i].map(norm);
    if (test(cells)) return { index: i, cells };
  }
  return null;
}

const FORMATS = [
  {
    key: "topper_answers",
    test: (c) => ["subject", "topper", "question", "link"].every((h) => c.includes(h)),
  },
  {
    key: "topic_map",
    test: (c) => c.some((h) => h.startsWith("question from topper")) && c.some((h) => h.startsWith("similar pyq")),
  },
  {
    key: "pyq_categories",
    test: (c) => c.includes("pyq") && c.some((h) => h.startsWith("categor")),
  },
];

/** "Truth knows no color.(2025)" → { topic, year }. */
export function splitTopicYear(cell) {
  const s = cleanText(cell);
  const m = s.match(/^(.*?)\s*\((\d{4})\)\s*\.?$/);
  return m ? { topic: m[1].trim(), year: Number(m[2]) } : { topic: s, year: null };
}

/** "{Justice(70), Power: the leader's burden(80)}" → [{ name, confidence }], best first. */
export function parseCategories(cell) {
  const out = [];
  const s = cleanText(cell).replace(/[{}]/g, "");
  for (const m of s.matchAll(/([^()]+?)\s*\(\s*(?:confidence:\s*)?(\d{1,3})\s*\)/gi)) {
    const name = m[1].replace(/^[\s,;]+/, "").trim();
    if (name) out.push({ name, confidence: Math.min(100, Number(m[2])) });
  }
  return out.sort((a, b) => b.confidence - a.confidence);
}

/** "Topic.(2025) (Confidence: 90)\n\n Other topic.(2019) (Confidence: 70)" */
export function parseSimilar(cell) {
  const out = [];
  const s = cleanText(cell);
  for (const m of s.matchAll(/([^;]+?)\s*\((\d{4})\)\s*\(\s*confidence:\s*(\d{1,3})\s*\)/gi)) {
    const topic = m[1].replace(/^[\s,;]+/, "").trim();
    if (topic) out.push({ topic, year: Number(m[2]), confidence: Math.min(100, Number(m[3])) });
  }
  return out;
}

/**
 * Parse a CSV export into { format, items, skipped, notes }. `items` is what
 * the matching db.js importer takes; `skipped` counts rows that could not be
 * used, with a reason each, so the preview can say why.
 */
export function parseImport(text) {
  const rows = parseCsv(text).filter((r) => r.some((c) => cleanText(c)));
  if (!rows.length) return { format: null, items: [], skipped: [], notes: ["The file is empty."] };

  let header = null;
  let format = null;
  for (const f of FORMATS) {
    header = findHeader(rows, f.test);
    if (header) { format = f.key; break; }
  }
  if (!format) {
    return { format: null, items: [], skipped: [], notes: ["No known header row. Expected one of: PYQ + Categories; Subject, Year, Rank, Topper, Coaching, Question, Page, Link; or Question from Topper Copy + Similar PYQs."] };
  }

  const col = (name) => header.cells.findIndex((h) => h === name || h.startsWith(name));
  const body = rows.slice(header.index + 1);
  const skipped = [];
  const items = [];

  if (format === "pyq_categories") {
    const cPyq = col("pyq");
    const cCat = col("categor");
    body.forEach((r, i) => {
      const { topic, year } = splitTopicYear(r[cPyq]);
      if (!topic) return;
      if (!year) { skipped.push({ row: header.index + i + 2, reason: "no year in brackets", text: topic }); return; }
      items.push({ topic, year, themes: parseCategories(r[cCat]) });
    });
  }

  if (format === "topper_answers") {
    const c = {
      subject: col("subject"), year: col("year"), rank: col("rank"), topper: col("topper"),
      coaching: col("coaching"), question: col("question"), page: col("page"), link: col("link"),
    };
    body.forEach((r, i) => {
      const rowNo = header.index + i + 2;
      const p = paperOf(r[c.subject]);
      const question = cleanQuestion(r[c.question]);
      const name = cleanText(r[c.topper]);
      const link = cleanText(r[c.link]);
      if (!p || !question || !name) { skipped.push({ row: rowNo, reason: "missing subject, topper or question", text: question || name }); return; }
      if (!/^https?:\/\//i.test(link)) { skipped.push({ row: rowNo, reason: "no link", text: question }); return; }
      const pageCell = parseInt(cleanText(r[c.page]), 10);
      const pageInLink = Number((link.match(/#page=(\d+)/i) || [])[1]);
      const url = copyLinkAt(link);
      items.push({
        paper: p.paper,
        paperLabel: p.label,
        topper: { name, ...rankAndYear(r[c.year], r[c.rank]) },
        coaching: cleanCoaching(r[c.coaching]),
        question,
        page: Number.isFinite(pageCell) && pageCell > 0 ? pageCell : (pageInLink || null),
        url,
        title: titleFromUrl(url),
      });
    });
  }

  if (format === "topic_map") {
    const cQ = col("question from topper");
    const cS = col("similar pyq");
    const merged = new Map();
    body.forEach((r) => {
      const topic = cleanQuestion(r[cQ]);
      if (!topic) return;
      const k = essayKey(topic);
      if (!k) return;
      const similar = parseSimilar(r[cS]);
      if (!merged.has(k)) merged.set(k, { topic, similar: [] });
      merged.get(k).similar.push(...similar);
    });
    items.push(...merged.values());
  }

  const notes = [];
  if (format === "topper_answers") {
    const by = items.reduce((m, it) => m.set(it.paper, (m.get(it.paper) || 0) + 1), new Map());
    notes.push([...by].map(([k, n]) => `${n} ${k}`).join(", "));
    notes.push(`${new Set(items.map((it) => it.url)).size} copies, ${new Set(items.map((it) => essayKey(it.topper.name))).size} toppers`);
  }
  if (format === "pyq_categories") {
    notes.push(`${new Set(items.flatMap((it) => it.themes.map((t) => t.name.toLowerCase()))).size} categories become themes`);
  }
  if (format === "topic_map") {
    notes.push(`${items.reduce((n, it) => n + it.similar.length, 0)} similar-PYQ entries across ${items.length} topics`);
  }
  return { format, items, skipped, notes };
}
