<template>
  <div class="input-container">
    <label :for="id">{{ name }}</label>
    <input :type="type" :name="name" :id="id" :value="value"/>
  </div>
</template>

<script setup>
import { defineProps } from "vue";

const props = defineProps({
  type: String,
  name: String,
  id: String,
  value:String
});
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
