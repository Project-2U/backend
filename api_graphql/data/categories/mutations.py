from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene import Field
from categories.forms import CategoryModelForm
from .types import CategoryType


class CategoryMutation(DjangoModelFormMutation):
    category = Field(CategoryType)

    class Meta:
        form_class = CategoryModelForm
