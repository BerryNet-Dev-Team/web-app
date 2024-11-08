<template>
  <div class="bg-brain-auxiliary-dark min-h-full">
    <div class="w-full h-50 flex flex-col md:flex-row justify-center items-center py-16">
      <div>
        <v-avatar image="@/assets/avatar.jpg" size="256" class="shadow-2xl hover:cursor-pointer">
        </v-avatar>
      </div>
      <div class="w-full md:w-1/4">
        <p class="font-semibold text-wrap text-6xl text-white tracking-normal p-5">
          {{ name }}
        </p>
      </div>
    </div>
    <v-card
      class="font-bold text-4xl text-center py-4"
      variant="elevated"
      color="orange-darken-1"
    >
      {{ $t('default.profile.myScans') }}
    </v-card>

    <div class="w-full my-5 p-5">
      <v-row>
        <v-col v-for="(map, index) in maps" cols="12" md="4" :key="index">
          <v-card link color="#2E5B7D">
            <v-card-title class="font-semibold text-center">{{map.name}}</v-card-title>
            <v-divider></v-divider>
            <v-img
              src="/src/assets/brain.png"
              height="200"
            ></v-img>
            <v-card-text>
              <div class="w-full flex justify-between px-5">
                <div class="text-left font-semibold text-xl">
                  {{ map.date }}
                </div>
                <div class="font-semibold text-xl">
                  {{ $t('default.profile.numPics') }} {{map.pictures}}
                </div>
              </div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </div>

  </div>
</template>

<script>
  export default {
    data() {
      return {
        name: 'Nombre1 Nombre2 ApellidoP ApellidoM',
        maps:[
          { name: "Mapeo1", date: "24/10/2024", pictures: 10 },
          { name: "Mapeo2", date: "25/10/2024", pictures: 10 },
          { name: "Mapeo3", date: "26/10/2024", pictures: 10 },
          { name: "Mapeo4", date: "27/10/2024", pictures: 10 },
          { name: "Mapeo5", date: "28/10/2024", pictures: 10 }
        ]
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
      "requiresAuth": false
    }
  }
</route>
