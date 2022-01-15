from django.forms import ModelForm
from .models import UserModel

class UserModelForm(ModelForm):
    class Meta:
        model= UserModel
        fields='__all__'
        exclude=['create_at', 'update_at']