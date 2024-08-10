<template>
  <div class="order-history">
    <h1 class="text-3xl font-bold mb-8">注文履歴</h1>
    <div v-if="sortedOrders.length > 0" class="space-y-8">
      <div v-for="order in sortedOrders" :key="order.id" class="bg-white rounded-lg shadow-md p-6">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-xl font-semibold">注文 #{{ order.id }}</h2>
          <span class="text-gray-600">{{ formatDate(order.date) }}</span>
        </div>
        
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h3 class="text-lg font-semibold mb-2">注文内容</h3>
            <div class="space-y-2">
              <div v-for="item in order.items" :key="item.id" class="flex justify-between">
                <span>{{ item.name }} x {{ item.quantity }}</span>
                <div>
                  <span v-if="item.salePrice !== undefined" class="text-red-600">¥{{ (item.salePrice * item.quantity).toLocaleString() }}</span>
                  <span v-else>¥{{ (item.price * item.quantity).toLocaleString() }}</span>
                </div>
              </div>
            </div>
            <div class="mt-4 pt-4 border-t border-gray-200 space-y-2">
              <div class="flex justify-between items-center">
                <span class="font-semibold">小計</span>
                <span>¥{{ calculateSubtotal(order).toLocaleString() }}</span>
              </div>
              <div class="flex justify-between items-center">
                <span class="font-semibold">送料</span>
                <span>¥500</span>
              </div>
              <div class="flex justify-between items-center text-lg font-bold">
                <span>合計</span>
                <span>¥{{ (calculateSubtotal(order) + 500).toLocaleString() }}</span>
              </div>
            </div>
          </div>

          <div>
            <h3 class="text-lg font-semibold mb-2">配送情報</h3>
            <p><strong>配送先:</strong> {{ order.shippingInfo.name }}</p>
            <!-- <p>{{ order.shippingInfo.postalCode }}</p> -->
            <p>{{ order.shippingInfo.address }}</p>
            <p><strong>配送予定日:</strong> {{ formatDateOnly(order.shippingInfo.deliveryDate) }}</p>
            <h3 class="text-lg font-semibold mt-4 mb-2">支払い情報</h3>
            <p><strong>支払い方法:</strong> {{ formatPaymentMethod(order.paymentMethod) }}</p>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="text-center text-gray-600">
      注文履歴がありません。
    </div>
  </div>
</template>


<script lang="ts">

import { defineComponent, computed } from 'vue'
import { useOrderStore } from '../stores/order'

interface OrderItem {
  id: number;
  name: string;
  price: number;
  salePrice?: number;
  quantity: number;
}

interface ShippingInfo {
  name: string;
  phone: string;
  postalCode: string;
  address: string;
  email: string;
  deliveryDate: string;
}

interface Order {
  id: string;
  date: string;
  items: OrderItem[];
  total: number;
  shippingInfo: ShippingInfo;
  paymentMethod: string;
}

export default defineComponent({
  name: 'OrderHistory',
  setup() {
    const orderStore = useOrderStore()

    const sortedOrders = computed<Order[]>(() => {
      return [...orderStore.orders].sort((a, b) => {
        return new Date(b.date).getTime() - new Date(a.date).getTime()
      })
    })

    const formatDate = (date: string) => {
      return new Date(date).toLocaleString('ja-JP', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      })
    }

    const formatPaymentMethod = (method: string) => {
      switch (method) {
        case 'creditCard':
          return 'クレジットカード';
        case 'bankTransfer':
          return '銀行振込';
        case 'cashOnDelivery':
          return '代金引換';
        default:
          return method;
      }
    }

    const calculateSubtotal = (order: Order) => {
      return order.items.reduce((total, item) => {
        const itemPrice = item.salePrice !== undefined ? item.salePrice : item.price;
        return total + itemPrice * item.quantity;
      }, 0);
    }

    const formatDateOnly = (dateString: string) => {
      return new Date(dateString).toLocaleDateString('ja-JP', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    }
    

    return {
      sortedOrders,
      formatDate,
      formatDateOnly,
      formatPaymentMethod,
      calculateSubtotal
    }
  }
})
</script>