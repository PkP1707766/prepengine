import {
  BookOpen, FileText, FolderOpen, Newspaper, HelpCircle, GraduationCap,
} from "lucide-react";

/* The public content hub's index. Kept out of the component file so hot
   reload doesn't tear down the whole page when only copy changes. */

export const RESOURCES = [
  { key: "syllabus",  label: "Syllabus",              icon: BookOpen,      blurb: "Full UPSC / BPSC / UPPCS syllabus, topic by topic." },
  { key: "pyq",       label: "Previous Year Papers",  icon: FileText,      blurb: "Solved papers going back several attempts." },
  { key: "materials", label: "Free Materials",        icon: FolderOpen,    blurb: "Notes and PDFs, free to download." },
  { key: "ncert",     label: "NCERT Books",           icon: GraduationCap, blurb: "Class 6–12 NCERTs, organised by subject." },
  { key: "news",      label: "Daily Current Affairs", icon: Newspaper,     blurb: "Today's news, filtered for what's exam-relevant." },
  { key: "faq",       label: "FAQ",                   icon: HelpCircle,    blurb: "Tests, payments, access and refunds." },
];

export const RESOURCE_KEYS = RESOURCES.map((r) => r.key);

export const RESOURCE_TITLES = {
  syllabus:  { t: "Syllabus",                   s: "What each exam actually asks of you" },
  pyq:       { t: "Previous Year Papers",       s: "The best predictor of what comes next" },
  materials: { t: "Free Study Material",        s: "Open to everyone, no account needed" },
  ncert:     { t: "NCERT Books",                s: "The foundation every serious aspirant starts from" },
  news:      { t: "Daily Current Affairs",      s: "Filtered for what the exam actually asks" },
  faq:       { t: "Frequently Asked Questions", s: "Tests, payments, access and refunds" },
};
