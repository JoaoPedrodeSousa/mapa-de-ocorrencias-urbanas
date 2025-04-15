<script setup>
import Map from "./components/Map.vue";
import Form from "./components/Form.vue";
import Modal from './components/Modal.vue'
</script>

<template>
  <!-- <Map /> -->
   <div class="container">
     <Form />
     <Modal success="false"/>
   </div>
</template>

<style scoped>
.container{
  display: flex;
}
</style>
