<script setup lang="ts">
import { cn } from '@/lib/utils'
import UserAuthForm from '@/components/UserAuthForm.vue'
import { buttonVariants } from '@/components/ui/button'
import { pathRoutes } from '@/router'
import LogoButton from '@/components/LogoButton.vue'
import { useLogin } from '@/hooks/useLogin'

const { handleSubmit, isLoading } = useLogin()
</script>

<template>
  <div
    class="container h-[100dvh] flex-col items-center justify-center grid lg:max-w-none lg:grid-cols-1 lg:px-0"
  >
    <LogoButton customClass="absolute left-4 top-4 md:left-8 md:top-8  " />

    <RouterLink
      :to="pathRoutes.register"
      :class="
        cn(
          buttonVariants({ variant: 'ghost' }),
          'absolute right-4 top-4 md:right-8 md:top-8',
        )
      "
    >
      Criar conta
    </RouterLink>

    <div class="lg:p-8">
      <div
        class="mx-auto flex w-full flex-col justify-center space-y-6 sm:w-[350px]"
      >
        <div class="flex flex-col space-y-2 text-center">
          <h1 class="text-2xl font-semibold tracking-tight">Login</h1>
          <p class="text-sm text-muted-foreground">
            Digite seu email e senha para entrar na sua conta
          </p>
        </div>
        <UserAuthForm @submit="handleSubmit" :isLoading="isLoading" />
        <p class="px-8 text-center text-sm text-muted-foreground">
          Caso você não tenha uma conta, clique em
          <RouterLink
            :to="pathRoutes.register"
            class="underline underline-offset-4 hover:text-primary"
          >
            Criar uma conta
          </RouterLink>
        </p>
      </div>
    </div>
  </div>
</template>
