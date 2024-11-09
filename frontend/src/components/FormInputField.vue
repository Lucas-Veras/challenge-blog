<script setup lang="ts">
import { defineProps } from 'vue'
import {
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
  FormControl,
} from '@/components/ui/form'
import type { PropType } from 'vue'
import Input from './ui/input/Input.vue';

type typeInput = 'text' | 'password' | 'email'

const { label, name, placeholder, type } = defineProps({
  name: {
    type: String,
    required: true,
  },
  label: {
    type: String,
    required: true,
  },
  placeholder: {
    type: String,
    default: '',
  },
  type: {
    type: String as PropType<typeInput>,
    default: 'text',
  },
})
</script>

<template>
  <FormField v-slot="{ componentField }" :name="name">
    <FormItem>
      <FormLabel>{{ label }}</FormLabel>
      <FormControl>
        <Input
          :type="type"
          :placeholder="placeholder"
          v-bind="componentField"
        />
      </FormControl>
    </FormItem>
    <FormMessage />
  </FormField>
</template>
