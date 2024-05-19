<script>
import upperPanel from '@/components/upperPanel.vue'
import backBtn from '@/components/goBackButton.vue'
export default {
  components: { upperPanel, backBtn }
}
</script>

<template> 
    <div class="page-profile">
        <upperPanel></upperPanel>
        <backBtn></backBtn>
        <div class="container">
            <form class="own-data">
                <h2 class="title-container">Личные данные</h2>
                <p class="heading">Имя</p>
                <input class="input" type="text" placeholder="Введите имя" />
                <p class="heading">Фамилия</p>
                <input class="input" type="text" placeholder="Введите фамилию" />
                <p class="heading">Город</p>
                <select class="input--select" v-model="selected">
                    <option disabled value="">Выберите город</option>
                    <option>Томск</option>
                    <option>Новосибирск</option>
                    <option>Красноярск</option>
                </select>
            
                <p class="heading">Email</p>
                <input class="input" type="text" placeholder="Введите электронную почту" />
                <button class="btn" @click="createAccount">Создать аккаунт</button>
            </form>
            <div class="form-dog">
                <div class="about-dog">
                    <h2 class="title-container">Моя собака</h2>
                    <img class="paws" src="./../assets/paws.jpg"  alt="лапки" width="109px" height="90px">
                </div>

            <button class="btn-purp" @click="createForm">Создать анкету</button>                
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
const selected = ref('')
// export default{
//     data(){
//         return{
//             ...
//         }
//     }
// }

// methods:{

// }
</script>

<style>
*{  @import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,100..900;1,100..900&display=swap');

    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
.page-profile{
    margin-top: 0;
}

.container{
    font-family: 'Jost', sans-serif;
    display: flex;
    justify-content: center;
    gap: 100px;
}
.own-data{
    width: 456px;
    height: 695px;
    background-color: #F2F2F2;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.title-container{
    margin-top: 30px;
    margin-bottom: 20px;
    font-size: 36px;
}
.heading{
    color: #474747;
    display: flex;
    align-self: start;
    padding-left: 44px;
    margin-top: 20px;
    margin-bottom: 10px;
    font-size: 24px;

}
.input{
    width: 368px;
    height: 48px;
    border-radius: 7px;
    border-color: 1px #5B5B5B;
    padding: 10px;
    font-size: 16px;
    background: url('./../assets/pencil.svg') no-repeat 320px white;
}

.input--select{
    width: 368px;
    height: 48px;
    border-radius: 7px;
    border-color: 1px #5B5B5B;
    padding: 10px;
    font-size: 16px;
}
.btn{
    font-family: 'Jost', sans-serif;
    width: 368px;
    height: 48px;
    border-radius: 7px;
    background-color: #85889E;
    color: #FFFFFF;
    border-color: 1px #5B5B5B;
    margin-top: 50px;
    font-size: 24px;
    &:hover{
        background-color: #B393E6;
        color: black;
    }
}
.btn-purp{
    font-family: 'Jost', sans-serif;
    width: 535px;
    height: 55px;
    border-radius: 7px;
    background-color: #B393E6;
    color: #FFFFFF;
    margin-top: 50px;
    font-size: 24px;
    &:hover{
        background-color: #FFFFFF;
        color: #B393E6;
    }
    
} 

.btn-go{
    font-family: 'Jost', sans-serif;
    font-size: 36px;
    display: flex;
    gap: 10px;
    margin-left: 21% ;
    margin-bottom: 40px;
    background-color: transparent;
    border: none;
    &:hover{
        color: #B393E6;
    }  
}

.about-dog{
    display: flex;
    justify-content: space-between;
    margin-right: +50px;
    margin-bottom: 5px;
}



</style>