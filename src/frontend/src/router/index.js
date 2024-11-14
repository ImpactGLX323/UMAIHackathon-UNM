//import createRouter and createWebHistory from vue-router
import { createRouter, createWebHistory } from 'vue-router';
import QuestionnairePage from '../components/QuestionnairePage.vue';
import ResultPage from '../components/ResultPage.vue';

//URL paths
const routes = [
  { path: '/', name: 'QuestionnairePage', component: QuestionnairePage },
  { path: '/results', name: 'ResultPage', component: ResultPage }
];
//initialise router
const router = createRouter({
  history: createWebHistory(),
  routes
});

//router instance so it could be imported to App.vue
export default router;
