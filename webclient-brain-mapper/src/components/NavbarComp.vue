<template>
  <nav class="flex justify-center w-full fixed top-6 z-50">
    <div class="bg-berry-primary rounded-xl w-auto p-0.5 flex justify-center items-center shadow-lg">

      <div class="p-2 transition-all duration-200 hover:brightness-110">
        <v-img
          class="hover:cursor-pointer"
          src="@/assets/BerryNet_LogoHorizontal.png"
          heigth="60" width="150"
          cover
          @click="$router.push({ path: '/dashboard' })"
        >
        </v-img>
      </div>

      <v-btn 
        value="recent"
        class="text-berry-whiteaux" size="small"
        rounded stacked variant="text"
        @click="$router.push({ path: '/inferences' })"
      >
        <v-icon>mdi-pin</v-icon>
        <span>{{ $t('appNavbar.generate') }}</span>
      </v-btn>

      <v-btn
        v-if="isAdmin"
        value="recent"
        class="text-berry-whiteaux" size="small"
        rounded stacked variant="text"
        @click="$router.push({ path: '/dataset' })"
      >
        <v-icon>mdi-brain</v-icon>
        <span>{{ $t('appNavbar.train') }}</span>
      </v-btn>

      <v-btn
        value="recent"
        class="text-berry-whiteaux" size="small"
        rounded stacked variant="text"
        @click="logout()"
      >
        <v-icon>mdi-logout</v-icon>
        <span>{{ $t('appNavbar.logout') }}</span>
      </v-btn>
    </div>
  </nav>
</template>

<script>
import { mapState } from 'pinia';
import { useAuthStore } from "@/stores/auth";

export default {
  name: 'NavbarComp',

  data: () => ({
    authStore: useAuthStore(),
  }),

  computed: {
    ...mapState(useAuthStore, {
      isAdmin: (store) => store.isAdmin,
    })
  },

  methods: {
    async logout() {
      let response;
      try {
        response = await this.authStore.logout();
      }
      catch (error) {
        this.toast.error(this.$t('navbarComp.logoutErr'));
        return;
      }

      this.$router.push('/');
    }
  }
};
</script>
