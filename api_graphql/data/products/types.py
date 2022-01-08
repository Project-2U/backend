from graphene_django import DjangoObjectType
from graphene import relay
from products.models import Product as ProductModel, OrderProduct as OrderProductModel

class ProductNode(DjangoObjectType):
    class Meta:
        model= ProductModel
        filter_fields={
            'prod_name': ['exact', 'contains', 'istartswith'], 
            'is_active':['exact']
            }
        interfaces=[relay.Node]

class OrderProductNode(DjangoObjectType):
    class Meta:
        model= OrderProductModel
        filter_fields=[ 'prod_id','order_id','quantity'] 
        interfaces=[relay.Node]