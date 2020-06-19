from django.db import models

# Create your models here.

class Product(models.Model):
	productId = models.AutoField(primary_key=True)
	productName = models.CharField(max_length=100)
	productCategory = models.TextField()
	productPrice = models.FloatField()
	productPreviewDesc = models.CharField(max_length=200, null=True)
	productFullDesc = models.CharField(max_length=400, null=True)	

