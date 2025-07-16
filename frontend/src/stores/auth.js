import { defineStore } from 'pinia';
import api from '@/utils/api';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || null,
  }),
  getters: {
    isLoggedIn: (state) => !!state.token,
  },
  actions: {
    async login(username, password) {
      const formData = new FormData();
      formData.append('username', username);
      formData.append('password', password);
      const response = await api.post('/token', formData);
      this.token = response.data.access_token;
      localStorage.setItem('token', this.token);
      await this.fetchUser();
    },
    async register(username, email, password) {
      await api.post('/users/', { username, email, password });
    },
    async fetchUser() {
      if (this.token) {
        const response = await api.get('/users/me');
        this.user = response.data;
      }
    },
    logout() {
      this.user = null;
      this.token = null;
      localStorage.removeItem('token');
    },
  },
});

