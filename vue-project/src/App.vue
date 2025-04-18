<template>
  <div class="container">
    <Map @handleClick="updateLatLng" :success="success" :category = "category" :categories="categories"/>
    <Form @handleSuccess="updateSuccess" :lng="longitude" :lat="latitude" :categories="categories"/>
  </div>
</template>

<script setup>
import Map from "./components/Map.vue";
import Form from "./components/Form.vue";
import { ref, onMounted } from "vue";

const latitude = ref(0)
const longitude = ref(0)
const success = ref(null)
const categories = ref([])
const category = ref(3)

function updateSuccess(value){
  success.value = value
}

function updateLatLng(coordinates){
  latitude.value = coordinates.lat
  longitude.value = coordinates.lng
}

onMounted(async () => {
  const response = await fetch('http://127.0.0.1:5000/category')
  categories.value = await response.json()
})

</script>

<style scoped>
.container{
  display: grid;
  grid-template-columns: 1fr auto;
  position: relative;
}
</style>
