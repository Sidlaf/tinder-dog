<script>
import panelButton from './panelButton.vue'
import logoButton from './logoButton.vue'
export default {
  components: { panelButton, logoButton }
}
</script>

<template>
<div class="panel">
    <logoButton class="logo"></logoButton>
    <div class="btns">
      <panelButton text="О нас"></panelButton>
      <panelButton text="Премиум"></panelButton>
      <panelButton text="Профиль"></panelButton>
      <panelButton text="Выйти"></panelButton>
    </div>
  </div>
</template>

<style scoped>
.panel {
  background-color: #b393e6;
  width: 100%;
  height: 100px;
}

.btns{
  display: flex;
  width: 900px;
  align-items: end;
  justify-content: space-between;
  margin-top: -80px;
  margin-left: 700px;
  padding-right: 50px;


}
</style>
