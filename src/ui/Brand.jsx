/* The JUNOONIAS diya mark, drawn as SVG so it stays crisp at any size. */
export function DiyaLogo({ size = 48, boxed = false, radius = 14, ring = false }) {
  const inner = (
    <svg width={boxed ? size * 0.66 : size} height={boxed ? size * 0.66 : size}
         viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <defs>
        <linearGradient id="jd-flame" x1="32" y1="6" x2="32" y2="40" gradientUnits="userSpaceOnUse">
          <stop offset="0" stopColor="#FFE9A8" />
          <stop offset="0.45" stopColor="#F4B23C" />
          <stop offset="1" stopColor="#C0392B" />
        </linearGradient>
        <linearGradient id="jd-bowl" x1="12" y1="40" x2="52" y2="52" gradientUnits="userSpaceOnUse">
          <stop offset="0" stopColor="#E6C074" />
          <stop offset="0.5" stopColor="#B8923A" />
          <stop offset="1" stopColor="#8A6A14" />
        </linearGradient>
        <radialGradient id="jd-glow" cx="32" cy="26" r="20" gradientUnits="userSpaceOnUse">
          <stop offset="0" stopColor="#F4B23C" stopOpacity="0.5" />
          <stop offset="1" stopColor="#F4B23C" stopOpacity="0" />
        </radialGradient>
      </defs>
      {ring && <circle cx="32" cy="32" r="30" stroke="#B8923A" strokeWidth="1.5" opacity="0.7" />}
      <circle cx="32" cy="25" r="18" fill="url(#jd-glow)" />
      {/* flame */}
      <path d="M32 7 C36.5 15 41 19.5 41 27 C41 33.2 37 37.5 32 37.5 C27 37.5 23 33.2 23 27 C23 19.5 27.5 15 32 7 Z"
            fill="url(#jd-flame)" />
      <path d="M32 16 C34.5 20.5 36.5 23 36.5 27 C36.5 30.8 34.6 33.4 32 33.4 C29.4 33.4 27.5 30.8 27.5 27 C27.5 23 29.5 20.5 32 16 Z"
            fill="#FFF3CF" opacity="0.85" />
      {/* wick */}
      <rect x="31" y="36" width="2" height="4" rx="1" fill="#5b1414" />
      {/* bowl */}
      <ellipse cx="32" cy="41.5" rx="20" ry="4.4" fill="#8A6A14" opacity="0.5" />
      <path d="M12.5 41.5 C12.5 47.6 20.7 51.5 32 51.5 C43.3 51.5 51.5 47.6 51.5 41.5 C46 44.4 39.5 45.6 32 45.6 C24.5 45.6 18 44.4 12.5 41.5 Z"
            fill="url(#jd-bowl)" />
      <path d="M12.5 41.5 C18 44.4 24.5 45.6 32 45.6 C39.5 45.6 46 44.4 51.5 41.5"
            stroke="#FBE7BF" strokeWidth="1" opacity="0.6" fill="none" />
    </svg>
  );
  if (!boxed) return inner;
  return (
    <div style={{
      width: size, height: size, borderRadius: radius, flex: "0 0 auto",
      display: "grid", placeItems: "center",
      background: "linear-gradient(150deg,#6b1a1a 0%,#3a0e0e 100%)",
      boxShadow: "inset 0 1px 0 rgba(255,220,150,.25), 0 6px 18px rgba(58,14,14,.30)",
    }}>{inner}</div>
  );
}
