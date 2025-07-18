<template>
  <Layout>
    <div class="flex items-center justify-center min-h-screen bg-gray-900 text-white">
      <div class="w-full max-w-md p-8 space-y-6 bg-gray-800 rounded-lg shadow-lg">
        <div class="text-center">
          <h1 class="text-3xl font-bold">注册</h1>
          <p class="text-gray-400">创建您的账户。</p>
        </div>
        <form @submit.prevent="handleRegister" class="space-y-4">
          <div class="space-y-2">
            <label for="username" class="text-sm font-medium">用户名</label>
            <Input v-model="username" id="username" type="text" placeholder="请输入您的用户名" class="w-full" />
          </div>
          <div class="space-y-2">
            <label for="email" class="text-sm font-medium">邮箱</label>
            <Input v-model="email" id="email" type="email" placeholder="请输入您的邮箱" class="w-full" />
          </div>
          <div class="space-y-2">
            <label for="password" class="text-sm font-medium">密码</label>
            <Input v-model="password" id="password" type="password" placeholder="请输入您的密码" class="w-full" />
          </div>
          <GradientButton type="submit" class="w-full">
            注册
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
