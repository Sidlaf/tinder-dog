<script>
import panelButton from './panelButton.vue'
import logoButton from './logoButton.vue'
export default {
  components: { panelButton, logoButton },
  methods: {
    goAboutUs() {
      this.$router.push('/aboutus')
    },
    goProfile() {
      this.$router.push('/NewProfile')
    },
    goPremium() {
      this.$router.push('/PremiumPage')
    },
    goIn() {
      this.$router.push('/LogIn')
    }
  }
}
</script>

<template>
  <div class="upperPanelPre-panel">
    <logoButton class="logo"></logoButton>
    <div class="upperPanelPre-btns">
      <panelButton text="О нас" @click="goAboutUs"></panelButton>
      <panelButton text="Премиум" @click="goPremium"></panelButton>
      <panelButton text="Войти" @click="goIn"></panelButton>
    </div>
  </div>
</template>

<style scoped>
.upperPanelPre-panel {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #b393e6;
  width: 100%;
  height: 100px;
}

.upperPanelPre-btns {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-right: 50px;
}
</style>
