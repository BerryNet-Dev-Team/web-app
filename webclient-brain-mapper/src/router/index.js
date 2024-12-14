/**
 * router/index.ts
 *
 * Automatic routes for `./src/pages/*.vue`
 */

// Composables
import { createRouter, createWebHistory } from 'vue-router/auto'
import { setupLayouts } from 'virtual:generated-layouts'
import { useAuthStore } from '@/stores/auth'

const router = createRouter({
  history: createWebHistory(import.meta.env.VITE_BASE_URL),
  extendRoutes: setupLayouts,
})

router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore();

  if (to.meta.requiresAuth) {
    if (authStore.getIsSessionActive) {
      if(to.meta.requiresAdmin) {
        if(!authStore.isAdmin) return false;
      }

      // If everything ok, continue navigation
      next();
    }
    else {
      // Logout user
      await authStore.logout();

      // Setting previous path here so that it can be rerouted to old url that was open before login
      next({
        path: '/login',
        query: {
          previousPath: from.fullPath
        }
      });
    }
  }
  else {
    next();
  }
})

export default router
