import { defineStore } from 'pinia'
import ApiUrls from '@/constants/ApiUrls';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isSessionActive: false,
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

          // Store JWT in localStorage
          localStorage.setItem('token', JSON.stringify(auth_jwt));

          // Returns true for better control in component
          return true;
        }
      }
      catch (error) {
        // If just creds are wrong return false
        if (
          error.response
          && error.response.status === 401
          || error.response.status === 400
        ) return false; // Returns false for better control in component

        // Otherwise re-throw error
        console.log(error);
        throw error;
      }
    },

    async isLoggedIn() {
      let res;
      try {
        res = await this.$axios.get(
          ApiUrls.isLoggedIn
        );
      }
      catch (error) {
        console.error(error)
        return false;
      }

      // If everything is ok return response data
      if (res && res.status === 200) {
        return res.data.loggedIn;
      }

      // If response was not successful return false
      return false;
    },

    async initiateAppSession() {
      // Get token from localStorage
      const auth_jwt = JSON.parse(localStorage.getItem('token'));

      // Set jwt into axios requests
      this.$axios.defaults.headers.common['Authorization'] = auth_jwt;

      // Verify session(token) validity
      let res;
      try {
        res = await this.$axios.get(
          ApiUrls.isLoggedIn
        );
      }
      catch (error) {
        // If something happened that triggered an Error
        // Or error is 500 or above, rethrow error to block app
        if(!error.response || error.response?.status >= 500) {
          throw error;
        }
      }

      // If user session is still alive
      if (res && res.data.loggedIn) {
        // Get and set user name from localStorage
        this.setName(localStorage.getItem('name'));

        // Set session as active
        this.setSessionActive(true);

        // Get and set user role
        let roleResponse;
        try {
          roleResponse = await this.$axios.get(
            ApiUrls.getUserRole
          );
        }
        catch (error) {
          // If something happened that triggered an Error
          // Or error is 500 or above, rethrow error to block app
          if(!error.response || error.response?.status >= 500) {
            throw error;
          }
        }

        const userRole = roleResponse.data.role;
        this.setRole(userRole);
      }
    },

    async logout() {
      try {
        const res = await this.$axios.post(
          ApiUrls.logout,
        );

        if (res && res.status === 200) {
          // Clear session data
          this.setSessionActive(false);
          this.resetUserInfo();

          // Clear jwt from axios requests
          delete this.$axios.defaults.headers.common['Authorization'];

          // Clear jwt from localStorage
          localStorage.removeItem('token');
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
      localStorage.setItem('name', payload.name);
    },

    setName(payload) {
      this.name = payload;
    },

    setRole(payload) {
      this.role = payload;
    },

    resetUserInfo() {
      this.name = '';
      this.email = '';
      this.role = '';
      localStorage.removeItem('name');
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
