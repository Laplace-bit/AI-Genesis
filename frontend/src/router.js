import { createRouter, createWebHistory } from 'vue-router'
import Timeline from './views/Timeline.vue'
import EmpowermentHub from './views/EmpowermentHub.vue'

const routes = [
  {
    path: '/',
    name: 'Timeline',
    component: Timeline,
  },
  {
    path: '/empowerment-hub',
    name: 'EmpowermentHub',
    component: EmpowermentHub,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
