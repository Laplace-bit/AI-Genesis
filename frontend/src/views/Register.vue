<template>
  <Layout>
    <div class="flex items-center justify-center min-h-screen">
      <div class="w-full max-w-md p-8 space-y-6 bg-white dark:bg-gray-800 rounded-lg shadow-md">
        <h1 class="text-2xl font-bold text-center text-gray-800 dark:text-white">注册</h1>
        <form @submit.prevent="handleRegister" class="space-y-6">
          <div>
            <label for="username" class="text-sm font-medium text-gray-700 dark:text-gray-300">用户名</label>
            <input v-model="username" type="text" id="username" class="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600">
          </div>
          <div>
            <label for="email" class="text-sm font-medium text-gray-700 dark:text-gray-300">邮箱</label>
            <input v-model="email" type="email" id="email" class="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600">
          </div>
          <div>
            <label for="password" class="text-sm font-medium text-gray-700 dark:text-gray-300">密码</label>
            <input v-model="password" type="password" id="password" class="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600">
          </div>
          <div>
            <button type="submit" class="w-full px-4 py-2 font-bold text-white bg-blue-600 rounded-md hover:bg-blue-700">注册</button>
          </div>
        </form>
      </div>
    </div>
  </Layout>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import Layout from '../components/Layout.vue';

const username = ref('');
const email = ref('');
const password = ref('');
const router = useRouter();
const authStore = useAuthStore();

const handleRegister = async () => {
  try {
    await authStore.register(username.value, email.value, password.value);
    router.push('/login');
  } catch (error) {
    console.error("Registration failed:", error);
  }
};
</script>
