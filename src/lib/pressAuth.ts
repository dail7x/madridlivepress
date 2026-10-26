import crypto from 'node:crypto';
import { directus, DIRECTUS_TOKEN } from './directus';
import { createItem } from '@directus/sdk';

export interface PressUser {
  email: string;
  nombre: string;
  medio?: string;
  tipo_medio?: string;
  status?: 'pending' | 'active';
}

export interface PendingVerification {
  email: string;
  nombre: string;
  medio: string;
  tipo_medio: string;
  code: string;
  magicToken: string;
  expiresAt: number; // timestamp ms
  isNewRegistration: boolean;
}

// In-memory runtime cache for active OTPs and tokens (guarantees zero latency and failsafe if Directus schema is migrating)
const globalAuthCache: Map<string, PendingVerification> = new Map();

// Secret for signing session cookies
const AUTH_SECRET = DIRECTUS_TOKEN || 'mlp_press_auth_secret_token_2026';

/**
 * Generates a 6-digit numeric OTP code (e.g. "849201")
 */
export function generateOtpCode(): string {
  const num = crypto.randomInt(100000, 999999);
  return num.toString();
}

/**
 * Generates a high-entropy hex string for Magic Links
 */
export function generateMagicToken(): string {
  return crypto.randomBytes(24).toString('hex');
}

/**
 * Creates a signed session token for cookies
 */
export function createSessionToken(user: PressUser, maxAgeDays = 90): string {
  const exp = Date.now() + maxAgeDays * 24 * 60 * 60 * 1000;
  const payload = JSON.stringify({
    email: user.email.toLowerCase().trim(),
    nombre: user.nombre,
    medio: user.medio || '',
    tipo_medio: user.tipo_medio || '',
    exp,
  });

  const b64Payload = Buffer.from(payload).toString('base64url');
  const signature = crypto
    .createHmac('sha256', AUTH_SECRET)
    .update(b64Payload)
    .digest('base64url');

  return `${b64Payload}.${signature}`;
}

/**
 * Verifies and decodes a session token from cookies
 */
export function verifySessionToken(token: string): PressUser | null {
  if (!token || !token.includes('.')) return null;

  try {
    const [b64Payload, signature] = token.split('.');
    if (!b64Payload || !signature) return null;

    const expectedSig = crypto
      .createHmac('sha256', AUTH_SECRET)
      .update(b64Payload)
      .digest('base64url');

    if (signature !== expectedSig) return null;

    const decoded = JSON.parse(Buffer.from(b64Payload, 'base64url').toString('utf8'));
    if (typeof decoded.exp !== 'number' || Date.now() > decoded.exp) {
      return null; // Expired
    }

    return {
      email: decoded.email,
      nombre: decoded.nombre,
      medio: decoded.medio,
      tipo_medio: decoded.tipo_medio,
      status: 'active',
    };
  } catch {
    return null;
  }
}

/**
 * Saves a pending verification record (OTP & Magic Token)
 */
export async function savePendingVerification(data: PendingVerification): Promise<void> {
  const normalizedEmail = data.email.toLowerCase().trim();
  globalAuthCache.set(normalizedEmail, { ...data, email: normalizedEmail });

  // Persist / Sync with Directus (non-blocking failsafe)
  try {
    await directus.request(
      createItem('solicitudes_acreditacion' as any, {
        medio: data.medio || 'Prensa Digital',
        periodista_nombre: data.nombre,
        periodista_email: normalizedEmail,
        tipo_medio: data.tipo_medio || 'Digital',
        pais: 'España',
        observaciones: `OTP:${data.code}|TOKEN:${data.magicToken}|EXP:${data.expiresAt}`,
        estado: 'pendiente',
      })
    ).catch(() => {});
  } catch {
    // Graceful fallback to cache
  }
}

/**
 * Retrieves a pending verification by email
 */
export function getPendingVerificationByEmail(email: string): PendingVerification | null {
  const normalizedEmail = email.toLowerCase().trim();
  const record = globalAuthCache.get(normalizedEmail);
  if (!record) return null;

  if (Date.now() > record.expiresAt) {
    globalAuthCache.delete(normalizedEmail);
    return null;
  }

  return record;
}

/**
 * Retrieves a pending verification by Magic Token
 */
export function getPendingVerificationByToken(token: string): PendingVerification | null {
  if (!token) return null;

  for (const [email, record] of globalAuthCache.entries()) {
    if (record.magicToken === token) {
      if (Date.now() > record.expiresAt) {
        globalAuthCache.delete(email);
        return null;
      }
      return record;
    }
  }

  return null;
}

/**
 * Consumes and marks verification as successful
 */
export async function completeVerification(email: string): Promise<PressUser | null> {
  const normalizedEmail = email.toLowerCase().trim();
  const record = globalAuthCache.get(normalizedEmail);
  if (!record) return null;

  globalAuthCache.delete(normalizedEmail);

  const pressUser: PressUser = {
    email: normalizedEmail,
    nombre: record.nombre,
    medio: record.medio,
    tipo_medio: record.tipo_medio,
    status: 'active',
  };

  // Sync with Directus newsletter / subscriptions
  try {
    await directus.request(
      createItem('suscripciones_prensa' as any, {
        email: normalizedEmail,
        medio: record.medio || 'Redacción Acreditada',
        pais: 'España',
      })
    ).catch(() => {});
  } catch {
    // directus sync fallback
  }

  return pressUser;
}

