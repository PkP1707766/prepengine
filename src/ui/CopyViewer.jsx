import { useState, useEffect, useRef, useCallback } from "react";
import { X, ZoomIn, ZoomOut, CornerDownRight, RotateCcw, Lock } from "lucide-react";
import { useLang } from "../lib/contexts.js";
import { copyPageUrls, COPY_URL_TTL } from "../lib/db.js";
import { loadKey, saveKey } from "../lib/storage.js";

/* ============================================================
   COPY VIEWER — reads a hosted topper copy page by page.

   It opens on the page where the essay starts, not on the cover:
   that is the whole point of mapping essays to pages. The pages
   between start and end carry a gold edge, so a student can see
   where this essay stops and the next one begins.

   Pages are painted onto canvases from short-lived signed URLs.
   No image URL ever sits in the page (so there is no "save image
   as"), URLs are re-signed before they expire, and canvases far
   from the reader are cleared -- 30 decoded pages would otherwise
   hold a quarter of a gigabyte.
   ============================================================ */

const VIEWER_CSS = `
.cv-root{position:fixed;inset:0;z-index:90;display:flex;flex-direction:column;background:#1b1714;color:#f4ece0}
.cv-bar{display:flex;align-items:center;gap:10px;padding:10px 14px;padding-top:max(10px,env(safe-area-inset-top,0px));
  background:#26201b;border-bottom:1px solid #3a3029;flex-wrap:wrap}
.cv-title{flex:1;min-width:0}
.cv-title b{display:block;font-size:14px;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cv-title span{display:block;font-size:12px;color:#c9b8a2;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cv-tools{display:flex;align-items:center;gap:6px}
.cv-btn{display:inline-flex;align-items:center;justify-content:center;gap:6px;min-width:38px;height:38px;padding:0 10px;
  border-radius:9px;border:1px solid #4a3d33;background:#2f2721;color:#f4ece0;font:inherit;font-size:13px;font-weight:600;cursor:pointer}
.cv-btn:hover{background:#3a3029}
.cv-btn:focus-visible{outline:2px solid #e3c877;outline-offset:2px}
.cv-page-in{width:56px;height:38px;border-radius:9px;border:1px solid #4a3d33;background:#2f2721;color:#f4ece0;
  font:inherit;font-size:13.5px;text-align:center;font-variant-numeric:tabular-nums}
.cv-of{font-size:13px;color:#c9b8a2;font-variant-numeric:tabular-nums;white-space:nowrap}
.cv-scroll{flex:1;overflow:auto;overscroll-behavior:contain;padding:18px 12px 60px}
.cv-stack{position:relative;margin:0 auto;display:flex;flex-direction:column;align-items:center;gap:16px}
.cv-page{position:relative;width:100%;background:#fdfbf6;border-radius:4px;box-shadow:0 6px 26px rgba(0,0,0,.45);overflow:hidden}
.cv-page.in{box-shadow:-5px 0 0 #e3c877,0 6px 26px rgba(0,0,0,.45)}
.cv-page canvas{position:absolute;inset:0;width:100%;height:100%;display:block}
.cv-ph{position:absolute;inset:0;display:grid;place-items:center;color:#8d7f70;font-size:13px;text-align:center;padding:16px}
.cv-ph button{margin-top:10px}
.cv-num{position:absolute;right:8px;bottom:8px;font-size:11.5px;font-weight:700;color:#5b4e44;background:rgba(253,251,246,.92);
  border-radius:6px;padding:2px 7px;font-variant-numeric:tabular-nums}
.cv-flag{position:absolute;left:10px;font-size:11.5px;font-weight:800;letter-spacing:.02em;color:#3d2a06;background:#e3c877;
  border-radius:6px;padding:4px 9px;z-index:1}
.cv-flag.top{top:10px}
.cv-flag.bottom{bottom:10px}
.cv-msg{max-width:420px;margin:12vh auto 0;text-align:center;color:#d9cbb8;font-size:14.5px;line-height:1.6}
.cv-msg svg{color:#e3c877;margin-bottom:10px}
@media(max-width:560px){
  .cv-bar{gap:8px}
  .cv-title{flex-basis:100%}
  .cv-hide-sm{display:none}
}
@media(prefers-reduced-motion:reduce){.cv-scroll{scroll-behavior:auto}}
`;

const BASE_WIDTH = 920;
const ZOOMS = [0.6, 0.8, 1, 1.25, 1.5, 1.75, 2];
const BATCH = 8;
const KEEP = 6; // pages either side of the reader that stay painted

