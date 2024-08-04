<template>
  <NavbarComp/>
  <div class="bg-auxiliary-dark min-h-full">
    Prueba de perfil
  </div>
  <FooterComp/>
</template>

<script>
  import NavbarComp from '@/components/NavbarComp.vue';
  import FooterComp from '@/components/FooterComp.vue';
</script>

<route lang="json">
  {
    "meta":{
      "layout": "profile",
      "requiresAuth": false
    }
  }
</route>