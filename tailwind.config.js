// tailwind.config.js
/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme'); // Import defaultTheme

module.exports = {
  content: [
    './udpp/templates/**/*.html',
    './udpp/templates/navbar.html',
    './udpa/templates/**/*.html',
    './udpa/static/**/*.js',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', ...defaultTheme.fontFamily.sans], // Add Inter to the sans stack
      },
    },
  },
  plugins: [],
}