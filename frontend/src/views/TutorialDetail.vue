<template>
  <Layout>
    <div v-if="tutorial" class="container mx-auto px-4 py-8">
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-8">
        <h1 class="text-4xl font-bold mb-4 text-gray-800 dark:text-white">{{ tutorial.title }}</h1>
        <div class="flex items-center mb-4">
          <span class="bg-blue-100 text-blue-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-blue-900 dark:text-blue-300">{{ tutorial.category }}</span>
          <span class="bg-green-100 text-green-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-green-900 dark:text-green-300">{{ tutorial.difficulty }}</span>
        </div>
        <img :src="tutorial.cover_image_url" alt="Tutorial cover image" class="w-full h-96 object-cover rounded-lg mb-8">
        <div class="prose dark:prose-invert max-w-none">
          <p class="lead">{{ tutorial.content }}</p>
          <!-- Here you would typically render the full content, perhaps from Markdown -->
        </div>
      </div>
    </div>
    <div v-else class="text-center py-16">
      <p class="text-gray-500">Loading tutorial...</p>
    </div>
  </Layout>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import Layout from '../components/Layout.vue';

const route = useRoute();
const tutorial = ref(null);

const fetchTutorial = async () => {
  try {
    const tutorialId = route.params.id;
    const response = await axios.get(`/api/v1/tutorials/${tutorialId}`);
    tutorial.value = response.data;
  } catch (error) {
    console.error("Error fetching tutorial:", error);
  }
};

onMounted(() => {
  fetchTutorial();
});
</script>

<style scoped>
.prose {
  /* Add custom prose styles if needed */
}
</style>
