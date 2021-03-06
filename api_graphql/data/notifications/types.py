from graphene_django import DjangoObjectType
from graphene import relay

from notifications.models import Notification


class NotificationType(DjangoObjectType):
    class Meta:
        model = Notification
        filter_fields = ['user', 'order', 'date']
        interfaces = [relay.Node]
