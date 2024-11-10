import type { ILogin } from '@/interfaces/authServices'
import type { IResponseError } from '@/interfaces/responseError'
import { pathRoutes } from '@/router'
import { AuthService } from '@/services/authService'
import { useUserLoggedStore } from '@/stores/authStore'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import useToast from '@/hooks/useToast'

export const useLogin = () => {
  const isLoading = ref(false)
  const { toastSuccess, toastError } = useToast()
  const router = useRouter()
  const { setLoggedUser } = useUserLoggedStore()

  async function handleSubmit({ data }: { data: ILogin }) {
    try {
      isLoading.value = true
      const res = await AuthService.login(data)
      localStorage.setItem('access_token', res.access)
      localStorage.setItem('refresh_token', res.refresh)
      const user = await AuthService.getLoggedUser()
      setLoggedUser(user)
      toastSuccess('Login efetuado com sucesso')
      router.push(pathRoutes.home)
    } catch (error: unknown) {
      const err = error as IResponseError
      toastError(err.response?.data?.message || 'Ocorreu um erro')
    } finally {
      isLoading.value = false
    }
  }

  return {
    isLoading,
    handleSubmit,
  }
}
