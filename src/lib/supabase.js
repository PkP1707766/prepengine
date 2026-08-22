import { createClient } from "@supabase/supabase-js";

const URL = import.meta.env.VITE_SUPABASE_URL;
const ANON = import.meta.env.VITE_SUPABASE_ANON_KEY;

/**
 * One client for the whole app. The previous code created a fresh client on
 * every call, which meant each screen had its own auth listener and token
 * refresh timer.
 */
let client = null;

export function getSupabaseSync() {
  if (client) return client;
  if (!URL || !ANON) return null;
  client = createClient(URL, ANON, {
    auth: {
      persistSession: true,
      autoRefreshToken: true,
      detectSessionInUrl: true,
      // Deliberately NOT setting a custom `storageKey`: changing it would
      // invalidate the stored token of every user who is already signed in and
      // silently log them all out on the next deploy.
    },
    global: { headers: { "x-application-name": "junoonias-web" } },
  });
  return client;
}

/** Kept async because most call sites already `await` it. */
export async function getSupabase() {
  const sb = getSupabaseSync();
  if (!sb) throw new Error("Supabase is not configured. Set VITE_SUPABASE_URL and VITE_SUPABASE_ANON_KEY.");
  return sb;
}

export const isSupabaseConfigured = () => Boolean(URL && ANON);
