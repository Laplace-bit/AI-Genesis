<template>
  <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden transform transition-all duration-500 hover:scale-105">
    <img :src="tutorial.cover_image_url" alt="Tutorial cover image" class="w-full h-48 object-cover">
    <div class="p-6">
      <h3 class="text-xl font-bold text-gray-800 dark:text-white mb-2">{{ tutorial.title }}</h3>
      <p class="text-gray-600 dark:text-gray-400 mb-4">{{ tutorial.subcategory }}</p>
      <div class="flex justify-between items-center">
        <span class="text-sm font-semibold text-blue-500">{{ tutorial.difficulty }}</span>
        <router-link :to="{ name: 'TutorialDetail', params: { id: tutorial.id } }" class="text-sm font-semibold text-blue-500 hover:underline">查看详情</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  tutorial: {
    type: Object,
    required: true,
  },
});
</script>
