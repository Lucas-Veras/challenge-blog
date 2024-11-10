<template>
  <DropdownMenu>
    <DropdownMenuTrigger as-child>
      <Button variant="outline">
        <div v-if="userName" class="flex items-center gap-2">
          <p>{{ userName }}</p>
          <User
            class="border border-w-5 rounded-full border-black text-sm w-4 h-4"
          />
        </div>
      </Button>
    </DropdownMenuTrigger>

    <DropdownMenuContent class="w-56">
      <DropdownMenuLabel>Minha conta</DropdownMenuLabel>

      <DropdownMenuSeparator />
      <DropdownMenuItem @click="handleLogout">
        <LogOut class="mr-2 h-4 w-4" />
        <span>Log out</span>
      </DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</template>

<script setup lang="ts">
import { pathRoutes, router } from '@/router'
import { useUserLoggedStore } from '@/stores/authStore'
import { computed } from 'vue'
import { formatFirstName } from '@/utils/formatFirstName'
import { Button } from '@/components/ui/button'

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
import { LogOut, User } from 'lucide-vue-next'
import { AuthService } from '@/services/authService'

const { loggedUser, setIsAuthenticated, setLoggedUser, setIsLoading } =
  useUserLoggedStore()
const userName = computed(() => {
  return formatFirstName(loggedUser?.name)
})

const handleLogout = async () => {
  try {
    setIsLoading(true)
    await AuthService.logout()
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    setLoggedUser(null)
    setIsAuthenticated(false)
    router.push(pathRoutes.home)
  } catch (error) {
    console.error('Erro ao fazer logout:', error)
  } finally {
    setIsLoading(false)
  }
}
</script>
