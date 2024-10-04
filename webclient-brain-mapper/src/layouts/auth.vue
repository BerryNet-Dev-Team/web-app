<template>
  <v-app>
    <v-container class="fill-height">
      <v-responsive
        class="mx-auto"
        max-width="500"
      >
        <v-sheet :elevation="6" rounded style="margin: 15px;">
          <v-main>
            <router-view />
          </v-main>
        </v-sheet>
      </v-responsive>
    </v-container>
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