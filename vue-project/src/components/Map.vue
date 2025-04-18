<template>
  <div class="map-container">
    <div id="map"></div>
    <Modal :success='success'/>
    <MapLegend :categories="categories"/>
  </div>
</template>

<script setup>
import { ref, onMounted, defineProps, defineEmits} from "vue";
import "leaflet/dist/leaflet.css";
import * as L from "leaflet";
import Modal from "./Modal.vue";
import MapLegend from "./MapLegend.vue";

const map = ref(null);
const marker = ref(null);
const categoryName = ref('')

const props = defineProps({
  success:Number,
  category:Number,
  categories: Object
})

const wmsOptions = {
  layers: "ocorrencias_wks:limite_do_distrito_federal",
  format: "image/png",
  transparent: true,
  version: "1.1.0",
};

async function getWFS(){
  const URL = "http://localhost:5000/occurrence"
  const response = await fetch(URL)
  const data = await response.json()

  return data
}

const emit = defineEmits(["handleClick"])
function sendCoordinates(lat, lng){
  emit("handleClick", {
    lat:lat,
    lng: lng
  })
}

function createPopupContent(key, value){
  return`<p><strong>${key}: </strong>${value}</p>`
}

function getOccurrences(map, geojson){
  let category_id = 0;

  L.geoJSON(geojson, {
    pointToLayer: function (feature,latlng){
      const properties = feature.properties;
      category_id = properties.category_id;
      const icon =  createIcon(category_id)

      return L.marker(latlng, {icon: icon})
    },
    onEachFeature: function (feature, layer) {
      const properties = feature.properties;
      const lng = feature.geometry.coordinates[0];
      const lat = feature.geometry.coordinates[1];
      categoryName.value = props.categories[category_id - 1].name

      let popup = "";
      popup += createPopupContent('Categoria', categoryName.value)
      popup += createPopupContent('Descrição', properties.description)
      popup += createPopupContent('Data', properties.date)
      popup += createPopupContent('Latitude', lat.toFixed(6))
      popup += createPopupContent('Longitude', lng.toFixed(6))

      layer.bindPopup(popup)
    }
  }).addTo(map)
};

function createIcon(category_id){
  const ICON_URL = category_id ? `/icons/${category_id}.png` : 'location.png'

  const icon = L.icon({
        iconUrl: ICON_URL,
        iconSize: [28, 28],
        iconAnchor: [16, 32],
        popupAnchor: [0, -32]
      });
  return icon
}

function createMarker(latlng) {
  const icon = createIcon(category.value);
  return L.marker(latlng, icon ? { icon } : undefined);
}
function handleCoordinates(event) {
  if (marker.value) {
    map.value.removeLayer(marker.value);
  }

  marker.value = createMarker(event.latlng).addTo(map.value);
  sendCoordinates(event.latlng.lat, event.latlng.lng);
}

onMounted(async () => {
  map.value = L.map("map", {
    center: [-15.7801, -47.7892],
    zoom: 10,
  });

  L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; Contribuidores do <a href="http://osm.org/copyright">OpenStreetMap</a>',
  }).addTo(map.value);

  L.tileLayer
    .wms("http://localhost:8082/geoserver/ocorrencias_wks/wms?", wmsOptions)
    .addTo(map.value);

  const wfs = await getWFS();
  getOccurrences(map.value, wfs)

  map.value.on("click",(e)=> handleCoordinates(e));
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
