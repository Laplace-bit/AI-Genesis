<template>
  <Layout>
    <div class="container mx-auto px-4 py-8">
      <div class="text-center my-8">
        <ColourfulText text="分享你的灵感" />
      </div>
      <form @submit.prevent="handleCreatePrompt" class="w-full max-w-lg mx-auto p-8 space-y-6 bg-gray-800 text-white rounded-lg shadow-md">
        <div class="space-y-2">
          <label for="title" class="text-sm font-medium">标题</label>
          <Input v-model="title" type="text" id="title" placeholder="请输入标题" class="w-full" />
        </div>
        <div class="space-y-2">
          <label for="prompt_text" class="text-sm font-medium">提示词</label>
          <textarea v-model="prompt_text" id="prompt_text" rows="4" class="w-full px-4 py-2 mt-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-1 focus:ring-blue-500"></textarea>
        </div>
        <div class="space-y-2">
          <label for="negative_prompt_text" class="text-sm font-medium">反向提示词</label>
          <textarea v-model="negative_prompt_text" id="negative_prompt_text" rows="2" class="w-full px-4 py-2 mt-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-1 focus:ring-blue-500"></textarea>
        </div>
        <div class="space-y-2">
          <label for="model" class="text-sm font-medium">所用模型</label>
          <Input v-model="model" type="text" id="model" placeholder="请输入所用模型" class="w-full" />
        </div>
        <div class="space-y-2">
          <label for="tags" class="text-sm font-medium">标签</label>
          <Input v-model="tags" type="text" id="tags" placeholder="请输入标签，以逗号分隔" class="w-full" />
        </div>
        <div class="space-y-2">
          <label for="preview_url" class="text-sm font-medium">效果预览图</label>
          <FileUpload @file-uploaded="handleFileUploaded" />
        </div>
        <div>
          <GradientButton type="submit" class="w-full">发布</GradientButton>
        </div>
      </form>
    </div>
  </Layout>
</template>

<script setup>
import api from '@/utils/api';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import Layout from '../components/Layout.vue';
import { IInput } from '@/components/ui/input';
import { GradientButton } from '@/components/ui/gradient-button';
import { FileUpload } from '@/components/ui/file-upload';
import { ColourfulText } from '@/components/ui/colourful-text';

const title = ref('');
const prompt_text = ref('');
const negative_prompt_text = ref('');
const model = ref('');
const preview_url = ref('');
const tags = ref('');
const router = useRouter();
const authStore = useAuthStore();

const handleFileUploaded = (url) => {
  preview_url.value = url;
};

const handleCreatePrompt = async () => {
  try {
    const response = await api.post('/prompts/', {
      title: title.value,
      prompt_text: prompt_text.value,
      negative_prompt_text: negative_prompt_text.value,
      model: model.value,
      preview_url: preview_url.value,
      tags: tags.value,
      author_id: authStore.user.id
    });
    console.log(response.data);
    router.push('/inspiration-workshop');
  } catch (error) {
    console.error("Failed to create prompt:", error);
  }
};
</script>
