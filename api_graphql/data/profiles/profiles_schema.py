from graphene import ObjectType, relay
from graphene_django.filter import DjangoFilterConnectionField

from .mutations import ProfileMutation

from .types import ProfileType


class Query(ObjectType):
    profiles = DjangoFilterConnectionField(ProfileType)
    profile = relay.Node.Field(ProfileType)


class Mutation(ObjectType):
    mutate_profile = ProfileMutation.Field()
