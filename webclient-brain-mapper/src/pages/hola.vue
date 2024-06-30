<template>
  <v-btn variant="outlined">
    {{ $t('hi') }}
    <v-icon icon="mdi-home" />
  </v-btn>
</template>

<route lang="json">
  {
    "meta":{
      "layout": "hola",
      "requiresAuth": false
    }
  }
</route>