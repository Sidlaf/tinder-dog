<script>
import upperPanel from '@/components/upperPanel.vue'
import backBtn from '@/components/goBackButton.vue'
export default {
  components: { upperPanel, backBtn }
}
</script>

<template>
  <div class="page-premium">
    <upperPanel></upperPanel>
        <backBtn></backBtn>
        <h2 class="title-premium">Купить премиум</h2>
        <div class="container-premium">
            <p class="support">Поддержи развитие проекта
                <img class="dogs" src="./../assets/dogs.png" alt="собаки" width="100px" height="60px" />
            </p>
            
            <p class="do">
                <img class="chevrons" src="./../assets/chevrons.svg" alt="chevrons" width="24px" height="24px" />
                Оформи рамку своего питомца в яркий цвет</p>
            <button class="btn-buy" @click="buy">Подключить за 191 руб/месяц</button>

        </div>
    </div>

</template>
<style>
.page-premium{
    background-color: #F4EDFF;
    height: 865px;
}
.title-premium{
    font-family: 'Jost', sans-serif;
    font-size: 48px;
    display: flex;
    justify-content: center;
    margin-bottom: 60px;
}
.container-premium{
    margin: 0 auto;
    background-color: #ffffff;
    border-radius: 40px;
    width: 650px;
    height: 400px;
    padding-top: 50px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 60px;
}
.dogs{
    margin-left: 30px;
}
.support{
    font-size: 24px;
}
.chevrons{
    margin-right: 10px;
}
.do{
    font-size: 24px;
    display: flex;
    align-items: center;
}
.btn-buy{
    width: 400px;
    height: 60px;
    border: none;
    border-radius: 15px;
    font-size: 24px;
    color: #ffffff;
    background-color: #b393e6;
    &:hover {
    background-color: #ffffff;
    color: #b393e6;
    border: #b393e6 3px solid;
  }
}
</style>
