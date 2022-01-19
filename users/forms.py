from django.forms import ModelForm
from .models import User


class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['create_at', 'update_at']
