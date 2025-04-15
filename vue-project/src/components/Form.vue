<template>
  <section>
    <h1>Cadastro de Ocorrências Urbanas</h1>
    <div class="form-container">
      <form @submit.prevent="sendForm">
        <FormField class="input-container" type="select" name="Categoria" id="categoria" v-model="category"/>

        <FormField class="input-container" type="date" name="Data de Registro" id="data" v-model="date"/>
        <FormField class="input-container" type="textarea" name="Descrição do Problema" id="descricao" v-model="description" />
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
  gap: 4rem;
  align-content: center;
  width: max-content;
  height: 100vh;
  padding: 0 1.5rem;
  color: #e0e0e0;
  background: linear-gradient(180deg, #121212 0%, #1E1E1E 100%);
  border-left: 3px solid #1DB954;
}

h1{
  text-decoration:underline 3px #1DB954;
  text-align: center;
  font-size: 1.5rem;
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
  border: 2px solid transparent; 
  padding: 0.5rem;
  font-size: 1rem;
  font-weight: bold;
  color: #014218;
  background-color: #1DB954;
}

button:hover{
  background-color:#1ED760;
}

</style>
