/**
 * Turns an uploaded topper copy (PDF) into one WebP image per page, in the
 * admin's own browser, so a copy can be read in the app with no rendering
 * server. Imported dynamically from the admin screen only: pdf.js (and its
 * worker) never reach a student's bundle.
 *
 * Pages are drawn 1240 px wide -- A4 at 150 dpi, enough to read handwriting
 * at full width -- and encoded as WebP at 0.72, which keeps a scanned page
 * near 150-300 KB.
 */

export const PAGE_WIDTH = 1240;
export const PAGE_QUALITY = 0.72;

/** SHA-256 of a file, hex. Two uploads of one PDF meet on this. */
export async function sha256Hex(file) {
  const digest = await crypto.subtle.digest("SHA-256", await file.arrayBuffer());
  return [...new Uint8Array(digest)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

let pdfjsPromise = null;
function loadPdfjs() {
  pdfjsPromise ||= (async () => {
    const pdfjs = await import("pdfjs-dist");
    const { default: workerUrl } = await import("pdfjs-dist/build/pdf.worker.min.mjs?url");
    pdfjs.GlobalWorkerOptions.workerSrc = workerUrl;
    return pdfjs;
  })();
  return pdfjsPromise;
}

/* The copies come from outside, so they are parsed defensively. pdf.js 5 has
   no eval path left to switch off (the CVE-2024-4367 one is gone upstream);
   what still needs a guard is size -- a crafted file can ask for an image or
   a page big enough to exhaust the admin's tab. */
export const MAX_PDF_BYTES = 150 * 1024 * 1024;
const MAX_IMAGE_PIXELS = 50_000_000;   // a 300 dpi A4 scan is ~8.7 million
const MAX_PAGE_HEIGHT = 6000;          // px; a normal page at 1240 wide is ~1754

/** Open a PDF file, refusing anything that is not one or is too large. */
export async function openPdf(file) {
  if (file.size > MAX_PDF_BYTES) throw new Error(`This PDF is over ${MAX_PDF_BYTES / 1024 / 1024} MB.`);
  const data = new Uint8Array(await file.arrayBuffer());
  const head = String.fromCharCode(...data.subarray(0, 5));
  if (head !== "%PDF-") throw new Error("This file is not a PDF.");
  const pdfjs = await loadPdfjs();
  return pdfjs.getDocument({ data, maxImageSize: MAX_IMAGE_PIXELS }).promise;
}

/** Render one page (1-based) to a WebP blob. */
export async function renderPage(pdf, n, { width = PAGE_WIDTH, quality = PAGE_QUALITY } = {}) {
  const page = await pdf.getPage(n);
  const base = page.getViewport({ scale: 1 });
  // Fit the width, unless that would make an absurdly tall canvas.
  const scale = Math.min(width / base.width, MAX_PAGE_HEIGHT / base.height);
  const viewport = page.getViewport({ scale });
  const canvas = document.createElement("canvas");
  canvas.width = Math.round(viewport.width);
  canvas.height = Math.round(viewport.height);
  const ctx = canvas.getContext("2d", { alpha: false });
  ctx.fillStyle = "#ffffff";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  await page.render({ canvas, canvasContext: ctx, viewport }).promise;
  const blob = await new Promise((resolve, reject) =>
    canvas.toBlob((b) => (b ? resolve(b) : reject(new Error("This browser could not encode the page as WebP."))), "image/webp", quality));
  page.cleanup();
  // Release the bitmap now rather than whenever the collector gets to it --
  // a 30-page copy would otherwise hold ~250 MB of canvases.
  canvas.width = 0;
  canvas.height = 0;
  return blob;
}
