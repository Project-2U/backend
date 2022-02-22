from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from django import forms

from .models import UserProfile


class UserProfileModelForm(forms.ModelForm):

    #password2 = forms.PasswordInput(label="Confirmar contraseña", required=False)

    class Meta:
        model = UserProfile
        fields='__all__'

class UserCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'password']


class UserChangeForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'password']
