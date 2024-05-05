<script>
import filterCard from './filterCard.vue'
export default {
  components: { filterCard }
}
</script>

<template>
  <div class="backCard">
    <filterCard></filterCard>
    <div class="card"></div>
    <filterCard style="visibility: hidden"></filterCard>
  </div>
</template>

<style scoped>
.backCard {
  width: 100%;
  display: flex;
  margin-top: 30px;
  justify-content: space-between;
  /* align-items: center; */
}
.card {
  background-image: url('../assets/image.png');
  background-size: cover;
  width: 353px;
  height: 514px;
  border-radius: 10px;
}
</style>
