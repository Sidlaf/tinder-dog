<script setup>
defineProps(['text'])
</script>

<template>
  <button>{{ text }}</button>
</template>

<style scoped>
button {
  margin: 7.5px 20px 7.5px;
  line-height: 0px;
  font-family: 'Jost', sans-serif;
  background-color: #ffffff;
  width: 130px;
  height: 45px;
  border-radius: 25px;
  text-align: center;
  vertical-align: middle;
  color: #000000;
  font-size: 24px;
}
</style>
