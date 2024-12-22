<template>
  <div class="flex flex-col bg-brain-auxiliary-dark min-h-full">
    <v-card 
      class="font-bold text-4xl text-center py-4"
      variant="elevated"
      color="orange-darken-1"
    >
      Mis mapeos
    </v-card>
    <div class="flex-1 flex justify-center items-center">
      <v-container class="w-full md:w-60">
        <div>
          <v-file-input
            ref="imgInput"
            v-model="imageInput"
            label="Ingresa una imagen"
            variant="solo-filled"
            prepend-inner-icon="mdi-image"
            chips accept="image/*"
            :rules="imageInputRules"
            @change="chargeImage"
          ></v-file-input>
        </div>
        <div v-if="isImgCharged" class="canvas-container">
          <canvas
            ref="canvas"
            @click="getPosition"
            :width="imgDimensions.width"
            :height="imgDimensions.height"
            :style="{background: `url(${finalImage.displayUrl})`}"
          ></canvas>
        </div>
      </v-container>
    </div>
  </div>
</template>

<script>
import ApiUrls from '@/constants/ApiUrls';
import { useSceneStore } from "@/stores/scene";

export default {
  data() {
    return {
      name: 'John Lasasgna',
      imageInput: null,
      isImgCharged: false,
      imgDimensions: {
        width: 0,
        height: 0
      },
      finalImage: {
        name: '',
        blob: null,
        displayUrl: ''
      },
      imgMap: [],
      pointSize: 3,
      dynamicHeight: 683,
      dynamicWidth: 1024,

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

    // validates if its an image valid file
    isValidFile(file) {
      const allowedMimeTypes = ["image/jpg", "image/jpeg", "image/png"];
      return allowedMimeTypes.includes(file.type);
    },

    async chargeImage() {
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

    // Esta función se ejecuta cuando se hace clic en el canvas
    getPosition(event) {
      const canvas = this.$refs.canvas;
      const rect = canvas.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;

      // Save coordinates in map array
      this.imgMap.push(`${x} ${y}`);

      // Draw the dot
      this.drawCoordinates(x, y);
    },
    
    // Esta función dibuja un círculo en las coordenadas clickeadas
    drawCoordinates(x, y) {
      const canvas = this.$refs.canvas;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#ff2626"; // Rojo

      ctx.beginPath();
      ctx.arc(x, y, this.pointSize, 0, Math.PI * 2, true);
      ctx.fill();
    },

    imgMapToFile() {
      const content = this.imgMap.join("/n")
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
        imgUrls = res.data.responseData.imgUrls;
        mapUrls = res.data.responseData.mapUrls;
      }
      catch (err) {
        console.log('Pre-sign error');
        return;
      }

      // Generate map file and upload it
      const mapFile = this.imgMapToFile();
      try {
        await this.$axios({
          method: 'put',
          headers: {
            'Content-Type': 'text/plain',
          },
          withCredentials: false,
          url: mapUrls.uploadURL,
          data: mapFile,
        });
      }
      catch (error) {
        console.log(error)
        return;
      }


      // Upload image to server and get its live url
      try {
        await this.$axios({
          method: 'put',
          headers: {
            'Content-Type': 'image/*',
          },
          withCredentials: false,
          url: imgUrls.uploadURL,
          data: imageObj.blob,
        });
      }
      catch (error) {
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
        return;
      }
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
.canvas-container{
  max-width: 100%;
  max-height: 900px;
  border: 1px solid black;
  overflow: auto;
}
</style>