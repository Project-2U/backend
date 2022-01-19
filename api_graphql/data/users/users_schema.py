from graphene import ObjectType, relay
from graphene_django import DjangoConnectionField

from .mutations import UserMutation

from .types import UserType


class Query(ObjectType):
    users = DjangoConnectionField(UserType)
    user = relay.Node.Field(UserType)


class Mutation(ObjectType):
    user = UserMutation.Field()
