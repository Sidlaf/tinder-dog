<script>
import filterCard from './filterCard.vue'
import cardCard from './cardCard.vue'
export default {
  components: { filterCard, cardCard }
}
</script>

<template>
  <div class="backCard">
    <filterCard></filterCard>
    <cardCard></cardCard>
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
</style>
