import { useUserLoggedStore } from '@/stores/authStore'
import { AuthService } from '@/services/authService'
import { pathRoutes, router } from '@/router'
import useToast from '@/hooks/useToast'

export const useLogout = () => {
  const { loggedUser, setIsAuthenticated, setLoggedUser, setIsLoading } =
    useUserLoggedStore()
  const { toastError, toastSuccess } = useToast()

  const handleLogout = async () => {
    try {
      setIsLoading(true)
      await AuthService.logout()
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      setLoggedUser(null)
      setIsAuthenticated(false)
      toastSuccess('Logout efetuado com sucesso')
      router.push(pathRoutes.home)
    } catch {
      toastError('Erro ao fazer logout')
    } finally {
      setIsLoading(false)
    }
  }

  return {
    loggedUser,
    handleLogout,
  }
}
