<template>
  <v-app-bar
    color="primary-darken-1"
    :absolute="false"
    style="position: fixed;"
  >
    <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

    <v-app-bar-title>{{ $t('appNavbar.title') }}</v-app-bar-title>

    <v-spacer></v-spacer>

    <template v-if="$vuetify.display.mdAndUp">
      <v-btn
        variant="text"
        class="mr-3 text-none"
      >
        {{ $t('appNavbar.signIn') }}
      </v-btn>

      <v-btn
        variant="outlined"
        class="text-none mr-5"
      >
        {{ $t('appNavbar.signUp') }}
      </v-btn>
    </template>

    <v-btn icon="mdi-cog-outline" variant="text"></v-btn>
  </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      :location="$vuetify.display.mobile ? 'bottom' : undefined"
      temporary
    >
      <v-list
        :items="items"
      ></v-list>
    </v-navigation-drawer>
</template>

<script>
export default {
  data: () => ({
    drawer: false,
    group: null,
    items: [
      {
        title: 'Foo',
        value: 'foo',
      },
      {
        title: 'Bar',
        value: 'bar',
      },
      {
        title: 'Fizz',
        value: 'fizz',
      },
      {
        title: 'Buzz',
        value: 'buzz',
      },
    ],
  }),

  watch: {
    group () {
      this.drawer = false
    },
  },
}
</script>