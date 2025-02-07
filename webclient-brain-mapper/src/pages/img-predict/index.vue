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
        class="w-full md:w-60"
        v-if="!showInferenceResults"
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
              @click="generateAndUploadInference"
            >
              {{ $t('imgPredict.mapImage') }}
            </v-btn>
          </div>
        </div>
      </v-container>

      <!-- Container to show the results -->
      <v-container
        class="w-full md:w-80"
        v-else
      >
        <!-- Mini sub title -->
        <p class="mb-8 text-center">
          {{ $t('imgPredict.mapResult') }}
        </p>

        <!-- Inference results -->
        <v-row>
          <!-- Base img -->
          <v-col cols="12" lg="6">
            <div>
              <img :src="baseImageUrls.liveURL" alt="Broken" style="max-width:100%; height:auto;">
            </div>
          </v-col>

          <!-- Prediction -->
          <v-col cols="12" lg="6">
            <div>
              <img :src="generatedImageUrl" alt="Broken" style="max-width:100%; height:auto;">
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
        console.error('Pre-sign error', err);
        return false;
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
        console.log(error);
        return false;
      }

      // If everything ok return acknowledge
      return true
    },

    async generateAndUploadInference() {
      // If no img charged in input ends function
      if(!this.isImgCharged) return;

      // If base image wasn't uploaded, upload base image to s3
      if(!this.baseImageUploaded) {
        // Upload img and set it as uploaded
        const wasUploaded = await this.uploadBaseImgToS3();

        // Mark it as uploaded
        if(wasUploaded) this.baseImageUploaded = true;
        else return; // otherwise end function
      }

      // If everything was ok, prepare api call to generate an inference
      const inferencePayload = {
        name: this.inferenceName,
        imgUrl: this.baseImageUrls.liveURL,
        imgObjectKey: this.generatedImageUrl
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
