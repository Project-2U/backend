from graphene import relay, ObjectType
from graphene_django import DjangoConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation

from .mutations import OrderProductMutation

from .types import OrderProductNode

class Query(ObjectType):
    orders_products= DjangoConnectionField(OrderProductNode)
    order_product = relay.Node.Field(OrderProductNode)

class Mutation (ObjectType):

    order_product= OrderProductMutation.Field()