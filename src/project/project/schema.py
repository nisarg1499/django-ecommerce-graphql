import graphene

import ecommerce.schema

class Query(ecommerce.schema.Query, graphene.ObjectType):
	pass

schema = graphene.Schema(query=Query)