from django import forms

from .models import Order, OrderProduct


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ["date"]


class OrderProductModelForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1)

    class Meta:
        model = OrderProduct
        fields = '__all__'
