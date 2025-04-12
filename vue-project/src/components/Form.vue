<template>
  <section>
    <h1>Cadastro de Ocorrências Urbanas</h1>
    <form>
      <CategoryField />
      <FormField type="text" name="Descrição do Problema" />
      <FormField type="date" name="Data de Registro" />

      <div class="coordinates">
        <FormField type="text" name="X:" />
        <FormField type="text" name="Y:" />
      </div>

      <button>ENVIAR</button>
    </form>
  </section>
</template>

<script setup>
import FormField from "./FormField.vue";
import CategoryField from "./CategoryField.vue";
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
