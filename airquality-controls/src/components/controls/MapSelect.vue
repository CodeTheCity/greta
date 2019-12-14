<template>
  <div id="map-select">
    <div class="map-box">
      <h3>Simple map</h3>
      <p>First marker is placed at {{ withPopup.lat }}, {{ withPopup.lng }}</p>
      <p>Center is at {{ currentCenter }} and the zoom is: {{ currentZoom }}</p>
      <button @click="showLongText">Toggle long popup</button>
      <button @click="showMap = !showMap">Toggle map</button>
    </div>
    <l-map :zoom="zoom" :center="center" style="height: 90%">
      <l-tile-layer :url="url" :attribution="attribution" />
    </l-map>
  </div>
</template>

<script>
import { LMap, LTileLayer } from "vue2-leaflet"
import { latLng } from "leaflet"

  export default {
    name: 'map-select',
    components: {
      LMap,
      LTileLayer
    },
    props: {
      progressMessage: {
        type: Object
      }
    },
    data () {
      return {
        zoom: 13,
        center: latLng(57.14, -2.09),
        url: "http://{s}.tile.osm.org/{z}/{x}/{y}.png",
        attribution:
          '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        marker: latLng(47.41322, -1.219482),
        text: "my marker popup text",
        title: "My marker popup title"
        }
    },
    created () {
    },
    computed: {
    },
    mounted () {
    },
    methods: {
      zoomUpdate(zoom) {
        this.currentZoom = zoom;
      },
      centerUpdate(center) {
        this.currentCenter = center;
      },
      showLongText() {
        this.showParagraph = !this.showParagraph;
      },
      innerClick() {
        alert("Click!");
      }
    }
  }
</script>

<style>
  @import 'https://unpkg.com/leaflet@1.2.0/dist/leaflet.css'

#map-select {
  display: block;
  border: 2px solid blue;
}

.map-box {
  border: 2px solid green;
  height: 800px;
  width: 800px;
}
</style>
