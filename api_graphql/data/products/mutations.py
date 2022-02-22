import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation

from orders.forms import OrderProductModelForm
from products.forms import ProductModelForm
from graphene import Field
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
    image = Upload(required=False)
    categories = graphene.List(graphene.ID)
    is_active = graphene.Boolean(default=True)
    id = graphene.ID()


class ProductMutation(graphene.Mutation):
    form = ProductModelForm
    product= graphene.Field(ProductType)

    class Arguments:
       input= ProductInput(required=True)

    success = graphene.Boolean()
    @classmethod
    def mutate(cls,root, info, image=None, **data):

        file_data = dict()
        if image:
            file_data = {"image": image}

        f = ProductMutation.form(data.get('input'), file_data)
        if f.is_valid():
            f.save()
            return ProductMutation(success=True)
        else:
            return ProductMutation(success=False)



class OrderProductMutation(DjangoModelFormMutation):
    order_product = Field(OrderProductType)

    class Meta:
        form_class = OrderProductModelForm
