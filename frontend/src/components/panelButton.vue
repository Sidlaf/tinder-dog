<script setup>
defineProps(['text'])
</script>

<template>
    <button>{{ text }}</button>
</template>

<style scoped>
    button{
        margin: 5px 5px 5px 5px;
        line-height: 0px;
        font-family: 'Jost', sans-serif;
        background-color: #ffffff;
        width: 180px;
        height: 60px;
        border-radius: 25px;
        text-align: center;
        vertical-align: middle;
        color: #000000;
        font-size: 30px;
    }
</style>