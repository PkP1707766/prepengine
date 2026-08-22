import { createContext, useContext } from "react";

/* Contexts live apart from the components that provide them so that editing a
   screen doesn't blow away app-wide state during hot reload. */

export const LangCtx = createContext({ lang: "en", t: (k) => k, setLang: () => {} });
export const useLang = () => useContext(LangCtx);

export const ThemeCtx = createContext({ theme: "light", toggle: () => {} });
export const useTheme = () => useContext(ThemeCtx);

/* The colour ways. `swatch` is the honest two-second preview of each: the
   brand mid-tone over that palette's own cream. */
export const PALETTES = [
  { key: "ember",    label: "Ember",    hint: "Maroon & gold", brand: "#631322", cream: "#fbf6ec" },
  { key: "indigo",   label: "Indigo",   hint: "Deep blue",     brand: "#2b3a76", cream: "#f7f6f0" },
  { key: "sapphire", label: "Sapphire", hint: "आसमानी",         brand: "#0f5079", cream: "#f6f8f6" },
  { key: "amethyst", label: "Amethyst", hint: "Aubergine",     brand: "#552271", cream: "#faf6f6" },
  { key: "forest",   label: "Forest",   hint: "Deep green",    brand: "#215139", cream: "#f8f7ee" },
];
