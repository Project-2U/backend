import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation

from orders.forms import OrderProductModelForm
from products.forms import ProductModelForm
from graphene import Field

from products.models import Product
from .types import ProductType, OrderProductType
from graphene_file_upload.scalars import Upload


class ProductInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    amount = graphene.Int(required=True)
    price = graphene.Int(required=True)
    description = graphene.String()
    trademark = graphene.String()
    warranty = graphene.String()
    tutorial_url = graphene.String()
    discount = graphene.Int()
    reference = graphene.String()
    image = graphene.List(Upload)
    categories = graphene.List(graphene.ID)
    is_active = graphene.Boolean(default=True)
    id = graphene.ID()


class ProductMutation(graphene.Mutation):
    form = ProductModelForm
    product = graphene.Field(ProductType)

    class Arguments:
        input = ProductInput(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    @classmethod
    def mutate(cls, root, info, **data_input):

        data = data_input.get('input')
        file_data = dict()
        if data.get('image'):
            file_data = {"image": data.get('image')}
        if data.get('id'):
            product = Product.objects.get(pk=data.get('id'))
            form = ProductMutation.form(data, instance=product)
        else:
            form = ProductMutation.form(data_input.get('input'), file_data)
        if form.is_valid():
            form.save()
            return ProductMutation(success=True)
        else:
            return ProductMutation(success=False, errors=form.errors)


class OrderProductMutation(DjangoModelFormMutation):
    order_product = Field(OrderProductType)

    class Meta:
        form_class = OrderProductModelForm
