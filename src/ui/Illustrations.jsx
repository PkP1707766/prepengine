/**
 * Hand-drawn SVG for the public site.
 *
 * Everything here is vector and inline: no image requests, crisp at any size,
 * theme-aware through currentColor and CSS variables, and animatable. Motion
 * is opt-out via prefers-reduced-motion, which the global stylesheet honours.
 *
 * The brand is "An Academy of Inner Fire", so the diya — a clay lamp — is the
 * organising motif rather than a generic education icon.
 */

let uid = 0;
const nextId = (p) => `${p}-${++uid}`;

/* ============================================================
   THE DIYA — hero centrepiece.
   Layered: glow, rotating mandala rings, lamp body, flame with
   an inner core, and embers rising off the tip.
   ============================================================ */
export function Diya({ size = 340, rings = true, embers = true }) {
  const g = nextId("dg");
  return (
    <svg className="ill-diya" width={size} height={size} viewBox="0 0 240 240"
         fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="presentation">
      <defs>
        {/* The glow has to fade fully to zero well inside the viewBox, or its
            own edge shows up as a visible disc against the hero gradient. */}
        <radialGradient id={`${g}-glow`} cx="50%" cy="40%" r="52%">
          <stop offset="0%"   stopColor="var(--flame-hi)" stopOpacity=".42" />
          <stop offset="38%"  stopColor="var(--flame-mid)" stopOpacity=".14" />
          <stop offset="72%"  stopColor="var(--flame-mid)" stopOpacity=".04" />
          <stop offset="100%" stopColor="var(--flame-mid)" stopOpacity="0" />
        </radialGradient>

        {/* Flame: bright, near-white at the core so it separates cleanly from
            the clay body. Gold-on-gold was why it read as one muddy shape. */}
        <linearGradient id={`${g}-flame`} x1="120" y1="50" x2="120" y2="126">
          <stop offset="0%"   stopColor="var(--flame-hi)" />
          <stop offset="30%"  stopColor="var(--flame-mid)" />
          <stop offset="68%"  stopColor="var(--flame-lo)" />
          <stop offset="100%" stopColor="var(--flame-base)" />
        </linearGradient>
        <linearGradient id={`${g}-core`} x1="120" y1="74" x2="120" y2="120">
          <stop offset="0%"   stopColor="#FFFFFF" stopOpacity=".96" />
          <stop offset="55%"  stopColor="var(--flame-hi)" stopOpacity=".85" />
          <stop offset="100%" stopColor="var(--flame-mid)" stopOpacity=".25" />
        </linearGradient>

        {/* Clay body — terracotta, lit from the upper left. */}
        <linearGradient id={`${g}-clay`} x1="66" y1="134" x2="176" y2="176">
          <stop offset="0%"   stopColor="var(--clay-hi)" />
          <stop offset="42%"  stopColor="var(--clay-mid)" />
          <stop offset="100%" stopColor="var(--clay-lo)" />
        </linearGradient>
        <linearGradient id={`${g}-rim`} x1="66" y1="128" x2="176" y2="142">
          <stop offset="0%"   stopColor="var(--clay-rim-hi)" />
          <stop offset="46%"  stopColor="var(--clay-rim)" />
          <stop offset="100%" stopColor="var(--clay-lo)" />
        </linearGradient>
        <radialGradient id={`${g}-oil`} cx="42%" cy="38%" r="70%">
          <stop offset="0%"   stopColor="#7A4526" />
          <stop offset="100%" stopColor="#361A0C" />
        </radialGradient>
      </defs>

      <circle cx="120" cy="100" r="104" fill={`url(#${g}-glow)`} />

      {rings && (
        <g>
          <circle className="ill-ring ill-ring-a" cx="120" cy="112" r="90"
                  stroke="var(--flame-hi)" strokeOpacity=".26" strokeWidth="1" strokeDasharray="2 10" />
          <circle className="ill-ring ill-ring-b" cx="120" cy="112" r="70"
                  stroke="var(--flame-hi)" strokeOpacity=".16" strokeWidth="1" strokeDasharray="1 8" />
          <g className="ill-ring ill-ring-c" stroke="var(--flame-hi)" strokeOpacity=".20" strokeWidth="1.2">
            {Array.from({ length: 24 }, (_, i) => (
              <line key={i} x1="120" y1="18" x2="120" y2="27"
                    transform={`rotate(${i * 15} 120 112)`} strokeLinecap="round" />
            ))}
          </g>
        </g>
      )}

      {embers && (
        <g fill="var(--flame-hi)">
          <circle className="ill-ember ill-ember-1" cx="105" cy="72" r="1.7" />
          <circle className="ill-ember ill-ember-2" cx="133" cy="66" r="1.3" />
          <circle className="ill-ember ill-ember-3" cx="120" cy="56" r="1"   />
          <circle className="ill-ember ill-ember-4" cx="112" cy="80" r="1.5" />
        </g>
      )}

      {/* ---- FLAME ----------------------------------------------------------
          One clean teardrop: pointed tip, bulbous base, a slight lean. Drawn
          at final size — the previous version was scaled with a transform,
          which is what put that notch in the tip. */}
      <g className="ill-flame">
        {/* Taller and narrower than a circle-with-a-point: the silhouette is
            what makes it read as flame rather than a droplet. */}
        <path d="M120 34c4.5 17 11.5 27 16.5 34.5 5.8 8.6 9.5 15.6 9.5 24.5
                 a26 26 0 0 1-52 0c0-8.9 3.7-15.9 9.5-24.5C108.5 61 115.5 51 120 34Z"
              fill={`url(#${g}-flame)`} />
        <path d="M120 66c2.6 9.6 6.4 15.2 9.3 19.4 3.1 4.5 4.7 8.4 4.7 13.1
                 a14 14 0 0 1-28 0c0-4.7 1.6-8.6 4.7-13.1C113.6 81.2 117.4 75.6 120 66Z"
              fill={`url(#${g}-core)`} />
      </g>

      {/* wick, sitting in the oil rather than floating above it */}
      <path d="M118.5 116h3v14h-3z" fill="#4A2412" />
      <path d="M118.5 116h3v5h-3z" fill="#1E0C05" />

      {/* ---- LAMP -----------------------------------------------------------
          Terracotta, not gold. A brass lamp under a gold flame is why the two
          shapes merged into one mustard blob. */}
      <ellipse cx="120" cy="200" rx="52" ry="7" fill="#000" opacity=".22" />

      {/* body */}
      <path d="M66 136c0 26 24 44 54 44s54-18 54-44c0 0-20 10-54 10s-54-10-54-10Z"
            fill={`url(#${g}-clay)`} />
      {/* pinched spout at the front */}
      <path d="M100 141c-6 3-10 7-11 12 5 1.5 10 2 14 1.6-1.8-4.4-2.6-9-3-13.6Z"
            fill="var(--clay-lo)" opacity=".55" />
      {/* rim */}
      <ellipse cx="120" cy="134" rx="54" ry="13.5" fill={`url(#${g}-rim)`} />
      <ellipse cx="120" cy="134" rx="44" ry="9"   fill={`url(#${g}-oil)`} />
      {/* oil sheen + rim highlight */}
      <ellipse cx="107" cy="131" rx="14" ry="3.4" fill="var(--flame-hi)" opacity=".20" />
      <path d="M70 130c10-6 30-9.5 50-9.5s40 3.5 50 9.5" stroke="var(--clay-rim-hi)"
            strokeOpacity=".8" strokeWidth="1.6" fill="none" strokeLinecap="round" />
      <path d="M70 148c12 9 31 14 50 14s38-5 50-14" stroke="var(--clay-hi)"
            strokeOpacity=".38" strokeWidth="1.4" fill="none" strokeLinecap="round" />
    </svg>
  );
}

