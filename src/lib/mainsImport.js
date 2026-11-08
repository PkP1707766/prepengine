/**
 * Reads the Mains spreadsheets we already keep, exported from Google Sheets
 * as CSV (File → Download → Comma-separated values), and turns them into rows
 * the db.js importers can save. Pure functions: nothing here touches the
 * network, so a preview can be shown before anything is written.
 *
 * Layouts are recognised by their header row, wherever it sits (the topper
 * sheet has two blank rows above its header):
 *
 *   pyq_categories    PYQ | Categories (with confidence levels)
 *                     "Truth knows no color.(2025)" | "{Justice(70), Power(80)}"
 *   topper_answers    Subject | Year | Rank | Topper | Coaching | Question | Page | Link
 *   topper_essays     File name | Topper Copy (Hand written) | ... | Question from
 *                     Topper Copy | Similar PYQs: one essay per row. Optional
 *                     Topper, Source, AIR and Essay marks columns replace what
 *                     the file name says about the writer.
 *   topic_map         ... | Question from Topper Copy | Similar PYQs | ...
 *                     "Similar PYQs" holds "Topic.(2025) (Confidence: 90)" entries
 *   copy_links        file_name | drive_id: a lookup list, read together with
 *                     the topper-essay tab. That tab's "Link" cells are formulas,
 *                     so its CSV export holds only the word "Link".
 *   essay_texts       File name | Topper Copy (Hand written) | Question from
 *                     Topper Copy | Text: each essay's full text, paragraphs
 *                     split by a blank line, matched to an imported essay by its
 *                     copy and question.
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

/** An essay's text: paragraphs split by a blank line, each paragraph's
 *  spacing tidied and mojibake repaired. Unlike cleanText, the paragraph
 *  breaks survive. */
export function cleanBody(s) {
  let out = String(s ?? "");
  for (const [bad, good] of MOJIBAKE) out = out.split(bad).join(good);
  return out.replace(/\r\n?/g, "\n").split(/\n\s*\n/)
    .map((p) => p.replace(/\s+/g, " ").trim()).filter(Boolean).join("\n\n");
}

export const wordCount = (s) => (String(s || "").match(/\S+/g) || []).length;

/** "Q.2) Elucidate…", "Q.12 The…", "Q 3. …" → the question alone. */
export function cleanQuestion(s) {
  return cleanText(s).replace(/^\s*Q\s*\.?\s*\d{1,3}\s*[).:\-–]?\s*/i, "").trim();
}

