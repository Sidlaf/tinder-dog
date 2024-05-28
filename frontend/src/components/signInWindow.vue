<script>
import inputField from './inputField.vue'
export default {
  components: { inputField }
}
</script>

<template>
  <div class="signIn-back">
    <div class="signIn-front">
      <img
        src=".././assets/logo.svg"
        alt="logo"
        style="width: 76px; height: 72px; margin-top: 21px"
      />
      <inputField text="email@example.com" name="Email"></inputField>
      <inputField text="example" name="Пароль"></inputField>
      <inputField text="example" name="Повторите пароль"></inputField>
      <button class="signIn-create" @click="createAcc">Создать аккаунт</button>
    </div>
  </div>
</template>

<style>
.signIn-back {
  width: 100vw;
  height: 56vw;
  display: none;
  align-items: center;
  justify-content: center;
  background-color: rgba(0, 0, 0, 0.15);
  z-index: 1000;
  position: absolute;
  top: o;
  flex-direction: column;
  backdrop-filter: blur(1px);
}
.signIn-front {
  background-color: white;
  border: 1px solid black;
  border-radius: 10px;
  width: 360px;
  height: auto;
  display: flex;
  align-items: center;
  justify-content: top;
  flex-direction: column;
}
.signIn-create {
  font-family: 'Jost', sans-serif;
  color: #ffffff;
  background-color: #b393e6;
  width: 271px;
  height: 40px;
  border: none;
  border-radius: 10px;
  font-size: 24px;
  font-weight: 600;
  margin-top: 20px;
  margin-bottom: 40px;
}
</style>
