/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*"],
  theme: {
    extend: {
      colors: {
        'ras-color': '#862632'
      },
      width: {
        '120px': '120px',
        '300px': '300px',
        '256px': '256px',
        '128px': '128px',
      }
    },
  },
  plugins: [],
}