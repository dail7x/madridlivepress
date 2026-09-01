import type { APIRoute } from 'astro';

export const prerender = false;

export const GET: APIRoute = async ({ url, redirect }) => {
  const slug = url.searchParams.get('slug') || '/';
  const token = url.searchParams.get('token') || '';

  // Redirect to target page with preview query parameter
  const targetUrl = new URL(slug.startsWith('/') ? slug : `/${slug}`, url.origin);
  targetUrl.searchParams.set('preview', 'true');
  if (token) {
    targetUrl.searchParams.set('token', token);
  }

  return redirect(targetUrl.toString(), 307);
};
