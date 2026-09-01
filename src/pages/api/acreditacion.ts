import type { APIRoute } from 'astro';
import { directus } from '@/lib/directus';
import { createItem } from '@directus/sdk';

export const prerender = false;

export const POST: APIRoute = async ({ request }) => {
  try {
    const body = await request.json();
    const {
      medio,
      periodista_nombre,
      periodista_email,
      periodista_telefono,
      pais,
      tipo_medio,
      evento,
      observaciones,
    } = body || {};

    if (!medio || !periodista_nombre || !periodista_email) {
      return new Response(
        JSON.stringify({ success: false, message: 'Faltan campos obligatorios para procesar la acreditación.' }),
        { status: 400, headers: { 'Content-Type': 'application/json' } }
      );
    }

    await directus.request(
      createItem('solicitudes_acreditacion' as any, {
        medio,
        periodista_nombre,
        periodista_email,
        periodista_telefono: periodista_telefono || '',
        pais: pais || 'España',
        tipo_medio: tipo_medio || 'Digital',
        evento: evento ? Number(evento) : null,
        observaciones: observaciones || '',
        estado: 'pendiente',
      })
    );

    return new Response(
      JSON.stringify({
        success: true,
        message: 'Solicitud de acreditación registrada con éxito. NocheMadrid contactará con su redacción en menos de 24 horas.',
      }),
      { status: 200, headers: { 'Content-Type': 'application/json' } }
    );
  } catch (error: any) {
    console.error('Error in /api/acreditacion:', error);
    return new Response(
      JSON.stringify({ success: false, message: 'Error al registrar la solicitud de acreditación.' }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
};
