import { createApp } from 'vue'
import FeedPage from './pages/FeedPage.vue'
import NewDog from './pages/NewDog.vue'
import PageProfile from './pages/PageProfile.vue'
import NewProfile from './pages/NewProfile.vue'
import App from './App.vue'

//import router from './router.js'
import { createWebHistory, createRouter } from 'vue-router'

const routes = [
  { path: '/', component: FeedPage },
  { path: '/newdog', component: NewDog },
  { path: '/newprofile', component: NewProfile },
  { path: '/profile', component: PageProfile }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

createApp(App).use(router).mount('#app');

import './assets/style.css'
