<template>
  <div class="main-container">
    <div>
      <img src="../assets/under-maintenance.png" alt="img">
    </div>
    <div>
      <h2 class="text-4xl mb-5">{{ $t('err5xx.title') }}</h2>
      <p>{{ $t('err5xx.text') }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Err5xx'
};
</script>

<route lang="json">
  {
    "meta": {
      "layout": "error",
      "requiresAuth": false
    }
  }
</route>

<style>
.main-container {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
