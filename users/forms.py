from django import forms

from profiles.forms import UserProfileModelForm
from .models import User


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['create_at', 'update_at']

