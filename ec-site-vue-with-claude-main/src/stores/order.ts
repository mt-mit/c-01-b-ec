import { defineStore } from 'pinia'

interface OrderItem {
  id: number
  name: string
  price: number
  salePrice?: number
  quantity: number
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
  id: string
  date: string
  items: OrderItem[]
  total: number
  shippingInfo: ShippingInfo;
  paymentMethod: string;
}

export const useOrderStore = defineStore('order', {
  state: () => ({
    orders: [] as Order[]
  }),
  getters: {
    latestOrder: (state) => state.orders[state.orders.length - 1] || null
  },
  actions: {
    addOrder(order: Order) {
      this.orders.push(order)
    }
  }
})