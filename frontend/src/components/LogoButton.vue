<script setup lang="ts">
import { cn } from '@/lib/utils'
import { RouterLink } from 'vue-router'
import { pathRoutes } from '@/router'

interface LogoButtonProps {
  customClass?: string
}

const props = defineProps<LogoButtonProps>()
</script>

<template>
  <RouterLink
    :to="pathRoutes.home"
    :class="
      cn(
        'z-20 flex items-center align-items-center gap-1 text-xl font-medium',
        props.customClass,
      )
    "
  >
    <v-icon name="la-pencil-alt-solid" :scale="1.5" />
    Writer
  </RouterLink>
</template>
