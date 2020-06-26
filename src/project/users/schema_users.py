import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

class UserType(DjangoObjectType):
	class Meta:
		model = get_user_model()

class CreateUser(graphene.Mutation):
	user = graphene.Field(UserType)

	class Arguments:
		username = graphene.String(required=True)
		password = graphene.String(required=True)
		email = graphene.String(required=True)
		firstName = graphene.String(required=True)
		lastName = graphene.String(required=True)
		
	def mutate(self, info, username: str, password: str, email: str, firstName: str, lastName: str):
		
		user = get_user_model()(
			username = username,
			email = email,
			first_name = firstName,
			last_name = lastName
		)
		user.set_password(password)

		user.save()

		return CreateUser(user=user)

class Mutation(graphene.ObjectType):
	create_user = CreateUser.Field()


class Query(graphene.ObjectType):
	login = graphene.Field(UserType, username = graphene.String(), password = graphene.String())
	users = graphene.List(UserType)

	def resolve_users(self, info):
		return get_user_model().objects.all()

	def resolve_login(self, info, username, password, **kwargs):
		auth_user = authenticate(username = username, password = password)

		if auth_user == None:
			raise Exception('Invalid Credentials')

		return user

schema = graphene.Schema(query=Query, mutation=Mutation)