/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        paper: '#ffffff',
        canvas: '#fbfbfb',
        'surface-subtle': '#f4f4f5',
        'surface-muted': '#e4e4e7',
        ink: '#09090b',
        'ink-muted': '#52525b',
        'ink-subtle': '#71717a',
        'border-grid': '#e4e4e7',
        'border-dark': '#09090b',
        vermilion: '#E11D48',
        // Backward compatibility mappings
        background: '#ffffff',
        surface: '#ffffff',
        'surface-card': '#fbfbfb',
        'brand-primary': '#E11D48',
        'brand-primary-hover': '#BE123C',
      },
      fontFamily: {
        display: ['"Geist Sans"', 'Inter', 'system-ui', 'sans-serif'],
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['"Geist Mono"', 'ui-monospace', 'monospace'],
      },
      letterSpacing: {
        'tightest': '-0.04em',
        'tighter': '-0.02em',
        'wide-meta': '0.12em',
        'widest-meta': '0.2em',
      },
      boxShadow: {
        'sharp': '0 1px 0 rgba(0, 0, 0, 0.05)',
        'float': '0 10px 30px -10px rgba(0,0,0,0.08)',
      },
    },
  },
  plugins: [],
};
