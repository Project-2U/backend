from graphene_django.forms.mutation import DjangoModelFormMutation
from notifications.forms import NotificationModelForm

class NotificationMutation(DjangoModelFormMutation):

    class Meta:
        form_class= NotificationModelForm
        