from django.forms import ModelForm

from .models import Notification

class NotificationModelForm(ModelForm):

    class Meta:
        model= Notification
        fields='__all__'