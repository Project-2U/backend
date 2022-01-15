from graphene import ObjectType
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation

from .types import NotificationType

from .mutations import NotificationMutation

class Query(ObjectType):
    
    notifications= DjangoFilterConnectionField(NotificationType)
    notidication= relay.Node.Field(NotificationType)

class Mutation(ObjectType):

    notification= NotificationMutation.Field()