import { loadKey, saveKey } from "./storage.js";

/* A subject picked on the home page, handed to PYQ Practice once. */
const OPEN_KEY = "pyq:open-subject";
export const openPyqSubject = (code) => saveKey(OPEN_KEY, code || null);
export const takePyqSubject = () => { const v = loadKey(OPEN_KEY, null); saveKey(OPEN_KEY, null); return v; };
