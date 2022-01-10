from graphene_django import DjangoObjectType
from graphene import relay
from orders.models import Order as OrderModel
class OrderNode(DjangoObjectType):
    class Meta:
        model=OrderModel
        filter_fields={
            'ord_state':['exact',],
            'ord_total':['exact'],
            'user':['exact']
        }
        interfaces= [relay.Node]