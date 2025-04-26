import { createApp } from 'vue'
import router from '@/router/index.js'
import ElementPlus from 'element-plus'
import App from './App.vue'
import 'element-plus/dist/index.css'
import'@/assets/index.css'

// const app = Vue.createApp({})
const app=createApp(App)
//确保 _use_ 路由实例使
//整个应用支持路由。
app.use(router)
app.use(ElementPlus)
app.mount('#app')

// 现在，应用已经启动了！
