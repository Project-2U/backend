from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation

from .mutations import OrderProductMutation

from .types import OrderProductType


class Query(ObjectType):
    orders_products = DjangoFilterConnectionField(OrderProductType)
    order_product = relay.Node.Field(OrderProductType)


class Mutation(ObjectType):
    mutate_order_product = OrderProductMutation.Field()
