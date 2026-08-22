// Allowed browser origins for the JUNOONIAS edge functions.
// Set ALLOWED_ORIGINS as a comma-separated list in the function secrets, e.g.
//   ALLOWED_ORIGINS="https://junoonias.com,https://www.junoonias.com"
// Anything not listed gets no CORS headers back, so a rogue site cannot call
// these endpoints with a logged-in user's cookies.
const DEV_ORIGINS = ["http://localhost:5173", "http://127.0.0.1:5173"];

function allowList(): string[] {
  const raw = Deno.env.get("ALLOWED_ORIGINS") ?? "";
  const listed = raw.split(",").map((s) => s.trim()).filter(Boolean);
  return [...listed, ...DEV_ORIGINS];
}

export function corsHeaders(req: Request): Record<string, string> {
  const origin = req.headers.get("origin") ?? "";
  const allowed = allowList();
  // A Vercel preview deployment for this project is also accepted.
  const ok = allowed.includes(origin) || /^https:\/\/[a-z0-9-]+\.vercel\.app$/.test(origin);
  return {
    "Access-Control-Allow-Origin": ok ? origin : allowed[0] ?? "",
    "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Vary": "Origin",
  };
}

export function json(req: Request, body: unknown, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...corsHeaders(req), "Content-Type": "application/json" },
  });
}

export function preflight(req: Request): Response | null {
  if (req.method === "OPTIONS") return new Response("ok", { headers: corsHeaders(req) });
  return null;
}
