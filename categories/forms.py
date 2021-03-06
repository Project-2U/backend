from django import forms

from categories.models import Category
from products.models import Product


class CategoryModelForm(forms.ModelForm):
    name = forms.CharField(min_length=3, max_length=30)
    description = forms.CharField(min_length=10, required=False)
    #categories = forms.ModelMultipleChoiceField(label="Categorias", queryset=Category.objects.all(), required=False)

    class Meta:
        model = Category
        fields = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].capitalize()

    def clean_description(self):
        return self.cleaned_data['description'].capitalize()