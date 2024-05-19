<script>
import upperPanel from '@/components/upperPanel.vue'
import backBtn from '@/components/goBackButton.vue'
import formForm from '@/components/formForm.vue'
import cardAndVision from '../components/cardAndVision.vue'
import addDogButton from '@/components/addDogButton.vue'
export default {
  components: { upperPanel, backBtn, formForm, cardAndVision, addDogButton }
}
</script>

<template>
  <div>
    <upperPanel></upperPanel>
    <backBtn></backBtn>
    <div class="newDBack">
      <cardAndVision></cardAndVision>
      <formForm></formForm>
    </div>
    <addDogButton></addDogButton>
  </div>
</template>

<style>
.newDBack {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
