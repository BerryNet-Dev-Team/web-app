/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors:{
        "brain-primary":{
          DEFAULT: '#33648A',
          light: '#3A739E',
          dark: '#2E5B7D'
        },
        "brain-secondary":{
          DEFAULT: '#5B999F',
          light: '#6AB3BA',
          dark: '#518A8F'
        },
        "brain-auxiliary":{
          DEFAULT: '#8AC6D0',
          light: '#91D0DB',
          dark: '#80B8C2'
        },
        "brain-alert":{
          DEFAULT: '#F26721',
          light: '#FC6C23',
          dark: '#E36120'
        },
        "brain-whiteaux":{
          DEFAULT: '#F2F2F3'
        }
      }
    },
  },
  plugins: [],
}

