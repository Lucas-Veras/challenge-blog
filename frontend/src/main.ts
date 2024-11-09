import './assets/index.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import { router } from './router'
import { OhVueIcon, addIcons } from 'oh-vue-icons'
import {
  FaFlag,
  RiZhihuFill,
  LaPencilAltSolid,
  RiLoader4Line,
} from 'oh-vue-icons/icons'

addIcons(FaFlag, RiZhihuFill, LaPencilAltSolid, RiLoader4Line)

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.component('v-icon', OhVueIcon)
app.mount('#app')
