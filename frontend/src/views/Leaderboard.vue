<template>
  <Layout>
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-4xl font-bold text-center my-8 text-gray-800 dark:text-white">热门提示排行榜</h1>
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-8">
        <ol class="list-decimal list-inside">
          <li v-for="prompt in leaderboard" :key="prompt.id" class="mb-4 text-lg">
            <span class="font-semibold">{{ prompt.title }}</span> - {{ prompt.liked_by.length }} aprecieri
          </li>
        </ol>
      </div>
    </div>
  </Layout>
</template>

<script setup>
import api from '@/utils/api';
import { ref, onMounted } from 'vue';
import Layout from '../components/Layout.vue';

const leaderboard = ref([]);

const fetchLeaderboard = async () => {
  try {
    const response = await api.get('/prompts/leaderboard/');
    leaderboard.value = response.data;
  } catch (error) {
    console.error("Error fetching leaderboard:", error);
  }
};

onMounted(() => {
  fetchLeaderboard();
});
</script>
