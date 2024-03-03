/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./*.html",
    "./*.js",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {
      fontFamily: {
        kodemono: ["Kode Mono", "serif"],
        anta: ["Anta", "serif"],
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

