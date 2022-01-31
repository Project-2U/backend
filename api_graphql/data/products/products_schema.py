from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation

from .types import ProductType
from .mutations import ProductMutation


class Query(ObjectType):
    products = DjangoFilterConnectionField(ProductType)
    product = relay.Node.Field(ProductType)


class Mutation(ObjectType):
    mutate_product = ProductMutation.Field()
