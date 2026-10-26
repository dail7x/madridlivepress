/// <reference path="../.astro/types.d.ts" />

declare namespace App {
  interface Locals {
    pressUser?: {
      email: string;
      nombre: string;
      medio?: string;
      tipo_medio?: string;
    } | null;
    isBot?: boolean;
  }
}
