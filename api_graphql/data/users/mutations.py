from graphene_django.forms.mutation import DjangoModelFormMutation
from users.forms import UserModelForm
from .types import UserType
from graphene import Field


class UserMutation(DjangoModelFormMutation):
    user = Field(UserType)

    class Meta:
        form_class = UserModelForm
