<script>
import panelButton from './panelButton.vue'
import logoButton from './logoButton.vue'
export default {
  components: { panelButton, logoButton },
  methods: {
    goAboutUs(){
      this.$router.push('/aboutus')
    },
    goProfile(){
      this.$router.push('/NewProfile')
    },
    goPremium(){
      this.$router.push('/PremiumPage')

    }
  }
}
</script>

<template>
  <div class="panel">
    <logoButton class="logo"></logoButton>
    <div class="btns">
      <panelButton text="О нас" @click="goAboutUs"></panelButton>
      <panelButton text="Премиум" @click="goPremium"></panelButton>
      <panelButton text="Профиль" @click="goProfile"></panelButton>
      <panelButton text="Выйти" @click="goExit"></panelButton>
    </div>
  </div>
</template>

<style scoped>
.panel {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #b393e6;
  width: 100%;
  height: 100px;
}

.btns {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-right: 50px;
}
</style>