/* ============================================================
   Decorative mandala — behind section headings and in bands.
   ============================================================ */
export function Mandala({ className = "", petals = 14, size = 420 }) {
  return (
    <svg className={"ill-mandala " + className} width={size} height={size} viewBox="0 0 200 200"
         fill="none" aria-hidden="true" role="presentation">
      {Array.from({ length: petals }, (_, i) => (
        <ellipse key={i} cx="100" cy="100" rx="90" ry="30" stroke="currentColor" strokeWidth="0.6"
                 transform={`rotate(${(i * 180) / petals} 100 100)`} />
      ))}
      <circle cx="100" cy="100" r="36" stroke="currentColor" strokeWidth="0.8" />
      <circle cx="100" cy="100" r="15" stroke="currentColor" strokeWidth="0.8" />
    </svg>
  );
}

/* ============================================================
   Journey art — three steps, one illustration each.
   Drawn rather than icon-fonted so they read as a set.
   ============================================================ */
export function StepArt({ step = 1, size = 78 }) {
  const g = nextId("st");
  const common = { width: size, height: size, viewBox: "0 0 80 80", fill: "none", "aria-hidden": true };

  if (step === 1) {
    // Choose your exam — three stacked cards, one lifting out.
    return (
      <svg {...common} className="ill-step">
        <defs>
          <linearGradient id={`${g}-a`} x1="0" y1="0" x2="0" y2="80">
            <stop offset="0" stopColor="var(--gold-300)" /><stop offset="1" stopColor="var(--gold-600)" />
          </linearGradient>
        </defs>
        <rect x="10" y="30" width="46" height="30" rx="6" fill="currentColor" opacity=".16" />
        <rect x="16" y="24" width="46" height="30" rx="6" fill="currentColor" opacity=".26" />
        <rect x="22" y="16" width="46" height="30" rx="6" fill={`url(#${g}-a)`} />
        <path d="M31 26h20M31 33h13" stroke="#4A0F19" strokeWidth="2.4" strokeLinecap="round" opacity=".65" />
        <circle cx="61" cy="55" r="11" fill="var(--brand-700)" />
        <path d="M56.5 55l3.2 3.2 6-6.4" stroke="#fff" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
    );
  }
  if (step === 2) {
    // Sit the paper — a clock over a sheet.
    return (
      <svg {...common} className="ill-step">
        <rect x="14" y="10" width="42" height="54" rx="6" fill="currentColor" opacity=".2" />
        <path d="M22 24h26M22 32h26M22 40h16" stroke="currentColor" strokeWidth="2.6" strokeLinecap="round" opacity=".55" />
        <circle cx="56" cy="50" r="16" fill="var(--gold-500)" />
        <circle cx="56" cy="50" r="16" stroke="var(--brand-700)" strokeWidth="2" />
        <path d="M56 41v9l6 4" stroke="var(--brand-900)" strokeWidth="2.6" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
    );
  }
  // Read the diagnosis — bars plus an upward trend.
  return (
    <svg {...common} className="ill-step">
      <rect x="10" y="12" width="60" height="52" rx="8" fill="currentColor" opacity=".16" />
      <rect x="20" y="40" width="8" height="16" rx="3" fill="var(--gold-600)" />
      <rect x="33" y="32" width="8" height="24" rx="3" fill="var(--gold-500)" />
      <rect x="46" y="22" width="8" height="34" rx="3" fill="var(--gold-300)" />
      <path d="M18 34l12-9 10 6 14-14" stroke="var(--brand-700)" strokeWidth="2.6"
            strokeLinecap="round" strokeLinejoin="round" fill="none" />
      <circle cx="54" cy="17" r="3.4" fill="var(--brand-700)" />
    </svg>
  );
}

