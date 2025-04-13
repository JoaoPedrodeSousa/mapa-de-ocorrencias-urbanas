<template>
  <section>
    <h1>Cadastro de Ocorrências Urbanas</h1>
    <form>
      <CategoryField />
      <FormField type="text" name="Descrição do Problema" id="descricao" @changeValue="setValue" />
      <FormField type="date" name="Data de Registro" id="data" @changeValue="setValue"/>

      <div class="coordinates">
        <FormField type="text" name="X:" id="X" @changeValue="setValue"/>
        <FormField type="text" name="Y:" id="Y" @changeValue="setValue"/>
      </div>
      <button>ENVIAR</button>
    </form>
  </section>
</template>

<script setup>
import FormField from "./FormField.vue";
import CategoryField from "./CategoryField.vue";
import { ref } from "vue";

const category = ref(null)
const description = ref('')
const date = ref(null)
const x = ref(0)
const y = ref(0)

function setValue({id, value}){
  if (id === 'descricao') {
    description.value = value
  } else if (id === 'data') {
    date.value = value
  } else if (id === 'categoria') {
    category.value = value
  } else if (id === 'X') {
    x.value = value
  } else if (id === 'Y') {
    y.value = value
  }
}

</script>
<style scoped>
h1{
    font-size: 2rem;
}
form{
    display: grid;
    gap: 1rem;
    place-items: start;
}
</style>
