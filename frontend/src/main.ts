import { createApp } from 'vue'
import FeedPage from './pages/FeedPage.vue'
import NewDog from './pages/NewDog.vue'
import PageProfile from './pages/PageProfile.vue'
import NewProfile from './pages/NewProfile.vue'
import App from './App.vue'

// import router from './router.js'
import { createMemoryHistory, createRouter } from 'vue-router'

const routes = [
  { path: '/', component: FeedPage },
  { path: '/newdog', component: NewDog },
  { path: '/newProfile', component: NewProfile },
  { path: '/profile', component: PageProfile }
]

const router = createRouter({
  history: createMemoryHistory(),
  routes
})

const app = createApp(App)
app.use(router)
app.mount('#app')
import './assets/style.css'
