<template>
  <div class="checkout">
    <h1 class="text-3xl font-bold mb-8">チェックアウト</h1>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
      <div class="order-summary bg-white p-6 rounded-lg shadow-md">
        <h2 class="text-2xl font-semibold mb-4">注文内容</h2>
        <div class="space-y-4">
          <div v-for="item in cartStore.items" :key="item.id" class="flex justify-between items-center">
            <div>
              <h3 class="font-semibold">{{ item.name }}</h3>
              <p class="text-sm text-gray-600">数量: {{ item.quantity }}</p>
            </div>
            <div class="text-right">
              <p v-if="item.salePrice" class="text-red-600 font-semibold">¥{{ (item.salePrice * item.quantity).toLocaleString() }}</p>
              <p v-if="item.salePrice" class="text-gray-500 line-through text-sm">¥{{ (item.price * item.quantity).toLocaleString() }}</p>
              <p v-else class="font-semibold">¥{{ (item.price * item.quantity).toLocaleString() }}</p>
            </div>
          </div>
        </div>
        <div class="mt-4 pt-4 border-t border-gray-200">
          <div class="flex justify-between items-center mb-2">
            <span class="text-gray-600">小計</span>
            <span class="font-semibold">¥{{ cartStore.totalPrice.toLocaleString() }}</span>
          </div>
          <div class="flex justify-between items-center mb-2">
            <span class="text-gray-600">送料</span>
            <span class="font-semibold">¥500</span>
          </div>
          <div class="flex justify-between items-center text-lg font-bold">
            <span>合計</span>
            <span>¥{{ (cartStore.totalPrice + 500).toLocaleString() }}</span>
          </div>
        </div>
      </div>

      <div class="shipping-payment">
        <form @submit.prevent="submitOrder" class="space-y-6">
          <div class="bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-2xl font-semibold mb-4">配送情報</h2>
            <div class="space-y-4">
              <div>
                <label for="name" class="block mb-1">氏名</label>
                <input v-model="form.name" type="text" id="name" required class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500">
              </div>
              <div>
                <label for="phone" class="block mb-1">電話番号</label>
                <input v-model="form.phone" type="tel" id="phone" required class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500">
              </div>
              <div>
                <label for="postalCode" class="block mb-1">郵便番号</label>
                <input v-model="form.postalCode" type="text" id="postalCode" required pattern="\d{7}" maxlength="7" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500">
              </div>
              <div>
                <label for="address" class="block mb-1">住所</label>
                <input v-model="form.address" type="text" id="address" required class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500">
              </div>
              <div>
                <label for="email" class="block mb-1">メールアドレス</label>
                <input v-model="form.email" type="email" id="email" required class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500">
              </div>
              <!-- 配送希望日を選択-->
              <div>
                <label for="deliveryDate" class="block mb-1">配送希望日</label>
                <input 
                  v-model="form.deliveryDate" 
                  type="date" 
                  id="deliveryDate" 
                  :min="minDeliveryDate" 
                  required 
                  class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
                >
              </div>
            </div>
          </div>

          <div class="bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-2xl font-semibold mb-4">支払い情報</h2>
            <div class="space-y-4">
              <div>
                <label for="paymentMethod" class="block mb-1">支払い方法</label>
                <select v-model="form.paymentMethod" id="paymentMethod" required class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500">
                  <option value="creditCard">クレジットカード</option>
                  <option value="bankTransfer">銀行振込</option>
                  <option value="cashOnDelivery">代金引換</option>
                </select>
              </div>
              <div v-if="form.paymentMethod === 'creditCard'" class="space-y-4">
                <div>
                  <label for="cardName" class="block mb-1">カード名義人</label>
                  <input v-model="form.cardName" type="text" id="cardName" required class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500">
                </div>
                <div>
                  <label for="cardNumber" class="block mb-1">カード番号（16桁）</label>
                  <input v-model="form.cardNumber" type="text" id="cardNumber" required pattern="\d{16}" maxlength="16" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500">
                </div>
                <div class="flex space-x-4">
                  <div class="w-1/2">
                    <label for="cardExpiry" class="block mb-1">有効期限（MM/YY）</label>
                    <input v-model="form.cardExpiry" type="text" id="cardExpiry" required pattern="\d{2}/\d{2}" maxlength="5" placeholder="MM/YY" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500">
                  </div>
                  <div class="w-1/2">
                    <label for="cardCVV" class="block mb-1">セキュリティコード（CVV）</label>
                    <input v-model="form.cardCVV" type="text" id="cardCVV" required pattern="\d{3}" maxlength="3" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500">
                  </div>
                </div>
              </div>
            </div>
          </div>

          <button type="submit" class="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 transition-colors">
            注文を確定する
          </button>
        </form>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent, reactive, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useCartStore } from '../stores/cart'
import { useOrderStore } from '../stores/order'

export default defineComponent({
  name: 'Checkout',
  setup() {
    const router = useRouter()
    const cartStore = useCartStore()
    const orderStore = useOrderStore()

    const form = reactive({
      name: '',
      phone: '',
      email: '',
      postalCode: '',
      address: '',
      deliveryDate: '',
      paymentMethod: 'creditCard',
      cardName: '',
      cardNumber: '',
      cardExpiry: '',
      cardCVV: ''
    })

    const minDeliveryDate = computed(() => {
      const tomorrow = new Date()
      tomorrow.setDate(tomorrow.getDate() + 1)
      return tomorrow.toISOString().split('T')[0]
    })

    const submitOrder = () => {
      // 注文を作成
      const newOrder = {
        id: 'ORD-' + Date.now(),
        date: new Date().toISOString(),
        items: cartStore.items.map(item => ({
          id: item.id,
          name: item.name,
          price: item.price,
          salePrice: item.salePrice,
          quantity: item.quantity
        })),
        total: cartStore.totalPrice + 500, // 送料を含む
        shippingInfo: {
          name: form.name,
          phone: form.phone,
          postalCode: form.postalCode,
          address: form.address,
          email: form.email,
          deliveryDate: form.deliveryDate
        },
        paymentMethod: form.paymentMethod
      }

      // 注文をストアに追加
      orderStore.addOrder(newOrder)

      // カートをクリア
      cartStore.clearCart()

      // 注文完了ページへ遷移
      router.push('/order-complete')
    }

    return {
      cartStore,
      form,
      minDeliveryDate,
      submitOrder
    }
  }
})
</script>