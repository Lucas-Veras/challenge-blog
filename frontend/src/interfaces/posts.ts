import type { IResponse } from './response'

interface IPost {
  id: number
  title: string
  author: string
  content: string
  created_at: string
}

type IResponsePost = IResponse<IPost[]>

export type { IPost, IResponsePost }
