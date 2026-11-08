/**
 * Local key/value storage with a real in-memory fallback.
 *
 * The app previously called `window.storage.get/set` — an API that does not
 * exist in any browser. Every read silently returned the fallback and every
 * write silently vanished, which is why nothing an admin created ever
 * persisted. This is the replacement.
 */
const MEM = new Map();
const PREFIX = "junoonias:";

function available() {
  try {
    const k = PREFIX + "__probe__";
    localStorage.setItem(k, "1");
    localStorage.removeItem(k);
    return true;
  } catch {
    return false; // Safari private mode, disabled storage, SSR
  }
}

const OK = typeof window !== "undefined" && available();

export function loadKey(key, fallback = null) {
  try {
    const raw = OK ? localStorage.getItem(PREFIX + key) : MEM.get(key);
    if (raw == null) return fallback;
    return JSON.parse(raw);
  } catch {
    return fallback;
  }
}

export function saveKey(key, value) {
  try {
    const raw = JSON.stringify(value);
    if (OK) localStorage.setItem(PREFIX + key, raw);
    else MEM.set(key, raw);
    return true;
  } catch {
    return false; // quota exceeded — caller keeps working from state
  }
}

/** A one-shot request, left by the public site, for the student dashboard to
 *  open on a given view: `{ view, at }`. The Mains section's buttons ask for
 *  the Essay view; the dashboard honours the request for half an hour, then
 *  drops it. */
export const OPEN_VIEW_KEY = "open-view";
const OPEN_VIEW_TTL = 30 * 60 * 1000;

export function askOpenView(view) {
  saveKey(OPEN_VIEW_KEY, { view, at: Date.now() });
}

/** The view the dashboard was asked to open on, if the request is recent. */
export function askedOpenView() {
  const ask = loadKey(OPEN_VIEW_KEY);
  return ask && Date.now() - (Number(ask.at) || 0) < OPEN_VIEW_TTL ? ask.view : null;
}

export function removeKey(key) {
  try {
    if (OK) localStorage.removeItem(PREFIX + key);
    else MEM.delete(key);
  } catch { /* nothing to do */ }
}
