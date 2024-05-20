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
  <div>
    <upperPanel></upperPanel>
    <backBtn></backBtn>
    <div class="newDBack">
      <cardAndVision></cardAndVision>
      <formForm></formForm>
    </div>
    <div class="btns">
      <button class="btn-delete" @click="deleteForm">Удалить анкету собаки</button>
      <button class="btn-save" @click="saveForm">Сохранить </button>
      <button class="btn-back" @click="backForm">Отмена</button>

    </div>
</div>
</template>

<style>
.newDBack {
  display: flex;
  justify-content: center;
  align-items: center;
}
.btns{
  margin-top: 20px;
  /* display: flex;
  gap: 100px;
  margin-left: 418px; */
}
.btn-delete{
  font-family: 'Jost', sans-serif;
  color: #ffffff;
  background-color: #b393e6;
  width: 294px;
  height: 47px;
  border: none;
  border-radius: 7px;
  font-size: 24px;
  margin-left: 418px;
  margin-right: 138px;
}
.btn-save{
  font-family: 'Jost', sans-serif;
  color: #ffffff;
  background-color: #b393e6;
  height: 47px;
  width: 140px;
  border: none;
  border-radius: 7px;
  font-size: 24px;
  margin-right: 50px;
}
.btn-back{
  font-family: 'Jost', sans-serif;
  color: #ffffff;
  background-color: #85889e;
  height: 47px;
  width: 140px;
  border: none;
  border-radius: 7px;
  font-size: 24px;
}
</style>
