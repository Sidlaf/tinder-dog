<script>
import cardNewDog from './cardNewDog.vue'
import visionBox from './visionBox.vue'
export default {
  components: { cardNewDog, visionBox }
}
</script>

<template>
  <div class="CVBack">
    <cardNewDog></cardNewDog>
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
