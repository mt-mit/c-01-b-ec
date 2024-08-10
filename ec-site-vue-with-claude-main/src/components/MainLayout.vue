<template>
  <div class="flex flex-col min-h-screen">
    <header class="bg-white shadow">
      <nav class="container mx-auto px-4 py-4 flex items-center justify-between">
        <router-link to="/" class="text-xl font-bold text-indigo-600">オシャレ雑貨</router-link>
        <div class="flex items-center space-x-4">
          <router-link to="/products" class="text-gray-600 hover:text-indigo-600">商品一覧</router-link>
          <router-link to="/order-history" class="text-gray-600 hover:text-indigo-600">注文履歴</router-link>
          <router-link to="/cart" class="text-gray-600 hover:text-indigo-600 relative">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
            </svg>
            <span v-if="cartItemCount > 0" class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full text-xs w-5 h-5 flex items-center justify-center">
              {{ cartItemCount }}
            </span>
          </router-link>
        </div>
      </nav>
    </header>

    <main class="container mx-auto px-4 py-8 flex-grow">
      <slot></slot>
    </main>

    <footer class="bg-gray-800 text-white py-4 mt-auto">
      <div class="container mx-auto px-4 text-center">
        &copy; 2023 オシャレ雑貨. All rights reserved.
      </div>
    </footer>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from 'vue'
import { useCartStore } from '../stores/cart'

export default defineComponent({
  name: 'MainLayout',
  setup() {
    const cartStore = useCartStore()
    const cartItemCount = computed(() => cartStore.totalItems)

    return {
      cartItemCount
    }
  }
})
</script>