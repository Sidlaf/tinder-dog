<template>
  <button class="btn-go" @click="goBack">
    <img class="arrow" src="./../assets/arrow.svg" alt="стрелка" />
    Вернуться на главную
  </button>
</template>

<style>
.btn-go {
  font-family: 'Jost', sans-serif;
  font-size: 36px;
  display: flex;
  gap: 10px;
  margin-left: 21%;
  margin-bottom: 40px;
  background-color: transparent;
  border: none;
  &:hover {
    color: #b393e6;
  }
}
</style>
