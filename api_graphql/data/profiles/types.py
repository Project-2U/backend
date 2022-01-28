from graphene_django import DjangoObjectType
from graphene import relay

from profiles.models import UserProfile


class ProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile
        filter_fields = {'email': ['exact', 'contains', 'isstartswith'],
                         'type': ['exact'],
                         'is_active': ['exact']}
        interfaces = [relay.Node]
