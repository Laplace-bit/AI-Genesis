<template>
  <Layout>
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-4xl font-bold text-center my-8 text-gray-800 dark:text-white">AI赋能站</h1>
      <div class="flex justify-center space-x-4 mb-8">
        <select v-model="selectedCategory" @change="fetchTutorials" class="p-2 border rounded-md">
          <option value="">所有类别</option>
          <option value="by_industry">按行业</option>
          <option value="by_task">按任务</option>
        </select>
        <select v-model="selectedDifficulty" @change="fetchTutorials" class="p-2 border rounded-md">
          <option value="">所有难度</option>
          <option value="入门">入门</option>
          <option value="进阶">进阶</option>
          <option value="专家">专家</option>
        </select>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <TutorialCard v-for="tutorial in tutorials" :key="tutorial.id" :tutorial="tutorial" />
      </div>
    </div>
  </Layout>
</template>

<script setup>
import api from '@/utils/api';
import { ref, onMounted } from 'vue';
import TutorialCard from '../components/TutorialCard.vue';
import Layout from '../components/Layout.vue';

const tutorials = ref([]);
const selectedCategory = ref('');
const selectedDifficulty = ref('');

const fetchTutorials = async () => {
  try {
    const params = new URLSearchParams();
    if (selectedCategory.value) {
      params.append('category', selectedCategory.value);
    }
    if (selectedDifficulty.value) {
      params.append('difficulty', selectedDifficulty.value);
    }
    const response = await api.get(`/tutorials/?${params.toString()}`);
    tutorials.value = response.data;
  } catch (error) {
    console.error("Error fetching tutorials:", error);
  }
};

onMounted(() => {
  fetchTutorials();
});
</script>
