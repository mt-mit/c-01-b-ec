<template>
  <div v-if="product" class="product-detail">
    <div class="flex flex-col md:flex-row">
      <div class="w-full md:w-1/2 mb-8 md:mb-0 md:mr-8">
        <img :src="product.image" :alt="product.name" class="w-full rounded-lg shadow-md">
      </div>
      <div class="w-full md:w-1/2">
        <h1 class="text-3xl font-bold mb-4">{{ product.name }}</h1>
        <div v-if="product.salePrice" class="mb-4">
          <p class="text-2xl font-semibold text-red-600">¥{{ product.salePrice.toLocaleString() }}</p>
          <p class="text-lg text-gray-500 line-through">¥{{ product.price.toLocaleString() }}</p>
        </div>
        <p v-else class="text-2xl font-semibold mb-4">¥{{ product.price.toLocaleString() }}</p>
        <p class="mb-4">{{ product.description }}</p>
        <div class="mb-4">
          <label for="quantity" class="block mb-2">数量:</label>
          <div class="flex items-center">
            <button @click="decrementQuantity" class="px-3 py-1 bg-gray-200 rounded-l">-</button>
            <input v-model="quantity" type="number" id="quantity" min="1" class="w-16 px-2 py-1 text-center border-t border-b border-gray-300">
            <button @click="incrementQuantity" class="px-3 py-1 bg-gray-200 rounded-r">+</button>
          </div>
        </div>
        <button @click="addToCart" class="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 transition-colors">
          カートに追加
        </button>
        <p v-if="showAddedToCart" class="text-green-600 mt-2">商品がカートに追加されました！</p>
      </div>
    </div>

    <div class="mt-12">
      <h2 class="text-2xl font-bold mb-4">カスタマーレビュー</h2>
      <div v-if="product.reviews.length > 0" class="space-y-4">
        <div v-for="review in product.reviews" :key="review.id" class="bg-white p-4 rounded-md shadow">
          <div class="flex items-center mb-2">
            <div class="font-semibold mr-2">{{ review.userName }}</div>
            <div class="text-yellow-400">{{ '★'.repeat(review.rating) }}</div>
          </div>
          <p>{{ review.comment }}</p>
        </div>
      </div>
      <p v-else class="text-gray-600">まだレビューがありません。</p>
    </div>
  </div>
  <div v-else class="text-center">
    <p>商品が見つかりません。</p>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useCartStore } from '../stores/cart'
import { getProductById, Product } from '../data/mockProducts'

export default defineComponent({
  name: 'ProductDetail',
  setup() {
    const route = useRoute()
    const cartStore = useCartStore()
    const product = ref<Product | null>(null)
    const quantity = ref(1)
    const showAddedToCart = ref(false)

    onMounted(() => {
      const productId = parseInt(route.params.id as string, 10)
      const fetchedProduct = getProductById(productId)
      if (fetchedProduct) {
        product.value = fetchedProduct
      }
    })

    const incrementQuantity = () => {
      quantity.value++
    }

    const decrementQuantity = () => {
      if (quantity.value > 1) {
        quantity.value--
      }
    }

    const addToCart = () => {
      if (product.value) {
        cartStore.addToCart({
          id: product.value.id,
          name: product.value.name,
          price: product.value.price,
          salePrice: product.value.salePrice,
          quantity: quantity.value
        })
        showAddedToCart.value = true
        setTimeout(() => {
          showAddedToCart.value = false
        }, 3000)
      }
    }

    return {
      product,
      quantity,
      showAddedToCart,
      incrementQuantity,
      decrementQuantity,
      addToCart
    }
  }
})
</script>