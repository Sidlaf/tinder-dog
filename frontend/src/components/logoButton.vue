<!-- <script setup>
defineProps(['text'])
</script>

<template>
    <button>{{ text }}</button>
</template>

<style scoped>
    button{
        margin: 5px 5px 5px 5px;
        line-height: 0px;
        font-family: 'Jost', sans-serif;
        background-color: #ffffff;
        width: 180px;
        height: 180px;
        border-radius: 25px;
        text-align: center;
        vertical-align: middle;
        color: #000000;
        font-size: 30px;
    }
</style> -->

<script>
export default {
  methods: {
    goToAbout() {
      this.$router.push('/')
    }
  }
}
</script>

<template>
  <button class="btn-logo" @click="goToAbout">
    <img class="logo" src="./../assets/logo-icon.jpg" alt="logo" />
  </button>
</template>

<style>
.btn-logo {
  display: contents;
}
.logo {
  margin-left: 10%;
  width: 75px;
  height: 80px;
  border-radius: 9px;
  border: 10px white solid;
}
</style>
