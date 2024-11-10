import type { ILogin, IRegister } from '@/interfaces/authServices'
import { pathRoutes } from '@/router'
import { AuthService } from '@/services/authService'
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import useToast from '@/hooks/useToast'

const useRegister = () => {
  const isLoading = ref(false)
  const { toastError, toastSuccess } = useToast()
  const router = useRouter()

  const computedIsLoading = computed(() => isLoading.value)

  async function handleSubmit({ data }: { data: ILogin | IRegister }) {
    try {
      isLoading.value = true
      const res = await AuthService.register(data as IRegister)
      toastSuccess(res?.message)
      router.push(pathRoutes.login)
    } catch (error: unknown) {
      const err = error as {
        response?: { data?: { email?: string[]; message?: string } }
      }
      const data = err?.response?.data
      const message = data?.message ? data.message : data?.email?.[0]
      toastError(message ?? 'Ocorreu um erro')
    } finally {
      isLoading.value = false
      console.log('entrou')
    }
  }

  return {
    computedIsLoading,
    handleSubmit,
  }
}

export default useRegister
