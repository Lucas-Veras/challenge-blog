import type { IPost } from '@/interfaces/posts'
import { PostService } from '@/services/postsService'
import { computed, onMounted, ref } from 'vue'
import useToast from '@/hooks/useToast'

const useGetPosts = () => {
  const posts = ref<IPost[]>()
  const isLoading = ref(true)
  const { toastError } = useToast()

  const computedIsLoading = computed(() => isLoading.value)
  const computedPosts = computed(() => posts.value)

  const getPosts = async (params?: unknown) => {
    try {
      isLoading.value = true
      const res = await PostService.gesPosts(params)
      posts.value = res.results
    } catch {
      toastError('Erro ao carregar posts')
    } finally {
      isLoading.value = false
    }
  }

  onMounted(() => {
    getPosts()
  })

  return {
    computedPosts,
    computedIsLoading,
    getPosts,
  }
}

export default useGetPosts
