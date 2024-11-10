import './assets/index.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import { router } from './router'
import { OhVueIcon, addIcons } from 'oh-vue-icons'
import { LaPencilAltSolid } from 'oh-vue-icons/icons'

addIcons(LaPencilAltSolid)

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.component('v-icon', OhVueIcon)
app.mount('#app')
