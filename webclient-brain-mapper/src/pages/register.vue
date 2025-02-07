<template>

  <div class="flex w-full min-h-screen">
    <div class="flex bg-berry-primary items-center justify-center w-full md:w-1/2 min-h-screen">
      <div class="p-8 bg-berry-whiteaux rounded-lg w-11/12 md:w-2/3 lg:w-3/6">
        <div class="text-center font-semibold text-2xl mb-5">
          <span>
            {{ $t('auth.register.title') }}
          </span>
        </div>
        <div>
          <v-form ref="form">
            <v-row>
              <v-col>
                <v-text-field
                  v-model="name"
                  :rules="nameRules"
                  :label="$t('auth.register.name')"
                  required
                ></v-text-field>
              </v-col>
              <v-col>
                <v-text-field
                  v-model="lastName"
                  :rules="lastNameRules"
                  :label="$t('auth.register.lastName')"
                  required
                ></v-text-field>
              </v-col>
            </v-row>

            <v-text-field
              v-model="email"
              :rules="emailRules"
              :label="$t('auth.email')"
              required
            ></v-text-field>

            <v-text-field
              v-model="password"
              :counter="10"
              :rules="passwordRules"
              :label="$t('auth.password')"
              prepend-inner-icon="mdi-lock-outline"
              :append-inner-icon="passwdVisible ? 'mdi-eye-off' : 'mdi-eye'"
              :type="passwdVisible ? 'text' : 'password'"
              @click:append-inner="passwdVisible = !passwdVisible"
              required
            ></v-text-field>

            <v-text-field
              v-model="passwdConfirm"
              :counter="10"
              :rules="passwdConfirmRules"
              :label="$t('auth.register.confirmPasswd')"
              :append-inner-icon="passwdConfirmVisible ? 'mdi-eye-off' : 'mdi-eye'"
              :type="passwdConfirmVisible ? 'text' : 'password'"
              prepend-inner-icon="mdi-lock-outline"
              @click:append-inner="passwdConfirmVisible = !passwdConfirmVisible"
              required
            ></v-text-field>

            <v-checkbox
              v-model="checkbox"
              :rules="[v => !!v || 'You must agree to continue!']"
              :label="$t('auth.register.agreement')"
              required
            ></v-checkbox>

            <div class="d-flex flex-column">
              <v-btn
                color="highlight"
                block
                class="mt-4"
                @click="register()"
              >
                {{ $t('auth.register.register') }}
              </v-btn>
            </div>
          </v-form>
        </div>
      </div>
    </div>

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
  </div>

</template>

<script>
import { useAuthStore } from "@/stores/auth";

export default {
  data: () => ({
    name: '',
    lastName: '',
    email: '',
    emailRegex: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
    password: '',
    passwdVisible: false,
    passwdConfirm: '',
    passwdConfirmVisible: false,

    checkbox: false,

    authStore: useAuthStore(),
  }),

  created() {
    this.nameRules = [
      v => !!v || this.$t('auth.register.emptyFieldFeedB')
    ];

    this.lastNameRules = [
      v => !!v || this.$t('auth.register.emptyFieldFeedB')
    ];

    this.emailRules = [
      v => !!v || this.$t('auth.register.emptyFieldFeedB'),
      v => this.emailRegex.test(v) ||  this.$t('auth.register.emailFeedB')
    ];

    this.passwordRules = [
      v => !!v || this.$t('auth.register.emptyFieldFeedB'),
      v => (v && v.length >= 10) || this.$t('auth.register.minCharsFeedB'),
    ];

    this.passwdConfirmRules = [
      v => !!v || this.$t('auth.register.emptyFieldFeedB'),
      v => (v && v.length >= 10) || this.$t('auth.register.minCharsFeedB'),
      v => v === this.password || this.$t('auth.register.passwdMatchFeedB')
    ];
  },

  methods: {
    async validate () {
      const { valid } = await this.$refs.form.validate();

      if (!valid) alert("Invalid form");
    },

    async register () {
      try {
        const response = await this.authStore.register({
          name: this.name,
          lastName: this.lastName,
          email: this.email,
          passwd: this.password
        });

        if(!response) {
          alert("Cannot register");
          return;
        }

        this.$router.push('/login');
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
