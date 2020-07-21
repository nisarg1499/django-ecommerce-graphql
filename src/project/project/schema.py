import graphene
import graphql_jwt

import ecommerce.schema
import users.schema_users


class Query(ecommerce.schema.Query, users.schema_users.Query, graphene.ObjectType):
    pass


class Mutation(
    ecommerce.schema.Mutation, users.schema_users.Mutation, graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
