from graphene_django.forms.mutation import DjangoModelFormMutation
import graphene

from orders.forms import OrderModelForm
from .types import OrderType
class OrderMutation(DjangoModelFormMutation):

    order=graphene.Field(OrderType)
    class Meta:
        form_class = OrderModelForm
        