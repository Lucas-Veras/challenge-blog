<template>
  <div class="p-4 flex justify-between items-center border-b-2">
    <div>
      <LogoButton />
    </div>
    <div>
      <UserLoggedDropdown v-if="computedLoggedUser" />

      <RouterLink v-else :to="pathRoutes.login">Login</RouterLink>
    </div>
  </div>
</template>

<script setup lang="ts">
import { pathRoutes } from '@/router'
import LogoButton from './LogoButton.vue'
import { useUserLoggedStore } from '@/stores/authStore'
import { computed } from 'vue'
import UserLoggedDropdown from './UserLoggedDropdown.vue'

const { loggedUser } = useUserLoggedStore()
const computedLoggedUser = computed(() => {
  return loggedUser
})
</script>
