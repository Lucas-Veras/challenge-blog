import { createRouter, createWebHistory } from 'vue-router'

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
      component: () => import('../views/HomeView.vue'),
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
