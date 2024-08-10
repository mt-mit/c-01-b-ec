<template>
  <div class="order-complete text-center">
    <div class="mb-8">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-24 w-24 text-green-500 mx-auto animate-bounce" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
    </div>
    <h1 class="text-3xl font-bold mb-4">ご注文ありがとうございます！</h1>
    <p class="text-xl mb-8">注文が正常に完了しました。</p>
    <div v-if="latestOrder" class="bg-white p-6 rounded-lg shadow-md inline-block">
      <p class="text-lg mb-2"><span class="font-semibold">注文ID:</span> {{ latestOrder.id }}</p>
      <p class="text-lg"><span class="font-semibold">注文日時:</span> {{ formatDate(latestOrder.date) }}</p>
    </div>
    <div class="mt-12 space-y-4">
      <router-link to="/order-history" class="block text-indigo-600 hover:text-indigo-800 text-lg">
        注文履歴を確認する
      </router-link>
      <router-link to="/" class="block text-indigo-600 hover:text-indigo-800 text-lg">
        ショッピングを続ける
      </router-link>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from 'vue'
import { useOrderStore } from '../stores/order'

export default defineComponent({
  name: 'OrderComplete',
  setup() {
    const orderStore = useOrderStore()
    const latestOrder = computed(() => orderStore.latestOrder)

    const formatDate = (dateString: string) => {
      return new Date(dateString).toLocaleString('ja-JP', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      })
    }

    return {
      latestOrder,
      formatDate
    }
  }
})
</script>

<style scoped>
.animate-bounce {
  animation: bounce 1s infinite;
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(-25%);
    animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
  }
  50% {
    transform: translateY(0);
    animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
  }
}
</style>