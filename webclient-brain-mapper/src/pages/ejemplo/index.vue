<template>
  <v-container class="bg-surface-variant">
    <v-row no-gutters>
      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>

      <v-col cols="6">
        <v-sheet class="pa-2 ma-2">
          .v-col-6
        </v-sheet>
      </v-col>

      <v-col>
        <v-sheet class="pa-2 ma-2">
          {{ store.country }}
        </v-sheet>
      </v-col>
    </v-row>

    <v-row no-gutters>
      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>

      <v-col cols="2">
        <v-sheet class="pa-2 ma-2">
          .v-col-2
        </v-sheet>
      </v-col>

      <v-col>
        <v-btn variant="tonal" @click="getCountryName">
          Index
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useAppStore } from '@/stores/app';

// Set store in the component
const store = useAppStore()

const pais = ref('')

async function getCountryName() {
  await store.getCountryName();
}
</script>

<route lang="json">
  {
    "meta":{
      "requiresAuth": false
    }
  }
</route>
