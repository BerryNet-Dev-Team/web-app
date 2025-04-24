/**
 * plugins/vuetify.js
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Composables
import { createVuetify } from 'vuetify'

//Labs component for file upload
import { VFileUpload } from 'vuetify/labs/VFileUpload'

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
export default createVuetify({
  components:{
    VFileUpload,
  },
  theme: {
    themes: {
      light: {
        dark: false,
        colors: {
          primary: '#2C3E50',
          'primary-darken-1': '#273748',
          secondary: '#F4E1D2',
          auxiliary: '#698F3F',
          highlight: '#A3153A'
        }
      },
    },
  },
})
