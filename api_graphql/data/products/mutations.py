from graphene_django.forms.mutation import DjangoModelFormMutation

from products.forms import ProductModelForm, OrderProductModelForm



class ProductMutation(DjangoModelFormMutation):
    class Meta:
        form_class= ProductModelForm

class OrderProductMutation(DjangoModelFormMutation):
    class Meta:
        form_class= OrderProductModelForm