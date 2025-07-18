<template>
  <Layout>
    <div class="container mx-auto px-4 py-8">
      <div class="text-center my-8">
        <ColourfulText text="个人资料" />
      </div>
      <div v-if="user" class="w-full max-w-4xl mx-auto">
        <BentoGrid class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div class="col-span-1 md:col-span-1 row-span-2 flex items-center justify-center">
            <DirectionAwareHover :imageUrl="user.avatar_url || 'https://via.placeholder.com/150'">
              <p class="font-bold text-xl">{{ user.full_name || user.username }}</p>
              <p class="font-normal text-sm">{{ user.email }}</p>
            </DirectionAwareHover>
          </div>
          <div class="col-span-1 md:col-span-2 bg-gray-800 p-4 rounded-lg">
            <h3 class="text-lg font-semibold text-white">简介</h3>
            <p class="text-gray-400">{{ user.bio || '暂无简介' }}</p>
          </div>
          <div class="col-span-1 md:col-span-2 bg-gray-800 p-4 rounded-lg flex justify-end items-center">
            <GradientButton @click="editProfile">编辑资料</GradientButton>
          </div>
        </BentoGrid>
      </div>
    </div>
  </Layout>
</template>

<script setup>
import api from '@/utils/api';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import Layout from '../components/Layout.vue';
import { BentoGrid } from '@/components/ui/bento-grid';
import { DirectionAwareHover } from '@/components/ui/direction-aware-hover';
import { GradientButton } from '@/components/ui/gradient-button';
import { ColourfulText } from '@/components/ui/colourful-text';

const user = ref(null);
const router = useRouter();

const fetchUser = async () => {
  try {
    const response = await api.get('/users/me');
    user.value = response.data;
  } catch (error) {
    console.error("Failed to fetch user:", error);
  }
};

const editProfile = () => {
  // router.push('/profile/edit');
  // Or open a modal
  console.log("Navigate to edit profile page");
};

onMounted(() => {
  fetchUser();
});
</script>
