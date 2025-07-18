<template>
  <div class="min-h-screen bg-gray-100 dark:bg-gray-900 text-gray-900 dark:text-gray-100">
    <nav class="bg-white dark:bg-gray-800 shadow-md">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <h1 class="text-2xl font-bold text-blue-500">AI Genesis</h1>
            </div>
            <div class="hidden md:block">
              <div class="ml-10 flex items-baseline space-x-4">
                <router-link to="/" class="nav-link">AI纪元</router-link>
                <router-link to="/empowerment-hub" class="nav-link">AI赋能站</router-link>
                <router-link to="/inspiration-workshop" class="nav-link">灵感工坊</router-link>
                <router-link to="/leaderboard" class="nav-link">排行榜</router-link>
              </div>
            </div>
          </div>
          <div class="hidden md:block">
            <div class="ml-4 flex items-center md:ml-6">
              <button @click="toggleDark()" class="p-2 rounded-full text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white">
                <span v-if="isDark">☀️</span>
                <span v-else>🌙</span>
              </button>
              <div v-if="isLoggedIn" class="flex items-center">
                <router-link to="/profile" class="nav-link ml-4">个人资料</router-link>
                <button @click="authStore.logout" class="px-3 py-2 rounded-md text-sm font-medium text-white bg-red-600 hover:bg-red-700 ml-4">注销</button>
              </div>
              <div v-else>
                <router-link to="/login" class="nav-link ml-4">登录</router-link>
                <router-link to="/register" class="px-3 py-2 rounded-md text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 ml-4">注册</router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <main>
      <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <slot></slot>
      </div>
    </main>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useAuthStore } from '../stores/auth';
import { useDark, useToggle } from '@vueuse/core';

const authStore = useAuthStore();
const isLoggedIn = computed(() => authStore.isLoggedIn);

const isDark = useDark();
const toggleDark = useToggle(isDark);
</script>

<style scoped>
.nav-link {
  @apply px-3 py-2 rounded-md text-sm font-medium text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700;
}
</style>
