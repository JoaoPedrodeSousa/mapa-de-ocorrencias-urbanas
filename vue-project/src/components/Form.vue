<template>
  <section>
    <h1>Cadastro de Ocorrências Urbanas</h1>
    <div class="form-container">
      <form @submit.prevent="handleForm">
        <FormField class="input-container" type="select" name="Categoria" id="categoria" v-model="category"/>

        <FormField class="input-container" type="date" name="Data de Registro" id="data" v-model="datetime"/>
        <FormField class="input-container" type="textarea" name="Descrição do Problema" id="descricao" v-model="description" />

        <div class="input-container">
          <h2>Coordenadas</h2>
          <div class="coordinates-container">
            <p class="coordinates">Lat:<span>{{lat.toFixed(6)}}</span></p>
            <p class="coordinates">Lng:<span>{{lng.toFixed(6)}}</span></p>
          </div>
        </div>
        <button type="submit">ENVIAR</button>
      </form>
    </div>
  </section>
</template>

<script setup>
import FormField from "./FormField.vue";
import { ref, defineProps, defineEmits } from "vue";

const category = ref('')
const description = ref('')
const datetime = ref(null)

const props = defineProps({
  lng:Number,
  lat:Number,
})

const success = ref(null)
const emit = defineEmits(['handleSubmit'])

function isSuccess(){
  emit('handleSubmit', success.value)
}

async function handleForm(){
  const body = {
    category: category.value,
    datetime: datetime.value,
    description: description.value,
    geometry: [props.lng,props.lat]
  }

  const response = await fetch('http://localhost:5000/occurrence',{
    method: 'POST',
    headers:{
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
    })
  
  if(response.ok) success.value = 'true'
  else if (!response.ok) success.value = 'false'
  isSuccess()
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

h2{
  font-size: 1.2rem;
  font-weight: normal;
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

p{
  display: grid;
  gap: 0.5rem;
  font-size: 1.2rem;
}

p span{
    padding: 0.6rem;
    border: 2px solid #2A2A2A;
    background-color: #181818;
    box-shadow: none;
    box-sizing: border-box;
    font-size: 1rem;
    width: 10rem;
    max-width: 100%;
    font-style: italic;
    color: #E0E0E0;
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
