<template>
  <div class="input-container">
    <label :for="name">{{ name }}</label>
    <input :type="type" value="value" :name="name" :id="name" />
  </div>
</template>

<script setup>
import { defineProps } from "vue";

const props = defineProps({
  value: String,
  type: String,
  name: String,
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
