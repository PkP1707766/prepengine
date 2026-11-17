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

   A terracotta lamp seen from the front and a little above, the way you look
   down at one on a step: a round bowl pinched to a spout that points at you,
   the wick lying in the spout and the flame at its tip, centred inside the
   glow. Shaded the way a lamp in a dark room is lit: by its own flame.
   The lip and the far inside wall catch the most light, the oil holds the
   flame's reflection, the bowl rounds away into shadow, the floor around it
   is a warm pool, and that pool bounces a little light back up the bowl.

   Three stacked layers, so the costly part is painted once:
     back  — the light in the room: glow, soft rays, the lit floor, dust
     lamp  — still: bowl, scored grooves, shading, clay grain, oil, wick, petals
     fire  — animated: the flame, its bloom, the flicker of its light on the
             lip, the glowing wick end, sparks. Blended as light (screen).

   Nothing clips: the glow runs past the drawing's box and the hero clips.
   ============================================================ */
const FX = 120, FY = 118;   // the centre of the flame's light

const RIM = "M64 136C64 128 90 123 120 123C150 123 176 128 176 136C176 143 150 149 134 153C127 155 123 157.5 120 160C117 157.5 113 155 106 153C90 149 64 143 64 136Z";
const OPENING = "M71 136C71 130.5 94 127.6 120 127.6C146 127.6 169 130.5 169 136C169 141 148 146 133 149.6C127 151 123 153 120 155C117 153 113 151 107 149.6C92 146 71 141 71 136Z";
const OIL = "M77 138.5C77 134.4 97 132.4 120 132.4C143 132.4 163 134.4 163 138.5C163 142.2 146 146 132.5 148.8C127 150 123 151.8 120 153.4C117 151.8 113 150 107.5 148.8C94 146 77 142.2 77 138.5Z";
const BODY = "M65 138C67 160 90 181 120 181.5C150 181 173 160 175 138C174 144 150 150 134 154C127 156 123 158.5 120 161C117 158.5 113 156 106 154C90 150 66 144 65 138Z";
const LIP_FRONT = "M64 136C64 143 90 149 106 153C113 155 117 157.5 120 160C123 157.5 127 155 134 153C150 149 176 143 176 136";
const FLAME_EDGE = "M121.1 61.7C124.4 79.3 139.8 96.9 140.9 118.9C142 138.7 132.1 153 120 153C107.9 153 98 139.8 99.1 121.1C100.2 101.3 117.8 85.9 121.1 61.7Z";
const FLAME_OUT = "M121 70C124 86 138 102 139 122C140 140 131 153 120 153C109 153 100 141 101 124C102 106 118 92 121 70Z";
const FLAME_MID = "M120.6 88C123 100 132 112 133 125C134 139 128 149 120 149C112 149 106 140 107 127C108 114 118.5 104 120.6 88Z";
const FLAME_CORE = "M120.3 108C122 116 127 123 127.5 131C128 140 124.5 146 120 146C115.5 146 112.5 140 113 132C113.5 124 118.8 118 120.3 108Z";

/* Soft rays out of the flame, uneven in width and spacing so they read as
   light through haze rather than as a sunburst. */
const RAYS = Array.from({ length: 11 }, (_, i) => {
  const a = ((i * 27.7 + (i % 3) * 9) * Math.PI) / 180, w = (0.035 + (i % 4) * 0.018), r = 178;
  const p = (t) => `${(FX + Math.cos(t) * r).toFixed(1)} ${(FY + Math.sin(t) * r).toFixed(1)}`;
  return `M${FX} ${FY}L${p(a - w)}L${p(a + w)}Z`;
});

/* Marigold petals on the floor, lit by the pool. */
/* Motes of dust in the lamp's light: x, y, size, phase, seconds a drift. */
const MOTES = [
  [62, 96, 1.7, 0, 11], [182, 74, 1.3, 1.6, 13], [94, 56, 1.1, 3.1, 10], [200, 140, 1.5, 0.8, 12],
  [48, 150, 1.2, 2.4, 14], [152, 46, 1, 4, 9.5], [212, 100, 1.1, 5.2, 12.5], [74, 176, 1.4, 1.1, 13.5],
  [168, 168, 1.2, 6.3, 11.5], [124, 36, 0.9, 7.4, 10.5],
];

