/* Two helpers that both db.js and the sheet importer need. They live apart
   so db.js does not pull the whole CSV parser (admin-only) into the bundle
   every student downloads. No imports: plain Node can run them too. */

/** Lowercase letters and digits only -- the same rule as SQL essay_key(), so
 *  a topic typed two ways meets in both places. */
export function essayKey(s) {
  return String(s ?? "").toLowerCase().replace(/[^a-z0-9]+/g, "") || null;
}

/** A link copy's URL at a page. The browser's own PDF viewer honours #page. */
export function copyLinkAt(sourceUrl, page) {
  const base = String(sourceUrl || "").split("#")[0];
  return page ? `${base}#page=${page}` : base;
}
