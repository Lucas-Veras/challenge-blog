<script setup lang="ts">
import { pathRoutes } from '@/router'
import { AuthService } from '@/services/authService'
import { useUserLoggedStore } from '@/stores/authStore'
import { computed, onMounted } from 'vue'

import { useRouter } from 'vue-router'

const router = useRouter()

const {
  getIsAuthenticated,
  getIsloading,
  setLoggedUser,
  setIsAuthenticated,
  setIsLoading,
} = useUserLoggedStore()

const checkAuthStatus = async () => {
  const access_token = localStorage.getItem('access_token')
  const refreshToken = localStorage.getItem('refresh_token')
  if (!refreshToken || !access_token) {
    setIsAuthenticated(false)
    setIsLoading(false)
    return
  }
  try {
    const res = await AuthService.refreshToken(refreshToken as string)
    localStorage.setItem('access_token', res.access)
    const user = await AuthService.getLoggedUser()
    setLoggedUser(user)
    setIsAuthenticated(true)
  } catch {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    router.push(pathRoutes.login)
  } finally {
    setIsLoading(false)
  }
}

onMounted(() => {
  checkAuthStatus()
})

const isUserAuthenticated = computed(() => getIsAuthenticated())
const loading = computed(() => getIsloading())

defineExpose({ isUserAuthenticated, loading })
</script>

<template>
  <div v-if="loading">Carregando...</div>
  <div v-else>
    <slot v-if="isUserAuthenticated" />
    <router-view v-else />
  </div>
</template>
