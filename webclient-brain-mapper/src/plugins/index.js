/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import vuetify from './vuetify'
import pinia from '@/stores'
import router from '@/router'
import vueI18n from './vueI18n'

import axiosInstance from './axios'

export function registerPlugins (app) {
  // Add axios instance to main app
  app.config.globalProperties.$axios = { ...axiosInstance }

  // Add Axios to Pinia
  pinia.use(({ store }) => {
    store.$axios = app.config.globalProperties.$axios;
  });

  // Add plugins to main app
  app
    .use(vueI18n)
    .use(vuetify)
    .use(router)
    .use(pinia)
}
