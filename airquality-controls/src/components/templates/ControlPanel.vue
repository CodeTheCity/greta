<template>
  <div id="tempate-controls">
    <div class="control-layout" id="left-controls">
      <map-select></map-select>
    </div>
    <div class="control-layout" id="right-controls">
      <control-buttons></control-buttons>
      <compute-status></compute-status>
    </div>
  </div>
</template>

<script>
  import MapSelect from '@/components/controls/MapSelect.vue'
  import ControlButtons from '@/components/controls/ControlButtons.vue'
  import ComputeStatus from '@/components/controls/ComputeStatus.vue'

  export default {
    name: 'control-panel',
    components: {
      MapSelect,
      ControlButtons,
      ComputeStatus
    },
    props: {
      progressMessage: {
        type: Object
      }
    },
    data () {
      return {
      }
    },
    created () {
    },
    computed: {
    },
    mounted () {
    },
    methods: {
    }
  }
</script>

<style>
#left-controls {

}

#right-controls {

}

.control-layout {
  display: inline-block;
}
</style>
