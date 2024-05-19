<script>
export default {
  name: 'cardCard',
  props: {
    width: {
      type: String,
      required: false
    },
    height: {
      type: String,
      required: false
    }
  },
  computed: {
    selectStyle() {
      if (this.width == null && this.height == null) {
        return ''
      }
      return 'width: ' + this.width + '; ' + 'height: ' + this.height
    }
  }
}
</script>

<template>
  <div class="card" :style="selectStyle"></div>
</template>

<style>
.card {
  background-image: url('../assets/image.png');
  background-size: cover;
  width: 353px;
  height: 514px;
  border-radius: 10px;
}
</style>
