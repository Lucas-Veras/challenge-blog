interface ILogin {
  email: string
  password: string
}

interface IRegister extends ILogin {
  name: string
}

export type { ILogin, IRegister }
