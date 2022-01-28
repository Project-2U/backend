from django import forms

from categories.models import Category
from .models import Product
from orders.models import OrderProduct


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'toppings' list should be empty)
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            initial['categories'] = [c.pk for c in kwargs['instance'].categorias.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

        def save(self):
            instance = forms.ModelForm.save(self)
            instance.topping_set.clear()
            instance.topping_set.add(*self.cleaned_data['categorias'])
            return instance


class OrderProductModelForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = '__all__'
