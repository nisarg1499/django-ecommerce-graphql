import graphene

import ecommerce.schema
import users.schema_users

class Query(ecommerce.schema.Query,
	users.schema_users.Query,
	graphene.ObjectType):
	pass

class Mutation(users.schema_users.Mutation, 
	graphene.ObjectType):
	pass

schema = graphene.Schema(query=Query, mutation=Mutation)