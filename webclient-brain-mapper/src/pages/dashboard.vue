<template>
  <div class="h-full w-full flex md:flex-col items-center justify-center flex-wrap bg-berry-secondary">
    <div class="mb-6 mt-16">
      <v-img
          src="@/assets/BerryNet_LogoHorizontal.png"
          width="300"
          cover
        >
      </v-img>
    </div>

    <div class="grid grid-cols-1 grid-rows-2 gap-4 w-full h-3/5 md:w-2/3 p-4">

      <div
        v-if="isAdmin"
        class="bg-berry-highlight rounded-xl shadow-xl
          grid grid-cols-1 md:grid-cols-6 grid-rows-2 md:grid-rows-1 gap-4
          text-berry-whiteaux font-semibold
          border-2 border-gray-700 transition-all duration-300 ease-in-out
          hover:border-berry-whiteaux group hover:opacity-90"
      >
        <div class="p-4 md:px-8 md:py-6 col-span-4">
          <h3 class="text-5xl">{{ $t('dashboard.dataset') }}</h3>
          <p class="text-balance text-2xl w-full my-2">{{ $t('dashboard.datasetDesc') }}</p>
          <v-btn 
            class="mt-4 bg-berry-primary text-berry-whiteaux" 
            size="x-large" 
            rounded
            @click="$router.push({ path: '/dataset' })"
          >
            Entrenar
          </v-btn>
        </div>

        <div class="col-span-2 md:opacity-0 w-[80px] md:w-[200px] group-hover:!opacity-100 transition-opacity duration-200 flex justify-center items-center">
          <v-img
            class="h-[80px] md:h-[200px]"
            src="@/assets/brain_intel.svg"
            height="200"
          ></v-img>
        </div>
      </div>

      <div
        class="bg-berry-highlight rounded-xl shadow-xl
          grid grid-cols-1 md:grid-cols-6 grid-rows-2 md:grid-rows-1 gap-4
          text-berry-whiteaux font-semibold
          border-2 border-gray-700 transition-all duration-300 ease-in-out
          hover:border-berry-whiteaux group hover:opacity-90"
      >
        <div class="p-4 md:p-8 col-span-4">
          <h3 class="text-5xl">{{ $t('dashboard.predict') }}</h3>
          <p class="text-balance text-2xl w-full my-2">{{ $t('dashboard.predictDesc') }}</p>
          <v-btn 
            class="mt-4 bg-berry-primary text-berry-whiteaux" 
            size="x-large" 
            rounded
            @click="$router.push({ path: '/inferences' })"
          >
            Generar
          </v-btn>
        </div>

        <div class="col-span-2 md:opacity-0 w-[80px] md:w-[200px] group-hover:!opacity-100 transition-opacity duration-200 flex justify-center items-center">
          <v-img
            class="h-[80px] md:h-[200px]"
            src="@/assets/pin.svg"
            height="200"
          ></v-img>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import { mapState } from 'pinia';
import { useAuthStore } from "@/stores/auth";
export default {
  name: 'DashboardPage',
  data(){
    return {
      prueba: 'Mensaje'
    }
  },

  computed: {
    ...mapState(useAuthStore, {
      isAdmin: (store) => store.isAdmin,
    })
  },
};
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