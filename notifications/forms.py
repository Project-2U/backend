from django import forms

from .models import Notification


class NotificationModelForm(forms.ModelForm):
    title = forms.CharField(max_length=64, min_length=5)
    body = forms.CharField(max_length=256, min_length=5, required=False)

    class Meta:
        model = Notification
        fields = '__all__'
