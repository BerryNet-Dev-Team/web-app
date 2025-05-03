<template>
  <div class="flex w-full min-h-screen">
    <div class="hidden md:flex md:flex-col md:w-1/2 justify-center items-center min-h-screen">
      <div>
        <v-img
          :width="500"
          aspect-ratio="1/1"
          cover
          src="@/assets/BerryNetLogo.png"
        ></v-img>
      </div>
      <div>
        <p class="text-left font-medium text-2xl">
          {{new Date().getFullYear()}} &copy; {{ $t('appName') }}
        </p>
      </div>
    </div>

    <div class="flex bg-berry-primary items-center justify-center w-full md:w-1/2 min-h-screen">
      <div class="p-8 bg-berry-whiteaux rounded-lg w-11/12 md:w-2/3 lg:w-3/6">
        <div class="text-center font-semibold text-2xl mb-5">
          <span>
            {{ $t('auth.login.title') }}
          </span>
        </div>
        <div>
          <!-- Unauthorized alert -->
          <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-start">
            <span
              v-if="wrongCredentials"
              class="text-caption text-decoration-none"
              style="color: rgb(var(--v-theme-error));"
            >
              {{ $t('auth.login.wrongCreds') }}
            </span>
            <div v-else style="height: 20px;"></div>
          </div>

          <!-- Login form -->
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
              required
              @click:append-inner="passwdVisible = !passwdVisible"
            ></v-text-field>

            <div class="d-flex flex-column">
              <v-btn
                block
                color='highlight'
                class="mt-4"
                @click="login"
              >
                {{ $t('auth.login.login') }}
              </v-btn>

              <v-btn
                variant="plain"
                color="highlight"
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
    </div>
  </div>
</template>

<script>
import { mapState } from 'pinia';
import { useAuthStore } from "@/stores/auth";
import { useToast } from "vue-toastification";

export default {
  name: 'UserLogin',
  data: () => ({
    email: '',
    password: '',
    passwdVisible: false,

    wrongCredentials: false,

    toast: useToast(),

    authStore: useAuthStore(),
  }),

  computed: {
    ...mapState(useAuthStore, {
      isAdmin: (store) => store.isAdmin,
    })
  },

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
      let response;
      try {
        response = await this.authStore.login({
          email: this.email,
          passwd: this.password
        });
      }
      catch (error) {
        this.toast.error(this.$t('auth.login.unexpectedErr'));
        return;
      }

      // If login was not successful, show credentials error
      if(!response) {
        this.wrongCredentials = true;
        return;
      }

      // Redirect user to dashboard
      this.$router.push('/dashboard');
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
