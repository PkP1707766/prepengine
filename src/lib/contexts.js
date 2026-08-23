import { createContext, useContext } from "react";

/* Contexts live apart from the components that provide them so that editing a
   screen doesn't blow away app-wide state during hot reload. */

export const LangCtx = createContext({ lang: "en", t: (k) => k, setLang: () => {} });
export const useLang = () => useContext(LangCtx);

export const ThemeCtx = createContext({ theme: "light", toggle: () => {} });
export const useTheme = () => useContext(ThemeCtx);

/* The colour ways. `swatch` is the honest two-second preview of each: the
   brand mid-tone over that palette's own cream. */
/* Both names are carried per palette rather than being looked up by key in the
   dictionary, because the swatch colours live here and a reader editing a
   palette should see its two names in the same line as its hex.

   Sapphire's English hint used to read "आसमानी" — a Hindi word stranded in the
   English column, and the wrong shade besides: #0f5079 is a sea blue, not a
   sky blue. Both columns are now stated deliberately. */
export const PALETTES = [
  { key: "ember",    label: "Ember",    labelHi: "अंगार", hint: "Maroon & gold", hintHi: "मैरून और सुनहरा", brand: "#631322", cream: "#fbf6ec" },
  { key: "indigo",   label: "Indigo",   labelHi: "नील",   hint: "Deep blue",     hintHi: "गहरा नीला",       brand: "#2b3a76", cream: "#f7f6f0" },
  { key: "sapphire", label: "Sapphire", labelHi: "नीलम",  hint: "Ocean blue",    hintHi: "समुद्री नीला",     brand: "#0f5079", cream: "#f6f8f6" },
  { key: "amethyst", label: "Amethyst", labelHi: "जामुनी", hint: "Aubergine",     hintHi: "गहरा बैंगनी",      brand: "#552271", cream: "#faf6f6" },
  { key: "forest",   label: "Forest",   labelHi: "वन",    hint: "Deep green",    hintHi: "गहरा हरा",        brand: "#215139", cream: "#f8f7ee" },
];
