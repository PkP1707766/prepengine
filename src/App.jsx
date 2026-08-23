import { useState, useEffect, useCallback } from "react";
import { AppProviders } from "./lib/i18n.jsx";
import { DiyaLogo } from "./ui/Brand.jsx";
import ErrorBoundary from "./ui/ErrorBoundary.jsx";
import { getSupabase, isSupabaseConfigured } from "./lib/supabase.js";
import {
  hasActiveAccess, ensureProfile, enableFixtures,
  capturePendingReferral, claimPendingReferral,
} from "./lib/db.js";

import PublicSite from "./screens/PublicSite.jsx";
import { PAGE_KEYS } from "./lib/resources.js";
import LoginScreen from "./screens/LoginScreen.jsx";
import JoinScreen from "./screens/JoinScreen.jsx";
import StudentApp from "./screens/StudentApp.jsx";
import AdminApp from "./screens/AdminApp.jsx";
import ExamApp from "./screens/ExamApp.jsx";

/* ============================================================
   Splash — shown while the session is being resolved.
   ============================================================ */
function Splash({ label = "JUNOONIAS" }) {
  return (
    <div style={{
      minHeight: "100vh", display: "grid", placeItems: "center",
      background: "linear-gradient(160deg,#f6ead0,#e7cfa6)", color: "#6b1a1a",
      fontFamily: 'var(--font-body,system-ui)',
    }}>
      <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 14 }}>
        <div style={{ animation: "jn-breathe 2.2s ease-in-out infinite" }}><DiyaLogo size={56} ring /></div>
        <div style={{ fontFamily: 'var(--font-display,serif)', letterSpacing: ".2em", fontWeight: 600 }}>{label}</div>
      </div>
    </div>
  );
}

/* ============================================================
   Configuration guard — a missing env var used to surface as a
   blank screen with a console error nobody would see.
   ============================================================ */
function MisconfiguredNotice() {
  return (
    <div style={{
      minHeight: "100vh", display: "grid", placeItems: "center", padding: 24,
      background: "#fdf6e3", fontFamily: 'var(--font-body,system-ui)', color: "#5b1414",
    }}>
      <div style={{ maxWidth: 480, textAlign: "center" }}>
        <DiyaLogo size={52} ring />
        <h1 style={{ fontFamily: 'var(--font-display,serif)', fontSize: 20, marginTop: 16 }}>Site not configured</h1>
        <p style={{ fontSize: 14.5, lineHeight: 1.7, color: "#7a6450" }}>
          <code>VITE_SUPABASE_URL</code> and <code>VITE_SUPABASE_ANON_KEY</code> are missing from this
          deployment's environment variables. Add them in the Vercel project settings and redeploy.
        </p>
      </div>
    </div>
  );
}

/* ============================================================
   ROOT ROUTER

   The site is public by default. A visitor lands on the
   storefront, browses every test series and its price, and is
   only asked to sign in at the moment they choose to enrol —
   the pattern every established coaching platform uses. The app
   used to open straight onto a login form, so a first-time
   visitor saw nothing at all before being asked for an account.

   Routes are mirrored into the URL hash so refresh, back and
   shared links all land where the user was.
   ============================================================ */
const HASH_ROUTES = {
  public: "#/",
  login: "#/signin",
  join: "#/join",
  student: "#/dashboard",
  admin: "#/admin",
  exam: "#/exam",
};

/* ============================================================
   DEV-ONLY responsiveness harness.

   #/__dev/student · #/__dev/admin · #/__dev/exam

   Mounts the real authenticated screens against fixture data so
   their layout can be measured at every breakpoint. Stripped from
   production builds by the import.meta.env.DEV guard.
   ============================================================ */
function DevHarness() {
  const [ready, setReady] = useState(false);
  const which = window.location.hash.split("/")[2] || "student";

  useEffect(() => {
    let alive = true;
    enableFixtures().then((ok) => { if (alive) setReady(!!ok); });
    return () => { alive = false; };
  }, []);

  if (!ready) return <Splash label="DEV HARNESS" />;
  const noop = () => {};
  if (which === "admin") return <AdminApp onLogout={noop} />;
  if (which === "exam") return <ExamApp testId="fx-test-0" onExit={noop} />;
  return <StudentApp onLaunchExam={noop} onBrowse={noop} onLogout={noop} />;
}

