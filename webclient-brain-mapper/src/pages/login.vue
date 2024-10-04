<template>
  <div class="p-4">
    <div class="text-center font-semibold text-2xl mb-5">
      <span>
        {{ $t('auth.login.title') }}
      </span>
    </div>
    <div>
      <v-form ref="form">

        <v-text-field
          v-model="email"
          :label="$t('auth.email')"
          :rules="emailRules"
          prepend-inner-icon="mdi-email-outline"
          required
        ></v-text-field>

        <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-end">
          <a
            class="text-caption text-decoration-none text-blue"
            href="#"
            rel="noopener noreferrer"
            target="_blank"
          >
            {{ $t('auth.login.forgotPasswd') }}
          </a>
        </div>
        <v-text-field
          v-model="password"
          :label="$t('auth.password')"
          :rules="passwordRules"
          prepend-inner-icon="mdi-lock-outline"
          :append-inner-icon="passwdVisible ? 'mdi-eye-off' : 'mdi-eye'"
          :type="passwdVisible ? 'text' : 'password'"
          @click:append-inner="passwdVisible = !passwdVisible"
          required
        ></v-text-field>

        <div class="d-flex flex-column">
          <v-btn
            class="mt-4"
            color="amber-darken-4"
            block
            @click="login"
          >
            {{ $t('auth.login.login') }}
          </v-btn>

          <v-btn
            variant="plain"
            color="amber-darken-4"
            class="mt-10 text-none"
            append-icon="mdi-chevron-right"
            @click="gotoRegister"
          >
            {{ $t('auth.login.register') }}
          </v-btn>
        </div>
      </v-form>
    </div>
  </div>
</template>

<script>
import { useAuthStore } from "@/stores/auth";

export default {
  data: () => ({
    email: '',
    password: '',
    passwdVisible: false,

    authStore: useAuthStore(),
  }),

  created() {
    this.emailRules = [
      v => !!v || this.$t('auth.login.emptyEmailFeedB')
    ];

    this.passwordRules = [
      v => !!v || this.$t('auth.login.emptyPasswdFeedB')
    ];
  },

  methods: {
    gotoRegister() {
      this.$router.push('/register');
    },

    async validate () {
      const { valid } = await this.$refs.form.validate()

      if (!valid) alert("Invalid form");
    },

    async login () {
      try {
        const response = await this.authStore.login({
          email: this.email,
          passwd: this.password
        });

        if(!response) {
          alert("Cannot register");
          return;
        }

        this.$router.push('/profile');
      }
      catch (error) {
        console.error(error);
      }
    }
  },
};
</script>

<route lang="json">
  {
    "meta":{
      "layout": "auth",
      "requiresAuth": false
    }
  }
</route>