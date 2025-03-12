// Utilities
import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
  state: () => ({
    backendAvailable: true // In theory backend is always up
  }),
  actions: {
    setBackendAvailable(payload) {
      this.backendAvailable = payload;
    }
  },
  getters: {
    isBackendAvailable: (state) => state.backendAvailable,
  },
})
