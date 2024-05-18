<script>
import upperPanel from '@/components/upperPanel.vue'
import card from '@/components/cardFeed.vue'
import likeButton from '@/components/likeButton.vue'
export default {
  components: { upperPanel, card, likeButton }
}
</script>

<template>
  <div id="app">
    <upperPanel></upperPanel>
    <card></card>
    <likeButton></likeButton>
  </div>
</template>

<style></style>
