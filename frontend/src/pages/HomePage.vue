<script>
import upperPanelPre from '@/components/upperPanelPre.vue'
import gavLogo from '@/components/gavLogo.vue'
import signInWindow from '../components/signInWindow.vue'
import logInWindow from '../components/logInWindow.vue'
export default {
  components: { upperPanelPre, gavLogo, signInWindow, logInWindow }
}
</script>

<template>
  <signInWindow></signInWindow>
  <logInWindow></logInWindow>
  <div class="homePage-div">
    <upperPanelPre></upperPanelPre>
    <div class="homePage-div2">
      <gavLogo></gavLogo>
      <button class="homePage-create" @click="createAcc">Создать аккаунт</button>
    </div>
  </div>
</template>

<style>
.homePage-div {
  background-image: url(./../assets/fon.png);
  background-size: 100%;
  height: 56vw;
  width: 100vw;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.homePage-create {
  font-family: 'Jost', sans-serif;
  color: #ffffff;
  background-color: #b393e6;
  width: 445px;
  height: 97px;
  border: none;
  border-radius: 30px;
  font-size: 48px;
}
.homePage-div2 {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 96px;
  margin-top: 48px;
}
</style>
