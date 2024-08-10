<template>
  <div class="product-list">
    <h1 class="text-3xl font-bold mb-8">商品一覧</h1>

    <div class="flex flex-col md:flex-row mb-8">
      <!-- カテゴリーフィルター -->
      <div class="w-full md:w-1/4 mb-4 md:mb-0 md:mr-4">
        <h2 class="text-xl font-semibold mb-2">カテゴリー</h2>
        <div class="space-y-2">
          <label v-for="category in categories" :key="category.id" class="flex items-center">
            <input type="checkbox" v-model="selectedCategories" :value="category.id" class="mr-2">
            {{ category.name }}
          </label>
        </div>
      </div>

      <!-- 商品リストと検索 -->
      <div class="w-full md:w-3/4">
        <div class="mb-4">
          <input v-model="searchQuery" type="text" placeholder="商品を検索..." class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500">
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div v-for="product in filteredProducts" :key="product.id" 
               @click="goToProductDetail(product.id)"
               class="bg-white rounded-lg shadow-md p-4 cursor-pointer hover:shadow-lg transition-shadow">
            <img :src="product.image" :alt="product.name" class="w-full h-48 object-cover mb-2 rounded">
            <h3 class="text-lg font-medium mb-1">{{ product.name }}</h3>
            <div v-if="product.salePrice">
              <p class="text-red-600 font-semibold">¥{{ product.salePrice.toLocaleString() }}</p>
              <p class="text-gray-500 line-through text-sm">¥{{ product.price.toLocaleString() }}</p>
            </div>
            <p v-else class="text-gray-600">¥{{ product.price.toLocaleString() }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, onMounted, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { mockProducts, Product } from '../data/mockProducts'

export default defineComponent({
  name: 'ProductList',
  setup() {
    const router = useRouter()
    const route = useRoute()

    const categories = ref([
      { id: 1, name: 'キッチン' },
      { id: 2, name: 'インテリア' },
      { id: 3, name: 'ステーショナリー' },
      { id: 4, name: 'ガーデニング' },
    ])

    const selectedCategories = ref<number[]>([])
    const searchQuery = ref('')

    const filteredProducts = computed(() => {
      return mockProducts.filter(product => {
        const categoryMatch = selectedCategories.value.length === 0 || selectedCategories.value.includes(product.categoryId)
        const searchMatch = product.name.toLowerCase().includes(searchQuery.value.toLowerCase())
        return categoryMatch && searchMatch
      })
    })

    const goToProductDetail = (productId: number) => {
      router.push(`/product/${productId}`)
    }

    const updateSelectedCategories = () => {
      const categoryQuery = route.query.category
      if (categoryQuery) {
        const categoryId = parseInt(categoryQuery as string, 10)
        if (!isNaN(categoryId) && !selectedCategories.value.includes(categoryId)) {
          selectedCategories.value = [categoryId]
        }
      }
    }

    onMounted(() => {
      updateSelectedCategories()
    })

    watch(() => route.query, () => {
      updateSelectedCategories()
    })

    return {
      categories,
      selectedCategories,
      searchQuery,
      filteredProducts,
      goToProductDetail
    }
  }
})
</script>