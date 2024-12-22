/**
 * router/index.ts
 *
 * Automatic routes for `./src/pages/*.vue`
 */

// Composables
import { createRouter, createWebHistory } from 'vue-router/auto'
import { setupLayouts } from 'virtual:generated-layouts'
import { useAuthStore } from '@/stores/auth'
import { storeToRefs } from 'pinia'
import emitter from '@/plugins/emitter'

const router = createRouter({
  history: createWebHistory(import.meta.env.VITE_BASE_URL),
  extendRoutes: setupLayouts,
})

router.beforeEach(async (to, from, next) => {
  // Set instance of authStore
  const authStore = useAuthStore();
  const {isAdmin} = storeToRefs(authStore);

  // Here route validations are done
  // Check if route needs auth and if user is authenticated
  if (to.meta.requiresAuth) {
    if (await authStore.isLoggedIn()) {
      // Check if route requires admin role ad if user has required role
      if(to.meta.requiresAdmin) {
        if(!isAdmin) {
          // If is not admin, goto previous page
          next(from.fullPath);
          return;
        }
      }

      // If auth and role are ok, continue navigation
      next();
      return;
    }
    else { // In case user is not logged in, show modal and logout
      // Emit event to app's root file
      emitter.emit('session-exp');
      next('/login');
    }
  }
  else { // If route requires nothing just go to
    next();
  }
})

export default router;
