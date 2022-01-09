from graphene import ObjectType
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation

from .types import NotificationNode

from .mutations import NotificationMutation

class Query(ObjectType):
    
    notifications= DjangoFilterConnectionField(NotificationNode)
    notidication= relay.Node.Field(NotificationNode)

class Mutation(ObjectType):

    notification= NotificationMutation.Field()