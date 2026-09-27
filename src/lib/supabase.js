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
    // No custom global headers: supabase-js sends them on edge-function calls
    // too, and a header missing from the functions' CORS allow-list
    // (_shared/cors.ts) makes the browser refuse the preflight. An
    // "x-application-name" header here blocked submit-attempt, coupon-check,
    // join-order and verify-payment for every browser from 02ec704 onwards.
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
