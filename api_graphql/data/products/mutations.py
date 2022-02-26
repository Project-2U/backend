import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation

from orders.forms import OrderProductModelForm
from products.forms import ProductModelForm, ProductImageModelForm
from graphene import Field

from products.models import Product, ProductImage
from .types import ProductType, OrderProductType, ProductImageType
from graphene_file_upload.scalars import Upload


class ProductImageInput(graphene.InputObjectType):
    image = Upload(required=True)
    product = graphene.ID(required=True)
    id = graphene.ID()


class ProductImageMutation(graphene.Mutation):
    form = ProductImageModelForm
    product_image = graphene.Field(ProductImageType)

    class Arguments:
        input = ProductImageInput(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    @classmethod
    def mutate(cls, root, info, **data_input):

        data = data_input.get('input')
        file_data = {"path_image": data.get('image')}
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


class DeleteProduct(graphene.Mutation):
    product = Field(ProductType)
    success = graphene.Boolean()
    errors = graphene.JSONString()

    class Input:
        prod_id = graphene.ID(required=True)

    def mutate(root, info, **args):
        prod_id = args.get('prod_id')
        try:
            obj = ProductImage.objects.get(pk=prod_id)
        except Exception:
            return DeleteProduct(success=False, errors={"error": "No existe el elemento con el id proporcionado."})
        if obj:
            obj.delete()
            return DeleteProduct(success=True)
        return DeleteProduct(success=False, errors={"error": "Error al acceder a la base de datos"})


class DeleteProductImage(graphene.Mutation):
    product = Field(ProductImageType)
    success = graphene.Boolean()
    errors = graphene.JSONString()

    class Input:
        prod_image_id = graphene.ID(required=True)

    def mutate(root, info, **args):
        prod_image_id = args.get('prod_image_id')
        try:
            obj = Product.objects.get(pk=prod_image_id)
        except Exception:
            return DeleteProduct(success=False, errors={"error": "No existe el elemento con el id proporcionado."})
        if obj:
            obj.delete()
            return DeleteProduct(success=True)
        return DeleteProduct(success=False, errors={"error": "Error al acceder a la base de datos"})
