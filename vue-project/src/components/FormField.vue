<template>
  <div class="input-container">
    <label :for="id">{{ name }}</label>
    <input :type="type" :name="name" :id="id" v-model="value" @input="handleInput"/>
  </div>
</template>

<script setup>
import { ref, defineProps, defineEmits } from "vue";

const value = ref(null)

const props = defineProps({
  type: String,
  name: String,
  id: String
});

const emit = defineEmits(["changeValue"]);

function handleInput(){
  emit("changeValue", {
    id: props.id,
    value: value.value
  })
}

</script>

<style scoped>
.input-container{
    display: grid;
    gap: 0.5rem;
}

input{
    all: unset;
    padding: 0.5rem;
    font-size: 1.2rem;
    border: 2px solid black;
    border-radius: 5px;
    box-shadow: none;
    box-sizing: border-box;
}

</style>
