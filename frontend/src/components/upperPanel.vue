<script>
    import panelButton from './panelButton.vue';
    export default{
        components: {panelButton},
    }
</script>

<template>
    <div>
        <panelButton text="О нас"></panelButton>
        <panelButton text="Премиум"></panelButton>
        <panelButton text="Профиль"></panelButton>
        <panelButton text="Выйти"></panelButton>
    </div>
</template>


<style scoped>
    div{
        display: flex;
        align-items: center;
        justify-content: right;
        background-color: #B393E6;
        width: 100%;
        height: 100px;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
    }
</style>