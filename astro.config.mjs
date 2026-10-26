// @ts-check
import { defineConfig } from 'astro/config';
import node from '@astrojs/node';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  site: process.env.SITE_URL || 'https://madridlivepress.116.203.118.1.sslip.io',
  output: 'server',
  adapter: node({
    mode: 'standalone',
  }),
  integrations: [
    tailwind({
      applyBaseStyles: false,
    }),
  ],
  i18n: {
    defaultLocale: 'es',
    locales: ['es', 'en', 'it', 'fr'],
    routing: {
      prefixDefaultLocale: false,
    },
  },
  server: {
    port: 3000,
    host: '0.0.0.0',
  },
});
