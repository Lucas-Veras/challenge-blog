import * as yup from 'yup'
import { commonValidation, messages } from '.'

const registerSchema = yup.object().shape({
  name: yup.string().max(50).required(messages.required),
  email: commonValidation.email,
  password: commonValidation.password,
})

export { registerSchema }
