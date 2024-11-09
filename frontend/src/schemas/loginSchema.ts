import * as yup from 'yup'
import { commonValidation } from '.'

const loginSchema = yup.object().shape({
  email: commonValidation.email,
  password: commonValidation.password,
})

export { loginSchema }
