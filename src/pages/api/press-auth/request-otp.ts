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
    const email = body?.email?.toLowerCase().trim();
    const redirectUrl = body?.redirectUrl || '/comunicados';

    if (!email || !email.includes('@')) {
      return new Response(
        JSON.stringify({ success: false, message: 'Por favor, introduce un correo electrónico válido.' }),
        { status: 400, headers: { 'Content-Type': 'application/json' } }
      );
    }

    const code = generateOtpCode();
    const magicToken = generateMagicToken();
    const expiresAt = Date.now() + 15 * 60 * 1000;

    await savePendingVerification({
      nombre: 'Periodista Acreditado',
      email,
      medio: 'Redacción',
      tipo_medio: 'Digital',
      code,
      magicToken,
      expiresAt,
      isNewRegistration: false,
    });

    const origin = url.origin;
    const magicUrl = `${origin}/api/press-auth/verify-magic?token=${magicToken}&email=${encodeURIComponent(email)}&redirect=${encodeURIComponent(redirectUrl)}`;

    await sendPressAuthEmail({
      email,
      nombre: 'Periodista',
      code,
      magicUrl,
      isNewRegistration: false,
    });

    return new Response(
      JSON.stringify({
        success: true,
        email,
        message: `Código de acceso enviado a ${email}.`,
      }),
      { status: 200, headers: { 'Content-Type': 'application/json' } }
    );
  } catch (error) {
    console.error('Error in /api/press-auth/request-otp:', error);
    return new Response(
      JSON.stringify({ success: false, message: 'Error interno al enviar el código de acceso.' }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
};
