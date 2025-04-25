<template>
  <nav class="flex justify-center w-full fixed top-6 z-50">
    <div class="bg-berry-primary rounded-xl w-auto p-0.5 flex justify-center items-center shadow-lg">

      <div class="p-2 transition-all duration-200 hover:brightness-110">
        <v-img
          class="hover:cursor-pointer"
          src="@/assets/BerryNet_LogoHorizontal.png"
          heigth="60" width="150"
          cover
          @click="$router.push({ path: '/dashboard' })"
        >
        </v-img>
      </div>

      <v-btn 
        value="recent"
        class="text-berry-whiteaux" size="small"
        rounded stacked variant="text"
        @click="$router.push({ path: '/inferences' })"
      >
        <v-icon>mdi-pin</v-icon>
        <span>{{ $t('appNavbar.generate') }}</span>
      </v-btn>

      <v-btn 
        value="recent"
        class="text-berry-whiteaux" size="small"
        rounded stacked variant="text"
        @click="$router.push({ path: '/dataset' })"
      >
        <v-icon>mdi-brain</v-icon>
        <span>{{ $t('appNavbar.train') }}</span>
      </v-btn>

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
