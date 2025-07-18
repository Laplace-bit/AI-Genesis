<template>
  <Layout>
    <div class="flex items-center justify-center min-h-screen bg-gray-900 text-white">
      <div class="w-full max-w-md p-8 space-y-6 bg-gray-800 rounded-lg shadow-lg">
        <div class="text-center">
          <h1 class="text-3xl font-bold">登录</h1>
          <p class="text-gray-400">欢迎回来！请输入您的凭据。</p>
        </div>
        <form @submit.prevent="handleLogin" class="space-y-4">
          <div class="space-y-2">
            <label for="username" class="text-sm font-medium">用户名</label>
            <IInput v-model="username" id="username" type="text" placeholder="请输入您的用户名" class="w-full" />
          </div>
          <div class="space-y-2">
            <label for="password" class="text-sm font-medium">密码</label>
            <IInput v-model="password" id="password" type="password" placeholder="请输入您的密码" class="w-full" />
          </div>
          <GradientButton type="submit" class="w-full">
            登录
          </GradientButton>
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
import { IInput } from '@/components/ui/input';
import { GradientButton } from '@/components/ui/gradient-button';

const username = ref('');
const password = ref('');
const router = useRouter();
const authStore = useAuthStore();

const handleLogin = async () => {
  try {
    await authStore.login(username.value, password.value);
    router.push('/');
  } catch (error) {
    console.error("Login failed:", error);
    // You might want to add some user-facing error handling here
  }
};
</script>
