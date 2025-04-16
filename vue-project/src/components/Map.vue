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

const wmsOptions = {
  layers: "limites_df:limites_df",
  format: "image/png",
  transparent: true,
  version: "1.1.0",
};

async function getWFS(){
  const URL = "http://localhost:5000/wfs/occurrence"
  const response = await fetch(URL)
  const data = await response.json()

  return await data
}

const map = ref(null);
const marker = ref(null);

const props = defineProps({
    success:String,
    category:String
})

const emit = defineEmits(["handleClick"])
function sendCoordinates(lat, lng){
  emit("handleClick", {
    lat:lat,
    lng: lng
  })
}

function makeIcon(category_id){
  const icon = L.icon({
        iconUrl: '/icons/' + category_id + '.png',
        iconSize: [28, 28],
        iconAnchor: [16, 32],
        popupAnchor: [0, -32]
      });
  return icon
}

function getOccurrences(map, geojson){
  L.geoJSON(geojson, {
    pointToLayer: function (feature,latlng){
      const properties = feature.properties;
      const category_id = properties.categoria_id;
      
      const icon =  makeIcon(category_id)

      return L.marker(latlng, {icon: icon})
    },
    onEachFeature: function (feature, layer) {
      const properties = feature.properties;
      const lng = feature.geometry.coordinates[0];
      const lat = feature.geometry.coordinates[1];

      let popup = "";
      for (const propertie in properties){
        if (propertie === 'id' || propertie === 'categoria_id') continue;
        const newPropertie = propertie[0].toUpperCase() + propertie.substring(1)

        popup += `<p><strong>${newPropertie.replace("_"," ")}:</strong> ${feature.properties[propertie]}</p>`
      }
      popup += `<p><strong>Latitude:</strong> ${lat}</p>`
      popup += `<p><strong>Longitude:</strong> ${lng}</p>`

      layer.bindPopup(popup)
    }
  }).addTo(map)
};

onMounted(async () => {
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

  const wfs = await getWFS();
  getOccurrences(map.value, wfs)

  const wms = {
    "Limite DF": limite_df,
  };

  L.control.layers(null, wms).addTo(map.value);

  map.value.on("click",function (e) {
    if(marker.value){
      map.value.removeLayer(marker.value)
    }
    if (category.value){
      const icon = makeIcon(category.value)
      marker.value = L.marker(e.latlng,{icon:icon}).addTo(map.value)
    } else{
      marker.value = L.marker(e.latlng).addTo(map.value)
    }

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
