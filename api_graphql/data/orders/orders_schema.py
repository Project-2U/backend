from graphene import ObjectType
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation

from .mutations import OrderMutation

from .types import OrderType

class Query(ObjectType):
    orders= DjangoFilterConnectionField(OrderType)
    order= relay.Node.Field(OrderType)

class Mutation(ObjectType):
    order= OrderMutation.Field()