from graphene_django import DjangoObjectType
from graphene import relay
from orders.models import Order as OrderModel
class OrderType(DjangoObjectType):
    class Meta:
        model=OrderModel
        filter_fields=[
            'ord_state',
            'ord_total',
            'user' ]
        interfaces= [relay.Node]