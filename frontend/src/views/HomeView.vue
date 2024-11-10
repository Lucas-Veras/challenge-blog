<script setup lang="ts">
import FormInputField from '@/components/FormInputField.vue'
import HeaderPage from '@/components/HeaderPage.vue'
import Button from '@/components/ui/button/Button.vue'
import { Search } from 'lucide-vue-next'

import { ref } from 'vue'

const search = ref('')
</script>

<template>
  <HeaderPage />
  <main class="p-4">
    <h1 class="text-center text-2xl font-bold mb-4">
      Seja bem-vindo ao Writer
    </h1>

    <div class="flex justify-center items-center gap-2 max-w-96 mx-auto mb-6">
      <FormInputField
        v-model="search"
        type="text"
        placeholder="Pesquisar posts"
        name="search"
        class="w-full"
      />
      <Button class="text-white p-2">
        <Search />
      </Button>
    </div>
  </main>
</template>
