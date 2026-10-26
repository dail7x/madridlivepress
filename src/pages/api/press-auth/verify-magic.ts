import type { APIRoute } from 'astro';
import {
  getPendingVerificationByToken,
  completeVerification,
  createSessionToken,
} from '@/lib/pressAuth';

export const prerender = false;

export const GET: APIRoute = async ({ url, cookies, redirect }) => {
  const token = url.searchParams.get('token');
  const redirectTarget = url.searchParams.get('redirect') || '/comunicados';

  if (!token) {
    return redirect(`${redirectTarget}?auth_error=missing_token`);
  }

  const pending = getPendingVerificationByToken(token);
  if (!pending) {
    return redirect(`${redirectTarget}?auth_error=invalid_or_expired`);
  }

  const user = await completeVerification(pending.email);
  if (!user) {
    return redirect(`${redirectTarget}?auth_error=verification_failed`);
  }

  const sessionToken = createSessionToken(user);

  cookies.set('mlp_press_session', sessionToken, {
    path: '/',
    httpOnly: true,
    secure: import.meta.env.PROD,
    sameSite: 'lax',
    maxAge: 90 * 24 * 60 * 60,
  });

  return redirect(redirectTarget);
};
