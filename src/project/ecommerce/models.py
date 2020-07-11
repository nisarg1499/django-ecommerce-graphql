from django.db import models
from django.conf import settings

class Product(models.Model):
	product_id = models.AutoField(primary_key=True)
	product_name = models.CharField(max_length=100)
	product_category = models.TextField()
	product_price = models.FloatField()
	product_discount_price = models.FloatField(blank=True, null=True)
	product_preview_desc = models.CharField(max_length=200, null=True)
	product_full_desc = models.CharField(max_length=400, null=True)

class OrderProduct(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	order_item = models.ForeignKey(Product, on_delete=models.CASCADE)
	order_quantity = models.IntegerField(default = 1)

class Categories(models.Model):
	category_name = models.CharField(max_length=50)
	category_description = models.TextField(null=True)

class Orders(models.Model):
	order_no = models.AutoField(primary_key=True)
	username = models.TextField()
	order_product = models.ForeignKey(OrderProduct, on_delete=models.CASCADE)


