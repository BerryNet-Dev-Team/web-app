<template>
  <nav class="bg-berry-primary text-white flex items-center justify-between px-8 py-5">
    <div>
      Logo
    </div>
    <div class="flex items-center justify-between">
      <v-btn class="bg-berry-alert text-white transition delay-75 hover:scale-105" @click="gotoImgPredict">{{$t('navFoot.generate')}}</v-btn>
      <button class="w-14 mx-3">
        <img src="../assets/avatar.jpg" alt="Profile picture" class="rounded-full">
      </button>
    </div>
  </nav>
</template>

<script>
  export default {
    name: 'NavbarComp',

    methods: {
      gotoImgPredict() {
        this.$router.push('/img-predict');
      }
    }
  }
</script>
