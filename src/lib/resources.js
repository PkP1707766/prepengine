import {
  BookOpen, FileText, FolderOpen, Newspaper, HelpCircle, GraduationCap,
} from "lucide-react";

/* The public content hub's index. Kept out of the component file so hot
   reload doesn't tear down the whole page when only copy changes.
 *
 * Labels are dictionary KEYS, not English text. They used to be literal
 * strings, which is why the whole free-resources band stayed English no
 * matter what the language toggle said. The component resolves them with
 * t(); the Hindi lives in i18n.jsx alongside every other string. */

export const RESOURCES = [
  { key: "syllabus",  icon: BookOpen,      labelKey: "res_syllabus_l",  blurbKey: "res_syllabus_b" },
  { key: "pyq",       icon: FileText,      labelKey: "res_pyq_l",       blurbKey: "res_pyq_b" },
  { key: "materials", icon: FolderOpen,    labelKey: "res_materials_l", blurbKey: "res_materials_b" },
  { key: "ncert",     icon: GraduationCap, labelKey: "res_ncert_l",     blurbKey: "res_ncert_b" },
  { key: "news",      icon: Newspaper,     labelKey: "res_news_l",      blurbKey: "res_news_b" },
  { key: "faq",       icon: HelpCircle,    labelKey: "res_faq_l",       blurbKey: "res_faq_b" },
];

export const RESOURCE_KEYS = RESOURCES.map((r) => r.key);

/* Page headers for each standalone content page, same arrangement. */
export const RESOURCE_TITLES = {
  syllabus:  { tKey: "rt_syllabus_t",  sKey: "rt_syllabus_s" },
  pyq:       { tKey: "rt_pyq_t",       sKey: "rt_pyq_s" },
  materials: { tKey: "rt_materials_t", sKey: "rt_materials_s" },
  ncert:     { tKey: "rt_ncert_t",     sKey: "rt_ncert_s" },
  news:      { tKey: "rt_news_t",      sKey: "rt_news_s" },
  faq:       { tKey: "rt_faq_t",       sKey: "rt_faq_s" },
};
