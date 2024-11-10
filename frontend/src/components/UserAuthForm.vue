<script setup lang="ts">
import { cn } from '@/lib/utils'
import Button from './ui/button/Button.vue'
import { type PropType } from 'vue'
import { type ILogin, type IRegister } from '@/interfaces/authServices'
import { useForm } from 'vee-validate'

import { loginSchema } from '@/schemas/loginSchema'
import { registerSchema } from '@/schemas/registerSchema'
import FormInputField from '@/components/FormInputField.vue'
import { LoaderCircle } from 'lucide-vue-next'

type FormType = 'login' | 'register'
const props = defineProps({
  formType: {
    type: String as PropType<FormType>,
    default: 'login',
  },
  isLoading: {
    type: Boolean as PropType<boolean>,
    default: false,
  },
})

const { handleSubmit } = useForm<ILogin | IRegister>({
  validationSchema: props.formType === 'login' ? loginSchema : registerSchema,
  validateOnMount: false,
})

const emit = defineEmits<{
  (e: 'submit', payload: { data: ILogin | IRegister }): Promise<void>
}>()

const onSubmit = handleSubmit(values => {
  emit('submit', { data: values })
})
</script>

<template>
  <div :class="cn('grid gap-6', $attrs.class ?? '')">
    <form @submit="onSubmit">
      <div class="grid gap-2">
        <FormInputField
          v-if="props?.formType === 'register'"
          name="name"
          label="Nome"
          placeholder="Digite seu nome de usuário"
          type="text"
        />

        <FormInputField
          name="email"
          label="Email"
          placeholder="Digite seu email"
          type="email"
        />

        <FormInputField
          name="password"
          label="Senha"
          placeholder="Digite sua senha"
          type="password"
        />

        <Button :disabled="isLoading" type="submit">
          <LoaderCircle
            v-if="isLoading"
            name="ri-loader-4-line"
            class="h-4 w-4 animate-spin text-white"
          />
          {{ props.formType === 'login' ? 'Entrar' : 'Cadastrar' }}
        </Button>
      </div>
    </form>
    <div class="relative">
      <div class="absolute inset-0 flex items-center">
        <span class="w-full border-t" />
      </div>
      <div class="relative flex justify-center text-xs uppercase"></div>
    </div>
  </div>
</template>
