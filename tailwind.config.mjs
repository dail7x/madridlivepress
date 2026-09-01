/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        background: '#090a0f',
        surface: {
          DEFAULT: '#12141c',
          light: '#1a1d29',
          border: 'rgba(255, 255, 255, 0.08)',
          'border-hover': 'rgba(255, 255, 255, 0.16)',
        },
        brand: {
          primary: '#E11D48',      // Madrid Rose/Crimson
          'primary-hover': '#BE123C',
          accent: '#F59E0B',       // Nightlife Gold
          electric: '#6366F1',     // Indigo Violet
          dark: '#050608',
        },
        madrid: {
          gold: '#F59E0B',
          crimson: '#E11D48',
          violet: '#8B5CF6',
          cyan: '#06B6D4',
        }
      },
      fontFamily: {
        display: ['"Geist Sans"', 'Inter', 'system-ui', '-apple-system', 'sans-serif'],
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
        mono: ['"Geist Mono"', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'],
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'hero-pattern': 'radial-gradient(circle at 50% 0%, rgba(225, 29, 72, 0.15), transparent 70%)',
        'card-glow': 'radial-gradient(circle at 50% 0%, rgba(255, 255, 255, 0.05), transparent 80%)',
      },
      keyframes: {
        ticker: {
          '0%': { transform: 'translateX(0%)' },
          '100%': { transform: 'translateX(-50%)' },
        },
        pulseGlow: {
          '0%, 100%': { opacity: 0.4 },
          '50%': { opacity: 0.8 },
        }
      },
      animation: {
        ticker: 'ticker 35s linear infinite',
        'pulse-glow': 'pulseGlow 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      }
    },
  },
  plugins: [],
};
