from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene import Field
from notifications.forms import NotificationModelForm
from .types import NotificationType


class NotificationMutation(DjangoModelFormMutation):
    notification = Field(NotificationType)

    class Meta:
        form_class = NotificationModelForm
