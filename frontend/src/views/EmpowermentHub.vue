<template>
  <Layout>
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-4xl font-bold text-center my-8 text-gray-800 dark:text-white">AI赋能站</h1>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <TutorialCard v-for="tutorial in tutorials" :key="tutorial.id" :tutorial="tutorial" />
      </div>
    </div>
  </Layout>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import TutorialCard from '../components/TutorialCard.vue';
import Layout from '../components/Layout.vue';

const tutorials = ref([]);

const fetchTutorials = async () => {
  try {
    const response = await axios.get('/api/v1/tutorials/');
    tutorials.value = response.data;
  } catch (error) {
    console.error("Error fetching tutorials:", error);
  }
};

onMounted(() => {
  fetchTutorials();
});
</script>
