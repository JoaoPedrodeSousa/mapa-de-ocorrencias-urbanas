<template>
  <div class="container">
    <Map @handleClick="updateLatLng" :success="success" :category = "category"/>
    <Form @handleSuccess="updateSuccess" @handleCategory="updateCategory"  :lng="longitude" :lat="latitude"/>
  </div>
</template>

<script setup>
import Map from "./components/Map.vue";
import Form from "./components/Form.vue";
import { ref } from "vue";

const latitude = ref(0)
const longitude = ref(0)
const success = ref('')
const category = ref(null)

function updateSuccess(value){
  success.value = value
}

function updateCategory(value){
  category.value = value
}

function updateLatLng(coordinates){
  latitude.value = coordinates.lat
  longitude.value = coordinates.lng
}

</script>

<style scoped>
.container{
  display: grid;
  grid-template-columns: 1fr auto;
  position: relative;
}
</style>
