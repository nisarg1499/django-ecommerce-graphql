import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q
from graphene import ObjectType

from .models import Product

class ProductType(DjangoObjectType):
	class Meta:
		model = Product

class Query(graphene.ObjectType):
	products = graphene.List(ProductType, productName = graphene.String())

	def resolve_products(self, info, productName, **kwargs):
		filter = (Q(productName__icontains = productName))
		return Product.objects.filter(filter)