<template>
  <div id="map"></div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import "leaflet/dist/leaflet.css";
import * as L from "leaflet";

const map = ref(null);

const wmsOptions = {
  layers: "limites_df:limites_df",
  format: "image/png",
  transparent: true,
  version: "1.1.0",
};

onMounted(() => {
  map.value = L.map("map", {
    center: [-15.7801, -47.7292],
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

  // map.value.on("click", function (e) {
  // }); // -----> definir evento de click
});
</script>

<style scoped>
#map {
  height: 90vh;
}
</style>
