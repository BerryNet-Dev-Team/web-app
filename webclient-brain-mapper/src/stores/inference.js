import { defineStore } from 'pinia'
import ApiUrls from '@/constants/ApiUrls';

export const useInferenceStore = defineStore('inference', {
  state: () => ({

  }),

  actions: {
    /**
     * @description Generate inference and save it into server
     * @param {Object} scene Obj {name: Str, imgUrl:Str, imgObjectKey:Str}
     */
    async generateInference(payload) {
      let res;
      try {
        res = await this.$axios.post(
          ApiUrls.generateInference,
          payload
        );

        return res.data.generatedImgUrl;
      }
      catch (error) {
        console.error(error);
        throw error;
      }
    }
  }
});
