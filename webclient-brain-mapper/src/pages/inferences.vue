<template>
  <div class="flex flex-col bg-berry-secondary min-h-full pb-16">

    <div class="font-bold text-center mt-40">
      <h1 class="uppercase text-berry-highlight text-6xl tracking-wide underline underline-offset-8 decoration-2 antialiased">{{ $t('inferences.title') }}</h1>
      <div class="py-4 text-berry-primary before:content-['⚊'] after:content-['⚊'] text-4xl">
        <v-icon class="text-4xl">mdi-pin</v-icon> {{ $t('inferences.shortTitle') }}
      </div>
    </div>

    
    <div class="flex-1 flex justify-center items-center">
      <!-- Show input just when there is no results to show -->
      <v-container
        v-if="!showInferenceResults"
        class="w-full md:w-60"
      >
        <div class="flex justify-center w-full">
          <div class="w-full md:w-3/5 bg-white rounded-lg shadow-md p-4">
            <v-file-upload
              ref="imgInput"
              v-model="imageInput"
              accept="image/*"
              show-size density="default" color="white"
              class="border-gray-300"
              :title="$t('inferences.instructions')"
              :browse-text="$t('inferences.searchBtn')"
              :rules="imageInputRules"
              @change="chargeImage"
              @update:modelValue="chargeImage"
              @click:clear="clearImgAndInput"
            >

              <!-- *Add the template empty so the divider doesn't appear -->
              <template v-slot:divider></template>

            </v-file-upload>
          </div>
        </div>

        <div v-if="isImgCharged" class="text-center">
          <v-btn
            color="highlight" size="x-large"
            class="mt-10 text-none"
            append-icon="mdi-upload"
            @click="generateInference"
          >
            {{ $t('inferences.mapImage') }}
          </v-btn>
        </div>

      </v-container>

      <!-- Container to show the results -->
      <v-container
        v-else
        class="w-full"
      >
        <!-- Mini sub title -->
        <p class="mb-8 text-center font-bold text-2xl">
          {{ $t('inferences.mapResult') }}
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <!-- *Original image -->
          <v-card
            color="white" rounded="lg" variant="elevated" 
          >
            <v-card-item>
              <!-- *The image should display an aspect ratio of 16/9 and have a limit heigth but auto width to display them correctly in the cards -->
              <v-img
                variant="elevated" alt="Broken"
                aspect-ratio="16/9" height="500" max-height="500" class="bg-berry-primary"
                :src="baseImageUrls.liveURL"
              ></v-img>

              <v-card-text class="font-semibold text-xl">{{ $t('inferences.originalImg') }}</v-card-text>

            </v-card-item>
          </v-card>

          <!-- *Inferences results -->
          <v-card
            color="white" rounded="lg" variant="elevated" 
          >
            <v-card-item>
              <v-img
                alt="Broken"
                aspect-ratio="16/9" height="500" max-height="500" class="bg-berry-primary"
                :src="generatedImageUrl"
              ></v-img>

              <v-card-text class="font-semibold text-xl">{{ $t('inferences.mappedImg') }}</v-card-text>

            </v-card-item>
          </v-card>

        </div>

        <!-- Button to close results -->
        <div class="flex justify-center items-center mt-8">
          <v-btn
            color="highlight"
            class="text-none"
            prepend-icon="mdi-close-circle"
            @click="clearAll()"
            >
            {{ $t('inferences.closeResults') }}
          </v-btn>
        </div>
      </v-container>
    </div>
  </div>
</template>

<script>
import ApiUrls from '@/constants/ApiUrls';
import { useInferenceStore } from "@/stores/inference";
import { useToast } from "vue-toastification";

export default {
  name: 'InferencesPage',
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

      // *Changed the default validation for a custom one since the component doesn't have a default one
      if(!this.isValidFile(this.imageInput)) {
        this.toast.error(this.$t('inferences.invalidFile'));
        this.imageInput = null; // Reset input
        return;
      }

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
        this.toast.error(this.$t('inferences.presignedErr'));
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
        this.toast.error(this.$t('inferences.imgUploadErr'));
        console.log(error);
        return false;
      }

      // If everything ok return acknowledge
      return true
    },

    async generateInference() {
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
        imgObjectKey: this.baseImageUrls.imgObjectKey
      }

      // API call to generate an inference using the base img and get the inference img url
      try {
        this.generatedImageUrl = await this.inferenceStore.generateInference(inferencePayload);
      } catch (error) {
        console.log(error);
        this.toast.error(this.$t('inferences.mapErr'));
        return;
      }

      // Set flag to show results, results are shown before storing inference
      this.showInferenceResults = true;

      // Show success notification
      this.toast.success(this.$t('inferences.mapOk'));
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
