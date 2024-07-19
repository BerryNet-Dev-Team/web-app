import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isSessionActive: null,
    email: '',
    name: ''
  }),
  actions: {
    // Expected payload { name: Str, email: Str, passwd: Str }
    async register(payload) {
      if (!payload) return null;
      try {
        const res = await this.$axios.post(
          '/auth/register',
          payload,
          { withCredentials: false }
        );
  
        if (res && res.status === 200) {
          return true;
        }
        return false;
      }
      catch (error) {
        console.log(error)
      }
    },

    // Expected payload { email:Str, passwd:Str }
    async login(payload) {
      if (!payload) return null;
      try {
        const res = await this.$axios.post(
          '/auth/login',
          payload,
          { withCredentials: false }
        );
  
        if (res && res.status === 200) {
          // Set session data
          this.setSessionActive(true);
          this.setNameAndEmail(res.data.user);

          // Set jwt into axios requests
          const auth_jwt = res.headers['authorization'];
          this.$axios.defaults.headers.common['Authorization'] = auth_jwt;
        }
      }
      catch (error) {
        console.log(error)
      }
    },

    // THIS IS AN API CALL TEST
    async test() {
      try {
        const res = await this.$axios.get(
          '/auth/protected'
        );
  
        if (res && res.status === 200) {
          console.log(res.data);
          return true;
        }
        return false;
      }
      catch (error) {
        console.log(error)
      }
    },

    setSessionActive(payload) {
      this.isSessionActive = payload;
    },

    setNameAndEmail(payload) {
      this.name = payload.name;
      this.email = payload.email;
    }
  },
  getters: {
    getIsSessionActive: (state) => state.isSessionActive,
    getName: (state) => state.name,
    getEmail: (state) => state.email
  },
})
