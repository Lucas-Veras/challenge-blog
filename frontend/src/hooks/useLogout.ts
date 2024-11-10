import { useUserLoggedStore } from '@/stores/authStore'
import { AuthService } from '@/services/authService'
import { pathRoutes, router } from '@/router'

export const useLogout = () => {
  const { loggedUser, setIsAuthenticated, setLoggedUser, setIsLoading } =
    useUserLoggedStore()

  const handleLogout = async () => {
    try {
      setIsLoading(true)
      await AuthService.logout()
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      setLoggedUser(null)
      setIsAuthenticated(false)
      router.push(pathRoutes.home)
    } catch (error) {
      console.error('Erro ao fazer logout:', error)
    } finally {
      setIsLoading(false)
    }
  }

  return {
    loggedUser,
    handleLogout,
  }
}
