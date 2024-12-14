import { defineStore } from 'pinia'
import ApiUrls from '@/constants/ApiUrls';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isSessionActive: null,
    email: '',
    name: '',
    role: ''
  }),
  actions: {
    // Expected payload { name: Str, lastName: Str, email: Str, passwd: Str }
    async register(payload) {
      if (!payload) return null;
      try {
        const res = await this.$axios.post(
          ApiUrls.register,
          payload,
          { withCredentials: false }
        );
  
        if (res && res.status === 200) {
          return true;
        }
        return false;
      }
      catch (error) {
        console.log(error);
        return false;
      }
    },

    // Expected payload { email:Str, passwd:Str }
    async login(payload) {
      if (!payload) return null;
      try {
        const res = await this.$axios.post(
          ApiUrls.login,
          payload,
          { withCredentials: false }
        );
  
        if (res && res.status === 200) {
          // Set session data
          this.setSessionActive(true);
          this.setUserInfo(res.data.user);

          // Set jwt into axios requests
          const auth_jwt = res.headers['authorization'];
          this.$axios.defaults.headers.common['Authorization'] = auth_jwt;

          // Returns true for better control in component
          return true;
        }

        // Returns false to raise error in component
        return false;
      }
      catch (error) {
        console.log(error);
        return false;
      }
    },

    async logout() {
      try {
        const res = await this.$axios.post(
          ApiUrls.logout,
          payload,
          { withCredentials: false }
        );

        if (res && res.status === 200) {
          // Clear session data
          this.setSessionActive(false);
          this.resetUserInfo();

          // Clear jwt from axios requests
          delete this.$axios.defaults.headers.common['Authorization'];
        }
      }
      catch (error) {
        console.error(error)
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

    setUserInfo(payload) {
      this.name = payload.name;
      this.email = payload.email;
      this.role = payload.role.name;
    },

    resetUserInfo() {
      this.name = '';
      this.email = '';
      this.role = '';
    }
  },
  getters: {
    getIsSessionActive: (state) => state.isSessionActive,
    getName: (state) => state.name,
    getEmail: (state) => state.email,

    // Check if user is admin
    isAdmin: (state) => state.role === 'ADMIN',
  },
})
