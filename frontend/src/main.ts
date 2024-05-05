import { createApp } from 'vue'
import App from './pages/Feed/App.vue'
import router from './router';


const app = createApp(App);
app.use(router);
app.mount('#app');
import './assets/style.css' 