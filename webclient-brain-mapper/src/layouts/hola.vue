<template>
  <v-container>
    {{ $t('hi') }}
  </v-container>
  <router-view />
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