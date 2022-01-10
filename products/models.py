from django.db import models
from django.utils.translation import gettext_lazy as _

from orders.models import Order

# Create your models here.


class Product (models.Model):

    prod_name=models.CharField(_('nombre'), max_length=254)
    prod_amount= models.IntegerField(_('cantidad'))
    prod_price= models.IntegerField(_('precio'))
    prod_description=models.CharField(_('descripción'), max_length=254, blank=True)
    prod_image= models.ImageField(_('imagen'),upload_to='media/products/',null=True, blank=True)
    prod_trademark=models.CharField(_('marca'), max_length=64,null=True, blank=True)
    prod_warranty= models.CharField(_('garantía'), max_length=20,null=True, blank=True)
    prod_tutorial_url=models.URLField(_('link del tutorial'), null=True, blank=True)
    prod_discount=models.IntegerField(_('descuento'), null=True, blank=True, default=0)
    create_at =models.DateTimeField(_('fecha de creación'), auto_now_add=True)
    update_at= models.DateTimeField(_('fecha de modificación'), auto_now=True)
    is_active= models.BooleanField(_('activo'),default=True)

    class Meta:
        verbose_name=_('productos')
        verbose_name_plural=_('productos')

    def __str__(self):
        return 'producto: '+self.prod_name
    


    class Meta:
        verbose_name=_('productos')
        verbose_name_plural=_('productos')


class OrderProduct(models.Model):

    quantity= models.IntegerField(_('cantidad'))
    prod_id= models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('producto'))
    order_id=models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_('pedido'))

    class Meta:
        verbose_name=_('producto/pedido')
        verbose_name_plural=_('productos/pedidos')