<script setup>
import { ref } from 'vue'

const likeClass = ref('likew')
</script>

<script>
import upperPanel from '../../components/upperPanel.vue';

export default {
  components: {upperPanel},
  data(){
    return{
      like: '♥︎',
      skip: 'X',
      status: ''
    }
  },
  methods: {
    swipeRight(){
      this.status = 'Карточка свайпнута вправо'
    },
    swipeLeft(){
      this.status = 'Карточка свайпнута влево'
    }
  }
}
</script>

<template>
  <upperPanel></upperPanel>
  <p>{{ status }}</p>
  <button type="button" @click="swipeLeft">{{ skip }}</button>
  <button type="button" @click="swipeRight" :class="likeClass">{{ like }}</button>
</template>

<style>
.likew{
  color: red;
}
</style>