<template>
  <div class="flex flex-col gap-2 w-full" v-if="posts && posts.length > 0">
    <PostCard
      v-for="post in posts"
      :key="post.id"
      :user="post.author"
      :title="post.title"
      :content="post.content"
      :createdAt="post.created_at"
    />
  </div>
  <p v-else-if="!isLoading && posts && posts.length === 0" class="text-center">
    Não há posts para exibir
  </p>
  <div class="my-5">
    <LoaderCircle
      v-if="isLoading"
      name="ri-loader-4-line"
      class="h-7 w-7 animate-spin mx-auto"
    />
  </div>
</template>

<script lang="ts" setup>
import PostCard from '@/components/PostCard.vue'
import type { IPost } from '@/interfaces/posts'
import { LoaderCircle } from 'lucide-vue-next'
import { defineProps } from 'vue'

defineProps({
  isLoading: {
    type: Boolean,
    required: true,
  },
  posts: {
    type: Array as () => IPost[] | undefined,
    required: true,
  },
})
</script>
