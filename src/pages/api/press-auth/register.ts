import type { APIRoute } from 'astro';
import {
  generateOtpCode,
  generateMagicToken,
  savePendingVerification,
  sendPressAuthEmail,
} from '@/lib/pressAuth';

export const prerender = false;

export const POST: APIRoute = async ({ request, url }) => {
  try {
    const body = await request.json();
    const nombre = body?.nombre?.trim();
    const email = body?.email?.toLowerCase().trim();
    const medio = body?.medio?.trim() || 'Prensa / Redacción';
    const tipo_medio = body?.tipo_medio || 'Digital';
    const redirectUrl = body?.redirectUrl || '/comunicados';

    if (!nombre || !email || !email.includes('@')) {
      return new Response(
        JSON.stringify({ success: false, message: 'Por favor, indica tu nombre y un correo electrónico válido.' }),
        { status: 400, headers: { 'Content-Type': 'application/json' } }
      );
    }

    const code = generateOtpCode();
    const magicToken = generateMagicToken();
    const expiresAt = Date.now() + 15 * 60 * 1000; // 15 minutes

    await savePendingVerification({
      nombre,
      email,
      medio,
      tipo_medio,
      code,
      magicToken,
      expiresAt,
      isNewRegistration: true,
    });

    const origin = url.origin;
    const magicUrl = `${origin}/api/press-auth/verify-magic?token=${magicToken}&email=${encodeURIComponent(email)}&redirect=${encodeURIComponent(redirectUrl)}`;

    await sendPressAuthEmail({
      email,
      nombre,
      code,
      magicUrl,
      isNewRegistration: true,
    });

    return new Response(
      JSON.stringify({
        success: true,
        email,
        message: `Hemos enviado un código de 6 dígitos a ${email}.`,
      }),
      { status: 200, headers: { 'Content-Type': 'application/json' } }
    );
  } catch (error) {
    console.error('Error in /api/press-auth/register:', error);
    return new Response(
      JSON.stringify({ success: false, message: 'Error interno al procesar la acreditación.' }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
};
