/* Shared formatters. Previously each of the three sub-apps defined its own
   near-identical copies, which is how the /50 divisor bug survived so long. */

const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

export const fmtINR = (n) => "₹" + Number(n || 0).toLocaleString("en-IN", { maximumFractionDigits: 0 });

export const fmtDate = (s) => {
  const d = s instanceof Date ? s : new Date(s);
  if (Number.isNaN(d.getTime())) return "—";
  return d.getDate() + " " + MONTHS[d.getMonth()];
};

export const fmtLongDate = (s) => {
  const d = s instanceof Date ? s : new Date(s);
  if (Number.isNaN(d.getTime())) return "—";
  return `${d.getDate()} ${MONTHS[d.getMonth()]} ${d.getFullYear()}`;
};

/** mm:ss / hh:mm:ss — used by the exam clock. */
export const fmtClock = (sec) => {
  const s = Math.max(0, Math.round(sec || 0));
  const h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), r = s % 60;
  const pad = (n) => String(n).padStart(2, "0");
  return h > 0 ? `${pad(h)}:${pad(m)}:${pad(r)}` : `${pad(m)}:${pad(r)}`;
};

/** "18m 04s" — used in analytics copy. */
export const fmtDuration = (sec) => {
  const s = Math.max(0, Math.round(sec || 0));
  const h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), r = s % 60;
  if (h > 0) return `${h}h ${m}m`;
  return `${m}m ${String(r).padStart(2, "0")}s`;
};

export const daysUntil = (target) => {
  if (!target) return 0;
  const d = new Date(target);
  if (Number.isNaN(d.getTime())) return 0;
  return Math.max(0, Math.ceil((d - new Date()) / 86400000));
};

export const pct = (part, whole) => (whole > 0 ? (part / whole) * 100 : 0);

export const SEM = { strong: "#1f8a4c", average: "#b8923a", weak: "#c0392b" };

export const bandFor = (accuracy) => (accuracy >= 75 ? "strong" : accuracy >= 50 ? "average" : "weak");

export const gradeFor = (p) =>
  p >= 85 ? { g: "A+", c: "#1f8a4c" } :
  p >= 70 ? { g: "A",  c: "#2f9e58" } :
  p >= 55 ? { g: "B",  c: "#d4a64a" } :
  p >= 40 ? { g: "C",  c: "#a8842f" } :
            { g: "D",  c: "#c0392b" };

export const initials = (name) =>
  String(name || "")
    .trim()
    .split(/\s+/)
    .map((w) => w[0])
    .filter(Boolean)
    .slice(0, 2)
    .join("")
    .toUpperCase() || "?";

export const uid = () =>
  typeof crypto !== "undefined" && crypto.randomUUID
    ? crypto.randomUUID()
    : "id-" + Date.now() + "-" + Math.random().toString(36).slice(2, 10);

/** Escapes user text before it goes anywhere near an attribute or template. */
export const clean = (s, max = 500) => String(s ?? "").slice(0, max);
