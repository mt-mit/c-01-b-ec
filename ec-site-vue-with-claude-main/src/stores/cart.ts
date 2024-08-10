import { defineStore } from 'pinia'

interface CartItem {
  id: number
  name: string
  price: number
  salePrice?: number
  quantity: number
}

export const useCartStore = defineStore('cart', {
  state: () => ({
    items: [] as CartItem[]
  }),
  getters: {
    totalItems: (state) => state.items.reduce((sum, item) => sum + item.quantity, 0),
    totalPrice: (state) => state.items.reduce((sum, item) => {
      const price = item.salePrice || item.price
      return sum + price * item.quantity
    }, 0)
  },
  actions: {
    addToCart(newItem: CartItem) {
      const existingItem = this.items.find(item => item.id === newItem.id)
      if (existingItem) {
        existingItem.quantity += newItem.quantity
      } else {
        this.items.push(newItem)
      }
    },
    removeFromCart(itemId: number) {
      const index = this.items.findIndex(item => item.id === itemId)
      if (index !== -1) {
        this.items.splice(index, 1)
      }
    },
    updateQuantity(itemId: number, quantity: number) {
      const item = this.items.find(item => item.id === itemId)
      if (item) {
        item.quantity = quantity
      }
    },
    clearCart() {
      this.items = []
    }
  }
})