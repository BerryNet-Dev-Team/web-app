<template>
  <div class="flex flex-col bg-berry-secondary min-h-full">
    <v-card
      color="highlight"
      class="font-bold text-4xl text-center py-4"
      variant="elevated"
    >
      {{ $t('imgPredict.title') }}
    </v-card>
    <div class="flex-1 flex justify-center items-center">
      <!-- Show input just when there is no results to show -->
      <v-container
        v-if="!showInferenceResults"
        class="w-full md:w-60"
      >
        <div>
          <p class="mb-8 text-center text-xl font-semibold">
            {{ $t('imgPredict.instructions') }}
          </p>
          <v-file-input
            ref="imgInput"
            v-model="imageInput"
            :label="$t('imgPredict.selectImg')"
            variant="solo-filled"
            prepend-icon="mdi-image"
            chips accept="image/*"
            class="mb-3"
            :rules="imageInputRules"
            @change="chargeImage"
            @click:clear="clearImgAndInput"
          ></v-file-input>

          <div v-if="isImgCharged" class="text-center">
            <v-btn
              color="highlight"
              class="mt-10 text-none"
              append-icon="mdi-upload"
              @click="generateInference"
            >
              {{ $t('imgPredict.mapImage') }}
            </v-btn>
          </div>
        </div>
      </v-container>

      <!-- Container to show the results -->
      <v-container
        v-else
        class="w-full md:w-80"
      >
        <!-- Mini sub title -->
        <div class="grid grid-cols-8 gap-2 mt-12 mb-8">
          <h3 class="col-span-6 col-start-2 text-center text-2xl font-semibold">
            {{ $t('imgPredict.mapResult') }}
          </h3>
          <v-btn
            color="highlight"
            class="text-none"
            prepend-icon="mdi-close-circle"
            @click="clearAll()"
          >
            {{ $t('imgPredict.closeResults') }}
          </v-btn>
        </div>

        <!-- Inference results -->
        <v-row class="mb-16">
          <!-- Base img -->
          <v-col cols="12" lg="6">
            <div class="bg-gray-50 border border-gray-100 rounded-lg shadow-xl p-4">
              <h3 class="mb-4 text-xl font-semibold">
                {{ $t('imgPredict.generatedImg') }}
              </h3>
              <img
                :src="generatedImageUrl"
                alt="Broken"
                style="max-width:100%; height:auto;"
                class="rounded-lg"
              >
            </div>
          </v-col>

          <!-- Prediction -->
          <v-col cols="12" lg="6">
            <div class="bg-gray-50 border border-gray-100 rounded-lg shadow-xl p-4">
              <h3 class="mb-4 text-xl font-semibold">
                {{ $t('imgPredict.baseImg') }}
              </h3>
              <img
                :src="baseImageUrls.liveURL"
                alt="Broken"
                style="max-width:100%; height:auto;"
                class="rounded-lg"
              >
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
import ApiUrls from '@/constants/ApiUrls';
import { useInferenceStore } from "@/stores/inference";
import { useToast } from "vue-toastification";

export default {
  name: 'ImgPredict',
  data() {
    return {
      imageInput: null,
      isImgCharged: false,

      inferenceName: '',
      baseImageUploaded: false,
      baseImageUrls: {
        uploadURL: '',
        liveURL: '',
        imgObjectKey: ''
      },
      generatedImageUrl: '',

      showInferenceResults: false,

      toast: useToast(),
      inferenceStore: useInferenceStore(),
    }
  },

  created() {
    this.imageInputRules = [
      v => !!v || this.$t('auth.register.emptyFieldFeedB'),
      v => !this.isValidFile(v) || "Invalid file type"
    ]
  },

  methods: {
    getFileName(url) {
      const splitted = url.split('/');
      const filename = splitted[splitted.length - 1];
      return filename;
    },

    // validates if its an image is a valid file
    isValidFile(file) {
      const allowedMimeTypes = ["image/jpg", "image/jpeg"];
      return allowedMimeTypes.includes(file.type);
    },

    async chargeImage() {
      if(!this.imageInput) return; // Default return for clear events

      if(!await this.$refs.imgInput.validate()) return;

      this.isImgCharged = true;
    },

    // Reset img, map and canvas data
    clearImgAndInput() {
      this.isImgCharged = false;
      this.imageInput = null;
    },
    
    clearAll() {
      this.isImgCharged = false;
      this.imageInput = null;
      this.baseImageUploaded = false;
      this.baseImageUrls= {
        uploadURL: '',
        liveURL: '',
        imgObjectKey: ''
      };
      this.generatedImageUrl= '';
      this.showInferenceResults= false;
    },

    async uploadBaseImgToS3() {
      // Get the upload and live URLs
      let res;
      try {
        res = await this.$axios.get(
          ApiUrls.getBaseImgPresignedUrls
        );
        Object.assign(this.baseImageUrls, res.data);
      }
      catch (err) {
        this.toast.error(this.$t('imgPredict.presignedErr'));
        throw err;
      }

      // Upload image to server
      try {
        await this.$axios.put(
          this.baseImageUrls.uploadURL,
          this.imageInput,
          {
            headers: {
              'Content-Type': 'image/*',
              'Authorization': ''
            },
            withCredentials: false
          }
        );
      }
      catch (error) {
        this.toast.error(this.$t('imgPredict.imgUploadErr'));
        throw error
      }

      // If everything ok acknowledge base img was uploaded
      this.baseImageUploaded = true;
    },

    async generateInference() {
      // If no img charged in input ends function
      if(!this.isImgCharged) return;

      // If base image wasn't uploaded, upload base image to s3
      if(!this.baseImageUploaded) {
        // Upload img and set it as uploaded
        try {
          await this.uploadBaseImgToS3();
        } catch (error) {
          console.log(error);
          return;
        }
      }

      // If everything was ok, prepare api call to generate an inference
      const inferencePayload = {
        name: this.inferenceName,
        imgUrl: this.baseImageUrls.liveURL,
        imgObjectKey: this.baseImageUrls.imgObjectKey
      }

      // API call to generate an inference using the base img and get the inference img url
      try {
        this.generatedImageUrl = await this.inferenceStore.generateInference(inferencePayload);
      } catch (error) {
        console.log(error);
        this.toast.error(this.$t('imgPredict.generateErr'));
        return;
      }

      // Set flag to show results, results are shown before storing inference
      this.showInferenceResults = true;

      // Show success notification
      this.toast.success(this.$t('imgPredict.generateOk'));
    }
  }
}
</script>

<route lang="json">
  {
    "meta": {
      "layout": "default",
      "requiresAuth": true
    }
  }
</route>

<style>

</style>
