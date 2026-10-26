import { defineMiddleware } from 'astro:middleware';
import { verifySessionToken, isSearchOrAiBot } from '@/lib/pressAuth';

export const onRequest = defineMiddleware(async ({ request, cookies, locals }, next) => {
  // 1. Detect AI / Search Bots
  const userAgent = request.headers.get('user-agent') || '';
  locals.isBot = isSearchOrAiBot(userAgent);

  // 2. Validate Press Session Cookie
  const sessionCookie = cookies.get('mlp_press_session')?.value;
  if (sessionCookie) {
    const user = verifySessionToken(sessionCookie);
    locals.pressUser = user;
  } else {
    locals.pressUser = null;
  }

  const response = await next();

  // 3. Allow Directus Admin to embed the website in an iframe for Live Preview and Visual Editor
  response.headers.set(
    'Content-Security-Policy',
    "frame-ancestors 'self' https://mlpdirectus.116.203.118.1.sslip.io"
  );
  response.headers.delete('x-frame-options');
  response.headers.delete('X-Frame-Options');

  return response;
});
