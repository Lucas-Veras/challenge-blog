<script setup lang="ts">
import { RouterView } from 'vue-router'
import Toaster from './components/ui/toast/Toaster.vue'
import AuthProvider from './Providers/AuthProvider.vue'
</script>

<template>
  <Toaster />
  <AuthProvider>
    <RouterView />
  </AuthProvider>
</template>
