import { useToast } from '@/components/ui/toast'
import type { ILogin } from '@/interfaces/authServices'
import type { IResponseError } from '@/interfaces/responseError'
import { pathRoutes } from '@/router'
import { AuthService } from '@/services/authService'
import { useUserLoggedStore } from '@/stores/authStore'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

export const useLogin = () => {
  const isLoading = ref(false)
  const { toast } = useToast()
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
      toast({
        title: 'Sucesso',
        description: 'Login efetuado com sucesso',
        variant: 'success',
      })
      router.push(pathRoutes.home)
    } catch (error: unknown) {
      const err = error as IResponseError
      toast({
        title: 'Erro',
        description: err.response?.data?.message || 'Ocorreu um erro',
        variant: 'destructive',
      })
    } finally {
      isLoading.value = false
    }
  }

  return {
    isLoading,
    handleSubmit,
  }
}
