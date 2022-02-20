from graphene_django import DjangoObjectType
from graphene import relay

from profiles.models import UserProfile


class ProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile
        filter_fields = {
            'email': ['exact', 'icontains', 'istartswith'],
            'password':['exact'],
            'type': ['exact'],
            'is_active': ['exact']}
        exclude = ['is_admin','is_staff', 'is_superuser']
        interfaces = [relay.Node]
