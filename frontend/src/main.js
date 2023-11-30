import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
import { createRouter, createWebHistory } from 'vue-router';
import VotingComponent from './components/VotingComponent.vue';

const routes = [
  { path: '/', component: VotingComponent },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App);

// Configuração do Axios
app.config.globalProperties.$axios = axios.create({
  baseURL: 'http://localhost:3000',
});

app.use(router);
app.mount('#app');
