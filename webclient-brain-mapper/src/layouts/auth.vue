<template>
  <v-app class="bg-berry-secondary">
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup>
  //
</script>

<route lang="json">
  {
    "meta":{
      "requiresAuth": false
    }
  }
</route>
