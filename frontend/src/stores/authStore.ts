import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useUserLoggedStore = defineStore('loggedUser', () => {
  const loggedUser = ref()
  const isAuthenticated = ref(false)
  const isLoading = ref(true)

  const setLoggedUser = (
    user: { id: number; name: string; email: string } | null,
  ) => {
    loggedUser.value = user
  }

  const setIsAuthenticated = (value: boolean) => {
    isAuthenticated.value = value
  }

  const setIsLoading = (value: boolean) => {
    isLoading.value = value
  }

  const getIsAuthenticated = () => {
    return isAuthenticated.value
  }

  const getIsloading = () => {
    return isLoading.value
  }

  return {
    loggedUser,
    getIsAuthenticated,
    getIsloading,
    setLoggedUser,
    setIsAuthenticated,
    setIsLoading,
  }
})
