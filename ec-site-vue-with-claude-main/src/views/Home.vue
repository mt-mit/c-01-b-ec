<template>
  <div class="home">
    <h1 class="text-3xl font-bold mb-8">オシャレ雑貨へようこそ</h1>

    <!-- カテゴリー別商品表示 -->
    <section class="mb-12">
      <h2 class="text-2xl font-semibold mb-4">カテゴリー</h2>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div v-for="category in categories" :key="category.id" 
             @click="goToProductList(category.id)"
             class="bg-white rounded-lg shadow-md p-4 text-center cursor-pointer hover:shadow-lg transition-shadow">
          <img :src="category.image" :alt="category.name" class="w-full h-32 object-cover mb-2 rounded">
          <h3 class="text-lg font-medium">{{ category.name }}</h3>
        </div>
      </div>
    </section>

    <!-- おすすめ商品 -->
    <section class="mb-12">
      <h2 class="text-2xl font-semibold mb-4">おすすめ商品</h2>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div v-for="product in recommendedProducts" :key="product.id" 
             @click="goToProductDetail(product.id)"
             class="bg-white rounded-lg shadow-md p-4 cursor-pointer hover:shadow-lg transition-shadow">
          <img :src="product.image" :alt="product.name" class="w-full h-48 object-cover mb-2 rounded">
          <h3 class="text-lg font-medium mb-1">{{ product.name }}</h3>
          <p class="text-gray-600">¥{{ product.price.toLocaleString() }}</p>
        </div>
      </div>
    </section>

    <!-- セール品 -->
    <section class="mb-12">
      <h2 class="text-2xl font-semibold mb-4">セール</h2>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div v-for="product in saleProducts" :key="product.id" 
             @click="goToProductDetail(product.id)"
             class="bg-white rounded-lg shadow-md p-4 cursor-pointer hover:shadow-lg transition-shadow relative overflow-hidden">
          <div class="absolute top-0 right-0 bg-red-500 text-white px-2 py-1 text-sm">SALE</div>
          <img :src="product.image" :alt="product.name" class="w-full h-48 object-cover mb-2 rounded">
          <h3 class="text-lg font-medium mb-1">{{ product.name }}</h3>
          <p class="text-gray-600 line-through">¥{{ product.price.toLocaleString() }}</p>
          <p class="text-red-500 font-bold">¥{{ product.salePrice!.toLocaleString() }}</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getRecommendedProducts, getSaleProducts, Product } from '../data/mockProducts'

export default defineComponent({
  name: 'Home',
  setup() {
    const router = useRouter()

    const categories = ref([
      { id: 1, name: 'キッチン', image: '/images/categories/kitchen.jpg' },
      { id: 2, name: 'インテリア', image: '/images/categories/interior.jpg' },
      { id: 3, name: 'ステーショナリー', image: '/images/categories/stationery.jpg' },
      { id: 4, name: 'ガーデニング', image: '/images/categories/gardening.jpg' },
    ])

    const recommendedProducts = ref<Product[]>([])
    const saleProducts = ref<Product[]>([])

    onMounted(() => {
      recommendedProducts.value = getRecommendedProducts()
      saleProducts.value = getSaleProducts()
    })

    const goToProductDetail = (productId: number) => {
      router.push(`/product/${productId}`)
    }

    const goToProductList = (categoryId: number) => {
      router.push({ path: '/products', query: { category: categoryId.toString() } })
    }

    return {
      categories,
      recommendedProducts,
      saleProducts,
      goToProductDetail,
      goToProductList
    }
  }
})
</script>