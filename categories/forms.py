from django import forms

from categories.models import Category
from products.models import Product


class CategoryModelForm(forms.ModelForm):
    name = forms.CharField(min_length=3, max_length=30)
    description = forms.CharField(min_length=10, required=False)

    class Meta:
        model = Category
        fields = '__all__'
