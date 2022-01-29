from graphene_django.forms.mutation import DjangoModelFormMutation

from products.forms import ProductModelForm, OrderProductModelForm
from graphene import Field
from .types import ProductType, OrderProductType


class ProductMutation(DjangoModelFormMutation):
    product = Field(ProductType)

    class Meta:
        form_class = ProductModelForm


class OrderProductMutation(DjangoModelFormMutation):
    order_product = Field(OrderProductType)

    class Meta:
        form_class = OrderProductModelForm
