from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User


# Create your models here.

class Order(models.Model):
    class State(models.TextChoices):
        CONFIRMED = 'CONFIRMED', _('confirmado')
        UNCONFIRMED = 'UNCONFIRMED', _('confirmado')
        CANCELLED = 'CANCELLED', _('cancelado')
        DISPATCHED = 'DISPATCHED', _('despachado')
        DELIVERED = 'DELIVERED', _('entregado')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('usuario'))
    ord_state = models.CharField(_('estado'), choices=State.choices, max_length=15)
    ord_total = models.IntegerField(_('total'))

    class Meta:
        verbose_name = _('pedido')
        verbose_name_plural = _('pedidos')

    def __str__(self):
        return f"{self.id}"
