<template>
  <div class="input-container">
    <label :for="id">{{ name }}</label>
    <input :type="type" :name="name" :id="id" v-model="value"  @input="handleInput"/>
  </div>
</template>

<script setup>
import { ref, defineProps } from "vue";

const value = ref(null)

const props = defineProps({
  type: String,
  name: String,
  id: String,
  src:String
});
</script>

<style scoped>
label{
  font-size: 1.2rem;
}

input{
    all: unset;
    padding: 0.6rem;
    font-size: 1rem;
    border: 2px solid #2A2A2A;
    background-color: #181818;
    color: #E0E0E0;
    box-shadow: none;
    box-sizing: border-box;
}

input:hover, input:focus{
  border: 2px solid #1DB954;
}

</style>

<!-- Botões:

    Fundo: #1DB954

    Texto: #121212

    Hover: #1ED760

Inputs e campos:

    Fundo: #181818

    Borda: #2A2A2A

    Texto: #E0E0E0

Links:

    Normal: #1DB954

    Hover: #1ED760

Background geral:

    Gradiente opcional: linear-gradient(180deg, #121212 0%, #1E1E1E 100%) -->