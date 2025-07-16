<template>
  <Layout>
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-4xl font-bold text-center my-8 text-gray-800 dark:text-white">个人资料</h1>
      <div v-if="user" class="w-full max-w-lg mx-auto p-8 space-y-6 bg-white dark:bg-gray-800 rounded-lg shadow-md">
        <div class="flex items-center space-x-4">
          <img :src="user.avatar_url || 'https://via.placeholder.com/150'" alt="Avatar" class="w-24 h-24 rounded-full">
          <div>
            <h2 class="text-2xl font-bold text-gray-800 dark:text-white">{{ user.full_name || user.username }}</h2>
            <p class="text-gray-600 dark:text-gray-400">{{ user.email }}</p>
          </div>
        </div>
        <div>
          <h3 class="text-lg font-semibold text-gray-800 dark:text-white">简介</h3>
          <p class="text-gray-600 dark:text-gray-400">{{ user.bio || '暂无简介' }}</p>
        </div>
        <!-- Add an edit button that links to an edit profile page -->
      </div>
    </div>
  </Layout>
</template>

<script setup>
import api from '@/utils/api';
import { ref, onMounted } from 'vue';
import Layout from '../components/Layout.vue';

const user = ref(null);

const fetchUser = async () => {
  try {
    const response = await api.get('/users/me');
    user.value = response.data;
  } catch (error) {
    console.error("Failed to fetch user:", error);
  }
};

onMounted(() => {
  fetchUser();
});
</script>
