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

// Initializes the session before router starts navigating
async function initializeSession(to, from, appStore, authStore) {
  try {
    if(from === START_LOCATION) {
      await authStore.initiateAppSession();

      // If user is actually logged in, prevents navigation to login
      if (to.fullPath === '/login') {
        if (authStore.getIsSessionActive) {
          return '/profile';
        }
      }

      // Otherwise just return null to just go
      return null;
    }
  } catch (error) {
    appStore.setBackendAvailable(false);
    return null;
  }
}

// Functions to handle some cases in the router guardian
function handleBackendError(to, appStore) {
  // If backend is dead, blocks navigation and redirects all to Err5xx page
  if (!appStore.isBackendAvailable) {
    if (to.fullPath !== '/err5xx') {
      return '/err5xx';
    }
  } else if (to.fullPath === '/err5xx') {
    return '/login'; // After reload, if backend is available(again) this will kick out user from error page(s)
  }

  // If no problem with backend send null redirection
  return null;
}

// Function to handle protected routes and its permissions
async function handleAuthAndPermissions(to, from, authStore) {
  // Handle protected routes
  if (to.meta.requiresAuth) {
    if (await authStore.isLoggedIn()) {
      // Check if route requires admin role and if user has required role
      if(to.meta.requiresAdmin) {
        // If is not admin, redirects to user main page
        if(!authStore.isAdmin) {
          return '/profile';
        }
      }

      // If auth and role are ok, continue navigation
      return null;
    }
    else { // In case user is not logged-in, show modal and logout
      // Emit event to app's root file
      emitter.emit('session-exp');
      return '/login';
    }
  }
  else { // If route are not protected & requires no authentication
    // Just sends no redirection
    return null;
  }
}

// Create a vue-router instance
const router = createRouter({
  history: createWebHistory(import.meta.env.VITE_BASE_URL),
  extendRoutes: setupLayouts,
})

// Defines router guardian
router.beforeEach(async (to, from) => {
  // Set instance of authStore & appStore
  const authStore = useAuthStore();
  const appStore = useAppStore();

  // 0. Waits for init session call to start routing
  const initRedirect = await initializeSession(to, from, appStore, authStore);
  if (initRedirect) return initRedirect;

  // Normal navigation
  try {
    // 1. Verify backend errors, and redirect to error page if required
    const backendErrRedirect = handleBackendError(to, appStore);
    if (backendErrRedirect) return backendErrRedirect;
  
    // 2. Here route validations and redirections are done
    // Check if route needs auth and if user is authenticated
    const authRedirect = await handleAuthAndPermissions(to, from, authStore);
    if (authRedirect) return authRedirect;

    // 3. If everything ok with previous validations, just continue
  } catch (error) {
    console.error('Fatal error in navigation guard:'/*, error*/);
    return '/';
  }
})

export default router;
