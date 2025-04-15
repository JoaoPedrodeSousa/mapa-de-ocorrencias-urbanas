<script setup>
import Map from "./components/Map.vue";
import Form from "./components/Form.vue";
</script>

<template>
  <div class="container">
    <Map />
    <Form />
  </div>
</template>

<style scoped>
.container{
  display: grid;
  grid-template-columns: 1fr auto;
  position: relative;
}
</style>
