import { defineStore } from 'pinia'
import ApiUrls from '@/constants/ApiUrls';

export const useSceneStore = defineStore('scene', {
  state: () => ({

  }),

  actions: {
    /**
     * @description Save scene into server
     * @param {Object} scene Obj {name: Str, imageUrl:Str, mapUrl:Str}
     */
    async addScene(payload) {
      let res;
      try {
        res = await this.$axios.post(
          ApiUrls.addScene,
          payload
        );
      }
      catch (error) {
        console.error(error);
        throw error;
      }
    }
  }
});
