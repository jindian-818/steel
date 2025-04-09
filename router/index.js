// 1. 定义路由组件.
// 也可以从其他文件导入
import{createRouter,createWebHistory,useRoute}from'vue-router'
import Main from '@/components/Main.vue'
import Login from '@/components/Login.vue'
import Home from'@/components/Home.vue'
import SteelUpload from'@/components/layout/diz/steel/steelUpload.vue'
import SteelHistory from'@/components/layout/diz/steel/steelHistory.vue'
import Report from'@/components/layout/diz/steel/report.vue'
import Detail from'@/components/layout/diz/steel/detail.vue'

import component from 'element-plus/es/components/tree-select/src/tree-select-option.mjs'
const routes = [
  { path: '/',name:'主页', component: Main },
  { path: '/login', name:'登录',component: Login },
  { path: '/home', name:'哈哈',component: Home,props:true ,
   
  children:[
     {path:'steelUpload',component:SteelUpload},
     {path:'steelHistory',component:SteelHistory},
     {path:'report',component:Report},
     {path:'detail',component:Detail},
  ]


  },
]

// 3. 创建路由实例并传递 `routes` 配置
// 你可以在这里输入更多的配置，但我们在这里
// 暂时保持简单
const router =createRouter({
  // 4. 内部提供了 history 模式的实现。为了简单起见，我们在这里使用 hash 模式。
  history:createWebHistory(),
  routes, // `routes: routes` 的缩写
})

router.beforeEach(async(to, from) => {
  // ...
  // 返回 false 以取消导航
  const result=localStorage.getItem('token')
  //console.log(localStorage.getItem('token'))
  if(to.path==='/home'&&result){
  
  return {
    path:'/login'
  }
}

})
export default router