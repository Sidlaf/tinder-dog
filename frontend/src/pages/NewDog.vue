<script>
import upperPanel from '@/components/upperPanel.vue'
import backBtn from '@/components/goBackButton.vue'
import formForm from '@/components/formForm.vue'
import cardAndVision from '../components/cardAndVision.vue'
export default {
  components: { upperPanel, backBtn, formForm, cardAndVision }
}
</script>

<template>
  <div id="app">
    <upperPanel></upperPanel>
    <backBtn></backBtn>
    <div class="newDBack">
      <cardAndVision></cardAndVision>
      <formForm></formForm>
    </div>
  </div>
</template>

<style>
.newDBack {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
