import type { IResponsePost } from '@/interfaces/posts'
import { api } from '.'

class PostService {
  static async getPosts(params?: unknown): Promise<IResponsePost> {
    try {
      const response = await api.get('/posts/', { params })
      return response.data
    } catch (error) {
      throw error
    }
  }
}

export { PostService }