/**
 * Detects if a User-Agent belongs to search engines or AI retrieval bots
 */
export function isSearchOrAiBot(userAgent: string | null | undefined): boolean {
  if (!userAgent) return false;
  const ua = userAgent.toLowerCase();
  const botKeywords = [
    'googlebot',
    'bingbot',
    'gptbot',
    'oai-searchbot',
    'chatgpt-user',
    'perplexitybot',
    'claudebot',
    'anthropic-ai',
    'google-extended',
    'applebot',
    'applebot-extended',
    'bytespider',
    'yandexbot',
    'duckduckbot',
    'diffbot',
    'meta-externalagent',
  ];

  return botKeywords.some((keyword) => ua.includes(keyword));
}

/**
 * Dispatches an institutional email with the 6-digit OTP code and the Magic Link
 */
export async function sendPressAuthEmail(params: {
  email: string;
  nombre: string;
  code: string;
  magicUrl: string;
  isNewRegistration: boolean;
}): Promise<boolean> {
  const { email, nombre, code, magicUrl, isNewRegistration } = params;

  console.log(`\n======================================================`);
  console.log(`[MLP PRESS AUTH] Código OTP enviado a: ${email}`);
  console.log(`[MLP PRESS AUTH] Periodista: ${nombre}`);
  console.log(`[MLP PRESS AUTH] CÓDIGO OTP (6 DÍGITOS): ${code}`);
  console.log(`[MLP PRESS AUTH] MAGIC LINK: ${magicUrl}`);
  console.log(`======================================================\n`);

  // Directus Mail / Webhook dispatcher if configured
  try {
    const formattedCode = `${code.slice(0, 3)} ${code.slice(3)}`;
    const emailSubject = isNewRegistration
      ? `${code} es tu código de verificación | Noche Madrid Press`
      : `${code} es tu código de acceso | Noche Madrid Press`;

    // Try sending via Directus /mail or internal API if available
    await fetch(`${directus.url}/mail`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${AUTH_SECRET}`,
      },
      body: JSON.stringify({
        to: email,
        subject: emailSubject,
        html: `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #f4f4f5; margin: 0; padding: 24px; color: #09090b; }
    .container { max-width: 580px; margin: 0 auto; background: #ffffff; border: 1px solid #e4e4e7; padding: 36px 32px; }
    .header { border-bottom: 2px solid #09090b; padding-bottom: 16px; margin-bottom: 24px; }
    .brand { font-size: 14px; font-weight: 800; letter-spacing: 0.15em; text-transform: uppercase; color: #09090b; }
    .subbrand { font-size: 10px; font-family: monospace; color: #71717a; text-transform: uppercase; letter-spacing: 0.1em; margin-top: 4px; }
    h1 { font-size: 20px; font-weight: 700; margin: 0 0 12px 0; color: #09090b; line-height: 1.3; }
    p { font-size: 14px; line-height: 1.6; color: #3f3f46; margin: 0 0 18px 0; }
    .otp-box { background: #fbfbfb; border: 1px solid #09090b; padding: 20px; text-align: center; margin: 24px 0; }
    .otp-label { font-family: monospace; font-size: 10px; text-transform: uppercase; letter-spacing: 0.15em; color: #71717a; margin-bottom: 8px; }
    .otp-code { font-family: monospace; font-size: 36px; font-weight: 800; letter-spacing: 0.25em; color: #E11D48; }
    .btn { display: inline-block; background: #09090b; color: #ffffff !important; text-decoration: none; padding: 14px 28px; font-size: 12px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; margin: 12px 0 24px 0; text-align: center; }
    .footer { border-top: 1px solid #e4e4e7; padding-top: 16px; margin-top: 24px; font-size: 11px; color: #a1a1aa; font-family: monospace; line-height: 1.5; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="brand">Noche Madrid Press</div>
      <div class="subbrand">Gabinete de Prensa Oficial · NocheMadrid</div>
    </div>

    <h1>Tu código de acceso profesional</h1>
    <p>Hola <strong>${nombre}</strong>,</p>
    <p>Usa el siguiente código de 6 dígitos en la pantalla donde estás leyendo para verificar tu acreditación y desbloquear los materiales de redacción:</p>

    <div class="otp-box">
      <div class="otp-label">Código de verificación (válido 15 min)</div>
      <div class="otp-code">${formattedCode}</div>
    </div>

    <p style="text-align: center; font-size: 12px; color: #71717a;">O si prefieres acceder con un solo clic:</p>
    <div style="text-align: center;">
      <a href="${magicUrl}" class="btn">Acceder directamente con Magic Link →</a>
    </div>

    <p style="font-size: 12px; color: #71717a;">Tu acreditación en Noche Madrid Press te da acceso inmediato a descargas de B-Roll en 4K, dossiers oficiales y notas de prensa bajo embargo.</p>

    <div class="footer">
      Noche Madrid Press · Servicio a Redacciones y Periodistas Culturales.<br>
      Si no has solicitado este pase, puedes ignorar este mensaje con total seguridad.
    </div>
  </div>
</body>
</html>
        `,
      }),
    }).catch(() => {});
  } catch {
    // console log fallback is already completed
  }

  return true;
}
