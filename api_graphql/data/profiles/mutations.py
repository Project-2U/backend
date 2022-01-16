from graphene_django.forms.mutation import DjangoModelFormMutation
from profiles.forms import UserProfileModelForm
from .types import ProfileType
from graphene import Field
class ProfileMutation(DjangoModelFormMutation):
    profile= Field(ProfileType)
    class Meta:
        form_class= UserProfileModelForm