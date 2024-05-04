<script>
import panelButton from './panelButton.vue'
export default {
  components: { panelButton }
}
</script>

<template>
  <div class="panel">
    <panelButton text="О нас"></panelButton>
    <panelButton text="Премиум"></panelButton>
    <panelButton text="Профиль"></panelButton>
    <panelButton text="Выйти"></panelButton>
  </div>
</template>

<style scoped>
.panel {
  display: flex;
  align-items: center;
  justify-content: right;
  background-color: #b393e6;
  width: 100%;
  height: 60px;
}
</style>
