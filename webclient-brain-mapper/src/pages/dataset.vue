<template>
  <div class="flex flex-col bg-berry-secondary min-h-full pb-16">

    <div class="font-bold text-center mt-40">
      <h1 class="uppercase text-berry-highlight text-6xl tracking-wide underline underline-offset-8 decoration-2 antialiased">
        {{ $t('dataset.title') }}
      </h1>
      <div class="py-4 text-berry-primary before:content-['⚊'] after:content-['⚊'] text-4xl">
        <v-icon class="text-4xl">mdi-brain</v-icon> {{ $t('dataset.shortTitle') }}
      </div>
    </div>

    <div class="flex-1 flex justify-center items-center">
      <v-container class="w-full md:w-60">
        <div
          v-if="!isImgCharged"
          class="flex justify-center w-full"
        >
          <div class="w-full md:w-3/5 bg-white rounded-lg shadow-md p-4">
            <v-file-upload
              ref="imgInput"
              v-model="imageInput"
              accept="image/*"
              show-size density="default" color="white"
              class="border-gray-300"
              :title="$t('dataset.instructions')"
              :browse-text="$t('inferences.searchBtn')"
              :rules="imageInputRules"
              @change="chargeImage"
              @update:modelValue="chargeImage"
              @click:clear="clearImgAndCanvasData"
            >

              <!-- *Add the template empty so the divider doesn't appear -->
              <template v-slot:divider></template>

            </v-file-upload>
          </div>
        </div>

        <!-- Charged image container -->
        <div v-if="isImgCharged" class="flex flex-col min-h-full">
          <!-- Clear button -->
          <div class="flex align-center justify-end mb-4 z-50">
            <v-btn
              color="highlight"
              class="text-none"
              prepend-icon="mdi-close-circle"
              @click="clearImgAndCanvasData()"
              >
              {{ $t('dataset.clearImg') }}
            </v-btn>
          </div>

          <!-- Canvas container -->
          <div class="canvas-container">
            <canvas
              id="canvas"
              ref="canvas"
              :width="imgDimensions.width"
              :height="imgDimensions.height"
              :style="{background: `url(${finalImage.displayUrl})`}"
              @click="getPosition"
            ></canvas>
          </div>
          
          <!-- Upload button -->
          <div class="text-center">
            <v-btn
              color="highlight"
              class="mt-10 text-none"
              append-icon="mdi-upload"
              @click="uploadScene"
            >
              {{ $t('dataset.upload') }}
            </v-btn>
          </div>
        </div>
      </v-container>
    </div>
  </div>
</template>

<script>
import ApiUrls from '@/constants/ApiUrls';
import { useSceneStore } from "@/stores/scene";
import { useToast } from "vue-toastification";

