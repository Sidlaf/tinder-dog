import { compile, createApp } from 'vue'
import FeedPage from './pages/FeedPage.vue'
import NewDog from './pages/NewDog.vue'
import PageProfile from './pages/PageProfile.vue'
import NewProfile from './pages/NewProfile.vue'
import AboutUs from './pages/AboutUs.vue'
import EditDog from './pages/EditDog.vue'
import PremiumPage from './pages/PremiumPage.vue'
import HomePage from './pages/HomePage.vue'
import SignInPage from './pages/SignInPage.vue'
import LogInPage from './pages/LogInPage.vue'
import App from './App.vue'

//import router from './router.js'
import { createWebHistory, createRouter } from 'vue-router'

const routes = [
  { path: '/', component: FeedPage },
  { path: '/newdog', component: NewDog },
  { path: '/newprofile', component: NewProfile },
  { path: '/profile', component: PageProfile },
  { path: '/aboutus', component: AboutUs },
  { path: '/editdog', component: EditDog },
  { path: '/premiumpage', component: PremiumPage },
  { path: '/homepage', component: HomePage },
  { path: '/signin', component: SignInPage },
  { path: '/login', component: LogInPage }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

createApp(App).use(router).mount('#app')

import './assets/style.css'
