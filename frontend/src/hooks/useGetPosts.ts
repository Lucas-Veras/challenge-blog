import { useToast } from '@/components/ui/toast'
import { PostService } from '@/services/postsService'
import { computed, onMounted, ref } from 'vue'

const useGetPosts = () => {
  const posts = ref()
  const isLoading = ref(true)
  const { toast } = useToast()

  const computedIsLoading = computed(() => isLoading.value)

  const getPosts = async (params?: unknown) => {
    try {
      isLoading.value = true
      const res = await PostService.gesPosts(params)
      posts.value = res?.results
    } catch {
      toast({
        title: 'Erro',
        description: 'Erro ao carregar posts',
        variant: 'destructive',
      })
    } finally {
      isLoading.value = false
    }
  }

  onMounted(() => {
    getPosts()
  })

  return {
    posts,
    computedIsLoading,
    getPosts,
  }
}

export default useGetPosts
