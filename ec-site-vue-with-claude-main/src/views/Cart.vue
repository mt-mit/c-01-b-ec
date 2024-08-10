<template>
  <div class="cart">
    <h1 class="text-3xl font-bold mb-8">ショッピングカート</h1>

    <div v-if="cartStore.items.length > 0">
      <div class="space-y-4">
        <div v-for="item in cartStore.items" :key="item.id" class="flex items-center justify-between bg-white p-4 rounded-md shadow">
          <div class="flex items-center">
            <img :src="`/images/products/${item.id}.jpg`" :alt="item.name" class="w-16 h-16 object-cover rounded mr-4">
            <div>
              <h3 class="font-semibold">{{ item.name }}</h3>
              <div v-if="item.salePrice">
                <p class="text-red-600">¥{{ item.salePrice.toLocaleString() }}</p>
                <p class="text-gray-500 line-through text-sm">¥{{ item.price.toLocaleString() }}</p>
              </div>
              <p v-else class="text-gray-600">¥{{ item.price.toLocaleString() }}</p>
            </div>
          </div>
          <div class="flex items-center">
            <div class="flex items-center mr-4">
              <button @click="decrementQuantity(item)" class="px-2 py-1 bg-gray-200 rounded-l">-</button>
              <input v-model="item.quantity" type="number" class="w-12 px-2 py-1 text-center border-t border-b border-gray-300" min="1">
              <button @click="incrementQuantity(item)" class="px-2 py-1 bg-gray-200 rounded-r">+</button>
            </div>
            <button @click="removeItem(item.id)" class="text-red-500 hover:text-red-700">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
            </button>
          </div>
        </div>
      </div>

      <!-- <div class="mt-8 bg-white p-4 rounded-md shadow">
        <div class="flex justify-between items-center mb-4">
          <span class="text-xl font-semibold">合計</span>
          <span class="text-2xl font-bold">¥{{ cartStore.totalPrice.toLocaleString() }}</span>
        </div>
        <button @click="goToCheckout" class="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 transition-colors">
          チェックアウトへ進む
        </button>
      </div>-->
      <div class="mt-8 flex justify-end">
        <div class="w-full max-w-md bg-white rounded-lg shadow-md p-6">
          <div class="flex justify-between items-center mb-6">
            <span class="text-xl font-bold">合計</span>
            <span class="text-xl font-bold">¥{{ (cartStore.totalPrice ).toLocaleString() }}</span>
          </div>
          <button @click="goToCheckout" class="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 transition-colors">
            チェックアウトへ進む
          </button>
        </div>
      </div>
    </div> 

    <div v-else class="text-center">
      <p class="text-xl mb-4">カートは空です。</p>
      <router-link to="/products" class="text-indigo-600 hover:text-indigo-800">商品一覧へ戻る</router-link>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { useRouter } from 'vue-router'
import { useCartStore } from '../stores/cart'

export default defineComponent({
  name: 'Cart',
  setup() {
    const router = useRouter()
    const cartStore = useCartStore()

    const incrementQuantity = (item: any) => {
      cartStore.updateQuantity(item.id, item.quantity + 1)
    }

    const decrementQuantity = (item: any) => {
      if (item.quantity > 1) {
        cartStore.updateQuantity(item.id, item.quantity - 1)
      }
    }

    const removeItem = (itemId: number) => {
      cartStore.removeFromCart(itemId)
    }

    const goToCheckout = () => {
      router.push('/checkout')
    }

    return {
      cartStore,
      incrementQuantity,
      decrementQuantity,
      removeItem,
      goToCheckout
    }
  }
})
</script>