export default function CopyViewer({ copyId, pageCount, startPage = null, endPage = null, title = "", subtitle = "", onClose }) {
  const { t } = useLang();
  const total = Math.max(0, Number(pageCount) || 0);
  const first = Math.min(Math.max(1, Number(startPage) || 1), Math.max(1, total));

  const scroller = useRef(null);
  const pageEls = useRef(new Map());
  const canvases = useRef(new Map());
  const urls = useRef(new Map());     // page -> { url, at }
  const status = useRef(new Map());   // page -> "loading" | "ready" | "error"
  const queue = useRef(new Set());
  const flushing = useRef(false);
  const currentRef = useRef(first);

  // A page's status lives in a ref for the loader -- the observers read it
  // synchronously -- and is mirrored into state, which is all render reads.
  const [pageStatus, setPageStatus] = useState({});
  const mark = useCallback((n, v) => {
    if (v) status.current.set(n, v);
    else status.current.delete(n);
    setPageStatus((s) => {
      if ((s[n] || null) === (v || null)) return s;
      const next = { ...s };
      if (v) next[n] = v;
      else delete next[n];
      return next;
    });
  }, []);
  const [zoom, setZoom] = useState(() => {
    const z = Number(loadKey("viewer:zoom", 1));
    return ZOOMS.includes(z) ? z : 1;
  });
  const [current, setCurrent] = useState(first);
  const [jump, setJump] = useState(String(first));
  const [ratio, setRatio] = useState(1754 / 1240);
  const [denied, setDenied] = useState(false);

  /* ---- painting --------------------------------------------------------- */
  const paint = useCallback(async (n) => {
    const entry = urls.current.get(n);
    if (!entry || !canvases.current.get(n)) return;
    mark(n, "loading");
    // Anonymous CORS first, which keeps the canvas readable for later tools
    // (text extraction); a host that sends no CORS header gets a plain
    // second attempt, so the page still shows.
    for (const cors of [true, false]) {
      const img = new Image();
      if (cors) img.crossOrigin = "anonymous";
      img.decoding = "async";
      img.src = entry.url;
      try {
        await img.decode();
      } catch {
        continue;
      }
      const cv = canvases.current.get(n);
      if (!cv) return;
      cv.width = img.naturalWidth;
      cv.height = img.naturalHeight;
      cv.getContext("2d").drawImage(img, 0, 0);
      if (img.naturalWidth > 0) setRatio((r) => (r === 1754 / 1240 ? img.naturalHeight / img.naturalWidth : r));
      mark(n, "ready");
      return;
    }
    mark(n, "error");
  }, [mark]);

  const flush = useCallback(async () => {
    if (flushing.current) return;
    flushing.current = true;
    try {
      while (queue.current.size) {
        const cur = currentRef.current;
        const pages = [...queue.current].sort((a, b) => Math.abs(a - cur) - Math.abs(b - cur));
        queue.current.clear();
        const now = Date.now();
        const stale = pages.filter((n) => {
          const u = urls.current.get(n);
          return !u || now - u.at > (COPY_URL_TTL - 60) * 1000;
        });
        for (let i = 0; i < stale.length; i += BATCH) {
          const chunk = stale.slice(i, i + BATCH);
          let got = {};
          let failed = false;
          try { got = await copyPageUrls(copyId, chunk); } catch (e) { failed = true; console.error("page signing failed", e); }
          const at = Date.now();
          chunk.forEach((n) => {
            if (got[n]) urls.current.set(n, { url: got[n], at });
            else mark(n, "error");
          });
          // Storage answered, and signed nothing on the very first request:
          // not a missing page -- this reader is not allowed the copy. A
          // network failure is different; it leaves Retry on each page.
          if (!failed && Object.keys(got).length === 0 && urls.current.size === 0) setDenied(true);
        }
        await Promise.all(pages.filter((n) => urls.current.has(n)).map((n) => paint(n)));
      }
    } finally {
      flushing.current = false;
    }
  }, [copyId, paint, mark]);

  const request = useCallback((n) => {
    const s = status.current.get(n);
    if (s === "ready" || s === "loading") return;
    queue.current.add(n);
    flush();
  }, [flush]);

  const release = useCallback((n) => {
    const cv = canvases.current.get(n);
    if (cv && status.current.get(n) === "ready") {
      cv.width = 0;
      cv.height = 0;
      mark(n, null);
    }
  }, [mark]);

  /* ---- observers: what to load, and which page the reader is on ---------- */
  useEffect(() => {
    const root = scroller.current;
    if (!root || total === 0) return undefined;
    const load = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        const n = Number(en.target.dataset.page);
        if (en.isIntersecting) request(n);
        else if (Math.abs(n - currentRef.current) > KEEP) release(n);
      });
    }, { root, rootMargin: "1400px 0px" });
    const band = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (!en.isIntersecting) return;
        const n = Number(en.target.dataset.page);
        currentRef.current = n;
        setCurrent(n);
        setJump(String(n));
      });
    }, { root, rootMargin: "-38% 0px -58% 0px" });
    pageEls.current.forEach((el) => { load.observe(el); band.observe(el); });
    return () => { load.disconnect(); band.disconnect(); };
  }, [total, request, release]);

  /* ---- scrolling -------------------------------------------------------- */
  const goTo = useCallback((n, smooth = true) => {
    const el = pageEls.current.get(n);
    const root = scroller.current;
    if (!el || !root) return;
    root.scrollTo({ top: el.offsetTop - 12, behavior: smooth ? "smooth" : "auto" });
  }, []);

  // Land on the essay's first page; again whenever the zoom changes the
  // page heights, so the reader stays on the page they were reading.
  useEffect(() => {
    const id = requestAnimationFrame(() => goTo(currentRef.current, false));
    return () => cancelAnimationFrame(id);
  }, [zoom, ratio, goTo]);

  /* ---- keyboard and body scroll ---------------------------------------- */
  useEffect(() => {
    const prev = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    const onKey = (e) => { if (e.key === "Escape") onClose?.(); };
    window.addEventListener("keydown", onKey);
    return () => { document.body.style.overflow = prev; window.removeEventListener("keydown", onKey); };
  }, [onClose]);

  const setZoomTo = (z) => { setZoom(z); saveKey("viewer:zoom", z); };
  const zi = ZOOMS.indexOf(zoom);
  const submitJump = (e) => {
    e.preventDefault();
    const n = Math.min(total, Math.max(1, parseInt(jump, 10) || current));
    setJump(String(n));
    currentRef.current = n;
    goTo(n);
  };

  const retry = (n) => {
    mark(n, null);
    urls.current.delete(n);
    request(n);
  };

  const start = Number(startPage) || null;
  const end = Number(endPage) || null;
  const inEssay = (n) => start && n >= start && (end ? n <= end : n === start);

  return (
    <div className="cv-root" role="dialog" aria-modal="true" aria-label={title}>
      <style>{VIEWER_CSS}</style>
      <div className="cv-bar">
        <div className="cv-title"><b>{title}</b>{subtitle && <span>{subtitle}</span>}</div>
        <div className="cv-tools">
          {total > 0 && (
            <form onSubmit={submitJump} style={{ display: "flex", alignItems: "center", gap: 6 }}>
              <input className="cv-page-in" inputMode="numeric" aria-label={t("es_v_page")} value={jump}
                     onChange={(e) => setJump(e.target.value.replace(/[^0-9]/g, ""))} onBlur={submitJump} />
              <span className="cv-of">/ {total}</span>
            </form>
          )}
          {start && (
            <button className="cv-btn" onClick={() => { currentRef.current = start; goTo(start); }} title={t("es_v_start")}>
              <CornerDownRight size={16} /><span className="cv-hide-sm">{t("es_v_start")}</span>
            </button>
          )}
          <button className="cv-btn" onClick={() => zi > 0 && setZoomTo(ZOOMS[zi - 1])} disabled={zi <= 0} aria-label={t("es_v_zoom_out")}><ZoomOut size={17} /></button>
          <button className="cv-btn" onClick={() => zi < ZOOMS.length - 1 && setZoomTo(ZOOMS[zi + 1])} disabled={zi >= ZOOMS.length - 1} aria-label={t("es_v_zoom_in")}><ZoomIn size={17} /></button>
          <button className="cv-btn" onClick={onClose} aria-label={t("es_v_close")}><X size={18} /></button>
        </div>
      </div>

      <div className="cv-scroll" ref={scroller}>
        {denied ? (
          <div className="cv-msg"><Lock size={30} /><div>{t("es_v_denied")}</div></div>
        ) : total === 0 ? (
          <div className="cv-msg">{t("es_v_no_pages")}</div>
        ) : (
          <div className="cv-stack" style={{ width: `min(${Math.round(BASE_WIDTH * zoom)}px, ${Math.round(100 * zoom)}%)` }}>
            {Array.from({ length: total }, (_, i) => {
              const n = i + 1;
              const s = pageStatus[n];
              return (
                <div key={n} data-page={n} className={"cv-page" + (inEssay(n) ? " in" : "")}
                     style={{ aspectRatio: `1 / ${ratio}` }}
                     ref={(el) => { if (el) pageEls.current.set(n, el); else pageEls.current.delete(n); }}>
                  {n === start && <span className="cv-flag top">{t("es_v_starts")}</span>}
                  {n === end && n !== start && <span className="cv-flag bottom">{t("es_v_ends")}</span>}
                  <canvas ref={(el) => { if (el) canvases.current.set(n, el); else canvases.current.delete(n); }} />
                  {s === "error" && (
                    <div className="cv-ph">
                      <div>
                        {t("es_v_failed")}
                        <div><button className="cv-btn" onClick={() => retry(n)}><RotateCcw size={15} />{t("es_v_retry")}</button></div>
                      </div>
                    </div>
                  )}
                  <span className="cv-num">{n}</span>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}
