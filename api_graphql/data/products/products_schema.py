from graphene import relay , ObjectType
from graphene_django import DjangoConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation

from .types import ProductType
from .mutations import ProductMutation

class Query(ObjectType):
    products= DjangoConnectionField(ProductType)
    product = relay.Node.Field(ProductType)

class Mutation(ObjectType):
    product=ProductMutation.Field()