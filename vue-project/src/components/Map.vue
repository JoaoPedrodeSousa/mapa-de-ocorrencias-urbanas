<template>
  <div id="map"></div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import "leaflet/dist/leaflet.css";
import * as L from "leaflet";
import "proj4leaflet";

const map = ref(null);

const wmsOptions = {
  layers: "limites_df:limites_df",
  format: "image/png",
  transparent: true,
  version: "1.1.0",
};

onMounted(() => {
  map.value = L.map("map", {
    center: [-15.7801, -47.9292],
    zoom: 12,
  });

  L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; Contribuidores do <a href="http://osm.org/copyright">OpenStreetMap</a>',
  }).addTo(map.value);
  L.tileLayer
    .wms("http://localhost:8082/geoserver/limites_df/wms?", wmsOptions)
    .addTo(map.value);
});
</script>

<style scoped>
#map {
  height: 90vh;
}
</style>
