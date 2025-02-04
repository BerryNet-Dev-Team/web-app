<template>
  <div class="bg-berry-secondary min-h-full">
    <div class="w-full h-50 flex flex-col md:flex-row justify-center items-center py-16">
      <div>
        <v-avatar image="@/assets/avatar.jpg" size="256" class="shadow-2xl hover:cursor-pointer">
        </v-avatar>
      </div>
      <v-icon
        icon="mdi-pencil"
        class="bg-whiteaux p-5 rounded-lg m-3 hover:cursor-pointer transition delay-75 hover:scale-105"
      >
      </v-icon>
      <p class="font-bold text-left text-pretty text-4xl text-white p-5">
        {{ name }}
      </p>
    </div>
    <v-card
      class="font-bold text-4xl text-center py-4 bg-berry-alert text-white"
      variant="elevated"
    >
      Mis mapeos
    </v-card>
    <div class="flex justify-center items-center">
      <v-container class="w-full md:w-60">
        <v-carousel>
          <v-carousel-item
            v-for="n in maps"
            :key="n"
            src="@/assets/brain.png"
            alt="Preview del mapeo"
            @click="getMapClicked(n)"
          >
          </v-carousel-item>
        </v-carousel>
      </v-container>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        name: 'John Lasasgna',
        maps:[1, 2, 3, 4, 5]
      }
    },
    methods:{
      getMapClicked(id){
        console.log(id);
      }
    }
  }

</script>

<route lang="json">
  {
    "meta": {
      "layout": "default",
      "requiresAuth": false,
      "requiresAdmin": false
    }
  }
</route>
