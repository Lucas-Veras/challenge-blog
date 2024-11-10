<script setup lang="ts">
import LogoButton from '@/components/LogoButton.vue'
import { buttonVariants } from '@/components/ui/button'
import UserAuthForm from '@/components/UserAuthForm.vue'
import useRegister from '@/hooks/useRegister'
import { cn } from '@/lib/utils'
import { pathRoutes } from '@/router'

const { handleSubmit, computedIsLoading: isLoading } = useRegister()
</script>

<template>
  <div
    class="container h-[100dvh] flex-col items-center justify-center grid lg:max-w-none lg:grid-cols-1 lg:px-0"
  >
    <LogoButton customClass="absolute left-4 top-4 md:left-8 md:top-8  " />

    <RouterLink
      :to="pathRoutes.login"
      :class="
        cn(
          buttonVariants({ variant: 'ghost' }),
          'absolute right-4 top-4 md:right-8 md:top-8',
        )
      "
    >
      Login
    </RouterLink>

    <div class="lg:p-8">
      <div
        class="mx-auto flex w-full flex-col justify-center space-y-6 sm:w-[350px]"
      >
        <div class="flex flex-col space-y-2 text-center">
          <h1 class="text-2xl font-semibold tracking-tight">Crie uma conta</h1>
          <p class="text-sm text-muted-foreground">
            Digite os dados abaixo para criar sua conta
          </p>
        </div>
        <UserAuthForm
          @submit="handleSubmit"
          :isLoading="isLoading"
          formType="register"
        />
        <p class="px-8 text-center text-sm text-muted-foreground">
          Já tem uma conta?
          <RouterLink
            :to="pathRoutes.login"
            class="underline underline-offset-4 hover:text-primary"
          >
            Faça login
          </RouterLink>
        </p>
      </div>
    </div>
  </div>
</template>
