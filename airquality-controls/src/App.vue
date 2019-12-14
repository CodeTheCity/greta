<template>
  <div id="app">
    AIR QUALITY CONTROLS
    <control-panel></control-panel>
  </div>

</template>

<script>
  import ControlPanel from '@/components/templates/ControlPanel.vue'

  export default {
    name: 'app',
    components: {
      ControlPanel
    }
  }
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
