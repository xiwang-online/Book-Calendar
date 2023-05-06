import { createRouter, createWebHashHistory, createWebHistory } from "vue-router"



// 2. 定义路由配置
const routes = [
  {
    path: '/',
    component: () => import('./pages/home.vue'),

  },
  {
    path: '/bookdetails',
    component: () => import('./pages/bookdetails.vue'),
    children: [

    ]
  },

  {
    path: '/booklist',
    component: () => import('./pages/booklist.vue'),
    children: [

    ]
  },

  {
    path: '/submit',
    component: () => import('./pages/submit.vue'),
    children: [

    ]
  },

  
  {
    path: '/signin',
    component: () => import('./pages/signin.vue'),
    children: [

    ]
  },



  {
    path: '/back',
    component: () => import('./pages/back.vue'),
    beforeEnter(to, from, next) {         //独享路由守卫  
      if (localStorage.getItem('key') === 'value') {
        next()
      } else {
        alert("未登录");
        router.push("signin"); 
      }
    },
    children: [
     
    ]
  },

  {
    path: '/backsub',
    component: () => import('./pages/backsub.vue'),
    beforeEnter(to, from, next) {         //独享路由守卫  
      if (localStorage.getItem('key') === 'value') {
        next()
      } else {
        alert("未登录");
        router.push("signin"); 
      }
    },
    children: [
     
    ]
  },


  
  {
    path: '/TemplateHope2',
    component: () => import('./pages/TemplateHope2.vue'),
    children: [

    ]
  },
  


];

// 3. 创建路由实例
const router = createRouter({
  // 4. 采用hash 模式
  history: createWebHashHistory(),
  // 采用 history 模式
  // history: createWebHistory(),
  routes, //使用上方定义的路由配置
});

/*
// 路由守卫
router.beforeEach((to, from, next) => {
    const isLogin = localStorage.ele_login ? true : false;
    if (to.path == '/login') {
      next();
    } else {
      // 是否在登录状态下
      isLogin ? next() : next('/login');
    }
  });
*/


export default router
//导出router
