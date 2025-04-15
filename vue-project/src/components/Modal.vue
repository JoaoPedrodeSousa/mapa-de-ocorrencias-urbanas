<template>
  <Transition name="fade">
    <div v-if="success === 'true'" class="modal success">
      <div class="image">
        <img src="../assets/check.png" alt="check" />
      </div>
      <p>Ocorrência cadastrada com sucesso!</p>
    </div>
  </Transition>

  <Transition name="fade">
    <div v-if="success === 'false'" class="modal failed">
      <div class="image">
        <img src="../assets/unchecked.png" alt="check" />
      </div>
      <p>Falha no cadastro da ocorrência!</p>
    </div>
  </Transition>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    success:Boolean
})

</script>

<style scoped>
.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.25rem;
  width: 23rem;
  padding: 1rem 0.5rem;
  height: 1rem;
}
.image img {
  height: 1.4rem;        
  display: block;
}
.modal p{
    font-size: 1.4rem;
}
.success{
    color: #014218;
    border: 2px solid #014218;
    background-color: #1DB954;
}
.failed{
    color: #3a0000;
    border: 2px solid #3a0000;
    background-color: #d83333;
}
.fade-enter-active,
.fade-leave-active {
  transition: all 0.4s ease;
}
.fade-enter-from {
  opacity: 0;
  transform: translateY(-10px);
}
.fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

</style>