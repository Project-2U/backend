from django import forms

from categories.models import Category
from products.models import Product


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
