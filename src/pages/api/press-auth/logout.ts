import type { APIRoute } from 'astro';

export const prerender = false;

export const POST: APIRoute = async ({ cookies }) => {
  cookies.delete('mlp_press_session', { path: '/' });
  return new Response(JSON.stringify({ success: true, message: 'Sesión cerrada.' }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' },
  });
};

export const GET: APIRoute = async ({ cookies, url, redirect }) => {
  cookies.delete('mlp_press_session', { path: '/' });
  const redirectTarget = url.searchParams.get('redirect') || '/comunicados';
  return redirect(redirectTarget);
};
