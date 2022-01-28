from django.db import models

from django.utils.translation import gettext_lazy as _
from users.models import User
from orders.models import Order


# Create your models here.

class Notification(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True, db_column="noti_date")
    title = models.CharField(_('titulo'), max_length=25, null=True, blank=True, db_column="noti_title")
    body = models.CharField(_('texto'), max_length=254, null=True, blank=True, db_column="noti_body")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('usuario'))
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_('pedido'))

    class Meta:
        verbose_name = _('notificacion')
        verbose_name_plural = _('notificaciones')

    def __str__(self):
        return self.not_title + ' \n ' + self.not_body
