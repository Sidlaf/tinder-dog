<script>
import upperPanel from '@/components/upperPanel.vue'
// import cardCard from '@/components/cardCard.vue'
// import likeButton from '@/components/likeButton.vue'

export default {
  components: { upperPanel
    // , cardCard, likeButton 
  }
}
</script>

<template>
  <div>
    <upperPanel></upperPanel>
    <!-- <cardCard></cardCard>
    <likeButton></likeButton> -->
  </div>
    <router-view> </router-view>

</template>

<style></style>
