<script setup lang="ts">
import { User } from 'lucide-vue-next'
import { defineProps } from 'vue'

interface BlogCardProps {
  user: string
  title: string
  content: string
  avatarUrl?: string
  createdAt: string
}

const props = defineProps<BlogCardProps>()
</script>

<template>
  <div class="mx-auto max-w-[1000px] cursor-pointer w-full">
    <div
      class="bg-white rounded-lg shadow-lg overflow-hidden border hover:shadow-xl transition-all group"
    >
      <div class="md:p-6 p-4">
        <div class="flex items-center gap-2 mb-2">
          <img
            v-if="props.avatarUrl"
            :src="props.avatarUrl"
            alt="user-avatar"
            class="border border-w-5 rounded-full border-black text-sm w-4 h-4"
          />
          <User
            v-else
            class="border border-w-5 rounded-full border-black text-sm w-4 h-4"
          />
          <p class="text-xs">{{ props.user }}</p>
        </div>

        <div class="flex items-center gap-4">
          <div>
            <h2
              class="sm:text-2xl text-base font-bold mb-2 overflow-hidden text-ellipsis line-clamp-2 group-hover:underline"
            >
              {{ props.title }}
            </h2>
            <p
              class="text-gray-700 sm:text-base text-sm overflow-hidden text-ellipsis line-clamp-2 mb-2"
            >
              {{ props.content }}
            </p>
            <p class="text-xs">{{ props.createdAt }}</p>
          </div>

          <!-- Optional image or additional content can go here -->
          <!-- <div class="md:w-[450px] md:h-[100px] border flex justify-center items-center"> -->
          <!--   <v-icon name="la-pencil-alt-solid" :scale="1.5" /> -->
          <!-- </div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Additional styles can be added here */
</style>
