import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q
from graphene import ObjectType

from .models import Product

class ProductType(DjangoObjectType):
	class Meta:
		model = Product

class Query(graphene.ObjectType):
	products = graphene.List(ProductType, product_name = graphene.String())

	def resolve_products(self, info, product_name, **kwargs):
		filter = (Q(product_name__icontains = product_name))
		return Product.objects.filter(filter)

class AddProduct(graphene.Mutation):
	addProduct = graphene.Field(ProductType)

	class Arguments:
		product_name = graphene.String(required=True)
		product_category = graphene.String(required=True)
		product_price = graphene.Float(required=True)
		product_discount_price = graphene.Float()
		product_preview_desc = graphene.String()
		product_full_desc = graphene.String(required=True)

	def mutate(self, info, product_name, product_category, product_price, product_discount_price, product_preview_desc, product_full_desc, **kwargs):
		product_discount_price = kwargs.get('product_discount_price', None)
		product_preview_desc = kwargs.get('product_preview_desc', None)

		product = Product(product_name=product_name,
					product_category=product_category,
					product_price=product_price,
					product_discount_price=product_discount_price,
					product_preview_desc=product_preview_desc,
					product_full_desc=product_full_desc)

		product.save()

		return AddProduct(addProduct=product)

class Mutation(graphene.ObjectType):
	add_product = AddProduct.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
