<script>
import inputField from './inputField.vue'
import passwordField from './passwordField.vue'
export default {
  components: { inputField, passwordField },
  directives: {
    clickOutside: {
      mounted: function (element, binding) {
        element.clickOutsideEvent = function (event) {
          const excludeComponent = document.getElementById(binding.arg)

          if (
            !(element == event.target || element.contains(event.target)) &&
            !(
              excludeComponent &&
              (event.target == excludeComponent || excludeComponent.contains(event.target))
            )
          ) {
            binding.value(event, element)
          }
        }
        document.addEventListener('mouseup', element.clickOutsideEvent)
      },
      unmounted: function (element) {
        document.removeEventListener('mouseup', element.clickOutsideEvent)
      }
    }
  },
  methods: {
    clickOutside: () => {
      // TODO: router или закрытие окна
      document.location.href = '/homepage'
    },
    signIn() {
      // TODO: прописать функцию signIn
    }
  }
}
</script>

<template>
  <div class="signIn-back">
    <div class="signIn-front" v-click-outside="clickOutside">
      <img
        src=".././assets/logo.svg"
        alt="logo"
        style="width: 76px; height: 72px; margin-top: 21px"
      />
      <inputField text="email@example.com" name="Email"></inputField>
      <passwordField text="" name="Пароль"></passwordField>
      <passwordField text="" name="Повторите пароль"></passwordField>
      <button class="signIn-create" @click="signIn">Создать аккаунт</button>
    </div>
  </div>
</template>

<style>
.signIn-back {
  width: 100vw;
  height: 56vw;
  display: flex;
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
