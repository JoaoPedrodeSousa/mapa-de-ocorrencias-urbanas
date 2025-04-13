<template>
  <section>
    <h1>Cadastro de Ocorrências Urbanas</h1>
    <form>
      <CategoryField />
      <FormField type="text" name="Descrição do Problema" id="descricao"/>
      <FormField type="date" name="Data de Registro" id="data" />

      <div class="coordinates">
        <FormField type="text" name="X:" id="X"/>
        <FormField type="text" name="Y:" id="Y"/>
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
