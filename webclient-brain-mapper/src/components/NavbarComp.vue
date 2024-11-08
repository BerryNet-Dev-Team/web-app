<template>
  <nav class="bg-brain-primary-dark text-white flex items-center justify-between px-8 py-5">
    <div class="flex items-center justify-around gap-4">
      <img src="/src/assets/LogoTemp.png" alt="Icono" class="h-16 max-h-16"/>
      <v-btn variant="text">{{ $t('navbar.start') }}</v-btn>
      <v-btn color="orange-darken-4" @click="ToCreate">{{ $t('navbar.create') }}</v-btn>
    </div>
    <div class="flex items-center justify-between">
      <v-menu>
        <template v-slot:activator="{ props }">
          <v-btn
            color="#8AC6D0"
            v-bind="props"
          >
            {{ $t('navbar.profile') }}
          </v-btn>
        </template>
        <v-list bg-color="#8AC6D0">
          <v-list-item>
            <v-btn variant="text" @click="ToProfile">{{ $t('navbar.viewProfile') }}</v-btn>
          </v-list-item>
          <v-divider></v-divider>
          <v-list-item>
            <v-btn variant="text">{{ $t('navbar.logOut') }}</v-btn>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>
  </nav>
</template>

<script>
  export default {
    name: 'NavbarComp',
    methods:{
      ToCreate(){
        this.$router.push('/create');
      },
      ToProfile(){
        this.$router.push('/profile');
      }
    }
  }
</script>
