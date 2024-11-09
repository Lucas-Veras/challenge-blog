import type { ILogin, IRegister } from '@/interfaces/authServices'
import { api } from '.'

class AuthService {
  static async login({ email, password }: ILogin) {
    try {
      const response = await api.post('/auth/login/', { email, password })
      return response.data
    } catch (error) {
      throw error
    }
  }

  static async register({ email, password, name }: IRegister) {
    try {
      const response = await api.post('/auth/register/', {
        name,
        email,
        password,
      })
      return response.data
    } catch (error) {
      throw error
    }
  }
}

export { AuthService }
