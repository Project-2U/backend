from graphene import ObjectType, String , Schema
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from .data.products import types
from .data.users.types import UserNode
from .data.orders.types import OrderNode
from .data.notifications.types import NotificationNode

class Query(ObjectType):    

    products= DjangoFilterConnectionField(types.ProductNode)
    product= relay.Node.Field(types.ProductNode)

    orders_products= DjangoFilterConnectionField(types.OrderProductNode)
    order_produc=relay.Node.Field(types.OrderProductNode)

    users= DjangoFilterConnectionField(UserNode)
    user= relay.Node.Field(UserNode)

    orders= DjangoFilterConnectionField(OrderNode)
    order = relay.Node.Field(OrderNode)

    notifications= DjangoFilterConnectionField(NotificationNode)
    notidication= relay.Node.Field(NotificationNode)

ROOT_SCHEMA= Schema(query=Query)