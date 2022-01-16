from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from django import forms

from .models import UserProfile

class UserProfileModelForm(forms.ModelForm):
    class Meta:
        model= UserProfile
        exclude=['password']

class UserCreationForm(UserCreationForm):
    class Meta:
        model=UserProfile
        fields=['user_email',]
      

class UserChangeForm(UserChangeForm):
    class Meta:
        model= UserProfile
        fields=['user_email']
      