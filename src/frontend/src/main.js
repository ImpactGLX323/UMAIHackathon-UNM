import { createApp } from 'vue';
import App from './App.vue';
//import router config
import router from './router';

createApp(App)
//allows us to use routes in the application
.use(router)
.mount('#app');

