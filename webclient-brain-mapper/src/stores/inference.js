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
            console.log(import.meta.env.VITE_NN_API_URL);
            const response = await fetch(import.meta.env.VITE_NN_API_URL, {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                  imgObjectKey: imgObjectKey,
                }),
            });

            if (!response.ok) {
                throw new Error('Could not generate an inference');
            }
          
            const data = await response.json();
            return data.generatedImgUrl;
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
