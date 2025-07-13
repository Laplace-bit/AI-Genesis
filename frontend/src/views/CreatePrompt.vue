<template>
  <Layout>
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-4xl font-bold text-center my-8 text-gray-800 dark:text-white">分享你的灵感</h1>
      <form @submit.prevent="handleCreatePrompt" class="w-full max-w-lg mx-auto p-8 space-y-6 bg-white dark:bg-gray-800 rounded-lg shadow-md">
        <div>
          <label for="title" class="text-sm font-medium text-gray-700 dark:text-gray-300">标题</label>
          <input v-model="title" type="text" id="title" class="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600">
        </div>
        <div>
          <label for="prompt_text" class="text-sm font-medium text-gray-700 dark:text-gray-300">提示词</label>
          <textarea v-model="prompt_text" id="prompt_text" rows="4" class="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600"></textarea>
        </div>
        <div>
          <label for="negative_prompt_text" class="text-sm font-medium text-gray-700 dark:text-gray-300">反向提示词</label>
          <textarea v-model="negative_prompt_text" id="negative_prompt_text" rows="2" class="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600"></textarea>
        </div>
        <div>
          <label for="model" class="text-sm font-medium text-gray-700 dark:text-gray-300">所用模型</label>
          <input v-model="model" type="text" id="model" class="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600">
        </div>
        <div>
          <label for="preview_url" class="text-sm font-medium text-gray-700 dark:text-gray-300">效果预览图URL</label>
          <input v-model="preview_url" type="text" id="preview_url" class="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600">
        </div>
        <div>
          <label for="tags" class="text-sm font-medium text-gray-700 dark:text-gray-300">标签</label>
          <input v-model="tags" type="text" id="tags" class="w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600">
        </div>
        <div>
          <button type="submit" class="w-full px-4 py-2 font-bold text-white bg-blue-600 rounded-md hover:bg-blue-700">发布</button>
        </div>
      </form>
    </div>
  </Layout>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { useAuthStore } from '../stores/auth';
import Layout from '../components/Layout.vue';

const title = ref('');
const prompt_text = ref('');
const negative_prompt_text = ref('');
const model = ref('');
const preview_url = ref('');
const tags = ref('');
const router = useRouter();
const authStore = useAuthStore();

const handleCreatePrompt = async () => {
  try {
    const response = await axios.post('/api/v1/prompts/', {
      title: title.value,
      prompt_text: prompt_text.value,
      negative_prompt_text: negative_prompt_text.value,
      model: model.value,
      preview_url: preview_url.value,
      tags: tags.value,
      author_id: authStore.user.id // Add this
    }, {
      headers: {
        Authorization: `Bearer ${authStore.token}`
      }
    });
    console.log(response.data);
    router.push('/inspiration-workshop');
  } catch (error) {
    console.error("Failed to create prompt:", error);
  }
};
</script>
