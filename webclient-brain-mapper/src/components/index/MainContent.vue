<template>
  <div id="main-content">
    <v-carousel
      hide-delimiters
      show-arrows="hover"
      cycle
      class="carousel w-100"
    >
      <v-carousel-item
        src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
        cover
      ></v-carousel-item>

      <v-carousel-item
        src="https://cdn.vuetifyjs.com/images/cards/hotel.jpg"
        cover
      ></v-carousel-item>

      <v-carousel-item
        src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
        cover
      ></v-carousel-item>
    </v-carousel>
    <div style="height: 500px">
      asdasdasdasd
    </div>
  </div>
</template>

<script>

</script>

<style>
  #main-content {
    height: 100%;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
  }

  .carousel {
    display: block;
    height: 95dvh !important;
  }
</style>
