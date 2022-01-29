from graphene_django import DjangoObjectType
from graphene import relay

from categories.models import Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'create_at', 'update_at']
        interfaces = [relay.Node]
