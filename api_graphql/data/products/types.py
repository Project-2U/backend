from graphene_django import DjangoObjectType
from graphene import relay
from products.models import Product as ProductModel
from orders.models import OrderProduct as OrderProductModel


class ProductType(DjangoObjectType):
    class Meta:
        model = ProductModel
        filter_fields = {
            'name': ['exact', 'contains', 'istartswith'],
            'is_active': ['exact'],
            'categories': ['exact'],
            'price':['exact','contains' ],
            'discount': ['exact']
        }
        interfaces = [relay.Node]


class OrderProductType(DjangoObjectType):
    class Meta:
        model = OrderProductModel
        filter_fields = ['prod_id', 'order_id', 'quantity']
        interfaces = [relay.Node]
