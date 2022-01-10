from graphene_django.forms.mutation import DjangoModelFormMutation

from orders.forms import OrderModelForm

class OrderMutation(DjangoModelFormMutation):

    class Meta:
        form_class= OrderModelForm
        