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

    <DropdownMenuContent class="w-56 mr-4">
      <DropdownMenuLabel>Minha conta</DropdownMenuLabel>

      <DropdownMenuSeparator />
      <DropdownMenuItem @click="handleLogout">
        <LogOut class="mr-2 h-4 w-4" />
        <span>Sair</span>
      </DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</template>

<script setup lang="ts">
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
import { useLogout } from '@/hooks/useLogout'

const { handleLogout, loggedUser } = useLogout()
const userName = computed(() => {
  return formatFirstName(loggedUser?.name)
})
</script>
