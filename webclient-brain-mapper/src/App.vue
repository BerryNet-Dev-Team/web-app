<template>
  <v-app>
    <v-main>
      <router-view />
    </v-main>

    <!-- Loading spinner -->
    <div v-if="isLoading" class="spinner">
      <radar-spinner :animation-duration="1800" :size="150" color="#33648A"/>
    </div>

    <!-- Session expired modal -->
    <v-dialog
      v-model="showSessionExpiredMod"
      width="auto"
      persistent
    >
      <v-card
        max-width="400"
        prepend-icon="mdi-account-reactivate"
        :title="$t('sessionExpired.title')"
        :text="$t('sessionExpired.text')"
      >
        <template v-slot:actions>
          <v-btn
            class="ms-auto"
            text="Ok"
            @click="showSessionExpiredMod = false"
          ></v-btn>
        </template>
      </v-card>
    </v-dialog>
  </v-app>
</template>

<script>
import { RadarSpinner  } from 'epic-spinners';
import { useAuthStore } from "@/stores/auth";

export default{
  name: 'app',

  components: {
    RadarSpinner
  },

  data: () => ({
    authStore: useAuthStore(),
    showSessionExpiredMod: false,
    refCount: 0,
    isLoading: false
  }),

  async created() {
    // Initiate events
    this.$emitter.on('session-exp', this.handleSessionExp);
    this.$emitter.on('before-request', this.setLoading);
    this.$emitter.on('request-error', this.unsetLoading);
    this.$emitter.on('after-response', this.unsetLoading);
    this.$emitter.on('response-error', this.unsetLoading);

    // Initiate an app session
    await this.authStore.initiateAppSession();
  },

  beforeUnmount() {
    // clearing all events
    this.$emitter.all.clear()
  },

  methods: {
    setLoading() {
      this.refCount += 1;
      this.isLoading = true;
    },

    unsetLoading() {
      if (this.refCount > 0) {
        this.refCount -= 1;
        this.isLoading = this.refCount > 0;
      }
    },

    async handleSessionExp() {
      const actualPath = this.$route.path;
      // Only if you are not in login, redirect you to login
      if(actualPath !== '/login') {
        // Delete all from local storage and deactivate animation
        await this.authStore.logout();
        this.unsetLoading();

        // Show a modal notification that session has expired
        this.showSessionExpiredMod = true;

        /*Redirect you to login*/
        this.$router.push({
          path: '/login'
        });
      } else {
        this.unsetLoading();
      }
    }
  }
};
</script>

<style>
.spinner {
  position: fixed !important;
  top: 0px !important;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh !important;
  width: 100% !important;
  z-index: 10000 !important;
  background: rgba(255, 255, 255, 0.8) !important;
}
</style>
