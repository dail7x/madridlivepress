/**
 * Contactos públicos.
 * Sede: https://nochemadrid.org/contacto/ (consultada el 25 nov 2026).
 * Prensa: contacto indicado por el cliente para la nota firmada.
 * Sustituye los contactos de prensa anteriores (prensa@nochemadrid.org,
 * Vicente Pizcueta, Marina Sanz y el teléfono 91 542 23 04 cuando se usaba
 * como teléfono de prensa).
 */

export const association = {
  name: 'Noche Madrid',
  description: 'Asociación de empresarios del ocio nocturno de la Comunidad de Madrid',
  sector: 'Ocio nocturno y espectáculos',
  address: 'C/ Valverde 13, 3º D',
  city: '28004 Madrid',
  phoneDisplay: '91 542 23 04',
  phoneTel: '+34915422304',
  email: 'info@nochemadrid.org',
  sourceUrl: 'https://nochemadrid.org/contacto/',
};

export const pressOffice = {
  office: 'Gabinete de Comunicación Noche Madrid',
  name: 'Jesús Martínez',
  phoneDisplay: '667 456 989',
  phoneTel: '+34667456989',
  lineEs: 'Gabinete de Comunicación Noche Madrid: Jesús Martínez — Tel. 667 456 989',
  lineEn: 'Noche Madrid Communications Office: Jesús Martínez — Tel. +34 667 456 989',
};

/** Nombres que la web trataba como contacto de prensa y que dejan de mostrarse. */
const PREVIOUS_PRESS_NAMES = ['vicente pizcueta', 'marina sanz'];

export function replacePreviousPressContact(name?: string | null, role?: string | null): { name?: string; role?: string } {
  const normalized = (name || '').trim().toLowerCase();
  if (normalized && PREVIOUS_PRESS_NAMES.includes(normalized)) {
    return { name: pressOffice.name, role: pressOffice.office };
  }
  return {
    name: name || undefined,
    role: role || undefined,
  };
}
