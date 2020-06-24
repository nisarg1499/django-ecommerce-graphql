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

class AddProduct(graphene.Mutation):
	addProduct = graphene.Field(ProductType)

	class Arguments:
		productName = graphene.String(required=True)
		productCategory = graphene.String(required=True)
		productPrice = graphene.Float(required=True)
		productDiscountPrice = graphene.Float()
		productPreviewDesc = graphene.String()
		productFullDesc = graphene.String(required=True)

	def mutate(self, info, productName, productCategory, productPrice, productDiscountPrice, productPreviewDesc, productFullDesc, **kwargs):
		productDiscountPrice = kwargs.get('productDiscountPrice', None)
		productPreviewDesc = kwargs.get('productPreviewDesc', None)

		product = Product(productName=productName,
					productCategory=productCategory,
					productPrice=productPrice,
					productDiscountPrice=productDiscountPrice,
					productPreviewDesc=productPreviewDesc,
					productFullDesc=productFullDesc)

		product.save()

		return AddProduct(addProduct=product)

class Mutation(graphene.ObjectType):
	add_product = AddProduct.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
