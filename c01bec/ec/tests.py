from django.test import TestCase

# Create your tests here.
# test products table
from .models import Products
class ProductsTestCase(TestCase):
    def setUp(self):
        Products.objects.create(product_name="test_product", price=1000)
    def test_products(self):
        test_product = Products.objects.get(product_name="test_product")
        self.assertEqual(test_product.product_name, "test_product")
        self.assertEqual(test_product.price, 1000)
        # 円からドルに変換するメソッドのテスト
        self.assertEqual(test_product.yen_to_dollar(), 1000/150)


# test orders table
from .models import Orders
class OrdersTestCase(TestCase):
    def setUp(self):
        Orders.objects.create(order_date="2021-01-01 00:00:00")
    def test_orders(self):
        test_order = Orders.objects.get(order_date="2021-01-01 00:00:00")
        self.assertEqual(test_order.order_date, "2021-01-01 00:00:00")

# test order_details table
from .models import OrderDetails
class OrderDetailsTestCase(TestCase):
    def setUp(self):
        order = Orders.objects.create(order_date="2021-01-01 00:00:00")
        product = Products.objects.create(product_name="test_product", price=1000)
        OrderDetails.objects.create(order_id=order, product_id=product, quantity=10)
    def test_order_details(self):
        test_order_details = OrderDetails.objects.get(quantity=10)
        self.assertEqual(test_order_details.quantity, 10)
        self.assertEqual(test_order_details.product_id.product_name, "test_product")
        self.assertEqual(test_order_details.order_id.order_date, "2021-01-01 00:00:00")

# test cart table
from .models import Cart
class CartTestCase(TestCase):
    def setUp(self):
        product = Products.objects.create(product_name="test_product", price=1000)
        Cart.objects.create(product_id=product, quantity=10)
    def test_cart(self):
        test_cart = Cart.objects.get(quantity=10)
        self.assertEqual(test_cart.quantity, 10)
        self.assertEqual(test_cart.product_id.product_name, "test_product")
        

