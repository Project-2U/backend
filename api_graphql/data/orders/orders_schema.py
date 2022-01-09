from graphene import ObjectType
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation

#from .mutations import OrderMutation

from .types import OrderNode

class Query(ObjectType):
    orders= DjangoFilterConnectionField(OrderNode)
    order= relay.Node.Field(OrderNode)

# class Mutation(ObjectType):
#     order= OrderMutation.Field()