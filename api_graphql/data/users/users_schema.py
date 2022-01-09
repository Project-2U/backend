from graphene import  ObjectType, relay
from graphene_django import DjangoConnectionField

#from .mutations import UserMutation

from .types import UserNode

class Query(ObjectType):
    users= DjangoConnectionField(UserNode)
    user= relay.Node.Field(UserNode)

# class Mutation(ObjectType):
#     user=UserMutation.Field()