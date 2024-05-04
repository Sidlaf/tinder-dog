<script>
export default {
  data() {
    return {
      imageUrl: '../assets/image.png'
    }
  }
}
</script>

<template>
  <div class="backCard">
    <div class="card"></div>
  </div>
</template>

<style scoped>
.backCard {
  width: 100%;
  display: flex;
  margin-top: 30px;
  justify-content: center;
  align-items: center;
}
.card {
  background-image: url('../assets/image.png');
  background-size: cover;
  width: 353px;
  height: 514px;
  border-radius: 10px;
}
</style>
