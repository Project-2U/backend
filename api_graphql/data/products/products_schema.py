from graphene import relay , ObjectType
from graphene_django import DjangoConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation

from .types import ProductNode
from .mutations import ProductMutation

class Query(ObjectType):
    products= DjangoConnectionField(ProductNode)
    product = relay.Node.Field(ProductNode)

class Mutation(ObjectType):
    product=ProductMutation.Field()