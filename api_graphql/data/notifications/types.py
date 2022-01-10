from graphene_django import DjangoObjectType
from graphene import relay

from notifications.models import Notification

class NotificationNode(DjangoObjectType):

    class Meta:
        model=Notification
        filter_fields=['user','order','not_date']
        interfaces=[relay.Node]