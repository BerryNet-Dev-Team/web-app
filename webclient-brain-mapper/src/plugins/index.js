/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import emitter from './emitter'
import vuetify from './vuetify'
import pinia from '@/stores'
import router from '@/router'
import vueI18n from './vueI18n'
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";

import axiosInstance from './axios'

export function registerPlugins (app) {
  // Create mitt instance and add it to main app
  app.config.globalProperties.$emitter = emitter;

  // Add axios instance to main app
  app.config.globalProperties.$axios = { ...axiosInstance }

  // Add Axios to Pinia
  pinia.use(({ store }) => {
    store.$axios = app.config.globalProperties.$axios;
  });

  // Config for toast notifications
  const toastConfigs = {
    position: "top-right",
    timeout: 4990,
    closeOnClick: true,
    pauseOnFocusLoss: true,
    pauseOnHover: true,
    draggable: true,
    draggablePercent: 0.6,
    showCloseButtonOnHover: false,
    hideProgressBar: true,
    closeButton: "button",
    icon: true,
    rtl: false
  };

  // Add plugins to main app
  app
    .use(Toast, toastConfigs)
    .use(vueI18n)
    .use(vuetify)
    .use(pinia)
    .use(router)
}