const COACHING = {
  forumias: "Forum IAS", visionias: "Vision IAS", nextias: "Next IAS", vajiramandravi: "Vajiram & Ravi",
  vajiram: "Vajiram & Ravi", drishtiias: "Drishti IAS", drishti: "Drishti IAS", insightsias: "Insights IAS",
  shankarias: "Shankar IAS", ksgindia: "KSG", ksg: "KSG", rauias: "Rau's IAS", sleepyclasses: "Sleepy Classes",
  // The topper sheet writes "Vision" for cdn.visionias.in copies, and "Mgp"
  // (Forum IAS's mains programme) for forumias.com ones.
  vision: "Vision IAS", mgp: "Forum IAS",
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

/** A Drive file id or link → its viewer URL; any other http(s) link as it is. */
export function driveViewUrl(s) {
  const t = cleanText(s);
  const m = t.match(/drive\.google\.com\/(?:file\/d\/|open\?id=|uc\?(?:[^#\s]*&)?id=)([\w-]{20,})/i) || t.match(/^([\w-]{25,})$/);
  if (m) return `https://drive.google.com/file/d/${m[1]}/view`;
  return /^https?:\/\/\S+$/i.test(t) ? t : null;
}

const nameCase = (s) => (s === s.toUpperCase()
  ? s.toLowerCase().split(" ").map((w) => w.charAt(0).toUpperCase() + w.slice(1)).join(" ")
  : s);

/** What a copy's file name says about its writer, if anything:
 *  "VisionIAS Toppers Answer Booklet ZUFISHAN HAQUE_1718713357.pdf",
 *  "Gautam Vivekanandan AIR211 Essay(149)-1.pdf", "Harshit Goyal - Essay 1 and 2.pdf".
 *  "1.pdf" and "230718 Essay Practice.pdf" say nothing: null. */
export function writerFromFileName(file) {
  const f = cleanText(file);
  let m = f.match(/^VisionIAS Toppers Answer Booklet (.+?)_\d+\.pdf$/i);
  if (m) return { name: nameCase(m[1].trim()), source: "Vision IAS", rank: null, essayMarks: null };
  m = f.match(/^(.+?)\s+AIR\s*(\d{1,4})\s+Essay\s*\((\d{1,3})\)/i);
  if (m) return { name: m[1].trim(), source: "", rank: Number(m[2]), essayMarks: Number(m[3]) <= 250 ? Number(m[3]) : null };
  m = f.match(/^([A-Za-z][A-Za-z .]+?)\s+-\s+Essay\b/i);
  if (m) return { name: m[1].trim(), source: "", rank: null, essayMarks: null };
  return null;
}

const positive = (v) => {
  const n = parseInt(cleanText(v), 10);
  return Number.isFinite(n) && n > 0 ? n : null;
};

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
    // First: an essay-text file carries the copy link and question as well.
    key: "essay_texts",
    test: (c) => c.includes("text") && c.some((h) => h.startsWith("question from topper")),
  },
  {
    key: "topper_answers",
    test: (c) => ["subject", "topper", "question", "link"].every((h) => c.includes(h)),
  },
  {
    // Before topic_map: the topper-essay tab carries that layout's headers too.
    key: "topper_essays",
    test: (c) => c.includes("file name") && c.some((h) => h.startsWith("question from topper"))
      && c.some((h) => h.startsWith("topper copy (hand") || h.startsWith("handwritten")),
  },
  {
    key: "topic_map",
    test: (c) => c.some((h) => h.startsWith("question from topper")) && c.some((h) => h.startsWith("similar pyq")),
  },
  {
    key: "pyq_categories",
    test: (c) => c.includes("pyq") && c.some((h) => h.startsWith("categor")),
  },
  {
    key: "copy_links",
    test: (c) => (c.includes("file_name") || c.includes("file name")) && (c.includes("drive_id") || c.includes("drive id")),
  },
];

/** A column value the essay sheet glues onto some topics:
 *  "Social media is inherently a selfish medium Domain.(2017)". */
const stripTopicArtifacts = (t) => t.replace(/\s+Domain\.?$/, "").trim();

/** "Truth knows no color.(2025)" → { topic, year }. */
export function splitTopicYear(cell) {
  const s = cleanText(cell);
  const m = s.match(/^(.*?)\s*\((\d{4})\)\s*\.?$/);
  return m ? { topic: stripTopicArtifacts(m[1].trim()), year: Number(m[2]) } : { topic: stripTopicArtifacts(s), year: null };
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
    const topic = stripTopicArtifacts(m[1].replace(/^[\s,;]+/, "").trim());
    if (topic) out.push({ topic, year: Number(m[2]), confidence: Math.min(100, Number(m[3])) });
  }
  return out;
}

function detect(rows) {
  for (const f of FORMATS) {
    const header = findHeader(rows, f.test);
    if (header) return { format: f.key, header };
  }
  return { format: null, header: null };
}

const NO_HEADER = "No known header row. Expected one of: PYQ + Categories; Subject, Year, Rank, Topper, Coaching, Question, Page, Link; "
  + "File name + Topper Copy (Hand written) + Question from Topper Copy; Question from Topper Copy + Similar PYQs; "
  + "or File name + Question from Topper Copy + Text.";

/** A link list: cleaned file name → copy URL (the drive_id column, or any
 *  cell holding a link). */
function readLinks({ rows, header }) {
  const cName = header.cells.findIndex((h) => h === "file_name" || h === "file name");
  const cId = header.cells.findIndex((h) => h === "drive_id" || h === "drive id");
  const out = new Map();
  rows.slice(header.index + 1).forEach((r) => {
    const name = cleanText(r[cName]);
    const url = driveViewUrl(r[cId]) || r.filter((_, i) => i !== cName).map(driveViewUrl).find(Boolean);
    if (name && url && !out.has(name)) out.set(name, url);
  });
  return out;
}

/** Rows with a topic and its "Similar PYQs", merged per topic. */
function mergeTopics(body, cQ, cS) {
  const merged = new Map();
  body.forEach((r) => {
    const topic = cleanQuestion(r[cQ]);
    const k = essayKey(topic);
    if (!k) return;
    if (!merged.has(k)) merged.set(k, { topic, similar: [] });
    merged.get(k).similar.push(...parseSimilar(r[cS]));
  });
  return [...merged.values()];
}

/** One data sheet → { format, items, skipped, notes, topics }. */
function parseData({ rows, header, format }, links) {
  const col = (name) => header.cells.findIndex((h) => h === name || h.startsWith(name));
  const exact = (...names) => header.cells.findIndex((h) => names.includes(h));
  const body = rows.slice(header.index + 1);
  const skipped = [];
  const items = [];
  let topics = [];

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
    items.push(...mergeTopics(body, col("question from topper"), col("similar pyq")));
  }

  if (format === "essay_texts") {
    const c = {
      file: col("file name"), q: col("question from topper"), text: exact("text"), source: exact("source"),
      hand: header.cells.findIndex((h) => h.startsWith("topper copy (hand") || h.startsWith("handwritten")),
    };
    body.forEach((r, i) => {
      const rowNo = header.index + i + 2;
      const question = cleanQuestion(r[c.q]);
      if (!question) return;
      const text = cleanBody(r[c.text]);
      const file = cleanText(r[c.file]);
      const url = c.hand >= 0 ? driveViewUrl(r[c.hand]) : null;
      if (!text) { skipped.push({ row: rowNo, reason: "no text", text: question }); return; }
      if (!url && !file) { skipped.push({ row: rowNo, reason: "no file name or copy link", text: question }); return; }
      items.push({ file, url, question, body: text, words: wordCount(text), source: c.source >= 0 ? cleanText(r[c.source]) || null : null });
    });
  }

  if (format === "topper_essays") {
    const c = {
      file: col("file name"), q: col("question from topper"), similar: col("similar pyq"),
      hand: header.cells.findIndex((h) => h.startsWith("topper copy (hand") || h.startsWith("handwritten")),
      topper: exact("topper", "writer"), source: exact("source", "coaching"), air: exact("air", "rank"), marks: exact("essay marks", "marks"),
    };
    // Every row's similar PYQs count, even when its essay cannot be imported.
    topics = mergeTopics(body, c.q, c.similar);
    body.forEach((r, i) => {
      const rowNo = header.index + i + 2;
      const file = cleanText(r[c.file]);
      const question = cleanQuestion(r[c.q]);
      if (!question) return;
      const url = driveViewUrl(r[c.hand]) || links.get(file) || null;
      if (!url) {
        skipped.push({ row: rowNo, reason: links.size ? "file not in the link list" : "no copy link: add the HandwrittenLinks export too", text: file || question });
        return;
      }
      let writer = null;
      if (c.topper >= 0) {
        const name = cleanText(r[c.topper]);
        const marks = positive(r[c.marks]);
        if (name) writer = { name, source: c.source >= 0 ? cleanText(r[c.source]) : "", rank: positive(r[c.air]), essayMarks: marks != null && marks <= 250 ? marks : null };
      } else {
        writer = writerFromFileName(file);
      }
      if (!writer) { skipped.push({ row: rowNo, reason: "no writer name", text: file }); return; }
      items.push({
        paper: "essay",
        paperLabel: "",
        topper: { name: writer.name, rank: writer.rank ?? null, cseYear: null, note: null, essayMarks: writer.essayMarks ?? null },
        coaching: writer.source ? cleanCoaching(writer.source) : "",
        question,
        page: null,
        url,
        title: file.replace(/\.pdf$/i, "") || null,
      });
    });
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
  if (format === "essay_texts") {
    const ws = items.map((it) => it.words).sort((a, b) => a - b);
    notes.push(`${items.length} essay texts, ${ws.reduce((a, b) => a + b, 0).toLocaleString("en-IN")} words`);
    if (ws.length) notes.push(`${ws[0]}–${ws[ws.length - 1]} words per essay, median ${ws[Math.floor(ws.length / 2)]}`);
  }
  if (format === "topper_essays") {
    notes.push(`${items.length} essays in ${new Set(items.map((it) => it.url)).size} copies by ${new Set(items.map((it) => essayKey(it.topper.name))).size} writers`);
    notes.push(`${topics.reduce((n, t) => n + t.similar.length, 0)} similar-PYQ entries across ${topics.length} topics`);
  }
  return { format, items, skipped, notes, topics };
}

/**
 * Parse one or more CSV exports into { format, items, skipped, notes, topics,
 * files }: one data sheet at a time, plus link lists to resolve the
 * topper-essay tab's file names. `items` is what the matching db.js importer
 * takes, `topics` the topper-essay tab's similar-PYQ part, and `skipped` the
 * rows that could not be used, each with a reason, so the preview can say why.
 */
export function parseImportFiles(files) {
  const read = files.map((f) => {
    const rows = parseCsv(f.text).filter((r) => r.some((c) => cleanText(c)));
    return { name: f.name || "", rows, ...detect(rows) };
  });
  const data = read.filter((f) => f.format && f.format !== "copy_links");
  const lists = read.filter((f) => f.format === "copy_links");

  // Typed transcripts share the handwritten copies' file names, so only the
  // handwritten list may resolve them. Google names an export "<sheet> - <tab>.csv".
  const typed = lists.filter((f) => /typed/i.test(f.name));
  const untyped = lists.filter((f) => !typed.includes(f));
  let hand = untyped.length > 1 ? untyped.filter((f) => /hand/i.test(f.name)) : untyped;
  const ambiguous = untyped.length > 1 && hand.length !== 1;
  if (ambiguous) hand = [];

  const role = (f) => {
    if (!f.rows.length) return "empty";
    if (!f.format) return "not recognised";
    if (f.format !== "copy_links") return "data";
    if (hand.includes(f)) return "handwritten links";
    return typed.includes(f) ? "typed links, not imported yet" : "links, not used";
  };
  const fileList = read.map((f) => ({ name: f.name, format: f.format, rows: Math.max(0, f.rows.length - 1), role: role(f) }));
  const none = (note) => ({ format: null, items: [], skipped: [], notes: [note], topics: [], files: fileList });

  if (!read.some((f) => f.rows.length)) return none("The file is empty.");
  if (data.length > 1) return none(`Add one data sheet at a time: ${data.map((f) => f.name || "the pasted text").join(" and ")} are both data sheets.`);
  if (!data.length) {
    return none(lists.length ? "These are link lists (file name → Drive file). Add them together with the topper-essay tab." : NO_HEADER);
  }

  const out = parseData(data[0], hand.length ? readLinks(hand[0]) : new Map());
  if (ambiguous) out.notes.push("Several link lists and none clearly named Handwritten, so none was used: add only the HandwrittenLinks export.");
  if (typed.length) out.notes.push("Typed transcripts are not imported yet.");
  const unknown = read.filter((f) => f.rows.length && !f.format);
  if (unknown.length) out.notes.push(`Not recognised: ${unknown.map((f) => f.name).join(", ")}.`);
  return { ...out, files: fileList };
}

/** One CSV export, as text. */
export function parseImport(text) {
  return parseImportFiles([{ name: "", text }]);
}
