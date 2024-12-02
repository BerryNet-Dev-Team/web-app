<template>
  <MainContent />
</template>

<script>
import MainContent from '@/components/index/MainContent.vue';

export default {
  components: {
    MainContent,
  }
};
</script>
<route lang="json">
  {
    "meta": {
      "layout": "public",
      "requiresAuth": false
    }
  }
</route>