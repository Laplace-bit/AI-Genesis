import { createRouter, createWebHistory } from 'vue-router'
import Timeline from './views/Timeline.vue'
import EmpowermentHub from './views/EmpowermentHub.vue'

import InspirationWorkshop from './views/InspirationWorkshop.vue'
import TutorialDetail from './views/TutorialDetail.vue'
import Login from './views/Login.vue'
import Register from './views/Register.vue'
import CreatePrompt from './views/CreatePrompt.vue'
import Profile from './views/Profile.vue'
import Leaderboard from './views/Leaderboard.vue'

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
  {
    path: '/tutorials/:id',
    name: 'TutorialDetail',
    component: TutorialDetail,
  },
  {
    path: '/inspiration-workshop',
    name: 'InspirationWorkshop',
    component: InspirationWorkshop,
  },
  {
    path: '/create-prompt',
    name: 'CreatePrompt',
    component: CreatePrompt,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/leaderboard',
    name: 'Leaderboard',
    component: Leaderboard,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
