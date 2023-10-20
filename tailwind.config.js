/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./api/templates/*.html'],
  theme: {
    extend: {
      colors: {
        'ras-color': '#862632'
      },
      width: {
        '120px': '120px',
        '250px': '250px',
        '256px': '256px',
        '128px': '128px',
      }
    },
  },
  plugins: [],
}