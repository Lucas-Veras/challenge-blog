<script setup lang="ts">
import FormInputField from '@/components/FormInputField.vue'
import HeaderPage from '@/components/HeaderPage.vue'
import PostCard from '@/components/PostCard.vue'
import Button from '@/components/ui/button/Button.vue'
import useGetPosts from '@/hooks/useGetPosts'
import { LoaderCircle, Search } from 'lucide-vue-next'

import { ref } from 'vue'

const search = ref('')
const { computedIsLoading, posts } = useGetPosts()
</script>

<template>
  <HeaderPage />
  <main class="p-4">
    <h1 class="text-center text-2xl font-bold mb-4">
      Seja bem-vindo ao Writer
    </h1>

    <form class="flex justify-center items-center gap-2 max-w-96 mx-auto mb-6">
      <FormInputField
        v-model="search"
        type="text"
        placeholder="Pesquisar posts"
        name="search"
        class="w-full"
      />
      <Button class="text-white p-2" :disabled="computedIsLoading">
        <Search />
      </Button>
    </form>

    <div class="flex flex-col gap-2 w-full">
      <LoaderCircle
        v-if="computedIsLoading"
        name="ri-loader-4-line"
        class="h-7 w-7 animate-spin mx-auto"
      />
      <PostCard
        v-else-if="!computedIsLoading && posts.length > 0"
        v-for="post in posts"
        :key="post.id"
        :user="post.author"
        :title="post.title"
        :content="post.content"
        :createdAt="post.created_at"
      />
      <p v-else>Não há posts para exibir</p>
    </div>
  </main>
</template>
