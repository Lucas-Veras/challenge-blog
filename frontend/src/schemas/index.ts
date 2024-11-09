import * as yup from 'yup'

export const messages = {
  required: 'Obrigatório',
  email: 'Email inválido',
  min: (min: number) => `Mínimo de ${min} caracteres`,
  noNumbersOnly: 'A senha não pode conter apenas números.',
  specialChar: 'A senha deve conter pelo menos um caractere especial.',
}

export const commonValidation = {
  email: yup.string().email(messages.email).required(messages.required),
  password: yup
    .string()
    .min(8, messages.min(8))
    .required(messages.required)
    .matches(/[a-zA-Z]/, messages.noNumbersOnly)
    .matches(/[!@#$%^&*(),.?":{}|<>]/, messages.specialChar),
}
