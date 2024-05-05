import { createRouter, createWebHashHistory } from "vue-router";
import PageProfile from "./pages/PageProfile.vue";
import cardCard from "./components/cardCard.vue";
import NewProfile from "./pages/NewProfile.vue";


export default createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: '/', component: cardCard },
        { path: '/PageProfile', component: PageProfile },
        { path: '/NewProfile', component: NewProfile }
    ]
})