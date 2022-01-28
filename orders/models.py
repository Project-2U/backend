from django.db import models
from django.utils.translation import gettext_lazy as _

from products.models import Product
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
    state = models.CharField(_('estado'), choices=State.choices, max_length=15, db_column="ord_state")
    total = models.IntegerField(_('total'), db_column="ord_total")
    products = models.ManyToManyField(Product, through="OrderProduct")

    class Meta:
        verbose_name = _('pedido')
        verbose_name_plural = _('pedidos')

    def __str__(self):
        return f"{self.id}"


class OrderProduct(models.Model):
    quantity = models.IntegerField(_('cantidad'))
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('producto'))
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_('pedido'))

    class Meta:
        verbose_name = _('producto/pedido')
        verbose_name_plural = _('productos/pedidos')
