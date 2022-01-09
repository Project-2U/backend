from django.forms import ModelForm

from .models import Product, OrderProduct

class ProductModelForm(ModelForm):
    class Meta:
        model= Product
        fields= '__all__'

class OrderProductModelForm(ModelForm):
    class Meta:
        model=OrderProduct
        fields= '__all__'