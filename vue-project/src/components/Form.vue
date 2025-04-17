<template>
  <section>
    <h1>Cadastro de Ocorrências Urbanas</h1>
    <div class="form-container">
      <form @submit.prevent="handleForm">
        <div class="input-container">
          <label for="category">Categoria</label>
          <select id="category" name="category" v-model="category">
            <option disabled value="">Selecione uma categoria</option>
            <option v-for="(ctg) in categories" :key="ctg.id" :value="ctg.id">
            {{ctg.name}}
            </option>
          </select>
        </div>

        <div class="input-container">
          <label for="date">Data de Registro</label>
          <input type="date" id="date" name="date" v-model="datetime">
        </div>

        <div class="input-container">
          <label for="description">Descrição do Problema</label>
          <textarea id="description" name="description" placeholder="Forneça um resumo da ocorrência." v-model="description"></textarea>
        </div>

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
import { ref, defineProps, defineEmits, onMounted } from "vue";

const categories = ref([])
const category = ref('')
const description = ref('')
const datetime = ref(null)
const success = ref(null)

const props = defineProps({
  lng:Number,
  lat:Number,
})

const emit = defineEmits(['handleSuccess'])

function isSuccess(){
  emit('handleSuccess', success.value)
}

async function handleForm(){
  const body = {
    category: category.value,
    datetime: datetime.value,
    description: description.value,
    geometry: [props.lng,props.lat]
  }
  console.log(body)
  const response = await fetch('http://localhost:5000/occurrence',{
    method: 'POST',
    headers:{
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
    })
  
  if(response.ok) {
    success.value = 'true'
    category.value = ''
    description.value = ''
    datetime.value = null
  }
  else if (!response.ok) success.value = 'false'
  isSuccess()
}

onMounted(async () => {
  const response = await fetch('http://127.0.0.1:5000/category')
  categories.value = await response.json()
})
</script>

<style scoped>
section {
  display: grid;
  gap: 4rem;
  align-content: center;
  width: max-content;
  height: 100vh;
  padding: 0 1.5rem;
  color: #e0e0e0;
  background: linear-gradient(180deg, #121212, #1E1E1E);
  border-left: 3px solid #1DB954;
}

h1 {
  text-decoration: underline 3px #1DB954;
  text-align: center;
  font-size: 1.5rem;
}

form {
  display: grid;
  gap: 2.5rem;
}

.input-container {
  display: grid;
  gap: 0.25rem;
}

label, h2 {
  font-size: 1.2rem;
}

input, textarea, select, p span {
  all: unset;
  padding: 0.6rem;
  font-size: 1rem;
  border: 2px solid #2A2A2A;
  background-color: #181818;
  color: #E0E0E0;
  box-sizing: border-box;
  max-width: 100%;
}

input:hover, input:focus,
textarea:hover, textarea:focus,
select:hover {
  border-color: #1DB954;
}

textarea {
  resize: vertical;
  min-height: 60px;
  max-height: 100px;
  overflow-y: auto;
  word-break: break-word;
}

select {
  appearance: none;
}

.coordinates-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.coordinates {
  display: flex;
  align-items: center;
  font-size: 1.2rem;
}

p span {
  font-style: italic;
  width: 10rem;
}

button {
  padding: 0.5rem;
  font-size: 1rem;
  font-weight: bold;
  color: #014218;
  background-color: #1DB954;
  border: 2px solid transparent;
  cursor: pointer;
}

button:hover {
  background-color: #1ED760;
}
</style>

