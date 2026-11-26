import crypto from 'node:crypto';

function readApiSharedSecret(): string | undefined {
  const fromProcess = typeof process !== 'undefined' ? process.env.API_SHARED_SECRET : undefined;
  if (typeof fromProcess === 'string' && fromProcess.length > 0) {
    return fromProcess;
  }

  const fromMeta = import.meta.env.API_SHARED_SECRET;
  if (typeof fromMeta === 'string' && fromMeta.length > 0) {
    return fromMeta;
  }

  return undefined;
}

function bearerToken(header: string | null): string | null {
  if (!header) return null;
  const match = /^Bearer\s+(.+)$/i.exec(header);
  return match ? match[1] : null;
}

function secretsEqual(provided: string, expected: string): boolean {
  const providedHash = crypto.createHash('sha256').update(provided).digest();
  const expectedHash = crypto.createHash('sha256').update(expected).digest();
  return crypto.timingSafeEqual(providedHash, expectedHash);
}

function json(status: number, body: Record<string, string>): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}

/** Response to return when the request must stop, or null when it may continue. */
export function requireApiSharedSecret(request: Request): Response | null {
  const secret = readApiSharedSecret();
  if (!secret) {
    return json(500, { error: 'API_SHARED_SECRET is not configured' });
  }

  const token = bearerToken(request.headers.get('authorization'));
  if (!token || !secretsEqual(token, secret)) {
    return json(401, { error: 'Unauthorized' });
  }

  return null;
}
