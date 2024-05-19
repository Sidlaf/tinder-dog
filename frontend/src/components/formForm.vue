<script>
import fieldWrite from './fieldWrite.vue'
import fieldOpen from './fieldOpen.vue'
import fieldBig from './fieldBig.vue'
export default {
  components: { fieldWrite, fieldOpen, fieldBig }
}
</script>
<template>
  <div class="formBack">
    <form>
      <fieldWrite text="Введите имя" name="Имя"></fieldWrite>
      <div class="miniBtns">
        <fieldWrite text="10" name="Возраст" width="50px"></fieldWrite>
        <fieldOpen
          mini=""
          name="Пол"
          width="74px"
          :items="['М', 'Ж']"
          style="margin-left: 20px"
        ></fieldOpen>
      </div>
      <fieldWrite text="Введите породу" name="Порода"></fieldWrite>
      <fieldOpen mini="Выберите тэг" name="Тэги" :items="['Тег1', 'Тег2', 'Тег3']"></fieldOpen>
      <fieldBig name="Описание"></fieldBig>
    </form>
  </div>
</template>

<style>
.miniBtns {
  display: flex;
  justify-content: left;
}
.formBack {
  background-color: #e2d1fd;
  display: flex;
  justify-content: center;
  width: 330px;
  height: fit-content;
  border-color: black;
  border: 1px solid;
  border-radius: 10px;
}
</style>
