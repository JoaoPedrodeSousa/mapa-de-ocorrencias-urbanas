<template>
  <select :name="name" id="category">
    <option v-for="(category) in categories" :key="category.id" :value="category.name">{{ category.name }}</option>
  </select>
</template>

<script setup>
import { defineProps, ref, onMounted } from 'vue';

const withinData = ref(true)
const categories = ref([])

const props = defineProps({
  name:String
})

onMounted(async () => {
  const response = await fetch('http://127.0.0.1:5000/category')

  if (!response.ok){
    withinData.value = false
    throw new Error('Erro na requisição')
  }
  categories.value = await response.json()
  console.log(categories.value)
})

</script>
<style scoped></style>
