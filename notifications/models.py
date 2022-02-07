from django.db import models

from django.utils.translation import gettext_lazy as _
from users.models import User
from orders.models import Order


# Create your models here.

class Notification(models.Model):
    date = models.DateTimeField(auto_now_add=True, db_column="noti_date")
    title = models.CharField(_('titulo'), max_length=25, db_column="noti_title", default="Notification")
    body = models.CharField(_('texto'), max_length=254, null=True, blank=True, db_column="noti_body")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('usuario'))
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_('pedido'))

    class Meta:
        verbose_name = _('notificacion')
        verbose_name_plural = _('notificaciones')
        ordering = ["-date"]

    def __str__(self):
        return self.title + ' \n ' + self.body
