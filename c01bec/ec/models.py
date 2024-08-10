from django.db import models

# Create your models here.
# # products table 商品ID、商品名、価格
# class Products(models.Model):
#     product_id = models.AutoField(primary_key=True)
#     product_name = models.CharField(max_length=100)
#     price = models.IntegerField()

#     def __str__(self):
#         return self.product_name

# products table 商品ID、商品名、価格(円からドルに変換する)
class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.product_name

    # 円からドルに変換するメソッド
    def yen_to_dollar(self):
        return self.price / 150

# orders table 注文ID、注文日時
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField()

    def __str__(self):
        return self.order_id

# order_details table 注文詳細ID、注文ID、商品ID、数量
class OrderDetails(models.Model):
    order_detail_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.order_detail_id

# cart table カートID、商品ID、数量
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.cart_id
