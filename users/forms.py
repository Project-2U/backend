from django import forms

from profiles.forms import UserProfileModelForm
from profiles.models import UserProfile
from .models import User


class UserModelForm(forms.ModelForm):
    name = forms.CharField(min_length=2, max_length=30)
    lastname = forms.CharField(min_length=2, max_length=30)
    age = forms.IntegerField(max_value=99, min_value=15, required=False)
    phone = forms.CharField(min_length=10, max_length=10, required=False)
    address = forms.CharField(min_length=8, max_length=64, required=False)
    occupation = forms.CharField(min_length=3, max_length=64, required=False)

    class Meta:
        model = User
        fields = '__all__'
        exclude = ['create_at', 'update_at']

    def clean_name(self):
        return self.cleaned_data['name'].title()

    def clean_lastname(self):
        return self.cleaned_data['lastname'].title()

    def clean_occupation(self):
        return self.cleaned_data['occupation'].capitalize()
