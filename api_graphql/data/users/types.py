from graphene_django import DjangoObjectType
from graphene import relay

from users.models import UserModel

class UserType(DjangoObjectType):
    class Meta:
        model= UserModel
        filter_fields={
            'user_name':['exact', 'contains', 'istartswith'],
            'id':['exact'],
            'user_lastname':['exact','contains', 'istartswith']
        }
        interfaces=[relay.Node]