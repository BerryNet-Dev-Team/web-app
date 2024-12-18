<template>
  <v-app>
    <v-main>
      <router-view />
    </v-main>

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
import { useAuthStore } from "@/stores/auth";

export default{
  name: 'app',

  data: () => ({
    authStore: useAuthStore(),
    showSessionExpiredMod: false,
  }),

  async created() {
    this.$emitter.on('session-exp', this.handleSessionExp);
    await this.authStore.initiateAppSession();
  },

  beforeUnmount() {
    // clearing all events
    this.$emitter.all.clear()
  },

  methods: {
    async handleSessionExp() {
      const actualPath = this.$route.path;
      // Only if you are not in login, redirect you to login
      if(actualPath !== '/login') {
        // Delete all from local storage and deactivate animation
        await this.authStore.logout();

        // Show a modal notification that session has expired
        this.showSessionExpiredMod = true;

        /*Redirect you to login*/
        this.$router.push({
          path: '/login'
        });
      }
    }
  }
};
</script>
