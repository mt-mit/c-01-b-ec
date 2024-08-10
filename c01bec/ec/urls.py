from django.urls import path
from django.urls.conf import include
from django.contrib.auth.models import User
from ec.models import Cart, OrderDetails, Orders, Products
from rest_framework import routers, serializers, viewsets

from . import views

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ここからコメントで自動生成
# ProductsSerializer
class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ['product_id', 'product_name', 'price'] # 手作業で修正...
# ProductsViewSet
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

# CartSerializer
class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['cart_id', 'product_id', 'quantity']
# CartViewSet
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# OrderDetailsSerializer
class OrderDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderDetails
        fields = ['order_detail_id', 'order_id', 'product_id', 'quantity']
# OrderDetailsViewSet
class OrderDetailsViewSet(viewsets.ModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer

# OrderSerializer
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = ['order_id', 'order_date']
# OrderViewSet
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductsViewSet) # 自動生成行
router.register(r'carts', CartViewSet) # 自動生成行
router.register(r'orderdetails', OrderDetailsViewSet) # 自動生成行
router.register(r'orders', OrderViewSet) # 自動生成行


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
