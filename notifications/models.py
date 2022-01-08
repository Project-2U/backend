from django.db import models

from django.utils.translation import gettext_lazy as _
from users.models import User
from orders.models import Order
# Create your models here.

class Notification(models.Model):
    not_date=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    not_title=models.CharField(_('titulo'), max_length=25, null=True, blank=True)
    not_body=models.CharField(_('texto'), max_length=254, null=True, blank=True)

    user=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= _('usuario'))
    order=models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_('pedido'))
    class Meta:
        verbose_name=_('notificacion')
        verbose_name_plural=_('notificaciones')
    
    def __str__(self):
        return self.not_title +' \n '+ self.not_body