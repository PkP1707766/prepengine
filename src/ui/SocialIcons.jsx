/* Brand glyphs for the footer.
 *
 * lucide-react v1 dropped its brand icons (Instagram, Youtube, Linkedin and
 * friends are simply not exported any more — the build fails on the import
 * rather than falling back), so these are drawn here. Kept deliberately plain:
 * single-colour marks on currentColor, sized by the `size` prop, so they take
 * the footer's hover colour like any other icon.
 */

const box = (size) => ({ width: size, height: size, display: "block" });

export function Instagram({ size = 17 }) {
  return (
    <svg viewBox="0 0 24 24" style={box(size)} fill="none" stroke="currentColor"
         strokeWidth="1.9" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
      <rect x="2.5" y="2.5" width="19" height="19" rx="5.4" />
      <circle cx="12" cy="12" r="4.1" />
      <circle cx="17.4" cy="6.6" r="1.05" fill="currentColor" stroke="none" />
    </svg>
  );
}

export function YouTube({ size = 17 }) {
  return (
    <svg viewBox="0 0 24 24" style={box(size)} fill="none" stroke="currentColor"
         strokeWidth="1.9" strokeLinejoin="round" aria-hidden="true">
      <rect x="1.8" y="5" width="20.4" height="14" rx="4.4" />
      <path d="M10.2 9.1v5.8l5-2.9-5-2.9Z" fill="currentColor" stroke="none" />
    </svg>
  );
}

export function Telegram({ size = 17 }) {
  return (
    <svg viewBox="0 0 24 24" style={box(size)} fill="none" stroke="currentColor"
         strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
      <path d="M21.3 4.1 2.9 11.2c-.7.3-.7 1.2 0 1.4l4.6 1.5 1.8 5.2c.2.6 1 .7 1.4.2l2.4-2.7 4.6 3.4c.5.4 1.3.1 1.4-.6l2.9-14.6c.1-.7-.6-1.2-1.2-.9Z" />
      <path d="M7.5 14.1 18.6 6.4l-7.9 8.9-.2 3.6" />
    </svg>
  );
}

export function WhatsApp({ size = 17 }) {
  return (
    <svg viewBox="0 0 24 24" style={box(size)} fill="none" stroke="currentColor"
         strokeWidth="1.85" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
      <path d="M3.2 20.8l1.3-4.5a8.4 8.4 0 1 1 3.3 3.2l-4.6 1.3Z" />
      <path d="M9 8.6c.3-.1.6 0 .8.3l.8 1.3c.1.2.1.5 0 .7l-.5.7c-.1.2-.1.4 0 .6.5.8 1.2 1.5 2 2 .2.1.4.1.6 0l.7-.5c.2-.1.5-.2.7 0l1.3.8c.3.2.4.5.3.8-.2.7-.9 1.2-1.7 1.2-2.6-.2-5.2-2.8-5.4-5.4 0-.8.5-1.4 1.2-1.6Z"
            fill="currentColor" stroke="none" />
    </svg>
  );
}

export function LinkedIn({ size = 17 }) {
  return (
    <svg viewBox="0 0 24 24" style={box(size)} fill="none" stroke="currentColor"
         strokeWidth="1.9" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
      <rect x="2.5" y="2.5" width="19" height="19" rx="4.2" />
      <path d="M7.1 10.4v6.4M7.1 7.3v.1" />
      <path d="M11.3 16.8v-6.4M11.3 12.8c0-1.4.9-2.4 2.2-2.4s2.2 1 2.2 2.4v4" />
    </svg>
  );
}

export function XMark({ size = 17 }) {
  return (
    <svg viewBox="0 0 24 24" style={box(size)} fill="none" stroke="currentColor"
         strokeWidth="1.95" strokeLinecap="round" aria-hidden="true">
      <path d="M4.2 3.8 19.8 20.2M19.8 3.8 4.2 20.2" />
    </svg>
  );
}
