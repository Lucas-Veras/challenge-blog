import { useToast as useCustomToast } from '@/components/ui/toast'

const useToast = () => {
  const { toast } = useCustomToast()

  const toastError = (message: string) => {
    toast({
      title: 'Erro',
      description: message,
      variant: 'destructive',
    })
  }

  const toastSuccess = (message: string) => {
    toast({
      title: 'Sucesso',
      description: message,
      variant: 'success',
    })
  }

  return {
    toastError,
    toastSuccess,
  }
  
}

export default useToast
