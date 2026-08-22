import { AlertCircle, RotateCcw, Inbox } from "lucide-react";

/** Shimmering placeholder used while a real query is in flight. */
export function Skeleton({ h = 16, w = "100%", r = 8, style }) {
  return (
    <span
      aria-hidden="true"
      style={{
        display: "block", height: h, width: w, borderRadius: r,
        background: "linear-gradient(90deg,#f3e8d0 25%,#fbf3e2 37%,#f3e8d0 63%)",
        backgroundSize: "400% 100%", animation: "jn-shimmer 1.3s ease infinite",
        ...style,
      }}
    />
  );
}

/** Card-shaped skeleton grid — matches the real card sizes so nothing jumps. */
export function SkeletonCards({ count = 3, height = 148 }) {
  return (
    <div style={{ display: "grid", gap: 16, gridTemplateColumns: "repeat(auto-fill,minmax(280px,1fr))" }}>
      {Array.from({ length: count }, (_, i) => (
        <div key={i} style={{ background: "var(--card,#fff)", border: "1px solid var(--line,#efe4cd)", borderRadius: 16, padding: 18 }}>
          <Skeleton h={14} w="65%" />
          <Skeleton h={11} w="40%" style={{ marginTop: 10 }} />
          <Skeleton h={height - 90} style={{ marginTop: 16 }} />
        </div>
      ))}
    </div>
  );
}

/** Honest empty state — says what is missing and what to do about it. */
export function EmptyState({ icon, title, text, action, compact }) {
  return (
    <div style={{
      textAlign: "center", padding: compact ? "28px 20px" : "52px 24px",
      color: "var(--muted,#7a6450)",
    }}>
      <div style={{
        width: 56, height: 56, borderRadius: 16, margin: "0 auto 14px",
        display: "grid", placeItems: "center",
        background: "var(--gold-bg,#faf2dc)", color: "var(--gold-2,#b8923a)",
      }}>
        {icon || <Inbox size={26} />}
      </div>
      <div style={{ fontSize: 16, fontWeight: 700, color: "var(--ink,#2e1c12)" }}>{title}</div>
      {text && <div style={{ fontSize: 13.5, marginTop: 6, maxWidth: 380, marginInline: "auto", lineHeight: 1.6 }}>{text}</div>}
      {action && <div style={{ marginTop: 18 }}>{action}</div>}
    </div>
  );
}

/** Shown when a query fails, with a way back rather than a dead end. */
export function ErrorState({ message, onRetry, compact }) {
  return (
    <div style={{
      textAlign: "center", padding: compact ? "24px 18px" : "44px 24px",
      color: "var(--muted,#7a6450)",
    }}>
      <div style={{
        width: 52, height: 52, borderRadius: 15, margin: "0 auto 14px",
        display: "grid", placeItems: "center", background: "#fbeaea", color: "#c0392b",
      }}>
        <AlertCircle size={24} />
      </div>
      <div style={{ fontSize: 15.5, fontWeight: 700, color: "var(--ink,#2e1c12)" }}>Couldn't load this</div>
      <div style={{ fontSize: 13.5, marginTop: 6, maxWidth: 400, marginInline: "auto", lineHeight: 1.6 }}>
        {message || "Something went wrong reaching the server."}
      </div>
      {onRetry && (
        <button className="btn btn-ghost btn-sm" style={{ marginTop: 16, width: "auto", display: "inline-flex" }} onClick={onRetry}>
          <RotateCcw size={15} /> Try again
        </button>
      )}
    </div>
  );
}
