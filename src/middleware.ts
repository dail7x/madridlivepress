import { defineMiddleware } from 'astro:middleware';

export const onRequest = defineMiddleware(async ({ request }, next) => {
  const response = await next();

  // Allow Directus Admin to embed the website in an iframe for Live Preview and Visual Editor
  response.headers.set(
    'Content-Security-Policy',
    "frame-ancestors 'self' https://mlpdirectus.116.203.118.1.sslip.io"
  );
  response.headers.delete('x-frame-options');
  response.headers.delete('X-Frame-Options');

  return response;
});
