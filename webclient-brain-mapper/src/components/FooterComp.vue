<template>
  <footer class="bg-berry-primary text-white font-bold text-center py-2">
    <p>
      &copy; {{$t('appName')}} {{ new Date().getFullYear() }}
    </p>
  </footer>
</template>

<script>
  export default {
    name: 'FooterComp'
  }
</script>
