import App from "./App.vue";
import axios from 'axios';
import { createApp } from "vue";
import { createRouter, createWebHistory } from 'vue-router';

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.js";

import LoginComponent from './components/LoginComponent.vue';
import SignUpComponent from './components/SignUpComponent.vue';

const routes = [
  { path: '/', component: LoginComponent },
  { path: '/signUp', component: SignUpComponent },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App);

// Configuração do Axios
app.config.globalProperties.$axios = axios.create({
  baseURL: 'URL_DO_BACKEND',
});

app.use(router);
app.mount('#app');
