import { createRouter, createWebHashHistory } from 'vue-router'
import PageProfile from './pages/PageProfile.vue'
import NewProfile from './pages/NewProfile.vue'
import FeedPage from './pages/FeedPage.vue'
import NewDog from './pages/NewDog.vue'
import HomePage from './pages/HomePage.vue'

export default createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/feed', component: FeedPage },
    { path: '/pageprofile', component: PageProfile },
    { path: '/newprofile', component: NewProfile },
    { path: '/newdog', component: NewDog },
    { path: '/home', component: HomePage }
  ]
})
