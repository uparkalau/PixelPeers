import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
// import Admin from '../views/Admin.vue'
// import Profile from '../views/Profile.vue'
// import PublicGallery from '../views/PublicGallery.vue'

const routes = [
  { path: '/', component: Home },
  // { path: '/admin', component: Admin },
  // { path: '/profile', component: Profile },
  // { path: '/:subdomain', component: PublicGallery }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router