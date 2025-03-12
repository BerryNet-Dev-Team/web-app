/**
 * router/index.ts
 *
 * Automatic routes for `./src/pages/*.vue`
 */

// Composables
import { createRouter, createWebHistory } from 'vue-router/auto'
import { START_LOCATION } from 'vue-router';
import { setupLayouts } from 'virtual:generated-layouts'
import { useAuthStore } from '@/stores/auth'
import { useAppStore } from '@/stores/app'
import emitter from '@/plugins/emitter'

// Functions to handle some cases in the router guardian
function handleBackendError(to, next, appStore) {
  // If backend is dead, blocks navigation and redirects all to Err5xx page
  if (!appStore.isBackendAvailable) {
    if (to.fullPath !== '/err-5xx') {
      next({path: '/err-5xx'});
      return;
    }
  } else if (to.fullPath === '/err-5xx') {
    next('/'); // After reload, if backend is available(again) this will kick out user from error page(s)
    return;
  }
}

// Function to handle protected routes and its permissions
async function handleAuthAndPermissions(to, from, next, authStore) {
  // Handle protected routes
  if (to.meta.requiresAuth) {
    if (await authStore.isLoggedIn()) {
      // Check if route requires admin role and if user has required role
      if(to.meta.requiresAdmin) {
        // If is not admin, cancels navigation
        if(!authStore.isAdmin) {
          next(false);
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
      return;
    }
  }
  else { // If route are not protected & requires no authentication
    // Just go
    next();
    return;
  }
}

// Create a vue-router instance
const router = createRouter({
  history: createWebHistory(import.meta.env.VITE_BASE_URL),
  extendRoutes: setupLayouts,
})

// Defines router guardian
router.beforeEach(async (to, from, next) => {
  // Set instance of authStore & appStore
  const authStore = useAuthStore();
  const appStore = useAppStore();

  // 0. Init session call
  try {
    if(from === START_LOCATION) {
      await authStore.initiateAppSession();

      // If user is actually logged in, prevents navigation to login
      if (to.fullPath === '/login') {
        if (authStore.getIsSessionActive) {
          next('/profile');
          return;
        }
      }

      // Otherwise just go
      next();
      return;
    }
  } catch (error) {
    appStore.setBackendAvailable(false);
    next('/err5xx');
    return;
  }


  try {
    // 1. Verify backend errors
    handleBackendError(to, next, appStore);
  
    // 2. Here route validations are done
    // Check if route needs auth and if user is authenticated
    await handleAuthAndPermissions(to, from, next, authStore);
  
    // 3. If there is nothing to verify, just continue
    // next();
  } catch (error) {
    console.error('Fatal error in navigation guard:'/*, error*/);
  }
})

export default router;
