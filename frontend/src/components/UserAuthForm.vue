<script setup lang="ts">
import { cn } from '@/lib/utils'
import Button from './ui/button/Button.vue'
import Label from './ui/label/Label.vue'
import Input from './ui/input/Input.vue'
import { ref, type PropType } from 'vue'
import { type ILogin, type IRegister } from '@/interfaces/authServices'

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

const name = ref('')
const email = ref('')
const password = ref('')

const emit = defineEmits<{
  (
    e: 'submit',
    payload: { event: Event; data: ILogin | IRegister },
  ): Promise<void>
}>()

function onSubmit(event: Event) {
  event.preventDefault()

  const data =
    props.formType === 'register'
      ? { name: name.value, email: email.value, password: password.value }
      : { email: email.value, password: password.value }

  emit('submit', { event, data })
}
</script>

<template>
  <div :class="cn('grid gap-6', $attrs.class ?? '')">
    <form @submit="onSubmit">
      <div class="grid gap-2">
        <div v-if="props?.formType === 'register'" class="grid gap-1">
          <Label for="nome"> Nome </Label>
          <Input
            id="nome"
            v-model="name"
            placeholder="Nome"
            type="text"
            auto-capitalize="words"
            auto-complete="name"
            auto-correct="off"
            :disabled="isLoading"
          />
        </div>

        <div class="grid gap-1">
          <Label for="email"> Email </Label>
          <Input
            id="email"
            v-model="email"
            placeholder="name@example.com"
            type="email"
            auto-capitalize="none"
            auto-complete="email"
            auto-correct="off"
            :disabled="isLoading"
          />
        </div>
        <div class="grid gap-1">
          <Label for="email"> Senha </Label>
          <Input
            id="senha"
            v-model="password"
            placeholder="senha"
            type="password"
            auto-correct="off"
            :disabled="isLoading"
          />
        </div>
        <Button :disabled="isLoading" type="submit">
          <LucideSpinner v-if="isLoading" class="mr-2 h-4 w-4 animate-spin" />
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
