import type { IPost } from '@/interfaces/posts'
import { PostService } from '@/services/postsService'
import { computed, onMounted, onUnmounted, ref } from 'vue'
import useToast from '@/hooks/useToast'

const useGetPosts = () => {
  const search = ref('')
  const pagination = ref({
    page: 1,
  })
  const hasMore = ref(true)
  const posts = ref<IPost[]>()
  const isLoading = ref(false)
  const { toastError } = useToast()

  const computedIsLoading = computed(() => isLoading.value)
  const computedPosts = computed(() => posts.value)

  const getPosts = async (params?: { search?: string }) => {
    try {
      isLoading.value = true
      const res = await PostService.getPosts({
        page: pagination.value.page,
        ...params,
      })

      if (res.results.length) {
        if (!posts.value) posts.value = [...res.results]
        else posts.value = [...posts.value, ...res.results]
        pagination.value.page++
        hasMore.value = res.next !== null
      } else {
        hasMore.value = false
      }
    } catch {
      toastError('Erro ao carregar posts')
    } finally {
      isLoading.value = false
    }
  }

  const resetPagination = () => {
    posts.value = []
    pagination.value.page = 1
    hasMore.value = true
  }

  const handleSearchSubmit = async (e: Event) => {
    e.preventDefault()
    resetPagination()
    await getPosts({ search: search.value })
  }

  const onScroll = () => {
    const scrollPosition = window.innerHeight + window.scrollY
    const bottomPosition = document.documentElement.offsetHeight - 100

    if (scrollPosition >= bottomPosition && hasMore.value && !isLoading.value) {
      getPosts({ search: search.value })
    }
  }

  onMounted(() => {
    getPosts()
    window.addEventListener('scroll', onScroll)
  })

  onUnmounted(() => {
    window.removeEventListener('scroll', onScroll)
  })

  return {
    computedPosts,
    computedIsLoading,
    getPosts,
    search,
    handleSearchSubmit,
  }
}

export default useGetPosts
