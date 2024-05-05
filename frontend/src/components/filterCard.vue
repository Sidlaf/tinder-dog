<script setup>
import { ref } from 'vue'
const picked = ref('male')
const selected = ref('')
</script>

<template>
  <div class="filter">
    <div class="pF">
      <u>Фильтр</u>
    </div>
    <div class="gender">
      <p><u>Пол</u></p>
      <div style="margin-left: 10px">
        <input type="radio" id="male" value="male" v-model="picked" />
        <label for="male">Мужской</label>
      </div>
      <div style="margin-left: 10px">
        <input type="radio" id="female" value="female" v-model="picked" />
        <label for="female">Женский</label>
      </div>
    </div>
    <div class="region">
      <p><u>Регион</u></p>
      <select v-model="selected" style="margin-left: 10px">
        <option disabled value="">Выберите город</option>
        <option>Город A</option>
        <option>Город B</option>
        <option>Город C</option>
      </select>
    </div>
  </div>
</template>

<style>
.filter {
  margin-left: 15px;
  width: 200px;
  height: 180px;
  float: left;
  border: 2px solid;
  border-color: black;
  border-radius: 5%;
}
.gender {
  height: 75px;
  margin-left: 15px;
}
.region {
  height: 70px;
  margin-left: 15px;
}
.pF {
  height: 40px;
  font-size: 20px;
  font-weight: bold;
  margin-left: 15px;
}
</style>
