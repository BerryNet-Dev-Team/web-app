<template>
  <div class="bg-brain-auxiliary-dark min-h-screen flex justify-center items-center">
    <div class=" min-w-3/5 max-w-3/5 flex flex-col gap-5 px-5 pb-5">
      <p class="text-balance md:text-center lg:text-center max-w-full font-semibold text-white text-5xl md:p-10">
        {{ $t('default.create.uploadMessage') }}
      </p>
      <v-form ref="form" @submit.prevent="SaveForm">
        <v-text-field
          :label="$t('default.create.labelName')" bg-color="white" variant="outlined"
          clearable class="my-2"
          required :rules="nameRules"
        ></v-text-field>

        <v-file-input
          v-model="images" @change="ChangeFiles" class="my-2"
          :label="$t('default.create.labelImages')" multiple
          prepend-icon="mdi-upload"
          @click:clear="ClearPreviews"
          outlined block bg-color="white"
          show-size variant="outlined"
          required :rules="fileRules"
        ></v-file-input>

        <v-divider></v-divider>
        <h4 class="text-3xl text-white font-semibold text-center">{{ $t('default.create.previewTitle') }}</h4>

        <v-carousel v-if="urlPreviews.length>0">
          <v-carousel-item
            v-for="(image, index) in urlPreviews" :key="index"
            :src="image" cover
          ></v-carousel-item>
        </v-carousel>

        <v-btn color="#F26721" type="submit" class="my-2" block>{{ $t('default.create.labelBtn') }}</v-btn>
      </v-form>
    </div>
  </div>
</template>

<script>
  export default {
    data(){
      return{
        images: [],
        urlPreviews: [],
      }
    },
    created() {
      this.nameRules = [
        v => !!v || this.$t('default.create.emptyName')
      ];
      this.fileRules = [
        v => v.length > 0 && !!v || this.$t('default.create.emptyFiles'),
      ];
    },
    methods:{
      async SaveForm(){
        const { valid } = await this.$refs.form.validate();
        if(!valid){
          console.log("Error al guardar el formulario");
        }else{
          console.log("Guardando formulario");
        }
      },
      ChangeFiles(){
        const newArray = Array.from(this.images)
          .filter(file => file.type.startsWith("image/"))
          .map(file => URL.createObjectURL(file));
        this.urlPreviews = newArray;
      },
      ClearPreviews(){
        this.urlPreviews = [];
      }
    }
  }
</script>

<route lang="json">
  {
    "meta": {
    "layout": "default",
    "requiresAuth": false
    }
  }
</route>

<style scoped>

</style>
