import { api } from '.'

class PostService {
  static async gesPosts(params?: unknown) {
    try {
      const response = await api.get('/posts/', { params })
      return response.data
    } catch (error) {
      throw error
    }
  }
}

export { PostService }
