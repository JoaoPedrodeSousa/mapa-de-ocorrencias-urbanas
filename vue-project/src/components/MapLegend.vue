<template>
    <div class="modal">
        <button v-if="!showModal" @click="showModal = !showModal" class="legend-image">
            <div class="image ">
                <img src="../../public/layers.png" alt="">
            </div>
        </button>
        
        <button class="legend-button" v-else-if="showModal" @click="showModal = !showModal">
           FECHAR LEGENDA
        </button>

        <div v-if="showModal" class="legend-item" v-for="(ctg, key) in props.categories" :key="key">
            <div class="image">
                <img :src="getIcon(ctg.id)" :alt="ctg.name" />
            </div>
            <p>{{ ctg.name }}</p>
        </div>
    </div>
</template>

<script setup>
import { ref, defineProps } from 'vue'

const showModal = ref(false)
const props = defineProps({
    categories: Object
})
const getIcon = (id) => {
    return `../../public/icons/${id}.png`
}
</script>

<style scoped>
button {
    padding: 0.5rem 1rem;
    color: white;
    border: none;
    cursor: pointer;
}
.legend-button{
    padding: 1rem;
    color:#014218;
    font-size: 0.75rem;
    font-weight: bold;
    background-color: #1DB954;
}
.legend-button:hover{
  background-color: #1ED760;
}
.legend-image{
    background-color: #1DB954;
}
.modal {
    display: flex;
    flex-direction: column;
    width: max-content;
    background-color: white;
    border: 2px solid #111;
    border-radius: 5px;
    position: absolute;
    top: 0.5rem;
    right: 0.5rem;
    z-index: 2;
}
.legend-item{
    display: flex;
    flex-direction: row;
    gap: 0.75rem;
    place-items: center;
    border-bottom: 2px solid #1DB954;
    padding: 0.15rem;
    margin: 0.25rem 1rem;
}
.image img {
    height: 1.7rem;        
    display: block;
}
.modal p{
    font-size: 1.2rem;
}
</style>