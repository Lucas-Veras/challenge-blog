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
import Input from './ui/input/Input.vue'

type typeInput = 'text' | 'password' | 'email'

const props = defineProps({
  name: {
    type: String,
    required: true,
  },
  label: {
    type: String,
    required: false,
  },
  placeholder: {
    type: String,
    default: '',
  },
  type: {
    type: String as PropType<typeInput>,
    default: 'text',
  },
  class: {
    type: String,
    default: '',
    required: false,
  },
})

const { label, name, placeholder, type, class: className } = props
</script>

<template>
  <FormField v-slot="{ componentField }" :name="name">
    <FormItem :class="className">
      <FormLabel v-if="label">{{ label }}</FormLabel>
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