function Root() {
  const [route, setRoute] = useState("public");
  const [contentPage, setContentPage] = useState(null); // syllabus | pyq | … | faq
  const [examTestId, setExamTestId] = useState(null);
  const [pendingPlan, setPendingPlan] = useState(null); // bundle the visitor chose before signing in
  const [session, setSession] = useState(null);
  const [booting, setBooting] = useState(true);

  /* A referral link (?ref=CODE) is read on load, long before there is any
     account to attach it to. The visitor is usually here to browse; the code
     waits in local storage until they eventually sign up, surviving the trip
     through Google OAuth or an emailed magic link.

     Declared above the boot effect on purpose — effects fire in declaration
     order, so the code is in storage before the session resolve below reaches
     claimPendingReferral(). */
  useEffect(() => { capturePendingReferral(); }, []);

  /** Where does a signed-in user belong? */
  const resolveDestination = useCallback(async (sb) => {
    const { data: { user } } = await sb.auth.getUser();
    if (!user) return "public";
    const profile = await ensureProfile(user).catch(() => null);
    // The profile row has to exist before a referral can point at it — the
    // binding is a foreign key to it. Idempotent, so calling it on every
    // resolve is harmless and covers OAuth returns as well as fresh signups.
    claimPendingReferral();
    if (profile?.role === "admin") return "admin";
    return (await hasActiveAccess(user.id)) ? "student" : "join";
  }, []);

  const go = useCallback((next, opts = {}) => {
    setRoute(next);
    if (next === "exam") setExamTestId(opts.testId ?? null);
    if (next !== "public") setContentPage(null);
    const hash = next === "exam" && opts.testId ? `#/exam/${opts.testId}` : HASH_ROUTES[next] || "#/";
    if (window.location.hash !== hash) window.history.pushState(null, "", hash);
    if (opts.scrollTop !== false) window.scrollTo({ top: 0 });
  }, []);

  /* Each content page gets a real, shareable URL of its own — that is what
     section 3 of the spec means by "standalone public page". */
  const openContent = useCallback((key) => {
    setContentPage(key);
    setRoute("public");
    const hash = key ? `#/${key}` : "#/";
    if (window.location.hash !== hash) window.history.pushState(null, "", hash);
    window.scrollTo({ top: 0 });
  }, []);

  /* Boot: resolve any existing session, then honour the deep link. */
  useEffect(() => {
    let alive = true;
    (async () => {
      if (!isSupabaseConfigured()) { if (alive) setBooting(false); return; }
      try {
        const sb = await getSupabase();
        const { data: { session: s } } = await sb.auth.getSession();
        if (!alive) return;
        setSession(s ?? null);

        const hash = window.location.hash;
        const contentKey = hash.replace(/^#\//, "");
        if (PAGE_KEYS.includes(contentKey)) { setContentPage(contentKey); setRoute("public"); }
        if (s) {
          const dest = await resolveDestination(sb);
          const m = hash.match(/^#\/exam\/([\w-]+)$/);
          if (dest === "student" && m) { setExamTestId(m[1]); setRoute("exam"); }
          // A signed-in visitor who deep-linked to the storefront stays there —
          // browsing the catalogue while logged in is perfectly normal.
          else if (hash === "#/" || hash === "" || PAGE_KEYS.includes(contentKey)) setRoute("public");
          else go(dest);
        } else if (hash === "#/signin") {
          setRoute("login");
        }
      } catch (e) {
        console.error("session boot failed", e);
      }
      if (alive) setBooting(false);
    })();
    return () => { alive = false; };
  }, [resolveDestination, go]);

  /* Keep the app in step with sign-out from another tab. */
  useEffect(() => {
    if (!isSupabaseConfigured()) return;
    let sub;
    (async () => {
      const sb = await getSupabase();
      const { data } = sb.auth.onAuthStateChange((event, s) => {
        setSession(s ?? null);
        if (event === "SIGNED_OUT") go("public");
      });
      sub = data?.subscription;
    })();
    return () => sub?.unsubscribe();
  }, [go]);

  /* Browser back / forward. */
  useEffect(() => {
    const onPop = () => {
      const h = window.location.hash;
      if (h.startsWith("#/exam/")) return; // leaving an exam is confirmed inside the exam screen
      const key = h.replace(/^#\//, "");
      if (PAGE_KEYS.includes(key)) { setContentPage(key); setRoute("public"); return; }
      setContentPage(null);
      const hit = Object.entries(HASH_ROUTES).find(([, v]) => v === h);
      if (hit && hit[0] !== "exam") setRoute(hit[0]);
      else if (h === "" || h === "#/") setRoute("public");
    };
    window.addEventListener("popstate", onPop);
    return () => window.removeEventListener("popstate", onPop);
  }, []);

  /* After a successful sign-in. If they came from an "Enroll now" click, take
     them straight to checkout for that bundle rather than dumping them on a
     generic dashboard. */
  const afterAuth = useCallback(async () => {
    try {
      const sb = await getSupabase();
      const { data: { session: s } } = await sb.auth.getSession();
      setSession(s ?? null);
      const dest = await resolveDestination(sb);
      if (pendingPlan && dest === "join") go("join");
      else go(dest);
    } catch {
      go("join");
    }
  }, [resolveDestination, go, pendingPlan]);

  /* "Enroll now" from the storefront. */
  const startEnrolment = useCallback((planCode) => {
    setPendingPlan(planCode);
    if (session) go("join");
    else go("login");
  }, [session, go]);

  const openDashboard = useCallback(async () => {
    if (!session) return go("login");
    try {
      const sb = await getSupabase();
      go(await resolveDestination(sb));
    } catch {
      go("join");
    }
  }, [session, resolveDestination, go]);

  const logout = useCallback(async () => {
    try { const sb = await getSupabase(); await sb.auth.signOut(); } catch { /* already gone */ }
    setSession(null);
    setPendingPlan(null);
    go("public");
  }, [go]);

  if (import.meta.env.DEV && window.location.hash.startsWith("#/__dev/")) {
    return <ErrorBoundary label="dev-harness"><DevHarness /></ErrorBoundary>;
  }
  if (!isSupabaseConfigured()) return <MisconfiguredNotice />;
  if (booting) return <Splash />;

  switch (route) {
    case "public":
      return (
        <ErrorBoundary label="public">
          <PublicSite
            session={session}
            page={contentPage}
            onNavigate={openContent}
            onLogin={() => go("login")}
            onEnroll={startEnrolment}
            onDashboard={openDashboard}
          />
        </ErrorBoundary>
      );
    case "login":
      return (
        <LoginScreen
          onStudent={afterAuth}
          onAdmin={afterAuth}
          onBack={() => go("public")}
        />
      );
    case "join":
      return (
        <JoinScreen
          planCode={pendingPlan}
          onJoined={() => { setPendingPlan(null); go("student"); }}
          onBrowse={() => go("public")}
          onLogout={logout}
        />
      );
    case "student":
      return (
        <ErrorBoundary label="student">
          <StudentApp
            onLaunchExam={(testId) => go("exam", { testId })}
            onBrowse={() => go("public")}
            onLogout={logout}
          />
        </ErrorBoundary>
      );
    case "exam":
      return (
        <ErrorBoundary label="exam">
          <ExamApp testId={examTestId} onExit={() => go("student")} />
        </ErrorBoundary>
      );
    case "admin":
      return (
        <ErrorBoundary label="admin">
          <AdminApp onLogout={logout} />
        </ErrorBoundary>
      );
    default:
      return <Splash />;
  }
}

export default function App() {
  return (
    <ErrorBoundary label="root">
      <AppProviders>
        <Root />
      </AppProviders>
    </ErrorBoundary>
  );
}
