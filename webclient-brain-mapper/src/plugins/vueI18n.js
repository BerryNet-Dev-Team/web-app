import { createI18n } from 'vue-i18n';
import en from '../i18n/locales/en.json';
import es from '../i18n/locales/es.json';

// get the translations from single files
const messages = {
  es: es,
  en: es
};

export default createI18n({
  locale: navigator.language.split('-')[0], // user navigator language
  fallbackLocale: 'es', // backup lenguage if the user language isnt found(spanish)
  messages, // messages object
  debug: true, // debug mode
});
