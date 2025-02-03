import { defineStore } from 'pinia'
import ApiUrls from '@/constants/ApiUrls';

export const useInferenceStore = defineStore('inference', {
  state: () => ({

  }),

  actions: {
    /**
     * @description Call to nn api to generate an inference
     * @param {String} imgObjectKey 
     */
    async generateInference(imgObjectKey) {
        try {
            const response = await this.$axios.post(
              import.meta.env.VITE_NN_API_URL,
              {imgObjectKey: imgObjectKey},
              {
                headers: {'Authorization': ''},
                withCredentials: false
              }
            );

            return response.data.generatedImgUrl;
        } catch (error) {
            console.error(error);
            throw error;
        }
    },

    /**
     * @description Save inference into server
     * @param {Object} scene Obj {name: Str, baseImageUrl:Str, generatedImageUrl:Str}
     */
    async addInference(payload) {
      let res;
      try {
        res = await this.$axios.post(
          ApiUrls.addInference,
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
