from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation

from .types import ProductType, ProductImageType
from .mutations import ProductMutation, ProductImageMutation


class Query(ObjectType):
    products = DjangoFilterConnectionField(ProductType)
    product = relay.Node.Field(ProductType)

    productImage = relay.Node.Field(ProductImageType)
    productImages = DjangoFilterConnectionField(ProductImageType)


class Mutation(ObjectType):
    mutate_product = ProductMutation.Field()
    mutate_product_image = ProductImageMutation.Field()
