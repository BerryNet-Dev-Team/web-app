/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors:{
        "berry-primary":{
          DEFAULT: '#2C3E50',
        },
        "berry-secondary":{
          DEFAULT: '#F4E1D2',
        },
        "berry-auxiliary":{
          DEFAULT: '#698F3F',
        },
        "berry-highlight":{
          DEFAULT: '#A3153A',
        },
        "berry-whiteaux":{
          DEFAULT: '#F2F2F3'
        }
      }
    },
  },
  plugins: [],
}

