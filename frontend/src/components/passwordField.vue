<script>
export default {
  name: 'passwordField',
  props: {
    name: {
      type: String,
      required: true
    },
    text: {
      type: String,
      required: true
    }
  }
}
</script>

<template>
  <div>
    <p style="margin-top: 14px; margin-bottom: 8px; font-size: 18px">{{ name }}</p>
    <div class="fieldBack">
      <input class="inputData" type="password" :placeholder="text" />
    </div>
  </div>
</template>

<style>
.fieldBack {
  background-color: white;
  width: fit-content;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-left: 10px;
  padding-right: 10px;
  border: 1px solid;
  border-color: black;
  border-radius: 10px;
}

.inputData {
  width: 250px;
  height: 40px;
  border-width: 0px;
  font-weight: 500;
  font-size: 18px;
}
.inputDogName:focus {
  outline: none;
}
</style>
