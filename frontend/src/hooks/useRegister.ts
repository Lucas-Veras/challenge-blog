import { useToast } from '@/components/ui/toast'
import type { ILogin, IRegister } from '@/interfaces/authServices'
import { pathRoutes } from '@/router'
import { AuthService } from '@/services/authService'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const useRegister = () => {
  const isLoading = ref(false)
  const { toast } = useToast()
  const router = useRouter()

  async function handleSubmit({ data }: { data: ILogin | IRegister }) {
    try {
      isLoading.value = true
      const res = await AuthService.register(data as IRegister)
      toast({
        title: 'Sucesso',
        description: res?.message,
        variant: 'default',
      })
      router.push(pathRoutes.login)
    } catch (error: unknown) {
      const err = error as { response?: { data?: { email?: string[] } } }
      toast({
        title: 'Erro',
        description: err.response?.data?.email?.[0] || 'Ocorreu um erro',
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

export default useRegister
