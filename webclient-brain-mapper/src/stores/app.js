// Utilities
import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
  state: () => ({
    pais: null
  }),
  actions: {
    async getCountryName() {
      try {
        const res = await this.$axios.get(
          '/api/',
          {
            withCredentials: false
          }
        );
  
        this.pais = res.data.info.seed;
      }
      catch (error) {
        console.log(error)
      }
    }
  },
  getters: {
    country: (state) => state.pais,
  },
})
