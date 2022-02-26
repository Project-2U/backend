import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation

from orders.forms import OrderProductModelForm
from products.forms import ProductModelForm, ProductImageModelForm
from graphene import Field

from products.models import Product, ProductImage
from .types import ProductType, OrderProductType, ProductImageType
from graphene_file_upload.scalars import Upload


class ProductImageInput(graphene.InputObjectType):
    image = Upload(required =True)
    product = graphene.ID(required= True)
    id = graphene.ID()


class ProductImageMutation(graphene.Mutation):
    form = ProductImageModelForm
    product_image = graphene.Field(ProductType)

    class Arguments:
        input = ProductImageInput(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    @classmethod
    def mutate(cls, root, info, **data_input):

        data = data_input.get('input')
        file_data = {"image": data.get('image')}
        if data.get('id'):
            product_image = ProductImage.objects.get(pk=data.get('id'))
            form = ProductImageMutation.form(data, instance=product_image)
        else:
            form = ProductImageMutation.form(data_input.get('input'), file_data)
        if form.is_valid():
            form.save()
            return ProductImageMutation(success=True)
        else:
            return ProductImageMutation(success=False, errors=form.errors)


class OrderProductMutation(DjangoModelFormMutation):
    order_product = Field(OrderProductType)

    class Meta:
        form_class = OrderProductModelForm


class ProductMutation(DjangoModelFormMutation):
    product = Field(ProductType)

    class Meta:
        form_class = ProductModelForm
