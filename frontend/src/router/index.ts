import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const pathRoutes = {
  home: '/',
  login: '/login',
  register: '/register',
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: pathRoutes.home,
      name: 'home',
      component: HomeView,
    },
    {
      path: pathRoutes.login,
      name: 'login',
      component: () => import('../views/LoginView.vue'),
    },
    {
      path: pathRoutes.register,
      name: 'register',
      component: () => import('../views/RegisterView.vue'),
    },
  ],
})

export { router, pathRoutes }
