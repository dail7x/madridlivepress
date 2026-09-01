import type { APIRoute } from 'astro';
import { directus } from '@/lib/directus';
import { createItem } from '@directus/sdk';

export const prerender = false;

export const POST: APIRoute = async ({ request }) => {
  try {
    const body = await request.json();
    const email = body?.email?.trim();

    if (!email || !email.includes('@')) {
      return new Response(
        JSON.stringify({ success: false, message: 'Por favor, introduce un correo electrónico corporativo válido.' }),
        { status: 400, headers: { 'Content-Type': 'application/json' } }
      );
    }

    await directus.request(
      createItem('suscripciones_prensa' as any, {
        email,
        medio: body?.medio || 'Redacción / Periodista Freelance',
        pais: body?.pais || 'España',
      })
    );

    return new Response(
      JSON.stringify({ success: true, message: 'Suscripción completada correctamente.' }),
      { status: 200, headers: { 'Content-Type': 'application/json' } }
    );
  } catch (error: any) {
    console.error('Error in /api/newsletter:', error);
    return new Response(
      JSON.stringify({ success: false, message: 'Error interno al registrar la suscripción.' }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
};
