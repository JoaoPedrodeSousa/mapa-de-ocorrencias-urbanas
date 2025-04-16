<template>
  <div>
    <label :for="id">{{ name }}</label>
    <input v-if="type === 'text' || type === 'date'" 
      :type="type" 
      :name="name" 
      :id="id" 
      :value="modelValue"  
      @input="$emit('update:modelValue', $event.target.value)"
    />

    <select v-else-if="type === 'select'" 
      :name="name" 
      id="category" 
      :value="modelValue" 
      @change="$emit('update:modelValue', $event.target.value)">

      <option v-for="(category) in categories" :key="category.id" :value="category.id">
        {{category.name}}
      </option>

    </select>

    <textarea v-else :name="name" :id="id" :value="modelValue" @input="$emit('update:modelValue', $event.target.value)" placeholder="Forneça um resumo da ocorrência."></textarea>
  </div>
</template>

<script setup>
import { defineProps, ref, onMounted } from 'vue';

const categories = ref([])

const props = defineProps({
  type: String,
  name: String,
  id: String,
  modelValue: [String, Number]
});

onMounted(async () => {
  const response = await fetch('http://127.0.0.1:5000/category')
  categories.value = await response.json()
})
</script>

<style scoped>
label{
  font-size: 1.2rem;
}
input, textarea{
  all: unset;
}
textarea{
  resize: vertical;
  overflow: hidden;
  overflow-y:scroll;
  overflow-wrap: break-word;
  min-height: 60px;
  max-height: 100px;
}

input,textarea{
    padding: 0.6rem;
    font-size: 1rem;
    border: 2px solid #2A2A2A;
    background-color: #181818;
    color: #E0E0E0;
    box-shadow: none;
    box-sizing: border-box;
    max-width: 100%;
}

input:hover, input:focus,
textarea:hover, textarea:focus{
  border: 2px solid #1DB954;
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