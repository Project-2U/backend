from graphene import ObjectType, relay, AbstractType
from graphene_django import DjangoConnectionField

from .mutations import UserMutation

from .types import UserType


class Query(ObjectType):
    users = DjangoConnectionField(UserType)
    user = relay.Node.Field(UserType)


class Mutation(ObjectType):
    mutate_user = UserMutation.Field()
