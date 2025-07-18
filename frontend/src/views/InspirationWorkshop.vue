<template>
  <Layout>
    <div class="container mx-auto px-4 py-8">
      <div class="flex justify-between items-center my-8">
        <ColourfulText text="灵感工坊" />
        <GradientButton @click="goToCreatePrompt">分享你的灵感</GradientButton>
      </div>
      <div class="masonry">
        <div v-for="prompt in prompts" :key="prompt.id" class="masonry-item">
          <DirectionAwareHover :imageUrl="prompt.preview_url">
            <p class="font-bold text-xl">{{ prompt.title }}</p>
            <p class="font-normal text-sm">{{ prompt.model }}</p>
          </DirectionAwareHover>
        </div>
      </div>
    </div>
  </Layout>
</template>

<script setup>
import api from '@/utils/api';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import Layout from '../components/Layout.vue';
import { ColourfulText } from '@/components/ui/colourful-text';
import { GradientButton } from '@/components/ui/gradient-button';
import { DirectionAwareHover } from '@/components/ui/direction-aware-hover';

const prompts = ref([]);
const router = useRouter();

const fetchPrompts = async () => {
  try {
    const response = await api.get('/prompts/');
    prompts.value = response.data;
  } catch (error) {
    console.error("Error fetching prompts:", error);
  }
};

const goToCreatePrompt = () => {
  router.push('/create-prompt');
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
