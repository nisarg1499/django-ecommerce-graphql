from django.db import models
from django.conf import settings

class Product(models.Model):
	productId = models.AutoField(primary_key=True)
	productName = models.CharField(max_length=100)
	productCategory = models.TextField()
	productPrice = models.FloatField()
	productDiscountPrice = models.FloatField(blank=True, null=True)
	productPreviewDesc = models.CharField(max_length=200, null=True)
	productFullDesc = models.CharField(max_length=400, null=True)

class OrderProduct(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	orderItem = models.ForeignKey(Product, on_delete=models.CASCADE)
	orderQuantity = models.IntegerField(default = 1)

