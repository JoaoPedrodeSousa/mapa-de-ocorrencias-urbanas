<template>
  <section>
    <h1>Cadastro de Ocorrências Urbanas</h1>
    <div class="form-container">
      <form @submit.prevent="sendForm">
        <CategoryField class="input-container" name="Categoria" v-model="category"/>
        <FormField class="input-container" type="date" name="Data de Registro" id="data" v-model="date"/>
        <FormField class="input-container" type="text" name="Descrição do Problema" id="descricao" v-model="description" />

        <div class="input-container">
          <label>Coordenadas</label>
          <div class="coordinates-container">
            <FormField class="coordinates" type="text" name="X" id="X" v-model="x"/>
            <FormField class="coordinates" type="text" name="Y" id="Y" v-model="y"/>
          </div>
        </div>
        <button>ENVIAR</button>
      </form>
    </div>
  </section>
</template>

<script setup>
import FormField from "./FormField.vue";
import CategoryField from "./CategoryField.vue";
import { ref } from "vue";

const category = ref('')
const description = ref('')
const date = ref(null)
const x = ref(0)
const y = ref(0)

function sendForm(){
  
}
</script>

<style scoped>
section{
  display: grid;
  align-content: center;
  gap: 3rem;
  width: max-content;
  height: 100vh;
  padding: 0 1.2rem;
  color: #e0e0e0;
  background: linear-gradient(180deg, #121212 0%, #1E1E1E 100%);
}

h1{
    font-size: 1.5rem;
    text-decoration:underline 3px #1DB954;
    text-align: center;
}

form{
    display: grid;
    gap: 2.5rem;
}

.input-container{
    display: grid;
    gap: 0.25rem;
}

label{
  font-size: 1.2rem;
}

.coordinates-container{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.coordinates {
  display: flex;
  place-items: center;
}

button{
  background-color: #1DB954;
  color: #121212;
  border: 2px solid transparent; 
  font-weight: bold; 
  font-size: 1rem;
  padding: 0.5rem;
}

button:hover{
  background-color:#1ED760;
}

</style>
