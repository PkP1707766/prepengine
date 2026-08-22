import React from "react";
import { DiyaLogo } from "./Brand.jsx";

/**
 * A runtime error anywhere below this point used to unmount the whole tree and
 * leave a blank white page — exactly what happened when the exam screen called
 * a helper that lived in another scope. Now it shows something a student can
 * act on, and logs enough to debug.
 */
export default class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { error: null };
  }

  static getDerivedStateFromError(error) {
    return { error };
  }

  componentDidCatch(error, info) {
    console.error("[JUNOONIAS] crashed in", this.props.label || "app", error, info?.componentStack);
  }

  render() {
    if (!this.state.error) return this.props.children;

    const wrap = {
      minHeight: "100vh", display: "grid", placeItems: "center", padding: 24,
      background: "linear-gradient(160deg,#f6ead0,#e7cfa6)",
      fontFamily: '"Mukta", system-ui, sans-serif', color: "#5b1414",
    };
    const card = {
      maxWidth: 460, width: "100%", background: "#fffdf7", borderRadius: 18,
      border: "1px solid #e8dcc0", padding: "34px 30px", textAlign: "center",
      boxShadow: "0 18px 50px rgba(90,40,10,.14)",
    };
    const btn = {
      marginTop: 20, width: "100%", padding: "13px 18px", borderRadius: 12, border: 0,
      background: "linear-gradient(135deg,#8a2222,#5b1414)", color: "#fff",
      fontWeight: 700, fontSize: 15, cursor: "pointer", fontFamily: "inherit",
    };

    return (
      <div style={wrap}>
        <div style={card} role="alert">
          <DiyaLogo size={54} ring />
          <h1 style={{ fontFamily: '"Cinzel", serif', fontSize: 21, margin: "16px 0 8px" }}>
            Something went wrong
          </h1>
          <p style={{ fontSize: 14.5, lineHeight: 1.6, color: "#7a6450", margin: 0 }}>
            Sorry — this page hit an unexpected error. Your progress is saved. Reloading usually fixes it.
          </p>
          <button style={btn} onClick={() => window.location.reload()}>Reload the page</button>
          <button
            style={{ ...btn, background: "transparent", color: "#7a6450", border: "1px solid #e8dcc0", marginTop: 10 }}
            onClick={() => { window.location.href = "/"; }}
          >
            Back to home
          </button>
          {import.meta.env.DEV && (
            <pre style={{
              textAlign: "left", marginTop: 18, fontSize: 11.5, whiteSpace: "pre-wrap",
              background: "#fdf6e3", padding: 12, borderRadius: 10, color: "#c0392b", overflowX: "auto",
            }}>
              {String(this.state.error?.stack || this.state.error)}
            </pre>
          )}
          <div style={{ marginTop: 18, fontSize: 12, color: "#a89474" }}>
            Still stuck? <a href="mailto:junoonias123@gmail.com" style={{ color: "#8a2222" }}>junoonias123@gmail.com</a>
          </div>
        </div>
      </div>
    );
  }
}
