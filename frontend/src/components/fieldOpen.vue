<script setup>
import { ref } from 'vue'
const selected = ref('')
</script>

<script>
export default {
  name: 'fieldOpen',
  props: {
    name: {
      type: String,
      required: true
    },
    items: {
      type: Array,
      required: true
    },
    width: {
      type: String,
      required: false
    },
    mini: {
      type: String,
      required: true
    }
  },
  computed: {
    selectStyle() {
      if (this.width == null) {
        return ''
      }
      return 'width: ' + this.width
    }
  }
}
</script>

<template>
  <div>
    <p style="margin-top: 12px; margin-bottom: 5px">{{ name }}</p>
    <div class="fieldBack">
      <select class="asdf" v-model="selected" :style="selectStyle">
        <option value="" disabled selected hidden>{{ mini }}</option>
        <option v-bind:key="item" v-for="item in items">{{ item }}</option>
      </select>
    </div>
  </div>
</template>

<style>
.asdf {
  width: 304px;
  height: 40px;
  border-width: 0px;
  background-color: white;

  font-weight: bold;
}
</style>
