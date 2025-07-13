<template>
  <Layout>
    <div>
      <h1 class="text-4xl font-bold text-center my-8 text-gray-800 dark:text-white">AI纪元</h1>
      <div class="flex justify-center mb-8">
        <input v-model="searchQuery" @input="fetchEvents" type="text" placeholder="搜索事件..." class="p-2 border rounded-md w-full max-w-lg">
      </div>
      <div class="timeline-container relative max-w-4xl mx-auto p-4 sm:p-0">
        <div v-for="(event, index) in events" :key="event.id" class="timeline-item mb-8 flex justify-between items-center w-full sm:flex-row-reverse" :class="index % 2 === 0 ? 'sm:flex-row-reverse' : 'sm:flex-row'">
          <div class="order-1 w-full sm:w-5/12"></div>
          <div class="z-20 flex items-center order-1 bg-gray-800 shadow-xl w-8 h-8 rounded-full">
            <h1 class="mx-auto font-semibold text-lg text-white">{{ index + 1 }}</h1>
          </div>
          <div class="order-1 bg-white dark:bg-gray-800 rounded-lg shadow-xl w-full sm:w-5/12 px-6 py-4 transform transition-all duration-500 hover:scale-105">
            <h3 class="mb-3 font-bold text-gray-800 dark:text-white text-xl">{{ event.title }}</h3>
            <p class="text-sm leading-snug tracking-wide text-gray-600 dark:text-gray-400 text-opacity-100">{{ event.description }}</p>
            <div class="text-sm font-semibold text-blue-500 mt-4">
              <a :href="event.source_url" target="_blank" rel="noopener noreferrer">了解更多</a>
            </div>
            <div class="text-xs text-gray-500 dark:text-gray-500 mt-2">{{ event.date }}</div>
            <div class="mt-2">
              <span v-for="tag in event.tags.split(',')" :key="tag" class="inline-block bg-gray-200 dark:bg-gray-700 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 dark:text-gray-200 mr-2 mb-2">{{ tag.trim() }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </Layout>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import Layout from '../components/Layout.vue';

const events = ref([]);
const searchQuery = ref('');

const fetchEvents = async () => {
  try {
    const params = new URLSearchParams();
    if (searchQuery.value) {
      params.append('q', searchQuery.value);
    }
    const response = await axios.get(`/api/v1/timeline/?${params.toString()}`);
    events.value = response.data;
  } catch (error) {
    console.error("Error fetching timeline events:", error);
  }
};

onMounted(() => {
  fetchEvents();
});
</script>

<style scoped>
@media (min-width: 640px) {
  .timeline-container::before {
    content: '';
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    top: 0;
    bottom: 0;
    width: 4px;
    background-color: #4A5568; /* gray-700 */
  }
}

.timeline-item {
  opacity: 0;
  animation: fadeIn 0.5s forwards;
  animation-delay: calc(var(--i, 1) * 0.2s);
}

@keyframes fadeIn {
  to {
    opacity: 1;
  }
}
</style>
