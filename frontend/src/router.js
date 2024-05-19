import { createRouter, createWebHashHistory } from 'vue-router'
import PageProfile from './pages/PageProfile.vue'
import NewProfile from './pages/NewProfile.vue'
import FeedPage from './pages/FeedPage.vue'
import NewDog from './pages/NewDog.vue'

export default createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/Feed', component: FeedPage },
    { path: '/PageProfile', component: PageProfile },
    { path: '/NewProfile', component: NewProfile },
    { path: '/NewDog', component: NewDog }
  ]
})
