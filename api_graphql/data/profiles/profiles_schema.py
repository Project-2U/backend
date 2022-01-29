from graphene import ObjectType, relay
from graphene_django import DjangoConnectionField

from .mutations import ProfileMutation

from .types import ProfileType


class Query(ObjectType):
    profiles = DjangoConnectionField(ProfileType)
    profile = relay.Node.Field(ProfileType)


class Mutation(ObjectType):
    mutate_profile = ProfileMutation.Field()
