<template>
  <div class="map-container">
    <div id="map"></div>
    <Modal :success='success'/>
  </div>
</template>

<script setup>
import { ref, onMounted, defineProps, defineEmits } from "vue";
import "leaflet/dist/leaflet.css";
import * as L from "leaflet";
import Modal from "./Modal.vue";

const map = ref(null);

const props = defineProps({
    success:String
})

const emit = defineEmits(["handleClick"])
function sendCoordinates(lat, lng){
  emit("handleClick", {
    lat:lat,
    lng: lng
  })
}

const wmsOptions = {
  layers: "limites_df:limites_df",
  format: "image/png",
  transparent: true,
  version: "1.1.0",
};

onMounted(() => {
  map.value = L.map("map", {
    center: [-15.7801, -47.7892],
    zoom: 10,
  });

  L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; Contribuidores do <a href="http://osm.org/copyright">OpenStreetMap</a>',
  }).addTo(map.value);

  const limite_df = L.tileLayer
    .wms("http://localhost:8082/geoserver/limites_df/wms?", wmsOptions)
    .addTo(map.value);

  const wms = {
    "Limite DF": limite_df,
  };

  L.control.layers(null, wms).addTo(map.value);

  map.value.on("click", function (e) {
    sendCoordinates(e.latlng.lat, e.latlng.lng)
  });
});
</script>

<style scoped>
.map-container{
  position: relative;
}

#map {
  height: 100vh;
  z-index: 1;
  cursor:crosshair;
}
</style>
