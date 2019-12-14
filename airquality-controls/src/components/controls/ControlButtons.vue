<template>
  <div id="control-buttons">
    <button @click.prevent="buttonsView($event)" id="view-compute-controls">View controls</button>
    <div id="compute-control-panel">
      <header>compute control panel</header>
      <div class="compute-control-item">
        <header>Status:</header>
          <div id="update-status">
          {{ }}
          </div>
      </div>
      <div class="compute-control-button">
        <button @click.prevent="filterStartCompute($event)" id="compute-start">Start</button>
      </div>
      <div class="compute-control-button">
        <button @click.prevent="filterStartCompute($event)" id="compute-stop">Stop:</button>
      </div>
      <div class="compute-control-item" id="repeat-select">
        <header>Repeat</header>
        <div>
          <b>Manual</b> --- AUTO
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'control-buttons',
  computed: {
  },
  mounted () {
  },
  data () {
    return {
    }
  },
  methods: {
    buttonsView () {
    },
    filterStartCompute () {
    }
  }
}
</script>

<style>
#control-buttons {
 border: 2px solid red;
}
</style>
