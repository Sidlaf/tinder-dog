<script setup>
defineProps(['text'])
</script>

<template>
  <button>{{ text }}</button>
</template>

<style scoped>
button {
  width: 170px;
  height: 50px;
  margin: 7.5px 20px 7.5px;
  line-height: 0px;
  font-family: 'Jost', sans-serif;
  background-color: #ffffff;
  border-radius: 18px;
  border: none;
  text-align: center;
  vertical-align: middle;
  color: #000000;
  font-size: 24px;
}
</style>