/* ============================================================
   A stylised report card — shows what the product produces,
   instead of describing it in another paragraph.
   ============================================================ */
export function ReportArt({ className = "" }) {
  const g = nextId("ra");
  const bars = [26, 40, 18, 46, 32, 38];
  return (
    <svg className={"ill-report " + className} viewBox="0 0 360 300" fill="none"
         aria-hidden="true" role="presentation">
      <defs>
        <linearGradient id={`${g}-bar`} x1="0" y1="1" x2="0" y2="0">
          <stop offset="0" stopColor="var(--gold-600)" /><stop offset="1" stopColor="var(--gold-300)" />
        </linearGradient>
        <linearGradient id={`${g}-area`} x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stopColor="var(--brand-600)" stopOpacity=".30" />
          <stop offset="1" stopColor="var(--brand-600)" stopOpacity="0" />
        </linearGradient>
      </defs>

      <rect x="6" y="8" width="348" height="284" rx="20" fill="var(--cream-50)"
            stroke="var(--line)" strokeWidth="1.5" />

      {/* --- header: score ring + meta lines --- */}
      <circle cx="56" cy="56" r="24" stroke="var(--line)" strokeWidth="7" />
      <circle className="ill-ring-draw" cx="56" cy="56" r="24" stroke="var(--gold-500)" strokeWidth="7"
              strokeLinecap="round" strokeDasharray="151" strokeDashoffset="45"
              transform="rotate(-90 56 56)" />
      <text x="56" y="62" textAnchor="middle" fontSize="17" fontWeight="700"
            fill="var(--ink-900)" fontFamily="Fraunces, Georgia, serif">76</text>

      <rect x="94" y="40" width="132" height="8" rx="4" fill="var(--ink-400)" opacity=".26" />
      <rect x="94" y="56" width="92"  height="8" rx="4" fill="var(--ink-400)" opacity=".16" />
      <rect x="94" y="72" width="58"  height="8" rx="4" fill="var(--gold-500)" opacity=".5" />
      <rect x="250" y="44" width="64" height="24" rx="12"
            fill="var(--ok-600)" opacity=".14" />
      <text x="282" y="60" textAnchor="middle" fontSize="11" fontWeight="700"
            fill="var(--ok-600)" fontFamily="Inter, sans-serif">Rank 88</text>

      <line x1="24" y1="102" x2="336" y2="102" stroke="var(--line)" strokeWidth="1" />

      {/* --- trend --- */}
      <text x="24" y="124" fontSize="10.5" fontWeight="700" fill="var(--ink-400)"
            fontFamily="Inter, sans-serif" letterSpacing="1.2">SCORE TREND</text>
      <path d="M28 196 L86 180 L144 186 L202 158 L260 164 L318 132"
            stroke="var(--brand-600)" strokeWidth="2.6" strokeLinecap="round" strokeLinejoin="round"
            fill="none" className="ill-line-draw" />
      <path d="M28 196 L86 180 L144 186 L202 158 L260 164 L318 132 L318 206 L28 206 Z"
            fill={`url(#${g}-area)`} />
      {[[86, 180], [202, 158], [318, 132]].map(([x, y], i) => (
        <circle key={i} cx={x} cy={y} r="3.6" fill="var(--brand-700)" />
      ))}
      <line x1="24" y1="216" x2="336" y2="216" stroke="var(--line)" strokeWidth="1" />

      {/* --- subject bars --- */}
      <text x="24" y="238" fontSize="10.5" fontWeight="700" fill="var(--ink-400)"
            fontFamily="Inter, sans-serif" letterSpacing="1.2">BY SUBJECT</text>
      {bars.map((h, i) => (
        <rect key={i} x={28 + i * 34} y={276 - h} width="18" height={h} rx="5"
              fill={`url(#${g}-bar)`} opacity={0.55 + i * 0.07} />
      ))}
      <line x1="24" y1="276" x2="336" y2="276" stroke="var(--line)" strokeWidth="1.5" />
    </svg>
  );
}

/* ============================================================
   Ticket notches for the coupon banner.
   ============================================================ */
export function TicketIcon({ size = 26 }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" aria-hidden="true">
      <path d="M20 12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v4a2 2 0 0 1 0 4v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2Z"
            stroke="currentColor" strokeWidth="1.6" strokeLinejoin="round" />
      <path d="M9 4v16" stroke="currentColor" strokeWidth="1.6" strokeDasharray="3 3" />
    </svg>
  );
}

/* ============================================================
   Section divider — a small lotus rule.
   ============================================================ */
export function Divider({ className = "" }) {
  return (
    <svg className={"ill-divider " + className} viewBox="0 0 120 20" fill="none" aria-hidden="true" role="presentation">
      <path d="M2 10h34M84 10h34" stroke="currentColor" strokeWidth="1" strokeLinecap="round" opacity=".45" />
      <path d="M60 3c4 4 6 5 6 7s-2.7 5-6 5-6-3-6-5 2-3 6-7Z" fill="currentColor" opacity=".75" />
      <path d="M48 10c3-2 5-2 7 0-2 2-4 2-7 0ZM72 10c-3-2-5-2-7 0 2 2 4 2 7 0Z" fill="currentColor" opacity=".45" />
    </svg>
  );
}