export default {
  name: 'DatasetPage',
  data() {
    return {
      imageInput: null,
      isImgCharged: false,
      imgDimensions: {
        width: 0,
        height: 0
      },
      pointSize: 3,

      sceneName: '',
      finalImage: {
        name: '',
        blob: null,
        displayUrl: ''
      },
      imgMap: [],

      toast: useToast(),
      sceneStore: useSceneStore(),
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

    async getImgDimensions(imgUrl) {
      return new Promise((resolve, reject) => {
        // Create temp instance of an image
        const img = new Image();
        img.src = imgUrl;

        // Wait for img until load to start validations
        img.onload = () => {
          // Validates if image has dimensions
          if (img.width && img.height) {
            const imgDimensions = {width: img.width, height: img.height};
            resolve(imgDimensions); // Resolve the promise as true if validation was a success
          }
          else {
            resolve(null);
          }
        };

        // If image couldnt be proccessed, reject the promise
        img.onerror = (error) => {
          console.log(error);
          reject(new Error("Error processing image"));
        };
      });
    },

    // validates if its an image is a valid file
    isValidFile(file) {
      const allowedMimeTypes = ["image/jpg", "image/jpeg", "image/png"];
      return allowedMimeTypes.includes(file.type);
    },

    async chargeImage() {
      if(!this.imageInput) return; // Default return for clear events

      // *Changed the default validation for a custom one since the component doesn't have a default one
      if(!this.isValidFile(this.imageInput)) {
        this.toast.error(this.$t('dataset.invalidFile'));
        this.imageInput = null; // Reset input
        return;
      }

      const fileTempUrl = URL.createObjectURL(this.imageInput);

      try {
        const imgDimensions = await this.getImgDimensions(fileTempUrl);
        this.imgDimensions.width = imgDimensions.width;
        this.imgDimensions.height = imgDimensions.height;
      }
      catch(error) {
        console.log(error)
        return;
      }

      this.finalImage = {
        name: this.imageInput.name,
        blob: this.imageInput,
        displayUrl: fileTempUrl
      };

      this.isImgCharged = true;
    },

    // Reset img, map and canvas data
    clearImgAndCanvasData() {
      this.isImgCharged = false;
      this.imageInput = null;
      this.imgDimensions = {
        width: 0,
        height: 0
      };
      this.finalImage = {
        name: '',
        blob: null,
        displayUrl: ''
      };
      this.imgMap.length = 0;
    },

    // Esta función se ejecuta cuando se hace clic en el canvas
    getPosition(event) {
      const canvas = this.$refs.canvas;
      const rect = canvas.getBoundingClientRect();
      let x = Math.round(event.clientX - rect.left);
      let y = Math.round(event.clientY - rect.top);

      // Validates negative coordinates
      if(x < 0) x = 0;
      if(y < 0) y = 0;

      // Validates overflow coordinates
      if(x > this.imgDimensions.width) x = this.imgDimensions.width;
      if(y > this.imgDimensions.height) y = this.imgDimensions.width;

      // Save coordinates in map array
      this.imgMap.push(`${x} ${y}`);

      // Draw the dot
      this.drawCoordinates(x, y);
    },

    // Esta función dibuja un círculo en las coordenadas clickeadas
    drawCoordinates(x, y) {
      const canvas = this.$refs.canvas;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#03d3fc";

      ctx.beginPath();
      ctx.arc(x, y, this.pointSize, 0, Math.PI * 2, true);
      ctx.fill();
    },

    imgMapToFile() {
      // Setup blob content, if nothing is on imgMap, by default content will be empty string
      let content = '';
      if(this.imgMap.length > 0) {
        content = this.imgMap.join("\n")
      }

      // Creates blob with the content
      let blob = new Blob([content], {type: 'text/plain'});

      // Convert map blob to file
      blob.lastModified = new Date();
      blob.name = `Scene-Map-${new Date()}.txt`;

      return blob;
    },

    async uploadScene() {
      // Get the upload and live URLs
      let imgUrls;
      let mapUrls;
      let res;
      try {
        res = await this.$axios.get(
          ApiUrls.getScenePresignedUrl
        );
        imgUrls = res.data.imgUrls;
        mapUrls = res.data.mapUrls;
      }
      catch (err) {
        this.toast.error(this.$t('dataset.presignedErr'));
        console.log('Pre-sign error', err);
        return;
      }

      // Generate map file and upload it
      const mapFile = this.imgMapToFile();
      try {
        const r = await this.$axios.put(
          mapUrls.uploadURL,
          mapFile,
          {
            headers: {
              'Content-Type': 'text/plain',
              'Authorization': ''
            },
            withCredentials: false
          }
        );
      }
      catch (error) {
        this.toast.error(this.$t('dataset.mapUploadErr'));
        console.log(error)
        return;
      }

      // Upload image to server and get its live url
      try {
        await this.$axios.put(
          imgUrls.uploadURL,
          this.finalImage.blob,
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
        this.toast.error(this.$t('dataset.imgUploadErr'));
        console.log(error);
        return;
      }

      // If everything was ok, now save scene data
      const scenePayload = {
        name: this.sceneName,
        imageUrl: imgUrls.liveURL,
        mapUrl: mapUrls.liveURL
      }

      // Add scene data into DB
      try {
        await this.sceneStore.addScene(scenePayload);
      } catch (error) {
        this.toast.error(this.$t('dataset.addSceneErr'));
        return;
      }

      // Show success notification
      this.toast.success(this.$t('dataset.addSceneOk'));

      // If everything was ok, clear the input, img, map and canvas data
      this.imageInput = null;
      await nextTick();
      this.clearImgAndCanvasData();
    }
  }
}
</script>

<route lang="json">
  {
    "meta": {
      "layout": "default",
      "requiresAuth": true,
      "requiresAdmin": true
    }
  }
</route>

<style>
#canvas {
  cursor: crosshair;
}

.canvas-container{
  max-width: 100%;
  max-height: 900px;
  border: 1px solid black;
  overflow: auto;
}
</style>
