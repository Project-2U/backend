from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Product(models.Model):
    name = models.CharField(_('nombre'), max_length=254, db_column="prod_name")
    amount = models.IntegerField(_('cantidad'), db_column="prod_amount")
    price = models.IntegerField(_('precio'), db_column="prod_price")
    description = models.CharField(_('descripción'), max_length=254, blank=True, db_column="prod_description")
    image = models.ImageField(_('imagen'), upload_to='media/products/', null=True, blank=True, db_column="prod_image")
    trademark = models.CharField(_('marca'), max_length=64, null=True, blank=True, db_column="prod_trademark")
    warranty = models.CharField(_('garantía'), max_length=20, null=True, blank=True, db_column="prod_warranty")
    tutorial_url = models.URLField(_('link del tutorial'), null=True, blank=True, db_column="prod_tutorial")
    discount = models.IntegerField(_('descuento'), null=True, blank=True, default=0, db_column="prod_discount")
    create_at = models.DateTimeField(_('fecha de creación'), auto_now_add=True)
    update_at = models.DateTimeField(_('fecha de modificación'), auto_now=True)
    is_active = models.BooleanField(_('activo'), default=True)



    class Meta:
        verbose_name = _('productos')
        verbose_name_plural = _('productos')

    def __str__(self):
        return 'producto: ' + self.name
