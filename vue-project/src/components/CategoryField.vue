<template>
  <div class="input-container">
    <label :for="name">{{ name }}</label>
    <select :name="name" id="category" :value="modelValue" @change="$emit('update:modelValue', $event.target.value)">
      <option v-for="(category) in categories" :key="category.id" >{{category.name}}</option>
    </select>
  </div>
</template>

<script setup>
import { defineProps, ref, onMounted } from 'vue';

const categories = ref([])

const props = defineProps({
  name:String,
  modelValue: String
})

onMounted(async () => {
  const response = await fetch('http://127.0.0.1:5000/category')
  
  categories.value = await response.json()
})
</script>

<style scoped>
label{
  font-size: 1.2rem;
}

select {
  padding: 0.6rem;
  border: 2px solid #2A2A2A;
  background-color: #181818;
  color: #E0E0E0;
  font-size: 1rem;
}

select:hover{
  border: 2px solid #1DB954;
}
</style>
