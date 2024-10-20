<template>
  <v-app>
    <navbar-comp/>

    <v-main>
      <router-view />
    </v-main>

    <footer-comp/>
  </v-app>
</template>

<script>
  import NavbarComp from '@/components/NavbarComp.vue';
  import FooterComp from '@/components/FooterComp.vue';

  export default {
    components: {
      NavbarComp,
      FooterComp
    },
  };
</script>
