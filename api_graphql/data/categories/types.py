from graphene_django import DjangoObjectType
from graphene import relay

from categories.models import Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = {'name': ['exact'],
                         'create_at':['exact'],
                        'update_at': ['exact'],
                         'products': ['exact']}
        interfaces = [relay.Node]
