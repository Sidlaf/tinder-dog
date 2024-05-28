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
