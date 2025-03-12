<template>
  <div class="main-container">
    <div>
      <img src="../assets/under-maintenance.png" alt="img">
    </div>
    <div>
      <h2>{{ $t('err5xx.title') }}</h2>
      <p>{{ $t('err5xx.text') }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Err5xx'
};
</script>

<style>
.main-container {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>

