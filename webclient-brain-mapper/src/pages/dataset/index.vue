<template>
  <div class="flex flex-col bg-berry-secondary min-h-full">
    <v-card
      color="highlight"
      class="font-bold text-4xl text-center py-4 mt-28"
      variant="elevated"
    >
      {{ $t('dataset.title') }}
    </v-card>
    <div class="flex-1 flex justify-center items-center">
      <v-container class="w-full md:w-60">
        <div>
          <p class="mb-8 text-center text-xl font-semibold">
            {{ $t('dataset.instructions') }}
          </p>
          <v-file-input
            ref="imgInput"
            v-model="imageInput"
            :label="$t('dataset.selectImg')"
            variant="solo-filled"
            prepend-icon="mdi-image"
            chips accept="image/*"
            class="mb-3"
            :rules="imageInputRules"
            @change="chargeImage"
            @click:clear="clearImgAndCanvasData"
          ></v-file-input>
        </div>
        <div v-if="isImgCharged" class="canvas-container">
          <canvas
            id="canvas"
            ref="canvas"
            @click="getPosition"
            :width="imgDimensions.width"
            :height="imgDimensions.height"
            :style="{background: `url(${finalImage.displayUrl})`}"
          ></canvas>
        </div>

        <div v-if="isImgCharged" class="text-center">
          <v-btn
            color="highlight"
            class="mt-10 text-none"
            append-icon="mdi-upload"
            @click="uploadScene"
          >
            {{ $t('dataset.upload') }}
          </v-btn>
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

      if(!await this.$refs.imgInput.validate()) return;

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
      const x = Math.round(event.clientX - rect.left);
      const y = Math.round(event.clientY - rect.top);

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
