<script>
import cardCard from './cardCard.vue'
import visionBox from './visionBox.vue'
export default {
  components: { cardCard, visionBox }
}
</script>

<template>
  <div class="CVBack">
    <cardCard width="330px" height="480px"></cardCard>
    <visionBox></visionBox>
  </div>
</template>

<style>
.CVBack {
  width: fit-content;
  height: fit-content;
  margin-right: 100px;
}
</style>
