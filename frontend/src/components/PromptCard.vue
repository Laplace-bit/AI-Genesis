<template>
  <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden transform transition-all duration-500 hover:scale-105">
    <img :src="prompt.preview_url" alt="Prompt preview" class="w-full h-48 object-cover">
    <div class="p-4">
      <h3 class="text-lg font-bold text-gray-800 dark:text-white mb-2">{{ prompt.title }}</h3>
      <div class="flex justify-between items-center mt-4">
        <span class="text-sm font-semibold text-blue-500">{{ prompt.model }}</span>
        <div>
          <button @click="likePrompt" class="text-sm font-semibold text-red-500 hover:underline mr-4">
            ❤ {{ prompt.liked_by.length }}
          </button>
          <button @click="copyPrompt" class="text-sm font-semibold text-blue-500 hover:underline">
            复制提示
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';
import axios from 'axios';

const props = defineProps({
  prompt: {
    type: Object,
    required: true,
  },
});

const copyPrompt = () => {
  navigator.clipboard.writeText(props.prompt.prompt_text);
  // You might want to add a notification to the user that the text has been copied.
};

const likePrompt = async () => {
  try {
    // In a real app, you would get the token from where you stored it (e.g., localStorage)
    const token = "YOUR_JWT_TOKEN"; // This needs to be replaced with actual token management
    const response = await axios.post(`/api/v1/prompts/${props.prompt.id}/like`, {}, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });
    // Ideally, you would update the prompt data in the parent component
    console.log(response.data);
  } catch (error) {
    console.error("Failed to like prompt:", error);
  }
};
</script>
