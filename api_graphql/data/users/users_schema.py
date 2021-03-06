from graphene import ObjectType, relay, AbstractType
from graphene_django.filter import DjangoFilterConnectionField
from .mutations import UserMutation, EditUserMutation

from .types import UserType


class Query(ObjectType):
    users = DjangoFilterConnectionField(UserType)
    user = relay.Node.Field(UserType)


class Mutation(ObjectType):
    mutate_user = UserMutation.Field()
    edit_user =  EditUserMutation.Field()
