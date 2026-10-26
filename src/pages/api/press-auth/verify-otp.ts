import type { APIRoute } from 'astro';
import {
  getPendingVerificationByEmail,
  completeVerification,
  createSessionToken,
} from '@/lib/pressAuth';

export const prerender = false;

export const POST: APIRoute = async ({ request, cookies }) => {
  try {
    const body = await request.json();
    const email = body?.email?.toLowerCase().trim();
    const code = body?.code?.toString().replace(/\s+/g, '').trim();

    if (!email || !code) {
      return new Response(
        JSON.stringify({ success: false, message: 'Email y código son obligatorios.' }),
        { status: 400, headers: { 'Content-Type': 'application/json' } }
      );
    }

    const pending = getPendingVerificationByEmail(email);
    if (!pending) {
      return new Response(
        JSON.stringify({
          success: false,
          message: 'El código ha expirado o no se ha solicitado ninguna verificación para este correo.',
        }),
        { status: 400, headers: { 'Content-Type': 'application/json' } }
      );
    }

    if (pending.code !== code) {
      return new Response(
        JSON.stringify({ success: false, message: 'El código introducido no es correcto. Verifica los 6 dígitos.' }),
        { status: 401, headers: { 'Content-Type': 'application/json' } }
      );
    }

    const user = await completeVerification(email);
    if (!user) {
      return new Response(
        JSON.stringify({ success: false, message: 'No se pudo completar la verificación.' }),
        { status: 500, headers: { 'Content-Type': 'application/json' } }
      );
    }

    const sessionToken = createSessionToken(user);

    cookies.set('mlp_press_session', sessionToken, {
      path: '/',
      httpOnly: true,
      secure: import.meta.env.PROD,
      sameSite: 'lax',
      maxAge: 90 * 24 * 60 * 60, // 90 days
    });

    return new Response(
      JSON.stringify({
        success: true,
        user,
        message: 'Acreditación confirmada. Acceso concedido.',
      }),
      { status: 200, headers: { 'Content-Type': 'application/json' } }
    );
  } catch (error) {
    console.error('Error in /api/press-auth/verify-otp:', error);
    return new Response(
      JSON.stringify({ success: false, message: 'Error interno al verificar el código.' }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
};
