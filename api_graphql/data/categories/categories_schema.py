from graphene import ObjectType
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation

from .types import CategoryType

from .mutations import CategoryMutation


class Query(ObjectType):
    categories = DjangoFilterConnectionField(CategoryType)
    category = relay.Node.Field(CategoryType)


class Mutation(ObjectType):
    mutate_category = CategoryMutation.Field()