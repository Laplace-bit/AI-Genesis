<template>
  <Layout>
    <div class="container mx-auto px-4 py-8">
      <div class="flex justify-between items-center my-8">
        <h1 class="text-4xl font-bold text-center text-gray-800 dark:text-white">灵感工坊</h1>
        <router-link to="/create-prompt" class="px-4 py-2 font-bold text-white bg-blue-600 rounded-md hover:bg-blue-700">分享你的灵感</router-link>
      </div>
      <div class="masonry">
        <div v-for="prompt in prompts" :key="prompt.id" class="masonry-item">
          <PromptCard :prompt="prompt" />
        </div>
      </div>
    </div>
  </Layout>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import PromptCard from '../components/PromptCard.vue';
import Layout from '../components/Layout.vue';

const prompts = ref([]);

const fetchPrompts = async () => {
  try {
    const response = await axios.get('/api/v1/prompts/');
    prompts.value = response.data;
  } catch (error) {
    console.error("Error fetching prompts:", error);
  }
};

onMounted(() => {
  fetchPrompts();
});
</script>

<style scoped>
.masonry {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1rem;
}

.masonry-item {
  break-inside: avoid;
}
</style>
