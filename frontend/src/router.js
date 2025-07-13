import { createRouter, createWebHistory } from 'vue-router'
import Timeline from './views/Timeline.vue'

const routes = [
  {
    path: '/',
    name: 'Timeline',
    component: Timeline,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