const PETALS = [
  [74, 189, -24, 4.2, 1.9, 0], [82, 194, 18, 3.6, 1.6, 0], [164, 190.5, 30, 4, 1.8, 0],
  [172, 186.5, -12, 3.4, 1.6, 1],
];

export function Diya({ size = 340, embers = true }) {
  const g = nextId("dg");
  const u = (n) => `url(#${g}-${n})`;
  const box = "28 32 184 184";
  return (
    <div className="ill-diya" style={{ "--d": `${size}px` }} aria-hidden="true" role="presentation">
      {/* ---- back: the light in the room ---- */}
      <svg className="ill-diya-back" viewBox={box} overflow="visible" fill="none" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <radialGradient id={`${g}-glow`} cx={FX} cy={FY} r="150" gradientUnits="userSpaceOnUse">
            <stop offset="0"   stopColor="#FFD58A" stopOpacity=".42" />
            <stop offset=".16" stopColor="#FFB45A" stopOpacity=".2" />
            <stop offset=".42" stopColor="#E9873A" stopOpacity=".075" />
            <stop offset=".72" stopColor="#C8642A" stopOpacity=".02" />
            <stop offset="1"   stopColor="#C8642A" stopOpacity="0" />
          </radialGradient>
          <radialGradient id={`${g}-ray`} cx={FX} cy={FY} r="178" gradientUnits="userSpaceOnUse">
            <stop offset="0"   stopColor="#FFE2A8" stopOpacity="0" />
            <stop offset=".1"  stopColor="#FFE2A8" stopOpacity=".075" />
            <stop offset=".45" stopColor="#FFC27A" stopOpacity=".025" />
            <stop offset="1"   stopColor="#FFC27A" stopOpacity="0" />
          </radialGradient>
          <radialGradient id={`${g}-mote`}>
            <stop offset="0"   stopColor="#FFE3B0" stopOpacity=".95" />
            <stop offset=".4"  stopColor="#FFC37A" stopOpacity=".4" />
            <stop offset="1"   stopColor="#FFC37A" stopOpacity="0" />
          </radialGradient>
          <radialGradient id={`${g}-pool`} cx={FX} cy="186" r="100" gradientUnits="userSpaceOnUse"
                          gradientTransform={`translate(${FX} 186) scale(1 .18) translate(${-FX} -186)`}>
            <stop offset="0"   stopColor="#FFB866" stopOpacity=".5" />
            <stop offset=".35" stopColor="#EE8C3E" stopOpacity=".2" />
            <stop offset=".7"  stopColor="#C8642A" stopOpacity=".06" />
            <stop offset="1"   stopColor="#C8642A" stopOpacity="0" />
          </radialGradient>
        </defs>
        <circle className="ill-glow" cx={FX} cy={FY} r="150" fill={u("glow")} />
        <g className="ill-rays" fill={u("ray")}>
          {RAYS.map((d, i) => <path key={i} d={d} />)}
        </g>
        <ellipse className="ill-pool" cx={FX} cy="186" rx="100" ry="18" fill={u("pool")} />
        {/* dust in the lamp's light, drifting up slowly */}
        {MOTES.map(([x, y, r, d, s], i) => (
          <circle key={i} className="ill-mote" cx={x} cy={y} r={r} fill={u("mote")}
                  style={{ animationDelay: `${-d}s`, animationDuration: `${s}s` }} />
        ))}
      </svg>

      {/* ---- lamp: still ---- */}
      <svg className="ill-diya-lamp" viewBox={box} overflow="visible" fill="none" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id={`${g}-clay`} x1="0" y1="138" x2="0" y2="182" gradientUnits="userSpaceOnUse">
            <stop offset="0"   stopColor="#CC6436" />
            <stop offset=".45" stopColor="#A9441D" />
            <stop offset="1"   stopColor="#5C200C" />
          </linearGradient>
          <radialGradient id={`${g}-form`} cx="117" cy="150" r="64" gradientUnits="userSpaceOnUse"
                          gradientTransform="translate(117 150) scale(1 .85) translate(-117 -150)">
            <stop offset="0"   stopColor="#1E0603" stopOpacity="0" />
            <stop offset=".55" stopColor="#1E0603" stopOpacity="0" />
            <stop offset="1"   stopColor="#1E0603" stopOpacity=".6" />
          </radialGradient>
          <linearGradient id={`${g}-top`} x1="0" y1="138" x2="0" y2="168" gradientUnits="userSpaceOnUse">
            <stop offset="0" stopColor="#FF9A5A" stopOpacity=".26" />
            <stop offset="1" stopColor="#FFB070" stopOpacity="0" />
          </linearGradient>
          <linearGradient id={`${g}-low`} x1="0" y1="158" x2="0" y2="182" gradientUnits="userSpaceOnUse">
            <stop offset="0" stopColor="#140402" stopOpacity="0" />
            <stop offset="1" stopColor="#140402" stopOpacity=".42" />
          </linearGradient>
          <radialGradient id={`${g}-lip`} cx="120" cy="152" r="78" gradientUnits="userSpaceOnUse"
                          gradientTransform="translate(120 152) scale(1 .42) translate(-120 -152)">
            <stop offset="0"   stopColor="#F08E58" />
            <stop offset=".42" stopColor="#C85C2C" />
            <stop offset="1"   stopColor="#7E2C12" />
          </radialGradient>
          <linearGradient id={`${g}-wall`} x1="0" y1="127" x2="0" y2="150" gradientUnits="userSpaceOnUse">
            <stop offset="0"   stopColor="#EA9058" />
            <stop offset=".35" stopColor="#A84A22" />
            <stop offset="1"   stopColor="#46200C" />
          </linearGradient>
          <radialGradient id={`${g}-oil`} cx="120" cy="146" r="48" gradientUnits="userSpaceOnUse"
                          gradientTransform="translate(120 146) scale(1 .45) translate(-120 -146)">
            <stop offset="0"   stopColor="#74390F" />
            <stop offset=".5"  stopColor="#3C1B08" />
            <stop offset="1"   stopColor="#1C0B04" />
          </radialGradient>
          <radialGradient id={`${g}-refl`} cx="120" cy="142.5" r="26" gradientUnits="userSpaceOnUse"
                          gradientTransform="translate(120 142.5) scale(1 .2) translate(-120 -142.5)">
            <stop offset="0" stopColor="#FFC873" stopOpacity=".6" />
            <stop offset="1" stopColor="#FFC873" stopOpacity="0" />
          </radialGradient>
          <radialGradient id={`${g}-streak`} cx="120" cy="142.5" r="6" gradientUnits="userSpaceOnUse"
                          gradientTransform="translate(120 142.5) scale(.8 1.2) translate(-120 -142.5)">
            <stop offset="0" stopColor="#FFF0C8" stopOpacity=".95" />
            <stop offset="1" stopColor="#FFC873" stopOpacity="0" />
          </radialGradient>
          <radialGradient id={`${g}-dark`}>
            <stop offset="0" stopColor="#0E0302" stopOpacity=".7" />
            <stop offset="1" stopColor="#0E0302" stopOpacity="0" />
          </radialGradient>
          <radialGradient id={`${g}-petal`} cx=".38" cy=".38" r=".75">
            <stop offset="0"   stopColor="#FFC24A" />
            <stop offset=".6"  stopColor="#EF8A1C" />
            <stop offset="1"   stopColor="#A9480C" />
          </radialGradient>
          <radialGradient id={`${g}-rose`} cx=".38" cy=".38" r=".75">
            <stop offset="0"   stopColor="#D8423C" />
            <stop offset="1"   stopColor="#7A1219" />
          </radialGradient>
          <clipPath id={`${g}-body`}><path d={BODY} /></clipPath>
          <filter id={`${g}-soft`} x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="1.8" />
          </filter>
          {/* Clay grain: dark specks and light ones, from one noise field. */}
          <filter id={`${g}-grain`} filterUnits="userSpaceOnUse" x="60" y="120" width="122" height="66">
            <feTurbulence type="fractalNoise" baseFrequency="1.15" numOctaves="2" seed="7" />
            <feColorMatrix values="0 0 0 0 .12  0 0 0 0 .05  0 0 0 0 .02  1.7 0 0 0 -.62" />
          </filter>
          <filter id={`${g}-fleck`} filterUnits="userSpaceOnUse" x="60" y="120" width="122" height="66">
            <feTurbulence type="fractalNoise" baseFrequency="1.4" numOctaves="1" seed="3" />
            <feColorMatrix values="0 0 0 0 1  0 0 0 0 .86  0 0 0 0 .68  -1.8 0 0 0 .52" />
          </filter>
        </defs>

        {/* where it touches the floor */}
        <ellipse cx="120" cy="184.5" rx="46" ry="6" fill={u("dark")} />
        <ellipse cx="120" cy="182.6" rx="28" ry="2.8" fill="#0E0302" opacity=".85" filter={u("soft")} />

        {PETALS.map(([x, y, r, rx, ry, red], i) => (
          <g key={i} transform={`rotate(${r} ${x} ${y})`}>
            <ellipse cx={x} cy={y + 0.9} rx={rx} ry={ry * 0.6} fill="#120403" opacity=".35" />
            <ellipse cx={x} cy={y} rx={rx} ry={ry} fill={u(red ? "rose" : "petal")} />
          </g>
        ))}

        {/* the bowl */}
        <ellipse cx="120" cy="181" rx="26" ry="4.6" fill="#5A2410" />
        <path d={BODY} fill={u("clay")} />
        <g clipPath={u("body")}>
          {/* bare clay, scored by hand with two grooves while it turned: each
              a dark cut with a lighter ridge just under it */}
          <path d="M67 145.6C80 157.6 98 164.1 120 164.6C142 164.1 160 157.6 173 145.6" stroke="#3A1206" strokeOpacity=".8" strokeWidth="1.5" />
          <path d="M67 146.8C80 158.8 98 165.3 120 165.8C142 165.3 160 158.8 173 146.8" stroke="#F59A66" strokeOpacity=".5" strokeWidth=".9" />
          <path d="M70 151.6C83 163 99 169.4 120 169.9C141 169.4 157 163 170 151.6" stroke="#3A1206" strokeOpacity=".7" strokeWidth="1.3" />
          <path d="M70 152.7C83 164.1 99 170.5 120 171C141 170.5 157 164.1 170 152.7" stroke="#F59A66" strokeOpacity=".42" strokeWidth=".8" />
          {/* shading over the clay */}
          <rect x="56" y="130" width="128" height="60" fill={u("form")} />
          <rect x="56" y="130" width="128" height="60" fill={u("top")} />
          <rect x="56" y="130" width="128" height="60" fill={u("low")} />
          {/* the glow behind the lamp catching both edges of the bowl */}
          <path d="M66.5 140C68 157 79 172 97 179.5" stroke="#FFB27A" strokeOpacity=".5" strokeWidth="2.4" filter={u("soft")} />
          <path d="M173.5 140C172 157 161 172 143 179.5" stroke="#FFB27A" strokeOpacity=".42" strokeWidth="2.4" filter={u("soft")} />
          {/* the shadow under the lip, and floor light bounced back up */}
          <path d={LIP_FRONT} transform="translate(0 3)" stroke="#1E0703" strokeOpacity=".6" strokeWidth="5" filter={u("soft")} />
          <path d="M70 152C75 169 95 180.5 120 181C145 180.5 165 169 170 152" stroke="#FF9E5A" strokeOpacity=".42"
                strokeWidth="3.4" filter={u("soft")} />
          <path d="M70 146C73 160 83 172 97 178" stroke="#FFE2C4" strokeOpacity=".2" strokeWidth="3" strokeLinecap="round" filter={u("soft")} />
          <rect x="60" y="120" width="122" height="66" filter={u("grain")} opacity=".7" />
          <rect x="60" y="120" width="122" height="66" filter={u("fleck")} opacity=".42" />
        </g>

        {/* the lip, lit from the flame above it */}
        <path d={RIM} fill={u("lip")} />
        <path d={LIP_FRONT} stroke="#5A220C" strokeOpacity=".75" strokeWidth="1.3" strokeLinecap="round" />
        <path d="M66 133C72 126.5 94 123.6 120 123.6C146 123.6 168 126.5 174 133" stroke="#FFD9A8" strokeOpacity=".55" strokeWidth="1" strokeLinecap="round" />

        {/* the inside: the far wall lit, then the oil, the flame lying in it */}
        <path d={OPENING} fill={u("wall")} />
        <path d={OPENING} stroke="#6A2A12" strokeOpacity=".55" strokeWidth=".9" />
        <path d={OIL} fill={u("oil")} />
        <path d="M78 137.6C84 134.2 100 132.6 120 132.6C140 132.6 156 134.2 162 137.6" stroke="#FFC890" strokeOpacity=".35" strokeWidth=".8" strokeLinecap="round" />
        <ellipse cx="120" cy="142.5" rx="26" ry="5" fill={u("refl")} />
        <ellipse cx="120" cy="142.5" rx="5" ry="7" fill={u("streak")} />
        {/* soot where the flame has licked the spout */}
        <ellipse cx="120" cy="155.6" rx="7.5" ry="3" fill={u("dark")} opacity=".7" />

        {/* the wick, oil-soaked */}
        <path d="M120 141C120 145 120 149 120 152.6" stroke="#3A2316" strokeWidth="3.6" strokeLinecap="round" />
        <path d="M119.3 141.5C119.3 145 119.3 148.5 119.3 151.5" stroke="#7A5638" strokeWidth=".9" strokeLinecap="round" strokeOpacity=".8" />
      </svg>

      {/* ---- fire: animated, added as light ---- */}
      <svg className="ill-diya-fire" viewBox={box} overflow="visible" fill="none" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <radialGradient id={`${g}-bloom`} cx={FX} cy="120" r="56" gradientUnits="userSpaceOnUse"
                          gradientTransform={`translate(${FX} 120) scale(.82 1.25) translate(${-FX} -120)`}>
            <stop offset="0"   stopColor="#FFC66E" stopOpacity=".55" />
            <stop offset=".4"  stopColor="#F59A42" stopOpacity=".2" />
            <stop offset="1"   stopColor="#E07A30" stopOpacity="0" />
          </radialGradient>
          <radialGradient id={`${g}-halo`} cx={FX} cy="126" r="26" gradientUnits="userSpaceOnUse"
                          gradientTransform={`translate(${FX} 126) scale(.8 1.35) translate(${-FX} -126)`}>
            <stop offset="0"   stopColor="#FFE7AE" stopOpacity=".7" />
            <stop offset="1"   stopColor="#FFB45A" stopOpacity="0" />
          </radialGradient>
          <radialGradient id={`${g}-lit`} cx="120" cy="150" r="62" gradientUnits="userSpaceOnUse"
                          gradientTransform="translate(120 150) scale(1 .5) translate(-120 -150)">
            <stop offset="0"   stopColor="#FFA060" stopOpacity=".32" />
            <stop offset="1"   stopColor="#FFB774" stopOpacity="0" />
          </radialGradient>
          <linearGradient id={`${g}-edge`} x1="0" y1="62" x2="0" y2="153" gradientUnits="userSpaceOnUse">
            <stop offset="0"  stopColor="#FF8A2A" stopOpacity="0" />
            <stop offset=".3" stopColor="#FF8A2A" stopOpacity=".35" />
            <stop offset="1"  stopColor="#D2470E" stopOpacity=".45" />
          </linearGradient>
          <linearGradient id={`${g}-flame`} x1="0" y1="70" x2="0" y2="154" gradientUnits="userSpaceOnUse">
            <stop offset="0"   stopColor="#FFB347" stopOpacity=".1" />
            <stop offset=".2"  stopColor="#FFAA40" stopOpacity=".9" />
            <stop offset=".65" stopColor="#FF8C26" />
            <stop offset=".9"  stopColor="#E85A12" />
            <stop offset="1"   stopColor="#B83A0C" stopOpacity=".7" />
          </linearGradient>
          <linearGradient id={`${g}-mid`} x1="0" y1="88" x2="0" y2="150" gradientUnits="userSpaceOnUse">
            <stop offset="0"   stopColor="#FFE08A" stopOpacity=".35" />
            <stop offset=".4"  stopColor="#FFEBAA" />
            <stop offset="1"   stopColor="#FFC155" />
          </linearGradient>
          <linearGradient id={`${g}-core`} x1="0" y1="108" x2="0" y2="147" gradientUnits="userSpaceOnUse">
            <stop offset="0"   stopColor="#FFFDF2" stopOpacity=".5" />
            <stop offset=".45" stopColor="#FFFDF2" />
            <stop offset="1"   stopColor="#FFF0C4" stopOpacity=".85" />
          </linearGradient>
          <radialGradient id={`${g}-blue`}>
            <stop offset="0" stopColor="#7C98FF" stopOpacity=".75" />
            <stop offset="1" stopColor="#4A62D8" stopOpacity="0" />
          </radialGradient>
          <radialGradient id={`${g}-ember`}>
            <stop offset="0"   stopColor="#FFD39A" />
            <stop offset=".5"  stopColor="#FF7A2A" />
            <stop offset="1"   stopColor="#FF5A1A" stopOpacity="0" />
          </radialGradient>
          <clipPath id={`${g}-litclip`}><path d={RIM} /><path d={BODY} /></clipPath>
        </defs>

        {/* the flame's light flickering on the lip and the bowl */}
        <g clipPath={u("litclip")} className="ill-gustlit">
          <ellipse className="ill-litflick" cx="120" cy="150" rx="62" ry="31" fill={u("lit")} />
        </g>

        {/* everything the wind leans: bloom, flame, halo */}
        <g className="ill-gust">
        <ellipse className="ill-aura" cx={FX} cy="120" rx="46" ry="70" fill={u("bloom")} />
        <g className="ill-flame">
          <path d={FLAME_EDGE} fill={u("edge")} />
          <path d={FLAME_OUT} fill={u("flame")} />
          <path d={FLAME_MID} fill={u("mid")} />
          <path className="ill-flame-core" d={FLAME_CORE} fill={u("core")} />
          <ellipse cx="120" cy="149.5" rx="6.5" ry="4" fill={u("blue")} />
        </g>
        <ellipse className="ill-aura" cx={FX} cy="126" rx="21" ry="35" fill={u("halo")} />
        </g>
        {/* the end of the wick, glowing under the flame */}
        <ellipse cx="120" cy="152.2" rx="3.2" ry="2.4" fill={u("ember")} />

        {embers && (
          <g className="ill-embers" fill="#FFD9A0">
            <circle className="ill-ember ill-ember-1" cx="114" cy="80" r="1.5" />
            <circle className="ill-ember ill-ember-2" cx="128" cy="74" r="1.1" />
            <circle className="ill-ember ill-ember-3" cx="121" cy="64" r="0.9" />
            <circle className="ill-ember ill-ember-4" cx="124" cy="90" r="1.3" />
            <circle className="ill-ember ill-ember-5" cx="110" cy="70" r="0.8" />
            <circle className="ill-ember ill-ember-6" cx="131" cy="84" r="1" />
          </g>
        )}
      </svg>
    </div>
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
