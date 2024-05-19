<script>
import upperPanel from '@/components/upperPanel.vue'

export default {
  components: { upperPanel,  }
}
</script>
<template> 
    <div class="page_aboutus">
                <upperPanel></upperPanel>
        <div class="abou-us">
        <h2 class="title">Добро пожаловать в ГАВ! – место, где лапы встречаются с судьбой!</h2>
        <p class="text"> Наша  миссия - помочь собакам и их хозяевам находить новых друзей,  единомышленников и, возможно, даже свою собачью любовь. Создавая профиль на «ГАВ!», вы сможете рассказать о своем хвостатом друге - его породе,  возрасте, увлечениях и особенностях характера. Загрузите милые  фотографии вашего питомца, чтобы привлечь внимание потенциальных друзей.<br><br>
            Безопасность и комфорт наших пользователей - главный приоритет. Мы тщательно модерируем все профили и следим за соблюдением правил  сообщества. <br><br>
            Присоединяйтесь к дружному сообществу владельцев собак  на ГАВ! Давайте вместе сделаем жизнь наших питомцев еще более яркой,  насыщенной и полной новых друзей. Ведь счастливая собака - это  счастливый хозяин. </p>
            <p class="gav">Ваша команда «ГАВ!»</p>
    </div>
    </div>

</template>

<style>
*{  @import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,100..900;1,100..900&display=swap');

    margin: 0;
    padding: 0;
    box-sizing: border-box;
} 
.page_aboutus{
    background-image: url(./../assets/fon.png);
    background-size: cover;
    height: 1080px;
    width: 1920px;

}
.abou-us{
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}
.title{
    font-size: 36px;
    margin-top: 100px;
    margin-bottom: 56px;

}
.text{
    width: 1164px;
    font-size: 24px;
    margin-bottom: 36px;
}
.gav{

    font-size: 24px;
    margin-bottom: 36px;
}

</style>