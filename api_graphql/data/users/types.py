from graphene_django import DjangoObjectType
from graphene import relay

from users.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            'user_name': ['exact', 'contains', 'istartswith'],
            'id': ['exact'],
            'user_lastname': ['exact', 'contains', 'istartswith']
        }
        interfaces = [relay.Node]
